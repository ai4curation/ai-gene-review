"""Tests for the scope-table derivation behind `just panther-report-stats`.

The command exists because the report's table went stale four times. It then
acquired the most intricate logic in the CLI -- a PAINT-index join, an evidence
filter, a per-annotation aggregation, and a prefix-stripping trap that made the
first implementation print 52/45 instead of 100/76 -- with no test at all. Every
case below is one the command got wrong at some point, or one where getting it
wrong would change a published figure rather than crash.
"""

from pathlib import Path

import pytest
import yaml
from typer.testing import CliRunner

from ai_gene_review.cli import app

runner = CliRunner()


@pytest.fixture
def repo(tmp_path: Path) -> Path:
    """A minimal repo skeleton the command can be pointed at."""
    (tmp_path / "modules").mkdir()
    (tmp_path / "interpro" / "panther").mkdir(parents=True)
    (tmp_path / "interpro" / "panther" / "panther-members.tsv").write_text(
        "uniprot_accession\tpanther_family_sf\nP1\tPTHR1:SF1\n"
    )
    (tmp_path / "interpro" / "panther" / "panther.obo").write_text(
        "format-version: 1.2\nontology: panther\n"
    )
    return tmp_path


def write_slice(repo: Path, family: str, rows: list[tuple[str, str, str, str]]) -> None:
    """Write a PAINT slice; each row is (node, go_id, evidence, seeds)."""
    directory = repo / "interpro" / "panther" / family
    directory.mkdir(parents=True, exist_ok=True)
    lines = ["family\tnode\tgo_id\taspect\tevidence\tnegated\tseeds\ttaxon\tdate"]
    for node, go_id, evidence, seeds in rows:
        lines.append(f"{family}\t{node}\t{go_id}\tF\t{evidence}\tfalse\t{seeds}\t\t")
    (directory / f"{family}-paint.tsv").write_text("\n".join(lines) + "\n")


def write_module(repo: Path, name: str, nodes: list[str]) -> None:
    document = {
        "module": {
            "id": "m",
            "parts": [
                {
                    "node": {
                        "annotons": [
                            {
                                "participant": {
                                    "family": {
                                        "ancestral_nodes": [
                                            {
                                                "term": {
                                                    "id": n,
                                                    "label": n.split(":")[1],
                                                }
                                            }
                                            for n in nodes
                                        ]
                                    }
                                }
                            }
                        ]
                    }
                }
            ],
        }
    }
    (repo / "modules" / name).write_text(yaml.safe_dump(document))


def write_obo(repo: Path, subfamilies: dict[str, int]) -> None:
    """Write a PANTHER OBO with `count` subfamily stanzas per family.

    load_subfamily_counts counts `id: PANTHER:PTHRn:SFm` lines, and an empty OBO
    makes subfamily_precision_case return None on its first line -- which is why
    the precision rows read zero in every fixture until this existed.
    """
    lines = ["format-version: 1.2", "ontology: panther", ""]
    for family, count in subfamilies.items():
        lines += ["[Term]", f"id: PANTHER:{family}", f"name: {family} FAMILY", ""]
        for index in range(1, count + 1):
            lines += [
                "[Term]",
                f"id: PANTHER:{family}:SF{index}",
                f"name: {family} SUBFAMILY {index}",
                "",
            ]
    (repo / "interpro" / "panther" / "panther.obo").write_text("\n".join(lines))


def write_members(repo: Path, members: dict[str, str]) -> None:
    """Write the accession -> family:subfamily index."""
    rows = ["uniprot_accession\tpanther_family_sf"]
    rows += [f"{accession}\t{family}" for accession, family in members.items()]
    (repo / "interpro" / "panther" / "panther-members.tsv").write_text(
        "\n".join(rows) + "\n"
    )


