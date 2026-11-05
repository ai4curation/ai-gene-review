"""Write plain-text, quotable summaries of the PP_0149 BERIL runs.
Usage: python3 -I summarize.py KT2440_RESULTS ORTHOLOG_RESULTS FAMILY_RESULTS OUTDIR"""
import json, sys, os
kt, orth, fam, out = sys.argv[1:5]
os.makedirs(out, exist_ok=True)
kt, orth, fam = (json.load(open(p)) for p in (kt, orth, fam))
L = ["# PP_0149 Fitness Browser summary (kescience.fitnessbrowser via BERDL)", "", "## KT2440 (orgId Putida)"]
for g in ("PP_0148", "PP_0149", "PP_0150", "PP_0151", "PP_0152"):
    s = kt["per_gene_summary"][g]
    L.append(f"{g}: {s['n_experiments']} experiments; {s['n_abs_fit_ge1_and_abs_t_ge4']} with |fit|>=1 and |t|>=4; min fit {s['min_fit']:.2f}; max fit {s['max_fit']:.2f}")
lo = kt["per_gene_summary"]["PP_0149"]["lowest5"][0]
L.append(f"PP_0149 lowest fitness: {lo['fit']:.2f} (t {lo['t']:.1f}) in {lo['expdesc']}")
L.append(f"KT2440 quaternary ammonium (benzalkonium/benzethonium) experiments: {len(kt['qac_experiments'])}")
L.append("KT2440 PP_0149 top cofitness partners (cofit): " + "; ".join(f"{c['hitid']} {c['desc']} ({c['cofit']:.2f})" for c in kt["cofit_top20"][:5]))
L += ["", "## Fitness Browser orthologs of PP_0149 (ortholog table)"]
for org, d in orth["per_ortholog"].items():
    if org == "SyringaeB728a_mexBdelta":
        continue
    sn = "; ".join(f"{r['expdesc']} {r['fit']:.2f} (t {r['t']:.1f})" for r in d["strong_neg"]) or "none"
    sp = "; ".join(s["expdesc"] for s in d["specificphenotype"]) or "none"
    L.append(f"{org} {d['locus']} (BLAST score ratio {d['bsr_ratio']:.2f}): {d['n_experiments']} experiments; strong defects (fit<=-1, t<=-4): {sn}; specific phenotypes: {sp}")
    for c in d["qac_experiments"]:
        of = c["ortholog_fit"][0] if c["ortholog_fit"] else None
        pf = c["PP_0150_ortholog_fit"][0] if c["PP_0150_ortholog_fit"] else None
        L.append(f"  {c['expdesc']} ({c['expname']}): {c['n_strong_neg']} of {c['n_genes']} genes have fit<=-1 and t<=-4; ortholog fit {of['fit']:.2f} (t {of['t']:.1f}); rank among those genes {c['ortholog_rank_among_strong']}"
                 + (f"; PP_0150 ortholog {d['PP_0150_ortholog']} fit {pf['fit']:.2f} (t {pf['t']:.1f})" if pf else ""))
    L.append("  top cofitness: " + "; ".join(f"{c['hitid']} {c['desc']} ({c['cofit']:.2f})" for c in d["cofit_top15"][:6]))
L += ["", "## DUF7844 (PF25226) family (UniProtKB)"]
L.append(f"PF25226 members in UniProtKB: {fam['n_members']}; with Lnb_N PF13387: {fam['frac_with_PF13387_Lnb_N']*100:.1f}%; with annotated signal peptide: {fam['frac_with_signal']*100:.1f}%; with annotated TM segment: {fam['frac_with_any_TM']*100:.1f}%")
L.append("Phyla: " + "; ".join(f"{p} {n}" for p, n in fam["phyla"]) + f"; genera: {fam['n_genera']}")
ids = sorted(a["pct_id"] for a in fam["reps"])
L.append(f"Q88RI0 aligned to {fam['n_aligned_reps']} representatives (one per genus plus PA5464 and Smlt2198), {ids[0]}-{ids[-1]}% identity")
for k, v in fam["conservation"].items():
    L.append(f"  {k}: conserved in {v['frac_identical']*100:.0f}% of representatives")
for a in fam["reps"]:
    if a["acc"] in ("Q9HTA6", "B2FPQ3"):
        L.append(f"Q88RI0 vs {a['acc']} ({a['org']}): {a['pct_id']}% identity over {a['aligned']} aligned residues")
L.append(f"N-terminus: {fam['nterm']['first40']}; lipobox in signal-peptide cleavage region: {fam['nterm']['lipobox_LxxC_at_20_25']}")
open(os.path.join(out, "PP_0149_summary.txt"), "w").write("\n".join(L) + "\n")
print("\n".join(L))
