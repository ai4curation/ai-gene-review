"""Lint the ACTA1 review's load-bearing claims against their computed sources.

The dominant failure mode in this campaign is not a wrong term or a fake quote: it
is one claim asserted at several sites and corrected at all but one of them. Quote
validation cannot catch that, because every individual quote stays verbatim - the
error is in the joins. So the claims that appear in more than one place are checked
here, mechanically, against the JSON that produced them.

Scope is every prose surface a claim can hide on: the review YAML, the notes, and
RESULTS.md. Run with --self-test to confirm the checks actually fire.

    uv run python genes/human/ACTA1/ACTA1-bioinformatics/audit_claims.py
    uv run python genes/human/ACTA1/ACTA1-bioinformatics/audit_claims.py --self-test
"""
import argparse
import collections
import csv
import re
import json
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
GENE = HERE.parent
SURFACES = {
    "review": GENE / "ACTA1-ai-review.yaml",
    "notes": GENE / "ACTA1-notes.md",
    "results": HERE / "RESULTS.md",
}
PEPTIDES = HERE / "peptide_specificity.json"
WITHFROM = HERE / "withfrom_resolution.json"
NUCLEOTIDE = HERE / "nucleotide_terms_in_family.json"
GOA = GENE / "ACTA1-goa.tsv"

# Prose spells small counts as words; the lint compares against both forms.
WORDS = {10: "ten", 11: "eleven", 24: "twenty-four", 8: "eight", 5: "five", 3: "three"}

# Phrasings that were WRONG at some point in this review's history. If any
# reappears anywhere, an edit has regressed. Each records what replaced it.
RETRACTED = {
    "Comparison of alpha-skeletal and alpha-cardiac actin expression":
        "PMID:16288873's title, written from memory; the real title begins 'Defining alpha-skeletal'",
    "20 / 24": "an undercount of the GO:0015629 donors caused by a silent QuickGO zero; it is 24/24",
    "| MARK_AS_OVER_ANNOTATED | 19 |":
        "a stale action tally from before the GO:0005829 rows were made consistent; it is 16",
    "| KEEP_AS_NON_CORE | 10 |": "a stale action tally; it is 13",
    "3 CDH1 Reactome cytosol": "implies a split verdict on GO:0005829; all eight rows are KEEP_AS_NON_CORE",
    "residues 1 to 30": "the ORF N-terminus; ACTA1's mature chain starts at residue 3, so the observable region is 3-30",
    "MCDEDETTALVCDNGSGLVK": "an ORF peptide that does not exist in vivo (INIT_MET removed, Cys-2 cleaved by ACTMAP)",
    "cross-linked between Lys-52 and Glu-272": "stated as fact; both CROSSLNK features are ECO:0000250 from beta-actin",
    "533 PTHR11937 protein members":
        "unqualified; the list is InterPro's reviewed-only subset, ~0.6% of 88,887 proteins",
    "sole holder of ADP binding in the entire family":
        "not what was measured; the measurement covers 533 reviewed entries only",
    "one of only two gene products in this family carrying both":
        "a sibling's ATP-binding list relayed as a two-term count; measured, 31 carry ATP binding and ACTA1 alone carries ADP binding",
}


def flatten(text: str) -> str:
    """Collapse whitespace runs to single spaces.

    Load-bearing. Both the review YAML and the markdown wrap prose, so a claim like
    "9 of ACTA1's 63 peptides" routinely straddles a newline; matching the raw text
    reported such claims as absent when they were present, which is the same
    false-negative shape as a silent zero. Also undoes YAML's doubled-apostrophe
    escaping so a quoted scalar matches the same string as the markdown.
    """
    text = text.replace("''", "'")
    # Strip quotation marks and normalise dashes. Load-bearing for the RETRACTED check,
    # not cosmetic: the reviewer found that a retracted phrase survived in a post-mortem
    # because an embedded quotation mark split the matched substring - i.e. the guard was
    # evadable by punctuation, which is worse than no guard because it still reports OK.
    text = text.replace('"', "").replace("\u201c", "").replace("\u201d", "")
    text = text.replace("\u2018", "").replace("\u2019", "'")
    text = text.replace("\u2014", "-").replace("\u2013", "-")
    return re.sub(r"\s+", " ", text)


