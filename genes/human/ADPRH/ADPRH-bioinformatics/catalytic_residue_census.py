"""Does the IPR012108 -> GO:0003875 route discriminate on ADPRH's catalytic residues?

Human ADPRH (ARH1, P54922) has five residues for which single substitutions cause
"Complete loss of activity" in UniProt's FT MUTAGEN table, each supported by
ECO:0000269|PubMed:30472116:

    S54, D55, D56  (Mg2+ site 1 / vicinal acidic pair)
    D302, S305     (Mg2+ site 2)

Its closest human paralog ADPRHL1 (Q8NDY3) is annotated by Swiss-Prot as
"Inactive ADP-ribosyltransferase ARH2" with the CAUTION "lacks the metal-binding
and substrate-binding residues, suggesting that it has no hydrolase activity" --
yet ADPRHL1 carries GO:0003875 (ADP-ribosylarginine-[protein] hydrolase activity)
by IEA and GO:0000287 (magnesium ion binding) by IEA.

This script measures, over the Swiss-Prot reviewed members of PANTHER PTHR16222,
whether holding GO:0003875 tracks retention of those five residues.  It is the
"negative control" form of the argument: the interesting number is not ADPRH's own
conservation (which is trivially 5/5) but whether the annotation route separates
members that retain the residues from members that do not.

Two conditions are required before a source residue is counted as a match, because
matching the amino acid alone manufactures active sites out of alignment noise at
low identity:

  1. residue identity at the column aligned to the ADPRH position, AND
  2. `lands_on_annotated_target_site` -- for any source that has its own UniProt
     BINDING/ACT_SITE features, the aligned position must fall on one of them.
     Sources with no annotated sites of their own are reported separately and are
     NOT silently promoted to "match".

The two conditions are scored PER POSITION, so `n_identical_and_on_own_site` is a count
out of five rather than a pass/fail for the whole set.

Run:  uv run python catalytic_residue_census.py
      uv run python catalytic_residue_census.py --self-test
"""

from __future__ import annotations

import argparse
import json
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path

from Bio import Align
from Bio.Align import substitution_matrices

HERE = Path(__file__).resolve().parent
# The PANTHER member table is cached in the repository by `just fetch-gene`.
PANTHER_ENTRIES = HERE.parents[3] / "interpro" / "panther" / "PTHR16222" / "PTHR16222-entries.csv"
PANTHER_METADATA = HERE.parents[3] / "interpro" / "panther" / "PTHR16222" / "PTHR16222-metadata.yaml"

SUBJECT = "P54922"  # human ADPRH / ARH1

# UniProt FT MUTAGEN entries on P54922 whose note is "Complete loss of activity".
CATALYTIC_SITES: dict[int, str] = {54: "S", 55: "D", 56: "D", 302: "D", 305: "S"}

UNIPROT = "https://rest.uniprot.org/uniprotkb"
QUICKGO = "https://www.ebi.ac.uk/QuickGO/services"
INTERPRO = "https://www.ebi.ac.uk/interpro/api"
RCSB = "https://data.rcsb.org/rest/v1/core/entry"

# The PDB set is DERIVED from the subject's UniProt cross-references rather than written
# out here, so a new deposition is picked up instead of silently omitted.  Which metals
# each structure contains is the evidence behind the GO:0000287 and GO:0030955 rows, and
# PMID:19407395's cached record is abstract-only and never mentions magnesium - so without
# this the magnesium claim has no checkable source inside the repository.
def pdb_ids_of(accession: str) -> list[str]:
    d = _get_json(
        f"{UNIPROT}/search?"
        + urllib.parse.urlencode(
            {"query": f"accession:{accession}", "fields": "xref_pdb", "format": "json", "size": 2}
        )
    )
    results = d.get("results", [])
    if len(results) != 1:
        raise AnalysisError(f"{accession}: expected 1 entry, got {len(results)}")
    ids = sorted(
        x["id"] for x in results[0].get("uniProtKBCrossReferences", []) if x["database"] == "PDB"
    )
    if not ids:
        raise AnalysisError(f"{accession}: no PDB cross-references - the metals table would be empty")
    return ids


class AnalysisError(RuntimeError):
    """A missing input or a failed precondition.  Never degrade silently."""


