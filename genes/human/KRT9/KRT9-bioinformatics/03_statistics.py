# /// script
# requires-python = ">=3.11"
# dependencies = ["scipy==1.16.1", "numpy==2.3.2"]
# ///
"""Positional distribution of disease vs population missense variants, and pLoF tolerance.

Reads results/02_variants_merged.tsv and data/gnomad_<gene>.json. Outputs:
  results/03_domain_distribution.tsv   variants per domain for each variant set
  results/03_enrichment_tests.tsv      Fisher exact / binomial tests for regions of interest
  results/03_boundary_gnomad_missense.tsv  gnomAD missense variants inside the boundary segments
  results/03_plof.tsv                  gnomAD predicted loss-of-function variants
  results/03_statistics.json           constraint metrics and pLoF / in-frame indel summaries

Variant sets (missense only unless stated):
  clinvar_plp   ClinVar Pathogenic / Likely pathogenic / Pathogenic/Likely pathogenic
  uniprot       UniProt natural variants carrying a disease note
  disease       union of the two
  gnomad        gnomAD variants passing filters with AC > 0 that are NOT in the disease set
Usage: uv run 03_statistics.py [--accession P35527] [--gene KRT9] [--tag KRT9]
"""
from __future__ import annotations

import argparse
from collections import Counter

from scipy.stats import binomtest, fisher_exact

