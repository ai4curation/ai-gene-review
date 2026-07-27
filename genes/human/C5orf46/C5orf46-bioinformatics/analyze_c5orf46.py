#!/usr/bin/env python3
"""Reproducible checks supporting the human C5orf46 (Q6UWT4) GO annotation review.

Every claim this script makes is computed here, and every *reported zero* is paired
with a positive control from the same endpoint in the same call pattern, so that a
rejected query cannot be mistaken for a negative result.

What it establishes
-------------------
A. MOLECULAR IDENTITY of the assayed peptide.
   PMID:33804835 names its molecule "AP-64" and states MW = 7.2 and PI = 4.54.
   Recomputing length, molecular weight and isoelectric point from UniProt's own
   annotated mature CHAIN of Q6UWT4 reproduces all three, which is what licenses
   using that paper as evidence about *this gene product* rather than about a
   synthetic fragment. (Positive control: the same MW routine must reproduce the
   full precursor mass UniProt states in its SQ line.)

B. AMPHIPATHICITY and where the hydrophobic maximum sits.
   Kyte-Doolittle over the precursor. Used only for the narrow claim that the
   uncleaved signal peptide is the most hydrophobic window in the construct that
   was used as a two-hybrid bait.

C. PARTNER-SET COMPOSITION for the 14 GO:0005515 rows.
   Partner accessions are parsed FROM the GOA TSV (never hand-listed) and are
   asserted to equal the set QuickGO returns. For each: reviewed status by exact
   prefix (never `"reviewed" in entryType`, which also matches "unreviewed"),
   length against the canonical entry for the same gene, transmembrane-feature
   count, and subcellular locations.

D. INTERACTION PROVENANCE from IntAct.
   Distinct publications, detection methods, and whether a partner's record count
   is independent experiments or sub-methods of one screen. Plus promiscuity:
   distinct interaction partners per protein, fully paginated.

E. THE ANNOTATION COVERAGE GAP, quantified.
   Evidence-code census for Q6UWT4; IBA count with two positive controls; the
   number of GOA annotations citing PMID:33804835 anywhere, with a positive
   control reference; and the annotation state of the two other reviewed members
   of PANTHER PTHR37864.

Usage
-----
    uv run python analyze_c5orf46.py             # use committed data/ cache
    uv run python analyze_c5orf46.py --refresh   # re-fetch from the web
    uv run python analyze_c5orf46.py --self-test # break-test every guard

`--self-test` exercises each guard in the direction it exists to catch AND asserts
the *message*, not merely that something failed.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.parse
import urllib.request
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
GOA_TSV = HERE.parent / "C5orf46-goa.tsv"
UNIPROT_TXT = HERE.parent / "C5orf46-uniprot.txt"
PANTHER_CSV = HERE.parents[3] / "interpro" / "panther" / "PTHR37864" / "PTHR37864-entries.csv"

SUBJECT = "Q6UWT4"
AP64_PAPER = "PMID:33804835"

# Positive controls. Each exists to make a reported zero falsifiable.
IBA_CONTROLS = {"Q96PE1": "ADGRA2", "P60709": "ACTB"}
REFERENCE_CONTROL = "PMID:19199708"  # the exosome HDA reference; must be non-zero

REVIEWED_PREFIX = "UniProtKB reviewed"

# Monoisotopic-free average residue masses (Da) + one water for the peptide bond count.
AA_MASS = {
    "A": 71.0788, "R": 156.1875, "N": 114.1038, "D": 115.0886, "C": 103.1388,
    "E": 129.1155, "Q": 128.1307, "G": 57.0519, "H": 137.1411, "I": 113.1594,
    "L": 113.1594, "K": 128.1741, "M": 131.1926, "F": 147.1766, "P": 97.1167,
    "S": 87.0782, "T": 101.1051, "W": 186.2132, "Y": 163.1760, "V": 99.1326,
}
WATER = 18.01524

# Kyte & Doolittle (1982) hydropathy index.
KD = {
    "A": 1.8, "R": -4.5, "N": -3.5, "D": -3.5, "C": 2.5, "E": -3.5, "Q": -3.5,
    "G": -0.4, "H": -3.2, "I": 4.5, "L": 3.8, "K": -3.9, "M": 1.9, "F": 2.8,
    "P": -1.6, "S": -0.8, "T": -0.7, "W": -0.9, "Y": -1.3, "V": 4.2,
}
KD_WINDOW = 19

# Bjellqvist-style pK set, sufficient to reproduce a one-decimal pI.
PK = {"Nterm": 7.5, "Cterm": 3.55, "D": 4.05, "E": 4.45, "C": 9.0,
      "Y": 10.0, "H": 5.98, "K": 10.0, "R": 12.0}


class CheckError(Exception):
    """Raised by a guard. Collected, never allowed to abort later checks."""


# --------------------------------------------------------------------------- IO


def _cache_path(key: str) -> Path:
    return DATA / (re.sub(r"[^A-Za-z0-9._-]", "_", key) + ".json")


def _get_json(url: str, cache_key: str, refresh: bool, project=None,
              compact: bool = False) -> dict:
    """Fetch JSON, caching under data/ so the analysis is reproducible offline.

    `project` narrows a response to the fields this analysis reads, *before* caching.
    IntAct returns every cross-reference of both partners on every record, which for
    a hub like AQP6 is tens of megabytes per page; the full set came to 532 MB, which
    is not committable. Projection keeps the cache under a megabyte while preserving
    `totalElements`, so the anti-truncation assertion still has something to check.
    """
    path = _cache_path(cache_key)
    if path.exists() and not refresh:
        return json.loads(path.read_text())
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    with urllib.request.urlopen(req) as resp:
        status = resp.status
        body = resp.read()
    if status != 200:
        raise CheckError(f"HTTP {status} for {url}")
    d = json.loads(body)
    if project is not None:
        d = project(d)
    DATA.mkdir(parents=True, exist_ok=True)
    # Indented by default so a reviewer can read the cache. `compact` is for the
    # id-only interaction caches, where indentation costs ~22,000 lines of partner
    # accessions that nobody will read and that only bloat the diff.
    if compact:
        path.write_text(json.dumps(d, sort_keys=True, separators=(",", ":")) + "\n")
    else:
        path.write_text(json.dumps(d, indent=1, sort_keys=True) + "\n")
    return d


# The only IntAct fields this analysis reads. Everything else is discarded at cache
# time; see the projection note in _get_json.
INTACT_FIELDS = (
    "ac", "uniqueIdA", "uniqueIdB", "moleculeA", "moleculeB", "detectionMethod",
    "publicationPubmedIdentifier", "intactMiscore", "typeA", "typeB", "type",
    "experimentalRoleA", "experimentalRoleB", "hostOrganism", "expansionMethod",
)


# The promiscuity census needs only the two partner ids per record, so its cache is
# projected harder still: 2 fields instead of 15. Hub proteins dominate the cache size
# (AQP6 alone has 1032 records) and none of their detail is read.
INTACT_ID_FIELDS = ("uniqueIdA", "uniqueIdB")


def _make_intact_projection(fields: tuple[str, ...]):
    def project(d: dict) -> dict:
        if "totalElements" not in d or "content" not in d:
            raise CheckError(f"unexpected IntAct response shape: keys={sorted(d)[:12]}")
        return {
            "totalElements": d["totalElements"],
            "content": [{k: r.get(k) for k in fields} for r in d["content"]],
        }
    return project


_project_intact = _make_intact_projection(INTACT_FIELDS)
_project_intact_ids = _make_intact_projection(INTACT_ID_FIELDS)

# Same treatment for QuickGO: only these annotation fields are read anywhere here.
# numberOfHits is preserved so the anti-truncation assertion keeps working.
QUICKGO_FIELDS = (
    "geneProductId", "goId", "goName", "goAspect", "goEvidence", "qualifier",
    "reference", "assignedBy", "withFrom", "taxonId",
)


def _project_quickgo(d: dict) -> dict:
    if "numberOfHits" not in d or "results" not in d:
        raise CheckError(f"unexpected QuickGO response shape: keys={sorted(d)[:12]}")
    return {
        "numberOfHits": d["numberOfHits"],
        "results": [{k: r.get(k) for k in QUICKGO_FIELDS} for r in d["results"]],
    }


def fetch_uniprot(acc: str, refresh: bool = False) -> dict:
    """Fetch a UniProt entry, asserting the accession did not silently drift.

    A merged or secondary accession returns HTTP 200 with a complete, normal-looking
    reviewed record for a *different* protein; only primaryAccession reveals it.
    """
    # `cc_function` and `cc_similarity` are retained deliberately. A PR review caught that a
    # narrowed projection had dropped FUNCTION, which is exactly the field the SGTA-versus-SGTB
    # correction rests on - "the claim is right; the evidence for it left with the projection".
    # When narrowing a cache, check that nothing asserted still depends on the dropped fields.
    fields = ("accession,id,protein_name,gene_names,length,sequence,"
              "cc_subcellular_location,cc_function,cc_similarity,"
              "ft_transmem,ft_signal,ft_chain")
    url = f"https://rest.uniprot.org/uniprotkb/{acc}.json?fields={fields}"
    d = _get_json(url, f"uniprot_{acc}", refresh)
    got = d.get("primaryAccession")
    if got != acc:
        raise CheckError(
            f"ACCESSION DRIFT: asked for {acc} but primaryAccession is {got} "
            f"({d.get('uniProtkbId')}) - this accession has been merged or replaced"
        )
    return d


def is_reviewed(entry: dict) -> bool:
    """Exact-prefix test. `'reviewed' in entryType` also matches 'unreviewed'."""
    return str(entry.get("entryType", "")).startswith(REVIEWED_PREFIX)


QUICKGO_ANN = "https://www.ebi.ac.uk/QuickGO/services/annotation/search"


def quickgo_hits(refresh: bool = False, **params) -> int:
    """Annotation count only. Cheap, and safe for references with 85k annotations."""
    p = dict(params, limit=1, page=1)
    url = QUICKGO_ANN + "?" + urllib.parse.urlencode(p)
    return _get_json(url, "qg_hits_" + urllib.parse.urlencode(params), refresh,
                     project=_project_quickgo)["numberOfHits"]


def quickgo_all(refresh: bool = False, max_pages: int = 20, **params) -> list[dict]:
    """Fully paginated annotation fetch.

    Asserts numberOfHits == len(results) rather than comparing against a page-size
    constant: if the service clamps instead of erroring, a constant-based guard
    passes while rows were silently dropped.
    """
    results: list[dict] = []
    page, total = 1, None
    while True:
        p = dict(params, limit=100, page=page)
        url = QUICKGO_ANN + "?" + urllib.parse.urlencode(p)
        d = _get_json(url, f"qg_all_{urllib.parse.urlencode(params)}_p{page}", refresh,
                      project=_project_quickgo)
        total = d["numberOfHits"]
        results.extend(d["results"])
        if len(results) >= total or page >= max_pages:
            break
        page += 1
    if total != len(results):
        raise CheckError(
            f"TRUNCATED QuickGO result for {params}: numberOfHits={total} "
            f"but only {len(results)} rows read"
        )
    return results


INTACT_WS = "https://www.ebi.ac.uk/intact/ws/interaction/findInteractions"


def intact_records(acc: str, refresh: bool = False, page_size: int = 500,
                   max_pages: int = 40, ids_only: bool = False) -> list[dict]:
    """Fully paginated IntAct fetch.

    Asserts totalElements == len(content) after paging, never against page_size:
    the service happily returns fewer rows than asked for, so a single-request
    fetch silently truncates any protein with more interactions than the page size
    (AQP6 has 1032, which is how this was found).
    """
    content: list[dict] = []
    page, total = 0, None
    while True:
        url = f"{INTACT_WS}/{acc}?page={page}&pageSize={page_size}"
        # The cache key encodes which projection produced the file, so a narrow cache
        # can never be mistaken for a full one by a later caller that needs the detail.
        suffix = "ids" if ids_only else "full"
        d = _get_json(url, f"intact_{acc}_{suffix}_p{page}", refresh,
                      project=_project_intact_ids if ids_only else _project_intact,
                      compact=ids_only)
        total = d["totalElements"]
        content.extend(d["content"])
        if len(content) >= total or not d["content"] or page >= max_pages:
            break
        page += 1
    if total != len(content):
        raise CheckError(
            f"TRUNCATED IntAct result for {acc}: totalElements={total} "
            f"but only {len(content)} records read"
        )
    return content


# ------------------------------------------------------------------- sequence


def peptide_mass(seq: str) -> float:
    return sum(AA_MASS[c] for c in seq) + WATER


def net_charge(seq: str, ph: float) -> float:
    q = 1.0 / (1 + 10 ** (ph - PK["Nterm"])) - 1.0 / (1 + 10 ** (PK["Cterm"] - ph))
    for aa in ("K", "R", "H"):
        q += seq.count(aa) / (1 + 10 ** (ph - PK[aa]))
    for aa in ("D", "E", "C", "Y"):
        q -= seq.count(aa) / (1 + 10 ** (PK[aa] - ph))
    return q


def isoelectric_point(seq: str) -> float:
    lo, hi = 0.0, 14.0
    for _ in range(100):
        mid = (lo + hi) / 2
        if net_charge(seq, mid) > 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def kd_profile(seq: str, window: int = KD_WINDOW) -> list[tuple[int, float]]:
    half = window // 2
    return [
        (i + 1 + half, sum(KD[c] for c in seq[i:i + window]) / window)
        for i in range(len(seq) - window + 1)
    ]


# ------------------------------------------------------------------- GOA TSV


def read_goa_rows() -> list[dict]:
    lines = GOA_TSV.read_text().splitlines()
    header = lines[0].split("\t")
    idx = {name: i for i, name in enumerate(header)}
    needed = ["GO TERM", "GO EVIDENCE CODE", "REFERENCE", "WITH/FROM", "QUALIFIER"]
    missing = [n for n in needed if n not in idx]
    if missing:
        raise CheckError(f"GOA TSV header lacks {missing}; columns are {header}")
    rows = []
    for line in lines[1:]:
        if not line.strip():
            continue
        f = line.split("\t")
        rows.append({n: f[idx[n]] for n in needed})
    return rows


def goa_binding_partners(rows: list[dict]) -> list[str]:
    """Partner accessions for GO:0005515, taken from the WITH/FROM column."""
    out = []
    for r in rows:
        if r["GO TERM"] != "GO:0005515":
            continue
        for token in r["WITH/FROM"].split("|"):
            token = token.strip()
            if not token:
                continue
            db, _, acc = token.partition(":")
            if db != "UniProtKB":
                raise CheckError(f"unexpected WITH/FROM namespace on a GO:0005515 row: {token}")
            out.append(acc)
    return out


# --------------------------------------------------------------------- checks


def check_a_identity(problems: list[str], refresh: bool, report: dict) -> None:
    """The peptide assayed as AP-64 is UniProt's annotated mature chain of Q6UWT4."""
    entry = fetch_uniprot(SUBJECT, refresh)
    seq = entry["sequence"]["value"]
    stated_mass = entry["sequence"]["molWeight"]

    chains = [f for f in entry.get("features", []) if f["type"] == "Chain"]
    signals = [f for f in entry.get("features", []) if f["type"] == "Signal"]
    if len(chains) != 1 or len(signals) != 1:
        problems.append(f"A: expected exactly one CHAIN and one SIGNAL feature, got "
                        f"{len(chains)} and {len(signals)}")
        return
    c_start = chains[0]["location"]["start"]["value"]
    c_end = chains[0]["location"]["end"]["value"]
    mature = seq[c_start - 1:c_end]
    signal = seq[signals[0]["location"]["start"]["value"] - 1:
                 signals[0]["location"]["end"]["value"]]

    # Positive control for the mass routine: it must reproduce UniProt's own number
    # for the full precursor. Without this, a wrong mass table would silently
    # "confirm" the paper.
    precursor_mass = peptide_mass(seq)
    if abs(precursor_mass - stated_mass) > 1.0:
        problems.append(
            f"A-control: mass routine gives {precursor_mass:.1f} Da for the precursor "
            f"but UniProt states {stated_mass} Da - the mass table is wrong, so the "
            f"mature-peptide numbers below cannot be trusted"
        )
        return

    mat_kda = peptide_mass(mature) / 1000.0
    mat_pi = isoelectric_point(mature)
    report["mature_len"] = len(mature)
    report["mature_kda"] = round(mat_kda, 2)
    report["mature_pi"] = round(mat_pi, 2)
    report["mature_cys"] = mature.count("C")
    report["mature_seq"] = mature
    report["signal_seq"] = signal
    report["precursor_mass_computed"] = round(precursor_mass, 1)
    report["precursor_mass_uniprot"] = stated_mass
    report["mature_acidic"] = mature.count("D") + mature.count("E")
    report["mature_basic"] = mature.count("K") + mature.count("R")

    # The paper's three stated properties of "AP-64".
    if len(mature) != 64:
        problems.append(f"A: mature chain is {len(mature)} aa, not the 64 the name AP-64 asserts")
    if abs(mat_kda - 7.2) > 0.05:
        problems.append(f"A: mature MW {mat_kda:.2f} kDa does not reproduce the paper's 7.2")
    if abs(mat_pi - 4.54) > 0.05:
        problems.append(f"A: mature pI {mat_pi:.2f} does not reproduce the paper's 4.54")
    if mature.count("C") != 0:
        problems.append(f"A: mature chain has {mature.count('C')} cysteines; the paper says none")


