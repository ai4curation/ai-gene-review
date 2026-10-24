"""One-off migration of reviewed ND rows to the NO_DATA acceptance rule.

The rule (projects/NO_DATA.md): an ND row is ACCEPT unless literature on this
gene product, in this species, identifies a function in that aspect. This
script applies decisions made by reading each non-ACCEPT ND row's review
reason and the review's other rows in the same aspect (2026-10-24):

- rows in ``STALE`` keep their REMOVE/MODIFY and gain ``nd_case: STALE``;
- every other ND row with action KEEP_AS_NON_CORE, MARK_AS_OVER_ANNOTATED,
  TOO_GENERAL, REMOVE or MODIFY becomes ACCEPT. Its ``nd_case`` is TRUE_GAP if
  the review has a matching BIOLOGY knowledge gap, INFERABLE if a retained
  inferred row covers the aspect, and is left unset otherwise;
- where a converted MODIFY proposed a term the review does not carry elsewhere,
  the term moves to a NEW row with the original reasoning (``NEW_ROWS``).

UNDECIDED and NEW ND rows are left alone. Run from the repository root:
    uv run python projects/NO_DATA/scripts/apply_acceptance_rule.py
"""

from __future__ import annotations

import copy
import io
import re
import textwrap
from pathlib import Path

from ruamel.yaml import YAML

ROOT = Path(__file__).resolve().parents[3]
ROOT_ASPECT = {"GO:0003674": "MF", "GO:0008150": "BP", "GO:0005575": "CC"}
MATCHING_DARK = {
    "MF": {"MF_DARK", "WHOLLY_DARK"},
    "BP": {"BP_DARK", "WHOLLY_DARK"},
    "CC": {"CC_DARK", "WHOLLY_DARK"},
}
CONVERT = {"KEEP_AS_NON_CORE", "MARK_AS_OVER_ANNOTATED", "TOO_GENERAL", "REMOVE", "MODIFY"}
INFERRED = {"IBA", "IBD", "IKR", "IRD", "ISS", "ISO", "ISA", "ISM", "IGC", "RCA", "IEA"}
RETAINED = {"ACCEPT", "KEEP_AS_NON_CORE", "NEW", "MODIFY", "TOO_GENERAL"}

#: (organism/gene, ND root term) whose ND is stale: literature on this gene product
#: in this species identifies a function in the aspect.
STALE = {
    ("ARATH/MLO2", "GO:0003674"), ("ARATH/PLGG1", "GO:0003674"),
    ("ARATH/PGLP1", "GO:0008150"), ("ARATH/Q1G3K8", "GO:0003674"),
    ("DANRE/elna", "GO:0003674"), ("DANRE/elna", "GO:0008150"),
    ("DANRE/elnb", "GO:0003674"), ("DANRE/elnb", "GO:0008150"),
    ("DROME/Tcs6", "GO:0008150"), ("DROME/Tcs6", "GO:0005575"),
    ("DROME/unc79", "GO:0003674"), ("DROME/Kpc1", "GO:0008150"),
    ("DROME/Kpc2", "GO:0008150"), ("DROME/Mo25", "GO:0003674"),
    ("DROME/hbt", "GO:0008150"), ("SCHPO/knh4", "GO:0008150"),
    ("human/AMTN", "GO:0003674"), ("human/ANKRD40", "GO:0003674"),
    ("human/ANKRD40", "GO:0005575"), ("human/ARL15", "GO:0003674"),
    ("human/ARL15", "GO:0008150"), ("human/BBS9", "GO:0003674"),
    ("human/CHCHD10", "GO:0003674"), ("human/HSCB", "GO:0003674"),
    ("human/AARSD1", "GO:0003674"), ("human/AARSD1", "GO:0008150"),
    ("human/CCDC40", "GO:0003674"), ("human/TAT", "GO:0005575"),
    ("mouse/Capsl", "GO:0008150"), ("rat/Aga", "GO:0008150"),
    ("worm/mut-16", "GO:0003674"), ("worm/nlp-29", "GO:0003674"),
    ("yeast/APS1", "GO:0003674"), ("yeast/CAF120", "GO:0008150"),
    ("yeast/DPH1", "GO:0003674"), ("yeast/DPH2", "GO:0003674"),
    ("yeast/MAD2", "GO:0003674"), ("yeast/MAD3", "GO:0003674"),
    ("yeast/MDM10", "GO:0003674"), ("yeast/MNN14", "GO:0003674"),
    ("yeast/MPS3", "GO:0003674"), ("yeast/NIP7", "GO:0003674"),
    ("yeast/SMX2", "GO:0003674"), ("yeast/SMX2", "GO:0008150"),
    ("yeast/TDA5", "GO:0003674"), ("yeast/THI5", "GO:0003674"),
    ("yeast/ZDS2", "GO:0003674"), ("yeast/CRT10", "GO:0005575"),
    ("yeast/SPH1", "GO:0003674"),
}

