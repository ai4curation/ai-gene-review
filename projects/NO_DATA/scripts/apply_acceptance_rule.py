"""Apply the NO_DATA acceptance rule to reviewed ND rows from a decision table.

The rule (projects/NO_DATA.md): an ND row is ACCEPT unless literature on this
gene product, in this species, identifies a function in that aspect. The
decisions live in ``projects/NO_DATA/data/nd-decisions.yaml``; they were made
by reading each ND row and the review's other rows in the same aspect, not by
a new literature search, and the generated text says so.

For each decision the script restores the ND row as it was before the pass
(``ORIGINAL_COMMITS``), drops any NEW row an earlier run generated, and then
edits only that row's review block:

- ``STALE``: the earlier REMOVE/MODIFY stays; ``nd_case: STALE`` is added.
- ``ACCEPT``: action becomes ACCEPT, summary and reason are rewritten,
  ``proposed_replacement_terms`` is dropped, and so is ``supported_by`` when
  the earlier action was MODIFY (those quotes supported the replacement term).
  ``nd_case`` is TRUE_GAP when the review has a BIOLOGY gap for the aspect,
  INFERABLE when a retained inferred row or a new row covers it, and is left
  unset otherwise. With ``new_row``, the replacement term becomes its own NEW
  row carrying the earlier quotes.

Run from the repository root, then ``just backfill-record-sections`` on the
changed reviews to restore ``record_section`` on restored UniProt quotes:
    uv run python projects/NO_DATA/scripts/apply_acceptance_rule.py
"""

from __future__ import annotations

import copy
import io
import re
import subprocess
import textwrap
from collections import defaultdict
from pathlib import Path

import yaml
from ruamel.yaml import YAML

ROOT = Path(__file__).resolve().parents[3]
DECISIONS = ROOT / "projects" / "NO_DATA" / "data" / "nd-decisions.yaml"

#: The commit before each pass touched a review: the first pass (2026-10-24)
#: and the follow-up over reviews merged from main (2026-10-26).
ORIGINAL_COMMITS = ("589ca34bd", "d2fa590c5")

ROOT_ASPECT = {"GO:0003674": "MF", "GO:0008150": "BP", "GO:0005575": "CC"}
ASPECT_NAME = {"MF": "molecular function", "BP": "biological process", "CC": "cellular component"}
MATCHING_DARK = {
    "MF": {"MF_DARK", "WHOLLY_DARK"},
    "BP": {"BP_DARK", "WHOLLY_DARK"},
    "CC": {"CC_DARK", "WHOLLY_DARK"},
}
INFERRED = {"IBA", "IBD", "IKR", "IRD", "ISS", "ISO", "ISA", "ISM", "IGC", "RCA", "IEA"}
RETAINED = {"ACCEPT", "KEEP_AS_NON_CORE", "NEW", "MODIFY", "TOO_GENERAL"}
#: Summaries of NEW rows this script generates (current and earlier wording).
GENERATED_NEW_ROW = ("proposed during the NO_DATA re-action pass",
                     "moved from the ND row it was proposed to replace")
ND_CLAUSE = re.compile(r"\bND\b|placeholder|superseded|out of date|outdated|replace", re.I)


def summary_text(aspect: str) -> str:
    return (
        f"Root {ASPECT_NAME[aspect]} ND annotation: when it was made, no "
        f"{ASPECT_NAME[aspect]} had been curated for this gene product from literature."
    )


def reason_text(aspect: str, earlier: str, note: str | None, new_label: str | None) -> str:
    parts = [
        "ACCEPT under the ND acceptance rule (projects/NO_DATA.md). The evidence this "
        f"review cites for the {ASPECT_NAME[aspect]} is inferred (from orthologs, family "
        "membership or sequence features) or comes from other species; none of it is "
        "literature on this gene product in this species. This was judged from the "
        "review's own content during the NO_DATA re-action pass, not from a new "
        f"literature search. Earlier action: {earlier}."
    ]
    if note:
        parts.append(note)
    if new_label:
        parts.append(f"The term the earlier MODIFY proposed, {new_label}, is kept as its own NEW row.")
    return " ".join(parts)


def new_row_reason(label: str, evidence: str, old_reason: str) -> str:
    kept = [
        s for s in re.split(r"(?<=[.!?])\s+", " ".join(old_reason.split()))
        if s and not ND_CLAUSE.search(s)
    ]
    head = (
        f"{label[:1].upper()}{label[1:]} is inferred for this gene product ({evidence}), not shown for it "
        "experimentally; the ND row for the aspect therefore stays (projects/NO_DATA.md)."
    )
    return " ".join([head, *kept])