def check_b_hydropathy(problems: list[str], refresh: bool, report: dict) -> None:
    """The uncleaved signal peptide is the most hydrophobic window in the bait ORF."""
    entry = fetch_uniprot(SUBJECT, refresh)
    seq = entry["sequence"]["value"]
    prof = kd_profile(seq)
    half = KD_WINDOW // 2
    sig_end = 23
    in_signal = [p for p in prof if p[0] - half <= sig_end]
    in_mature = [p for p in prof if p[0] - half > sig_end]
    if not in_signal or not in_mature:
        problems.append("B: hydropathy profile does not span both signal and mature regions")
        return
    sig_peak = max(in_signal, key=lambda x: x[1])
    mat_peak = max(in_mature, key=lambda x: x[1])
    trough = min(prof, key=lambda x: x[1])
    report["kd_signal_peak"] = (sig_peak[0], round(sig_peak[1], 2))
    report["kd_mature_peak"] = (mat_peak[0], round(mat_peak[1], 2))
    report["kd_trough"] = (trough[0], round(trough[1], 2))
    report["kd_mature_peak_segment"] = seq[mat_peak[0] - 1 - half:mat_peak[0] + half]
    if not sig_peak[1] > mat_peak[1]:
        problems.append(
            f"B: signal-peptide KD-{KD_WINDOW} peak {sig_peak[1]:.2f} is not greater than the "
            f"mature-chain peak {mat_peak[1]:.2f}, so the bait's most hydrophobic window is "
            f"not the signal peptide"
        )