def load_surfaces() -> dict[str, str]:
    out = {}
    for name, path in SURFACES.items():
        if not path.exists():
            raise SystemExit(f"missing surface {path}")
        out[name] = flatten(path.read_text())
    return out


def required_claims() -> list[tuple[str, str, int]]:
    """(claim string, why it is load-bearing, minimum occurrences across all surfaces).

    Values come from the JSON outputs, never from literals here, so a recomputation
    that changes a number makes this lint fail rather than silently disagree.
    """
    pep = json.loads(PEPTIDES.read_text())
    wf = json.loads(WITHFROM.read_text())
    rows = {r["goa_row"]: r for r in wf["rows"]}
    ident = pep["pairwise_identity_pct"]

    n_unique = pep["n_unique_to_subject"]
    n_total = pep["n_subject_peptides_in_window"]
    n_regions = pep["n_independent_distinguishing_regions"]
    n_cyto = pep["n_shared_with_cytoplasmic_actins"]
    pct_shared = round(100.0 * pep["n_shared"] / n_total, 1)

    r1, r2 = rows[1], rows[2]
    claims = [
        (f"{ident['ACTA1|ACTA2']} per cent identical",
         "the reason an ISS between alpha-actins carries no isoform information", 1),
        (f"{ident['ACTA1|ACTA2']}%",
         "same identity figure, stated in the markdown surfaces", 1),
        (f"{n_unique} of ACTA1's {n_total}",
         "the HDA verdicts rest on this fraction", 1),
        (f"{n_regions} independent", "the collapsed region count, not the raw peptide count", 2),
        (f"{n_cyto} of", "peptides shared with the ubiquitous cytoplasmic actins", 1),
        (f"{pct_shared} per cent", "the shared fraction as quoted in the review reasons", 1),
        (f"{r1['n_with_own_experimental']} / {r1['n_protein_sources']}",
         "GO:0015629 donors with their own experimental evidence", 1),
        ((f"| {r2['n_protein_sources']} | **{r2['n_with_own_experimental']} / "
          f"{r2['n_protein_sources']}**",
          f"all {WORDS[r2['n_with_own_experimental']]} carry their own experimental",
          f"all {r2['n_with_own_experimental']} carry their own experimental"),
         "GO:0005200 donors, the basis of the headline ACCEPT", 1),
        ("P08023", "the chicken ACTA2 donor accession behind the five REMOVEs", 3),
        ("P68139", "chicken's own ACTA1: the ortholog that should have been used", 3),
        ("eight descendant nodes", "the IRD negation count that places ACTA1 on the accepting side", 2),
        ("PTN000940351", "the conventional-actin node asserting GO:0005200", 3),
        ("PTN000233075", "the self-referential PAN-GO node behind the stress fiber row", 3),
        # Minimums are SURFACE counts. These two are review-and-notes claims: the Reactome
        # generic-polymer finding and the IntAct MI-score are curation evidence, not outputs
        # of any script in this directory, so requiring them in RESULTS.md would be requiring
        # the wrong thing - and padding RESULTS.md to satisfy a lint is how a lint starts
        # shaping the prose instead of checking it. They were only ever reaching 3 because
        # the old check summed occurrences across surfaces.
        ("F-actin (all)", "Reactome's generic polymer, on the review and the notes", 2),
        ("0.56", "the IntAct MI-score shared by all seven two-hybrid partners", 2),
    ]
    if NUCLEOTIDE.exists():
        nt = json.loads(NUCLEOTIDE.read_text())
        atp, adp = nt["n_reviewed_with_atp_binding"], nt["n_reviewed_with_adp_binding"]
        claims += [
            ((f"{atp} reviewed members carry", f"| **{atp}** |"),
             "reviewed family members carrying GO:0005524, the figure that replaced a "
             "relayed claim", 1),
            ((f"exactly {adp} carries", f"**{adp}** carries `GO:0043531`"),
             "ACTA1 is the sole ADP binding holder among reviewed members", 1),
            # The scope qualifier must travel with the number, on every surface. A count
            # over 533 reviewed entries restated as a fact about an 88,887-protein family
            # is the error this pins. The phrase is deliberately specific - a bare
            # "reviewed" already occurs for unrelated reasons and would pass vacuously.
            (f"{nt['n_reviewed_members_queried']} reviewed",
             "the subset qualifier bound to the member count, on review/notes/RESULTS", 3),
            # Pin the DENOMINATOR too. Last round I pinned the numerator's scope and left
            # the family total hand-typed in prose, so a refreshed member list would move
            # the JSON and fire the 533 guard while 88,887 and the derived 0.6% went stale
            # in silence - the same numerator/denominator asymmetry that motivated parsing
            # it in the script, fixed in one place and not the other.
            ((f"{nt['n_proteins_in_family_per_panther_metadata']:,}",
              str(nt["n_proteins_in_family_per_panther_metadata"])),
             "the family protein total, which the prose states alongside the 533", 3),
            (f"{nt['fraction_of_family_measured'] * 100:.1f}",
             "the derived percentage of the family actually measured", 2),
        ]
    return claims


