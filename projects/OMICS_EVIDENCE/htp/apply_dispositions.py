"""Apply the OMICS_EVIDENCE default dispositions to existing gene reviews.

Two rules, agreed on projects/OMICS_EVIDENCE.md (Recommendations, 2026-10-06):

  V. Vesicle-type location from a bulk vesicle/body-fluid proteome.
     Rows: evidence_type HDA or HTP, not negated, term in VESICLE_TERMS.
     Change: action UNDECIDED / MARK_AS_OVER_ANNOTATED / PENDING / unset -> KEEP_AS_NON_CORE.
     Left alone: ACCEPT and REMOVE (explicit protein-specific judgements; ACCEPT rows are
     listed in the audit for follow-up), KEEP_AS_NON_CORE (already compliant), MODIFY, NEW.

  M. Generic `membrane` (GO:0016020) from a membrane-fraction proteome, for a protein
     with no membrane anchor.
     Rows: evidence_type HDA or HTP, not negated, term GO:0016020, and the gene's
     *-uniprot.txt records no membrane anchor (see has_membrane_anchor).
     Change: action KEEP_AS_NON_CORE / UNDECIDED / PENDING / unset
     -> MARK_AS_OVER_ANNOTATED.
     Left alone: ACCEPT (explicit judgement; listed in the audit), REMOVE, MODIFY (a
     replacement was chosen), NEW, and every row of a protein with a documented membrane
     anchor or association, or with no UniProt file to check.

Edits are textual and minimal: only the row's `action:` line changes, and its `reason:`
value is rewritten to the original text plus a disposition note. Each edited file is
re-parsed and compared with the original parse; any difference other than the intended
action/reason values aborts that file (nothing is written for it).

Outputs an audit file listing every changed row (old -> new action) and every ACCEPT
row the rules matched but left in place.

Usage:
  python3 projects/OMICS_EVIDENCE/htp/apply_dispositions.py            # dry run
  python3 projects/OMICS_EVIDENCE/htp/apply_dispositions.py --write    # edit files
"""

from __future__ import annotations

import argparse
import copy
import glob
import os
import re
import sys
import textwrap
from collections import Counter

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
AUDIT = os.path.join(HERE, "disposition-2026-10-06.yaml")
LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CODES = {"HDA", "HTP"}
VESICLE_TERMS = {
    "GO:0070062": "extracellular exosome",
    "GO:1903561": "extracellular vesicle",
    "GO:0072562": "blood microparticle",
    "GO:0031982": "vesicle",
    "GO:0065010": "extracellular membrane-bounded organelle",
    "GO:0043230": "extracellular organelle",
}
MEMBRANE = "GO:0016020"
UNSET = {None, "PENDING"}
RULE_V_FROM = {"UNDECIDED", "MARK_AS_OVER_ANNOTATED"} | UNSET
RULE_M_FROM = {"KEEP_AS_NON_CORE", "UNDECIDED"} | UNSET

NOTE_V = (
    "OMICS_EVIDENCE disposition (2026-10-06): a vesicle-type location (exosome, "
    "extracellular vesicle, microparticle) from a bulk vesicle or body-fluid proteome "
    "records detection in secreted cargo, not where the protein acts, so it is kept as "
    "non-core by default (previous action: {old}). See projects/OMICS_EVIDENCE.md."
)
NOTE_M = (
    "OMICS_EVIDENCE disposition (2026-10-06): UniProt records no transmembrane segment, "
    "lipid anchor or membrane-protein topology for this protein, so the generic "
    "located_in membrane from a membrane-fraction proteome is treated as "
    "over-annotation (previous action: {old}). See projects/OMICS_EVIDENCE.md."
)


def subcellular_location_text(uniprot_text: str) -> str:
    """The CC SUBCELLULAR LOCATION block(s) of a UniProt flat file, joined into one string.

    >>> subcellular_location_text("CC   -!- SUBCELLULAR LOCATION: Cell membrane;\\nCC       Single-pass.\\nCC   -!- PTM: x\\n")
    'Cell membrane; Single-pass.'
    """
    out, inside = [], False
    for line in uniprot_text.split("\n"):
        if line.startswith("CC   -!- "):
            inside = line.startswith("CC   -!- SUBCELLULAR LOCATION:")
            if inside:
                out.append(line[len("CC   -!- SUBCELLULAR LOCATION:"):].strip())
        elif inside and line.startswith("CC       "):
            out.append(line[9:].strip())
        else:
            inside = False
    return " ".join(out)