def check_c_partners(problems: list[str], refresh: bool, report: dict) -> None:
    """Partner set from the TSV must equal QuickGO's, then characterise each partner."""
    rows = read_goa_rows()
    tsv_partners = goa_binding_partners(rows)
    report["goa_tsv_data_rows"] = len(rows)
    report["goa_binding_rows"] = sum(1 for r in rows if r["GO TERM"] == "GO:0005515")

    qg = quickgo_all(refresh, geneProductId=f"UniProtKB:{SUBJECT}")
    qg_partners = []
    for a in qg:
        if a["goId"] != "GO:0005515":
            continue
        for e in (a.get("withFrom") or []):
            for x in e.get("connectedXrefs", []):
                qg_partners.append(x["id"])

    # Assert on set MEMBERSHIP, not cardinality: two cancelling errors keep a count
    # correct while corrupting the set in both directions.
    if set(tsv_partners) != set(qg_partners):
        problems.append(
            f"C: partner sets differ - missing from QuickGO {sorted(set(tsv_partners) - set(qg_partners))}, "
            f"unexpected in QuickGO {sorted(set(qg_partners) - set(tsv_partners))}"
        )
    if SUBJECT in set(tsv_partners):
        problems.append("C: the subject appears in its own partner set")

    partners = []
    for acc in sorted(set(tsv_partners)):
        e = fetch_uniprot(acc, refresh)
        gene = (e.get("genes") or [{}])[0].get("geneName", {}).get("value")
        feats = e.get("features", [])
        locs = []
        for c in e.get("comments", []):
            if c["commentType"] == "SUBCELLULAR LOCATION":
                for loc in c.get("subcellularLocations", []):
                    locs.append(loc.get("location", {}).get("value"))
        partners.append({
            "acc": acc,
            "gene": gene,
            "length": e["sequence"]["length"],
            "reviewed": is_reviewed(e),
            "entryType": e["entryType"],
            "transmembrane": sum(1 for f in feats if f["type"] == "Transmembrane"),
            "signal": sum(1 for f in feats if f["type"] == "Signal"),
            "locations": sorted(set(x for x in locs if x)),
            "n_goa_rows": tsv_partners.count(acc),
        })

    n_reviewed = sum(1 for p in partners if p["reviewed"])
    n_naive = sum(1 for p in partners if "reviewed" in p["entryType"])
    if n_naive == n_reviewed and n_reviewed != len(partners):
        problems.append(
            "C-control: the naive `'reviewed' in entryType` test agrees with the exact-prefix "
            "test even though not all partners are reviewed - the anchor check is not discriminating"
        )
    report["partners"] = partners
    report["n_partners"] = len(partners)
    report["n_partners_reviewed"] = n_reviewed
    report["n_partners_reviewed_naive"] = n_naive
    report["n_partners_with_tm"] = sum(1 for p in partners if p["transmembrane"] > 0)
    report["partners_without_tm"] = [p["gene"] for p in partners if p["transmembrane"] == 0]


