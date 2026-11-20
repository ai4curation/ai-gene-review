"""Decision-record style GO annotation guidelines (``projects/GO_GUIDELINES``).

Each guideline is one Markdown file, ``guidelines/<TOPIC>/<ID>.md``, whose YAML
frontmatter is a ``Guideline`` (``src/ai_gene_review/schema/guideline.yaml``).
Each topic folder has a ``README.md`` whose frontmatter is a ``Chapter``.

The frontmatter is the single source of truth for metadata. Two things are
derived from it and kept in the files so that GitHub and the rendered project
pages show them too:

- the block between :data:`BEGIN` and :data:`END` at the end of each guideline
  (record table, differences, open questions, sources), and
- the rule index between :data:`INDEX_BEGIN` and :data:`INDEX_END` in each README.

``build`` rewrites both and writes the static browser payload
(``app/guidelines/data.js``); ``validate`` reports schema errors, broken
cross-references and stale derived text.

Topics not yet split into folders remain single chapter files
(``guidelines/<name>.md``) with ``### X-N.`` rule headings; references to their
rules are resolved to those headings.
"""

from __future__ import annotations

import json
import os
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import typer
import yaml

from ai_gene_review.render_projects import parse_frontmatter

GUIDELINES_DIR = Path("projects/GO_GUIDELINES/guidelines")
BROWSER_DIR = Path("app/guidelines")
SCHEMA_PATH = Path(__file__).parent / "schema" / "guideline.yaml"
GITHUB_BLOB = "https://github.com/ai4curation/ai-gene-review/blob/main/"

BEGIN = "<!-- BEGIN GENERATED: edit the frontmatter, then run `just build-guidelines` -->"
END = "<!-- END GENERATED -->"
INDEX_BEGIN = "<!-- BEGIN GENERATED RULE INDEX -->"
INDEX_END = "<!-- END GENERATED RULE INDEX -->"

RULE_ID = re.compile(r"\b([A-Z]{2,4})-(\d+)\b")
LEGACY_HEADING = re.compile(r"^### ([A-Z]{2,4}-\d+)\.\s+(.*)$", re.M)
LINK = re.compile(r"(\[[^\]]*\]\()([^)\s]+)(\))")
PROVENANCE_LABEL = {"GOC": "[GOC]", "GOC_PLUS": "[GOC+]", "NEW": "[NEW]"}


@dataclass
class Record:
    """A guideline or chapter file: its repo path, frontmatter and body."""

    path: Path
    meta: Dict[str, Any]
    body: str

    @property
    def id(self) -> str:
        return str(self.meta.get("id", ""))


@dataclass
class Collection:
    """Every guideline record, chapter and legacy rule heading under a root."""

    root: Path
    guidelines: Dict[str, Record] = field(default_factory=dict)
    chapters: Dict[str, Record] = field(default_factory=dict)
    #: Rules still inside an unsplit chapter file: id -> (repo path, title).
    legacy: Dict[str, Tuple[Path, str]] = field(default_factory=dict)

    def location(self, rule_id: str) -> Optional[Tuple[Path, Optional[str]]]:
        """Repo path (and anchor, for a legacy rule) where a rule id lives."""
        if rule_id in self.guidelines:
            return self.guidelines[rule_id].path, None
        if rule_id in self.legacy:
            return self.legacy[rule_id][0], rule_id.lower()
        return None


def load(root: Path = Path(".")) -> Collection:
    """Load all guideline records under ``root``."""
    base = root / GUIDELINES_DIR
    coll = Collection(root=root)
    for md in sorted(base.glob("*/*.md")):
        meta, body = parse_frontmatter(md.read_text())
        rec = Record(md.relative_to(root), meta, body)
        if md.name == "README.md":
            coll.chapters[md.parent.name] = rec
        else:
            coll.guidelines[md.stem] = rec
    for md in sorted(base.glob("*.md")):
        for m in LEGACY_HEADING.finditer(md.read_text()):
            coll.legacy[m.group(1)] = (md.relative_to(root), m.group(2).strip())
    return coll


