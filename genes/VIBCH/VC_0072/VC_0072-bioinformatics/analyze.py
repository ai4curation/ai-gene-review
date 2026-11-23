"""VC_0072 (Q9KVR7) motif check: GGDEF and EAL catalytic motifs, I-site, and
dashboard-vs-UniProt start comparison. Usage: analyze.py <uniprot.txt> <dashboard.fasta> <outdir>"""
import json, re, sys, os, difflib

def uniprot_seq(path):
    lines = open(path).read().split("\nSQ ")[1].split("\n")[1:]
    return "".join(l.strip().replace(" ", "") for l in lines if not l.startswith("//"))

def fasta_seq(path):
    return "".join(l.strip() for l in open(path) if not l.startswith(">"))

up = uniprot_seq(sys.argv[1]); db = fasta_seq(sys.argv[2]); out = sys.argv[3]
os.makedirs(out, exist_ok=True)
res = {"uniprot_len": len(up), "dashboard_len": len(db)}

# N-terminal comparison: locate UniProt residues 2.. in dashboard
off = db.find(up[1:20])
res["dashboard_nterm_extension"] = db[:off]
res["uniprot_met1_aligns_to_dashboard_pos"] = off  # 1-based pos of residue preceding up[1]
sm = difflib.SequenceMatcher(None, db[off:], up[1:], autojunk=False)
subs = []
for tag, i1, i2, j1, j2 in sm.get_opcodes():
    if tag != "equal":
        subs.append({"tag": tag, "dashboard": db[off+i1:off+i2], "dashboard_pos": off+i1+1,
                     "uniprot": up[1+j1:1+j2], "uniprot_pos": j1+2})
res["differences_after_alignment"] = subs

def find(pattern, seq=up):
    return [{"pos": m.start()+1, "match": m.group(0)} for m in re.finditer(pattern, seq)]

# GGDEF domain (UniProt 368-501): catalytic GG(D/E)EF A-site
res["GGDEF_motif_GGDEF_or_GGEEF"] = find(r"GG[DE]EF")
# I-site RxxD: in PleD it sits 5 residues upstream of the GG(D/E)EF motif (RxxD-x5-GGDEF)
gg = res["GGDEF_motif_GGDEF_or_GGEEF"][0]["pos"]
res["I_site_window_(GGDEF-9..GGDEF-1)"] = up[gg-10:gg-1]
res["I_site_RxxD_in_window"] = bool(re.search(r"R..D", up[gg-12:gg-1]))
res["RxxD_anywhere_in_GGDEF_domain_368_501"] = [dict(d, pos=d["pos"]+367) for d in find(r"R..D", up[367:501])]
# Metal-binding D in 'DxLD' (beta1, ~ 30 aa upstream of GGDEF) and 'GHxxGD'
res["GGDEF_beta1_D[LI]D_metal_site"] = [dict(d, pos=d["pos"]+367) for d in find(r"D[LI]D", up[367:430])]
res["GGDEF_HxxGD"] = [dict(d, pos=d["pos"]+367) for d in find(r"H..GD", up[367:430])]
# EAL domain (UniProt 512-767)
eal = up[511:767]
res["EAL_ExLxR_(E-A/V-L-x-R)"] = [dict(d, pos=d["pos"]+511) for d in find(r"E[AVI]L.R", eal)]
res["EAL_DDFGTG_loop6"] = [dict(d, pos=d["pos"]+511) for d in find(r"DDFG.G", eal)]
res["EAL_N-loop_N"] = [dict(d, pos=d["pos"]+511) for d in find(r"[IVL]N[LIVM][SA]", eal)]
res["EAL_KxD_(K316-like)"] = [dict(d, pos=d["pos"]+511) for d in find(r"K[IVL]D", eal)]
res["EAL_E352-like_(ExxE/EGVE)"] = [dict(d, pos=d["pos"]+511) for d in find(r"E[GF]VE", eal)]
res["EAL_E265-like_(ExxE in 'FEITE')"] = [dict(d, pos=d["pos"]+511) for d in find(r"E[IL]TE", eal)]
json.dump(res, open(os.path.join(out, "results.json"), "w"), indent=1)
print(json.dumps(res, indent=1))
