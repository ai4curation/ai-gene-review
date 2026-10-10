"""RETIRED batch-disposition script for OMICS_EVIDENCE; now a helper module.

Both rules below were applied on 2026-10-06 and withdrawn on 2026-10-10, and all their
edits were undone: a rule must not make curation calls. HTP-family rows are now reviewed
row by row from dossiers (membrane_review/, vesicle_review/). main() no longer edits
anything; the module is kept for its helpers (edit_file, render_reason, has_anchor_feature,
membrane_closure, membrane_annotations), which the review scripts import, and as a record
of what the rules did (audit files disposition-2026-10-06*.yaml).

  V. WITHDRAWN 2026-10-10. Vesicle-type location from a bulk vesicle/body-fluid proteome.
     Rows: evidence_type HDA or HTP, not negated, term in VESICLE_TERMS.
     Change: action UNDECIDED / MARK_AS_OVER_ANNOTATED / PENDING / unset -> KEEP_AS_NON_CORE.
     Left alone: ACCEPT and REMOVE (explicit protein-specific judgements; ACCEPT rows are
     listed in the audit for follow-up), KEEP_AS_NON_CORE (already compliant), MODIFY, NEW.

  M. WITHDRAWN 2026-10-10. A rule for generic `membrane` (GO:0016020) rows was applied
     on 2026-10-06, first with a label-text test and then with an identifier-based test
     (UniProt anchor features, or GOA rows to the GO:0016020 is_a/part_of closure). Both
     were still a rule deciding the outcome, with existing annotations treated as
     authoritative rather than as leads, so the rule was withdrawn, its edits undone, and
     every candidate row reviewed by hand: see membrane_review/ (build_dossiers.py,
     decisions_draft.py, apply_decisions.py, decisions.yaml). The helper functions
     below (has_anchor_feature, membrane_closure, membrane_annotations) remain because
     build_dossiers.py uses them to *gather* leads, not to decide.

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

import os
import re
import sys
import textwrap

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
    "OMICS_EVIDENCE disposition (2026-10-06): the protein has no membrane anchor among "
    "its UniProt features (transmembrane, intramembrane or lipidation) and no annotation "
    "outside high-throughput studies to membrane (GO:0016020) or any is_a/part_of "
    "descendant, so the generic located_in membrane from a membrane-fraction proteome is "
    "treated as over-annotation (previous action: {old}). See projects/OMICS_EVIDENCE.md."
)
# note written by the first, label-text-based run of rule M (see Revision above)
OLD_NOTE_M_RE = re.compile(
    r"\s*OMICS_EVIDENCE disposition \(2026-10-06\): UniProt records no transmembrane "
    r"segment.*?\(previous action: (\w+)\)\. See projects/OMICS_EVIDENCE\.md\.",
    re.S,
)
HTP_FAMILY = {"HDA", "HTP", "HMP", "HGI", "HEP"}
GO_ADAPTER = os.environ.get("OMICS_GO_ADAPTER", "sqlite:obo:go")


def has_anchor_feature(uniprot_text: str) -> bool:
    """True if a UniProt flat file has a structured membrane-anchor feature.

    >>> has_anchor_feature("FT   TRANSMEM        10..30\\n")
    True
    >>> has_anchor_feature("CC   -!- SUBCELLULAR LOCATION: Cell membrane.\\n")
    False
    """
    return bool(re.search(r"^FT   (TRANSMEM|INTRAMEM|LIPID) ", uniprot_text, re.M))


def membrane_closure() -> set[str]:
    """GO:0016020 and all its is_a/part_of descendants, from the GO ontology (OAK)."""
    from oaklib import get_adapter

    adapter = get_adapter(GO_ADAPTER)
    return set(adapter.descendants(MEMBRANE, predicates=["rdfs:subClassOf", "BFO:0000050"],
                                   reflexive=True))


def membrane_annotations(goa_path: str, closure: set[str]) -> list[str]:
    """Non-NOT, non-high-throughput GOA rows to a term in `closure`, as 'GO:id CODE ref'."""
    import csv

    out = []
    with open(goa_path, newline="") as fh:
        for r in csv.DictReader(fh, delimiter="\t"):
            if (r.get("GO TERM") in closure and not (r.get("QUALIFIER") or "").startswith("NOT")
                    and r.get("GO EVIDENCE CODE") not in HTP_FAMILY):
                out.append(f'{r["GO TERM"]} {r["GO EVIDENCE CODE"]} {r["REFERENCE"]}')
    return sorted(set(out))


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
    print("apply_dispositions.py is retired: rules V and M were withdrawn on 2026-10-10 and "
          "their edits undone. See membrane_review/ and vesicle_review/.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