def rel_link(from_file: Path, target: Path, anchor: Optional[str] = None) -> str:
    """Relative Markdown link from one repo file to another.

    >>> rel_link(Path("a/b/MF/MF-1.md"), Path("a/b/MF/MF-2.md"))
    'MF-2.md'
    >>> rel_link(Path("a/b/MF/MF-1.md"), Path("a/b/qn.md"), "qn-7")
    '../qn.md#qn-7'
    """
    rel = os.path.relpath(target, from_file.parent)
    return f"{rel}#{anchor}" if anchor else rel


def rule_link(coll: Collection, from_file: Path, rule_id: str) -> str:
    """Markdown link text for a rule id, or the bare id if it is unknown."""
    loc = coll.location(rule_id)
    if loc is None:
        return rule_id
    return f"[{rule_id}]({rel_link(from_file, *loc)})"


def _cell(text: Any) -> str:
    return " ".join(str(text).split()).replace("|", "\\|")


def _source_line(rec_path: Path, src: Dict[str, Any]) -> str:
    title = src.get("title") or src.get("url") or src.get("path")
    target = src.get("url") or rel_link(rec_path, Path(src["path"]))
    return f"- {src['kind']}: [{title}]({target})"


def _differences_table(diffs: List[Dict[str, Any]]) -> List[str]:
    lines = [
        "| Prior source | What it said | What we recommend | Why |",
        "|---|---|---|---|",
    ]
    for d in diffs:
        why = _cell(d["why"])
        if d.get("issue"):
            why += f" (#{d['issue']})"
        lines.append(
            f"| {_cell(d['prior_source'])} | {_cell(d['prior_said'])} | "
            f"{_cell(d['we_recommend'])} | {why} |"
        )
    return lines


def generated_block(coll: Collection, rec: Record) -> str:
    """The derived Markdown block for a guideline (or chapter) record."""
    m = rec.meta
    out = [BEGIN, ""]
    if rec.path.name != "README.md":
        out += ["## Record", "", "| | |", "|---|---|"]
        out.append(f"| Status | {m.get('status', '')} |")
        prov = PROVENANCE_LABEL.get(m.get("provenance", ""), "")
        note = _cell(m.get("provenance_note", ""))
        if note:
            prov = note if note.startswith(prov) else f"{prov} {note}"
        out.append(f"| Provenance | {prov} |")
        if m.get("date"):
            out.append(f"| Date | {m['date']} |")
        for key, label in (("supersedes", "Supersedes"), ("related", "Related")):
            if m.get(key):
                out.append(f"| {label} | " + ", ".join(rule_link(coll, rec.path, r) for r in m[key]) + " |")
        if m.get("superseded_by"):
            out.append(f"| Superseded by | {rule_link(coll, rec.path, m['superseded_by'])} |")
        if m.get("enforced_by"):
            links = ", ".join(f"[`{p}`]({rel_link(rec.path, Path(p))})" for p in m["enforced_by"])
            out.append(f"| Enforced by | {links} |")
        if m.get("evidence_codes"):
            out.append("| Evidence codes | " + ", ".join(m["evidence_codes"]) + " |")
        if m.get("go_terms"):
            terms = [
                f"`{t['term_id']}` " + (t.get("label") or "") + (" (obsolete)" if t.get("obsolete") else "")
                for t in m["go_terms"]
            ]
            out.append("| GO terms | " + "; ".join(x.strip() for x in terms) + " |")
        for r in m.get("reviews") or []:
            out.append(
                f"| Review | {r['reviewed_by']} {r.get('review_date', '')} "
                f"{r.get('review_status', '')} {_cell(r.get('notes', ''))} |".replace("  ", " ")
            )
        out.append("")
    if m.get("differences"):
        out += ["## Differences from prior guidance", ""] + _differences_table(m["differences"]) + [""]
    if m.get("open_questions"):
        out += ["## Open questions", ""]
        out += [f"{i}. {' '.join(q.split())}" for i, q in enumerate(m["open_questions"], 1)] + [""]
    if m.get("sources"):
        out += ["## Sources", ""] + [_source_line(rec.path, s) for s in m["sources"]] + [""]
    out.append(END)
    return "\n".join(out)