def write_family_module(
    repo: Path, name: str, descriptors: list[tuple[list[str], list[str]]]
) -> None:
    """Write a module of family descriptors: (declared families, members)."""
    annotons = [
        {
            "participant": {
                "family": {
                    "term": {"id": families[0], "label": "F"},
                    "family_terms": [{"id": f, "label": "F"} for f in families[1:]],
                    "representative_members": [
                        {"term": {"id": f"UniProtKB:{a}", "label": a}} for a in accs
                    ],
                }
            }
        }
        for families, accs in descriptors
    ]
    document = {"module": {"id": "m", "parts": [{"node": {"annotons": annotons}}]}}
    (repo / "modules" / name).write_text(yaml.safe_dump(document))


def run(repo: Path) -> str:
    result = runner.invoke(app, ["panther-report-stats", "--output-dir", str(repo)])
    assert result.exit_code == 0, result.output
    return result.output


def test_counts_citations_and_distinct_nodes_separately(repo):
    """One node cited twice is 2 citations, 1 node -- the row rename's whole point."""
    write_slice(repo, "PTHR1", [("PTN1", "GO:1", "IBD", "UniProtKB:A|UniProtKB:B")])
    write_module(repo, "a.yaml", ["PANTHER:PTN1"])
    write_module(repo, "b.yaml", ["PANTHER:PTN1"])

    assert "| PAINT node citations | 2 (of 1 distinct nodes) |" in run(repo)


def test_seed_count_is_not_inflated_by_prefix_stripping(repo):
    """The bug that printed 52/45: unioning bare accessions with prefixed tokens.

    The seed set must straddle the threshold for this to bite. Two UniProt seeds
    count as 2 (thin); double-counted they become 4 (not thin), which is exactly
    how the original bug hid thin nodes. A 4-seed fixture would pass either way.
    """
    write_slice(repo, "PTHR1", [("PTN1", "GO:1", "IBD", "UniProtKB:A|UniProtKB:B")])
    write_module(repo, "a.yaml", ["PANTHER:PTN1"])

    assert "| PAINT annotations resting on <=3 seeds | 1 / 1 distinct" in run(repo)


def test_non_uniprot_seeds_are_counted(repo):
    """Seeds are counted as written, so a PANTHER-node seed is still a seed.

    Counting only `UniProtKB:` tokens is the error that reported 82 seeds as
    180; the guard against it must not swing the other way and discard them.
    """
    write_slice(
        repo,
        "PTHR1",
        [("PTN1", "GO:1", "IBD", "PANTHER:PTN9|PANTHER:PTN8|UniProtKB:A|UniProtKB:B")],
    )
    write_module(repo, "a.yaml", ["PANTHER:PTN1"])

    assert "| PAINT annotations resting on <=3 seeds | 0 / 1 distinct" in run(repo)


def test_thinness_is_per_annotation_not_pooled_across_rows(repo):
    """PTN000329346's shape: two 3-seed rows. Pooled reads 5-6; per-term reads 3.

    Both annotations are thin. Pooling would credit each with seeds that were
    never used together to infer it.
    """
    write_slice(
        repo,
        "PTHR1",
        [
            ("PTN1", "GO:1", "IBD", "UniProtKB:A|UniProtKB:B|UniProtKB:Q"),
            ("PTN1", "GO:2", "IBD", "UniProtKB:C|UniProtKB:D|UniProtKB:Q"),
        ],
    )
    write_module(repo, "a.yaml", ["PANTHER:PTN1"])

    assert "| PAINT annotations resting on <=3 seeds | 2 / 2 distinct" in run(repo)


def test_a_well_supported_sibling_does_not_rescue_a_thin_annotation(repo):
    """The quantifier the row label got wrong.

    Requiring EVERY annotation to be thin would report 0 here, even though the
    2-seed term is exactly the thinly-propagated claim the figure is about.
    """
    write_slice(
        repo,
        "PTHR1",
        [
            ("PTN1", "GO:1", "IBD", "|".join(f"UniProtKB:S{i}" for i in range(40))),
            ("PTN1", "GO:2", "IBD", "UniProtKB:A|UniProtKB:B"),
        ],
    )
    write_module(repo, "a.yaml", ["PANTHER:PTN1"])

    assert "| PAINT annotations resting on <=3 seeds | 1 / 2 distinct" in run(repo)