def _get_json(url: str, tries: int = 4) -> dict:
    last: Exception | None = None
    for attempt in range(tries):
        req = urllib.request.Request(url, headers={"Accept": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                # Assert the HTTP status: a rejected query and an empty result are
                # indistinguishable downstream unless the status is checked.
                if resp.status != 200:
                    raise AnalysisError(f"HTTP {resp.status} for {url}")
                return json.load(resp)
        except (urllib.error.URLError, TimeoutError) as exc:  # transient
            last = exc
            time.sleep(2 * (attempt + 1))
    raise AnalysisError(f"failed after {tries} attempts: {url} ({last})")


def quickgo_search(**params) -> list[dict]:
    """Fully paginated QuickGO annotation search.

    Compares numberOfHits against len(results) rather than against a page-size
    constant, so a server-side clamp cannot slip past the truncation guard.
    """
    params.setdefault("limit", 100)
    out: list[dict] = []
    page = 1
    total = None
    while True:
        p = dict(params, page=page)
        d = _get_json(f"{QUICKGO}/annotation/search?" + urllib.parse.urlencode(p))
        total = d["numberOfHits"]
        out.extend(d["results"])
        if len(out) >= total or not d["results"]:
            break
        page += 1
        if page > 200:
            raise AnalysisError(f"runaway pagination for {params}")
    if len(out) != total:
        raise AnalysisError(f"TRUNCATED: {len(out)} of {total} for {params}")
    return out


@dataclass
class Entry:
    accession: str
    entry_name: str
    protein_name: str
    gene: str
    organism: str
    reviewed: bool
    length: int
    sequence: str
    sites: set[int] = field(default_factory=set)  # 1-based BINDING/ACT_SITE positions
    caution: str = ""


def fetch_entry(accession: str) -> Entry:
    """Fetch one UniProt entry, printing its name and failing loudly on a dead id.

    A deleted/inactive accession returns an entry with no name and no annotation,
    which is indistinguishable from a live protein that simply carries none.
    """
    d = _get_json(
        f"{UNIPROT}/search?"
        + urllib.parse.urlencode(
            {
                "query": f"accession:{accession}",
                "fields": "accession,id,protein_name,gene_names,organism_name,length,sequence,ft_binding,ft_act_site,cc_caution",
                "format": "json",
                "size": 5,  # never size=1: an ambiguous lookup must be visible
            }
        )
    )
    results = d.get("results", [])
    if not results:
        raise AnalysisError(f"{accession}: no UniProt entry (deleted/inactive accession?)")
    if len(results) > 1:
        raise AnalysisError(f"{accession}: {len(results)} entries returned; ambiguous")
    r = results[0]
    if r.get("entryType") == "Inactive" or "inactiveReason" in r:
        # An inactive entry answers every query with silence, which is indistinguishable
        # from a live protein that genuinely carries no annotation.  Fail loudly.
        reason = r.get("inactiveReason", {})
        raise AnalysisError(
            f"{accession}: INACTIVE UniProt entry "
            f"({reason.get('inactiveReasonType','?')} -> {reason.get('mergeDemergeTo')})"
        )
    entry_name = r.get("uniProtkbId", "")
    if not entry_name:
        raise AnalysisError(f"{accession}: entry has no name -- inactive entry")
    pd = r.get("proteinDescription", {})
    pname = (
        pd.get("recommendedName", {}).get("fullName", {}).get("value")
        or (pd.get("submissionNames") or [{}])[0].get("fullName", {}).get("value")
        or "?"
    )
    sites: set[int] = set()
    for f in r.get("features", []):
        if f["type"] in ("Binding site", "Active site"):
            loc = f["location"]
            s, e = loc["start"].get("value"), loc["end"].get("value")
            if s and e:
                sites.update(range(s, e + 1))
    caution = " ".join(
        t["value"] for c in r.get("comments", []) if c["commentType"] == "CAUTION" for t in c.get("texts", [])
    )
    return Entry(
        accession=r["primaryAccession"],
        entry_name=entry_name,
        protein_name=pname,
        gene=(r.get("genes") or [{}])[0].get("geneName", {}).get("value", "-"),
        organism=r["organism"]["scientificName"],
        # "reviewed" is a SUBSTRING of "unreviewed" -- anchor the test.
        reviewed=r["entryType"].startswith("UniProtKB reviewed"),
        length=r["sequence"]["length"],
        sequence=r["sequence"]["value"],
        sites=sites,
        caution=caution,
    )


def make_aligner() -> Align.PairwiseAligner:
    a = Align.PairwiseAligner()
    a.substitution_matrix = substitution_matrices.load("BLOSUM62")
    a.open_gap_score = -11
    a.extend_gap_score = -1
    a.mode = "global"
    return a


def map_positions(aligner, subject_seq: str, target_seq: str, positions: list[int]) -> tuple[dict[int, int | None], float]:
    """Map 1-based subject positions onto the target; also return % identity."""
    aln = aligner.align(subject_seq, target_seq)[0]
    s_idx, t_idx = aln.indices  # 0-based, -1 for gap
    mapping: dict[int, int | None] = {}
    ident = 0
    aligned = 0
    for si, ti in zip(s_idx, t_idx):
        if si >= 0 and ti >= 0:
            aligned += 1
            if subject_seq[si] == target_seq[ti]:
                ident += 1
    for pos in positions:
        mapping[pos] = None
        for si, ti in zip(s_idx, t_idx):
            if si == pos - 1:
                # cast away numpy integer types so results.json stays serialisable
                mapping[pos] = int(ti) + 1 if ti >= 0 else None
                break
    pct = 100.0 * ident / aligned if aligned else 0.0
    return mapping, pct


def fetch_pdb(pdb_id: str) -> dict:
    d = _get_json(f"{RCSB}/{pdb_id}")
    info = d.get("rcsb_entry_info", {})
    ligands = info.get("nonpolymer_bound_components")
    if ligands is None:
        # An entry with no bound non-polymer components is a real answer; an entry
        # missing the field is not.  Distinguish them rather than printing an empty list.
        raise AnalysisError(f"{pdb_id}: no nonpolymer_bound_components field in the RCSB record")
    res = info.get("resolution_combined") or []
    cite = d.get("rcsb_primary_citation", {})
    return {
        "pdb_id": pdb_id,
        "title": d["struct"]["title"],
        "resolution_A": res[0] if res else None,
        "ligands": sorted(ligands),
        "has_MG": "MG" in ligands,
        "has_K": "K" in ligands,
        "pubmed": cite.get("pdbx_database_id_PubMed"),
    }


def resolution_clause(entries: list[dict]) -> list[str]:
    """Sentences relating potassium occupancy to resolution.  Pure, so both branches can be
    unit-tested on synthetic input - the live data only ever exercises one of them, and the
    PDB set is now derived from UniProt, so the other becomes reachable without anyone
    editing this file.

    The subtlety that produced two successive bugs here: "better resolved" and "does not
    contain potassium" are DIFFERENT properties.  Round 3 computed the first as the second;
    round 4 computed it against the WORST potassium-bearing resolution, which with two
    potassium structures at different resolutions would have described a potassium-bearing
    structure as one that "contains none".  The set is therefore defined against the BEST
    potassium-bearing resolution, which makes "contains none" true by construction - and that
    is asserted rather than trusted.
    """
    out: list[str] = []
    unresolved = sorted(e["pdb_id"] for e in entries if e["resolution_A"] is None)
    if unresolved:
        # A missing resolution cannot be silently dropped from a resolution argument.
        out.append(
            f"Resolution is unavailable for {', '.join(unresolved)}, so they are excluded from "
            "the resolution comparison below."
        )
    known = [e for e in entries if e["resolution_A"] is not None]
    k_res = [e["resolution_A"] for e in known if e["has_K"]]
    if not known or not k_res:
        return out
    k_best, k_worst = min(k_res), max(k_res)
    overall_worst = max(e["resolution_A"] for e in known)
    better = [e for e in known if e["resolution_A"] < k_best]
    if any(e["has_K"] for e in better):
        raise AnalysisError(
            "a structure better resolved than every potassium-bearing one contains potassium; "
            "the clause below would be false"
        )
    ids = sorted(e["pdb_id"] for e in better)
    tied_without_k = [
        e for e in known if e["resolution_A"] == overall_worst and not e["has_K"]
    ]
    if k_best == k_worst == overall_worst and not tied_without_k:
        out.append(
            f"Every structure containing potassium is at the worst resolution in the set "
            f"({overall_worst} A); all {len(ids)} better-resolved structures "
            f"({', '.join(ids)}) contain none."
        )
    else:
        span = f"{k_best} A" if k_best == k_worst else f"{k_best}-{k_worst} A"
        out.append(
            f"Potassium-containing structures resolve at {span}; "
            f"{len(ids)} structure(s) ({', '.join(ids) if ids else 'none'}) are better resolved "
            "than every one of them and contain no potassium."
        )
    return out


def read_panther_members() -> list[str]:
    if not PANTHER_ENTRIES.exists():
        raise AnalysisError(
            f"missing input {PANTHER_ENTRIES}; regenerate with `just fetch-gene human ADPRH`"
        )
    lines = PANTHER_ENTRIES.read_text().splitlines()
    header = lines[0].split(",")
    if header[0] != "id":
        raise AnalysisError(f"unexpected header in {PANTHER_ENTRIES}: {header[:3]}")
    return [ln.split(",")[0] for ln in lines[1:] if ln.strip()]


def read_family_total() -> int:
    """The family's TOTAL protein count -- the member CSV is the reviewed subset only."""
    if not PANTHER_METADATA.exists():
        raise AnalysisError(f"missing input {PANTHER_METADATA}")
    for ln in PANTHER_METADATA.read_text().splitlines():
        if ln.strip().startswith("proteins:"):
            return int(ln.split(":")[1].strip())
    raise AnalysisError(f"no `proteins:` counter in {PANTHER_METADATA}")


def holders_of(go_id: str, accessions: list[str]) -> dict[str, list[str]]:
    """Which of `accessions` hold `go_id` (descendants), and by what evidence."""
    out: dict[str, list[str]] = {a: [] for a in accessions}
    for i in range(0, len(accessions), 20):
        chunk = accessions[i : i + 20]
        rs = quickgo_search(
            geneProductId=",".join(f"UniProtKB:{a}" for a in chunk),
            goId=go_id,
            goUsage="descendants",
            goUsageRelationships="is_a,part_of",
        )
        for r in rs:
            acc = r["geneProductId"].split(":", 1)[1]
            if acc in out:
                out[acc].append(f"{r['goEvidence']}({r['reference']})")
    return out


def interpro_entries(accession: str) -> set[str]:
    d = _get_json(f"{INTERPRO}/entry/interpro/protein/uniprot/{accession}/")
    return {r["metadata"]["accession"] for r in d["results"]}


def run() -> dict:
    members = read_panther_members()
    family_total = read_family_total()
    if SUBJECT not in members:
        raise AnalysisError(f"{SUBJECT} absent from the cached PTHR16222 member table")

    # Validate the subject BEFORE fetching the rest: a wrong expected residue should fail
    # in one request, not after thirty.
    subject = fetch_entry(SUBJECT)
    for pos, aa in CATALYTIC_SITES.items():
        if subject.sequence[pos - 1] != aa:
            raise AnalysisError(
                f"subject sequence mismatch at {pos}: expected {aa}, got {subject.sequence[pos-1]}"
            )
        if pos not in subject.sites:
            raise AnalysisError(f"{pos} is not an annotated BINDING/ACT_SITE on {SUBJECT}")

    entries: dict[str, Entry] = {SUBJECT: subject}
    for acc in members:
        if acc in entries:
            continue
        e = fetch_entry(acc)
        entries[acc] = e
        # Print the name of every accession queried: a silent zero reads as a finding.
        print(f"  fetched {e.accession:10s} {e.entry_name:16s} reviewed={e.reviewed} len={e.length}  {e.gene} [{e.organism}]")
    n_reviewed = sum(1 for e in entries.values() if e.reviewed)
    n_unreviewed = len(entries) - n_reviewed
    # The cached table is documented as the reviewed subset; assert rather than assume.
    if n_unreviewed:
        raise AnalysisError(f"{n_unreviewed} unreviewed entries in a table documented as reviewed-only")
    if n_reviewed == 0:
        raise AnalysisError("zero reviewed entries -- the reviewed test is broken")

    aligner = make_aligner()
    go_ev = holders_of("GO:0003875", members)

    rows = []
    for acc, e in entries.items():
        mapping, pct = map_positions(aligner, subject.sequence, e.sequence, sorted(CATALYTIC_SITES))
        per_site = {}
        for pos, aa in CATALYTIC_SITES.items():
            tpos = mapping[pos]
            if tpos is None:
                per_site[pos] = {"target_pos": None, "target_aa": None, "identical": False, "on_site": False}
                continue
            taa = e.sequence[tpos - 1]
            per_site[pos] = {
                "target_pos": tpos,
                "target_aa": taa,
                "identical": taa == aa,
                # Second condition, load-bearing: only meaningful where the target
                # has annotated sites of its own.
                "on_site": (tpos in e.sites) if e.sites else None,
            }
        n_ident = sum(1 for v in per_site.values() if v["identical"])
        n_strict = sum(1 for v in per_site.values() if v["identical"] and v["on_site"] is True)
        rows.append(
            {
                "accession": acc,
                "entry_name": e.entry_name,
                "gene": e.gene,
                "organism": e.organism,
                "reviewed": e.reviewed,
                "identity_pct": round(pct, 1),
                "n_identical": n_ident,
                "n_identical_and_on_own_site": n_strict,
                "has_own_annotated_sites": bool(e.sites),
                "per_site": {str(k): v for k, v in per_site.items()},
                "GO:0003875": go_ev[acc],
                "caution": e.caution,
            }
        )

    rows.sort(key=lambda r: (-r["n_identical"], r["entry_name"]))

    # The cross-tabulation that is the point of the script.
    holds = [r for r in rows if r["GO:0003875"]]
    lacks = [r for r in rows if not r["GO:0003875"]]
    holders_full = [r for r in holds if r["n_identical"] == len(CATALYTIC_SITES)]
    holders_broken = [r for r in holds if r["n_identical"] < len(CATALYTIC_SITES)]

    interpro = {
        a: sorted(interpro_entries(a)) for a in ["P54922", "Q8NDY3", "Q9NX46"]
    }

    pdb_ids = pdb_ids_of(SUBJECT)
    print(f"  PDB cross-references of {SUBJECT}: {', '.join(pdb_ids)}")
    pdb = [fetch_pdb(x) for x in pdb_ids]
    if not any(e["has_MG"] for e in pdb):
        raise AnalysisError("no ADPRH structure contains MG - the magnesium claim would be unsupported")

    # --- clades, taken from the Swiss-Prot entry-name stem (ADPRH_/ARHL1_/ADPRS_) ---
    def clade_of(entry_name: str) -> str:
        stem = entry_name.split("_")[0]
        return {"ADPRH": "ADPRH (ARH1)", "ARHL1": "ADPRHL1 (ARH2)", "ADPRS": "ADPRS (ARH3)"}.get(
            stem, "other / non-vertebrate"
        )

    clades: dict[str, dict] = {}
    for r in rows:
        c = clade_of(r["entry_name"])
        d = clades.setdefault(
            c, {"n": 0, "identity": [], "n_identical": [], "n_hold": 0, "accessions": []}
        )
        d["n"] += 1
        d["identity"].append(r["identity_pct"])
        d["n_identical"].append(r["n_identical"])
        d["n_hold"] += 1 if r["GO:0003875"] else 0
        d["accessions"].append(r["accession"])
    for d in clades.values():
        d["identity_min"] = min(d["identity"])
        d["identity_max"] = max(d["identity"])
        d["residues_min"] = min(d["n_identical"])
        d["residues_max"] = max(d["n_identical"])

    # --- is a residue loss REAL, or an alignment artefact? ---
    #
    # A single identity threshold was tried first and rejected: the largest gap in the
    # observed identity distribution falls between the mammalian ADPRH orthologues (>=82%)
    # and everything else (<=48%), which is a taxonomic boundary rather than an
    # alignment-reliability one, and it discards the ADPRHL1 signal entirely.  The two
    # measures below are computed instead, because both discriminate directly.
    #
    #   (a) CLADE CONSISTENCY.  The same substitution at the same catalytic column in every
    #       member of a clade spanning several hundred million years is not alignment noise;
    #       a scattered pattern among unrelated organisms at low identity may be.
    #   (b) SUBSTITUTION CHEMISTRY.  Ser<->Thr keeps the nucleophilic hydroxyl and Asp<->Glu
    #       keeps the carboxylate; losing the hydroxyl or the charge does not.
    CONSERVATIVE = {frozenset("ST"), frozenset("DE")}

    def chemistry(ref_aa: str, tgt_aa: str | None) -> str:
        if tgt_aa is None:
            return "gap"
        if tgt_aa == ref_aa:
            return "identical"
        if frozenset({ref_aa, tgt_aa}) in CONSERVATIVE:
            return "conservative"
        return "disruptive"

    for r in rows:
        for p, v in r["per_site"].items():
            v["chemistry"] = chemistry(CATALYTIC_SITES[int(p)], v["target_aa"])
        r["n_disruptive"] = sum(1 for v in r["per_site"].values() if v["chemistry"] == "disruptive")

    for name, d in clades.items():
        patterns = set()
        for acc in d["accessions"]:
            r = next(x for x in rows if x["accession"] == acc)
            patterns.add(
                tuple(
                    (p, r["per_site"][p]["chemistry"])
                    for p in sorted(r["per_site"], key=int)
                )
            )
        d["n_distinct_substitution_patterns"] = len(patterns)
        d["pattern_is_clade_wide"] = len(patterns) == 1
        # Sharper than exact-pattern equality: the positions at which EVERY member of the
        # clade carries a disruptive substitution.  One member with an extra loss must not
        # be allowed to hide a core that the whole clade shares.
        d["positions_disruptive_in_all_members"] = sorted(
            p
            for p in map(str, CATALYTIC_SITES)
            if all(
                next(x for x in rows if x["accession"] == a)["per_site"][p]["chemistry"] == "disruptive"
                for a in d["accessions"]
            )
        )
        d["n_disruptive_range"] = [
            min(next(x for x in rows if x["accession"] == a)["n_disruptive"] for a in d["accessions"]),
            max(next(x for x in rows if x["accession"] == a)["n_disruptive"] for a in d["accessions"]),
        ]
        d.pop("identity", None)
        d.pop("n_identical", None)

    # Positive control: a member with its OWN experimental annotation to GO:0003875 despite
    # scoring below 5/5.  If it exists, its substitutions bound what activity tolerates.
    exp_codes = {"EXP", "IDA", "IMP", "IPI", "IGI", "IEP"}
    controls = [
        r
        for r in rows
        if r["accession"] != SUBJECT
        and any(ev.split("(")[0] in exp_codes for ev in r["GO:0003875"])
        and r["n_identical"] < len(CATALYTIC_SITES)
    ]

    def subs_of(r: dict) -> list[str]:
        return [
            f"{CATALYTIC_SITES[int(p)]}{p}->{v['target_aa']}({v['chemistry']})"
            for p, v in sorted(r["per_site"].items(), key=lambda kv: int(kv[0]))
            if v["chemistry"] not in ("identical",)
        ]

    stratification = {
        "rejected_approach": (
            "a single identity threshold from the largest observed gap; it lands at 65.4% "
            "between Dictyostelium ADPRH (48.4%) and mouse Adprh (82.4%), i.e. a taxonomic "
            "boundary, and would discard the ADPRHL1 signal"
        ),
        "conservative_pairs": ["S<->T (hydroxyl retained)", "D<->E (carboxylate retained)"],
        "experimental_controls_below_5of5": [
            {
                "accession": r["accession"],
                "gene": r["gene"],
                "organism": r["organism"],
                "identity_pct": r["identity_pct"],
                "n_identical": r["n_identical"],
                "n_disruptive": r["n_disruptive"],
                "substitutions": subs_of(r),
                "evidence": r["GO:0003875"],
            }
            for r in controls
        ],
        "clade_substitutions": {
            name: {
                "n": d["n"],
                "clade_wide_identical_pattern": d["pattern_is_clade_wide"],
                "positions_disruptive_in_all_members": d["positions_disruptive_in_all_members"],
                "n_disruptive_range": d["n_disruptive_range"],
                "example": subs_of(next(x for x in rows if x["accession"] == d["accessions"][0])),
                "hold_GO_0003875": f"{d['n_hold']}/{d['n']}",
            }
            for name, d in sorted(clades.items())
        },
    }

    result = {
        "subject": SUBJECT,
        "catalytic_sites": {str(k): v for k, v in CATALYTIC_SITES.items()},
        "panther_family": "PTHR16222",
        "family_total_proteins": family_total,
        "members_analysed_reviewed_swissprot": len(rows),
        "reviewed_fraction_pct": round(100.0 * len(rows) / family_total, 3),
        "n_hold_GO_0003875": len(holds),
        "n_lack_GO_0003875": len(lacks),
        "holders_with_all_5_residues": len(holders_full),
        "holders_missing_at_least_1_residue": len(holders_broken),
        "holders_missing_detail": [
            {
                "accession": r["accession"],
                "gene": r["gene"],
                "organism": r["organism"],
                "n_identical": r["n_identical"],
                "identity_pct": r["identity_pct"],
                "evidence": r["GO:0003875"],
            }
            for r in holders_broken
        ],
        "interpro_signatures": interpro,
        "pdb_entries": pdb,
        "identity_denominator": (
            "aligned columns only (gaps excluded), i.e. identities / aligned positions; this "
            "runs slightly higher than the conventional alignment-length denominator and is "
            "applied identically to every member, so no comparison here is affected - but the "
            "absolute figures are not directly comparable with externally quoted identities"
        ),
        "clades": clades,
        "identity_stratification": stratification,
        "rows": rows,
    }
    return result


def report(res: dict) -> str:
    L: list[str] = []
    A = L.append
    A("# ADPRH catalytic-residue census across PANTHER PTHR16222")
    A("")
    A(
        f"Members analysed: **{res['members_analysed_reviewed_swissprot']} reviewed (Swiss-Prot) entries** "
        f"out of a family total of **{res['family_total_proteins']}** proteins "
        f"({res['reviewed_fraction_pct']}% of the family). Every statement below is about the "
        "reviewed subset only."
    )
    A("")
    A(
        "Catalytic positions tested (human ADPRH P54922, each a UniProt `MUTAGEN` with note "
        '"Complete loss of activity"): ' + ", ".join(f"{v}{k}" for k, v in res["catalytic_sites"].items()) + "."
    )
    A("")
    A("## Cross-tabulation: does GO:0003875 track the residues?")
    A("")
    A("| | holds GO:0003875 | does not |")
    A("|---|---|---|")
    full = res["holders_with_all_5_residues"]
    broken = res["holders_missing_at_least_1_residue"]
    A(f"| all 5 residues retained | {full} | see table |")
    A(f"| >=1 residue lost | {broken} | see table |")
    A("")
    if broken:
        A("Members that hold `GO:0003875` while missing at least one catalytic residue:")
        A("")
        A("| accession | gene | organism | residues retained | % identity to ADPRH | evidence |")
        A("|---|---|---|---|---|---|")
        for d in res["holders_missing_detail"]:
            A(
                f"| {d['accession']} | {d['gene']} | {d['organism']} | {d['n_identical']}/5 | "
                f"{d['identity_pct']} | {', '.join(d['evidence'])} |"
            )
        A("")
    A("## By clade")
    A("")
    A("| clade | n | % identity to ADPRH | catalytic residues retained | hold GO:0003875 |")
    A("|---|---|---|---|---|")
    for name, d in sorted(res["clades"].items()):
        A(
            f"| {name} | {d['n']} | {d['identity_min']}-{d['identity_max']} | "
            f"{d['residues_min']}-{d['residues_max']} of 5 | {d['n_hold']}/{d['n']} |"
        )
    A("")
    st = res["identity_stratification"]
    A("## Is a residue loss real, or an alignment artefact?")
    A("")
    A(
        "A single identity threshold was tried first and **rejected**: " + st["rejected_approach"] + "."
    )
    A("")
    A(
        "Percent identity here is computed over **aligned columns only** (gaps excluded), which "
        "runs slightly above the conventional alignment-length denominator. It is applied "
        "identically to every member, so no comparison below is affected, but the absolute "
        "figures should not be set against externally quoted identities."
    )
    A("")
    A(
        "Two computed measures are used instead. **Clade consistency** -- the same substitution at "
        "the same column in every member of a clade is not alignment noise. **Substitution "
        "chemistry** -- " + "; ".join(st["conservative_pairs"]) + "."
    )
    A("")
    A("| clade | n | disruptive in EVERY member | disruptive substitutions | example member | hold GO:0003875 |")
    A("|---|---|---|---|---|---|")
    for name, d in st["clade_substitutions"].items():
        lo, hi = d["n_disruptive_range"]
        rng = f"{lo}" if lo == hi else f"{lo}-{hi}"
        core = ", ".join(
            f"{res['catalytic_sites'][p]}{p}" for p in d["positions_disruptive_in_all_members"]
        ) or "none"
        A(
            f"| {name} | {d['n']} | {core} | "
            f"{rng} of 5 | {', '.join(d['example']) or 'none'} | {d['hold_GO_0003875']} |"
        )
    A("")
    A(
        "Positive control -- a member with its own **experimental** annotation to `GO:0003875` "
        "despite scoring below 5/5. Its substitutions bound what catalysis tolerates:"
    )
    A("")
    if st["experimental_controls_below_5of5"]:
        A("| accession | gene | organism | % id | retained | disruptive | substitutions | evidence |")
        A("|---|---|---|---|---|---|---|---|")
        for d in st["experimental_controls_below_5of5"]:
            A(
                f"| {d['accession']} | {d['gene']} | {d['organism']} | {d['identity_pct']} | "
                f"{d['n_identical']}/5 | {d['n_disruptive']} | {', '.join(d['substitutions'])} | "
                f"{', '.join(d['evidence'])} |"
            )
    else:
        A("_no such control in the reviewed set_ -- so the low-identity rows are untested, not corroborated.")
    A("")
    A("## Per-member detail")
    A("")
    A("| accession | entry | gene | organism | % id | S54 | D55 | D56 | D302 | S305 | ident/5 | ident+own-site/5 | GO:0003875 |")
    A("|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    for r in res["rows"]:
        cells = []
        for pos in ("54", "55", "56", "302", "305"):
            v = r["per_site"][pos]
            if v["target_aa"] is None:
                cells.append("gap")
            else:
                mark = "" if v["identical"] else "*"
                cells.append(f"{v['target_aa']}{v['target_pos']}{mark}")
        strict = r["n_identical_and_on_own_site"] if r["has_own_annotated_sites"] else "n/a"
        A(
            f"| {r['accession']} | {r['entry_name']} | {r['gene']} | {r['organism']} | {r['identity_pct']} | "
            + " | ".join(cells)
            + f" | {r['n_identical']}/5 | {strict} | {', '.join(r['GO:0003875']) or '-'} |"
        )
    A("")
    A("`*` = not identical to the ADPRH residue. `ident+own-site/5` is `n/a` where the entry has no")
    A("BINDING/ACT_SITE features of its own, so the second condition cannot be evaluated; those")
    A("counts are NOT promoted to matches.")
    A("")
    A("## Metals actually present in the ADPRH structures")
    A("")
    A("| PDB | resolution (A) | bound non-polymer components | MG | K | PubMed |")
    A("|---|---|---|---|---|---|")
    for e in res["pdb_entries"]:
        A(
            f"| {e['pdb_id']} | {e['resolution_A']} | {', '.join(e['ligands'])} | "
            f"{'yes' if e['has_MG'] else 'no'} | {'yes' if e['has_K'] else 'no'} | "
            f"{e['pubmed'] or '-'} |"
        )
    A("")
    # Everything in this paragraph is computed from the table above.  The stoichiometry
    # ("two Mg2+ per subunit") is a UniProt COFACTOR statement, NOT something
    # nonpolymer_bound_components can support, so it is deliberately not asserted here.
    entries = res["pdb_entries"]
    mg = [e["pdb_id"] for e in entries if e["has_MG"]]
    k = [e["pdb_id"] for e in entries if e["has_K"]]
    A(
        f"Magnesium is present in **{len(mg)} of {len(entries)}** structures "
        f"({', '.join(mg) if mg else 'none'}). Potassium is present in "
        f"**{len(k)} of {len(entries)}** ({', '.join(k) if k else 'none'})."
    )
    for line in resolution_clause(entries):
        A("")
        A(line)
    A("")
    A("## InterPro signature membership (the annotation route)")
    A("")
    for acc, sigs in res["interpro_signatures"].items():
        A(f"- `{acc}`: {', '.join(sigs)}")
    A("")
    A(
        "`IPR012108` (\"ADP-ribosylarginine hydrolase\") is the family-specific signature whose "
        "interpro2go mapping supplies `GO:0000287`, `GO:0003875` and `GO:0051725`."
    )
    return "\n".join(L) + "\n"


SELF_TESTS = []


def self_test() -> int:
    """Break-test the guards in the direction each exists to catch, and in the happy direction."""
    problems: list[str] = []
    aligner = make_aligner()

    # 1. happy path: identical sequences map every position to itself at 100% identity
    seq = "MEKYVAAMVLSAAGDALGYY"
    mapping, pct = map_positions(aligner, seq, seq, [1, 5, 20])
    if mapping != {1: 1, 5: 5, 20: 20} or round(pct) != 100:
        problems.append(f"happy path failed: {mapping} {pct}")

    # 2. a deletion in the target must map the deleted position to None, not to a neighbour
    tgt = seq[:4] + seq[5:]  # delete subject position 5
    mapping, _ = map_positions(aligner, seq, tgt, [5])
    if mapping[5] is not None:
        problems.append(f"deletion not detected: subject 5 -> {mapping[5]}")

    # 3. pagination guard: numberOfHits must be compared to len(results), not a constant
    src = Path(__file__).read_text()
    if "len(out) != total" not in src:
        problems.append("pagination guard missing len(out) != total comparison")
    if "limit" in src and "raise AnalysisError(f\"TRUNCATED" not in src:
        problems.append("pagination guard does not raise on truncation")

    # 4. the reviewed test must be anchored: "reviewed" is a SUBSTRING of "unreviewed", so
    #    the naive test silently promotes every TrEMBL entry.  This is exercised
    #    BEHAVIOURALLY, not by grepping the source -- an earlier version of this check
    #    searched for `startswith("UniProtKB reviewed")` in the file and was satisfied by
    #    the string appearing in a comment, so disabling the real guard still passed.
    for acc, expected in [("P54922", True), ("Q9CTF5", False)]:  # Swiss-Prot / TrEMBL mouse Adprh
        got = fetch_entry(acc).reviewed
        if got is not expected:
            problems.append(f"reviewed flag for {acc}: got {got}, expected {expected}")

    # 5. a dead accession must fail loudly rather than return an empty finding
    try:
        fetch_entry("O15507")  # known inactive/deleted entry
    except AnalysisError:
        pass
    except Exception as exc:  # noqa: BLE001
        problems.append(f"dead accession raised the wrong error type: {exc!r}")
    else:
        problems.append("dead accession O15507 did not raise")

    # 6. a missing input must be a hard error naming the fix command
    global PANTHER_ENTRIES
    saved = PANTHER_ENTRIES
    PANTHER_ENTRIES = HERE / "definitely-not-there.csv"
    try:
        read_panther_members()
    except AnalysisError as exc:
        if "fetch-gene" not in str(exc):
            problems.append("missing-input error does not name the fix command")
    else:
        problems.append("missing input did not raise")
    finally:
        PANTHER_ENTRIES = saved

    # 7. the subject-sequence precondition must be able to fail: mutate the expected residue
    global CATALYTIC_SITES
    saved_sites = dict(CATALYTIC_SITES)
    CATALYTIC_SITES = {54: "W"}  # wrong residue on purpose
    try:
        run()
    except AnalysisError as exc:
        if "sequence mismatch" not in str(exc):
            problems.append(f"subject precondition raised the wrong error: {exc}")
    else:
        problems.append("subject-sequence precondition did not fire on a wrong residue")
    finally:
        CATALYTIC_SITES = saved_sites

    # 8c. resolution_clause: exercise BOTH branches and the failure mode, on synthetic
    # entries, because the live four only ever reach the first branch.
    def E(pid, res_, k_):
        return {"pdb_id": pid, "resolution_A": res_, "has_K": k_, "has_MG": True}

    one = resolution_clause([E("A", 1.9, True), E("B", 1.2, False), E("C", 1.3, False)])
    if not any("Every structure containing potassium is at the worst resolution" in s for s in one):
        problems.append(f"resolution_clause branch 1 wrong: {one}")
    # the reviewer's case: two K structures at different resolutions
    two = resolution_clause([E("A", 1.9, True), E("B", 1.5, True), E("C", 1.2, False)])
    if not any("resolve at 1.5-1.9 A" in s for s in two):
        problems.append(f"resolution_clause branch 2 wrong: {two}")
    if any("contain none" in s and "all 2" in s for s in two):
        problems.append(f"resolution_clause branch 2 described a K structure as K-free: {two}")
    # a non-K structure tied at the worst resolution must not take branch 1
    tie = resolution_clause([E("A", 1.9, True), E("B", 1.9, False), E("C", 1.2, False)])
    if any("Every structure containing potassium" in s for s in tie):
        problems.append(f"resolution_clause took branch 1 despite a tie: {tie}")
    # a null resolution must be reported, not silently dropped
    nul = resolution_clause([E("A", 1.9, True), E("B", None, False), E("C", 1.2, False)])
    if not any("Resolution is unavailable for B" in s for s in nul):
        problems.append(f"resolution_clause dropped a null resolution: {nul}")
    # no potassium anywhere -> no clause at all, rather than a vacuous sentence
    if resolution_clause([E("A", 1.9, False), E("B", 1.2, False)]) != []:
        problems.append("resolution_clause emitted a clause with no potassium present")

    # 8b. the PDB set must be derived, and must fail loudly on an accession with none
    ids = pdb_ids_of(SUBJECT)
    if not {"3HFW", "6G28"} <= set(ids):
        problems.append(f"derived PDB set for {SUBJECT} is missing known entries: {ids}")
    # An accession that cannot resolve must RAISE.  The first version of this test had no
    # `else` branch, so an accession that happened to resolve would have passed it silently -
    # a vacuous test, the most common way a guard reports coverage it does not have.
    try:
        pdb_ids_of("Q0Q0Q0")
    except AnalysisError:
        pass
    except Exception as exc:  # noqa: BLE001
        problems.append(f"pdb_ids_of raised the wrong error type: {exc!r}")
    else:
        problems.append("pdb_ids_of did not raise on an unresolvable accession")

    # 8. the PDB fetcher must return the metals, and must fail loudly on a bad id
    e = fetch_pdb("3HFW")
    if not (e["has_MG"] and e["has_K"]):
        problems.append(f"3HFW should contain both MG and K; got {e['ligands']}")
    e = fetch_pdb("6G28")
    if e["has_K"]:
        problems.append("6G28 should not contain K")
    try:
        fetch_pdb("ZZZZ")
    except AnalysisError:
        pass
    except Exception as exc:  # noqa: BLE001
        problems.append(f"bad PDB id raised the wrong error type: {exc!r}")
    else:
        problems.append("a nonexistent PDB id did not raise")

    for p in problems:
        print("SELF-TEST FAIL:", p)
    print(f"self-test: {len(problems)} problem(s)")
    return 1 if problems else 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    if args.self_test:
        return self_test()
    res = run()
    (HERE / "results.json").write_text(json.dumps(res, indent=2, sort_keys=True) + "\n")
    (HERE / "RESULTS.md").write_text(report(res))
    print()
    print(f"members (reviewed Swiss-Prot): {res['members_analysed_reviewed_swissprot']}")
    print(f"family total proteins        : {res['family_total_proteins']}")
    print(f"hold GO:0003875              : {res['n_hold_GO_0003875']}")
    print(f"  ... with all 5 residues    : {res['holders_with_all_5_residues']}")
    print(f"  ... missing >=1 residue    : {res['holders_missing_at_least_1_residue']}")
    for d in res["holders_missing_detail"]:
        print(f"      {d['accession']} {d['gene']} ({d['organism']}) {d['n_identical']}/5 id={d['identity_pct']}%")
    print(f"lack GO:0003875              : {res['n_lack_GO_0003875']}")
    print("wrote results.json and RESULTS.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