#: (organism/gene, ND root term) -> (evidence_type, qualifier) for a NEW row carrying
#: the term a converted MODIFY proposed, where the review has no row for it.
NEW_ROWS = {
    ("DROME/CG14662", "GO:0005575"): ("ISM", "located_in"),
    ("DROME/CG31606", "GO:0005575"): ("ISM", "located_in"),
    ("DROME/CG42763", "GO:0005575"): ("ISM", "located_in"),
    ("DROME/Tango5", "GO:0003674"): ("ISS", "enables"),
    ("DROME/Vps50", "GO:0003674"): ("ISS", "contributes_to"),
    ("DROME/Vps51", "GO:0003674"): ("ISS", "contributes_to"),
    ("DROME/Vps53", "GO:0003674"): ("ISS", "contributes_to"),
    ("SCHPO/apc2", "GO:0003674"): ("ISS", "enables"),
    ("SCHPO/vms1", "GO:0003674"): ("ISS", "enables"),
    ("mouse/Sdhaf2__Q8C6I2", "GO:0003674"): ("ISO", "enables"),
    ("mouse/Shld2", "GO:0003674"): ("ISS", "enables"),
}

ACCEPT_REASON = (
    "No literature on this gene product, in this species, identifies a function in "
    "this aspect, so the ND follows the evidence-code guideline and is accepted "
    "(projects/NO_DATA.md). Inferred rows in the same aspect do not make it stale."
)


def gaps(doc) -> list:
    """BIOLOGY knowledge gaps on the gene and its core functions."""
    found = list(doc.get("knowledge_gaps") or [])
    for cf in doc.get("core_functions") or []:
        found += list(cf.get("knowledge_gaps") or [])
    return [g for g in found if "BIOLOGY" in (g.get("gap_kind") or [])]


DROPPED = ("proposed_replacement_terms", "supported_by")


def rewrite_review(
    block: list[str], reason: str | None, nd_case: str | None, aliases: str = ""
):
    """Edit one annotation's text lines in place, leaving all other lines untouched.

    With ``reason`` set: action becomes ACCEPT, the reason is replaced and the
    replacement-term and support sections are dropped, unless they define a YAML
    anchor that ``aliases`` (the file text) refers to elsewhere. ``nd_case`` is added at the
    end of the review. Works for either list indentation used in the repo
    (``- term:`` or ``  - term:``). Returns None if the block has no review.
    """
    ind = block[0].index("-") + 2
    pad, child = " " * ind, " " * (ind + 2)
    key = re.compile(rf"^{child}([a-z_]+):")
    start = next((i for i, line in enumerate(block) if line.startswith(f"{pad}review:")), None)
    if start is None:
        return None
    end = next(
        (i for i in range(start + 1, len(block))
         if block[i].strip() and len(block[i]) - len(block[i].lstrip()) <= ind),
        len(block),
    )
    while end > start + 1 and not block[end - 1].strip():
        end -= 1

    def folded(text: str) -> list[str]:
        return [f"{child}reason: >-\n"] + [
            f"{child}  {w}\n" for w in textwrap.wrap(text, 84 - ind)
        ]

    sections: list[tuple[str, list[str]]] = []
    for line in block[start + 1:end]:
        m = key.match(line)
        if m:
            sections.append((m.group(1), [line]))
        else:
            sections[-1][1].append(line)
    out: list[tuple[str, list[str]]] = []
    for name, body in sections:
        if name == "nd_case":
            continue
        if reason is not None:
            if name in DROPPED:
                anchors = re.findall(r"&(id\d+)", "".join(body))
                if not any(f"*{a}" in aliases for a in anchors):
                    continue
            if name == "action":
                body = [f"{child}action: ACCEPT\n"]
            elif name == "reason":
                body = folded(reason)
        out.append((name, body))
    if reason is not None and not any(n == "reason" for n, _ in out):
        out.append(("reason", folded(reason)))
    if nd_case:
        out.append(("nd_case", [f"{child}nd_case: {nd_case}\n"]))
    return block[:start + 1] + [line for _, body in out for line in body] + block[end:]


