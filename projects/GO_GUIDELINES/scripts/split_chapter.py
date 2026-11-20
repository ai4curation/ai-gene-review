"""Split one monolithic guideline chapter into decision-record files.

    uv run python projects/GO_GUIDELINES/scripts/split_chapter.py \
        projects/GO_GUIDELINES/guidelines/molecular-function.md MF [--assign assign/MF.yaml] [--write]

Reads ``<chapter>.md`` (rules as ``### MF-n. Title`` headings) and writes
``guidelines/MF/README.md`` plus one ``guidelines/MF/MF-n.md`` per rule, with
frontmatter extracted from the text: provenance, GO terms (labels from the
local GO build), evidence codes, related rules, validators, sources.
Rows of the Differences table and items of Open questions are attached to the
rule they cite; ``--assign`` gives the rest (row/item number -> rule id or
``chapter``). Without ``--write`` it only reports what it would do.

After writing, it deletes the chapter file and rewrites links to it in the
other guideline files and the project page. Run ``just build-guidelines``
afterwards to fill in the generated blocks.
"""

from __future__ import annotations

import argparse
import os
import re
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import yaml
from oaklib import get_adapter

from ai_gene_review.guidelines import (
    BEGIN,
    END,
    GUIDELINES_DIR,
    INDEX_BEGIN,
    INDEX_END,
    LINK,
    dump_frontmatter,
)

EVIDENCE_CODES = (
    "EXP IDA IPI IMP IGI IEP HTP HDA HMP HGI HEP IBA IBD IKR IRD ISS ISO ISA ISM IGC RCA TAS NAS IC ND IEA"
).split()
PREFIXES = "EV LIT MF TR BP RS CC PC QN AE PH IEA CAM MO REV ONT".split()
RULE_REF = re.compile(r"\b(" + "|".join(PREFIXES) + r")-(\d+)\b")
HEADING = re.compile(r'^<a id="[^"]+"></a>\n### ([A-Z]+-\d+)\. (.+)$', re.M)
ASPECTS = {"MF": ["F"], "BP": ["P"], "RS": ["P"], "TR": ["F", "P"], "CC": ["C"], "PC": ["C", "F"]}


def sections(text: str) -> Dict[str, str]:
    """Top-level ``## `` sections by heading, plus ``_head`` for the preamble."""
    parts = re.split(r"^## (.+)$", text, flags=re.M)
    out = {"_head": parts[0]}
    for name, body in zip(parts[1::2], parts[2::2]):
        out[name.strip()] = body
    return out


def deepen(text: str, topic: str, rule_ids: set) -> str:
    """Rewrite links for text moving one folder deeper (into ``<TOPIC>/``)."""

    def fix(m: re.Match) -> str:
        target = m.group(2)
        if re.match(r"^[a-z]+:", target):
            return m.group(0)
        if target.startswith("#"):
            anchor = target[1:]
            if anchor.upper() in rule_ids:
                return m.group(1) + f"{anchor.upper()}.md" + m.group(3)
            return m.group(1) + f"README.md{target}" + m.group(3)
        return m.group(1) + "../" + target + m.group(3)

    return LINK.sub(fix, text)


def classify(target: str, file_dir: Path, root: Path) -> Optional[Dict[str, str]]:
    """A SourceRef for a link target, or None for links that are not sources."""
    if target.startswith("#"):
        return None
    if re.match(r"^https?://", target):
        if "wiki.geneontology.org" in target:
            kind = "wiki"
        elif "drive.google.com" in target or "docs.google.com" in target:
            kind = "drive"
        elif "/issues/" in target or "/pull/" in target:
            kind = "issue"
        elif "europepmc.org" in target or "pubmed" in target or "doi.org" in target:
            kind = "paper"
        else:
            kind = "web"
        return {"kind": kind, "url": target}
    rel_path = Path(os.path.normpath(os.path.join(file_dir, target.split("#")[0])))
    if GUIDELINES_DIR.as_posix() in rel_path.as_posix():
        return None  # another guideline: a relation, not a source
    return {"kind": "repo", "path": rel_path.as_posix()}