def folded(key: str, text: str, pad: str) -> list[str]:
    width = 88 - len(pad) - 2
    return [f"{pad}{key}: >-\n"] + [
        f"{pad}  {w}\n" for w in textwrap.wrap(text, width, break_on_hyphens=False)
    ]


def blocks(text: str, rt: YAML) -> tuple[list[str], list[int], list]:
    """Lines, the start line of each annotation plus the list end, and the annotations."""
    doc = rt.load(text)
    anns = doc["existing_annotations"]
    keys = list(doc.keys())
    after = keys[keys.index("existing_annotations") + 1:]
    lines = text.splitlines(keepends=True)
    end = doc.lc.key(after[0])[0] if after else len(lines)
    return lines, [a.lc.line for a in anns] + [end], list(anns)


def rewrite_review(block: list[str], drop: set[str], replace: dict[str, list[str]],
                   nd_case: str | None) -> list[str]:
    """Edit one annotation's review section; all other lines are left untouched."""
    ind = block[0].index("-") + 2
    pad, child = " " * ind, " " * (ind + 2)
    key = re.compile(rf"^{child}([a-z_]+):")
    start = next(i for i, line in enumerate(block) if line.startswith(f"{pad}review:"))
    end = next((i for i in range(start + 1, len(block))
                if block[i].strip() and len(block[i]) - len(block[i].lstrip()) <= ind), len(block))
    while end > start + 1 and not block[end - 1].strip():
        end -= 1
    sections: list[tuple[str, list[str]]] = []
    for line in block[start + 1:end]:
        m = key.match(line)
        if m:
            sections.append((m.group(1), [line]))
        else:
            sections[-1][1].append(line)
    out = []
    for name, body in sections:
        if name in drop or name == "nd_case":
            continue
        out.append(replace.pop(name, body))
    out.extend(replace.values())
    if nd_case:
        out.append([f"{child}nd_case: {nd_case}\n"])
    return block[:start + 1] + [line for body in out for line in body] + block[end:]


def move_dangling_anchors(text: str, original: str) -> str:
    """Re-home anchors defined in dropped sections at their first remaining alias.

    The anchored node is copied from ``original`` and placed, re-indented, where
    the first alias stood, so the rest of the file still resolves.
    """
    defined = set(re.findall(r"&(id\d+)", text))
    dangling = sorted({a for a in re.findall(r"\*(id\d+)", text) if a not in defined})
    lines = text.splitlines(keepends=True)
    o_lines = original.splitlines(keepends=True)
    for anchor in dangling:
        i = next(k for k, ln in enumerate(o_lines) if re.search(rf"- &{anchor}\s*$", ln))
        base = len(o_lines[i]) - len(o_lines[i].lstrip()) + 2
        body = []
        for ln in o_lines[i + 1:]:
            if ln.strip() and len(ln) - len(ln.lstrip()) < base:
                break
            body.append(ln[base:])
        j = next(k for k, ln in enumerate(lines) if re.search(rf"\*{anchor}\s*$", ln))
        ind = len(lines[j]) - len(lines[j].lstrip()) + 2
        lines[j] = lines[j].replace(f"*{anchor}", f"&{anchor}")
        lines[j + 1:j + 1] = [(" " * ind + b) if b.strip() else b for b in body]
    return "".join(lines)


