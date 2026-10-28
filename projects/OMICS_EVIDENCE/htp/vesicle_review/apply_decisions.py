"""Apply the manual vesicle-row decisions to the gene reviews.

Pass 1 (default): decisions_draft.py over dossiers.yaml, writing decisions.yaml.
Pass 2 (--settled): decisions_settled.py over dossiers_settled.yaml, writing
decisions_settled.yaml.

A decisions module supplies G (one decision per protein), and may supply SUPERSEDED
(genes whose rows a later, separate review has taken over; recorded but not edited), R (per-row
overrides keyed by (gene, row_index), for proteins whose rows need different calls or
row-specific wording) and S (supported_by entries, by reference_id, to drop from a row
because they argued for the action this review overturned).

A row whose decision differs from its pre-review action gets the decision, a reason made
of the reviewer's basis plus a dated provenance note, a summary matching the decision, and
the S drops. A row whose decision equals its pre-review action but which an earlier run of
this script changed is restored to its pre-review action and reason. Re-running is a no-op;
the mechanics (textual edit, parse check) are in ../apply_dispositions.py.

Usage:  python3 projects/OMICS_EVIDENCE/htp/vesicle_review/apply_decisions.py [--settled] [--write]
"""

from __future__ import annotations

import argparse
import csv
import os
import re
import subprocess
import sys
from collections import Counter, defaultdict
from functools import cache

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))
sys.path.insert(0, os.path.dirname(HERE))
sys.path.insert(0, HERE)
from apply_dispositions import LOADER, VESICLE_TERMS, apply_row_targets  # noqa: E402

NOTE = "(Manual re-review for OMICS_EVIDENCE, 2026-10-10; previous action: {old}.)"
MARKER = "Manual re-review for OMICS_EVIDENCE, 2026-10-10"
SUMMARY = {
    "KEEP_AS_NON_CORE": "Detected in an extracellular-vesicle proteome. The protein is plausible EV content, "
                        "but this is not where it functions.",
    "MARK_AS_OVER_ANNOTATED": "Detected in an extracellular-vesicle proteome, but the detection does not "
                              "establish that this protein is an EV constituent.",
    "ACCEPT": "The protein is an established EV marker incorporated by the EV biogenesis machinery; the "
              "vesicle location is supported.",
}


def base_summary(path: str, idx: int, ann: dict) -> str | None:
    """The row's summary as it was before this project, read from the merge base with main."""
    rel = os.path.relpath(path, ROOT)
    base = subprocess.run(["git", "merge-base", "HEAD", "origin/main"], cwd=ROOT, capture_output=True,
                          text=True, check=True).stdout.strip()
    text = subprocess.run(["git", "show", f"{base}:{rel}"], cwd=ROOT, capture_output=True, text=True,
                          check=True).stdout
    old = yaml.load(text, Loader=LOADER)["existing_annotations"][idx]
    assert (old["term"]["id"], old.get("original_reference_id")) == (
        ann["term"]["id"], ann.get("original_reference_id")), (path, idx)
    return old["review"].get("summary")


# CAT5's last clause is a per-protein factual claim; check it against the gene's own GOA rows
# and UniProt FUNCTION text instead of trusting the decision file.
NO_BINDING = "record no experimental proteoglycan, heparin or lipid binding"
EXPERIMENTAL = {"EXP", "IDA", "IPI", "IMP", "IGI", "IEP", "IC", "TAS", "HTP", "HDA", "HMP", "HGI", "HEP"}
# lipid binding, glycosaminoglycan binding, proteoglycan binding, lipoprotein particle binding,
# lipid transfer activity, lipid chaperone activity, and their is_a descendants
BINDING_ROOTS = ["GO:0008289", "GO:0005539", "GO:0043394", "GO:0071813", "GO:0120013", "GO:7770043"]
# GO files these outside the roots: hyaluronic acid binding is_a carboxylic acid binding only
BINDING_EXTRA = {"GO:0005540"}
LIPID = (r"lipid|lipoprotein|heparin|heparan|glycosaminoglycan|proteoglycan|hyaluron|chondroitin|dermatan|"
         r"keratan|phosphatid|ganglioside|sphingo|ceramide|sterol|fatty acid|retinol|cardiolipin")
