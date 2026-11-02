"""VC_1370 (Q9KS89) motif check: identity of dashboard sequence to UniProt, GGDEF
catalytic (A-site) motif, primary I-site RxxD, metal-binding residues, and hydrophobic
segments. Usage: analyze.py <uniprot.txt> <dashboard.fasta> <outdir>"""
import json, re, sys, os

def uniprot_seq(path):
    lines = open(path).read().split("\nSQ ")[1].split("\n")[1:]
    return "".join(l.strip().replace(" ", "") for l in lines if not l.startswith("//"))

def fasta_seq(path):
    return "".join(l.strip() for l in open(path) if not l.startswith(">"))

up = uniprot_seq(sys.argv[1]); db = fasta_seq(sys.argv[2]); out = sys.argv[3]
os.makedirs(out, exist_ok=True)
res = {"uniprot_len": len(up), "dashboard_len": len(db), "identical": up == db,
       "n_identical_positions": sum(a == b for a, b in zip(up, db))}

def find(pattern, start=0, end=None):
    s = up[start:end]
    return [{"pos": m.start() + 1 + start, "match": m.group(0)} for m in re.finditer(pattern, s)]

# GGDEF domain per UniProt FT (PROSITE PS50887) 300..433; Pfam 272..426
dom = (259, 437)
res["GGDEF_domain_used"] = list(dom)
res["A_site_GG(D/E)EF"] = find(r"[RK]?GG[DE]EF", *dom)
gg = find(r"GG[DE]EF", *dom)[0]["pos"]
# Primary I-site: RxxD located ~5 residues upstream of GG(D/E)EF (PleD R359xxD362 / G368GEEF)
win = up[gg - 13:gg - 1]
res["I_site_window_(GGDEF-12..GGDEF-1)"] = {"start": gg - 12, "seq": win}
res["I_site_RxxD"] = find(r"R..D", gg - 13, gg - 1)
res["I_site_spacing_D_to_first_G"] = (gg - res["I_site_RxxD"][0]["pos"] - 3) if res["I_site_RxxD"] else None
# Metal-coordinating Asp in beta1 'D[LIVM]D' (PleD D327 in 'DxD') and the GGDEF Asp/Glu
res["beta1_DxD_metal_site"] = find(r"D[LIVMF]D", dom[0], gg)
res["guanine_binding_N_in_'xxNxxxGHxxGD'"] = find(r"N...GH..GD", dom[0], gg)
# Kyte-Doolittle hydrophobic windows (19 aa, mean >= 1.6) as a crude TM check
kd = dict(A=1.8,R=-4.5,N=-3.5,D=-3.5,C=2.5,Q=-3.5,E=-3.5,G=-0.4,H=-3.2,I=4.5,L=3.8,K=-3.9,M=1.9,F=2.8,P=-1.6,S=-0.8,T=-0.7,W=-0.9,Y=-1.3,V=4.2)
w = 19; segs = []
for i in range(len(up) - w + 1):
    m = sum(kd[c] for c in up[i:i + w]) / w
    if m >= 1.6:
        if segs and i <= segs[-1][1]:
            segs[-1][1] = i + w
        else:
            segs.append([i + 1, i + w])
res["hydrophobic_segments_KD19_ge1.6"] = [{"start": a, "end": b, "seq": up[a - 1:b]} for a, b in segs]
json.dump(res, open(os.path.join(out, "results.json"), "w"), indent=1)
print(json.dumps(res, indent=1))