def test_distinct_and_citation_weighted_aggregations_differ(repo):
    """A node cited twice contributes its annotation twice to the weighted count."""
    write_slice(repo, "PTHR1", [("PTN1", "GO:1", "IBD", "UniProtKB:A")])
    write_module(repo, "a.yaml", ["PANTHER:PTN1"])
    write_module(repo, "b.yaml", ["PANTHER:PTN1"])

    assert (
        "| PAINT annotations resting on <=3 seeds | 1 / 1 distinct (node, term) "
        "= 2 / 2 citation-weighted |" in run(repo)
    )


def test_an_annotation_in_several_family_slices_counts_once(repo):
    """A node's annotation is committed once per family slice containing it.

    `PTN000010968`'s GO:0008168 sits in three committed slices, and
    load_paint_index appends across them. Counting rows let "how many slices we
    happened to commit" masquerade as citation frequency -- inflating the real
    denominator by 120 and, because duplicates are overwhelmingly thick,
    deflating the thin fraction from 40% to 37%. Every other fixture here
    writes a single family, so nothing else in this file reaches it.
    """
    row = ("PTN1", "GO:1", "IBD", "UniProtKB:A|UniProtKB:B")
    write_slice(repo, "PTHR1", [row])
    write_slice(repo, "PTHR2", [row])
    write_slice(repo, "PTHR3", [row])
    write_module(repo, "a.yaml", ["PANTHER:PTN1"])

    assert (
        "| PAINT annotations resting on <=3 seeds | 1 / 1 distinct (node, term) "
        "= 1 / 1 citation-weighted |" in run(repo)
    )


def test_duplicate_slices_with_divergent_seeds_are_reported(repo):
    """Dedup must not silently become glob-order-dependent.

    Copies are byte-identical today, so this cannot fire against real data --
    but a future PANTHER release shipping divergent copies would otherwise
    decide a published figure by directory iteration order.
    """
    # Slice order is load-bearing: load_paint_index reads sorted(), so the THIN
    # copy must come last. With the thick copy last, last-write-wins agrees with
    # max by coincidence and this test cannot tell them apart -- the first draft
    # was ordered that way and passed under the very bug it names.
    write_slice(
        repo,
        "PTHR1",
        [("PTN1", "GO:1", "IBD", "|".join(f"UniProtKB:S{i}" for i in range(9)))],
    )
    write_slice(repo, "PTHR2", [("PTN1", "GO:1", "IBD", "UniProtKB:A|UniProtKB:B")])
    write_module(repo, "a.yaml", ["PANTHER:PTN1"])

    output = run(repo)
    assert "differing seed counts across family slices" in output
    # Resolved to the better-supported copy, not to whichever was globbed last.
    assert "| PAINT annotations resting on <=3 seeds | 0 / 1 distinct" in output


def test_non_ibd_rows_are_excluded(repo):
    """The evidence filter is part of the definition, not an implementation detail."""
    write_slice(
        repo,
        "PTHR1",
        [
            ("PTN1", "GO:1", "IBD", "UniProtKB:A"),
            ("PTN1", "GO:2", "IRD", "UniProtKB:B"),
        ],
    )
    write_module(repo, "a.yaml", ["PANTHER:PTN1"])

    assert "| PAINT annotations resting on <=3 seeds | 1 / 1 distinct" in run(repo)