def action_counts() -> collections.Counter:
    """Read actions from the YAML on disk, never from the flattened prose copy."""
    doc = yaml.safe_load(SURFACES["review"].read_text())
    return collections.Counter(a["review"]["action"] for a in doc["existing_annotations"])


def duplicate_key_problems() -> list[str]:
    """Detect duplicated mapping keys in the review YAML.

    PyYAML keeps the LAST of a duplicated key, so a second ``supported_by:`` under one
    review silently deletes the first one's entries. Nothing else in this repo can see
    it: the quote checker and both validators walk the *parsed* document, so a quote
    that parsing already removed is simply not there to fail. Checked two ways - a
    strict loader that rejects duplicates outright, and a raw-versus-parsed count of
    provenance entries.
    """
    problems: list[str] = []
    path = SURFACES["review"]
    raw = path.read_text()

    class Strict(yaml.SafeLoader):
        pass

    def construct_mapping(loader, node, deep=False):
        keys = [loader.construct_object(k, deep=deep) for k, _ in node.value]
        dups = [k for k, c in collections.Counter(keys).items() if c > 1]
        if dups:
            raise RuntimeError(
                f"duplicate mapping key(s) {dups} near line {node.start_mark.line + 1}"
            )
        return yaml.SafeLoader.construct_mapping(loader, node, deep)

    Strict.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, construct_mapping)
    try:
        yaml.load(raw, Loader=Strict)
    except RuntimeError as exc:
        problems.append(f"duplicate YAML key: {exc}")

    # Independent cross-check. `- reference_id:` counts provenance entries; note that
    # `original_reference_id:` also contains the substring "reference_id:", which is why
    # the pattern is anchored to the list-item form.
    raw_n = len(re.findall(r"^\s*- reference_id:", raw, flags=re.M))
    doc = yaml.safe_load(raw)
    parsed_n = 0

    def walk(o):
        nonlocal parsed_n
        if isinstance(o, dict):
            for k, v in o.items():
                if k == "supported_by" and isinstance(v, list):
                    parsed_n += len(v)
                walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)

    walk(doc)
    if raw_n != parsed_n:
        problems.append(
            f"provenance entries: {raw_n} '- reference_id:' lines in the raw file but "
            f"{parsed_n} after parsing - a duplicated key has silently dropped "
            f"{raw_n - parsed_n} entry/entries"
        )
    return problems