UNIPROT_BINDS = re.compile(rf"\bbind(s|ing)?\b[^.]*\b({LIPID})", re.I)
HEDGE = re.compile(r"\b(may|might|probably|possibly|could|potential|putative)\b", re.I)


@cache
def binding_ids() -> frozenset[str]:
    from oaklib import get_adapter
    from oaklib.datamodels.vocabulary import IS_A
    go = get_adapter("sqlite:obo:go")
    ids = frozenset(go.descendants(BINDING_ROOTS, predicates=[IS_A])) | BINDING_EXTRA
    # a root missing from the loaded GO release would silently drop its whole branch
    assert set(BINDING_ROOTS) <= ids, f"GO release lacks {set(BINDING_ROOTS) - ids}"
    return ids


def binding_evidence(organism: str, gene: str, codes: frozenset[str] | set[str] = EXPERIMENTAL) -> list[str]:
    # the loose EXPERIMENTAL set is conservative for CAT5's negative clause; the positive CAT5_BOUND
    # claim cites direct assays, so it is checked with the narrow set
    folder = os.path.join(ROOT, "genes", organism, gene)
    with open(os.path.join(folder, f"{gene}-goa.tsv")) as fh:
        hits = {f'{r["GO TERM"]} {r["GO NAME"]} ({r["GO EVIDENCE CODE"]})'
                for r in csv.DictReader(fh, delimiter="\t")
                if r["GO ASPECT"] == "molecular_function" and "NOT" not in r["QUALIFIER"]
                and r["GO EVIDENCE CODE"] in codes and r["GO TERM"] in binding_ids()}
    uniprot = os.path.join(folder, f"{gene}-uniprot.txt")
    assert os.path.exists(uniprot), f"{gene}: no cached UniProt entry to check the CAT5 clause against"
    with open(uniprot) as fh:
        text = re.sub(r"\s+", " ", " ".join(line[5:] for line in fh if line.startswith("CC   ")))
    for block in re.findall(r"-!- FUNCTION: (.*?)(?= -!- |$)", text):
        # unhedged sentences only: "May act as a carrier of hyaluronan" does not count
        hits.update(f"UniProt: {sentence}" for sentence in re.split(r"(?<=\.) ", block)
                    if UNIPROT_BINDS.search(sentence) and not HEDGE.search(sentence))
    return sorted(hits)


# CAT4's claim that the protein's own review keeps no experimental surface pool, checked the same way.
SURFACE_CLAIM = "its own review keeps no experimental cell-surface or plasma-membrane pool"
SURFACE_POOL_CLAIM = "plasma-membrane pool that its own review keeps"
BOUND_CLAIM = "promiscuous (proteoglycan, lipid) receptors on the EV surface, so the detection is plausible"
SURFACE_TERMS = {"GO:0009986", "GO:0005886"}
SURFACE_EVIDENCE = {"EXP", "IDA", "IMP", "IPI"}


@cache
def surface_ids() -> frozenset[str]:
    """Cell surface and plasma membrane with their is_a/part_of descendants (e.g. external side of plasma membrane)."""
    from oaklib import get_adapter
    from oaklib.datamodels.vocabulary import IS_A, PART_OF
    ids = frozenset(get_adapter("sqlite:obo:go").descendants(sorted(SURFACE_TERMS), predicates=[IS_A, PART_OF]))
    assert SURFACE_TERMS <= ids, f"GO release lacks {SURFACE_TERMS - ids}"
    return ids