def check_d_intact(problems: list[str], refresh: bool, report: dict) -> None:
    """Interaction provenance: how many screens, and what a record count counts."""
    recs = intact_records(SUBJECT, refresh)
    rows = []
    for i in recs:
        a, b = i["uniqueIdA"], i["uniqueIdB"]
        if SUBJECT not in (a, b):
            problems.append(f"D: IntAct record {i['ac']} does not involve the subject ({a}/{b})")
            continue
        partner = b if a == SUBJECT else a
        rows.append({
            "partner": partner,
            "name": i["moleculeB"] if a == SUBJECT else i["moleculeA"],
            "method": i.get("detectionMethod"),
            "pub": i.get("publicationPubmedIdentifier"),
            "score": i.get("intactMiscore"),
            "type_a": i.get("typeA"), "type_b": i.get("typeB"),
        })
    if SUBJECT in {r["partner"] for r in rows}:
        problems.append("D: the subject is present in its own IntAct partner set - "
                        "a symptom of a predicate that never fired")
    non_protein = {(r["partner"], r["type_a"], r["type_b"]) for r in rows
                   if r["type_a"] != "protein" or r["type_b"] != "protein"}
    if non_protein:
        problems.append(f"D: non-protein entities in the partner set: {sorted(non_protein)}")

    report["intact_records"] = len(rows)
    report["intact_partners"] = sorted({r["partner"] for r in rows})
    report["intact_publications"] = sorted({r["pub"] for r in rows})
    report["intact_method_by_pub"] = {
        f"{k[0]}|{k[1]}": v for k, v in
        sorted(Counter((r["pub"], r["method"]) for r in rows).items())
    }
    per_partner = {}
    for p in sorted({r["partner"] for r in rows}):
        rs = [r for r in rows if r["partner"] == p]
        per_partner[p] = {
            "name": rs[0]["name"],
            "records": len(rs),
            "publications": sorted({r["pub"] for r in rs}),
            "methods": sorted({str(r["method"]) for r in rs}),
            "miscore": sorted({r["score"] for r in rs}),
        }
    report["intact_per_partner"] = per_partner

    # The claim being tested: for every partner whose records all come from ONE
    # publication, the record count is sub-methods of one screen, not independent
    # experiments. Flag any partner where that reading would be wrong.
    multi_pub = {p: v for p, v in per_partner.items() if len(v["publications"]) > 1}
    report["partners_with_multiple_publications"] = multi_pub
    single_pub_multi_record = {
        p: v for p, v in per_partner.items()
        if len(v["publications"]) == 1 and v["records"] > 1
    }
    report["single_screen_multi_record"] = {
        p: {"records": v["records"], "distinct_methods": len(v["methods"])}
        for p, v in single_pub_multi_record.items()
    }
    if not single_pub_multi_record:
        problems.append("D: no partner has multiple records from a single publication, "
                        "so the sub-method claim has nothing to rest on")