def check(surfaces: dict[str, str]) -> list[str]:
    problems: list[str] = []
    blob = "\n".join(surfaces.values())

    for phrase, why in RETRACTED.items():
        where = [n for n, t in surfaces.items() if phrase in t]
        if where:
            problems.append(f"RETRACTED phrasing {phrase!r} reappeared in {where}: {why}")

    for claim, why, minimum in required_claims():
        # A claim may be given as a tuple of equivalent phrasings; prose legitimately
        # spells a small count as a word in one place and a digit in another, and a
        # lint that insists on one spelling reports a false positive rather than a
        # regression. Satisfied if ANY variant reaches the minimum.
        variants = claim if isinstance(claim, tuple) else (claim,)
        # Count SURFACES that contain the claim, not total occurrences summed across them.
        # Summing defeats the whole point of this lint: P08023 occurs 13/2/2 across the
        # three surfaces, so a minimum of 3 was satisfied 17 times over and would still
        # have passed with every mention deleted from the review YAML - which is exactly
        # the corrected-at-all-but-one-site failure the module docstring is about.
        present = [n for n, t in surfaces.items() if any(v in t for v in variants)]
        if len(present) < minimum:
            missing = sorted(set(surfaces) - set(present))
            problems.append(
                f"claim {variants!r} is on {len(present)} surface(s) {sorted(present)}, "
                f"expected >= {minimum}; missing from {missing} ({why})"
            )

    # The action tally in the notes must match the YAML it describes.
    counts = action_counts()
    for action, n in counts.items():
        if action == "NEW":
            continue
        row = f"| {action} | {n} |"
        if row not in surfaces["notes"]:
            problems.append(
                f"notes action summary disagrees with the YAML: expected row {row!r} "
                f"({action} appears {n}x in existing_annotations)"
            )

    # Row coverage: non-NEW annotations must equal the GOA row count.
    with GOA.open() as fh:
        goa_rows = sum(1 for _ in csv.DictReader(fh, delimiter="\t"))
    non_new = sum(v for k, v in counts.items() if k != "NEW")
    if non_new != goa_rows:
        problems.append(
            f"coverage: {non_new} non-NEW annotations against {goa_rows} GOA rows"
        )
    if counts.get("PENDING"):
        problems.append(f"{counts['PENDING']} annotation(s) still PENDING")
    if f"{goa_rows} GOA rows" not in blob:
        problems.append(f"no surface states the GOA row count ({goa_rows} GOA rows)")
    problems.extend(duplicate_key_problems())

    if NUCLEOTIDE.exists():
        nt = json.loads(NUCLEOTIDE.read_text())
        if not nt.get("subject_is_sole_adp_holder_among_reviewed"):
            problems.append(
                "nucleotide_terms_in_family.json no longer shows ACTA1 as the sole ADP "
                "binding holder among reviewed members, which the GO:0043531 reason asserts"
            )
        # The measurement covers the reviewed subset only; if a future run silently widened
        # to the whole family the prose qualifier would become wrong rather than merely
        # conservative, so pin the scope too.
        if nt.get("n_reviewed_members_queried") != 533:
            problems.append(
                f"reviewed member count is {nt.get('n_reviewed_members_queried')}, not the "
                "533 the review's prose states; update both together"
            )
    return problems


def self_test() -> None:
    """Break each class of check and require it to fire.

    A passing self-test proves the checks I thought of work; it cannot tell me which
    check I failed to write. So each case names the real regression it stands for.
    """
    surfaces = load_surfaces()
    assert not check(surfaces), f"baseline must be clean, got {check(surfaces)}"
    print("self-test 0 OK: baseline is clean")

    # 1. A retracted phrasing creeping back in (the PMID:16288873 title error).
    mutated = dict(surfaces)
    bad = "Comparison of alpha-skeletal and alpha-cardiac actin expression"
    mutated["notes"] = surfaces["notes"] + f"\n{bad} in human skeletal and cardiac muscle.\n"
    got = check(mutated)
    assert any("RETRACTED" in p for p in got), got
    print("self-test 1 OK: retracted phrasing detected")

    # 2. A required claim deleted from every surface (a number silently dropped).
    mutated = {k: v.replace("P68139", "REDACTED") for k, v in surfaces.items()}
    assert mutated != surfaces, "mutation did not apply - has the token changed?"
    got = check(mutated)
    assert any("P68139" in p for p in got), got
    print("self-test 2 OK: missing required claim detected")

    # 3. The notes tally drifting from the YAML (the fixed-in-N-1-places failure).
    counts = action_counts()
    stale = f"| MARK_AS_OVER_ANNOTATED | {counts['MARK_AS_OVER_ANNOTATED']} |"
    assert stale in surfaces["notes"], f"anchor {stale!r} absent; cannot exercise case 3"
    mutated = dict(surfaces)
    mutated["notes"] = surfaces["notes"].replace(stale, "| MARK_AS_OVER_ANNOTATED | 99 |")
    got = check(mutated)
    assert any("action summary disagrees" in p for p in got), got
    print("self-test 3 OK: notes/YAML tally drift detected")

    print("\nall self-tests passed")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    if args.self_test:
        self_test()
        return
    problems = check(load_surfaces())
    if problems:
        for p in problems:
            print(f"FAIL {p}", file=sys.stderr)
        raise SystemExit(f"{len(problems)} claim problem(s)")
    print("OK: all load-bearing claims agree across the review, notes and RESULTS.md")


if __name__ == "__main__":
    main()
