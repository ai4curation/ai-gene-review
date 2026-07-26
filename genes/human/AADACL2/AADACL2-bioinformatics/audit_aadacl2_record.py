#!/usr/bin/env python3
"""Audit the human AADACL2 (Q6P093) GO record.

Two opposite errors are common when a protein is named after a domain family. One is
to accept an activity because the fold is there; the other is to reject it without
checking whether the catalytic residues survived. This script asks both questions of
AADACL2, plus where its two mutually exclusive localisation annotations come from.

Q1  Is the GDXG serine-hydrolase machinery present in AADACL2? Reciprocal test: align
    AADACL2 to each experimentally characterised relative cited in its own GOA
    WITH/FROM column and read off what AADACL2 carries at that relative's
    UniProt-annotated ACT_SITE positions. Nothing about the triad is hardcoded; the
    positions are fetched from the source records.
Q2  Does 'membrane' transfer across the InterPro signature that produced it? Tabulate
    SIGNAL vs TRANSMEM features and subcellular locations for every reviewed UniProtKB
    entry carrying IPR017157 (the Arylacetamide_deacetylase family signature named in
    the GOA WITH/FROM column).
Q3  Resolve every WITH/FROM identifier in AADACL2-goa.tsv to a species and a protein.
Q4  An independent localisation opinion: Human Protein Atlas protein-class assignment
    (a majority vote over several secretome/membrane predictors) for the five human
    AADAC-family members.
Q5  Signal-peptide geometry: the (-3, -1) residues at each annotated cleavage site and
    the peak Kyte-Doolittle hydropathy of a 19-residue window near the N-terminus,
    measured the same way for every family member.
Q6  Which PANTHER node carries which term for the family? Compare the IBA annotations
    of all five human AADAC-family members via QuickGO.
Q7  AADACL2 is 'PE 1: Evidence at protein level'. Which residues do the observed
    peptides actually cover? If none of them touch the N-terminus, mass spectrometry
    cannot adjudicate the cleaved-signal-peptide versus retained-signal-anchor question.

Run with:
    uv run --no-project --with requests --with biopython python audit_aadacl2_record.py

Inputs: this gene's own genes/human/AADACL2/AADACL2-goa.tsv (required; the script aborts
with the regeneration command if it is missing) plus the UniProt, InterPro, QuickGO and
Human Protein Atlas REST APIs at run time. Nothing is hardcoded and no fetch failure is
silently converted into an absence: requests raise. Machine-readable output goes to
results.json next to this file; RESULTS.md is prose written from that file.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

import requests
from Bio import Align
from Bio.Align import substitution_matrices

HERE = Path(__file__).resolve().parent
GENE_DIR = HERE.parent
GOA_TSV = GENE_DIR / "AADACL2-goa.tsv"
TARGET = "Q6P093"

UNIPROT = "https://rest.uniprot.org/uniprotkb"
QUICKGO = "https://www.ebi.ac.uk/QuickGO/services"
INTERPRO = "https://www.ebi.ac.uk/interpro/api"
PROTEINS_API = "https://www.ebi.ac.uk/proteins/api"
HPA = "https://www.proteinatlas.org/api/search_download.php"

# GOA WITH/FROM prefix -> UniProt cross-reference database name. Identifiers of a kind
# that is not a protein (a PANTHER node, an InterPro signature, an ARBA rule, a
# SubCell keyword) are deliberately absent and are reported as non-protein sources.
XREF_DB = {"MGI": "mgi", "RGD": "rgd", "SGD": "sgd", "AGI_LocusCode": "araport"}

# Kyte-Doolittle hydropathy. A mean over a ~19-residue window is the standard way to
# score a candidate membrane-spanning segment, and unlike a "count the hydrophobic
# letters" rule it does not depend on an arbitrary hydrophobic/polar cut for Tyr, Gly
# and Pro, which differ between the AADAC-family N-termini being compared.
KYTE_DOOLITTLE = {
    "A": 1.8, "R": -4.5, "N": -3.5, "D": -3.5, "C": 2.5, "Q": -3.5, "E": -3.5,
    "G": -0.4, "H": -3.2, "I": 4.5, "L": 3.8, "K": -3.9, "M": 1.9, "F": 2.8,
    "P": -1.6, "S": -0.8, "T": -0.7, "W": -0.9, "Y": -1.3, "V": 4.2,
}
KD_WINDOW = 19

SESSION = requests.Session()
SESSION.headers.update({"Accept": "application/json"})


def get_json(url: str, **params) -> dict:
    r = SESSION.get(url, params=params or None, timeout=90)
    r.raise_for_status()
    return r.json()


def entry(acc: str) -> dict:
    return get_json(f"{UNIPROT}/{acc}.json")


def sequence(rec: dict) -> str:
    return rec["sequence"]["value"]


def features(rec: dict, kind: str) -> list[dict]:
    return [f for f in rec.get("features", []) if f["type"] == kind]


def span(f: dict) -> tuple[int, int]:
    return f["location"]["start"]["value"], f["location"]["end"]["value"]


def locations(rec: dict) -> list[str]:
    out = []
    for c in rec.get("comments", []):
        if c["commentType"] != "SUBCELLULAR LOCATION":
            continue
        for loc in c.get("subcellularLocations", []):
            text = loc.get("location", {}).get("value", "")
            topology = loc.get("topology", {}).get("value")
            out.append(f"{text} ({topology})" if topology else text)
    return out


def gene_symbol(rec: dict) -> str | None:
    for g in rec.get("genes", []):
        name = g.get("geneName", {}).get("value")
        if name:
            return name
    return None


def organism(rec: dict) -> str:
    return rec.get("organism", {}).get("scientificName", "")


def function_text(rec: dict) -> str | None:
    for c in rec.get("comments", []):
        if c["commentType"] == "FUNCTION" and c.get("texts"):
            return c["texts"][0]["value"]
    return None


def make_aligner() -> Align.PairwiseAligner:
    a = Align.PairwiseAligner(mode="global")
    a.substitution_matrix = substitution_matrices.load("BLOSUM62")
    a.open_gap_score = -11
    a.extend_gap_score = -1
    a.target_end_gap_score = 0.0
    a.query_end_gap_score = 0.0
    return a


def source_to_target_map(aligner, target_seq: str, source_seq: str) -> tuple[dict[int, int], int]:
    """Map 1-based source positions to 1-based target positions; also return identities."""
    aln = aligner.align(target_seq, source_seq)[0]
    tblocks, sblocks = aln.aligned
    mapping: dict[int, int] = {}
    identities = 0
    for (t0, t1), (s0, s1) in zip(tblocks, sblocks):
        t0, t1, s0 = int(t0), int(t1), int(s0)
        for k in range(t1 - t0):
            mapping[s0 + k + 1] = t0 + k + 1
            if target_seq[t0 + k] == source_seq[s0 + k]:
                identities += 1
    return mapping, identities


def parse_with_from(path: Path) -> list[dict]:
    """Rows of (term, evidence, reference, [with/from ids]) from a QuickGO GOA TSV."""
    if not path.exists():
        raise SystemExit(
            f"missing required input {path}\n"
            "Regenerate it with:  just fetch-gene human AADACL2"
        )
    lines = path.read_text().rstrip("\n").split("\n")
    header = lines[0].split("\t")
    idx = {name: i for i, name in enumerate(header)}
    for needed in ("GO TERM", "GO NAME", "GO EVIDENCE CODE", "REFERENCE", "WITH/FROM"):
        if needed not in idx:
            raise SystemExit(f"{path} has no {needed!r} column; header was {header}")
    rows = []
    for line in lines[1:]:
        if not line.strip():
            continue
        cells = line.split("\t")
        raw = cells[idx["WITH/FROM"]].strip()
        rows.append(
            {
                "term": cells[idx["GO TERM"]],
                "term_label": cells[idx["GO NAME"]],
                "evidence": cells[idx["GO EVIDENCE CODE"]],
                "reference": cells[idx["REFERENCE"]],
                "with_from": [x for x in raw.split("|") if x],
            }
        )
    return rows


def resolve_source(ident: str) -> dict:
    """Resolve one WITH/FROM identifier. Non-protein sources are labelled, not dropped."""
    out: dict[str, object] = {"id": ident}
    if ident.startswith("UniProtKB:"):
        rec = entry(ident.split(":", 1)[1])
        out.update(
            kind="protein",
            accession=rec["primaryAccession"],
            uniprot_id=rec.get("uniProtkbId"),
            gene=gene_symbol(rec),
            organism=organism(rec),
            reviewed=rec.get("entryType", "").startswith("UniProtKB reviewed"),
            function=function_text(rec),
            transmem=[span(f) for f in features(rec, "Transmembrane")],
            signal=[span(f) for f in features(rec, "Signal")],
            subcellular=locations(rec),
        )
        return out
    prefix = ident.split(":", 1)[0]
    if prefix in XREF_DB:
        local = ident.split(":", 1)[1]
        if local.startswith(prefix + ":"):  # MGI:MGI:1915008
            local = local.split(":", 1)[1]
        hits = get_json(
            f"{UNIPROT}/search",
            query=f"xref:{XREF_DB[prefix]}-{local} AND reviewed:true",
            fields="accession,id,gene_names,organism_name",
            size=5,
        )["results"]
        out.update(kind="model-organism gene", database=prefix, local_id=local)
        if not hits:
            out["resolved"] = False
            return out
        rec = entry(hits[0]["primaryAccession"])
        out.update(
            resolved=True,
            accession=rec["primaryAccession"],
            uniprot_id=rec.get("uniProtkbId"),
            gene=gene_symbol(rec),
            organism=organism(rec),
            function=function_text(rec),
            transmem=[span(f) for f in features(rec, "Transmembrane")],
            signal=[span(f) for f in features(rec, "Signal")],
            subcellular=locations(rec),
        )
        return out
    if prefix == "InterPro":
        acc = ident.split(":", 1)[1]
        meta = get_json(f"{INTERPRO}/entry/interpro/{acc}")["metadata"]
        out.update(kind="InterPro signature", accession=acc, name=meta.get("name", {}).get("name"))
        return out
    out.update(kind="non-protein source", note=f"{prefix} identifier; no protein to resolve")
    return out


def q1_catalytic_machinery(target_rec: dict, protein_sources: list[dict]) -> dict:
    """Do AADACL2's own annotated active sites coincide with those of characterised relatives?"""
    target_seq = sequence(target_rec)
    own_act = [span(f)[0] for f in features(target_rec, "Active site")]
    own_motif = [
        {"span": span(f), "note": f.get("description"), "residues": target_seq[span(f)[0] - 1 : span(f)[1]]}
        for f in features(target_rec, "Motif")
    ]
    gdxg = [
        {"start": m.start() + 1, "residues": m.group()}
        for m in re.finditer(r"G[DE][SA].G", target_seq)
    ]
    aligner = make_aligner()
    per_source = []
    for src in protein_sources:
        rec = entry(src["accession"])
        src_act = [span(f)[0] for f in features(rec, "Active site")]
        src_seq = sequence(rec)
        mapping, identities = source_to_target_map(aligner, target_seq, src_seq)
        mapped = []
        for pos in src_act:
            tpos = mapping.get(pos)
            # Residue identity alone is not enough: at low sequence identity a global
            # alignment can park a source Asp on some unrelated Asp elsewhere in
            # AADACL2. The transfer only corroborates AADACL2's triad if the mapped
            # position IS one of AADACL2's own annotated active sites.
            mapped.append(
                {
                    "source_position": pos,
                    "source_residue": src_seq[pos - 1],
                    "target_position": tpos,
                    "target_residue": target_seq[tpos - 1] if tpos else None,
                    "same_residue": bool(tpos) and target_seq[tpos - 1] == src_seq[pos - 1],
                    "lands_on_annotated_target_site": tpos in own_act,
                }
            )
        per_source.append(
            {
                "accession": src["accession"],
                "gene": src.get("gene"),
                "organism": src.get("organism"),
                "length": len(src_seq),
                "identities_to_AADACL2": identities,
                "percent_identity": round(100 * identities / min(len(src_seq), len(target_seq)), 1),
                "annotated_active_sites": src_act,
                "mapped_active_sites": mapped,
                "corroborates_target_triad": bool(src_act)
                and all(m["same_residue"] and m["lands_on_annotated_target_site"] for m in mapped),
            }
        )
    # Per-residue breakdown. The aggregate "triad complete" count understates the
    # nucleophile evidence: the serine elbow is the most conserved part of the fold and
    # never loses alignment register, while the acid and base sit in the C-terminal half
    # where a global alignment drifts at low identity. Report the three positions
    # separately so the aggregate cannot be mistaken for a statement about the serine.
    by_residue = {}
    with_sites = [s for s in per_source if s["annotated_active_sites"]]
    for rank, position in enumerate(own_act):
        landed, identical = 0, 0
        for s in with_sites:
            hit = next(
                (m for m in s["mapped_active_sites"] if m["target_position"] == position), None
            )
            if hit is None and rank < len(s["mapped_active_sites"]):
                hit = s["mapped_active_sites"][rank] if s["mapped_active_sites"][rank]["target_position"] == position else None
            if hit is None:
                continue
            landed += 1
            if hit["same_residue"]:
                identical += 1
        by_residue[str(position)] = {
            "target_residue": target_seq[position - 1],
            "sources_landing_here": landed,
            "sources_with_identical_residue": identical,
            "n_sources_considered": len(with_sites),
        }

    return {
        "target_length": len(target_seq),
        "target_annotated_active_sites": own_act,
        "target_active_site_residues": [target_seq[p - 1] for p in own_act],
        "target_annotated_motifs": own_motif,
        "gdxg_nucleophile_elbow_matches": gdxg,
        "prosite_gdxg_serine_signature": "PS01174" in json.dumps(target_rec.get("uniProtKBCrossReferences", [])),
        "per_target_active_site": by_residue,
        "n_sources_corroborating_full_triad": sum(
            1 for s in with_sites if s["corroborates_target_triad"]
        ),
        "per_source": per_source,
    }