def extract_sources(text: str, file_dir: Path, root: Path) -> List[Dict[str, str]]:
    seen, out = set(), []
    for m in re.finditer(r"\[([^\]]*)\]\(([^)\s]+)\)", text):
        src = classify(m.group(2), file_dir, root)
        if src is None:
            continue
        key = src.get("url") or src.get("path")
        if key in seen:
            continue
        seen.add(key)
        title = re.sub(r"^(wiki|Drive|drive):\s*", "", m.group(1)).strip("` ")
        out.append({"kind": src["kind"], "title": title or key, **{k: v for k, v in src.items() if k != "kind"}})
    return out


def go_terms(text: str, adapter: Any, obsolete: set) -> List[Dict[str, Any]]:
    out = []
    for tid in dict.fromkeys(re.findall(r"\bGO:\d{7}\b", text)):
        if tid in obsolete:
            out.append({"term_id": tid, "obsolete": True})
        else:
            label = adapter.label(tid)
            if label is None:
                raise SystemExit(f"{tid} is neither live nor obsolete in the local GO build")
            out.append({"term_id": tid, "label": label})
    return out


def provenance(note: str) -> str:
    tags = re.findall(r"\[(GOC\+?|NEW)\]", note)
    if "NEW" in tags:
        return "NEW"
    if "GOC+" in tags:
        return "GOC_PLUS"
    if "GOC" in tags:
        return "GOC"
    raise SystemExit(f"no provenance tag in: {note[:80]}")


def split_rule(body: str) -> Tuple[str, str, str, str]:
    """(decision, context, application, provenance paragraph) of a rule body."""
    paras = [p.strip() for p in re.split(r"\n\s*\n", body.strip()) if p.strip()]
    prov = [p for p in paras if p.startswith("Provenance:")]
    if len(prov) != 1:
        raise SystemExit(f"expected one Provenance paragraph, got {len(prov)}: {paras[0][:80]}")
    paras.remove(prov[0])
    decision = paras.pop(0) if paras and paras[0].startswith("**") else ""
    if decision.startswith("**") and decision.endswith("**") and decision.count("**") == 2:
        decision = decision[2:-2]
    if paras and paras[0].startswith("Rationale. "):
        paras[0] = paras[0][len("Rationale. "):]
    ctx: List[str] = []
    app: List[str] = []
    target = ctx
    for p in paras:
        if re.match(r"^\*?(Worked|Examples?\b|In review)", p):
            target = app
        target.append(p)
    return decision, "\n\n".join(ctx), "\n\n".join(app), prov[0]


def table_rows(section: str) -> List[List[str]]:
    rows = []
    for line in section.splitlines():
        if line.startswith("|") and not re.match(r"^\|\s*-", line) and "What we recommend" not in line:
            cells = [c.strip() for c in re.split(r"(?<!\\)\|", line.strip())[1:-1]]
            if len(cells) == 4:
                rows.append(cells)
    return rows


def list_items(section: str) -> List[str]:
    items: List[str] = []
    for line in section.splitlines():
        m = re.match(r"^\d+\.\s+(.*)$", line)
        if m:
            items.append(m.group(1))
        elif items and line.strip():
            items[-1] += " " + line.strip()
    return items