def test_single_subfamily_and_heterogeneity_rows(repo):
    """The precision rows, which read zero in every earlier fixture.

    PTHR1 is split into 20 subfamilies (the advisory threshold) with both members
    in one of them; PTHR2 into 3, so it counts toward the population but not the
    advisory. PTHR3's members are spread, so the family really is the level that
    covers them and it is not a precision case at all.
    """
    write_obo(repo, {"PTHR1": 20, "PTHR2": 3, "PTHR3": 5})
    write_members(
        repo,
        {
            "A": "PTHR1:SF1",
            "B": "PTHR1:SF1",
            "C": "PTHR2:SF2",
            "D": "PTHR3:SF1",
            "E": "PTHR3:SF2",
        },
    )
    write_family_module(
        repo,
        "a.yaml",
        [
            (["PANTHER:PTHR1"], ["A", "B"]),
            (["PANTHER:PTHR2"], ["C"]),
            (["PANTHER:PTHR3"], ["D", "E"]),
        ],
    )

    output = run(repo)
    assert "| declared at family level | 3 |" in output
    assert (
        "with all members in one subfamily | 2 / 3 checkable (of 3 declared) |"
        in output
    )
    assert "subfamilies (the advisory) | 1 |" in output


def test_a_subfamily_level_declaration_is_not_a_precision_case(repo):
    """Already at the sharper level, so there is nothing to narrow."""
    write_obo(repo, {"PTHR1": 20})
    write_members(repo, {"A": "PTHR1:SF1"})
    write_family_module(repo, "a.yaml", [(["PANTHER:PTHR1:SF1"], ["A"])])

    output = run(repo)
    assert "| declared at subfamily level | 1 |" in output
    # Subfamily-level declarations belong in neither half of the ratio.
    assert (
        "with all members in one subfamily | 0 / 0 checkable (of 0 declared) |"
        in output
    )


def test_a_two_family_descriptor_does_not_make_each_family_ambiguous(repo):
    """The misattribution: crediting every member to every declared family.

    peroxisome-lifecycle declares PTHR12652 and PTHR20990 together because
    PANTHER splits those paralogs -- and says so in its own prose. Unioning made
    each family look ambiguous on the other's proteins, counting the descriptors
    most explicit about the split as evidence that ids cannot distinguish
    between proteins. Only PTHR1 genuinely covers two.
    """
    write_obo(repo, {"PTHR1": 3, "PTHR2": 3})
    write_members(repo, {"A": "PTHR1:SF1", "B": "PTHR1:SF2", "C": "PTHR2:SF1"})
    write_family_module(
        repo, "a.yaml", [(["PANTHER:PTHR1", "PANTHER:PTHR2"], ["A", "B", "C"])]
    )

    assert "| family ids covering more than one distinct protein | 1 (over 2" in run(
        repo
    )


def test_a_member_outside_every_declared_family_still_counts(repo):
    """The UniProt/PAINT disagreement, which must not be dropped.

    P08887's sequence classification puts it in PTHR23036 while its PAINT node
    is in the declared PTHR23037. The index cannot settle it, so the module's
    grounding is the only claim available and the declared id is still being
    asked to cover the protein. Excluding it understated the row.
    """
    write_obo(repo, {"PTHR1": 3, "PTHR9": 3})
    write_members(repo, {"A": "PTHR1:SF1", "B": "PTHR9:SF1"})
    write_family_module(repo, "a.yaml", [(["PANTHER:PTHR1"], ["A", "B"])])

    assert "| family ids covering more than one distinct protein | 1 (over 2" in run(
        repo
    )


def test_the_divergence_note_prints_once_per_annotation(repo):
    """Not once per citation -- a node cited 29 times printed 29 identical notes."""
    write_slice(
        repo,
        "PTHR1",
        [("PTN1", "GO:1", "IBD", "|".join(f"UniProtKB:S{i}" for i in range(9)))],
    )
    write_slice(repo, "PTHR2", [("PTN1", "GO:1", "IBD", "UniProtKB:A|UniProtKB:B")])
    for name in ("a.yaml", "b.yaml", "c.yaml"):
        write_module(repo, name, ["PANTHER:PTN1"])

    output = run(repo)
    assert output.count("differing seed counts") == 1
    assert "| PAINT node citations | 3 (of 1 distinct nodes) |" in output