def rule_index(coll: Collection, chapter: str) -> str:
    """The generated rule table for a chapter README."""
    readme = coll.chapters[chapter].path
    lines = [INDEX_BEGIN, "", "| Id | Guideline | Status | Provenance |", "|---|---|---|---|"]
    for rid in sorted((g for g in coll.guidelines if g.split("-")[0] == chapter), key=sort_key):
        m = coll.guidelines[rid].meta
        lines.append(
            f"| [{rid}]({rel_link(readme, coll.guidelines[rid].path)}) | {_cell(m['title'])} | "
            f"{m.get('status', '')} | {PROVENANCE_LABEL.get(m.get('provenance', ''), '')} |"
        )
    return "\n".join(lines + ["", INDEX_END])


def sort_key(rule_id: str) -> Tuple[str, int]:
    """Sort ``MF-2`` before ``MF-10``.

    >>> sorted(["MF-10", "MF-2"], key=sort_key)
    ['MF-2', 'MF-10']
    """
    prefix, _, num = rule_id.partition("-")
    return prefix, int(num)


def _replace_between(text: str, begin: str, end: str, block: str) -> str:
    """Replace ``begin..end`` (inclusive) with ``block``, or append it.

    >>> _replace_between("a\\nB\\nold\\nE\\n", "B", "E", "B\\nnew\\nE")
    'a\\nB\\nnew\\nE\\n'
    >>> _replace_between("a\\n", "B", "E", "B\\nE")
    'a\\n\\nB\\nE\\n'
    """
    if begin in text and end in text:
        head, rest = text.split(begin, 1)
        _, tail = rest.split(end, 1)
        return head + block + tail
    return text.rstrip("\n") + "\n\n" + block + "\n"


def expected_text(coll: Collection, rec: Record) -> str:
    """The full file text a record should have after ``build``."""
    text = (coll.root / rec.path).read_text()
    if rec.path.name == "README.md":
        text = _replace_between(text, INDEX_BEGIN, INDEX_END, rule_index(coll, rec.path.parent.name))
        if rec.meta.get("differences") or rec.meta.get("open_questions"):
            text = _replace_between(text, BEGIN, END, generated_block(coll, rec))
        return text
    return _replace_between(text, BEGIN, END, generated_block(coll, rec))


def strip_generated(body: str) -> str:
    """Body without its derived blocks.

    >>> strip_generated("x\\n\\n" + BEGIN + "\\nstuff\\n" + END + "\\n")
    'x'
    """
    for begin, end in ((BEGIN, END), (INDEX_BEGIN, INDEX_END)):
        if begin in body:
            head, rest = body.split(begin, 1)
            body = head + rest.split(end, 1)[1] if end in rest else head
    return body.strip()


def browser_href(coll: Collection, from_file: Path, target: str) -> str:
    """Where a Markdown link in ``from_file`` should point inside the browser.

    Guideline links become in-app routes; other project pages go to their
    rendered HTML; anything else in the repository goes to GitHub.
    """
    if re.match(r"^[a-z]+:", target) or target.startswith("#"):
        return target
    path_part, _, anchor = target.partition("#")
    repo = Path(os.path.normpath(from_file.parent / path_part))
    for rid, rec in coll.guidelines.items():
        if rec.path == repo:
            return f"#{rid}"
    if repo.name == "README.md" and repo.parent.name in coll.chapters:
        return f"#chapter/{repo.parent.name}"
    if anchor and anchor.upper() in coll.legacy and coll.legacy[anchor.upper()][0] == repo:
        return f"#{anchor.upper()}"
    if repo.parts[:1] == ("projects",) and repo.suffix == ".md":
        html = Path(*repo.parts[1:]).with_suffix(".html").as_posix()
        return f"../../pages/projects/{html}" + (f"#{anchor}" if anchor else "")
    return GITHUB_BLOB + repo.as_posix() + (f"#{anchor}" if anchor else "")


def browser_markdown(coll: Collection, from_file: Path, text: str) -> str:
    """Rewrite every relative link in ``text`` for the browser."""
    return LINK.sub(lambda m: m.group(1) + browser_href(coll, from_file, m.group(2)) + m.group(3), text)


def _page_url(path: Path) -> str:
    return "../../pages/" + path.with_suffix(".html").as_posix()