def has_membrane_anchor(uniprot_text: str) -> bool:
    """True if a UniProt flat file records any membrane anchor or membrane association.

    Anchors: FT TRANSMEM / INTRAMEM / LIPID features; KW Transmembrane, Lipoprotein,
    GPI-anchor. Association: any membrane named in the SUBCELLULAR LOCATION block
    ("Cell membrane", "Endoplasmic reticulum membrane", "Peripheral membrane protein").
    The rule only targets proteins with no documented membrane association at all.

    >>> has_membrane_anchor("FT   TRANSMEM        10..30\\n")
    True
    >>> has_membrane_anchor("CC   -!- SUBCELLULAR LOCATION: Cytoplasm.\\n")
    False
    >>> has_membrane_anchor("CC   -!- SUBCELLULAR LOCATION: Peroxisome membrane.\\n")
    True
    >>> has_membrane_anchor("CC   -!- FUNCTION: Binds membrane proteins.\\nCC   -!- SUBCELLULAR LOCATION: Nucleus.\\n")
    False
    """
    if re.search(r"^FT   (TRANSMEM|INTRAMEM|LIPID) ", uniprot_text, re.M):
        return True
    kw = " ".join(re.findall(r"^KW   (.*)$", uniprot_text, re.M))
    if re.search(r"\b(Transmembrane|Lipoprotein|GPI-anchor)\b", kw):
        return True
    return "membrane" in subcellular_location_text(uniprot_text).lower()


def block_end(lines: list[str], start: int, indent: int) -> int:
    """Index of the first line after `start` that is non-blank and indented <= indent."""
    i = start + 1
    while i < len(lines):
        s = lines[i]
        if s.strip() and (len(s) - len(s.lstrip(" "))) <= indent:
            return i
        i += 1
    return i


def render_reason(indent: int, text: str) -> list[str]:
    """Render `reason:` as a block scalar that parses back to exactly `text`."""
    pad = " " * (indent + 2)
    if "\n" in text:
        body = [pad + ln if ln else "" for ln in text.split("\n")]
        return [" " * indent + "reason: |-"] + body
    wrapped = textwrap.wrap(text, width=96, break_long_words=False, break_on_hyphens=False)
    return [" " * indent + "reason: >-"] + [pad + ln for ln in wrapped]