from common import DATA, RESULTS, architecture, dump_json, load_json, read_tsv, seg, write_tsv


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--accession", default="P35527")
    ap.add_argument("--gene", default="KRT9")
    ap.add_argument("--tag", default="KRT9")
    ap.add_argument("--windows", default="10,15,20,25,30")
    a = ap.parse_args()

    entry = load_json(DATA / f"uniprot_{a.accession}.json")
    L = entry["sequence"]["length"]
    arch = architecture(entry)
    rows = read_tsv(RESULTS / "02_variants_merged.tsv")
    syn = read_tsv(RESULTS / "02_gnomad_synonymous.tsv")
    for r in rows:
        r["pos"] = int(r["position"]) if r["position"] else None
        r["ac"] = int(r["gnomad_ac"] or 0)
    mis = [r for r in rows if r["type"] == "missense"]
    sets = {
        "clinvar_plp": [r for r in mis if r["clinvar_summary"] == "P/LP"],
        "uniprot": [r for r in mis if r["uniprot_disease_variant"] == "yes"],
        "disease": [r for r in mis if r["disease_set"] == "yes"],
        "gnomad": [r for r in mis if r["gnomad_pass"] == "yes" and r["disease_set"] != "yes"],
        "gnomad_all_pass": [r for r in mis if r["gnomad_pass"] == "yes"],
        "clinvar_blb": [r for r in mis if r["clinvar_summary"] == "B/LB"],
        "clinvar_vus_other": [r for r in mis if r["clinvar_summary"] == "VUS/conflicting/other"],
    }
    inframe = [r for r in rows if r["type"].startswith("inframe") and r["gnomad_pass"] == "yes"]

    # ---------------- per-domain distribution
    dom_rows = []
    for s in arch + [{"name": "full length", "start": 1, "end": L}]:
        inside = lambda r: r["pos"] is not None and s["start"] <= r["pos"] <= s["end"]
        n = s["end"] - s["start"] + 1
        d = {"domain": s["name"], "start": s["start"], "end": s["end"], "length": n,
             "fraction_of_protein": n / L}
        for k, v in sets.items():
            sub = [r for r in v if inside(r)]
            d[f"{k}_variants"] = len(sub)
            d[f"{k}_positions"] = len({r["pos"] for r in sub})
        d["disease_variants_per_100_residues"] = 100 * d["disease_variants"] / n
        d["gnomad_variants_per_100_residues"] = 100 * d["gnomad_variants"] / n
        d["gnomad_missense_allele_count"] = sum(r["ac"] for r in sets["gnomad"] if inside(r))
        d["gnomad_synonymous_variants"] = sum(1 for r in syn if s["start"] <= int(r["position"]) <= s["end"]
                                              and int(r["gnomad_ac_pass"]) > 0)
        sub = [r for r in inframe if inside(r)]
        d["gnomad_inframe_indel_variants"] = len(sub)
        d["gnomad_inframe_indel_allele_count"] = sum(r["ac"] for r in sub)
        dom_rows.append(d)
    write_tsv(dom_rows, RESULTS / "03_domain_distribution.tsv")

    # ---------------- enrichment tests
    c1a, c2 = seg(arch, "Coil 1A"), seg(arch, "Coil 2")
    coils = [s for s in arch if s["name"].startswith("Coil")]
    regions = {}
    for w in [int(x) for x in a.windows.split(",")]:
        him = set(range(c1a["start"], c1a["start"] + w))
        htm = set(range(c2["end"] - w + 1, c2["end"] + 1))
        regions[f"helix initiation segment (first {w} of Coil 1A)"] = him
        regions[f"helix termination segment (last {w} of Coil 2)"] = htm
        regions[f"both boundary segments ({w}+{w} residues)"] = him | htm
    regions["Coil 1A (whole)"] = set(range(c1a["start"], c1a["end"] + 1))
    regions["rod coils (1A+1B+2)"] = {p for s in coils for p in range(s["start"], s["end"] + 1)}
    regions["heptad a/d positions of rod coils"] = {r["pos"] for r in rows if r["heptad"] in ("a", "d")} | set()
    reg_from_table = {int(r["position"]) for r in read_tsv(RESULTS / f"01_{a.tag}_heptad_register.tsv")
                      if r["heptad"] in ("a", "d")}
    regions["heptad a/d positions of rod coils"] = reg_from_table

    tests = []
    for case_name in ("disease", "clinvar_plp", "uniprot"):
        case = sets[case_name]
        ctrl = [r for r in sets["gnomad_all_pass"] if r["variant"] not in {c["variant"] for c in case}]
        for label, reg in regions.items():
            for level in ("variants", "positions"):
                if level == "variants":
                    ci = sum(1 for r in case if r["pos"] in reg); co = len(case) - ci
                    gi = sum(1 for r in ctrl if r["pos"] in reg); go = len(ctrl) - gi
                else:
                    cpos = {r["pos"] for r in case}
                    gpos = {r["pos"] for r in ctrl} - cpos
                    ci = len(cpos & reg); co = len(cpos) - ci
                    gi = len(gpos & reg); go = len(gpos) - gi
                odds, p = fisher_exact([[ci, co], [gi, go]], alternative="two-sided")
                frac = len(reg) / L
                b = binomtest(ci, ci + co, frac, alternative="greater") if ci + co else None
                tests.append({"case_set": case_name, "control_set": "gnomAD PASS missense not in case set",
                              "level": level, "region": label, "region_length": len(reg),
                              "region_fraction_of_protein": frac,
                              "case_in": ci, "case_out": co, "control_in": gi, "control_out": go,
                              "case_fraction_in": ci / (ci + co) if ci + co else "",
                              "control_fraction_in": gi / (gi + go) if gi + go else "",
                              "fisher_odds_ratio": odds, "fisher_p_two_sided": p,
                              "binomial_p_vs_length_fraction_greater": b.pvalue if b else ""})
    write_tsv(tests, RESULTS / "03_enrichment_tests.tsv")

    w0 = 20
    him = set(range(c1a["start"], c1a["start"] + w0)); htm = set(range(c2["end"] - w0 + 1, c2["end"] + 1))
    bnd = [{"variant": r["variant"], "position": r["pos"], "segment": "initiation" if r["pos"] in him else "termination",
            "heptad": r["heptad"], "gnomad_ac": r["ac"], "gnomad_af": r["gnomad_af"],
            "gnomad_homozygotes": r["gnomad_homozygotes"], "disease_set": r["disease_set"],
            "clinvar_classifications": r["clinvar_classifications"]}
           for r in sets["gnomad_all_pass"] if r["pos"] in him | htm]
    write_tsv(bnd, RESULTS / "03_boundary_gnomad_missense.tsv")

    # ---------------- pLoF
    gn = load_json(DATA / f"gnomad_{a.gene}.json")
    canon = gn["gene"]["canonical_transcript_id"]
    plof_rows = []
    for v in gn["variants"]:
        if v["transcript_id"] != canon or not v.get("lof"):
            continue
        ac = an = hom = 0
        passed = False
        for ds in ("exome", "genome"):
            d = v.get(ds)
            if d and not d["filters"]:
                ac += d["ac"]; an += d["an"]; hom += d["homozygote_count"]; passed = True
        plof_rows.append({"variant_id": v["variant_id"], "consequence": v["consequence"], "hgvsc": v["hgvsc"],
                          "hgvsp": v["hgvsp"], "loftee": v["lof"], "loftee_filter": v["lof_filter"],
                          "loftee_flags": v["lof_flags"], "pass": passed, "ac": ac, "an": an,
                          "af": ac / an if an else "", "homozygotes": hom})
    plof_rows.sort(key=lambda r: -r["ac"])
    write_tsv(plof_rows, RESULTS / "03_plof.tsv")
    hc = [r for r in plof_rows if r["loftee"] == "HC" and r["pass"] and r["ac"] > 0]
    hc_noflag = [r for r in hc if not r["loftee_flags"]]
    merged_lof = [r for r in rows if r["type"] in ("nonsense", "frameshift") and r["pos"]]

    def lof_summary(sub):
        return {"n_variants": len(sub), "total_allele_count": sum(r["ac"] for r in sub),
                "cumulative_allele_frequency": sum(r["af"] for r in sub if r["af"] != ""),
                "homozygotes": sum(r["homozygotes"] for r in sub),
                "max_af_variant": max(sub, key=lambda r: r["af"] or 0)["variant_id"] if sub else None,
                "max_af": max((r["af"] or 0) for r in sub) if sub else None,
                "by_consequence": dict(Counter(r["consequence"] for r in sub))}

    by_dom = Counter()
    for r in merged_lof:
        if r["gnomad_pass"] == "yes" and "HC" in r["gnomad_lof"]:
            by_dom[r["domain"]] += 1
    clin_lof = [{"variant": r["variant"], "domain": r["domain"], "classification": r["clinvar_classifications"],
                 "review_status": r["clinvar_review_status"], "conditions": r["clinvar_conditions"],
                 "gnomad_ac": r["ac"]}
                for r in rows if r["type"] in ("nonsense", "frameshift", "start_lost") and r["clinvar_accessions"]]
    disease_types = Counter(r["type"] for r in rows if r["disease_set"] == "yes")
    top_mis = sorted(sets["gnomad_all_pass"], key=lambda r: -r["ac"])[:10]
    dump_json({
        "gnomad_dataset": gn["dataset"], "gnomad_gene": {k: gn["gene"][k] for k in ("gene_id", "canonical_transcript_id")},
        "constraint": gn["gene"]["gnomad_constraint"],
        "plof_HC_pass": lof_summary(hc), "plof_HC_pass_without_loftee_flags": lof_summary(hc_noflag),
        "plof_LC_or_filtered_n": len(plof_rows) - len(hc),
        "plof_HC_nonsense_frameshift_by_domain": dict(by_dom),
        "clinvar_truncating_records": clin_lof,
        "disease_set_variant_types": dict(disease_types),
        "disease_missense_by_heptad_position": dict(Counter(r["heptad"] or "none" for r in sets["disease"])),
        "gnomad_missense_by_heptad_position": dict(Counter(r["heptad"] or "none" for r in sets["gnomad"])),
        "disease_missense_to_proline": sorted(r["variant"] for r in sets["disease"] if r["variant"].endswith("Pro")),
        "gnomad_missense_to_proline_in_coil_segments": sorted(
            f"{r['variant']} (AC {r['ac']})" for r in sets["gnomad"]
            if r["variant"].endswith("Pro") and r["domain"].startswith("Coil")),
        "set_sizes": {k: {"variants": len(v), "positions": len({r['pos'] for r in v})} for k, v in sets.items()},
        "disease_variants_also_in_gnomad": [{"variant": r["variant"], "gnomad_ac": r["ac"], "gnomad_af": r["gnomad_af"],
                                             "gnomad_homozygotes": r["gnomad_homozygotes"],
                                             "clinvar": r["clinvar_classifications"]}
                                            for r in sets["disease"] if r["gnomad_pass"] == "yes"],
        "top10_gnomad_missense_by_allele_count": [{"variant": r["variant"], "domain": r["domain"], "gnomad_ac": r["ac"],
                                                   "gnomad_af": r["gnomad_af"], "clinvar": r["clinvar_classifications"],
                                                   "disease_set": r["disease_set"]} for r in top_mis],
        "gnomad_inframe_indels": {"n_variants": len(inframe), "total_allele_count": sum(r["ac"] for r in inframe),
                                  "by_domain": dict(Counter(r["domain"] for r in inframe))},
    }, RESULTS / "03_statistics.json")
    print("wrote 03_*")


if __name__ == "__main__":
    main()