def check_e_promiscuity(problems: list[str], refresh: bool, report: dict) -> None:
    """Distinct interaction partners per protein, subject included as the baseline."""
    accs = [SUBJECT] + report.get("intact_partners", [])
    counts = {}
    for acc in accs:
        try:
            recs = intact_records(acc, refresh, ids_only=True)
        except CheckError as exc:
            problems.append(f"E: {exc}")
            continue
        partners = set()
        for i in recs:
            a, b = i["uniqueIdA"], i["uniqueIdB"]
            partners.add(b if a == acc else a)
        partners.discard(acc)
        counts[acc] = {"records": len(recs), "distinct_partners": len(partners)}
    report["promiscuity"] = counts
    if SUBJECT not in counts:
        problems.append("E: no baseline computed for the subject, so the comparison has no scale")


def check_f_coverage(problems: list[str], refresh: bool, report: dict) -> None:
    """The annotation coverage gap, with a positive control behind every zero."""
    ann = quickgo_all(refresh, geneProductId=f"UniProtKB:{SUBJECT}")
    codes = Counter(a["goEvidence"] for a in ann)
    report["subject_evidence_codes"] = dict(sorted(codes.items()))
    report["subject_total_annotations"] = len(ann)
    report["subject_terms"] = sorted({a["goId"] for a in ann})

    control_iba = {}
    for acc, name in IBA_CONTROLS.items():
        c = Counter(a["goEvidence"] for a in quickgo_all(refresh, geneProductId=f"UniProtKB:{acc}"))
        control_iba[name] = c.get("IBA", 0)
    report["iba_controls"] = control_iba
    if min(control_iba.values(), default=0) == 0:
        problems.append(
            f"F-control: an IBA positive control returned zero IBA rows ({control_iba}), "
            f"so a zero on the subject cannot be distinguished from a rejected query"
        )
    else:
        report["subject_iba"] = codes.get("IBA", 0)

    n_ap64 = quickgo_hits(refresh, reference=AP64_PAPER)
    n_ctrl = quickgo_hits(refresh, reference=REFERENCE_CONTROL)
    report["annotations_citing_ap64_paper"] = n_ap64
    report["annotations_citing_control_reference"] = n_ctrl
    if n_ctrl == 0:
        problems.append(
            f"F-control: the reference positive control {REFERENCE_CONTROL} returned zero "
            f"annotations, so the {AP64_PAPER} zero proves nothing about GOA coverage"
        )

    # Family: the other two reviewed members of PANTHER PTHR37864.
    fam = [l.split(",") for l in PANTHER_CSV.read_text().splitlines()]
    fam_header, fam_rows = fam[0], fam[1:]
    acc_i = fam_header.index("id")
    tax_i = fam_header.index("source_tax_name")
    report["panther_reviewed_members"] = [(r[acc_i], r[tax_i]) for r in fam_rows]
    fam_state = {}
    for r in fam_rows:
        acc = r[acc_i]
        if acc == SUBJECT:
            continue
        rows_ = quickgo_all(refresh, geneProductId=f"UniProtKB:{acc}")
        fam_state[acc] = {
            "taxon": r[tax_i],
            "n": len(rows_),
            "rows": sorted({(a["goId"], a["goEvidence"], a["reference"]) for a in rows_}),
        }
    report["panther_member_annotation_state"] = fam_state


# Curatorial precedents the review's prose leans on. Every other quantitative claim here is
# paired with a cached query; these were originally asserted from an interactive lookup, which
# the PR review correctly flagged as not checkable by any reader of the tree.
PRECEDENTS = {
    "P81605": ("DCD (dermcidin)", "GO:0031640"),   # the anionic cysteine-free comparator
    "Q6UWK7": ("GPR15LG (C10orf99 / AP-57)", "GO:0050830"),
}


def check_g_precedents(problems: list[str], refresh: bool, report: dict) -> None:
    """Verify the curated precedents rather than asserting them."""
    out = {}
    for acc, (label, expected_term) in PRECEDENTS.items():
        entry = fetch_uniprot(acc, refresh)           # asserts primaryAccession
        rows = quickgo_all(refresh, geneProductId=f"UniProtKB:{acc}")
        if not rows:
            problems.append(
                f"G: {acc} ({label}) returned ZERO annotations - a precedent claim cannot rest "
                f"on an empty query, and the subject's own non-empty result shows the endpoint works")
            continue
        holds = sorted({(r["goId"], r["goEvidence"], r["reference"]) for r in rows
                        if r["goId"] == expected_term})
        out[acc] = {
            "label": label,
            "uniprot_name": (entry.get("proteinDescription", {})
                             .get("recommendedName", {}).get("fullName", {}).get("value")),
            "length": entry["sequence"]["length"],
            "reviewed": is_reviewed(entry),
            "total_annotations": len(rows),
            "expected_term": expected_term,
            "expected_term_rows": holds,
            "defense_or_killing_terms": sorted({
                (r["goId"], r["goEvidence"], r["reference"]) for r in rows
                if r["goId"] in ("GO:0031640", "GO:0042742", "GO:0050829", "GO:0050830",
                                 "GO:0050832", "GO:0019731", "GO:0061844", "GO:0140367")}),
        }
        if not holds:
            problems.append(
                f"G: {acc} ({label}) does NOT hold {expected_term} - the precedent asserted in "
                f"the review prose is false and must be removed")
    report["precedents"] = out
    # The subject must NOT hold any of these terms; that absence is the whole point.
    subj = quickgo_all(refresh, geneProductId=f"UniProtKB:{SUBJECT}")
    subj_defense = sorted({r["goId"] for r in subj
                           if r["goId"] in ("GO:0031640", "GO:0042742", "GO:0050829",
                                            "GO:0050830", "GO:0019731", "GO:0061844")})
    report["subject_defense_terms"] = subj_defense
    if subj_defense:
        problems.append(
            f"G: the subject already holds defence/killing terms {subj_defense}, so the two NEW "
            f"proposals are not new - re-check before proposing them")


# The two co-chaperone partners, and the distinction the review's argument turns on. SGTA's
# curated FUNCTION includes hydrophobic-client / transmembrane-domain binding; SGTB's does not.
SGT_PAIR = {"O43765": "SGTA", "Q96EQ0": "SGTB"}
HYDROPHOBIC_CLIENT_CUES = ("hydrophobic", "transmembrane")


def _function_texts(entry: dict) -> list[str]:
    return [txt["value"] for c in entry.get("comments", [])
            if c["commentType"] == "FUNCTION" for txt in c.get("texts", [])]


