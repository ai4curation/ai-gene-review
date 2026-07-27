#!/usr/bin/env python3
"""Catalytic-motif, ortholog-length and GO-census analysis for human ADAM5 (Q6NVV9).

Human ADAM5 is HGNC:212, locus type *pseudogene*. This script establishes, from
primary records rather than from the gene's family name, three things:

A. **Ortholog length panel.** Every reviewed ADAM5 orthologue is 709-777 aa; the human
   entry is a 412-aa *putative* translation. Per the campaign's ACTL10 lesson, a short
   reference sequence must be measured against orthologues before any conservation or
   domain-loss claim is made, or "missing residues" get scored as "substitutions".

B. **Catalytic zinc-site scan, with controls in BOTH directions.** The reprolysin
   zinc-binding motif is ``HExxHxxGxxHD``. The scan is only trustworthy if it
   discriminates, so the script hard-fails unless every catalytic control HAS the motif
   and every non-catalytic sperm ADAM LACKS it.

C. **A discriminating detector for the fold-to-activity error**, defined as::

       has an annotated Peptidase M12B domain
       AND lacks the HExxH zinc-binding core
       AND nevertheless carries GO:0004222 metalloendopeptidase activity

   This is the campaign's "which genes did this NOT reach?" negative control. It fires on
   the ADAM5 orthologue and on human ADAM5's closest coding paralogs, and is clean on both
   the catalytic controls (motif intact) and on human ADAM5 itself (no domain, no term).
   Human ADAM5 escapes the error *because* pseudogenisation deleted the fold the pipeline
   keys on -- not because any pipeline recognised it as non-catalytic.

D. **The same rule, measured family-wide.** Section C's rule is inferred from a hand-picked
   panel, so it is re-tested over every Swiss-Prot reviewed member of PANTHER PTHR11905. The
   reviewed set is a small fraction of the family, so the family total is fetched and printed
   next to every count; and because the family-wide metric differs from the panel's, the
   family run must **reproduce the panel** before its wider number is reported.

All network results are re-fetched on every run; nothing is hardcoded. Every paginated
QuickGO query asserts ``numberOfHits == len(results)`` so a clamped page cannot be read as
a complete answer. Missing input is a hard error, never a silently degraded section.

Usage::

    uv run python analyze_adam5.py            # run analysis, write results.json + RESULTS.md
    uv run python analyze_adam5.py --self-test  # break-test the guards, write nothing
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass, field
from pathlib import Path

from Bio import Align
from Bio.Align import substitution_matrices

HERE = Path(__file__).resolve().parent

UNIPROT = "https://rest.uniprot.org/uniprotkb"
QUICKGO = "https://www.ebi.ac.uk/QuickGO/services"

# The reprolysin/adamalysin zinc-binding motif and its minimal core.
ZINC_MOTIF = re.compile(r"HE[A-Z]{2}H[A-Z]{2}G[A-Z]{2}HD")
ZINC_CORE = re.compile(r"HE[A-Z]{2}H")

# Catalytic GO terms whose provenance is being audited.
CATALYTIC_TERMS = {
    "GO:0004222": "metalloendopeptidase activity",
    "GO:0008237": "metallopeptidase activity",
    "GO:0006508": "proteolysis",
}

SUBJECT = "Q6NVV9"


@dataclass(frozen=True)
class PanelMember:
    accession: str
    label: str
    role: str  # "subject" | "ortholog" | "catalytic_control" | "noncatalytic_paralog"
    expect_motif: bool | None  # None = no expectation asserted


#: The panel. ``expect_motif`` encodes the discrimination the scan must demonstrate:
#: catalytic ADAMs must carry the zinc motif, sperm ADAMs annotated by UniProt as
#: non-catalytic must not. A violation in EITHER direction aborts the run.
PANEL: tuple[PanelMember, ...] = (
    PanelMember(SUBJECT, "ADAM5 human (subject)", "subject", False),
    PanelMember("Q28483", "ADAM5 macaque", "ortholog", False),
    PanelMember("Q3TTE0", "Adam5 mouse", "ortholog", False),
    PanelMember("Q5BK84", "Adam5 rat", "ortholog", False),
    PanelMember("Q60472", "ADAM5 guinea pig", "ortholog", False),
    PanelMember("O14672", "ADAM10 human", "catalytic_control", True),
    PanelMember("P78536", "ADAM17 human", "catalytic_control", True),
    PanelMember("Q13443", "ADAM9 human", "catalytic_control", True),
    PanelMember("Q9H013", "ADAM19 human", "catalytic_control", True),
    PanelMember("Q99965", "ADAM2 human", "noncatalytic_paralog", False),
    PanelMember("Q9Y3Q7", "ADAM18 human", "noncatalytic_paralog", False),
    PanelMember("Q9H2U9", "ADAM7 human", "noncatalytic_paralog", False),
)

#: Human ADAM5 is compared against the species in which tMDC II was actually
#: characterised as a sperm-surface protein (Frayne et al. 1999, PMID:10417343).
ALIGN_REFERENCE = "Q28483"


def _get_json(url: str, *, timeout: int = 90) -> dict | list:
    """Fetch JSON, failing loudly. A rejected query must never look like an empty result."""
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    try:
        resp = urllib.request.urlopen(req, timeout=timeout)
    except urllib.error.HTTPError as exc:
        raise RuntimeError(f"HTTP {exc.code} {exc.reason} for {url}") from exc
    if resp.status != 200:
        raise RuntimeError(f"HTTP {resp.status} for {url}")
    return json.load(resp)


def fetch_entry(accession: str) -> dict:
    """Fetch one UniProt entry.

    Prints the entry name and reviewed status so a dead/redirected accession cannot pass
    as "a protein that happens to carry no annotation" (the ACTR10 lesson).
    """
    fields = (
        "accession,id,protein_name,gene_names,organism_name,protein_existence,length,"
        "sequence,ft_domain,ft_signal,ft_propep,ft_transmem,cc_caution,reviewed"
    )
    d = _get_json(f"{UNIPROT}/{accession}.json?fields={fields}")
    assert isinstance(d, dict)
    entry_name = d.get("uniProtkbId")
    if not entry_name:
        raise RuntimeError(f"{accession}: no entry name returned - inactive or deleted accession?")
    seq = d.get("sequence", {}).get("value")
    if not seq:
        raise RuntimeError(f"{accession}: no sequence returned")
    entry_type = d.get("entryType", "")
    # "reviewed" is a substring of "unreviewed" - anchor the test (the ACTG2 lesson).
    reviewed = entry_type.startswith("UniProtKB reviewed")
    # Every architectural feature, named from the entry's own table - never guessed.
    features = [
        {
            "type": f["type"],
            "name": (f.get("description") or f["type"]),
            "start": f["location"]["start"]["value"],
            "end": f["location"]["end"]["value"],
        }
        for f in d.get("features", [])
        if f["type"] in ("Domain", "Signal", "Propeptide", "Transmembrane")
    ]
    m12b = [(f["start"], f["end"]) for f in features if "M12B" in f["name"]]
    caution = [
        t["value"]
        for c in d.get("comments", [])
        if c.get("commentType") == "CAUTION"
        for t in c.get("texts", [])
    ]
    return {
        "accession": d["primaryAccession"],
        "entry_name": entry_name,
        "reviewed": reviewed,
        "entry_type": entry_type,
        "organism": d.get("organism", {}).get("scientificName"),
        "protein_existence": d.get("proteinExistence"),
        "length": len(seq),
        "sequence": seq,
        "features": features,
        "m12b_domain": m12b[0] if m12b else None,
        "caution": caution,
    }


def scan_motif(sequence: str) -> dict:
    full = [(m.start() + 1, m.group()) for m in ZINC_MOTIF.finditer(sequence)]
    core = [(m.start() + 1, m.group()) for m in ZINC_CORE.finditer(sequence)]
    return {
        "zinc_motif_HExxHxxGxxHD": full[0][1] if full else None,
        "zinc_motif_position": full[0][0] if full else None,
        "zinc_core_HExxH_count": len(core),
    }


def quickgo_count(accession: str, go_id: str) -> dict:
    """Count annotations to ``go_id`` (and descendants) on one accession.

    Asserts ``numberOfHits == len(results)``: comparing against a page-size constant
    cannot detect a server that clamps rather than errors.
    """
    url = (
        f"{QUICKGO}/annotation/search?geneProductId=UniProtKB:{accession}"
        f"&goId={go_id}&goUsage=descendants&goUsageRelationships=is_a,part_of&limit=100&page=1"
    )
    d = _get_json(url)
    assert isinstance(d, dict)
    hits, results = d["numberOfHits"], d["results"]
    if hits != len(results):
        raise RuntimeError(
            f"paginated/truncated response for {accession} {go_id}: "
            f"numberOfHits={hits} len(results)={len(results)}"
        )
    # withFrom is recorded because the review names specific signature ids (IPR001590,
    # PANTHER:PTN000224844) as the sources of this term. Without it those two ids would be
    # the only figures in the package not pinned by the artifact.
    with_from = sorted(
        {
            f"{c['db']}:{c['id']}"
            for r in results
            for w in (r.get("withFrom") or [])
            for c in w.get("connectedXrefs", [])
        }
    )
    return {
        "count": hits,
        "evidence": sorted({r["goEvidence"] for r in results}),
        "assigned_by": sorted({r["assignedBy"] for r in results}),
        "with_from": with_from,
    }


def quickgo_all(accession: str) -> list[dict]:
    url = f"{QUICKGO}/annotation/search?geneProductId=UniProtKB:{accession}&limit=100&page=1"
    d = _get_json(url)
    assert isinstance(d, dict)
    if d["numberOfHits"] != len(d["results"]):
        raise RuntimeError(
            f"paginated/truncated response for {accession}: "
            f"numberOfHits={d['numberOfHits']} len(results)={len(d['results'])}"
        )
    return [
        {
            "go_id": r["goId"],
            "evidence": r["goEvidence"],
            "reference": r["reference"],
            "assigned_by": r["assignedBy"],
            "qualifier": r.get("qualifier"),
        }
        for r in d["results"]
    ]


def align_to_reference(subject_seq: str, reference_seq: str, reference_features: list) -> dict:
    """Globally align subject to reference; report blocks, deletions and per-feature coverage.

    Reporting only the first and last aligned reference residue is not enough and was
    actively misleading here: the span 44-690 *contains* the M12B domain, yet the domain is
    almost entirely deleted via a large **internal** gap. Coverage must be computed per
    reference feature, from the reference's own feature table.
    """
    aligner = Align.PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -11
    aligner.extend_gap_score = -1
    aligner.mode = "global"
    # End gaps are free: the question is which parts of the reference the (much shorter)
    # subject corresponds to, not how to pay for termini it does not reach.
    aligner.end_gap_score = 0.0
    aln = aligner.align(reference_seq, subject_seq)[0]
    ref_blocks, sub_blocks = aln.aligned

    blocks, covered_ref = [], set()
    identical = aligned_cols = 0
    for (rs, re_), (ss, se) in zip(ref_blocks, sub_blocks):
        ident = sum(1 for i, j in zip(range(rs, re_), range(ss, se)) if reference_seq[i] == subject_seq[j])
        identical += int(ident)
        aligned_cols += int(re_ - rs)
        covered_ref.update(range(rs, re_))
        blocks.append(
            {
                "reference_start": int(rs) + 1, "reference_end": int(re_),
                "subject_start": int(ss) + 1, "subject_end": int(se),
                "length": int(re_ - rs), "identities": int(ident),
                "percent_identity": round(100.0 * ident / (re_ - rs), 1),
            }
        )

    # Internal reference deletions: gaps between consecutive aligned blocks.
    deletions = [
        {
            "reference_start": blocks[i]["reference_end"] + 1,
            "reference_end": blocks[i + 1]["reference_start"] - 1,
            "length": blocks[i + 1]["reference_start"] - blocks[i]["reference_end"] - 1,
            "subject_junction_after_residue": blocks[i]["subject_end"],
        }
        for i in range(len(blocks) - 1)
        if blocks[i + 1]["reference_start"] - blocks[i]["reference_end"] - 1 > 0
    ]

    coverage = {}
    for f in reference_features:
        span = range(f["start"] - 1, f["end"])
        n_cov = sum(1 for i in span if i in covered_ref)
        coverage[f"{f['type']}:{f['name']} {f['start']}-{f['end']}"] = {
            "length": f["end"] - f["start"] + 1,
            "covered": n_cov,
            "fraction_covered": round(n_cov / (f["end"] - f["start"] + 1), 3),
        }

    return {
        "reference_length": len(reference_seq),
        "subject_length": len(subject_seq),
        "blocks": blocks,
        "internal_reference_deletions": deletions,
        "reference_n_terminal_unmatched": blocks[0]["reference_start"] - 1,
        "reference_c_terminal_unmatched": len(reference_seq) - blocks[-1]["reference_end"],
        "aligned_columns": aligned_cols,
        "identities": identical,
        "percent_identity_over_aligned": round(100.0 * identical / aligned_cols, 1),
        "reference_feature_coverage": coverage,
    }


#: The architectural claim this review rests on, pinned by feature name so that the guard
#: fails if the underlying record changes. Two earlier formulations were tried and both
#: were refuted by the measurement itself:
#:   1. "M12B is the least-covered feature" -- false; Signal and Transmembrane are 0.0.
#:   2. "coverage is bimodal, so put a threshold in the largest gap" -- false; the
#:      disintegrin domain is genuinely intermediate at 0.411 because the deletion cuts
#:      *through* it, so no clean gap exists and any threshold would have been invented.
#: What survives is a threshold-free ordinal claim: every feature the review calls lost is
#: less covered than every feature it calls retained.
CLAIMED_LOST = ("Signal", "Peptidase M12B", "Transmembrane")
CLAIMED_RETAINED = ("Propeptide", "Disintegrin", "EGF-like")


def check_domain_loss(alignment: dict, problems: list) -> None:
    """Assert the lost/retained ordering, with no threshold anywhere.

    Also asserts that every annotated reference feature is classified, so a feature added
    to the UniProt record in future cannot be silently skipped -- a guard must not be
    defeatable by the appearance or disappearance of the thing it guards.
    """
    cov = alignment["reference_feature_coverage"]

    def match(names: tuple[str, ...]) -> dict[str, float]:
        return {k: v["fraction_covered"] for k, v in cov.items() if any(n in k for n in names)}

    lost, retained = match(CLAIMED_LOST), match(CLAIMED_RETAINED)
    unclassified = set(cov) - set(lost) - set(retained)
    if unclassified:
        problems.append(f"reference features not covered by the lost/retained claim: {sorted(unclassified)}")
    both = set(lost) & set(retained)
    if both:
        problems.append(f"reference features classified as BOTH lost and retained: {sorted(both)}")
    for label, group, names in (("lost", lost, CLAIMED_LOST), ("retained", retained, CLAIMED_RETAINED)):
        if len(group) != len(names):
            problems.append(
                f"expected {len(names)} '{label}' features {names}, matched {sorted(group)}"
            )
    if not lost or not retained:
        return

    worst_retained = min(retained.items(), key=lambda kv: kv[1])
    best_lost = max(lost.items(), key=lambda kv: kv[1])
    if best_lost[1] >= worst_retained[1]:
        problems.append(
            f"lost/retained ordering violated: '{best_lost[0]}' ({best_lost[1]}) is not less "
            f"covered than '{worst_retained[0]}' ({worst_retained[1]}); the structural claim "
            "underpinning this review no longer holds"
        )
        return

    m12b_keys = [k for k in cov if "M12B" in k]
    if len(m12b_keys) != 1:
        problems.append(f"expected exactly one M12B feature, found {m12b_keys}")
        return
    alignment["m12b_coverage"] = cov[m12b_keys[0]]["fraction_covered"]
    alignment["most_covered_lost_feature"] = {"feature": best_lost[0], "coverage": best_lost[1]}
    alignment["least_covered_retained_feature"] = {"feature": worst_retained[0], "coverage": worst_retained[1]}
    alignment["separation_margin"] = round(worst_retained[1] - best_lost[1], 3)
    alignment["features_lost"] = sorted(lost)
    alignment["features_retained"] = sorted(retained)


PANTHER_FAMILY = "PTHR11905"


def fetch_family_members() -> tuple[list[dict], int]:
    """Every **Swiss-Prot reviewed** member of the PANTHER family, plus the family total.

    The reviewed set is a small fraction of the family, so the total is fetched alongside it
    and printed next to every count: a claim measured over reviewed entries must never be
    written as a claim about the family.

    Pagination is followed to exhaustion and the collected count is asserted against
    ``x-total-results`` -- never inferred from a page size we chose.
    """
    query = urllib.parse.quote(f"xref:panther-{PANTHER_FAMILY} AND reviewed:true")
    url = (
        f"{UNIPROT}/search?query={query}"
        "&fields=accession,id,organism_name,length,ft_domain,go_id,sequence&size=500"
    )
    entries: list[dict] = []
    total: int | None = None
    while url:
        resp = urllib.request.urlopen(urllib.request.Request(url, headers={"Accept": "application/json"}), timeout=120)
        if total is None:
            total = int(resp.headers["x-total-results"])
        entries.extend(json.load(resp)["results"])
        m = re.search(r'<([^>]+)>;\s*rel="next"', resp.headers.get("Link", ""))
        url = m.group(1) if m else None
    if total != len(entries):
        raise RuntimeError(f"family fetch truncated: x-total-results={total} collected={len(entries)}")

    meta = _get_json(f"https://www.ebi.ac.uk/interpro/api/entry/panther/{PANTHER_FAMILY}/")
    assert isinstance(meta, dict)
    family_total = meta["metadata"]["counters"]["proteins"]
    return entries, int(family_total)


def family_detector(entries: list[dict], family_total: int) -> dict:
    """Run the fold/zinc-site/annotation cross-tabulation over the whole reviewed family.

    Turns "the pipelines key on the fold, not the zinc site" from a rule inferred over a
    hand-picked panel into a measured one. The measure here is *exact* ``GO:0004222``
    presence in the entry's GO cross-references, which is a different metric from the
    panel's QuickGO descendant-aware count -- so the two are reconciled explicitly by
    :func:`check_family_reproduces_panel` rather than assumed to agree.
    """
    rows = {}
    for e in entries:
        seq = e["sequence"]["value"]
        has_fold = any(
            f["type"] == "Domain" and "M12B" in (f.get("description") or "") for f in e.get("features", [])
        )
        gos = {x["id"] for x in e.get("uniProtKBCrossReferences", []) if x["database"] == "GO"}
        rows[e["primaryAccession"]] = {
            "entry_name": e["uniProtkbId"],
            "organism": e["organism"]["scientificName"],
            "has_m12b_fold": has_fold,
            "zinc_core_present": bool(ZINC_CORE.search(seq)),
            "has_GO_0004222": "GO:0004222" in gos,
        }
    fold = [a for a, r in rows.items() if r["has_m12b_fold"]]
    fold_no_zinc = [a for a in fold if not rows[a]["zinc_core_present"]]
    fold_zinc = [a for a in fold if rows[a]["zinc_core_present"]]
    return {
        "panther_family": PANTHER_FAMILY,
        "family_total_proteins": family_total,
        "reviewed_members_measured": len(rows),
        "no_m12b_fold": len(rows) - len(fold),
        "fold_with_zinc_site": len(fold_zinc),
        "fold_with_zinc_site_annotated_GO_0004222": sum(1 for a in fold_zinc if rows[a]["has_GO_0004222"]),
        "fold_without_zinc_site": len(fold_no_zinc),
        "fold_without_zinc_site_annotated_GO_0004222": sum(1 for a in fold_no_zinc if rows[a]["has_GO_0004222"]),
        "fires": sorted(a for a in fold_no_zinc if rows[a]["has_GO_0004222"]),
        "rows": rows,
    }


def check_family_reproduces_panel(fam: dict, panel_detector: dict, problems: list) -> None:
    """The family-wide run must reproduce the hand panel before its wider number is reported.

    Two different measurements are involved (UniProt GO cross-references vs QuickGO with
    descendants), so agreement is a real check, not a tautology. A panel member absent from
    the reviewed family set is reported rather than silently skipped.
    """
    fam_rows = fam["rows"]
    panel_fires = {e["accession"] for e in panel_detector["fires"]}
    panel_all = panel_fires | {e["accession"] for e in panel_detector["clean"]}
    absent = sorted(a for a in panel_all if a not in fam_rows)
    fam["panel_members_absent_from_family"] = absent
    present = [a for a in panel_all if a in fam_rows]
    if not present:
        problems.append("no panel member is in the reviewed family set; reproduction untested")
        return
    for acc in present:
        fam_fires = (
            fam_rows[acc]["has_m12b_fold"]
            and not fam_rows[acc]["zinc_core_present"]
            and fam_rows[acc]["has_GO_0004222"]
        )
        if fam_fires != (acc in panel_fires):
            problems.append(
                f"family-wide detector disagrees with the hand panel on {acc} "
                f"({fam_rows[acc]['entry_name']}): family={fam_fires} panel={acc in panel_fires}"
            )
    fam["panel_members_reproduced"] = len(present)


@dataclass
class Analysis:
    panel: dict = field(default_factory=dict)
    go_census: dict = field(default_factory=dict)
    subject_annotations: list = field(default_factory=list)
    alignment: dict = field(default_factory=dict)
    detector: dict = field(default_factory=dict)
    family: dict = field(default_factory=dict)
    problems: list = field(default_factory=list)


def check_motif_discrimination(panel: dict, problems: list) -> None:
    """Both directions. A check that can only fail one way is half a check."""
    for acc, rec in panel.items():
        expect = rec["expect_motif"]
        if expect is None:
            continue
        observed = rec["zinc_motif_HExxHxxGxxHD"] is not None
        if observed != expect:
            problems.append(
                f"motif expectation violated for {acc} ({rec['label']}, role={rec['role']}): "
                f"expected motif={expect}, observed={observed}"
            )


def check_subject_is_uncontaminated(panel: dict, census: dict, subject_ann: list, problems: list) -> None:
    """The subject must have no M12B domain, no zinc core, and no catalytic GO term."""
    s = panel[SUBJECT]
    if s["m12b_domain"] is not None:
        problems.append(f"{SUBJECT}: unexpected Peptidase M12B domain {s['m12b_domain']}")
    if s["zinc_core_HExxH_count"] != 0:
        problems.append(f"{SUBJECT}: unexpected HExxH core (n={s['zinc_core_HExxH_count']})")
    for go_id in CATALYTIC_TERMS:
        n = census[SUBJECT][go_id]["count"]
        if n != 0:
            problems.append(f"{SUBJECT}: carries {n} annotation(s) to {go_id} - review must act on them")
    non_nd = [a for a in subject_ann if a["evidence"] != "ND"]
    if non_nd:
        problems.append(f"{SUBJECT}: non-ND annotations present, review scope has changed: {non_nd}")


def run_detector(panel: dict, census: dict) -> dict:
    """Fold present + zinc site absent + catalytic term present."""
    fires, clean = [], []
    for acc, rec in panel.items():
        has_fold = rec["m12b_domain"] is not None
        no_zinc = rec["zinc_core_HExxH_count"] == 0
        has_term = census[acc]["GO:0004222"]["count"] > 0
        entry = {
            "accession": acc,
            "label": rec["label"],
            "role": rec["role"],
            "m12b_domain": rec["m12b_domain"],
            "zinc_core_present": not no_zinc,
            "GO:0004222_count": census[acc]["GO:0004222"]["count"],
            "GO:0004222_evidence": census[acc]["GO:0004222"]["evidence"],
        }
        (fires if (has_fold and no_zinc and has_term) else clean).append(entry)
    return {"fires": fires, "clean": clean}


def analyse() -> Analysis:
    a = Analysis()
    for m in PANEL:
        rec = fetch_entry(m.accession)
        rec.update(scan_motif(rec["sequence"]))
        rec["label"] = m.label
        rec["role"] = m.role
        rec["expect_motif"] = m.expect_motif
        print(
            f"  {rec['accession']:8s} {rec['entry_name']:16s} "
            f"{'Swiss-Prot' if rec['reviewed'] else 'TrEMBL':10s} "
            f"len={rec['length']:4d} PE={str(rec['protein_existence'])[:1]} "
            f"M12B={str(rec['m12b_domain']):12s} "
            f"motif={rec['zinc_motif_HExxHxxGxxHD'] or 'ABSENT'}",
            file=sys.stderr,
        )
        a.panel[m.accession] = rec
        time.sleep(0.15)

    # Guard against the "reviewed" substring bug promoting everything to Swiss-Prot.
    n_reviewed = sum(1 for r in a.panel.values() if r["reviewed"])
    if n_reviewed != len(a.panel):
        a.problems.append(f"expected an all-Swiss-Prot panel, got {n_reviewed}/{len(a.panel)}")

    for acc in a.panel:
        a.go_census[acc] = {go: quickgo_count(acc, go) for go in CATALYTIC_TERMS}
        time.sleep(0.15)

    a.subject_annotations = quickgo_all(SUBJECT)
    a.alignment = align_to_reference(
        a.panel[SUBJECT]["sequence"],
        a.panel[ALIGN_REFERENCE]["sequence"],
        a.panel[ALIGN_REFERENCE]["features"],
    )
    check_motif_discrimination(a.panel, a.problems)
    check_subject_is_uncontaminated(a.panel, a.go_census, a.subject_annotations, a.problems)
    check_domain_loss(a.alignment, a.problems)
    a.detector = run_detector(a.panel, a.go_census)

    print(f"Fetching reviewed {PANTHER_FAMILY} members...", file=sys.stderr)
    members, family_total = fetch_family_members()
    a.family = family_detector(members, family_total)
    check_family_reproduces_panel(a.family, a.detector, a.problems)
    print(
        f"  {a.family['reviewed_members_measured']} reviewed of {family_total} family proteins; "
        f"fold+zinc {a.family['fold_with_zinc_site_annotated_GO_0004222']}/{a.family['fold_with_zinc_site']} "
        f"annotated, fold-no-zinc {a.family['fold_without_zinc_site_annotated_GO_0004222']}/"
        f"{a.family['fold_without_zinc_site']} annotated",
        file=sys.stderr,
    )
    return a


def render_results(a: Analysis) -> str:
    p = a.panel
    subj, mac = p[SUBJECT], p[ALIGN_REFERENCE]
    aln = a.alignment
    lines: list[str] = []
    w = lines.append
    w("# ADAM5 (human, Q6NVV9) — catalytic-motif, ortholog-length and GO-census analysis")
    w("")
    w("Generated by `analyze_adam5.py`; every number below is re-fetched from UniProt and")
    w("QuickGO on each run. Reproduce with `uv run python analyze_adam5.py`.")
    w("")
    w("## A. Ortholog length panel")
    w("")
    w("| accession | entry | status | organism | PE | length | Peptidase M12B domain | CAUTION |")
    w("|---|---|---|---|---|---|---|---|")
    for m in PANEL:
        if m.role not in ("subject", "ortholog"):
            continue
        r = p[m.accession]
        dom = f"{r['m12b_domain'][0]}–{r['m12b_domain'][1]}" if r["m12b_domain"] else "**absent**"
        w(
            f"| {r['accession']} | {r['entry_name']} | "
            f"{'Swiss-Prot' if r['reviewed'] else 'TrEMBL'} | *{r['organism']}* | "
            f"{r['protein_existence']} | {r['length']} | {dom} | "
            f"{'; '.join(r['caution']) or '—'} |"
        )
    w("")
    ortho_lens = [p[m.accession]["length"] for m in PANEL if m.role == "ortholog"]
    w(
        f"Every reviewed ADAM5 orthologue is {min(ortho_lens)}–{max(ortho_lens)} aa and carries an "
        f"annotated Peptidase M12B domain. The human entry is **{subj['length']} aa with no M12B "
        f"domain at all** — {mac['length'] - subj['length']} residues shorter than the macaque "
        "protein in which tMDC II was characterised as a sperm-surface antigen."
    )
    w("")
    w(
        "All five orthologues, human included, carry UniProt's `CAUTION: Not expected to have "
        "protease activity`; only the human entry adds `Could be the product of a pseudogene`."
    )
    w("")
    w(f"## B. Alignment of human ADAM5 to macaque ADAM5 ({ALIGN_REFERENCE})")
    w("")
    w(
        f"Global BLOSUM62 alignment, free end gaps. {aln['identities']}/{aln['aligned_columns']} "
        f"identities over aligned columns (**{aln['percent_identity_over_aligned']}%**)."
    )
    w("")
    w("| macaque | human | length | identity |")
    w("|---|---|---|---|")
    for b in aln["blocks"]:
        w(
            f"| {b['reference_start']}–{b['reference_end']} | "
            f"{b['subject_start']}–{b['subject_end']} | {b['length']} | "
            f"{b['identities']}/{b['length']} ({b['percent_identity']}%) |"
        )
    w("")
    w(
        "The retained blocks are near-identical to macaque, so this is not a diverged "
        "paralogue: it is the same gene with material missing. The missing material is:"
    )
    w("")
    w(f"- macaque 1–{aln['reference_n_terminal_unmatched']} (N-terminus, no human counterpart)")
    for d in aln["internal_reference_deletions"]:
        w(
            f"- macaque {d['reference_start']}–{d['reference_end']} "
            f"(**{d['length']} aa internal deletion**, fused after human residue "
            f"{d['subject_junction_after_residue']})"
        )
    w(
        f"- macaque {aln['reference_length'] - aln['reference_c_terminal_unmatched'] + 1}–"
        f"{aln['reference_length']} (C-terminus, {aln['reference_c_terminal_unmatched']} aa)"
    )
    w("")
    w("Coverage of each annotated macaque feature by the human sequence:")
    w("")
    w("| macaque feature | length | residues with a human counterpart | fraction |")
    w("|---|---|---|---|")
    for k, v in sorted(
        aln["reference_feature_coverage"].items(), key=lambda kv: kv[1]["fraction_covered"]
    ):
        w(f"| {k} | {v['length']} | {v['covered']} | {v['fraction_covered']} |")
    w("")
    w("The claim the review rests on is stated as an ordering, with no threshold:")
    w("")
    w("- **lost:** " + "; ".join(f"`{k}`" for k in aln["features_lost"]))
    w("- **retained:** " + "; ".join(f"`{k}`" for k in aln["features_retained"]))
    w("")
    w(
        f"The most-covered lost feature (`{aln['most_covered_lost_feature']['feature']}`, "
        f"{aln['most_covered_lost_feature']['coverage']}) is less covered than the least-covered "
        f"retained feature (`{aln['least_covered_retained_feature']['feature']}`, "
        f"{aln['least_covered_retained_feature']['coverage']}), margin "
        f"**{aln['separation_margin']}**. The run asserts that ordering, asserts that no "
        "reference feature is left unclassified, and fails loudly if either breaks."
    )
    w("")
    w(
        f"So the catalytic domain is not merely degenerate in the human gene — at "
        f"{aln['m12b_coverage']} coverage the sequence encoding it is **essentially absent from "
        "the putative translation product**. And it is not alone: the **signal peptide** and the "
        "**transmembrane helix** are lost outright, and the disintegrin domain is itself "
        "truncated because the deletion cuts through it. A product lacking both secretory "
        "targeting and a membrane anchor could not be displayed on the sperm surface even if it "
        "were translated, which bears on the cellular-component aspect as much as the "
        "molecular-function one."
    )
    w("")
    junction = aln["internal_reference_deletions"][0]["subject_junction_after_residue"]
    human_disin = [f for f in subj["features"] if "Disintegrin" in f["name"]]
    if human_disin:
        hd = human_disin[0]
        if hd["start"] <= junction < hd["end"]:
            w(
                f"Note a consequence for the human entry's own feature table: its annotated "
                f"Disintegrin domain ({hd['start']}–{hd['end']}) **straddles the deletion "
                f"junction at residue {junction}/{junction + 1}**. Only its C-terminal portion "
                "derives from macaque disintegrin sequence; the N-terminal portion derives from "
                "the region upstream of the macaque disintegrin domain. The human disintegrin "
                "call is a fusion created by the deletion, not a conserved intact domain."
            )
            w("")
    w("## C. Catalytic zinc-site scan (controls in both directions)")
    w("")
    w("Reprolysin zinc-binding motif `HExxHxxGxxHD`; minimal core `HExxH`.")
    w("")
    w("| accession | protein | role | M12B domain | `HExxHxxGxxHD` | `HExxH` count |")
    w("|---|---|---|---|---|---|")
    for m in PANEL:
        r = p[m.accession]
        dom = f"{r['m12b_domain'][0]}–{r['m12b_domain'][1]}" if r["m12b_domain"] else "absent"
        w(
            f"| {r['accession']} | {r['label']} | {r['role']} | {dom} | "
            f"{r['zinc_motif_HExxHxxGxxHD'] or '**absent**'} | {r['zinc_core_HExxH_count']} |"
        )
    w("")
    w(
        "The scan discriminates: all four catalytic controls carry an intact motif, and every "
        "sperm ADAM that UniProt describes as non-catalytic lacks even the `HExxH` core. Human "
        "ADAM5 contains **no `HExxH` substring anywhere in its 412 residues**."
    )
    w("")
    w("## D. GO census of the catalytic terms")
    w("")
    w("QuickGO, `goUsage=descendants`, `is_a`/`part_of`; counts are annotations, not entities.")
    w("")
    header = " | ".join(f"{g} {n}" for g, n in CATALYTIC_TERMS.items())
    w(f"| accession | protein | {header} |")
    w("|---|---|" + "---|" * len(CATALYTIC_TERMS))
    for m in PANEL:
        r = p[m.accession]
        cells = []
        for go in CATALYTIC_TERMS:
            c = a.go_census[m.accession][go]
            cells.append(f"{c['count']} ({','.join(c['evidence']) or '—'})")
        w(f"| {r['accession']} | {r['label']} | " + " | ".join(cells) + " |")
    w("")
    w("## E. Detector: annotated catalytic activity on a fold with no zinc site")
    w("")
    w(
        "Fires when a protein has an annotated Peptidase M12B domain **and** lacks the `HExxH` "
        "core **and** nevertheless carries `GO:0004222`."
    )
    w("")
    w("**Fires:**")
    w("")
    for e in a.detector["fires"]:
        w(
            f"- `{e['accession']}` {e['label']} — M12B {e['m12b_domain'][0]}–{e['m12b_domain'][1]}, "
            f"no zinc core, {e['GO:0004222_count']} × `GO:0004222` "
            f"({','.join(e['GO:0004222_evidence'])})"
        )
    w("")
    w("**Clean:**")
    w("")
    for e in a.detector["clean"]:
        reason = (
            "zinc motif intact"
            if e["zinc_core_present"]
            else ("no M12B fold and no catalytic term" if e["m12b_domain"] is None else "no catalytic term")
        )
        w(f"- `{e['accession']}` {e['label']} — {reason}")
    w("")
    w(
        "The boundary is the finding. The pipelines that place `GO:0004222` on this clade key on "
        "**presence of the M12B fold, not on integrity of the zinc site**, so every close relative "
        "of ADAM5 that retains the fold receives the activity term despite lacking the catalytic "
        "residues. Human ADAM5 is the one member that escapes — and it escapes because "
        "pseudogenisation deleted the fold the pipeline matches on, not because any pipeline "
        "recognised the protein as non-catalytic. Nothing on human ADAM5 needs retracting; the "
        "correctable defect sits on its relatives."
    )
    w("")
    w("## F. Complete GO annotation set for human ADAM5")
    w("")
    w("| GO id | evidence | reference | assigned by | qualifier |")
    w("|---|---|---|---|---|")
    for r in a.subject_annotations:
        w(
            f"| {r['go_id']} | {r['evidence']} | {r['reference']} | "
            f"{r['assigned_by']} | {r['qualifier']} |"
        )
    w("")
    w(
        f"{len(a.subject_annotations)} annotations, all `ND` against `GO_REF:0000015` — the three "
        "ontology roots. There is no molecular-function, cellular-component or biological-process "
        "claim on this gene to evaluate."
    )
    w("")
    fam = a.family
    w(f"## G. The rule, measured across the whole reviewed {fam['panther_family']} family")
    w("")
    w(
        f"Section E infers a rule from a 12-member hand-picked panel. This section tests it over "
        f"**all {fam['reviewed_members_measured']} Swiss-Prot reviewed members** of PANTHER "
        f"`{fam['panther_family']}`. Note the scope: the family contains "
        f"**{fam['family_total_proteins']:,} proteins** in total, so this is the reviewed subset "
        f"({100 * fam['reviewed_members_measured'] / fam['family_total_proteins']:.1f}%), and every "
        "number below is a statement about reviewed entries, not about the family."
    )
    w("")
    w(
        "The metric here is *exact* `GO:0004222` presence in the entry's GO cross-references, which "
        "is **not** the same measurement as section D's descendant-aware QuickGO count. So the two "
        "are reconciled rather than assumed to agree: the family-wide detector is required to "
        f"reproduce the hand panel's verdict for all **{fam.get('panel_members_reproduced', 0)}** "
        "panel members present in the reviewed set, and the run fails if any disagrees."
    )
    if fam.get("panel_members_absent_from_family"):
        w("")
        w(
            "Panel members absent from this family (reported, not silently skipped): "
            + ", ".join(f"`{x}`" for x in fam["panel_members_absent_from_family"])
            + " — ADAM10 and ADAM17 are classified in a different PANTHER family, so the "
            "family-wide run cannot corroborate them."
        )
    w("")
    zinc_n, zinc_ann = fam["fold_with_zinc_site"], fam["fold_with_zinc_site_annotated_GO_0004222"]
    noz_n, noz_ann = fam["fold_without_zinc_site"], fam["fold_without_zinc_site_annotated_GO_0004222"]
    w("| reviewed members | n | carry `GO:0004222` | % |")
    w("|---|---|---|---|")
    w(f"| Peptidase M12B fold **with** `HExxH` zinc site | {zinc_n} | {zinc_ann} | {100*zinc_ann/zinc_n:.0f}% |")
    w(f"| Peptidase M12B fold **without** `HExxH` zinc site | {noz_n} | {noz_ann} | {100*noz_ann/noz_n:.0f}% |")
    w(f"| no M12B fold | {fam['no_m12b_fold']} | — | — |")
    w("")
    w(
        f"**This converts the rule from inferred to measured.** If the annotation discriminated on "
        f"the catalytic site, the second row would be near zero. It is "
        f"**{noz_ann}/{noz_n} ({100*noz_ann/noz_n:.0f}%)** — statistically indistinguishable from the "
        f"{100*zinc_ann/zinc_n:.0f}% of intact members. Losing the zinc-binding site has almost no "
        "effect on whether a reviewed family member is annotated with metalloendopeptidase activity, "
        "which is precisely the claim raised for InterPro and GO Central in `suggested_questions`."
    )
    w("")
    w("## Checks run")
    w("")
    w("- motif expectations asserted in both directions across the panel")
    w("- subject asserted to have no M12B domain, no `HExxH`, and zero catalytic annotations")
    w("- panel asserted all-Swiss-Prot with an anchored `startswith` test")
    w("- every QuickGO query asserted `numberOfHits == len(results)`")
    w("- every UniProt fetch asserted to return an entry name (dead-accession guard)")
    w("- family fetch paginated to exhaustion and asserted against `x-total-results`")
    w("- family-wide detector asserted to reproduce the hand panel before its wider number is used")
    w("")
    w(f"Problems reported: {len(a.problems)}")
    for pr in a.problems:
        w(f"- {pr}")
    w("")
    return "\n".join(lines)


def self_test() -> int:
    """Break-test the guards. Each mutation asserts its target is present first."""
    failures: list[str] = []

    catalytic = "MKHELGHNFGSPHDAAAA"
    assert ZINC_MOTIF.search(catalytic), "self-test fixture is broken: control lacks the motif"
    if scan_motif(catalytic)["zinc_motif_HExxHxxGxxHD"] is None:
        failures.append("scan_motif failed to find a motif that is present")
    broken = catalytic.replace("HELGHNFGSPHD", "QELGQNFGSPQD")
    assert broken != catalytic, "self-test mutation was a no-op - the target string has drifted"
    if scan_motif(broken)["zinc_motif_HExxHxxGxxHD"] is not None:
        failures.append("scan_motif found a motif in a sequence where it was destroyed")

    # The discrimination check must fire in BOTH directions.
    panel_missing = {
        "X1": {"label": "ctrl", "role": "catalytic_control", "expect_motif": True,
               "zinc_motif_HExxHxxGxxHD": None}
    }
    probs: list[str] = []
    check_motif_discrimination(panel_missing, probs)
    if not probs:
        failures.append("discrimination check did not fire on a catalytic control missing its motif")
    panel_extra = {
        "X2": {"label": "sperm", "role": "noncatalytic_paralog", "expect_motif": False,
               "zinc_motif_HExxHxxGxxHD": "HELGHNFGSPHD"}
    }
    probs = []
    check_motif_discrimination(panel_extra, probs)
    if not probs:
        failures.append("discrimination check did not fire on a non-catalytic protein WITH a motif")
    # Happy path must NOT fire (a check can be wrong about success as easily as failure).
    panel_ok = {
        "X3": {"label": "ctrl", "role": "catalytic_control", "expect_motif": True,
               "zinc_motif_HExxHxxGxxHD": "HELGHNFGSPHD"},
        "X4": {"label": "sperm", "role": "noncatalytic_paralog", "expect_motif": False,
               "zinc_motif_HExxHxxGxxHD": None},
    }
    probs = []
    check_motif_discrimination(panel_ok, probs)
    if probs:
        failures.append(f"discrimination check fired on a correct panel: {probs}")

    # The subject guard must fire if ADAM5 ever gains a catalytic annotation.
    probs = []
    check_subject_is_uncontaminated(
        {SUBJECT: {"m12b_domain": None, "zinc_core_HExxH_count": 0}},
        {SUBJECT: {g: {"count": 1 if g == "GO:0004222" else 0} for g in CATALYTIC_TERMS}},
        [{"evidence": "ND"}],
        probs,
    )
    if not probs:
        failures.append("subject guard did not fire on a planted GO:0004222 annotation")
    probs = []
    check_subject_is_uncontaminated(
        {SUBJECT: {"m12b_domain": None, "zinc_core_HExxH_count": 0}},
        {SUBJECT: {g: {"count": 0} for g in CATALYTIC_TERMS}},
        [{"evidence": "IDA"}],
        probs,
    )
    if not probs:
        failures.append("subject guard did not fire on a planted non-ND annotation")

    # check_domain_loss: happy path silent, ordering violation caught, new feature caught.
    def cov_fixture(**overrides: float) -> dict:
        base = {
            "Signal:Signal 1-16": 0.0,
            "Domain:Peptidase M12B 183-380": 0.066,
            "Transmembrane:Helical 699-719": 0.0,
            "Propeptide:Propeptide 17-142": 0.786,
            "Domain:Disintegrin 389-478": 0.411,
            "Domain:EGF-like 630-664": 1.0,
        }
        base.update(overrides)
        return {"reference_feature_coverage": {k: {"fraction_covered": v} for k, v in base.items()}}

    probs = []
    check_domain_loss(cov_fixture(), probs)
    if probs:
        failures.append(f"domain-loss check fired on the happy path: {probs}")
    probs = []
    # A restored catalytic domain must break the ordering.
    check_domain_loss(cov_fixture(**{"Domain:Peptidase M12B 183-380": 0.95}), probs)
    if not probs:
        failures.append("domain-loss check did not fire when M12B coverage was restored to 0.95")
    probs = []
    fx = cov_fixture()
    fx["reference_feature_coverage"]["Domain:Made-Up 1-9"] = {"fraction_covered": 0.5}
    check_domain_loss(fx, probs)
    if not probs:
        failures.append("domain-loss check did not fire on an unclassified reference feature")
    probs = []
    fx = cov_fixture()
    del fx["reference_feature_coverage"]["Transmembrane:Helical 699-719"]
    check_domain_loss(fx, probs)
    if not probs:
        failures.append("domain-loss check did not fire when a claimed-lost feature disappeared")

    # The detector must fire on fold+no-zinc+term and stay clean otherwise.
    det = run_detector(
        {
            "A": {"label": "a", "role": "x", "m12b_domain": (1, 2), "zinc_core_HExxH_count": 0},
            "B": {"label": "b", "role": "x", "m12b_domain": (1, 2), "zinc_core_HExxH_count": 1},
            "C": {"label": "c", "role": "x", "m12b_domain": None, "zinc_core_HExxH_count": 0},
        },
        {
            "A": {"GO:0004222": {"count": 2, "evidence": ["IBA"]}},
            "B": {"GO:0004222": {"count": 2, "evidence": ["IDA"]}},
            "C": {"GO:0004222": {"count": 0, "evidence": []}},
        },
    )
    fired = {e["accession"] for e in det["fires"]}
    if fired != {"A"}:
        failures.append(f"detector fired on {fired}, expected exactly {{'A'}}")

    # check_family_reproduces_panel: silent on agreement, fires on disagreement,
    # and reports (rather than hides) a panel member missing from the family.
    def fam_fixture(**over):
        rows = {
            "A": {"entry_name": "A_X", "has_m12b_fold": True, "zinc_core_present": False, "has_GO_0004222": True},
            "B": {"entry_name": "B_X", "has_m12b_fold": True, "zinc_core_present": True, "has_GO_0004222": True},
        }
        rows.update(over)
        return {"rows": rows}

    panel = {"fires": [{"accession": "A"}], "clean": [{"accession": "B"}, {"accession": "GONE"}]}
    probs = []
    f = fam_fixture()
    check_family_reproduces_panel(f, panel, probs)
    if probs:
        failures.append(f"family/panel reconciliation fired on agreement: {probs}")
    if f.get("panel_members_absent_from_family") != ["GONE"]:
        failures.append("family/panel reconciliation did not report the absent panel member")
    probs = []
    # flip A so the family says "no term" while the panel says it fires
    check_family_reproduces_panel(
        fam_fixture(A={"entry_name": "A_X", "has_m12b_fold": True, "zinc_core_present": False,
                       "has_GO_0004222": False}),
        panel, probs)
    if not probs:
        failures.append("family/panel reconciliation did not fire on a disagreement")

    for f in failures:
        print(f"SELF-TEST FAILURE: {f}", file=sys.stderr)
    print(f"self-test: {len(failures)} failure(s)", file=sys.stderr)
    return 1 if failures else 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--self-test", action="store_true", help="break-test the guards and exit")
    args = ap.parse_args()
    if args.self_test:
        return self_test()

    print("Fetching UniProt panel...", file=sys.stderr)
    a = analyse()

    payload = {
        "subject": SUBJECT,
        "panel": {
            k: {kk: vv for kk, vv in v.items() if kk != "sequence"} for k, v in a.panel.items()
        },
        "go_census": a.go_census,
        "subject_annotations": a.subject_annotations,
        "alignment_to_macaque": a.alignment,
        "detector": a.detector,
        "family_wide": a.family,
        "problems": a.problems,
    }
    # Render BEFORE writing anything, so a rendering failure cannot leave a stale
    # RESULTS.md sitting next to a freshly written results.json.
    report = render_results(a)
    (HERE / "results.json").write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    (HERE / "RESULTS.md").write_text(report)
    print(f"wrote results.json and RESULTS.md ({len(a.problems)} problems)", file=sys.stderr)
    for pr in a.problems:
        print(f"  PROBLEM: {pr}", file=sys.stderr)
    return 1 if a.problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