def test_grounding_inconsistent_descriptors_are_not_checkable(repo):
    """il6_signaling's shape: declared PTHR23037, member indexed in PTHR23036.

    It is family-level with a member in the index, so the earlier hand-rolled
    guard admitted it -- putting a correctness finding the sweep reports
    separately into the complement of a precision ratio. Worse, it is the very
    descriptor the attribution rule reasons about, so it was counted one way for
    the ambiguity row and another for the precision row.
    """
    write_obo(repo, {"PTHR1": 20, "PTHR9": 20})
    write_members(repo, {"A": "PTHR9:SF1"})
    write_family_module(repo, "a.yaml", [(["PANTHER:PTHR1"], ["A"])])

    output = run(repo)
    assert "| declared at family level | 1 |" in output
    assert (
        "with all members in one subfamily | 0 / 0 checkable (of 1 declared) |"
        in output
    )


def test_a_member_with_no_subfamily_is_not_checkable(repo):
    """No subfamily is recorded, so nothing exists to narrow to.

    dtdp_l_rhamnose_biosynthesis declares PTHR43000 whose sole member Q88LZ1 is
    indexed without a :SF; 20 rows of panther-members.tsv are this shape. The
    blank means the consulted source recorded no subfamily, not that PANTHER
    assigns none -- both resolution paths admit a bare row and the artifact does
    not say which produced one.
    """
    write_obo(repo, {"PTHR1": 20})
    write_members(repo, {"A": "PTHR1"})
    write_family_module(repo, "a.yaml", [(["PANTHER:PTHR1"], ["A"])])

    assert (
        "with all members in one subfamily | 0 / 0 checkable (of 1 declared) |"
        in run(repo)
    )


def test_members_spread_is_checkable_but_not_a_finding(repo):
    """The complement of the ratio must be exactly this population.

    Spread members mean the family really is the level that covers them -- a
    real answer to "could this be narrowed?", so it belongs in the denominator.
    """
    write_obo(repo, {"PTHR1": 20})
    write_members(repo, {"A": "PTHR1:SF1", "B": "PTHR1:SF2"})
    write_family_module(repo, "a.yaml", [(["PANTHER:PTHR1"], ["A", "B"])])

    assert (
        "with all members in one subfamily | 0 / 1 checkable (of 1 declared) |"
        in run(repo)
    )


def test_a_mixed_granularity_descriptor_is_not_checkable(repo):
    """Declaring both a family and a subfamily is already at the sharper level.

    The family/subfamily counters classify on the first sorted curie while the
    predicate rejects on any declared subfamily, so this shape could enter the
    denominator while being unreachable in the numerator. Nothing in the tree
    mixes granularity today; this pins the behaviour before something does.
    """
    write_obo(repo, {"PTHR1": 20})
    write_members(repo, {"A": "PTHR1:SF1"})
    write_family_module(
        repo, "a.yaml", [(["PANTHER:PTHR1", "PANTHER:PTHR1:SF1"], ["A"])]
    )

    assert "with all members in one subfamily | 0 / 0 checkable" in run(repo)


def test_a_member_with_no_subfamily_blocks_the_narrowing(repo):
    """histidine_catabolism's shape: some members placed, one not.

    Unplaced members were discarded before the count, so the remainder was
    reported as a clean finding and the advisory asserted "every representative
    member here is in SF1" about a member the index places in no subfamily. Two
    such descriptors sat inside the published advisory, recommending a narrowing
    that would drop the module's own exemplar.
    """
    write_obo(repo, {"PTHR1": 20})
    write_members(repo, {"A": "PTHR1:SF1", "B": "PTHR1:SF1", "C": "PTHR1"})
    write_family_module(repo, "a.yaml", [(["PANTHER:PTHR1"], ["A", "B", "C"])])

    output = run(repo)
    # Checkable -- narrowing has a real answer, and the answer is no.
    assert (
        "with all members in one subfamily | 0 / 1 checkable (of 1 declared) |"
        in output
    )
    assert "subfamilies (the advisory) | 0 |" in output