def q2_family_topology(signature: str) -> dict:
    hits = get_json(
        f"{UNIPROT}/search",
        query=f"xref:interpro-{signature} AND reviewed:true",
        fields="accession,id,gene_names,organism_name",
        size=200,
    )["results"]
    members = []
    for h in hits:
        rec = entry(h["primaryAccession"])
        tm = [span(f) for f in features(rec, "Transmembrane")]
        sp = [span(f) for f in features(rec, "Signal")]
        members.append(
            {
                "accession": rec["primaryAccession"],
                "uniprot_id": rec.get("uniProtkbId"),
                "gene": gene_symbol(rec),
                "organism": organism(rec),
                "transmem": tm,
                "transmem_notes": [f.get("description") for f in features(rec, "Transmembrane")],
                "signal": sp,
                "subcellular": locations(rec),
            }
        )
    members.sort(key=lambda m: (m["gene"] or "", m["organism"]))
    with_tm = [m for m in members if m["transmem"]]
    with_sp = [m for m in members if m["signal"] and not m["transmem"]]
    neither = [m for m in members if not m["signal"] and not m["transmem"]]
    return {
        "signature": signature,
        "n_reviewed_members": len(members),
        "n_with_transmembrane": len(with_tm),
        "n_with_cleaved_signal_only": len(with_sp),
        "n_with_neither": len(neither),
        "cleaved_signal_only_members": [f"{m['gene']} ({m['organism']})" for m in with_sp],
        "neither_members": [f"{m['gene']} ({m['organism']})" for m in neither],
        "members": members,
    }