def owner(text: str, topic: str, own_ids: set, manual: Dict[int, str], n: int) -> str:
    if n in manual:
        return manual[n]
    refs = [f"{p}-{k}" for p, k in RULE_REF.findall(text)] + [a.upper() for a in re.findall(r"\(#([a-z]+-\d+)\)", text)]
    mine = [r for r in dict.fromkeys(refs) if r in own_ids]
    return mine[0] if len(mine) == 1 else ""


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("chapter", type=Path)
    ap.add_argument("topic")
    ap.add_argument("--assign", type=Path, help="YAML: {differences: {row: id|chapter}, open_questions: {...}}")
    ap.add_argument("--date", default="2026-11-15")
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()

    root = Path(".")
    topic = args.topic
    text = args.chapter.read_text()
    secs = sections(text)
    folder = args.chapter.parent / topic
    file_dir = folder  # links are rewritten as if already moved

    rules_text = secs["Rules"]
    heads = list(HEADING.finditer(rules_text))
    ids = [h.group(1) for h in heads]
    own_ids = set(ids)
    manual = yaml.safe_load(args.assign.read_text()) if args.assign else {}
    adapter = get_adapter("sqlite:obo:go")
    obsolete = set(adapter.obsoletes())

    records: Dict[str, Dict[str, Any]] = {}
    bodies: Dict[str, str] = {}
    for i, h in enumerate(heads):
        rid, title = h.group(1), h.group(2).strip()
        end = heads[i + 1].start() if i + 1 < len(heads) else len(rules_text)
        raw = deepen(rules_text[h.end():end], topic, own_ids)
        decision, context, application, prov = split_rule(raw)
        note = " ".join(re.sub(r"^Provenance:\s*", "", prov).split())
        note = re.sub(r"\s*Sources:.*$", "", note)  # the links are kept in `sources`
        related = [r for r in dict.fromkeys(f"{p}-{k}" for p, k in RULE_REF.findall(raw)) if r != rid]
        enforced = [
            s["path"] for s in extract_sources(raw, file_dir, root)
            if s["kind"] == "repo" and s["path"].startswith("src/ai_gene_review/validation/")
        ]
        meta: Dict[str, Any] = {
            "id": rid,
            "title": title,
            "status": "proposed",
            "topic": topic,
            "provenance": provenance(note),
        }
        if not re.fullmatch(r"\[(GOC\+?|NEW)\]\.?", note):
            meta["provenance_note"] = note
        if topic in ASPECTS:
            meta["aspects"] = ASPECTS[topic]
        codes = [c for c in EVIDENCE_CODES if re.search(rf"(?<![\w-]){c}(?![\w-])", raw)]
        if codes:
            meta["evidence_codes"] = codes
        terms = go_terms(raw, adapter, obsolete)
        if terms:
            meta["go_terms"] = terms
        if related:
            meta["related"] = related
        if enforced:
            meta["enforced_by"] = enforced
        meta["differences"] = []
        meta["open_questions"] = []
        meta["sources"] = extract_sources(raw, file_dir, root)
        meta["date"] = args.date
        records[rid] = meta
        parts = [f"# {rid}. {title}", ""]
        parts += ["## Decision", "", decision or "(see Context)", ""]
        if context:
            parts += ["## Context", "", context, ""]
        if application:
            parts += ["## Application", "", application, ""]
        bodies[rid] = "\n".join(parts)

    chapter_diffs: List[Dict[str, Any]] = []
    unassigned = []
    for n, (src, said, rec, why) in enumerate(table_rows(secs["Differences from prior guidance"]), 1):
        d = {k: deepen(v, topic, own_ids) for k, v in
             zip(("prior_source", "prior_said", "we_recommend", "why"), (src, said, rec, why))}
        who = owner(rec, topic, own_ids, manual.get("differences", {}), n) or owner(
            " ".join((src, said, why)), topic, own_ids, {}, n)
        if who == "chapter":
            chapter_diffs.append(d)
        elif who:
            d["we_recommend"] = re.sub(rf"\s*\(\[{who}\]\({who}\.md\)\)", "", d["we_recommend"])
            records[who]["differences"].append(d)
        else:
            unassigned.append(("difference", n, rec[:110]))
    chapter_qs: List[str] = []
    for n, q in enumerate(list_items(secs["Open questions"]), 1):
        q = deepen(q, topic, own_ids)
        who = owner(q, topic, own_ids, manual.get("open_questions", {}), n)
        if who == "chapter":
            chapter_qs.append(q)
        elif who:
            records[who]["open_questions"].append(q)
        else:
            unassigned.append(("question", n, q[:110]))

    for kind, n, snippet in unassigned:
        print(f"UNASSIGNED {kind} {n}: {snippet}")
    for rid, meta in records.items():
        print(f"{rid}: {meta['provenance']}, {len(meta['differences'])} diffs, "
              f"{len(meta['open_questions'])} questions, {len(meta['sources'])} sources, "
              f"{len(meta.get('go_terms', []))} terms")
    if unassigned:
        raise SystemExit("assign the rows above with --assign before writing")
    if not args.write:
        return

    title_line = secs["_head"].splitlines()[0]
    head = deepen(secs["_head"], topic, own_ids)
    head = re.sub(r"^Status: .*$", "Status: see each guideline · Part of [GO_GUIDELINES](../../../GO_GUIDELINES.md)",
                  head, flags=re.M)
    readme_body = [head.rstrip(), ""]
    for name in ("Scope", "Principles"):
        readme_body += [f"## {name}", deepen(secs[name], topic, own_ids).rstrip(), ""]
    readme_body += [
        "## Rules", "",
        "Each rule is its own record in this folder. Its frontmatter holds the metadata "
        "(status, provenance, differences from prior guidance, open questions, sources).", "",
        INDEX_BEGIN, INDEX_END, "",
    ]
    for name in ("Decision aid", "Common errors"):
        readme_body += [f"## {name}", deepen(secs[name], topic, own_ids).rstrip(), ""]
    readme_body += ["## Reading list", deepen(secs["Sources"], topic, own_ids).rstrip(), ""]
    chapter_meta: Dict[str, Any] = {
        "id": topic,
        "title": re.sub(r"^# ", "", title_line).replace(": GO annotation guidelines", ""),
        "status": "proposed",
    }
    if topic in ASPECTS:
        chapter_meta["aspects"] = ASPECTS[topic]
    if chapter_diffs:
        chapter_meta["differences"] = chapter_diffs
    if chapter_qs:
        chapter_meta["open_questions"] = chapter_qs
    chapter_meta["date"] = args.date

    folder.mkdir(exist_ok=True)
    (folder / "README.md").write_text(dump_frontmatter(chapter_meta) + "\n" + "\n".join(readme_body).rstrip() + "\n")
    for rid, meta in records.items():
        meta = {k: v for k, v in meta.items() if v != []}
        (folder / f"{rid}.md").write_text(dump_frontmatter(meta) + "\n" + bodies[rid].rstrip() + "\n\n" + BEGIN + "\n" + END + "\n")
    args.chapter.unlink()
    relink(args.chapter, folder, own_ids)


def relink(old: Path, folder: Path, own_ids: set) -> None:
    """Point links at the removed chapter file to the new records."""
    files = list(GUIDELINES_DIR.glob("*.md")) + list(GUIDELINES_DIR.glob("*/*.md")) + [Path("projects/GO_GUIDELINES.md")]
    for f in files:
        text = f.read_text()

        def fix(m: re.Match) -> str:
            target = m.group(2)
            if re.match(r"^[a-z]+:", target) or target.startswith("#"):
                return m.group(0)
            path_part, _, anchor = target.partition("#")
            if Path(os.path.normpath(f.parent / path_part)) != Path(os.path.normpath(old)):
                return m.group(0)
            dest = folder / (f"{anchor.upper()}.md" if anchor.upper() in own_ids else "README.md")
            new = os.path.relpath(dest, f.parent)
            if anchor and anchor.upper() not in own_ids:
                new += f"#{anchor}"
            return m.group(1) + new + m.group(3)

        new_text = LINK.sub(fix, text)
        if new_text != text:
            f.write_text(new_text)
            print(f"relinked {f}")


if __name__ == "__main__":
    main()