def check_h_sgt_pair(problems: list[str], refresh: bool, report: dict) -> None:
    """Verify from the cached records which of SGTA/SGTB carries the hydrophobic-client role.

    The review states this asymmetry in fourteen places. It must be checkable from the tree.
    """
    out = {}
    for acc, label in SGT_PAIR.items():
        entry = fetch_uniprot(acc, refresh)           # asserts primaryAccession
        funcs = _function_texts(entry)
        if not funcs:
            problems.append(
                f"H: no FUNCTION comment cached for {acc} ({label}) - the SGTA-versus-SGTB "
                f"claim is not verifiable from this cache, so either widen the projection or "
                f"stop asserting it")
            continue
        joined = " ".join(funcs).lower()
        cues = sorted(c for c in HYDROPHOBIC_CLIENT_CUES if c in joined)
        sims = [txt["value"] for c in entry.get("comments", [])
                if c["commentType"] == "SIMILARITY" for txt in c.get("texts", [])]
        out[acc] = {
            "label": label,
            "n_function_comments": len(funcs),
            "hydrophobic_client_cues": cues,
            "similarity": sims,
            "function_first_120": funcs[0][:120],
        }
    report["sgt_pair"] = out
    if set(out) != set(SGT_PAIR):
        return                                        # a missing record was already reported
    a, b = out["O43765"], out["Q96EQ0"]
    if not a["hydrophobic_client_cues"]:
        problems.append(
            "H: SGTA's cached FUNCTION contains neither 'hydrophobic' nor 'transmembrane', so "
            "the claim that the hydrophobic-client role is curated FOR SGTA is unsupported")
    if b["hydrophobic_client_cues"]:
        problems.append(
            f"H: SGTB's cached FUNCTION does contain {b['hydrophobic_client_cues']}, so the "
            f"claim that the role is curated for SGTA ONLY is false and must be corrected")
    # The pair must also genuinely be one family, which is the corroboration half of the claim.
    if not all("SGT family" in s for v in (a, b) for s in v["similarity"]):
        problems.append(
            f"H: the SGT-family similarity statement is not present on both entries "
            f"(SGTA: {a['similarity']}, SGTB: {b['similarity']}), so describing SGTB as a "
            f"same-family paralogue is not supported by the cache")


CHECKS = [
    ("A molecular identity of the assayed peptide", check_a_identity),
    ("B amphipathicity / hydrophobic maximum", check_b_hydropathy),
    ("C partner-set composition", check_c_partners),
    ("D interaction provenance", check_d_intact),
    ("E partner promiscuity", check_e_promiscuity),
    ("F annotation coverage gap", check_f_coverage),
    ("G curatorial precedents", check_g_precedents),
    ("H SGTA/SGTB hydrophobic-client asymmetry", check_h_sgt_pair),
]


def run(refresh: bool = False) -> tuple[list[str], dict]:
    problems: list[str] = []
    report: dict = {}
    for label, fn in CHECKS:
        try:
            fn(problems, refresh, report)
        except CheckError as exc:
            problems.append(f"{label}: {exc}")
    return problems, report


# ----------------------------------------------------------------- self-tests


def _expect(fn, fragment: str, what: str) -> None:
    """Assert the call fails AND that it fails for the stated reason."""
    try:
        fn()
    except (CheckError, AssertionError) as exc:
        if fragment not in str(exc):
            raise AssertionError(
                f"{what}: failed for the WRONG reason.\n  expected fragment: {fragment}\n"
                f"  actual message  : {exc}"
            ) from exc
        print(f"  ok   {what}")
        return
    raise AssertionError(f"{what}: guard did NOT fire")


