"""Check every load-bearing number in the ACTRT3 review and notes against results.json.

The recurring failure in this campaign is not a wrong term or a fabricated quote; it is a
number asserted in prose drifting from the number the analysis computed, or a claim fixed in
N places landing in N-1. Quote validation cannot catch either, because each constituent string
is verbatim and the error is in the join.

Design note, and the reason this file looks the way it does. The first version of this script
checked that a phrase such as `"18 of 38"` appeared at least N times. Deliberately corrupting
one instance of it in the review did NOT fail the audit, because the phrase occurred more than
N times elsewhere and the count never dropped below the floor. That is the same shape of bug as
a detector and a mutator disagreeing on scope: the verification was not weak, it was blind to
the class of thing being damaged.

So this version does not count phrases. For each quantity it matches a **context pattern with
the number as a capture group**, and asserts that *every* match in the text carries the value
computed in results.json. A changed digit then fails wherever it occurs and however many other
occurrences remain. `min_hits` guards the opposite failure, a claim being deleted outright.

Two checks in total:

  1. PATTERNS: every numeric match of a context must equal the computed value, and the context
     must appear at least `min_hits` times.
  2. RETRACTED: phrasings an earlier draft contained and this one rejects must be absent.

Run after any edit to the review or the notes:  uv run python audit_claims.py
Every failure is printed rather than raised on the first, so one run shows the whole picture.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
GENE_DIR = HERE.parent
REVIEW = GENE_DIR / "ACTRT3-ai-review.yaml"
NOTES = GENE_DIR / "ACTRT3-notes.md"
RESULTS = HERE / "results.json"
WITHFROM = HERE / "withfrom.json"

ACTRT3 = "Q9BYD9"


def require(path: Path, fix: str) -> Path:
    if not path.exists():
        raise FileNotFoundError(f"missing required input {path}\n  regenerate with: {fix}")
    return path


def norm(text: str) -> str:
    """Collapse whitespace AND strip markdown emphasis.

    Whitespace collapsing alone let a retracted phrasing survive: the notes wrote it as
    `**IPI twice**`, and the asterisks defeated a plain substring test on "IPI twice". A
    retraction guard that any emphasis can bypass is not a guard.
    """
    return re.sub(r"\s+", " ", text.replace("**", "").replace("*", "").replace("`", ""))


def compat(tally: dict) -> int:
    """Chemically compatible contacts: identical plus conservative substitutions."""
    return tally.get("identical", 0) + tally.get("conservative", 0)


WORDS = {2: "two", 8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve",
         13: "thirteen", 14: "fourteen", 15: "fifteen"}


def word(n: int) -> str:
    if n not in WORDS:
        raise RuntimeError(
            f"the prose spells {n} as an English word but this audit has no spelling for it; "
            "extend WORDS and re-read the affected sentences"
        )
    return WORDS[n]


def main() -> int:
    require(RESULTS, "uv run python analyze_actrt3.py")
    require(WITHFROM, "uv run python resolve_withfrom.py")
    require(REVIEW, "just fetch-gene human ACTRT3")
    require(NOTES, "hand-written; see ACTRT3-notes.md")

    r = json.loads(RESULTS.read_text())
    wf = json.loads(WITHFROM.read_text())
    review = norm(REVIEW.read_text())
    notes = norm(NOTES.read_text())
    both = review + " \n " + notes

    ns, ps, fs = (r["nucleotide_site"]["summary"], r["profilin_interface"]["summary"],
                  r["filament_interface"]["summary"])
    n_nuc, n_pro, n_fil = ns["n_contacts"], ps["n_contacts"], fs["n_contacts"]
    paint = r["paint_go0005200"]
    n_rejected = len(paint["rejected_at"])
    rejected_genes = sorted({g for row in paint["rejected_at"] for g in row["human_targets"]})
    n_genes = len(rejected_genes)
    rel = r["relatives"]["summary"]
    mouse = r["mouse_orthologue"]
    ident_actb = r["donating_nodes"]["summary"]["ACTRT3_identity_to_ACTB_pct"]

    def donors(row: int) -> int:
        rec = next(x for x in wf if x["row"] == row)
        return sum(1 for s in rec["sources"] if s["kind"] == "protein")

    # Guards on phrasings that collapse two proteins into one number. If the two stop
    # agreeing, the sentence is wrong even though no single number changed.
    coupled = [
        ("filament interface, 'the dynactin Arp1 paralogues'", compat(fs["P61163"]), compat(fs["P42025"])),
        ("profilin surface, 'Arp53D and Arp1'", compat(ps["P45891"]), compat(ps["P61163"])),
        ("filament interface, 'ACTA1/ACTC1'", compat(fs["P68133"]), compat(fs["P68032"])),
        ("filament interface, 'ACTB/ACTG1'", compat(fs["P60709"]), compat(fs["P63261"])),
        ("nucleotide site, 'beta-actin and Drosophila Arp53D'", compat(ns["P60709"]), compat(ns["P45891"])),
    ]

    # (label, pattern, expected tuple, haystack, min_hits)
    P: list[tuple[str, str, tuple, str, int]] = [
        # --- the three headline tallies. Every id/cons/non-cons/gap quadruple in the review
        #     must be one of the three the analysis produced for ACTRT3.
        ("filament, 'N of the M computed F-actin'",
         r"(\d+) of the (\d+) computed F-actin protomer-interface contacts",
         (compat(fs[ACTRT3]), n_fil), review, 1),
        ("filament, 'only N of M protomer-interface contacts'",
         r"only (\d+) of (\d+) protomer-interface contacts", (compat(fs[ACTRT3]), n_fil), review, 1),
        ("filament, 'N of M contacts compatible'",
         r"(\d+) of (\d+) contacts compatible", (compat(fs[ACTRT3]), n_fil), review, 1),
        ("filament, 'only N of M protomer-interface contacts' (notes)",
         r"(\d+) of (\d+) protomer-interface contacts", (compat(fs[ACTRT3]), n_fil), both, 3),
        ("filament, 'above ACTL8's N of M'",
         r"ACTL8's (\d+) of (\d+)", (compat(fs["Q9H568"]), n_fil), review, 1),
        ("filament, 'Arp3 scores N of M and Arp2 K'",
         r"Arp3 scores (\d+) of (\d+) and Arp2 (\d+)",
         (compat(fs["P61158"]), n_fil, compat(fs["P61160"])), review, 1),
        ("filament, 'K for the divergent but polymerising Arp53D'",
         r"(\d+) for the divergent but polymerising Arp53D", (compat(fs["P45891"]),), review, 1),
        ("filament, 'K for the dynactin Arp1 paralogues'",
         r"(\d+) for the dynactin Arp1 paralogues", (compat(fs["P61163"]),), review, 1),
        ("filament, 'against K for the weakest ... that does polymerise'",
         r"against (\d+) for the weakest actin-fold protein that does polymerise",
         (compat(fs["P61163"]),), review, 1),
        ("filament, 'well below the K of the weakest polymerising'",
         r"well below the (\d+) of the weakest polymerising", (compat(fs["P61163"]),), review, 1),
        ("filament, 'against K for Drosophila Arp53D and J for the dynactin Arp1'",
         r"against (\d+) for Drosophila Arp53D and (\d+) for the dynactin Arp1",
         (compat(fs["P45891"]), compat(fs["P61163"])), review, 1),

        # --- nucleotide site
        ("nucleotide, 'N of M computed beta-actin ATP and cation contacts'",
         r"(\d+) of (\d+) computed beta-actin ATP and cation contacts",
         (compat(ns[ACTRT3]), n_nuc), review, 1),
        ("nucleotide, 'N of M nucleotide-site contacts'",
         r"(\d+) of (\d+) nucleotide-site contacts", (compat(ns[ACTRT3]), n_nuc), review, 1),
        ("nucleotide, 'N of M computed ATP/cation contacts'",
         r"(\d+) of (\d+) computed ATP/cation contacts", (compat(ns[ACTRT3]), n_nuc), review, 1),
        ("nucleotide, 'N of M contacts are chemically compatible' (notes)",
         r"(\d+) of (\d+) contacts are chemically compatible", (compat(ns[ACTRT3]), n_nuc), notes, 1),

        # --- profilin surface
        ("profilin, 'N of those M contacts as chemically compatible ... comparators'",
         r"(\d+) of those (\d+) contacts as chemically compatible, against (\d+) for beta-actin, "
         r"(\d+) for Arp53D and Arp1, (\d+) for ACTL8 and (\d+) for ACTR10",
         (compat(ps[ACTRT3]), n_pro, compat(ps["P60709"]), compat(ps["P45891"]),
          compat(ps["Q9H568"]), compat(ps["Q9NZ32"])), review, 1),
        ("profilin, 'N of M contacts, and across the ARP-T clade'",
         r"(\d+) of (\d+) contacts, and across the ARP-T clade", (compat(ps[ACTRT3]), n_pro),
         review, 1),
        ("profilin, 'N of the M residues by which beta-actin contacts profilin'",
         r"(\d+) of the (\d+) residues by which beta-actin contacts profilin",
         (compat(ps[ACTRT3]), n_pro), review, 1),
        # The clade rankings are quoted verbatim from RESULTS.md as supporting_text, so the
        # whole row is reconstructed from results.json below in RANKING_ROWS rather than
        # pattern-matched here; a bare `ACTRT1 N, ACTRT2 N, ACTRT3 N` is ambiguous across the
        # three contact sets and matching it caused a false failure on the first run.

        # --- the trio, in the redundancy-experiment sentence
        ("trio, 'nucleotide site A, B and C of M'",
         r"nucleotide site (\d+), (\d+) and (\d+) of (\d+)",
         (compat(ns[ACTRT3]), compat(ns["Q8TDY3"]), compat(ns["Q8TDG2"]), n_nuc), review, 1),
        ("trio, 'protomer interface A, B and C of M'",
         r"protomer interface (\d+), (\d+) and (\d+) of (\d+)",
         (compat(fs[ACTRT3]), compat(fs["Q8TDG2"]), compat(fs["Q8TDY3"]), n_fil), review, 1),

        # --- identities
        ("identity, 'at N per cent to beta-actin' (ACTRT3 vs ACTB)",
         r"at ([\d.]+) per cent to beta-actin", (ident_actb,), review, 1),
        ("identity, 'against N per cent to beta-actin' (mouse Actrt3 vs ACTB)",
         r"against ([\d.]+) per cent to beta-actin",
         (mouse["local_identity_to_ACTB"]["pct_identity_over_aligned_block"],), review, 1),
        ("identity, 'N per cent globally identical'",
         r"([\d.]+) per cent globally identical",
         (mouse["global_identity_to_human_ACTRT3"]["pct_identity"],), review, 2),
        ("identity, 'N per cent identical to human ACTRT3'",
         r"([\d.]+) per cent identical to the human protein",
         (mouse["global_identity_to_human_ACTRT3"]["pct_identity"],), review, 1),
        ("identity, 'N per cent local identity to beta-actin'",
         r"([\d.]+) per cent local identity to beta-actin",
         (mouse["local_identity_to_ACTB"]["pct_identity_over_aligned_block"],), review, 1),

        # --- PAINT negation survey, in both digit and word spellings
        ("PAINT, 'negated it at WORD descendant nodes covering WORD human genes'",
         r"negated it at (\w+) descendant nodes covering (\w+) human genes",
         (word(n_rejected), word(n_genes)), review, 1),
        ("PAINT, 'negated at WORD descendant nodes covering WORD human genes'",
         r"negated at (\w+) descendant nodes covering (\w+) human genes",
         (word(n_rejected), word(n_genes)), review, 1),
        ("PAINT, 'covering N human genes' (digits, in a source_entities comment)",
         r"covering (\d+) human genes", (n_genes,), review, 1),
        ("PAINT, 'N human genes across M clades' (notes)",
         r"(\d+) human genes across (\d+) clades", (n_genes, n_rejected), notes, 1),
        ("PAINT, 'negated ... at WORD of its descendant nodes'",
         r"negated this same term at (\w+) of its descendant nodes", (word(n_rejected),), review, 1),

        # --- relatives census
        ("census, 'ACTL8 carries N IBA rows; ACTRT3 carries M'",
         r"ACTL8 carries (\d+) IBA rows; ACTRT3 carries (\d+)",
         (rel["ACTL8_iba_rows"], rel["ACTRT3_iba_rows"]), both, 1),
        ("census, 'median across the other seven divergent relatives is N'",
         r"median across the other seven divergent relatives is (\d+)",
         (int(rel["median_iba_rows_excluding_ACTL8"]),), both, 1),

        # --- WITH/FROM donor counts
        ("donors, 'All N protein donors on the GO:0015629 row and all M on the GO:0005200 row'",
         r"All (\d+) protein donors on the GO:0015629 row and all (\d+) on the GO:0005200 row",
         (donors(1), donors(2)), both, 2),
        ("donors, 'whose N protein donors are M conventional actins'",
         r"whose (\d+) protein donors are (\d+) conventional actins", (donors(1), donors(1) - 1),
         review, 1),
        ("donors, 'N/N carry their own' (notes)",
         r"(\d+)/(\d+) carry their own", (donors(1), donors(1)), notes, 1),
        ("donors, 'Row 1 carries **N** tokens (M protein donors + one PANTHER node)'",
         r"Row 1 carries (\d+) tokens \((\d+) protein donors",
         (donors(1) + 1, donors(1)), notes, 1),
        ("donors, 'same N WITH/FROM tokens'",
         r"same (\d+) WITH/FROM tokens", (donors(1) + 1,), review, 1),
        ("donors, 'PTN000940351 (IBD, date, N seeds)'",
         r"IBD, 2025-08-05, (\d+) seeds", (donors(2),), review, 1),
        ("donors, 'All N carry their own experimental evidence' for row 2",
         r"all (\d+) donors carry their own experimental evidence", (donors(2),), review, 1),
    ]

    # --- reference-scope figures, from reference_scope.json rather than typed.
    #     Looked up through a helper that names the missing key, because indexing the dict by a
    #     hardcoded PMID raised a bare KeyError when the file was regenerated with a different
    #     citation set - an unhelpful failure for a script whose job is clear failure.
    scope_path = HERE / "reference_scope.json"
    problems_early: list[str] = []
    if not scope_path.exists():
        problems_early.append(
            f"missing {scope_path}; regenerate with: uv run python reference_scope.py")
    else:
        sc = json.loads(scope_path.read_text())

        def ref(pmid: str) -> dict:
            if pmid not in sc:
                raise RuntimeError(
                    f"reference_scope.json has no block for PMID:{pmid}; it holds "
                    f"{sorted(sc)}. Either the review stopped citing it or the audit needs "
                    "updating - re-run reference_scope.py and re-read the affected prose."
                )
            return sc[pmid]

        bioplex, theca, prof = ref("33961781"), ref("35793634"), ref("18692047")

        def entity_count(block: dict, go_id: str, why: str) -> int | None:
            """Distinct-entity count, or None with a recorded problem.

            Records rather than raises: this script's contract is that one run prints every
            failure, and raising here aborted the remaining patterns so a second, unrelated
            drift would stay hidden until the first was fixed.
            """
            if not block.get("entities_per_term_available"):
                problems_early.append(
                    f"PMID:{block['pmid']} no longer yields a distinct-entity count per term "
                    f"(rows_complete is false, i.e. the row list is a sample), so {why} is "
                    "unsupported: an annotation count is not an entity count. Re-run "
                    "reference_scope.py and re-read the affected prose rather than substituting "
                    "the annotation count."
                )
                return None
            if go_id not in block["entities_per_term"]:
                problems_early.append(
                    f"PMID:{block['pmid']} no longer annotates {go_id}; {why} must be re-read. "
                    f"Terms present: {sorted(block['entities_per_term'])}"
                )
                return None
            return block["entities_per_term"][go_id]

        theca_pt = entity_count(theca, "GO:0033011",
                                "the prose's '12 mouse perinuclear-theca proteins'")
        theca_pheno = entity_count(theca, "GO:0007286", "the projection argument")
        prof_pb = entity_count(prof, "GO:0005515", "the annotations-versus-entities sentence")
        # Entity-count patterns are added only where the count is available; the absence is already
        # recorded above, so skipping here loses nothing and keeps the remaining checks running.
        if theca_pt is not None:
            P.extend([
                ("scope, theca proteins carrying GO:0033011 IDA",
                 r"carries GO:0033011 by IDA for (\d+) mouse perinuclear-theca proteins",
                 (theca_pt,), review, 1),
                ("scope, theca proteins named in the notes table",
                 r"by IDA for (\w+) mouse theca proteins", (word(theca_pt),), notes, 1),
            ])
        if prof_pb is not None:
            P.append(
                ("scope, profilin GO:0005515 annotations vs entities (the double-logging itself)",
                 r"(\d+) protein-binding annotations spread over only (\d+) entities",
                 (prof["true_annotations_per_term"].get("GO:0005515", "MISSING"), prof_pb),
                 review, 1))
        # rows_complete is the property entity counting actually needs; term-list closure is
        # weaker and was the wrong gate. Both are asserted so a regression in either is visible.
        def flag(block: dict, field: str, want, why: str) -> None:
            """Assert a JSON field without direct indexing, so a renamed or dropped field is
            reported by name rather than raising KeyError -- the same reason entity_count()
            uses .get()."""
            if field not in block:
                problems_early.append(
                    f"PMID:{block.get('pmid', '?')} has no '{field}' field; reference_scope.py's "
                    f"output shape changed and {why} can no longer be checked")
            elif block[field] != want:
                problems_early.append(
                    f"PMID:{block.get('pmid', '?')}: {field} is {block[field]!r}, expected "
                    f"{want!r} - {why}")

        flag(theca, "rows_complete", True,
             "its entity counts would be a lower bound and the '12 proteins' sentence would rest "
             "on a sample")
        flag(theca, "term_list_provably_complete", True,
             "the projection verdict on it would rest on a partial term list")
        flag(theca, "projecting_database_rows", [],
             "the review states this reference has no projecting-database rows")
        flag(bioplex, "assigning_databases_provably_complete", True,
             "the review's 'sum exactly to the total' sentence would be unproven")
        P.extend([
            ("scope, theca reference distinct entities",
             r"reference annotates (\d+) entities across (\d+) terms",
             (theca["distinct_entities_seen"], len(theca["true_annotations_per_term"])),
             review, 1),
            ("scope, BioPlex total annotations",
             r"PMID:33961781 accounts for (\d+) GOA annotations",
             (bioplex["total_annotations"],), review, 1),
            ("scope, BioPlex exact protein-binding count",
             r"of which (\d+) are GO:0005515 itself",
             (bioplex["true_annotations_per_term"].get("GO:0005515", "MISSING"),), review, 1),
            ("scope, BioPlex per-database split",
             r"\(IntAct (\d+), ComplexPortal (\d+)\)",
             (bioplex["true_annotations_per_db"].get("IntAct", "MISSING"),
              bioplex["true_annotations_per_db"].get("ComplexPortal", "MISSING")), review, 1),
            ("scope, profilin reference entity count",
             r"yields (\d+) annotations across just (\d+) entities",
             (prof["total_annotations"], prof["distinct_entities_seen"]), review, 1),
        ])
        # The projection argument on the two GO:0033011 ACCEPTs depends on three properties of
        # PMID:35793634. If any changes, the prose must be re-read rather than the number bumped.
        if theca_pheno is not None and theca_pheno != 1:
            problems_early.append(
                "PMID:35793634's GO:0007286 row no longer covers exactly one entity; the "
                "'not a projection' argument on the GO:0033011 rows depends on it")
        # And the BioPlex reference's projection tail is asserted in the review, so it must exist.
        if not bioplex["projecting_database_rows"]:
            problems_early.append(
                "the review states PMID:33961781 carries a ComplexPortal projection tail, but "
                "reference_scope.json no longer finds one")

    # Phrasings an earlier draft contained; each was a real error, so each stays retracted.
    RETRACTED = [
        "23 protein tokens",
        "23/23 carry their own",
        "22 conventional actins",
        "same 24 WITH/FROM tokens",
        "eleven human genes",
        "covering 11 human genes",
        "11 human genes across",
        # Read as two experiments; it is one co-IP logged by two databases and reciprocally on
        # both partners. Kept SHORT on purpose: the first version retracted the whole sentence
        # "by IPI twice from PMID:18692047", which a reworded or **emphasised** variant walked
        # straight past. The claim being retracted is the word "twice", so that is what is banned.
        "IPI twice",
    ]

    ranking = r["divergent_clade_ranking"]
    sym = ranking["accession_to_symbol"]
    RANKING_ROWS: list[tuple[str, str]] = []
    for setname, block in ranking["per_contact_set"].items():
        cells = ", ".join(f"{sym[a]} {v}" for a, v in
                          block["compatible_identical_plus_conservative"])
        RANKING_ROWS.append((setname, f"| {setname} | {block['n_contacts']} | {cells} |"))

    problems: list[str] = []
    problems.extend(problems_early)

    for setname, row_text in RANKING_ROWS:
        if norm(row_text) not in review:
            problems.append(
                f"RANKING ROW NOT QUOTED ({setname}): the review does not contain the row this "
                f"run computes: {row_text}"
            )

    # The prose enumerates by name the human genes PAINT has withdrawn GO:0005200 from, and the
    # count and the enumeration are separate claims that can drift apart -- the first version of
    # this audit had a correct enumeration and a wrong total. Both are checked, and this loop is
    # what catches a name silently dropping out of the list.
    for gene in rejected_genes:
        if gene not in review:
            problems.append(
                f"GENE MISSING FROM ENUMERATION: {gene} is one of the {n_genes} human genes at a "
                "GO:0005200-rejected node but is not named anywhere in the review"
            )
    # and the reverse: the un-adjudicated set the recommendation is addressed to
    still_holding = ["ACTL9", "ACTL10", "ACTRT1", "ACTRT2", "ACTRT3"]
    for gene in still_holding:
        if gene not in review:
            problems.append(f"GENE MISSING: {gene} is in the un-adjudicated set but is not named")

    for label, expected_a, expected_b in coupled:
        if expected_a != expected_b:
            problems.append(
                f"COUPLED VALUES DIVERGED ({label}): {expected_a} vs {expected_b}; the prose "
                "quotes them as a single number and must be split"
            )

    n_value_checks = 0
    for label, pattern, expected, hay, min_hits in P:
        want = tuple(str(x) for x in expected)
        hits = re.findall(pattern, hay)
        if len(hits) < min_hits:
            problems.append(f"MISSING ({label}): pattern found {len(hits)}x, need >={min_hits}")
            continue
        for h in hits:
            got = (h,) if isinstance(h, str) else tuple(h)
            n_value_checks += 1
            if got != want:
                problems.append(f"WRONG VALUE ({label}): text says {got}, computed {want}")

    for phrase in RETRACTED:
        if norm(phrase) in both:
            problems.append(f"RETRACTED PHRASING STILL PRESENT: {phrase!r}")

    # The MODIFY argument depends on ACTRT3's own path being un-adjudicated. If PAINT
    # reaches the ARP-T branch, the reasoning must be rewritten rather than the number bumped.
    if paint["actrt3_go0005200_rejected_anywhere_on_its_path"]:
        problems.append(
            "PAINT has now rejected GO:0005200 on ACTRT3's own path "
            f"({paint['actrt3_go0005200_rejected_anywhere_on_its_path']}); the MODIFY reasoning "
            "must be rewritten, because the row would already be blocked upstream"
        )

    for p in problems:
        print(p)
    print(f"\naudited {len(P)} patterns ({n_value_checks} numeric matches), "
          f"{len(RANKING_ROWS)} clade-ranking rows, {len(coupled)} coupling guards, "
          f"{len(RETRACTED)} retracted phrasings: {len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
