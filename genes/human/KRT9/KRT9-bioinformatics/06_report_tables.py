# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Render the key result tables as Markdown (results/06_tables.md) from the results/ files.

No analysis happens here; this only formats numbers already written by scripts 01-05 so that
RESULTS.md can be assembled without retyping them.
Usage: uv run 06_report_tables.py [--tag KRT9]
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict

from common import DATA, RESULTS, load_json, read_tsv


def f(v, nd=3):
    if v in ("", None):
        return ""
    try:
        x = float(v)
    except (TypeError, ValueError):
        return str(v)
    if x in (float("inf"), float("-inf")) or x != x:
        return str(v)
    if x == int(x) and abs(x) < 1e6 and "." not in str(v) and "e" not in str(v).lower():
        return str(int(x))
    if x != 0 and (abs(x) < 1e-3 or abs(x) >= 1e5):
        return f"{x:.2e}"
    return f"{x:.{nd}g}"


def table(rows, cols, heads=None):
    heads = heads or cols
    out = ["| " + " | ".join(heads) + " |", "|" + "|".join("---" for _ in cols) + "|"]
    for r in rows:
        out.append("| " + " | ".join(str(f(r.get(c, ""))).replace("|", "/") for c in cols) + " |")
    return "\n".join(out)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--tag", default="KRT9")
    ap.add_argument("--window", type=int, default=20)
    a = ap.parse_args()
    md = []

    dom = read_tsv(RESULTS / f"01_{a.tag}_domains.tsv")
    md += ["## T1 Domain architecture and composition (01_%s_domains.tsv)\n" % a.tag,
           table(dom, ["domain", "start", "end", "length", "pct_G", "pct_S", "pct_G_plus_S", "pct_aromatic_FYW",
                       "pct_charged_DEKR", "shannon_entropy_bits", "top_residues"]), ""]

    arch = load_json(RESULTS / f"01_{a.tag}_architecture.json")
    md += ["## T2 Coiled-coil register per coil segment (01_%s_architecture.json)\n" % a.tag,
           table(arch["coil_segments"], ["segment", "start", "end", "length", "n_core_positions",
                                         "core_fraction_apolar_LIVMFAYWC", "n_discontinuities"]), "",
           table(arch["register_discontinuities"], ["segment", "after_residue", "before_residue", "position_before",
                                                    "position_after", "residues_to_insert_to_restore_heptad",
                                                    "class", "residues_from_segment_end", "context"]), ""]

    merged = read_tsv(RESULTS / "02_variants_merged.tsv")
    cons = {r["position"]: r for r in read_tsv(RESULTS / "04_conservation_per_residue.tsv")}
    vs = {r["position"]: r for r in read_tsv(RESULTS / "05_variant_structure_summary.tsv")}
    dis = [r for r in merged if r["disease_set"] == "yes"]
    for r in dis:
        c = cons.get(r["position"], {})
        r["typeI_identity"] = c.get("typeI_identity", "")
        r["ortholog_identity"] = c.get("ortholog_identity", "")
        r["n_other_keratin_genes"] = c.get("n_other_keratin_genes_with_disease_variant_at_column", "")
        r["clinvar"] = r["clinvar_classifications"] or "(no ClinVar record)"
        r["uniprot"] = r["uniprot_disease"] or "-"
    md += ["## T3 Disease-set variants (02_variants_merged.tsv, 04_conservation_per_residue.tsv)\n",
           table(dis, ["variant", "ref_check", "domain", "heptad", "offset_from_coil1A_start", "offset_to_coil2_end",
                       "uniprot", "clinvar", "clinvar_review_status", "gnomad_ac", "gnomad_af", "typeI_identity",
                       "ortholog_identity", "n_other_keratin_genes", "sources"],
                 ["variant", "ref check", "domain", "heptad", "offset from 1A start", "offset to coil 2 end",
                  "UniProt disease", "ClinVar classification", "ClinVar review status", "gnomAD AC", "gnomAD AF",
                  "type I identity", "ortholog identity", "other keratin genes with disease variant at column",
                  "sources"]), ""]

    dd = read_tsv(RESULTS / "03_domain_distribution.tsv")
    md += ["## T4 Missense variants per domain (03_domain_distribution.tsv)\n",
           table(dd, ["domain", "length", "clinvar_plp_variants", "uniprot_variants", "disease_variants",
                      "disease_positions", "gnomad_variants", "gnomad_positions", "gnomad_missense_allele_count",
                      "gnomad_synonymous_variants", "gnomad_inframe_indel_variants",
                      "gnomad_inframe_indel_allele_count"],
                 ["domain", "length", "ClinVar P/LP", "UniProt disease", "disease set (union)", "disease positions",
                  "gnomAD missense (not in disease set)", "gnomAD missense positions", "gnomAD missense AC",
                  "gnomAD synonymous", "gnomAD in-frame indels", "gnomAD in-frame indel AC"]), ""]

    et = read_tsv(RESULTS / "03_enrichment_tests.tsv")
    keep = [r for r in et if (f"first {a.window} " in r["region"] or f"last {a.window} " in r["region"]
                              or f"({a.window}+{a.window} " in r["region"] or "whole" in r["region"]
                              or "rod coils" in r["region"] or "a/d" in r["region"])]
    cols = ["case_set", "level", "region", "region_length", "case_in", "case_out", "control_in", "control_out",
            "fisher_odds_ratio", "fisher_p_two_sided", "binomial_p_vs_length_fraction_greater"]
    md += ["## T5 Enrichment tests (03_enrichment_tests.tsv)\n", table(keep, cols), "",
           "### T5b Window-size sensitivity, disease set, variant level\n",
           table([r for r in et if r["case_set"] == "disease" and r["level"] == "variants"
                  and ("first" in r["region"] or "last" in r["region"])], cols[2:]), ""]

    st = load_json(RESULTS / "03_statistics.json")
    c = st["constraint"]
    md += ["## T6 gnomAD constraint (03_statistics.json)\n",
           table([{"metric": k, "value": c[k]} for k in ("pLI", "oe_lof", "oe_lof_lower", "oe_lof_upper", "obs_lof",
                                                         "exp_lof", "lof_z", "oe_mis", "oe_mis_lower", "oe_mis_upper",
                                                         "obs_mis", "exp_mis", "mis_z", "oe_syn", "obs_syn", "exp_syn",
                                                         "syn_z")], ["metric", "value"]), "",
           table([{"set": k, **{kk: vv for kk, vv in st[k].items() if kk != "by_consequence"},
                   "by_consequence": ", ".join(f"{x}:{y}" for x, y in st[k]["by_consequence"].items())}
                  for k in ("plof_HC_pass", "plof_HC_pass_without_loftee_flags")],
                 ["set", "n_variants", "total_allele_count", "cumulative_allele_frequency", "homozygotes", "max_af",
                  "max_af_variant", "by_consequence"]), "",
           "ClinVar truncating records:\n",
           table(st["clinvar_truncating_records"], ["variant", "domain", "classification", "review_status",
                                                    "conditions", "gnomad_ac"]), "",
           "Disease-set variants present in gnomAD:\n",
           table(st["disease_variants_also_in_gnomad"], ["variant", "gnomad_ac", "gnomad_af", "gnomad_homozygotes",
                                                         "clinvar"]), "",
           "Ten most frequent gnomAD missense variants:\n",
           table(st["top10_gnomad_missense_by_allele_count"], ["variant", "domain", "gnomad_ac", "gnomad_af", "clinvar",
                                                               "disease_set"]), ""]

    md += ["## T7 Conservation by region (04_region_conservation.tsv)\n",
           table(read_tsv(RESULTS / "04_region_conservation.tsv"),
                 ["region", "n_residues", "mean_typeI_identity", "mean_all_keratin_identity", "mean_ortholog_identity",
                  "n_invariant_in_typeI", "n_positions_with_other_keratin_disease_variant"]), ""]

    vc = read_tsv(RESULTS / "04_variant_conservation.tsv")
    md += ["## T8 Conservation and cross-keratin disease variants at disease-set positions (04_variant_conservation.tsv)\n",
           table(vc, ["position", "residue", "heptad", "typeI_identity", "typeI_residue_counts", "ortholog_identity",
                      "ortholog_residue_counts", "aligned_residues_other_keratins",
                      "n_other_keratin_genes_with_disease_variant_at_column", "hotspot_rank_by_genes",
                      "other_keratin_disease_variants"]), ""]
    hs = read_tsv(RESULTS / "04_hotspot_columns.tsv")[:15]
    md += ["### T8b Alignment columns with disease variants in the most keratin genes (04_hotspot_columns.tsv)\n",
           table(hs, ["rank_by_genes", f"{a.tag}_position", f"{a.tag}_residue", f"{a.tag}_domain",
                      "n_keratin_genes_with_disease_variant", "n_disease_variants", "genes"]), ""]

    md += ["## T9 AlphaFold pLDDT by domain (05_alphafold_plddt_by_domain.tsv)\n",
           table(read_tsv(RESULTS / "05_alphafold_plddt_by_domain.tsv"),
                 ["domain", "start", "end", "mean_plddt", "min_plddt", "max_plddt", "fraction_plddt_ge_90",
                  "fraction_plddt_ge_70", "fraction_plddt_lt_50"]), ""]

    tm = read_tsv(RESULTS / "05_templates.tsv")
    ker = [r for r in tm if r["template_class"].startswith("keratin")]
    rem = [r for r in tm if not r["template_class"].startswith("keratin") and r["alignment_blocks"] == "1"
           and int(r["n_disease_positions_covered"]) > 0]
    tc = ["template", "resolution_A", "chain_gene", "partner_chain", "partner_keratin_gene", "partner_description",
          "template_first_resnum", "template_last_resnum", "target_start", "target_end", "n_aligned_pairs",
          "identity_to_target", "target_domains_covered", "n_disease_positions_covered", "pubmed"]
    md += ["## T10 Templates (05_templates.tsv)\n", "Keratin type I / type II heterodimers:\n", table(ker, tc), "",
           "Non-keratin IF homodimers aligned without gaps and covering disease-set positions:\n", table(rem, tc), "",
           "## T11 Predicted heptad position vs observed partner contact (05_heptad_vs_contact.tsv)\n",
           table(read_tsv(RESULTS / "05_heptad_vs_contact.tsv"),
                 ["template_set", "target_heptad", "n_residue_observations", "fraction_sidechain_contacting_partner",
                  "mean_rsa_in_dimer", "mean_rsa_lost_on_dimerisation"]), ""]

    vss = list(vs.values())
    md += ["## T12 Structural context of disease-set positions (05_variant_structure_summary.tsv)\n",
           table(vss, ["position", "residue", "domain", "heptad", "alphafold_plddt", "keratin_template_residues",
                       "keratin_n_obs", "keratin_n_contact_partner", "keratin_mean_rsa_dimer", "keratin_n_buried",
                       "nonkeratin_template_residues", "nonkeratin_n_obs", "nonkeratin_n_contact_partner",
                       "nonkeratin_mean_rsa_dimer", "nonkeratin_n_buried", "nonkeratin_n_interchain_salt_bridge",
                       "nonkeratin_n_interchain_hbond", "nonkeratin_n_intrachain_salt_bridge", "structural_class"]), ""]

    vm = read_tsv(RESULTS / "05_variant_structure_map.tsv")
    agg = defaultdict(lambda: {"partners": Counter(), "intra": Counter(), "hb": Counter(), "n": 0})
    for r in vm:
        if not (r["template_class"].startswith("keratin") or r["alignment_blocks"] == "1"):
            continue
        key = (r["target_position"], "keratin" if r["template_class"].startswith("keratin") else "non-keratin")
        agg[key]["n"] += 1
        for field, name in (("partner_residues_within_4A", "partners"), ("intrachain_salt_bridges", "intra"),
                            ("interchain_hbond_candidates", "hb")):
            for x in filter(None, r[field].split(";")):
                agg[key][name][r["template"].split(":")[0] + " " + x] += 1
    rows = [{"position": k[0], "template_set": k[1], "n_obs": v["n"],
             "partner_residues_within_4A": ", ".join(sorted(v["partners"])),
             "intrachain_salt_bridge_partners": ", ".join(sorted(v["intra"])),
             "interchain_hbond_candidates": ", ".join(sorted(v["hb"]))} for k, v in sorted(agg.items(), key=lambda kv: (int(kv[0][0]), kv[0][1]))]
    md += ["### T12b Contact partners per position (05_variant_structure_map.tsv; entry, chain:residue)\n",
           table(rows, ["position", "template_set", "n_obs", "partner_residues_within_4A",
                        "intrachain_salt_bridge_partners", "interchain_hbond_candidates"]), ""]

    man = load_json(DATA / "manifest.json")
    md += ["## T0 Data sources (data/manifest.json)\n",
           table([{"key": k, "retrieved_utc": v.get("retrieved_utc", ""), "url": v.get("url", "")[:110],
                   "release": v.get("X-UniProt-Release", v.get("dataset", v.get("panther_version", "")))}
                  for k, v in man.items() if not k.startswith("alphafold_model")],
                 ["key", "retrieved_utc", "release", "url"]), ""]
    (RESULTS / "06_tables.md").write_text("\n".join(md) + "\n")
    print("wrote results/06_tables.md")


if __name__ == "__main__":
    main()