def edit_file(path: str, changes: list[tuple[int, str, str]]) -> str:
    """Return new text for `path` with (annotation index, new action, new reason) applied.

    Locates each annotation's review block by walking `existing_annotations` items in
    order; raises if the text layout is not the expected block style.
    """
    lines = open(path).read().split("\n")
    # positions of existing_annotations items ("- " at the list's indent)
    ea = next(i for i, ln in enumerate(lines) if ln.startswith("existing_annotations:"))
    # the list may sit at column 0 ("- term:"), so the section ends at the next
    # top-level key, not at the next column-0 line
    end_ea = next((i for i in range(ea + 1, len(lines))
                   if re.match(r"^[A-Za-z_]", lines[i])), len(lines))
    item_starts = []
    item_indent = None
    for i in range(ea + 1, end_ea):
        m = re.match(r"^( *)- ", lines[i])
        if m and (item_indent is None or len(m.group(1)) == item_indent):
            if item_indent is None:
                item_indent = len(m.group(1))
            item_starts.append(i)
    item_starts.append(end_ea)
    n_items = len(yaml.load("\n".join(lines), Loader=LOADER)["existing_annotations"])
    if len(item_starts) - 1 != n_items:
        raise ValueError(f"found {len(item_starts) - 1} list items, expected {n_items}")
    # apply bottom-up so earlier line numbers stay valid
    for idx, new_action, new_reason in sorted(changes, key=lambda c: -c[0]):
        s, e = item_starts[idx], item_starts[idx + 1]
        rv = next(i for i in range(s, e) if re.match(r"^ *review:\s*$", lines[i]))
        rv_indent = len(lines[rv]) - len(lines[rv].lstrip(" "))
        rv_end = block_end(lines, rv, rv_indent)
        key_indent = rv_indent + 2
        act = next((i for i in range(rv + 1, rv_end)
                    if re.match(rf"^ {{{key_indent}}}action:", lines[i])), None)
        rea = next((i for i in range(rv + 1, rv_end)
                    if re.match(rf"^ {{{key_indent}}}reason:", lines[i])), None)
        new_reason_lines = render_reason(key_indent, new_reason)
        if rea is not None:
            rea_end = block_end(lines, rea, key_indent)
            lines[rea:rea_end] = new_reason_lines
        if act is not None:
            lines[act] = " " * key_indent + f"action: {new_action}"
        else:
            lines.insert(rv + 1, " " * key_indent + f"action: {new_action}")
        if rea is None:
            act = next(i for i in range(rv + 1, block_end(lines, rv, rv_indent))
                       if re.match(rf"^ {{{key_indent}}}action:", lines[i]))
            lines[act + 1:act + 1] = new_reason_lines
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true", help="edit files (default: dry run)")
    args = ap.parse_args()

    changed_rows, accepted_vesicle, accepted_membrane, skipped, failed = [], [], [], [], []
    files_changed = 0
    for path in sorted(glob.glob(os.path.join(ROOT, "genes", "*", "*", "*-ai-review.yaml"))):
        text = open(path).read()
        if not (any(t in text for t in VESICLE_TERMS) or MEMBRANE in text):
            continue
        doc = yaml.load(text, Loader=LOADER) or {}
        org, gene = path.split(os.sep)[-3], path.split(os.sep)[-2]
        uni_path = os.path.join(os.path.dirname(path), f"{gene}-uniprot.txt")
        anchor = has_membrane_anchor(open(uni_path).read()) if os.path.exists(uni_path) else None
        changes = []
        for idx, a in enumerate(doc.get("existing_annotations") or []):
            if a.get("evidence_type") not in CODES or a.get("negated"):
                continue
            tid = (a.get("term") or {}).get("id")
            rv = a.get("review") or {}
            old = rv.get("action")
            base = {"organism": org, "gene": gene, "term": f"{tid} {(a.get('term') or {}).get('label')}",
                    "evidence_type": a.get("evidence_type"), "reference": a.get("original_reference_id")}
            if tid in VESICLE_TERMS:
                if old == "ACCEPT":
                    accepted_vesicle.append(base)
                if old in RULE_V_FROM:
                    new, note = "KEEP_AS_NON_CORE", NOTE_V
                else:
                    continue
            elif tid == MEMBRANE:
                if anchor is None:
                    skipped.append({**base, "why": "no UniProt file"})
                    continue
                if anchor:
                    continue
                if old == "ACCEPT":
                    accepted_membrane.append(base)
                if old not in RULE_M_FROM:
                    continue
                new, note = "MARK_AS_OVER_ANNOTATED", NOTE_M
            else:
                continue
            reason = (str(rv.get("reason") or "").strip())
            new_reason = (reason + " " if reason else "") + note.format(old=old or "unset")
            changes.append((idx, new, new_reason))
            changed_rows.append({**base, "rule": "V" if tid in VESICLE_TERMS else "M",
                                 "old_action": old or "unset", "new_action": new})
        if not changes:
            continue
        try:
            new_text = edit_file(path, changes)
        except (ValueError, StopIteration):
            new_text = None
        # verify: parse result must equal original parse with only intended changes
        expect = copy.deepcopy(doc)
        for idx, new, new_reason in changes:
            r = expect["existing_annotations"][idx].setdefault("review", {})
            r["action"], r["reason"] = new, new_reason
        got = yaml.load(new_text, Loader=LOADER) if new_text is not None else None
        if got != expect:
            failed.append(os.path.relpath(path, ROOT))
            changed_rows = [r for r in changed_rows if not (r["organism"] == org and r["gene"] == gene)]
            continue
        files_changed += 1
        if args.write:
            with open(path, "w") as fh:
                fh.write(new_text)

    summary = Counter((r["rule"], r["old_action"], r["new_action"]) for r in changed_rows)
    print(f"{'WROTE' if args.write else 'DRY RUN'}: {len(changed_rows)} rows in {files_changed} files")
    for (rule, old, new), n in sorted(summary.items()):
        print(f"  rule {rule}: {old:24s} -> {new:24s} {n}")
    print(f"vesicle rows left as ACCEPT: {len(accepted_vesicle)}")
    print(f"no-anchor membrane rows left as ACCEPT: {len(accepted_membrane)}")
    print(f"membrane rows skipped (no UniProt file): {len(skipped)}")
    print(f"files failing the parse check (not edited): {len(failed)}")
    for f in failed:
        print(f"  {f}")
    if args.write:
        with open(AUDIT, "w") as fh:
            fh.write("# Generated by apply_dispositions.py -- audit of the 2026-10-06 batch\n")
            yaml.safe_dump({"rules": {"V": NOTE_V.format(old="X"), "M": NOTE_M.format(old="X")},
                            "changed_rows": changed_rows,
                            "vesicle_rows_left_as_accept": accepted_vesicle,
                            "no_anchor_membrane_rows_left_as_accept": accepted_membrane,
                            "membrane_rows_skipped_no_uniprot": skipped,
                            "files_failing_parse_check": failed},
                           fh, sort_keys=False, width=120, allow_unicode=True)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
