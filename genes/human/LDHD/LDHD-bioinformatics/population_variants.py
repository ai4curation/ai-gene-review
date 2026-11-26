"""Population and clinical-database view of LDHD variation (gnomAD v4, ClinVar).

Outputs:
  * gnomAD constraint metrics (is LDHD haploinsufficient? expected for a recessive enzyme defect: no)
  * predicted loss-of-function (pLoF) alleles: counts, cumulative frequency, homozygotes
  * expected birth prevalence of biallelic pLoF genotypes under Hardy-Weinberg
  * missense variants at residues that contact FAD, Mn2+ or substrate in PDB 8JDE
  * ClinVar small variants by classification, with both isoform numberings
gnomAD annotates each variant on the MANE Select transcript ENST00000450168 (NM_194436,
isoform 2) where it has a coding consequence there; variants that are coding only in
ENST00000300051 (NM_153486, isoform 1) are the ones inside the 69-nt isoform-1-only
start of exon 6, which is intronic in MANE. Those are reported separately and are NOT
counted as loss-of-function alleles of the MANE protein. The isoform-1 (UniProt
displayed) number is added to MANE positions through the VAR_SEQ-derived map.
"""
from __future__ import annotations

import csv
import json
import re
from collections import Counter

import common as c

LOF = {"frameshift_variant", "stop_gained", "splice_acceptor_variant", "splice_donor_variant", "start_lost"}