def browser_data(coll: Collection) -> Dict[str, Any]:
    """The payload the static browser reads."""
    guidelines = []
    for rid in sorted(coll.guidelines, key=sort_key):
        rec = coll.guidelines[rid]
        item = dict(rec.meta)
        item["date"] = str(item.get("date", ""))
        item["body"] = browser_markdown(coll, rec.path, strip_generated(rec.body))
        for d in item.get("differences") or []:
            for key in ("prior_source", "we_recommend", "why", "prior_said"):
                d[key] = browser_markdown(coll, rec.path, str(d[key]))
        item["open_questions"] = [browser_markdown(coll, rec.path, q) for q in item.get("open_questions") or []]
        item["sources"] = [
            {**s, "href": s.get("url") or browser_href(coll, rec.path, rel_link(rec.path, Path(s["path"])))}
            for s in item.get("sources") or []
        ]
        item["path"] = rec.path.as_posix()
        item["page"] = _page_url(rec.path)
        guidelines.append(item)
    chapters = []
    for cid in sorted(coll.chapters):
        rec = coll.chapters[cid]
        item = dict(rec.meta)
        item["date"] = str(item.get("date", ""))
        item["body"] = browser_markdown(coll, rec.path, strip_generated(rec.body))
        for d in item.get("differences") or []:
            for key in ("prior_source", "we_recommend", "why", "prior_said"):
                d[key] = browser_markdown(coll, rec.path, str(d[key]))
        item["open_questions"] = [browser_markdown(coll, rec.path, q) for q in item.get("open_questions") or []]
        item["path"] = rec.path.as_posix()
        item["page"] = _page_url(rec.path)
        chapters.append(item)
    legacy = [
        {"id": rid, "title": title, "page": _page_url(path) + f"#{rid.lower()}"}
        for rid, (path, title) in sorted(coll.legacy.items(), key=lambda kv: sort_key(kv[0]))
    ]
    return {"guidelines": guidelines, "chapters": chapters, "unsplit_rules": legacy}


def browser_payload(coll: Collection) -> str:
    """Text of ``app/guidelines/data.js``."""
    return "window.GUIDELINES_DATA = " + json.dumps(browser_data(coll), ensure_ascii=False, indent=1) + ";\n"


def build(root: Path = Path(".")) -> List[Path]:
    """Rewrite derived blocks and the browser payload; return files changed."""
    coll = load(root)
    changed = []
    for rec in [*coll.guidelines.values(), *coll.chapters.values()]:
        target = root / rec.path
        new = expected_text(coll, rec)
        if new != target.read_text():
            target.write_text(new)
            changed.append(rec.path)
    coll = load(root)
    out = root / BROWSER_DIR / "data.js"
    out.parent.mkdir(parents=True, exist_ok=True)
    payload = browser_payload(coll)
    if not out.exists() or out.read_text() != payload:
        out.write_text(payload)
        changed.append(BROWSER_DIR / "data.js")
    return changed


def _schema_errors(rec: Record, target_class: str) -> List[str]:
    from linkml.validator import validate as linkml_validate

    instance = json.loads(json.dumps(rec.meta, default=str))
    report = linkml_validate(instance, str(SCHEMA_PATH), target_class)
    return [f"{rec.path}: {r.message}" for r in report.results]


def term_errors(coll: Collection, adapter: Any) -> List[str]:
    """Check each ``go_terms`` entry against an OAK adapter."""
    obsolete = set(adapter.obsoletes())
    errors = []
    for rec in coll.guidelines.values():
        for t in rec.meta.get("go_terms") or []:
            tid = t["term_id"]
            if tid in obsolete:
                if not t.get("obsolete"):
                    errors.append(f"{rec.path}: {tid} is obsolete but not flagged obsolete")
                continue
            label = adapter.label(tid)
            if label is None:
                errors.append(f"{rec.path}: {tid} is not in the ontology")
            elif t.get("obsolete"):
                errors.append(f"{rec.path}: {tid} ({label}) is flagged obsolete but is live")
            elif t.get("label") != label:
                errors.append(f"{rec.path}: {tid} label {t.get('label')!r} should be {label!r}")
    return errors


