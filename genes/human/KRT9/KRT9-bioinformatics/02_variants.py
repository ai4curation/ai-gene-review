# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Merge KRT9 variants from UniProt, ClinVar and gnomAD onto the canonical UniProt sequence.

Every variant with a protein-level description is checked against the canonical sequence
(reference residue(s) at the stated position). Outputs:
  results/02_variants_merged.tsv   one row per protein-level change (protein-altering only)
  results/02_clinvar_records.tsv   every ClinVar record returned for the gene
  results/02_gnomad_synonymous.tsv gnomAD synonymous variants (neutral comparison set)
  results/02_numbering_check.json  reference-residue checks and legacy-numbering offsets
  results/02_variant_summary.json  counts per source / class

Usage: uv run 02_variants.py [--accession P35527] [--gene KRT9] [--tag KRT9] [--boundary-window 20]
"""
from __future__ import annotations

import argparse
import re
from collections import Counter, defaultdict

from common import (DATA, HERE, RESULTS, THREE2ONE, architecture, domain_of, dump_json, load_json,
                    natural_variants, read_tsv, seg, write_tsv)

ONE2THREE = {v: k for k, v in THREE2ONE.items() if k != "Sec"}
PLP = {"Pathogenic", "Likely pathogenic", "Pathogenic/Likely pathogenic"}
BLB = {"Benign", "Likely benign", "Benign/Likely benign"}
AA3 = "(?:" + "|".join(THREE2ONE) + ")"


def parse_hgvsp(p: str) -> dict | None:
    """Parse a three-letter protein HGVS string (without transcript prefix)."""
    p = p.strip()
    if p.startswith("p."):
        p = p[2:]
    p = p.strip("()")
    m = re.fullmatch(rf"({AA3})(\d+)=", p)
    if m:
        return {"type": "synonymous", "start": int(m[2]), "end": int(m[2]), "ref_first": THREE2ONE[m[1]]}
    m = re.fullmatch(rf"({AA3})(\d+)({AA3})", p)
    if m:
        ref, alt = THREE2ONE[m[1]], THREE2ONE[m[3]]
        if ref == alt:  # gnomAD writes synonymous changes as p.Ser623Ser
            return {"type": "synonymous", "start": int(m[2]), "end": int(m[2]), "ref_first": ref}
        kind = "nonsense" if alt == "*" else ("stop_lost" if ref == "*" else ("start_lost" if int(m[2]) == 1 else "missense"))
        return {"type": kind, "start": int(m[2]), "end": int(m[2]), "ref_first": ref, "alt": alt,
                "short": f"{ref}{m[2]}{alt}"}
    m = re.fullmatch(rf"({AA3})(\d+)\?", p)
    if m:
        return {"type": "start_lost" if int(m[2]) == 1 else "other", "start": int(m[2]), "end": int(m[2]),
                "ref_first": THREE2ONE[m[1]]}
    m = re.fullmatch(rf"({AA3})(\d+)(?:{AA3})?fs(?:Ter\??\d*|\*\??\d*)?", p)
    if m:
        return {"type": "frameshift", "start": int(m[2]), "end": int(m[2]), "ref_first": THREE2ONE[m[1]]}
    m = re.fullmatch(rf"({AA3})(\d+)(?:_({AA3})(\d+))?(delins|del|dup|ins)((?:{AA3})*)", p)
    if m:
        end = int(m[4]) if m[4] else int(m[2])
        d = {"type": "inframe_" + m[5], "start": int(m[2]), "end": end, "ref_first": THREE2ONE[m[1]]}
        if m[3]:
            d["ref_last"] = THREE2ONE[m[3]]
        return d
    m = re.fullmatch(rf"({AA3})(\d+)(?:{AA3})?ext.*", p)
    if m:
        return {"type": "stop_lost" if THREE2ONE[m[1]] == "*" else "extension", "start": int(m[2]),
                "end": int(m[2]), "ref_first": THREE2ONE[m[1]]}
    return None


def ref_check(parsed: dict, seq: str) -> str:
    def at(pos):
        if pos == len(seq) + 1:
            return "*"
        return seq[pos - 1] if 1 <= pos <= len(seq) else "?"
    ok = at(parsed["start"]) == parsed["ref_first"]
    if "ref_last" in parsed:
        ok = ok and at(parsed["end"]) == parsed["ref_last"]
    return "OK" if ok else f"MISMATCH(canonical {at(parsed['start'])}{parsed['start']})"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--accession", default="P35527")
    ap.add_argument("--gene", default="KRT9")
    ap.add_argument("--tag", default="KRT9")
    ap.add_argument("--boundary-window", type=int, default=20)
    a = ap.parse_args()

    entry = load_json(DATA / f"uniprot_{a.accession}.json")
    seq = entry["sequence"]["value"]
    arch = architecture(entry)
    heptad = {int(r["position"]): r["heptad"] for r in read_tsv(RESULTS / f"01_{a.tag}_heptad_register.tsv")}
    c1a, c2 = seg(arch, "Coil 1A"), seg(arch, "Coil 2")
    interpro = load_json(DATA / f"interpro_{a.accession}.json")
    ps = [m for m in interpro if m["accession"] == "PS00226"]
    w = a.boundary_window

    merged: dict[str, dict] = {}

    def row_for(hgvsp: str, parsed: dict) -> dict:
        key = "p." + hgvsp.removeprefix("p.").strip("()")
        if key not in merged:
            pos = parsed["start"]
            in_seq = 1 <= pos <= len(seq)
            r = {"variant": key, "short": parsed.get("short", ""), "type": parsed["type"],
                 "position": pos, "end_position": parsed["end"],
                 "canonical_residue": seq[pos - 1] if in_seq else "",
                 "ref_check": ref_check(parsed, seq),
                 "domain": domain_of(pos, arch) if in_seq else "",
                 "heptad": heptad.get(pos, ""),
                 "offset_from_coil1A_start": pos - c1a["start"], "offset_to_coil2_end": c2["end"] - pos,
                 "in_helix_initiation_segment": in_seq and c1a["start"] <= pos < c1a["start"] + w,
                 "in_helix_termination_segment": in_seq and c2["end"] - w < pos <= c2["end"],
                 "in_PS00226_signature": any(m["start"] <= pos <= m["end"] for m in ps),
                 "sources": set(), "uniprot_ids": [], "uniprot_disease": set(), "uniprot_pubmed": set(),
                 "clinvar_accessions": [], "clinvar_classifications": [], "clinvar_review_status": [],
                 "clinvar_conditions": set(), "gnomad_variant_ids": [], "gnomad_ac": 0, "gnomad_an": 0,
                 "gnomad_homozygotes": 0, "gnomad_filters": set(), "gnomad_lof": set(),
                 "gnomad_ac_all_incl_filtered": 0}
            merged[key] = r
        return merged[key]

    checks = {"UniProt": Counter(), "ClinVar": Counter(), "gnomAD": Counter()}
    mismatches, unparsed = [], []

    # ---------------- UniProt natural variants
    for v in natural_variants(entry):
        for alt in v["alts"] or [""]:
            if len(v["ref"]) == 1 and len(alt) == 1:
                h = f"p.{ONE2THREE[v['ref']]}{v['start']}{ONE2THREE[alt]}"
            elif alt == "":
                rng = (f"{ONE2THREE[v['ref'][0]]}{v['start']}" +
                       (f"_{ONE2THREE[v['ref'][-1]]}{v['end']}" if v["end"] != v["start"] else ""))
                h = f"p.{rng}del"
            else:
                rng = (f"{ONE2THREE[v['ref'][0]]}{v['start']}" +
                       (f"_{ONE2THREE[v['ref'][-1]]}{v['end']}" if v["end"] != v["start"] else ""))
                h = f"p.{rng}delins{''.join(ONE2THREE[x] for x in alt)}"
            parsed = parse_hgvsp(h)
            ok = seq[v["start"] - 1:v["end"]] == v["ref"]
            checks["UniProt"]["OK" if ok else "MISMATCH"] += 1
            r = row_for(h, parsed)
            r["sources"].add("UniProt")
            r["uniprot_ids"].append(v["feature_id"])
            if v["disease"]:
                r["uniprot_disease"].add(v["disease"])
            r["uniprot_pubmed"].update(v["pubmed"])

    # ---------------- ClinVar
    cv = load_json(DATA / f"clinvar_{a.gene}.json")
    cv_rows = []
    for x in cv["records"]:
        title = x["title"] or ""
        m = re.search(r"\((p\.[^)]+)\)\s*$", title)
        hg = m.group(1) if m else ""
        parsed = parse_hgvsp(hg) if hg else None
        single_gene = x["genes"] == [a.gene]
        on_tx = title.startswith("NM_")
        status = "no protein change"
        if hg and parsed is None:
            unparsed.append({"source": "ClinVar", "id": x["accession"], "hgvsp": hg})
            status = "unparsed"
        elif parsed:
            status = ref_check(parsed, seq)
            checks["ClinVar"]["OK" if status == "OK" else "MISMATCH"] += 1
            if status != "OK":
                mismatches.append({"source": "ClinVar", "id": x["accession"], "hgvsp": hg, "check": status})
        cv_rows.append({"accession": x["accession"], "title": title, "variation_type": x["obj_type"],
                        "n_genes": len(x["genes"]), "hgvsp": hg, "class": parsed["type"] if parsed else "",
                        "ref_check": status, "classification": x["germline_classification"],
                        "review_status": x["review_status"], "last_evaluated": x["last_evaluated"],
                        "conditions": x["conditions"], "molecular_consequences": x["molecular_consequences"],
                        "dbsnp": x["dbsnp"]})
        if parsed and single_gene and on_tx and parsed["type"] != "synonymous":
            r = row_for(hg, parsed)
            r["sources"].add("ClinVar")
            r["clinvar_accessions"].append(x["accession"])
            r["clinvar_classifications"].append(x["germline_classification"] or "not provided")
            r["clinvar_review_status"].append(x["review_status"] or "")
            r["clinvar_conditions"].update(c for c in x["conditions"] if c)
    write_tsv(cv_rows, RESULTS / "02_clinvar_records.tsv")

    # ---------------- gnomAD
    gn = load_json(DATA / f"gnomad_{a.gene}.json")
    canon = gn["gene"]["canonical_transcript_id"]
    n_noncanon = 0
    syn_rows = []
    for v in gn["variants"]:
        if v["transcript_id"] != canon:
            n_noncanon += 1
            continue
        ac = an = hom = ac_all = 0
        filt = set()
        for ds in ("exome", "genome"):
            d = v.get(ds)
            if not d:
                continue
            ac_all += d["ac"]
            if d["filters"]:
                filt.update(f"{ds}:{f}" for f in d["filters"])
                continue
            ac += d["ac"]; an += d["an"]; hom += d["homozygote_count"]
        hg = v.get("hgvsp") or ""
        parsed = parse_hgvsp(hg) if hg else None
        if hg and parsed is None:
            unparsed.append({"source": "gnomAD", "id": v["variant_id"], "hgvsp": hg})
        if parsed is None:
            if v.get("lof") or v["consequence"].startswith("splice_"):
                key = f"{v['consequence']}:{v['hgvsc'] or v['variant_id']}"
                merged[key] = {"variant": key, "short": "", "type": v["consequence"], "position": "",
                               "sources": {"gnomAD"}, "gnomad_variant_ids": [v["variant_id"]], "gnomad_ac": ac,
                               "gnomad_an": an, "gnomad_homozygotes": hom, "gnomad_filters": filt,
                               "gnomad_lof": {v["lof"]} if v.get("lof") else set(),
                               "gnomad_ac_all_incl_filtered": ac_all, "uniprot_ids": [],
                               "clinvar_accessions": [], "clinvar_classifications": [],
                               "clinvar_review_status": [], "clinvar_conditions": set(),
                               "uniprot_disease": set(), "uniprot_pubmed": set(), "ref_check": "NA"}
            continue
        status = ref_check(parsed, seq)
        checks["gnomAD"]["OK" if status == "OK" else "MISMATCH"] += 1
        if parsed["type"] == "synonymous":
            syn_rows.append({"variant_id": v["variant_id"], "hgvsp": hg, "position": parsed["start"],
                             "domain": domain_of(parsed["start"], arch), "ref_check": status,
                             "gnomad_ac_pass": ac, "gnomad_an": an})
            continue
        if status != "OK":
            mismatches.append({"source": "gnomAD", "id": v["variant_id"], "hgvsp": hg, "check": status})
        r = row_for(hg, parsed)
        r["sources"].add("gnomAD")
        r["gnomad_variant_ids"].append(v["variant_id"])
        r["gnomad_ac"] += ac
        r["gnomad_an"] = max(r["gnomad_an"], an)
        r["gnomad_homozygotes"] += hom
        r["gnomad_filters"].update(filt)
        r["gnomad_ac_all_incl_filtered"] += ac_all
        if v.get("lof"):
            r["gnomad_lof"].add(v["lof"])

    write_tsv(syn_rows, RESULTS / "02_gnomad_synonymous.tsv")
    rows = []
    for r in merged.values():
        cls = set(r["clinvar_classifications"])
        r["clinvar_summary"] = ("P/LP" if cls & PLP else "B/LB" if cls and cls <= BLB else
                                "VUS/conflicting/other" if cls else "")
        r["uniprot_disease_variant"] = bool(r["uniprot_disease"])
        r["disease_set"] = bool(r["uniprot_disease"]) or bool(cls & PLP)
        r["gnomad_af"] = (r["gnomad_ac"] / r["gnomad_an"]) if r.get("gnomad_an") else ""
        r["gnomad_pass"] = ("gnomAD" in r["sources"]) and r["gnomad_ac"] > 0
        for k in ("sources", "uniprot_disease", "uniprot_pubmed", "clinvar_conditions", "gnomad_filters",
                  "gnomad_lof"):
            r[k] = sorted(r[k])
        r["clinvar_classifications"] = sorted(set(r["clinvar_classifications"]))
        r["clinvar_review_status"] = sorted(set(r["clinvar_review_status"]))
        rows.append(r)
    rows.sort(key=lambda r: (r["position"] if r["position"] != "" else 10 ** 6, r["variant"]))
    cols = ["variant", "short", "type", "position", "end_position", "canonical_residue", "ref_check", "domain",
            "heptad", "offset_from_coil1A_start", "offset_to_coil2_end", "in_helix_initiation_segment",
            "in_helix_termination_segment", "in_PS00226_signature", "disease_set", "uniprot_disease_variant",
            "uniprot_disease", "uniprot_ids", "uniprot_pubmed", "clinvar_summary", "clinvar_classifications",
            "clinvar_review_status", "clinvar_conditions", "clinvar_accessions", "gnomad_pass", "gnomad_ac",
            "gnomad_an", "gnomad_af", "gnomad_homozygotes", "gnomad_lof", "gnomad_filters",
            "gnomad_ac_all_incl_filtered", "gnomad_variant_ids", "sources"]
    write_tsv(rows, RESULTS / "02_variants_merged.tsv", cols)

    # ---------------- numbering check
    conflicts = []
    for f in entry["features"]:
        if f["type"] != "Sequence conflict":
            continue
        alt = f.get("alternativeSequence", {})
        orig = alt.get("originalSequence", "")
        alts = alt.get("alternativeSequences", [""])
        conflicts.append({"start": f["location"]["start"]["value"], "end": f["location"]["end"]["value"],
                          "canonical": orig, "alternative": alts[0] if alts else "",
                          "length_change": len(alts[0] if alts else "") - len(orig),
                          "description": f.get("description", "")})
    disease_pos = sorted({r["position"] for r in rows if r.get("disease_set") and r["position"] != ""})
    legacy = []
    for pos in disease_pos:
        for c in conflicts:
            if c["length_change"] != 0 and c["end"] < pos:
                legacy.append({"canonical_position": pos, "canonical_residue": seq[pos - 1],
                               "position_in_conflicting_sequence": pos + c["length_change"],
                               "conflict": f"{c['start']}..{c['end']} {c['canonical']}->{c['alternative']}",
                               "conflict_description": c["description"]})
    arg_window = {str(p): seq[p - 1] for p in range(c1a["start"], c1a["start"] + w)}
    local = HERE.parent / f"{a.gene}-uniprot.txt"
    local_check = "local flat file not found"
    if local.exists():
        lines = local.read_text().splitlines()
        i = next(k for k, ln in enumerate(lines) if ln.startswith("SQ "))
        lseq = "".join("".join(ln.split()) for ln in lines[i + 1:] if not ln.startswith("//"))
        local_check = "identical" if lseq == seq else f"DIFFERENT (local length {len(lseq)})"
    dump_json({
        "canonical_length": len(seq),
        "fetched_sequence_vs_local_uniprot_flat_file": local_check, "sequence_version": entry["entryAudit"]["sequenceVersion"],
        "reference_residue_checks": {k: dict(v) for k, v in checks.items()},
        "mismatches": mismatches, "unparsed_protein_hgvs": unparsed,
        "gnomad_canonical_transcript": canon, "gnomad_mane_select": gn["gene"].get("mane_select_transcript"),
        "gnomad_variants_on_other_transcripts_skipped": n_noncanon,
        "canonical_residues_start_of_coil_1A": arg_window,
        "arginine_positions_in_first_window_of_coil_1A": [int(p) for p, aa in arg_window.items() if aa == "R"],
        "sequence_conflicts": conflicts, "legacy_numbering_of_disease_positions": legacy,
    }, RESULTS / "02_numbering_check.json")

    by = defaultdict(Counter)
    for r in rows:
        for s in r["sources"]:
            by[s][r["type"]] += 1
        if r.get("disease_set"):
            by["disease_set"][r["type"]] += 1
        if r["clinvar_summary"]:
            by["ClinVar:" + r["clinvar_summary"]][r["type"]] += 1
    dump_json({"n_rows": len(rows), "counts_by_source_and_type": {k: dict(v) for k, v in by.items()},
               "clinvar_esearch_count": cv["esearch_count"], "clinvar_records": len(cv["records"]),
               "clinvar_classification_counts_all_records": dict(Counter(x["classification"] or "none" for x in cv_rows)),
               "clinvar_multigene_records": sum(1 for x in cv_rows if x["n_genes"] != 1),
               "gnomad_dataset": gn["dataset"], "gnomad_consequence_counts_all": gn["consequence_counts"],
               "disease_set_definition": "UniProt natural variant with a disease note, or ClinVar "
                                         "Pathogenic / Likely pathogenic / Pathogenic/Likely pathogenic"},
              RESULTS / "02_variant_summary.json")
    print(f"merged rows: {len(rows)}; mismatches: {len(mismatches)}; unparsed: {len(unparsed)}")


if __name__ == "__main__":
    main()
