"""Population and clinical-database evidence for AK1 from gnomAD (GraphQL API).

Retrieves gene constraint, every gnomAD v4 variant on the MANE transcript, and
the ClinVar records gnomAD mirrors for the gene. Reports the frequency of each
reported disease variant, the count of predicted loss-of-function alleles and any
homozygotes. If the API is unreachable the script fails; it writes no placeholder.
"""
from __future__ import annotations

import json
import re

import yaml

from ak1_common import HERE, dump, fetch

QUERY = """
query AK1 {
  gene(gene_symbol: "AK1", reference_genome: GRCh38) {
    gene_id symbol chrom start stop canonical_transcript_id
    mane_select_transcript { ensembl_id ensembl_version refseq_id refseq_version }
    gnomad_constraint { pLI oe_lof oe_lof_lower oe_lof_upper oe_mis oe_mis_lower oe_mis_upper mis_z syn_z exp_lof obs_lof exp_mis obs_mis }
    variants(dataset: gnomad_r4) {
      variant_id consequence hgvsc hgvsp lof transcript_id flags
      exome { ac an homozygote_count }
      genome { ac an homozygote_count }
    }
    clinvar_variants {
      variant_id clinvar_variation_id clinical_significance gold_stars review_status
      major_consequence hgvsc hgvsp transcript_id
    }
  }
}
"""

THREE2ONE = {"Ala": "A", "Arg": "R", "Asn": "N", "Asp": "D", "Cys": "C", "Gln": "Q", "Glu": "E",
             "Gly": "G", "His": "H", "Ile": "I", "Leu": "L", "Lys": "K", "Met": "M", "Phe": "F",
             "Pro": "P", "Ser": "S", "Thr": "T", "Trp": "W", "Tyr": "Y", "Val": "V", "Ter": "*"}
LOF = {"stop_gained", "frameshift_variant", "splice_acceptor_variant", "splice_donor_variant", "start_lost"}