def self_test() -> int:
    print("Break-tests (each guard, in the direction it exists to catch):")

    # 1. Merged-accession guard. O15507 returns HTTP 200 and a complete reviewed
    #    record for GFRA1 (P56159); only primaryAccession reveals it.
    _expect(lambda: fetch_uniprot("O15507"), "ACCESSION DRIFT",
            "merged accession O15507 is rejected")

    # ... and the happy direction: a live accession must NOT raise.
    fetch_uniprot(SUBJECT)
    print("  ok   live accession Q6UWT4 is accepted")

    # 2. The mass-table positive control must fire when the table is wrong, and it
    #    must abort before the mature-peptide numbers are reported (otherwise a
    #    wrong table could still "confirm" the paper).
    saved = AA_MASS["D"]
    try:
        AA_MASS["D"] = saved + 5.0
        probs, rep = [], {}
        check_a_identity(probs, False, rep)
        hit = [p for p in probs if "A-control" in p]
        assert hit, f"mass-table control did not fire; problems={probs}"
        assert "mature_kda" not in rep, (
            "mass-table control fired but the mature-peptide numbers were still reported, "
            "so a wrong table would appear to confirm the paper")
        print("  ok   corrupted mass table trips A-control and suppresses the derived numbers")
    finally:
        AA_MASS["D"] = saved

    # 3. Hydropathy direction. Invert the KD scale: the signal peptide must then
    #    stop being the most hydrophobic window.
    saved_kd = dict(KD)
    try:
        for k in KD:
            KD[k] = -saved_kd[k]
        probs, rep = [], {}
        check_b_hydropathy(probs, False, rep)
        assert any("is not greater than the" in p for p in probs), \
            f"hydropathy direction guard did not fire; problems={probs}"
        print("  ok   inverted hydropathy scale trips the B direction guard")
    finally:
        KD.clear()
        KD.update(saved_kd)

    # 4. Partner-set membership guard.
    #
    #    The first version of this break-test dropped `real[-1]`, which is P55061 -
    #    a DUPLICATE, because that accession appears on two GOA rows. Removing it
    #    left the *set* unchanged, so the guard correctly did not fire and the
    #    break-test reported the guard as broken. The mutation has to be as fine as
    #    the claim: mutate DISTINCT membership, not the row list.
    real = goa_binding_partners(read_goa_rows())
    distinct = sorted(set(real))
    assert len(real) == 14 and len(distinct) == 13, (
        f"expected 14 GO:0005515 partner tokens over 13 distinct accessions, "
        f"got {len(real)} over {len(distinct)}")
    dropped = [a for a in real if a != distinct[0]]
    assert set(dropped) != set(real), "the drop mutation did not change the partner SET"
    # Length-preserving substitution: a count-based check cannot see this one.
    swapped = [("P00000" if a == distinct[0] else a) for a in real]
    assert len(swapped) == len(real), "the swap mutation changed the row count"
    assert set(swapped) != set(real), "the swap mutation did not change the partner SET"

    for mutant, label in (
        (dropped, "a dropped partner"),
        (real + ["P00000"], "an invented partner"),
        (swapped, "a substituted partner at IDENTICAL row count"),
    ):
        def broken(m=mutant):
            probs, rep = [], {}
            globals()["goa_binding_partners"] = lambda rows, _m=m: list(_m)
            try:
                check_c_partners(probs, False, rep)
            finally:
                globals()["goa_binding_partners"] = _ORIGINAL_PARTNERS
            hit = [p for p in probs if p.startswith("C: partner sets differ")]
            if not hit:
                raise AssertionError(f"membership guard did not fire; problems={probs}")
            raise CheckError(hit[0])
        _expect(broken, "partner sets differ", f"membership guard catches {label}")

    # ... and prove the membership check does work a cardinality check cannot: the
    # substitution above is invisible to `len(a) == len(b)`.
    assert len(swapped) == len(real), "sanity"
    print("  ok   the substitution mutation is invisible to a cardinality check "
          "(14 == 14), so the membership assertion is load-bearing")

    # 5. Self-inclusion guard.
    def self_included():
        probs, rep = [], {}
        globals()["goa_binding_partners"] = lambda rows: [SUBJECT]
        try:
            check_c_partners(probs, False, rep)
        finally:
            globals()["goa_binding_partners"] = _ORIGINAL_PARTNERS
        hit = [p for p in probs if "own partner set" in p]
        if not hit:
            raise AssertionError(f"self-inclusion guard did not fire; problems={probs}")
        raise CheckError(hit[0])
    _expect(self_included, "own partner set", "self-inclusion guard fires")

    # 6. Truncation guard: numberOfHits vs len(results), never vs a page constant.
    def truncated():
        d = {"numberOfHits": 250, "results": [{}] * 100}
        saved_get = globals()["_get_json"]
        globals()["_get_json"] = lambda url, key, refresh, project=None, compact=False: d
        try:
            quickgo_all(False, max_pages=1, geneProductId="UniProtKB:TEST")
        finally:
            globals()["_get_json"] = saved_get
    _expect(truncated, "TRUNCATED QuickGO", "QuickGO truncation guard fires on a clamped page")

    def intact_truncated():
        d = {"totalElements": 99, "content": [{}] * 10}
        saved_get = globals()["_get_json"]
        globals()["_get_json"] = lambda url, key, refresh, project=None, compact=False: d
        try:
            intact_records("TEST")
        finally:
            globals()["_get_json"] = saved_get
    _expect(intact_truncated, "TRUNCATED IntAct", "IntAct truncation guard fires")

    # ... and against the defect that ACTUALLY shipped, which is a stronger claim
    # than a synthetic fixture. The first version of this script fetched IntAct in
    # one request with pageSize=1000; AQP6 (Q13520) has 1032 interaction records, so
    # 32 were silently dropped. Reproducing that call must still raise.
    _expect(lambda: intact_records("Q13520", page_size=1000, max_pages=0, ids_only=True),
            "TRUNCATED IntAct result for Q13520",
            "the guard fires on the real single-page AQP6 fetch that shipped broken")

    # 7. Positive-control guards. If a control silently returns zero, the guard
    #    must say so instead of letting the subject's zero read as a finding.
    def dead_iba_control():
        probs, rep = [], {}
        saved_all = globals()["quickgo_all"]
        def fake_all(refresh=False, max_pages=20, **params):
            if params.get("geneProductId") == f"UniProtKB:{SUBJECT}":
                return saved_all(refresh, max_pages, **params)
            return []          # every control comes back empty
        globals()["quickgo_all"] = fake_all
        try:
            check_f_coverage(probs, False, rep)
        finally:
            globals()["quickgo_all"] = saved_all
        hit = [p for p in probs if "F-control" in p and "IBA positive control" in p]
        if not hit:
            raise AssertionError(f"IBA control guard did not fire; problems={probs}")
        assert "subject_iba" not in rep, (
            "the IBA control failed but the subject's IBA count was still reported")
        raise CheckError(hit[0])
    _expect(dead_iba_control, "IBA positive control", "dead IBA control is detected")

    def dead_reference_control():
        probs, rep = [], {}
        saved_hits = globals()["quickgo_hits"]
        globals()["quickgo_hits"] = lambda refresh=False, **p: 0
        try:
            check_f_coverage(probs, False, rep)
        finally:
            globals()["quickgo_hits"] = saved_hits
        hit = [p for p in probs if "reference positive control" in p]
        if not hit:
            raise AssertionError(f"reference control guard did not fire; problems={probs}")
        raise CheckError(hit[0])
    _expect(dead_reference_control, "reference positive control",
            "dead reference control is detected")

    # 8. Check G, both directions. A precedent must be queried, and a false precedent must
    #    be reported as false rather than quietly omitted.
    def dead_precedent():
        probs, rep = [], {}
        saved = globals()["quickgo_all"]
        def fake(refresh=False, max_pages=20, **params):
            if params.get("geneProductId") == f"UniProtKB:{SUBJECT}":
                return saved(refresh, max_pages, **params)
            return []
        globals()["quickgo_all"] = fake
        try:
            check_g_precedents(probs, False, rep)
        finally:
            globals()["quickgo_all"] = saved
        hit = [p for p in probs if "returned ZERO annotations" in p]
        if not hit:
            raise AssertionError(f"empty-precedent guard did not fire; problems={probs}")
        raise CheckError(hit[0])
    _expect(dead_precedent, "returned ZERO annotations",
            "a precedent whose query comes back empty is reported, not assumed")

    def false_precedent():
        probs, rep = [], {}
        saved = dict(PRECEDENTS)
        try:
            # Ask dermcidin for a term it does not hold. The guard must say so.
            PRECEDENTS["P81605"] = ("DCD (dermcidin)", "GO:0004672")
            check_g_precedents(probs, False, rep)
        finally:
            PRECEDENTS.clear(); PRECEDENTS.update(saved)
        hit = [p for p in probs if "does NOT hold" in p]
        if not hit:
            raise AssertionError(f"false-precedent guard did not fire; problems={probs}")
        raise CheckError(hit[0])
    _expect(false_precedent, "does NOT hold",
            "a precedent the source does not actually hold is reported as false")

    # ... and the happy direction: the real precedents must verify.
    probs, rep = [], {}
    check_g_precedents(probs, False, rep)
    assert not probs, f"the real precedents do not verify: {probs}"
    assert rep["subject_defense_terms"] == [], (
        f"the subject already holds defence terms {rep['subject_defense_terms']}, "
        f"so the NEW proposals would be redundant")
    for acc, v in rep["precedents"].items():
        assert v["expected_term_rows"], acc
    print("  ok   both real precedents verify and the subject holds no defence/killing term")

    # 9. Check H, one break-test per direction it advertises, plus the defect that shipped.
    import copy as _copy

    def _with_patched_uniprot(mutator):
        """Run check_h_sgt_pair against a mutated copy of the cached records."""
        saved = globals()["fetch_uniprot"]
        cache = {acc: _copy.deepcopy(saved(acc)) for acc in SGT_PAIR}
        mutator(cache)
        globals()["fetch_uniprot"] = lambda acc, refresh=False: cache.get(acc, saved(acc, refresh))
        try:
            probs, rep = [], {}
            check_h_sgt_pair(probs, False, rep)
            return probs, rep
        finally:
            globals()["fetch_uniprot"] = saved

    # 9a. THE DEFECT THAT SHIPPED: the narrowed projection dropped FUNCTION entirely, so the
    #     cache could not support the claim the same commit was making. Reproduce it exactly.
    def strip_function(cache):
        for acc, e in cache.items():
            before = len([c for c in e.get("comments", []) if c["commentType"] == "FUNCTION"])
            assert before, f"fixture invalid: {acc} had no FUNCTION comment to strip"
            e["comments"] = [c for c in e.get("comments", []) if c["commentType"] != "FUNCTION"]
    def shipped_defect():
        probs, _ = _with_patched_uniprot(strip_function)
        hit = [x for x in probs if "no FUNCTION comment cached" in x]
        if not hit:
            raise AssertionError(f"the dropped-FUNCTION guard did not fire; problems={probs}")
        raise CheckError(hit[0])
    _expect(shipped_defect, "no FUNCTION comment cached",
            "a cache projection that drops FUNCTION is caught (the defect that shipped)")

    # 9b. The asymmetry itself: if SGTB's FUNCTION acquired a hydrophobic-client claim, the
    #     "SGTA only" statement would be false and must be reported as false.
    def give_sgtb_the_role(cache):
        e = cache["Q96EQ0"]
        fn = [c for c in e["comments"] if c["commentType"] == "FUNCTION"]
        assert fn, "fixture invalid: SGTB has no FUNCTION comment"
        fn[0]["texts"][0]["value"] += " Also binds hydrophobic transmembrane segments."
    def false_asymmetry():
        probs, _ = _with_patched_uniprot(give_sgtb_the_role)
        hit = [x for x in probs if "curated for SGTA ONLY is false" in x]
        if not hit:
            raise AssertionError(f"the asymmetry guard did not fire; problems={probs}")
        raise CheckError(hit[0])
    _expect(false_asymmetry, "curated for SGTA ONLY is false",
            "SGTB acquiring the hydrophobic-client role is reported as falsifying the claim")

    # 9c. The mirror: SGTA losing it must also be caught, not just SGTB gaining it.
    def take_role_from_sgta(cache):
        e = cache["O43765"]
        fn = [c for c in e["comments"] if c["commentType"] == "FUNCTION"]
        assert fn, "fixture invalid"
        for c in fn:
            for txt in c["texts"]:
                new_v = txt["value"].replace("hydrophobic", "polar").replace("transmembrane", "soluble")
                assert new_v != txt["value"] or "hydrophobic" not in txt["value"].lower(), \
                    "fixture invalid: nothing to replace"
                txt["value"] = new_v
    def sgta_loses_role():
        probs, _ = _with_patched_uniprot(take_role_from_sgta)
        hit = [x for x in probs if "curated FOR SGTA is unsupported" in x]
        if not hit:
            raise AssertionError(f"the SGTA-side guard did not fire; problems={probs}")
        raise CheckError(hit[0])
    _expect(sgta_loses_role, "curated FOR SGTA is unsupported",
            "SGTA losing the hydrophobic-client cues is caught (the mirror direction)")

    # 9d. The family-corroboration half.
    def drop_family(cache):
        e = cache["Q96EQ0"]
        sims = [c for c in e["comments"] if c["commentType"] == "SIMILARITY"]
        assert sims, "fixture invalid: SGTB has no SIMILARITY comment"
        for c in sims:
            for txt in c["texts"]:
                txt["value"] = "Belongs to some other family"
    def family_broken():
        probs, _ = _with_patched_uniprot(drop_family)
        hit = [x for x in probs if "same-family paralogue is not supported" in x]
        if not hit:
            raise AssertionError(f"the family guard did not fire; problems={probs}")
        raise CheckError(hit[0])
    _expect(family_broken, "same-family paralogue is not supported",
            "losing the SGT-family similarity statement is caught")

    # 9e. Happy direction, run against the real cache.
    probs, rep = [], {}
    check_h_sgt_pair(probs, False, rep)
    assert not probs, f"the real SGT records do not support the asymmetry: {probs}"
    assert rep["sgt_pair"]["O43765"]["hydrophobic_client_cues"] == ["hydrophobic", "transmembrane"], rep
    assert rep["sgt_pair"]["Q96EQ0"]["hydrophobic_client_cues"] == [], rep
    print("  ok   the real cache supports the SGTA-only asymmetry and the SGT-family pairing")

    print("\nAll break-tests fired for the right reason.")
    return 0


_ORIGINAL_PARTNERS = goa_binding_partners


# --------------------------------------------------------------------- output


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--refresh", action="store_true", help="re-fetch from the web")
    ap.add_argument("--self-test", action="store_true", help="break-test every guard")
    ap.add_argument("--json", type=Path, default=HERE / "results.json")
    args = ap.parse_args()

    if args.self_test:
        return self_test()

    problems, report = run(args.refresh)
    args.json.write_text(json.dumps(report, indent=1, sort_keys=True) + "\n")
    print(json.dumps(report, indent=1, sort_keys=True))
    print()
    if problems:
        print(f"{len(problems)} PROBLEM(S):")
        for p in problems:
            print("  - " + p)
        return 1
    print("0 problems.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