def q4_hpa_protein_class(symbols: list[str]) -> dict:
    out = {}
    for sym in symbols:
        rows = get_json(
            HPA,
            search=sym,
            format="json",
            columns="g,eg,pc,scl,rnatd,rnatsm",
            compress="no",
        )
        match = [r for r in rows if r.get("Gene", "").upper() == sym.upper()]
        if not match:
            out[sym] = {"found": False}
            continue
        r = match[0]
        out[sym] = {
            "found": True,
            "ensembl": r.get("Ensembl"),
            "protein_class": r.get("Protein class"),
            "subcellular_location": r.get("Subcellular location"),
            "rna_tissue_distribution": r.get("RNA tissue distribution"),
            "rna_tissue_specific_ntpm": r.get("RNA tissue specific nTPM"),
        }
    return out


def peak_hydropathy(seq: str, search_to: int = 45) -> dict:
    """Highest mean Kyte-Doolittle hydropathy over a KD_WINDOW-residue window near the N-terminus."""
    region = seq[:search_to]
    if len(region) < KD_WINDOW:
        raise ValueError(f"sequence shorter than the {KD_WINDOW}-residue hydropathy window")
    best_score, best_start = None, None
    for start in range(len(region) - KD_WINDOW + 1):
        chunk = region[start : start + KD_WINDOW]
        score = sum(KYTE_DOOLITTLE[aa] for aa in chunk) / KD_WINDOW
        if best_score is None or score > best_score:
            best_score, best_start = score, start + 1
    return {
        "peak_kd_window": [best_start, best_start + KD_WINDOW - 1],
        "peak_kd_mean": round(best_score, 2),
    }