def main() -> None:
    from ai_gene_review.validation.action_consistency import go_ancestors

    ancestors = go_ancestors()

    def aspect(term_id: str) -> str | None:
        if term_id in ROOT_ASPECT:
            return ROOT_ASPECT[term_id]
        anc = ancestors(term_id)
        return next((v for k, v in ROOT_ASPECT.items() if k in anc), None)

    yaml = YAML()
    yaml.preserve_quotes = True
    yaml.width = 88
    yaml.indent(mapping=2, sequence=2, offset=0)
    changed, skipped = [], []
    for path in sorted(ROOT.glob("genes/*/*/*-ai-review.yaml")):
        text = path.read_text()
        if "evidence_type: ND" not in text:
            continue
        key = f"{path.parent.parent.name}/{path.parent.name}"
        doc = yaml.load(text)
        anns = doc.get("existing_annotations") or []
        lines = text.splitlines(keepends=True)
        keys = list(doc.keys())
        after = keys[keys.index("existing_annotations") + 1:]
        list_end = doc.lc.key(after[0])[0] if after else len(lines)
        starts = [a.lc.line for a in anns] + [list_end]
        edits: dict[int, list] = {}
        additions = []
        for i, ann in enumerate(anns):
            if ann.get("evidence_type") != "ND":
                continue
            review = ann.get("review") or {}
            action = review.get("action")
            term = ann["term"]["id"]
            asp = ROOT_ASPECT.get(term)
            if action not in CONVERT:
                continue
            if (key, term) in STALE:
                if review.get("nd_case") != "STALE":
                    block = rewrite_review(lines[starts[i]:starts[i + 1]], None, "STALE")
                    if block is None:
                        skipped.append(f"{key} {term}: unexpected layout")
                    else:
                        edits[i] = block
                continue
            new_rows = []
            if (key, term) in NEW_ROWS:
                evidence, qualifier = NEW_ROWS[(key, term)]
                for rep in review.get("proposed_replacement_terms") or []:
                    row = {
                        "term": {"id": rep["id"], "label": rep.get("label")},
                        "evidence_type": evidence,
                        "original_reference_id": (review.get("supported_by") or [{}])[0].get(
                            "reference_id", "GO_REF:0000024"
                        ),
                        "qualifier": qualifier,
                        "review": {
                            "summary": f"Inferred {rep.get('label')}, moved from the ND row "
                            "it was proposed to replace.",
                            "action": "NEW",
                            "reason": str(review.get("reason")),
                        },
                    }
                    if review.get("supported_by"):
                        row["review"]["supported_by"] = copy.deepcopy(
                            list(review["supported_by"])
                        )
                    new_rows.append(row)
            others = [
                b for b in anns
                if b is not ann and b.get("evidence_type") != "ND"
                and (b.get("term") or {}).get("id")
                and aspect(b["term"]["id"]) == asp
            ]
            if any(g.get("dark_aspect") in MATCHING_DARK[asp] for g in gaps(doc)):
                nd_case = "TRUE_GAP"
            elif new_rows or any(
                b.get("evidence_type") in INFERRED
                and (b.get("review") or {}).get("action") in RETAINED
                for b in others
            ):
                nd_case = "INFERABLE"
            else:
                nd_case = None
            old = " ".join(str(review.get("reason") or "no reason given").split())
            reason = f"{ACCEPT_REASON} Earlier action {action}, because: {old}"
            if new_rows:
                reason += " The proposed term now sits on its own NEW row."
            new_block = rewrite_review(
                lines[starts[i]:starts[i + 1]], reason, nd_case, text
            )
            if new_block is None:
                skipped.append(f"{key} {term}: unexpected layout")
                continue
            edits[i] = new_block
            additions.extend(new_rows)
        if not edits and not additions:
            continue
        out = []
        starts_pad = lines[starts[0]].index("-")
        for i in range(len(anns)):
            chunk = lines[starts[i]:starts[i + 1]]
            if i in edits:
                out.append("".join(edits[i]))
            else:
                out.append("".join(chunk))
            if i == len(anns) - 1 and additions:
                buf = io.StringIO()
                yaml.indent(mapping=2, sequence=starts_pad + 2, offset=starts_pad)
                yaml.dump(additions, buf)
                out.append("".join(line.rstrip() + "\n" for line in buf.getvalue().splitlines()))
        text = "".join(lines[:starts[0]]) + "".join(out) + "".join(lines[list_end:])
        path.write_text(text)
        changed.append(key)
    print("\n".join(changed))
    print(f"{len(changed)} files changed")
    print("\n".join(f"SKIPPED {s}" for s in skipped))


if __name__ == "__main__":
    main()