def surface_rows(organism: str, gene: str) -> list[str]:
    path = os.path.join(ROOT, "genes", organism, gene, f"{gene}-ai-review.yaml")
    anns = yaml.load(open(path).read(), Loader=LOADER)["existing_annotations"]
    return sorted({f'{a["term"]["id"]} {a.get("evidence_type")} {a.get("original_reference_id")}' for a in anns
                   if a["term"]["id"] in surface_ids() and a.get("evidence_type") in SURFACE_EVIDENCE
                   and not a.get("negated") and a["review"].get("action") in ("ACCEPT", "KEEP_AS_NON_CORE", "MODIFY")})


# CAT1's claim that the protein spans or is lipid-anchored in a membrane, checked against UniProt features.
ANCHOR_CLAIM = "Transmembrane/lipid-anchored protein"
ANCHOR_FEATURE = re.compile(r"^FT   (TRANSMEM|INTRAMEM|LIPID) |^CC .*GPI-anchor", re.M)


def has_anchor(organism: str, gene: str) -> bool:
    with open(os.path.join(ROOT, "genes", organism, gene, f"{gene}-uniprot.txt")) as fh:
        return bool(ANCHOR_FEATURE.search(fh.read()))


# CAT2's attribution of the cytosolic location, checked against its stated source.
CYTO_UNIPROT = "Cytosolic protein (UniProt)"
CYTO_GO = "Cytosolic protein (GO cytosol or cytoplasm annotation)"


def uniprot_cytosolic(organism: str, gene: str) -> bool:
    return bool(re.search(r"cytoplasm|cytosol", uniprot_locations(organism, gene), re.I))


def go_cytosolic(organism: str, gene: str) -> bool:
    with open(os.path.join(ROOT, "genes", organism, gene, f"{gene}-goa.tsv")) as fh:
        return any(r["GO TERM"] in ("GO:0005829", "GO:0005737") and "NOT" not in r["QUALIFIER"]
                   for r in csv.DictReader(fh, delimiter="\t"))


# CAT1's compartment, checked against its cited source: UniProt location text, or GO rows (is_a/part_of
# closure of plasma membrane, cell surface and endosome).
CAT1_UNIPROT = "plasma membrane or endosomal system (UniProt);"
CAT1_GO_SOURCE = "compartment from GO"
PM_ENDOSOME_TEXT = re.compile(r"cell membrane|plasma membrane|endosom|lysosom|multivesicular|apical cell|basolateral cell|"
                              r"cell surface|membrane raft", re.I)


def uniprot_locations(organism: str, gene: str) -> str:
    with open(os.path.join(ROOT, "genes", organism, gene, f"{gene}-uniprot.txt")) as fh:
        text = re.sub(r"\s+", " ", " ".join(line[5:] for line in fh if line.startswith("CC   ")))
    return " ".join(re.findall(r"-!- SUBCELLULAR LOCATION:(.*?)(?= -!- |$)", text))


@cache
def pm_endosome_ids() -> frozenset[str]:
    from oaklib import get_adapter
    from oaklib.datamodels.vocabulary import IS_A, PART_OF
    roots = ["GO:0005886", "GO:0009986", "GO:0005768"]
    ids = frozenset(get_adapter("sqlite:obo:go").descendants(roots, predicates=[IS_A, PART_OF]))
    assert set(roots) <= ids, f"GO release lacks {set(roots) - ids}"
    return ids


def go_pm_endosome(organism: str, gene: str) -> bool:
    with open(os.path.join(ROOT, "genes", organism, gene, f"{gene}-goa.tsv")) as fh:
        return any(r["GO TERM"] in pm_endosome_ids() and "NOT" not in r["QUALIFIER"]
                   for r in csv.DictReader(fh, delimiter="\t"))


# CAT4's residency claim and CAT2A's cytosolic/membrane-binding claim, checked against UniProt or GO.
RESIDENT_CLAIM = "Mainly resident in an intracellular compartment"
RESIDENT_TEXT = re.compile(r"nucleus|nuclear|mitochondri|endoplasmic|golgi|peroxisom|lipid droplet|sarcoplasmic", re.I)
RIBOSOMAL_CLAIM = "Ribosomal protein; MISEV2018"
CAT2A_CLAIM = "Cytosolic protein with lipid or membrane-protein binding ability"
CAT2A_TEXT = re.compile(r"cytoplasm|cytosol|peripheral membrane|lipid-anchor", re.I)