def q5_signal_geometry(accessions: list[str]) -> list[dict]:
    out = []
    for acc in accessions:
        rec = entry(acc)
        seq = sequence(rec)
        sp = features(rec, "Signal")
        tm = features(rec, "Transmembrane")
        row = {
            "accession": acc,
            "gene": gene_symbol(rec),
            "organism": organism(rec),
            "n_terminus_40": seq[:40],
            "signal": [span(f) for f in sp],
            "transmem": [span(f) for f in tm],
        }
        row.update(peak_hydropathy(seq))
        if sp:
            end = span(sp[0])[1]
            row["cleavage_after_position"] = end
            row["minus3_minus1"] = seq[end - 3 : end]
            row["plus1_plus3"] = seq[end : end + 3]
            row["minus1_is_small_neutral"] = seq[end - 1] in set("ASCGT")
        out.append(row)
    return out


def q7_observed_peptides(acc: str, signal_end: int | None) -> dict:
    data = get_json(f"{PROTEINS_API}/proteomics/{acc}")
    peptides = []
    for f in data.get("features", []):
        begin, end = int(f["begin"]), int(f["end"])
        peptides.append(
            {
                "begin": begin,
                "end": end,
                "peptide": f.get("peptide"),
                "sources": sorted(
                    {e["source"]["name"] for e in f.get("evidences", []) if e.get("source")}
                ),
            }
        )
    peptides.sort(key=lambda p: p["begin"])
    earliest = min((p["begin"] for p in peptides), default=None)
    return {
        "accession": acc,
        "n_observed_peptides": len(peptides),
        "earliest_observed_residue": earliest,
        "annotated_signal_cleavage_after": signal_end,
        "any_peptide_spans_the_annotated_cleavage_site": bool(
            signal_end is not None
            and any(p["begin"] <= signal_end < p["end"] for p in peptides)
        ),
        "any_peptide_starts_at_mature_n_terminus": bool(
            signal_end is not None and any(p["begin"] == signal_end + 1 for p in peptides)
        ),
        "peptides": peptides,
    }