def test_members_sharing_one_subfamily_are_still_a_finding(repo):
    """Guards the miscount that read every shared subfamily as partial coverage.

    Comparing DISTINCT subfamilies against member count misreads three members
    in one subfamily as "some unassigned" -- it reported 91 such descriptors
    where there are 5, and silently cut the finding count by 79.
    """
    write_obo(repo, {"PTHR1": 20})
    write_members(repo, {"A": "PTHR1:SF1", "B": "PTHR1:SF1", "C": "PTHR1:SF1"})
    write_family_module(repo, "a.yaml", [(["PANTHER:PTHR1"], ["A", "B", "C"])])

    output = run(repo)
    assert (
        "with all members in one subfamily | 1 / 1 checkable (of 1 declared) |"
        in output
    )
    assert "subfamilies (the advisory) | 1 |" in output


def test_the_partition_row_covers_only_family_level_statuses(repo):
    """Declared-at-subfamily descriptors are excluded before the denominator.

    Listing them beside the family-level statuses mixed populations, and in the
    real tree they number 101 -- exactly the same as the rest of the 907 -- so a
    reader checking the arithmetic found it worked while the leading term came
    from a different set. Here PTHR2 is declared at subfamily level and must not
    appear in the row, whose total must equal the family-level non-findings.
    """
    write_obo(repo, {"PTHR1": 20, "PTHR2": 20, "PTHR9": 20})
    write_members(
        repo, {"A": "PTHR1:SF1", "B": "PTHR1:SF2", "C": "PTHR2:SF1", "D": "PTHR9:SF1"}
    )
    write_family_module(
        repo,
        "a.yaml",
        [
            (["PANTHER:PTHR1"], ["A", "B"]),  # members spread
            (["PANTHER:PTHR2:SF1"], ["C"]),  # declared at subfamily
            (["PANTHER:PTHR3"], ["D"]),  # grounding inconsistent
        ],
    )

    output = run(repo)
    row = next(
        line for line in output.splitlines() if "family-level ones are not" in line
    )
    # Assert against the row itself: "declared at subfamily" also appears in the
    # scope table's own count row, and a substring check over the whole output
    # would pass or fail for the wrong reason.
    assert row == (
        "| ...why the other 2 family-level ones are not | "
        "1 members spread, 1 grounding inconsistent |"
    )


def test_no_member_resolvable_is_not_checkable(repo):
    """A descriptor whose members are absent from the index cannot be judged."""
    write_obo(repo, {"PTHR1": 20})
    write_members(repo, {"Z": "PTHR1:SF1"})
    write_family_module(repo, "a.yaml", [(["PANTHER:PTHR1"], ["A"])])

    output = run(repo)
    assert (
        "with all members in one subfamily | 0 / 0 checkable (of 1 declared) |"
        in output
    )
    assert "1 no member resolvable" in output


def test_without_subfamily_data_nothing_is_checkable(repo):
    """No OBO means no subfamily counts, so the question cannot be put at all."""
    write_members(repo, {"A": "PTHR1:SF1"})
    write_family_module(repo, "a.yaml", [(["PANTHER:PTHR1"], ["A"])])

    output = run(repo)
    assert (
        "with all members in one subfamily | 0 / 0 checkable (of 1 declared) |"
        in output
    )
    assert "1 no subfamily data" in output


def test_spread_beats_unplaced_when_a_descriptor_is_both(repo):
    """de_novo_purine_synthesis's shape: two placed subfamilies plus an unplaced member.

    Both facts are true, and the stronger one is that the placeable members
    genuinely sit in different subfamilies -- that is a statement about PANTHER's
    classification, whereas an unplaced co-member is a statement about what the
    index recorded. Checking unplaced first filed such descriptors under the
    weaker fact and left the published members-spread count one short.
    """
    write_obo(repo, {"PTHR1": 20})
    write_members(repo, {"A": "PTHR1:SF1", "B": "PTHR1:SF2", "C": "PTHR1"})
    write_family_module(repo, "a.yaml", [(["PANTHER:PTHR1"], ["A", "B", "C"])])

    output = run(repo)
    assert "1 members spread" in output
    assert "some members unplaced" not in output