def main():
    g = c.gnomad()
    i2to1 = c.iso2_to_iso1()
    site = json.loads((c.RESULTS / "structure_survey.json").read_text())["active_site"]
    site_pos = {}
    for k, lst in site.items():
        for x in lst:
            if "mouse" in x:
                site_pos.setdefault(int(x["mouse"][1:]), set()).add(k.split("_within")[0])

    seg = [f for f in c.uniprot_features() if f["type"] == "Alternative sequence"][0]
    seg_a, seg_b = seg["location"]["start"]["value"], seg["location"]["end"]["value"]
    rows, lof_rows = [], []
    for v in g["variants"]:
        n = c.gnomad_counts(v)
        filt = set((v.get("exome") or {}).get("filters") or []) | set((v.get("genome") or {}).get("filters") or [])
        if n["ac"] == 0:
            continue
        on_mane = v["transcript_id"] == g["mane_select_transcript"]["ensembl_id"]
        rec = {"variant_id": v["variant_id"], "annotated_transcript": v["transcript_id"], "isoform1_only_segment": not on_mane, "consequence": v["consequence"], "hgvsc": v["hgvsc"], "hgvsp": v["hgvsp"],
               "lof": v["lof"], "lof_flags": v["lof_flags"], "ac": n["ac"], "an": n["an"], "hom": n["hom"], "af": n["af"], "filters": ";".join(sorted(filt))}
        m = re.match(r"p\.([A-Z][a-z]{2})(\d+)", v["hgvsp"] or "")
        if m and on_mane:
            p2 = int(m.group(2))
            rec["pos_iso2"] = p2
            rec["pos_iso1"] = i2to1.get(p2)
            rec["site_role_8JDE"] = ";".join(sorted(site_pos.get(p2, [])))
        elif m:
            rec["pos_iso1"] = int(m.group(2))  # numbering of the isoform-1 transcript
            assert seg_a <= rec["pos_iso1"] <= seg_b or v["consequence"] not in ("missense_variant", "stop_gained", "frameshift_variant"), rec
        rows.append(rec)
        if v["consequence"] in LOF:
            lof_rows.append(rec)

    iso1_only = [r for r in rows if r["isoform1_only_segment"] and r["consequence"] not in ("intron_variant", "synonymous_variant")]
    hc = [r for r in lof_rows if r["lof"] == "HC" and not r["filters"] and not r["isoform1_only_segment"]]
    cum = sum(r["af"] for r in hc)
    summary = {
        "gnomad_constraint": g["gnomad_constraint"],
        "n_variants_observed": len(rows),
        "consequence_counts": dict(Counter(r["consequence"] for r in rows)),
        "variants_coding_only_in_isoform1_segment": sorted(iso1_only, key=lambda r: -r["af"])[:12],
        "isoform1_segment_pLoF_homozygotes": sum(r["hom"] for r in iso1_only if r["consequence"] in LOF),
        "pLoF_all": len(lof_rows), "pLoF_high_confidence_pass": len(hc),
        "pLoF_HC_cumulative_allele_frequency": cum,
        "pLoF_HC_carrier_frequency_1_in": round(1 / (2 * cum)) if cum else None,
        "pLoF_HC_homozygous_individuals_in_gnomAD": sum(r["hom"] for r in hc),
        "expected_biallelic_pLoF_prevalence_1_in_HWE": round(1 / cum ** 2) if cum else None,
        "top_pLoF": sorted(hc, key=lambda r: -r["af"])[:10],
        "pLoF_HC_with_homozygotes": [r for r in hc if r["hom"]],
        "missense_at_active_site_residues": sorted([r for r in rows if r["consequence"] == "missense_variant" and r.get("site_role_8JDE")], key=lambda r: -r["af"]),
        "missense_homozygotes": sorted([r for r in rows if r["consequence"] == "missense_variant" and r["hom"] > 0], key=lambda r: -r["af"])[:15],
    }
    # add reported pathogenic missense alleles to the cumulative estimate
    rep = json.loads((c.RESULTS / "reported_variants_placed.json").read_text())["database_lookup"]
    rep_af = {k: v["gnomad"]["allele_frequency"] for k, v in rep.items() if v.get("gnomad") and v["gnomad"]["consequence"] == "missense_variant"}
    cum2 = cum + sum(x for x in rep_af.values() if x)
    summary["reported_pathogenic_missense_allele_frequencies"] = rep_af
    summary["cumulative_AF_pLoF_plus_reported_missense"] = cum2
    summary["expected_biallelic_prevalence_1_in_HWE_incl_reported_missense"] = round(1 / cum2 ** 2)

    # ClinVar small variants
    cv = []
    for rec in c.clinvar().values():
        if rec["obj_type"] in ("copy number gain", "copy number loss"):
            continue
        gc = rec["germline_classification"]
        cv.append({"accession": rec["accession"], "title": rec["title"], "type": rec["obj_type"], "classification": gc["description"] or "not classified (germline)",
                   "review_status": gc["review_status"], "conditions": "; ".join(t["trait_name"] for t in gc["trait_set"]),
                   "consequence": "; ".join(rec.get("molecular_consequence_list") or []), "protein_change_iso1_iso2": rec.get("protein_change")})
    summary["clinvar_small_variant_classification_counts"] = dict(Counter(r["classification"] for r in cv))
    summary["clinvar_pathogenic_or_likely_pathogenic"] = [r for r in cv if "athogenic" in r["classification"] and "LDHD" in r["title"]]
    summary["clinvar_copy_number_records_spanning_LDHD"] = sum(1 for r in c.clinvar().values() if r["obj_type"] in ("copy number gain", "copy number loss"))

    (c.RESULTS / "population_variants.json").write_text(json.dumps(summary, indent=1, default=str))
    with open(c.RESULTS / "gnomad_coding_variants.tsv", "w", newline="") as fh:
        keys = ["variant_id", "annotated_transcript", "isoform1_only_segment", "consequence", "hgvsc", "hgvsp", "pos_iso2", "pos_iso1", "site_role_8JDE", "lof", "lof_flags", "ac", "an", "hom", "af", "filters"]
        w = csv.DictWriter(fh, keys, delimiter="\t", extrasaction="ignore")
        w.writeheader()
        w.writerows(r for r in rows if r["consequence"] not in ("intron_variant", "5_prime_UTR_variant", "3_prime_UTR_variant", "synonymous_variant"))
    with open(c.RESULTS / "clinvar_small_variants.tsv", "w", newline="") as fh:
        w = csv.DictWriter(fh, list(cv[0]), delimiter="\t")
        w.writeheader()
        w.writerows(cv)
    print(json.dumps(summary, indent=1, default=str))


if __name__ == "__main__":
    main()