def main() -> None:
    from ai_gene_review.validation.action_consistency import go_ancestors

    ancestors = go_ancestors()

    def aspect_of(term_id: str) -> str | None:
        if term_id in ROOT_ASPECT:
            return ROOT_ASPECT[term_id]
        anc = ancestors(term_id)
        return next((v for k, v in ROOT_ASPECT.items() if k in anc), None)

    decisions = yaml.safe_load(DECISIONS.read_text())["decisions"]
    by_file: dict[str, dict[str, dict]] = defaultdict(dict)
    for d in decisions:
        organism, gene = d["gene"].split("/")
        by_file[f"genes/{organism}/{gene}/{gene}-ai-review.yaml"][d["term"]] = d

    rt = YAML()
    rt.indent(mapping=2, sequence=2, offset=0)
    rt.width = 88
    problems = []
    for rel, terms in sorted(by_file.items()):
        path = ROOT / rel
        original = None
        for commit in ORIGINAL_COMMITS:
            shown = subprocess.run(["git", "show", f"{commit}:{rel}"], capture_output=True,
                                   text=True, cwd=ROOT)
            doc = yaml.safe_load(shown.stdout) if shown.returncode == 0 else None
            if doc and any(
                a.get("evidence_type") == "ND" and a["term"]["id"] in terms
                and (a.get("review") or {}).get("action") == terms[a["term"]["id"]]["earlier_action"]
                for a in doc.get("existing_annotations") or []
            ):
                original = shown.stdout
                break
        if original is None:
            problems.append(f"{rel}: no pre-pass version found")
            continue

        text = path.read_text()
        lines, starts, anns = blocks(text, rt)
        o_lines, o_starts, o_anns = blocks(original, rt)
        o_block = {
            a["term"]["id"]: o_lines[o_starts[i]:o_starts[i + 1]]
            for i, a in enumerate(o_anns) if a.get("evidence_type") == "ND"
        }
        o_parsed = {a["term"]["id"]: a for a in yaml.safe_load(original)["existing_annotations"]
                    if a.get("evidence_type") == "ND"}
        parsed = yaml.safe_load(text)
        doc_gaps = list(parsed.get("knowledge_gaps") or [])
        for cf in parsed.get("core_functions") or []:
            doc_gaps += list(cf.get("knowledge_gaps") or [])
        biology = [g for g in doc_gaps if "BIOLOGY" in (g.get("gap_kind") or [])]

        out: list[str] = []
        additions = []
        for i, ann in enumerate(anns):
            block = lines[starts[i]:starts[i + 1]]
            summary = str((ann.get("review") or {}).get("summary") or "")
            if any(m in summary for m in GENERATED_NEW_ROW):
                continue
            term = ann["term"]["id"]
            d = terms.get(term) if ann.get("evidence_type") == "ND" else None
            if d is None:
                out.append("".join(block))
                continue
            block = o_block[term]
            o_review = o_parsed[term].get("review") or {}
            if d["decision"] == "STALE":
                out.append("".join(rewrite_review(block, set(), {}, "STALE")))
                continue
            aspect = d["aspect"]
            ind = block[0].index("-") + 4
            child = " " * ind
            drop = {"proposed_replacement_terms"}
            if d["earlier_action"] == "MODIFY":
                drop.add("supported_by")
            new_rows = []
            if "new_row" in d:
                for rep in o_review.get("proposed_replacement_terms") or []:
                    row = {
                        "term": {"id": rep["id"], "label": rep.get("label")},
                        "evidence_type": d["new_row"]["evidence_type"],
                        "original_reference_id": (o_review.get("supported_by") or [{}])[0].get(
                            "reference_id", "GO_REF:0000024"),
                        "qualifier": d["new_row"]["qualifier"],
                        "review": {
                            "summary": f"Inferred {rep.get('label')} for this gene product, "
                                       "proposed during the NO_DATA re-action pass.",
                            "action": "NEW",
                            "reason": new_row_reason(rep.get("label"), d["new_row"]["evidence_type"],
                                                     str(o_review.get("reason") or "")),
                        },
                    }
                    if o_review.get("supported_by"):
                        row["review"]["supported_by"] = copy.deepcopy(o_review["supported_by"])
                    new_rows.append(row)
            others = [b for b in parsed["existing_annotations"]
                      if b.get("evidence_type") != "ND" and (b.get("term") or {}).get("id")
                      and not any(m in str((b.get("review") or {}).get("summary")) for m in GENERATED_NEW_ROW)
                      and aspect_of(b["term"]["id"]) == aspect]
            if any(g.get("dark_aspect") in MATCHING_DARK[aspect] for g in biology):
                nd_case = "TRUE_GAP"
            elif new_rows or any(b.get("evidence_type") in INFERRED
                                 and (b.get("review") or {}).get("action") in RETAINED
                                 for b in others):
                nd_case = "INFERABLE"
            else:
                nd_case = None
            labels = ", ".join(r["term"]["label"] for r in new_rows) or None
            replace = {
                "summary": folded("summary", summary_text(aspect), child),
                "action": [f"{child}action: ACCEPT\n"],
                "reason": folded("reason", reason_text(aspect, d["earlier_action"],
                                                       d.get("note"), labels), child),
            }
            out.append("".join(rewrite_review(block, drop, replace, nd_case)))
            additions.extend(new_rows)
        if additions:
            buf = io.StringIO()
            seq_pad = lines[starts[0]].index("-")
            rt.indent(mapping=2, sequence=seq_pad + 2, offset=seq_pad)
            rt.dump(additions, buf)
            rt.indent(mapping=2, sequence=2, offset=0)
            out.append("".join(line.rstrip() + "\n" for line in buf.getvalue().splitlines()))
        new_text = "".join(lines[:starts[0]]) + "".join(out) + "".join(lines[starts[-1]:])
        path.write_text(move_dangling_anchors(new_text, original))
    print(f"{len(by_file)} reviews processed")
    for p in problems:
        print("PROBLEM", p)


if __name__ == "__main__":
    main()