def main() -> None:
    raw = json.loads(fetch("https://gnomad.broadinstitute.org/api", "gnomad_ak1.json",
                           post_json={"query": QUERY}).read_text())
    if raw.get("errors"):
        raise SystemExit(f"gnomAD API errors: {raw['errors']}")
    gene = raw["data"]["gene"]
    canon = gene["canonical_transcript_id"]

    def counts(v):
        ac = sum((v[k] or {}).get("ac", 0) for k in ("exome", "genome"))
        an = max(((v[k] or {}).get("an", 0) for k in ("exome", "genome")), default=0)
        an_sum = sum((v[k] or {}).get("an", 0) for k in ("exome", "genome"))
        hom = sum((v[k] or {}).get("homozygote_count", 0) for k in ("exome", "genome"))
        return ac, an_sum, hom

    variants = [v for v in gene["variants"] if v["transcript_id"] == canon]
    by_hgvsc = {}
    for v in variants:
        if v["hgvsc"]:
            by_hgvsc.setdefault(v["hgvsc"], []).append(v)
    spec = yaml.safe_load((HERE / "reported_variants.yaml").read_text())
    reported = []
    cons_path = HERE / "results" / "variant_consequences.json"
    computed_p = {}
    if cons_path.exists():
        computed_p = {v["cdna"]: v.get("hgvs_p") for v in json.loads(cons_path.read_text())["variants"]
                      if v.get("class") != "missense" and v.get("hgvs_p")}
    for r in spec["variants"]:
        hits = by_hgvsc.get(r["cdna"], [])
        if not hits:  # deletions/duplications are written with the bases in gnomAD
            pos = re.search(r"c\.(\d+)", r["cdna"]).group(1)
            kind = "del" if "del" in r["cdna"] else "dup" if "dup" in r["cdna"] else None
            if kind:
                hits = [v for h, vs in by_hgvsc.items() for v in vs
                        if re.match(rf"c\.{pos}(_\d+)?{kind}", h)]
        if not hits and r["cdna"] in computed_p:
            # gnomAD left-/right-shifts indels in repeats (c.418_420del is written c.421_423del),
            # so fall back to the protein consequence computed by 01_variant_consequences.py
            hits = [v for v in variants if v["hgvsp"] == computed_p[r["cdna"]]]
        row = {"cdna": r["cdna"], "in_gnomad_v4": bool(hits)}
        if hits:
            ac, an, hom = (sum(x) for x in zip(*(counts(v) for v in hits)))
            row.update({"gnomad_ids": [v["variant_id"] for v in hits], "gnomad_hgvsc": [v["hgvsc"] for v in hits],
                        "hgvsp": hits[0]["hgvsp"],
                        "allele_count": ac, "allele_number": an, "homozygotes": hom,
                        "allele_frequency": ac / an if an else None})
        reported.append(row)

    lof = [v for v in variants if v["consequence"] in LOF]
    lof_rows = []
    for v in lof:
        ac, an, hom = counts(v)
        lof_rows.append({"variant_id": v["variant_id"], "consequence": v["consequence"], "hgvsc": v["hgvsc"],
                         "hgvsp": v["hgvsp"], "loftee": v["lof"], "flags": v["flags"],
                         "allele_count": ac, "allele_number": an, "homozygotes": hom})
    mis = [v for v in variants if v["consequence"] == "missense_variant"]
    mis_hom = []
    for v in mis:
        ac, an, hom = counts(v)
        if hom:
            mis_hom.append({"hgvsp": v["hgvsp"], "allele_count": ac, "allele_number": an, "homozygotes": hom,
                            "allele_frequency": ac / an if an else None})
    hc_lof = [r for r in lof_rows if r["loftee"] == "HC"]
    clin = gene["clinvar_variants"] or []
    clin_plp = [c for c in clin if re.search(r"athogenic", c["clinical_significance"] or "")
                and "Conflicting" not in c["clinical_significance"]]
    sig_counts: dict[str, int] = {}
    for c in clin:
        sig_counts[c["clinical_significance"]] = sig_counts.get(c["clinical_significance"], 0) + 1
    out = {
        "gene": {k: gene[k] for k in ("gene_id", "symbol", "chrom", "start", "stop", "canonical_transcript_id",
                                      "mane_select_transcript")},
        "constraint": gene["gnomad_constraint"],
        "n_variants_on_canonical_transcript": len(variants),
        "n_missense": len(mis),
        "missense_with_homozygotes": sorted(mis_hom, key=lambda r: -r["homozygotes"]),
        "predicted_lof_variants": sorted(lof_rows, key=lambda r: -r["allele_count"]),
        "all_predicted_lof_summary": {"n_variants": len(lof_rows),
                                      "total_allele_count": sum(r["allele_count"] for r in lof_rows),
                                      "homozygotes": sum(r["homozygotes"] for r in lof_rows)},
        "high_confidence_lof_summary": {
            "n_variants": len(hc_lof),
            "total_allele_count": sum(r["allele_count"] for r in hc_lof),
            "homozygotes": sum(r["homozygotes"] for r in hc_lof),
            "max_allele_number": max((r["allele_number"] for r in hc_lof), default=0),
        },
        "reported_disease_variants": reported,
        "clinvar": {"n_records": len(clin), "by_significance": sig_counts,
                    "pathogenic_or_likely_pathogenic": clin_plp},
    }
    hc = out["high_confidence_lof_summary"]
    if hc["max_allele_number"]:
        q = hc["total_allele_count"] / hc["max_allele_number"]
        out["high_confidence_lof_summary"]["cumulative_carrier_allele_frequency"] = q
        out["high_confidence_lof_summary"]["expected_biallelic_lof_per_million_births_hardy_weinberg"] = q * q * 1e6
    dump(out, "population.json")
    print(json.dumps({k: out[k] for k in ("gene", "constraint", "n_variants_on_canonical_transcript", "n_missense",
                                          "high_confidence_lof_summary")}, indent=1))
    print("missense with homozygotes:", out["missense_with_homozygotes"][:8])
    for r in reported:
        print(r)
    print("ClinVar:", sig_counts)
    for c in clin_plp:
        print("  ", c["clinvar_variation_id"], c["clinical_significance"], c["gold_stars"], c["hgvsc"], c["hgvsp"], c["major_consequence"])


if __name__ == "__main__":
    main()