def q6_family_iba_nodes(accessions: list[str]) -> list[dict]:
    ids = ",".join(f"UniProtKB:{a}" for a in accessions)
    data = get_json(
        f"{QUICKGO}/annotation/search",
        geneProductId=ids,
        evidenceCode="ECO:0000318",
        limit=200,
    )
    rows = []
    for r in data["results"]:
        sources = []
        for wf in r.get("withFrom") or []:
            for x in wf.get("connectedXrefs") or []:
                sources.append(f"{x.get('db')}:{x.get('id')}" if x.get("db") else x.get("id"))
        nodes = [s for s in sources if "PTN" in s]
        rows.append(
            {
                "gene_product": r["geneProductId"],
                "symbol": r.get("symbol"),
                "term": r["goId"],
                "aspect": r["goAspect"],
                "panther_nodes": nodes,
                "n_sources": len(sources),
            }
        )
    rows.sort(key=lambda x: (x["term"], x["symbol"] or ""))
    return rows


def main() -> None:
    goa_rows = parse_with_from(GOA_TSV)
    target_rec = entry(TARGET)

    resolved = {}
    for row in goa_rows:
        for ident in row["with_from"]:
            if ident not in resolved:
                resolved[ident] = resolve_source(ident)

    protein_sources = [
        r
        for r in resolved.values()
        if r.get("kind") in {"protein", "model-organism gene"} and r.get("accession")
    ]
    characterised = [r for r in protein_sources if r.get("function")]

    signatures = sorted({r["accession"] for r in resolved.values() if r.get("kind") == "InterPro signature"})
    family_signature = "IPR017157" if "IPR017157" in signatures else (signatures[0] if signatures else None)
    if family_signature is None:
        raise SystemExit(
            "no InterPro signature found in the WITH/FROM column of "
            f"{GOA_TSV}; Q2 cannot be computed from this record"
        )

    human_family = ["P22760", "Q6PIU2", "Q6P093", "Q5VUY0", "Q5VUY2"]

    results = {
        "target": {
            "accession": TARGET,
            "uniprot_id": target_rec.get("uniProtkbId"),
            "gene": gene_symbol(target_rec),
            "length": len(sequence(target_rec)),
            "subcellular": locations(target_rec),
            "signal": [span(f) for f in features(target_rec, "Signal")],
            "transmem": [span(f) for f in features(target_rec, "Transmembrane")],
        },
        "goa_rows": goa_rows,
        "q1_catalytic_machinery": q1_catalytic_machinery(target_rec, characterised),
        "q2_family_topology": q2_family_topology(family_signature),
        "q3_with_from_resolution": list(resolved.values()),
        "q4_hpa_protein_class": q4_hpa_protein_class(
            ["AADAC", "NCEH1", "AADACL2", "AADACL3", "AADACL4"]
        ),
        "q5_signal_geometry": q5_signal_geometry(human_family),
        "q6_family_iba_nodes": q6_family_iba_nodes(human_family),
        "q7_observed_peptides": q7_observed_peptides(
            TARGET,
            span(features(target_rec, "Signal")[0])[1] if features(target_rec, "Signal") else None,
        ),
    }

    (HERE / "results.json").write_text(json.dumps(results, indent=2, sort_keys=False) + "\n")

    q1 = results["q1_catalytic_machinery"]
    print(f"AADACL2 ({TARGET}), {q1['target_length']} aa")
    print(f"  own annotated active sites: {q1['target_annotated_active_sites']} "
          f"= {''.join(q1['target_active_site_residues'])}")
    print(f"  GDXG nucleophile-elbow matches: {q1['gdxg_nucleophile_elbow_matches']}")
    print(f"  PROSITE PS01174 (GDXG lipase Ser) on the record: {q1['prosite_gdxg_serine_signature']}")
    for pos, v in q1["per_target_active_site"].items():
        print(f"  position {pos} ({v['target_residue']}): {v['sources_landing_here']}"
              f"/{v['n_sources_considered']} sources align here, "
              f"{v['sources_with_identical_residue']} with the same residue")
    print(f"  sources corroborating the complete triad: "
          f"{q1['n_sources_corroborating_full_triad']}/"
          f"{len([s for s in q1['per_source'] if s['annotated_active_sites']])}")
    for s in q1["per_source"]:
        if not s["annotated_active_sites"]:
            continue
        detail = ", ".join(
            f"{m['source_residue']}{m['source_position']}->{m['target_residue']}{m['target_position']}"
            for m in s["mapped_active_sites"]
        )
        print(f"  vs {s['gene']} ({s['organism']}, {s['percent_identity']}% id): {detail} "
              f"| corroborates the AADACL2 triad: {s['corroborates_target_triad']}")

    q2 = results["q2_family_topology"]
    print(f"\n{q2['signature']}: {q2['n_reviewed_members']} reviewed members; "
          f"{q2['n_with_transmembrane']} with TRANSMEM, "
          f"{q2['n_with_cleaved_signal_only']} with a cleaved SIGNAL and no TRANSMEM "
          f"({q2['cleaved_signal_only_members']}), {q2['n_with_neither']} with neither "
          f"({q2['neither_members']})")

    print("\nHPA protein class:")
    for sym, v in results["q4_hpa_protein_class"].items():
        print(f"  {sym}: {v.get('protein_class')} | RNA: {v.get('rna_tissue_distribution')} "
              f"{v.get('rna_tissue_specific_ntpm')}")

    print("\nSignal-peptide geometry:")
    for r in results["q5_signal_geometry"]:
        print(f"  {r['gene']}: signal={r['signal']} transmem={r['transmem']} "
              f"peak KD-{19} window {r['peak_kd_window']} mean={r['peak_kd_mean']}"
              + (f" | (-3,-1)={r['minus3_minus1']} small at -1: {r['minus1_is_small_neutral']}"
                 if "minus3_minus1" in r else ""))

    print("\nFamily IBA annotations and their PANTHER nodes:")
    for r in results["q6_family_iba_nodes"]:
        print(f"  {r['symbol']:8s} {r['term']} ({r['aspect'][:2]}) nodes={r['panther_nodes']}")

    q7 = results["q7_observed_peptides"]
    print(f"\nObserved peptides for {q7['accession']}: {q7['n_observed_peptides']}, "
          f"earliest residue {q7['earliest_observed_residue']}, annotated cleavage after "
          f"{q7['annotated_signal_cleavage_after']}; any peptide spanning that site: "
          f"{q7['any_peptide_spans_the_annotated_cleavage_site']}; any starting at the mature "
          f"N-terminus: {q7['any_peptide_starts_at_mature_n_terminus']}")
    for p in q7["peptides"]:
        print(f"  {p['begin']:>4}-{p['end']:<4} {p['peptide']} ({', '.join(p['sources'])})")

    print(f"\nwrote {HERE / 'results.json'}")


if __name__ == "__main__":
    main()
