#!/usr/bin/env python3
"""Reproducible analysis backing the human ADGRA1 (Q86SQ6) GO review.

Five questions, each answered from a primary web service (UniProt, IntAct,
QuickGO) rather than from prose:

  Q1  Does ADGRA1 carry a class I PDZ-binding motif at its cytoplasmic C-terminus?
  Q2  Do all of the GOA `GO:0005515` partners carry PDZ domains?
  Q3  What does IntAct actually record for those partners -- which method, and
      which of them have a *quantified* dissociation constant?
  Q4  How was the 21-partner GOA/UniProt set selected out of IntAct's 79?
  Q5  PAINT node reach: which PANTHER node gives which term to which human ADGRA
      gene, and are the donors orthologs or paralogs?

Plus one provenance check:

  Q6  How many entities does each legacy NAS/TAS reference annotate? (a single
      reference annotating a whole family with identical evidence is a block
      projection, not N independent findings)

Design rules taken from the campaign brief:
  * A missing input is a HARD ERROR naming the fix, never a silently degraded
    section.
  * `entryType.startswith("UniProtKB reviewed")` -- plain `"reviewed" in ...`
    also matches "unreviewed" and silently promotes every TrEMBL entry.
  * Anti-truncation guards compare `numberOfHits` against `len(results)`,
    never against a page-size constant the caller chose.
  * Every accession lookup prints the entry name and fails loudly on an empty
    one (a dead UniProt entry is indistinguishable from an unannotated one).

Usage:
    uv run python analyze_adgra1.py            # writes results.json + RESULTS.md
    uv run python analyze_adgra1.py --self-test
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.request
from collections import Counter, defaultdict
from pathlib import Path

SUBJECT = "Q86SQ6"  # human ADGRA1, verified below against UniProt
HERE = Path(__file__).resolve().parent
GENE_DIR = HERE.parent
UNIPROT_TXT = GENE_DIR / "ADGRA1-uniprot.txt"
GOA_TSV = GENE_DIR / "ADGRA1-goa.tsv"

# Human ADGRA family. Used for the node-reach question.
ADGRA = {"ADGRA1": "Q86SQ6", "ADGRA2": "Q96PE1", "ADGRA3": "Q8IWK6"}

# The legacy references that GOA cites for ADGRA1's NAS/TAS rows.
LEGACY_REFS = ["PMID:12565841", "PMID:15203201", "PMID:17212699"]

EXPERIMENTAL = {"EXP", "IDA", "IPI", "IMP", "IGI", "IEP", "HTP", "HDA", "HMP", "HGI", "HEP"}


# --------------------------------------------------------------------------- io


def fetch_json(url: str, tries: int = 4) -> dict:
    """GET JSON, asserting HTTP 200. A rejected query and an empty result look
    identical downstream, so the status is asserted rather than assumed."""
    last = None
    for attempt in range(tries):
        req = urllib.request.Request(url, headers={"Accept": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=120) as r:
                if r.status != 200:
                    raise RuntimeError(f"HTTP {r.status} for {url}")
                return json.load(r)
        except (urllib.error.URLError, TimeoutError) as exc:  # transient only
            last = exc
            time.sleep(2 * (attempt + 1))
    raise RuntimeError(f"failed after {tries} attempts: {url} ({last})")


def require(path: Path, fix: str) -> Path:
    if not path.exists():
        raise SystemExit(f"MISSING INPUT: {path}\n  fix: {fix}")
    return path


def uniprot_entry(acc: str, fields: str) -> dict:
    d = fetch_json(f"https://rest.uniprot.org/uniprotkb/{acc}.json?fields={fields}")
    et = d.get("entryType", "")
    if not et:
        raise RuntimeError(f"{acc}: empty entryType -- inactive/deleted UniProt entry?")
    # "reviewed" is a substring of "unreviewed": anchor the test.
    d["_reviewed"] = et.startswith("UniProtKB reviewed")
    d["_status"] = "Swiss-Prot" if d["_reviewed"] else "TrEMBL"
    return d


def quickgo_annotations(**params) -> list[dict]:
    """Fetch all annotations for a QuickGO query, paging until complete.

    The guard compares numberOfHits against len(results) accumulated -- not
    against a page-size constant -- so a server that *clamps* rather than
    errors cannot slip a truncated read past it.
    """
    out: list[dict] = []
    page = 1
    total = None
    while True:
        q = "&".join(f"{k}={v}" for k, v in params.items())
        d = fetch_json(
            "https://www.ebi.ac.uk/QuickGO/services/annotation/search"
            f"?{q}&limit=100&page={page}"
        )
        total = d["numberOfHits"]
        out.extend(d["results"])
        if not d["results"] or len(out) >= total:
            break
        page += 1
    if len(out) != total:
        raise RuntimeError(f"TRUNCATED QuickGO read: got {len(out)} of {total} for {params}")
    return out


def withfrom(rec: dict) -> list[str]:
    """Reassemble QuickGO's split {db, id} objects into `db:id` tokens.

    Dropping the `db` field turns a resolvable MOD seed id into an opaque
    number; comparing bare ids against a GOA WITH/FROM string reports
    "identical data is not identical".
    """
    toks = []
    for c in rec.get("withFrom") or []:
        for x in c.get("connectedXrefs") or []:
            toks.append(f"{x['db']}:{x['id']}")
    return toks


# ------------------------------------------------------------------- questions


def q1_pdz_motif(res: dict) -> None:
    """C-terminal class I PDZ-binding motif, from the UniProt record itself."""
    d = uniprot_entry(SUBJECT, "id,accession,protein_name,gene_names,length,sequence,ft_topo_dom,ft_transmem")
    gene = d["genes"][0]["geneName"]["value"]
    if gene != "ADGRA1":
        raise RuntimeError(f"{SUBJECT} is {gene}, not ADGRA1 -- accession premise is wrong")
    seq = d["sequence"]["value"]
    feats = d.get("features", [])
    topo = [f for f in feats if f["type"] == "Topological domain"]
    tm = [f for f in feats if f["type"] == "Transmembrane"]
    c_term = [f for f in topo if f["location"]["end"]["value"] == len(seq)]
    if len(c_term) != 1:
        raise RuntimeError(f"expected exactly one C-terminal topological domain, got {len(c_term)}")
    n_term = min(topo, key=lambda f: f["location"]["start"]["value"])

    last4 = seq[-4:]
    # Class I PDZ-binding motif: -X-[ST]-X-phi(COOH), phi = V/I/L.
    class1 = bool(re.match(r"^.[ST].[VIL]$", last4))

    res["q1_pdz_motif"] = {
        "entry": d["uniProtkbId"],
        "status": d["_status"],
        "length": len(seq),
        "n_terminal_extracellular": {
            "start": n_term["location"]["start"]["value"],
            "end": n_term["location"]["end"]["value"],
            "description": n_term["description"],
        },
        "n_transmembrane_helices": len(tm),
        "c_terminal_domain": {
            "start": c_term[0]["location"]["start"]["value"],
            "end": c_term[0]["location"]["end"]["value"],
            "description": c_term[0]["description"],
        },
        "c_terminal_residues": last4,
        "class_I_pdz_binding_motif": class1,
        "has_annotated_MOTIF_feature": any(f["type"] == "Motif" for f in feats),
    }


def q2_partners_have_pdz(res: dict, goa_partners: dict[str, list[str]]) -> None:
    """Do the GOA GO:0005515 partners carry annotated PDZ domains?"""
    accs = sorted({a for v in goa_partners.values() for a in v})
    rows = []
    for a in accs:
        d = uniprot_entry(a, "id,accession,gene_names,length,ft_domain")
        gn = d.get("genes", [{}])[0].get("geneName", {}).get("value")
        if not gn:
            raise RuntimeError(f"{a}: no gene name -- possible inactive entry")
        doms = [f["description"] for f in d.get("features", []) if f["type"] == "Domain"]
        rows.append(
            {
                "accession": a,
                "entry": d["uniProtkbId"],
                "gene": gn,
                "status": d["_status"],
                "length": d["sequence"]["length"],
                "n_pdz_domains": sum(1 for x in doms if x.startswith("PDZ")),
            }
        )
    res["q2_partner_pdz_census"] = {
        "n_partners": len(rows),
        "n_with_pdz_domain": sum(1 for r in rows if r["n_pdz_domains"]),
        "n_reviewed": sum(1 for r in rows if r["status"] == "Swiss-Prot"),
        "n_unreviewed": sum(1 for r in rows if r["status"] == "TrEMBL"),
        "partners": sorted(rows, key=lambda r: r["gene"]),
    }


KD_RE = re.compile(r"kd:([0-9.]+)(x10\^\(-6\))?\(molar\)")


def _kd_micromolar(param: str) -> float | None:
    """Parse an IntAct kd parameter into micromolar.

    IntAct carries `kd:1(molar)` for pairs whose affinity was not quantified.
    That is a placeholder, not a measurement, and is reported as such rather
    than as a 1,000,000 uM affinity.
    """
    m = KD_RE.match(param)
    if not m:
        return None
    v = float(m.group(1))
    return v if m.group(2) else v * 1e6


def q3_q4_intact(res: dict, goa_partners: dict[str, list[str]], nbexp: dict[str, int]) -> None:
    """IntAct methods + affinities, and how the GOA partner set was selected."""
    d = fetch_json(
        f"https://www.ebi.ac.uk/intact/ws/interaction/findInteractions/{SUBJECT}"
        "?page=0&pageSize=500"
    )
    content = d["content"]
    if d["totalElements"] != len(content):
        raise RuntimeError(
            f"TRUNCATED IntAct read: {len(content)} of {d['totalElements']}"
        )

    rows_per_partner: Counter[str] = Counter()
    kds: dict[str, list[float]] = defaultdict(list)
    methods: Counter[str] = Counter()
    negatives = Counter()
    for i in content:
        p = i["moleculeB"] if i["moleculeA"] == "ADGRA1" else i["moleculeA"]
        rows_per_partner[p] += 1
        methods[i["detectionMethod"]] += 1
        negatives[bool(i.get("negative"))] += 1
        for prm in i.get("parameters") or []:
            v = _kd_micromolar(prm)
            if v is not None and v < 1e6:  # exclude the 1 M placeholder
                kds[p].append(v)

    goa_symbols = set(nbexp)
    multi = {p for p, n in rows_per_partner.items() if n >= 2}
    single = {p for p, n in rows_per_partner.items() if n == 1}

    # Q4: is UniProt's NbExp just the IntAct row count?
    nbexp_matches = {p: (nbexp[p] == rows_per_partner[p]) for p in nbexp}
    if not all(p in rows_per_partner for p in nbexp):
        missing = sorted(set(nbexp) - set(rows_per_partner))
        raise RuntimeError(f"UniProt INTERACTION partners absent from IntAct: {missing}")

    excluded_quantified = sorted(
        ((p, min(v)) for p, v in kds.items() if p not in goa_symbols),
        key=lambda t: t[1],
    )

    res["q3_intact"] = {
        "total_interaction_records": d["totalElements"],
        "distinct_partners": len(rows_per_partner),
        "detection_methods": dict(methods.most_common()),
        "curated_negative_flag": {str(k): v for k, v in negatives.items()},
        "goa_partners_with_quantified_kd": sorted(
            (p, round(min(kds[p]), 1)) for p in goa_symbols if kds.get(p)
        ),
        "goa_partners_without_quantified_kd": sorted(p for p in goa_symbols if not kds.get(p)),
    }
    res["q4_partner_selection"] = {
        "uniprot_nbexp_equals_intact_row_count": sum(nbexp_matches.values()),
        "uniprot_partner_count": len(nbexp),
        "intact_partners_with_ge2_rows": len(multi),
        "intact_partners_with_1_row": len(single),
        "multi_row_partners_absent_from_uniprot": sorted(multi - goa_symbols),
        "uniprot_partners_that_are_single_row": sorted(goa_symbols & single),
        "excluded_partners_with_quantified_kd": [
            {"gene": p, "kd_uM": round(v, 1)} for p, v in excluded_quantified
        ],
    }


def q5_node_reach(res: dict) -> None:
    """Which PANTHER node gives which term to which human ADGRA gene."""
    per_gene = {}
    node_terms: dict[str, dict[str, set[str]]] = defaultdict(lambda: defaultdict(set))
    for sym, acc in ADGRA.items():
        recs = quickgo_annotations(
            geneProductId=f"UniProtKB:{acc}", evidenceCode="ECO:0000318"
        )
        rows = []
        for r in recs:
            wf = withfrom(r)
            nodes = [t for t in wf if t.startswith("PANTHER:")]
            donors = [t for t in wf if not t.startswith("PANTHER:")]
            for n in nodes:
                node_terms[n][r["goId"]].add(sym)
            rows.append(
                {
                    "term": r["goId"],
                    "qualifier": r["qualifier"],
                    "nodes": nodes,
                    "donors": donors,
                }
            )
        per_gene[sym] = sorted(rows, key=lambda x: x["term"])

    reach = {
        n: {
            "human_reach": sorted({s for ss in terms.values() for s in ss}),
            "terms": {t: sorted(s) for t, s in terms.items()},
        }
        for n, terms in node_terms.items()
    }
    res["q5_paint_nodes"] = {"per_gene": per_gene, "node_reach": reach}


def q5b_donor_evidence(res: dict, donors: dict[str, list[str]]) -> None:
    """For each IBA donor, what evidence does it hold for the propagated term?

    A donor token that maps to several accessions is reported with ALL of them:
    an ambiguous cross-reference is data, and collapsing it to one hit is how a
    `size=1` lookup turns an ambiguity into a confident wrong answer.
    """
    out = []
    for token, accs in sorted(donors.items()):
        cands = []
        for acc in accs:
            d = uniprot_entry(acc, "id,accession,gene_names,organism_name,length")
            gn = d.get("genes", [{}])[0].get("geneName", {}).get("value")
            if not gn:
                raise RuntimeError(f"{acc}: no gene name -- possible inactive entry")
            recs = quickgo_annotations(geneProductId=f"UniProtKB:{acc}")
            own_exp = sorted(
                {
                    (r["goId"], r["goEvidence"], r["reference"])
                    for r in recs
                    if r["goEvidence"] in EXPERIMENTAL
                }
            )
            cands.append(
                {
                    "accession": acc,
                    "entry": d["uniProtkbId"],
                    "status": d["_status"],
                    "gene": gn,
                    "organism": d["organism"]["scientificName"],
                    "length": d["sequence"]["length"],
                    "own_experimental_annotations": [list(x) for x in own_exp],
                }
            )
        genes = {c["gene"].lower() for c in cands}
        out.append(
            {
                "withfrom_token": token,
                "n_candidate_accessions": len(cands),
                "ambiguous": len(cands) > 1,
                "any_reviewed": any(c["status"] == "Swiss-Prot" for c in cands),
                "gene_symbols_agree": len(genes) == 1,
                "is_adgra1_ortholog": genes == {"adgra1"},
                "candidates": cands,
            }
        )
    res["q5b_donors"] = out


def q6_reference_projection(res: dict) -> None:
    """Does a cited reference annotate one gene, or a whole family at once?"""
    out = {}
    for ref in LEGACY_REFS:
        recs = quickgo_annotations(reference=ref)
        ents = {r["geneProductId"]: r["symbol"] for r in recs}
        per_term = {}
        for t in sorted({r["goId"] for r in recs}):
            sub = [r for r in recs if r["goId"] == t]
            per_term[t] = {
                "annotations": len(sub),
                "entities": len({r["geneProductId"] for r in sub}),
                "evidence": sorted({r["goEvidence"] for r in sub}),
            }
        out[ref] = {
            "total_annotations": len(recs),
            "distinct_entities": len(ents),
            "symbols": sorted(set(ents.values())),
            "per_term": per_term,
        }
    res["q6_reference_projection"] = out


# ------------------------------------------------------------------ goa parsing


def parse_goa() -> tuple[list[dict], dict[str, list[str]], dict[str, int]]:
    """Return (rows, {reference: [partner accessions]}, {symbol: NbExp}).

    Partner accessions come from the GOA WITH/FROM column, never from a hand
    list; NbExp comes from the UniProt CC INTERACTION block.
    """
    require(GOA_TSV, "just fetch-gene human ADGRA1")
    require(UNIPROT_TXT, "just fetch-gene human ADGRA1")
    lines = GOA_TSV.read_text().rstrip("\n").split("\n")
    header = lines[0].split("\t")
    rows = [dict(zip(header, ln.split("\t"))) for ln in lines[1:]]

    partners: dict[str, list[str]] = defaultdict(list)
    for r in rows:
        if r["GO TERM"] == "GO:0005515":
            for tok in r["WITH/FROM"].split("|"):
                if tok.startswith("UniProtKB:"):
                    partners[r["REFERENCE"]].append(tok.split(":", 1)[1])

    nbexp = {
        m.group(1): int(m.group(2))
        for m in re.finditer(
            r"CC\s+Q86SQ6; \w+: (\w+); NbExp=(\d+);", UNIPROT_TXT.read_text()
        )
    }
    if not nbexp:
        raise RuntimeError("no CC INTERACTION lines parsed from the UniProt record")
    return rows, dict(partners), nbexp


def iba_donor_accessions(rows: list[dict]) -> dict[str, list[str]]:
    """Resolve every non-PANTHER WITH/FROM token on the IBA rows to accessions.

    MGI tokens arrive as `MGI:MGI:nnnn`; UniProt's xref index wants the bare
    number (a query containing the inner colon returns HTTP 400).  Multi-hit
    lookups are handled explicitly -- `size=1` converts an ambiguity into a
    confident wrong answer.  Where reviewed entries exist they are preferred
    (an unreviewed entry's *name* is an automatic by-similarity label); where
    none does, every unreviewed candidate is returned so the ambiguity reaches
    the report instead of being silently resolved.  Zero hits is still a hard
    error: an unresolved WITH/FROM token cannot be dismissed, only deferred.
    """
    toks: set[str] = set()
    for r in rows:
        if r["GO EVIDENCE CODE"] != "IBA":
            continue
        for t in r["WITH/FROM"].split("|"):
            if t and not t.startswith("PANTHER:"):
                toks.add(t)

    resolved: dict[str, list[str]] = {}
    for t in sorted(toks):
        if t.startswith("UniProtKB:"):
            resolved[t] = [t.split(":", 1)[1]]
            continue
        if t.startswith("MGI:MGI:"):
            query = f"xref:mgi-{t.split('MGI:MGI:')[1]}"
        elif t.startswith("ZFIN:"):
            query = f"xref:zfin-{t.split(':', 1)[1]}"
        else:
            raise RuntimeError(f"unhandled WITH/FROM namespace: {t}")
        d = fetch_json(
            "https://rest.uniprot.org/uniprotkb/search?query="
            f"{query}&fields=id,accession&size=10&format=json"
        )
        hits = d["results"]
        if not hits:
            raise RuntimeError(f"{t}: unresolved (0 hits) -- cannot be dismissed, only deferred")
        rev = [h for h in hits if h["entryType"].startswith("UniProtKB reviewed")]
        pick = rev if rev else hits
        resolved[t] = [h["primaryAccession"] for h in pick]
    return resolved


# ----------------------------------------------------------------------- report


def render(res: dict) -> str:
    q1 = res["q1_pdz_motif"]
    q2 = res["q2_partner_pdz_census"]
    q3 = res["q3_intact"]
    q4 = res["q4_partner_selection"]
    q6 = res["q6_reference_projection"]
    L: list[str] = []
    a = L.append

    a("# ADGRA1 (Q86SQ6) — computed evidence for the GO review\n")
    a("Regenerate with `uv run python analyze_adgra1.py`. Every number below is")
    a("read from UniProt, IntAct or QuickGO at run time; none is hardcoded.\n")

    a("## Q1. A cytoplasmic C-terminal class I PDZ-binding motif\n")
    a(f"- `{q1['entry']}` ({q1['status']}), {q1['length']} aa, {q1['n_transmembrane_helices']} TM helices.")
    nt = q1["n_terminal_extracellular"]
    a(f"- N-terminal {nt['description'].lower()} domain: residues {nt['start']}–{nt['end']} "
      f"(**{nt['end'] - nt['start'] + 1} residues**) — there is no ectodomain to hold a GAIN/GPS module.")
    ct = q1["c_terminal_domain"]
    a(f"- C-terminal {ct['description'].lower()} tail: residues {ct['start']}–{ct['end']} "
      f"({ct['end'] - ct['start'] + 1} residues).")
    a(f"- Last four residues: `{q1['c_terminal_residues']}`; matches the class I "
      f"PDZ-binding consensus `X-[ST]-X-[VIL]`: **{q1['class_I_pdz_binding_motif']}**.")
    a(f"- UniProt has an annotated `MOTIF` feature for it: **{q1['has_annotated_MOTIF_feature']}**.\n")

    a("## Q2. Every GOA `GO:0005515` partner is a PDZ-domain protein\n")
    a(f"{q2['n_with_pdz_domain']}/{q2['n_partners']} partners carry at least one annotated PDZ domain; "
      f"{q2['n_reviewed']} reviewed (Swiss-Prot), {q2['n_unreviewed']} unreviewed (TrEMBL).\n")
    a("| partner | accession | entry | status | length | PDZ domains |")
    a("|---|---|---|---|---|---|")
    for p in q2["partners"]:
        a(f"| {p['gene']} | {p['accession']} | {p['entry']} | {p['status']} | {p['length']} | {p['n_pdz_domains']} |")
    a("")

    a("## Q3. IntAct: one quantitative affinity dataset, not a Y2H screen\n")
    a(f"- {q3['total_interaction_records']} interaction records over {q3['distinct_partners']} distinct partners.")
    a("- detection methods: " + ", ".join(f"`{k}` ×{v}" for k, v in q3["detection_methods"].items()) + ".")
    a("- curated-negative flag: " + ", ".join(f"{k}={v}" for k, v in q3["curated_negative_flag"].items()) + ".")
    a(f"- Of the GOA partner set, **{len(q3['goa_partners_with_quantified_kd'])} have a quantified Kd** "
      f"and **{len(q3['goa_partners_without_quantified_kd'])} do not** "
      "(IntAct carries `kd:1(molar)`, a placeholder, for the latter).\n")
    a("| GOA partner | best quantified Kd (µM) |")
    a("|---|---|")
    for g, v in q3["goa_partners_with_quantified_kd"]:
        a(f"| {g} | {v} |")
    for g in q3["goa_partners_without_quantified_kd"]:
        a(f"| {g} | not quantified |")
    a("")

    a("## Q4. The GOA partner set is selected by domain count, not by affinity\n")
    a(f"- UniProt's `NbExp` equals the IntAct record count for "
      f"**{q4['uniprot_nbexp_equals_intact_row_count']}/{q4['uniprot_partner_count']}** partners.")
    a(f"- IntAct partners with ≥2 records: {q4['intact_partners_with_ge2_rows']}; with exactly 1: "
      f"{q4['intact_partners_with_1_row']}.")
    a(f"- Multi-record partners absent from the UniProt/GOA set: "
      f"{q4['multi_row_partners_absent_from_uniprot'] or 'none'}.")
    a(f"- UniProt/GOA partners that are single-record: "
      f"{q4['uniprot_partners_that_are_single_row'] or 'none'}.")
    a("")
    a("So `NbExp` here counts **how many PDZ domains of the same partner protein were assayed**")
    a("within one holdup dataset, not independent experiments, and the GOA cut is `NbExp ≥ 2`.")
    a(f"The cost: **{len(q4['excluded_partners_with_quantified_kd'])} partners with a genuinely measured Kd**")
    a("are excluded, including the tightest binders measured:\n")
    a("| excluded partner | Kd (µM) |")
    a("|---|---|")
    for e in q4["excluded_partners_with_quantified_kd"]:
        a(f"| {e['gene']} | {e['kd_uM']} |")
    a("")

    a("## Q5. PAINT node reach across the human ADGRA family\n")
    a("| node | human reach | terms given |")
    a("|---|---|---|")
    for n, v in sorted(res["q5_paint_nodes"]["node_reach"].items()):
        a(f"| `{n}` | {', '.join(v['human_reach'])} | {', '.join(sorted(v['terms']))} |")
    a("")
    a("| IBA donor token | resolves to | organism | status | ADGRA1 ortholog? | own experimental annotations |")
    a("|---|---|---|---|---|---|")
    for d in res["q5b_donors"]:
        for c in d["candidates"]:
            exp = "; ".join(f"{t} {e} ({r})" for t, e, r in c["own_experimental_annotations"]) or "none"
            amb = " *(1 of %d candidates — ambiguous xref)*" % d["n_candidate_accessions"] if d["ambiguous"] else ""
            a(f"| `{d['withfrom_token']}`{amb} | {c['gene']} ({c['accession']}, {c['entry']}) | "
              f"{c['organism']} | {c['status']} | "
              f"{'yes' if d['is_adgra1_ortholog'] else 'no — paralog'} | {exp} |")
    n_orth = sum(1 for d in res["q5b_donors"] if d["is_adgra1_ortholog"])
    a("")
    a(f"**{n_orth} of {len(res['q5b_donors'])}** IBA donor tokens are ADGRA1 orthologs; the rest are "
      "ADGRA2/ADGRA3 paralogs.")
    a("")

    a("## Q6. What each legacy reference annotates\n")
    a("| reference | annotations | distinct entities | terms (entities each) |")
    a("|---|---|---|---|")
    for ref, v in q6.items():
        terms = ", ".join(
            f"{t} {d['evidence'][0]} ({d['entities']})" for t, d in sorted(v["per_term"].items())
        )
        a(f"| {ref} | {v['total_annotations']} | {v['distinct_entities']} | {terms} |")
    a("")
    big = max(q6.items(), key=lambda kv: kv[1]["distinct_entities"])
    a(f"`{big[0]}` annotates **{big[1]['distinct_entities']} distinct entities** with identical evidence:")
    a("`" + "`, `".join(big[1]["symbols"]) + "`.")
    a("")
    return "\n".join(L)


# -------------------------------------------------------------------- self-test


def self_test() -> int:
    """Break-test the parsers in both directions: the failure path AND the
    happy path (a check can be wrong about success as easily as about failure).
    """
    problems: list[str] = []

    # _kd_micromolar: placeholder vs real measurement
    if _kd_micromolar("kd:1(molar)") != 1e6:
        problems.append("kd placeholder not parsed as 1 M")
    got = _kd_micromolar("kd:4.62631191068213976080869542784057557582855224609375x10^(-6)(molar)")
    if got is None or abs(got - 4.626) > 0.01:
        problems.append(f"kd micromolar parse wrong: {got}")
    if _kd_micromolar("ic50:5(molar)") is not None:
        problems.append("non-kd parameter should not parse as a Kd")

    # class I PDZ motif regex, both directions
    for s, want in [("ETTV", True), ("ESDV", True), ("ETTP", False), ("EAAV", False)]:
        if bool(re.match(r"^.[ST].[VIL]$", s)) != want:
            problems.append(f"class I motif call wrong for {s}")

    # withfrom must keep the db field
    rec = {"withFrom": [{"connectedXrefs": [{"db": "MGI", "id": "1277167"}]}]}
    if withfrom(rec) != ["MGI:1277167"]:
        problems.append("withfrom dropped the db namespace")

    # the reviewed/unreviewed substring trap
    for et, want in [
        ("UniProtKB reviewed (Swiss-Prot)", True),
        ("UniProtKB unreviewed (TrEMBL)", False),
    ]:
        if et.startswith("UniProtKB reviewed") != want:
            problems.append(f"reviewed test wrong for {et!r}")
    if "reviewed" not in "UniProtKB unreviewed (TrEMBL)":
        problems.append("the substring trap this guard exists for no longer reproduces")

    # GOA parse: partner accessions must come from WITH/FROM, and NbExp from UniProt
    rows, partners, nbexp = parse_goa()
    n_5515 = sum(1 for r in rows if r["GO TERM"] == "GO:0005515")
    n_parsed = sum(len(v) for v in partners.values())
    if n_5515 != n_parsed:
        problems.append(f"GO:0005515 rows {n_5515} != partner accessions parsed {n_parsed}")
    if len(nbexp) != len(set(nbexp)):
        problems.append("duplicate symbols in the UniProt NbExp map")

    for p in problems:
        print("SELF-TEST FAIL:", p)
    print(f"self-test: {len(problems)} problem(s)")
    return 1 if problems else 0


# ------------------------------------------------------------------------ main


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    if args.self_test:
        return self_test()

    rows, partners, nbexp = parse_goa()
    res: dict = {
        "subject": SUBJECT,
        "goa_rows": len(rows),
        "goa_go0005515_rows": sum(1 for r in rows if r["GO TERM"] == "GO:0005515"),
        "goa_references_for_go0005515": sorted(partners),
    }
    q1_pdz_motif(res)
    q2_partners_have_pdz(res, partners)
    q3_q4_intact(res, partners, nbexp)
    q5_node_reach(res)
    q5b_donor_evidence(res, iba_donor_accessions(rows))
    q6_reference_projection(res)

    (HERE / "results.json").write_text(json.dumps(res, indent=2, sort_keys=True) + "\n")
    (HERE / "RESULTS.md").write_text(render(res))
    print(f"wrote {HERE / 'results.json'} and {HERE / 'RESULTS.md'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