@cache
def closure(*roots: str) -> frozenset[str]:
    from oaklib import get_adapter
    from oaklib.datamodels.vocabulary import IS_A, PART_OF
    ids = frozenset(get_adapter("sqlite:obo:go").descendants(list(roots), predicates=[IS_A, PART_OF]))
    assert set(roots) <= ids, f"GO release lacks {set(roots) - ids}"
    return ids


def go_rows_in(organism: str, gene: str, ids: frozenset[str]) -> bool:
    # any non-NOT row: these clauses name a compartment, not the strength of the evidence for it
    with open(os.path.join(ROOT, "genes", organism, gene, f"{gene}-goa.tsv")) as fh:
        return any(r["GO TERM"] in ids and "NOT" not in r["QUALIFIER"] for r in csv.DictReader(fh, delimiter="\t"))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--settled", action="store_true", help="second pass: rows already KEEP_AS_NON_CORE")
    args = ap.parse_args()
    if args.settled:
        import decisions_settled as dm
        dossier_file, out_file, source = "dossiers_settled.yaml", "decisions_settled.yaml", "decisions_settled.py"
    else:
        import decisions_draft as dm
        dossier_file, out_file, source = "dossiers.yaml", "decisions.yaml", "decisions_draft.py"
    G, R, S = dm.G, getattr(dm, "R", {}), getattr(dm, "S", {})
    superseded = getattr(dm, "SUPERSEDED", {})
    dossiers = yaml.safe_load(open(os.path.join(HERE, dossier_file)))
    genes = {d["gene"] for d in dossiers}
    assert genes == set(G), f"missing: {genes - set(G)}; extra: {set(G) - genes}"
    rows = {(d["gene"], d["row_index"]) for d in dossiers}
    assert set(R) <= rows and set(S) <= rows, "overrides must name dossier rows"
    records, targets, parsed = [], defaultdict(list), {}
    for d in dossiers:
        key = (d["gene"], d["row_index"])
        action, basis = R.get(key, G[d["gene"]])
        if NO_BINDING in basis:
            hits = binding_evidence(d["organism"], d["gene"])
            assert not hits, f"{key}: CAT5 says no experimental lipid/proteoglycan binding, but found {hits}"
        if CYTO_UNIPROT in basis:
            assert uniprot_cytosolic(d["organism"], d["gene"]), f"{key}: CAT2 cites UniProt, which records no cytosol"
        if CYTO_GO in basis:
            assert go_cytosolic(d["organism"], d["gene"]), f"{key}: CAT2_GO cites GO, which records no cytosol"
        if "Secreted or lumenal protein (UniProt)" in basis:
            assert re.search(r"secreted|lumen|lysosom|extracellular", uniprot_locations(d["organism"], d["gene"]), re.I), \
                f"{key}: CAT5 cites UniProt, which records no secreted or lumenal location"
        if RESIDENT_CLAIM in basis:
            org, gene = d["organism"], d["gene"]
            assert RESIDENT_TEXT.search(uniprot_locations(org, gene)) or go_rows_in(org, gene, closure(
                "GO:0005634", "GO:0005739", "GO:0005783", "GO:0005794", "GO:0005777", "GO:0005811")), \
                f"{key}: CAT4 says intracellular resident, but neither UniProt nor GO records such a compartment"
        if CAT2A_CLAIM in basis:
            org, gene = d["organism"], d["gene"]
            assert CAT2A_TEXT.search(uniprot_locations(org, gene)) or go_rows_in(org, gene, closure(
                "GO:0005829", "GO:0005737")), f"{key}: CAT2A says cytosolic, but neither UniProt nor GO records it"
        if CAT1_UNIPROT in basis:
            assert PM_ENDOSOME_TEXT.search(uniprot_locations(d["organism"], d["gene"])), \
                f"{key}: CAT1 cites UniProt, which records no plasma-membrane or endosomal location"
        if CAT1_GO_SOURCE in basis:
            assert go_pm_endosome(d["organism"], d["gene"]), f"{key}: CAT1_GO cites GO, which records no such location"
        if ANCHOR_CLAIM in basis:
            assert has_anchor(d["organism"], d["gene"]), f"{key}: CAT1 says transmembrane/lipid-anchored, UniProt has no anchor"
        # the positive clauses of CAT5_BOUND and CAT4_SURFACE, checked the same way
        if BOUND_CLAIM in basis:
            assert any(not h.startswith("UniProt:") for h in
                       binding_evidence(d["organism"], d["gene"], SURFACE_EVIDENCE)), \
                f"{key}: CAT5_BOUND but no directly assayed (EXP/IDA/IMP/IPI) binding found"
        if RIBOSOMAL_CLAIM in basis:
            assert go_rows_in(d["organism"], d["gene"], closure("GO:0005840", "GO:0003735")), \
                f"{key}: CAT3B says ribosomal protein, but GO records no ribosome row"
        if SURFACE_POOL_CLAIM in basis:
            assert surface_rows(d["organism"], d["gene"]), f"{key}: CAT4_SURFACE but the review keeps no surface row"
        if SURFACE_CLAIM in basis:
            hits = surface_rows(d["organism"], d["gene"])
            assert not hits, f"{key}: CAT4 says no kept experimental surface pool, but the review keeps {hits}"
        old = d["current_action"]
        changed = action != old
        records.append({"gene": f'{d["organism"]}/{d["gene"]}', "row_index": d["row_index"], "term": d["term"],
                        "reference": d["reference"], "previous_action": old,
                        "decision": action, "changed": changed, "basis": basis})
        if d["gene"] in superseded:
            records[-1]["superseded_by"] = superseded[d["gene"]]
            continue
        path = os.path.join(ROOT, "genes", d["organism"], d["gene"], f'{d["gene"]}-ai-review.yaml')
        if path not in parsed:
            parsed[path] = yaml.load(open(path).read(), Loader=LOADER)["existing_annotations"]
        ann = parsed[path][d["row_index"]]
        assert ann["term"]["id"] in VESICLE_TERMS, (path, d["row_index"])
        rv = ann["review"]
        if changed:
            targets[path].append((d["row_index"], action, f"{basis} {NOTE.format(old=old)}",
                                  SUMMARY[action], set(S.get(key, []))))
        elif MARKER in str(rv.get("reason") or ""):
            # changed by an earlier run, now decided back to the pre-review action and reason.
            # Dropped supported_by entries are not restored here, so S must not name such a row.
            assert key not in S, f"{key}: S drop on a row decided back to its pre-review action"
            # A summary this script generated is put back to the pre-review one as well
            summary = rv.get("summary")
            if summary in SUMMARY.values():
                summary = base_summary(path, d["row_index"], ann)
            targets[path].append((d["row_index"], old, d["current_reason"], summary, set()))
    edited, failed = apply_row_targets(targets, args.write)
    moves = Counter((r["previous_action"], r["decision"]) for r in records if r["changed"])
    print(f"{'WROTE' if args.write else 'DRY RUN'}: {sum(1 for r in records if r['changed'])} of "
          f"{len(records)} rows differ from their pre-review action; {edited} files needed edits; "
          f"failed: {len(failed)}")
    for (a, b), n in sorted(moves.items(), key=lambda kv: -kv[1]):
        print(f"  {a:24s} -> {b:24s} {n}")
    print("final decisions:", dict(Counter(r["decision"] for r in records)))
    if args.write:
        with open(os.path.join(HERE, out_file), "w") as fh:
            fh.write(f"# Manual review of HTP-family vesicle-type rows, 2026-10-10. Source: {source}\n")
            yaml.safe_dump(records, fh, sort_keys=False, width=120, allow_unicode=True)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