def validate(root: Path = Path("."), check_terms: bool = False) -> List[str]:
    """Every problem found in the guideline records, as messages."""
    coll = load(root)
    errors: List[str] = []
    for topic, rec in coll.chapters.items():
        errors += _schema_errors(rec, "Chapter")
        if rec.id != topic:
            errors.append(f"{rec.path}: chapter id {rec.id!r} does not match folder {topic!r}")
    for rid, rec in coll.guidelines.items():
        errors += _schema_errors(rec, "Guideline")
        m = rec.meta
        topic = rec.path.parent.name
        if m.get("id") != rid:
            errors.append(f"{rec.path}: id {m.get('id')!r} does not match file name")
        if m.get("topic") != topic or not rid.startswith(topic + "-"):
            errors.append(f"{rec.path}: topic {m.get('topic')!r} and id must match folder {topic!r}")
        if topic not in coll.chapters:
            errors.append(f"{rec.path}: folder has no README.md chapter record")
        if rid in coll.legacy:
            errors.append(f"{rec.path}: {rid} is also still a heading in {coll.legacy[rid][0]}")
        for key in ("related", "supersedes"):
            for ref in m.get(key) or []:
                if coll.location(ref) is None:
                    errors.append(f"{rec.path}: {key} names unknown guideline {ref}")
        sup = m.get("superseded_by")
        if sup:
            if coll.location(sup) is None:
                errors.append(f"{rec.path}: superseded_by names unknown guideline {sup}")
            elif sup in coll.guidelines and rid not in (coll.guidelines[sup].meta.get("supersedes") or []):
                errors.append(f"{rec.path}: {sup} does not list {rid} in supersedes")
        if (m.get("status") == "superseded") != bool(sup):
            errors.append(f"{rec.path}: status 'superseded' and superseded_by must go together")
        for old in m.get("supersedes") or []:
            if old in coll.guidelines and coll.guidelines[old].meta.get("superseded_by") != rid:
                errors.append(f"{rec.path}: {old} does not name {rid} as superseded_by")
        for p in m.get("enforced_by") or []:
            if not (root / p).exists():
                errors.append(f"{rec.path}: enforced_by path {p} does not exist")
        for s in m.get("sources") or []:
            if bool(s.get("url")) == bool(s.get("path")):
                errors.append(f"{rec.path}: source {s.get('title')!r} needs exactly one of url or path")
            elif s.get("path") and not (root / s["path"]).exists():
                errors.append(f"{rec.path}: source path {s['path']} does not exist")
    if errors:
        return errors  # derived text is only defined for well-formed records
    for rec in [*coll.guidelines.values(), *coll.chapters.values()]:
        if expected_text(coll, rec) != (root / rec.path).read_text():
            errors.append(f"{rec.path}: generated text is stale; run `just build-guidelines`")
    data_js = root / BROWSER_DIR / "data.js"
    if coll.guidelines and (not data_js.exists() or data_js.read_text() != browser_payload(coll)):
        errors.append(f"{BROWSER_DIR / 'data.js'}: browser data is stale; run `just build-guidelines`")
    if check_terms:
        from oaklib import get_adapter

        errors += term_errors(coll, get_adapter("sqlite:obo:go"))
    return errors


def dump_frontmatter(meta: Dict[str, Any]) -> str:
    """Serialise a record's frontmatter block.

    >>> print(dump_frontmatter({"id": "MF-1", "title": "x"}), end="")
    ---
    id: MF-1
    title: x
    ---
    """
    text = yaml.safe_dump(meta, sort_keys=False, allow_unicode=True, width=100)
    return f"---\n{text}---\n"


guidelines_app = typer.Typer(help="Decision-record GO annotation guidelines (projects/GO_GUIDELINES).")


@guidelines_app.command("build")
def build_command(root: Path = typer.Option(Path("."), help="Repository root.")) -> None:
    """Regenerate derived blocks in the guideline files and the browser data."""
    for path in build(root):
        typer.echo(f"updated {path}")


@guidelines_app.command("validate")
def validate_command(
    root: Path = typer.Option(Path("."), help="Repository root."),
    check_terms: bool = typer.Option(False, help="Also check GO term labels against the local GO build."),
) -> None:
    """Report schema errors, broken references and stale generated text."""
    errors = validate(root, check_terms=check_terms)
    for e in errors:
        typer.echo(e)
    if errors:
        raise typer.Exit(1)
    typer.echo("guidelines OK")
