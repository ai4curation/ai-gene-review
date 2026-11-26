# /// script
# requires-python = ">=3.11"
# dependencies = ["biopython>=1.83", "numpy", "pyyaml"]
# ///
"""Place GNRHR variants on the protein and compute structural context.

Inputs: data/ (written by 01_fetch_data.py) and variants_literature.yaml.
Outputs: results/*.tsv and results/summary.json. Nothing is hardcoded: every
number in RESULTS.md is read from these outputs. Missing inputs are reported,
not replaced.

Per residue of the canonical sequence (UniProt P30968):
  - UniProt topology and GPCRdb segment / generic (Ballesteros-Weinstein) number
  - 7BR3 (human, elagolix-bound, inactive): relative side-chain SASA of the receptor
    chain alone, heavy-atom neighbour count, min distance to the antagonist, whether
    the side chain points into the helical bundle or at the lipid
  - 9U4W (pig, GnRH- and Gq-bound, active), mapped to human numbering by sequence
    alignment: min distance to the GnRH peptide and to G-alpha-q
  - AlphaFold pLDDT
  - conservation across reviewed mammalian type I GnRH receptors
Variants: UniProt natural variants, the curated literature table, ClinVar, gnomAD v4.
"""
import collections
import csv
import json
import pathlib
import re
import sys

import numpy as np
import yaml
from Bio import SeqIO
from Bio.Align import PairwiseAligner, substitution_matrices
from Bio.PDB import MMCIFParser, NeighborSearch, ShrakeRupley
from Bio.PDB.Polypeptide import protein_letters_3to1

HERE = pathlib.Path(__file__).parent
DATA, OUT = HERE / "data", HERE / "results"
OUT.mkdir(exist_ok=True)
THREE = {k.capitalize(): v for k, v in protein_letters_3to1.items()}
# Tien et al. 2013 theoretical max ASA (A^2)
MAXASA = dict(A=129, R=274, N=195, D=193, C=167, Q=225, E=223, G=104, H=224, I=197, L=201, K=236,
              M=224, F=240, P=159, S=155, T=172, W=285, Y=263, V=174)

seq = str(next(SeqIO.parse(DATA / "P30968.fasta", "fasta")).seq)
N = len(seq)
summary = {"canonical_length": N}

# ---------------------------------------------------------------- annotation tracks
uni = json.load(open(DATA / "P30968.json"))
topo = [""] * (N + 1)
special = collections.defaultdict(list)
uniprot_variants = []
for f in uni["features"]:
    b, e = f["location"]["start"]["value"], f["location"]["end"]["value"]
    t = f["type"]
    if t in ("Topological domain", "Transmembrane"):
        for i in range(b, e + 1):
            topo[i] = f["description"] if t == "Topological domain" else "TM " + f["description"].split("Name=")[-1]
    elif t == "Glycosylation":
        special[b].append("N-glycosylation site")
    elif t == "Disulfide bond":
        special[b].append(f"disulfide C{b}-C{e}")
        special[e].append(f"disulfide C{b}-C{e}")
    elif t == "Natural variant" and b == e and f.get("alternativeSequence", {}).get("alternativeSequences"):
        uniprot_variants.append({"pos": b, "ref": f["alternativeSequence"]["originalSequence"],
                                 "alt": f["alternativeSequence"]["alternativeSequences"][0],
                                 "note": f.get("description", "")})
gp = {r["sequence_number"]: r for r in json.load(open(DATA / "gpcrdb_residues.json"))}
assert all(gp[i]["amino_acid"] == seq[i - 1] for i in range(1, N + 1)), "GPCRdb sequence differs from UniProt canonical"
bw = {i: (gp[i]["display_generic_number"] or "") for i in gp}
seg = {i: gp[i]["protein_segment"] for i in gp}
gen2pos = {v.split("x")[0]: k for k, v in bw.items() if v}
# class A landmarks located by generic number, never by a remembered residue number
MOTIFS = {"3.49": "D(R)S/DRY motif D3.49", "3.50": "DRS/DRY motif R3.50", "3.51": "DRS/DRY motif S3.51",
          "6.47": "CWxP motif C6.47", "6.48": "CWxP toggle W6.48", "6.50": "CWxP motif P6.50",
          "7.49": "N/DPxxY motif D7.49", "7.50": "N/DPxxY motif P7.50", "7.53": "N/DPxxY motif Y7.53",
          "2.50": "sodium-site position 2.50", "7.39": "ligand-contact position 7.39"}
for g, lab in MOTIFS.items():
    if g in gen2pos:
        special[gen2pos[g]].append(f"{lab} = {seq[gen2pos[g]-1]}{gen2pos[g]}")
summary["landmarks"] = {g: f"{seq[p-1]}{p}" for g, p in sorted(gen2pos.items()) if g in MOTIFS or g.endswith(".50")}

# ---------------------------------------------------------------- structures
aligner = PairwiseAligner()
aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
aligner.open_gap_score, aligner.extend_gap_score, aligner.mode = -11, -1, "local"
parser = MMCIFParser(QUIET=True)


def chain_seq(chain):
    res = [r for r in chain if r.id[0] == " " and r.get_resname().capitalize() in THREE]
    return res, "".join(THREE[r.get_resname().capitalize()] for r in res)


def map_chain(chain, min_id=0.6):
    """Map residues of a structure chain to canonical positions by local alignment.
    Returns {canonical_pos: residue} and (n_aligned, n_identical, mismatches)."""
    res, s = chain_seq(chain)
    best, mapping, mism, ident = None, {}, [], 0
    # a fusion construct aligns in several local blocks: iterate, masking what is used
    used_t = np.zeros(len(s), bool)
    masked = list(s)
    for _ in range(6):
        aln = aligner.align(seq, "".join(masked))
        if not len(aln) or aln[0].score < 40:
            break
        a = aln[0]
        for (qs, qe), (ts, te) in zip(*a.aligned):
            for q, t in zip(range(qs, qe), range(ts, te)):
                if q + 1 in mapping or used_t[t]:
                    continue
                mapping[q + 1] = res[t]
                used_t[t] = True
                if seq[q] == s[t]:
                    ident += 1
                else:
                    mism.append(f"{seq[q]}{q+1}{s[t]}")
                masked[t] = "X"
    return mapping, (len(mapping), ident, mism)


def receptor_chain(struct):
    best = None
    for ch in struct[0]:
        m, st = map_chain(ch)
        if best is None or st[1] > best[2][1]:
            best = (ch, m, st)
    return best


def min_dist(res, atoms):
    if not atoms:
        return None
    c = np.array([a.coord for a in atoms])
    return float(min(np.min(np.linalg.norm(c - a.coord, axis=1)) for a in res if a.element != "H"))


track = {i: {} for i in range(1, N + 1)}
# --- 7BR3 inactive human
st = parser.get_structure("7BR3", DATA / "7BR3.cif")
ch, m7, stat = receptor_chain(st)
summary["7BR3"] = {"chain": ch.id, "mapped": stat[0], "identical": stat[1], "construct_mismatches": stat[2],
                   "auth_numbering_equals_uniprot": sum(1 for p, r in m7.items() if r.id[1] == p),
                   "unmodelled": [i for i in range(1, N + 1) if i not in m7]}
hets = collections.Counter()
het_atoms = collections.defaultdict(list)
for r in st[0].get_residues():
    if r.id[0].startswith("H_"):
        hets[r.get_resname()] += len(r)
        het_atoms[r.get_resname()].extend(r.get_atoms())
# the drug is the het group closest to the transmembrane ligand pocket: choose the largest single
# non-lipid, non-PEG component and report all components so the choice is auditable
cc = {}
for line in open(DATA / "7BR3.cif"):
    mm = re.match(r"^(\w{3})\s+non-polymer\s+\.\s+(.+?)\s+\S+\s+'[^']*'\s+[\d.]+\s*$", line)
    if mm:
        cc[mm.group(1)] = mm.group(2).strip("'\" ")
summary["7BR3"]["het_components"] = {k: {"atoms": v, "name": cc.get(k, "?")} for k, v in hets.items()}
lig = next((k for k, n in cc.items() if "elagolix" in n.lower() or "ELAGOLIX" in n), None)
if lig is None:  # fall back to the het group buried deepest among receptor atoms
    rec_atoms = [a for r in m7.values() for a in r]
    ns_r = NeighborSearch(rec_atoms)
    lig = max(het_atoms, key=lambda k: np.mean([len(ns_r.search(a.coord, 6.0)) for a in het_atoms[k]]))
summary["7BR3"]["ligand_component"] = lig
lig_atoms = het_atoms[lig]
rec_res = list(m7.values())
sr = ShrakeRupley()
# SASA of the receptor residues only (fusion partner, ligand, lipids removed)
import copy
from Bio.PDB import Chain, Model, Structure
s2 = Structure.Structure("rec"); mod = Model.Model(0); c2 = Chain.Chain("A"); s2.add(mod); mod.add(c2)
for r in rec_res:
    c2.add(copy.deepcopy(r))
sr.compute(mod, level="A")
rec_atoms2 = [a for a in mod.get_atoms() if a.element != "H"]
ns = NeighborSearch(rec_atoms2)
ca = np.array([r["CA"].coord for r in c2 if "CA" in r and seg.get([p for p, rr in m7.items() if rr.id == r.id][0], "").startswith("TM")])
centre = ca.mean(axis=0)
# bundle axis = first principal component of TM CA atoms
axis = np.linalg.svd(ca - centre)[2][0]
id2pos = {r.id: p for p, r in m7.items()}
for r in c2:
    p = id2pos[r.id]
    aa = seq[p - 1]
    sc = [a for a in r if a.get_id() not in ("N", "C", "O", "CA")] or [r["CA"]]
    sasa_sc = sum(a.sasa for a in sc)
    sasa = sum(a.sasa for a in r)
    nb = {a.get_parent().id for x in sc for a in ns.search(x.coord, 4.5)} - {r.id}
    d = {"rsa_7BR3": round(sasa / MAXASA[aa], 2), "neighbours_4.5A": len(nb)}
    # radial orientation: is the side-chain centroid closer to the bundle axis than CA?
    def radial(x):
        v = x - centre
        return float(np.linalg.norm(v - np.dot(v, axis) * axis))
    if "CA" in r:
        scc = np.mean([a.coord for a in sc], axis=0)
        d["radial_CA"] = round(radial(r["CA"].coord), 1)
        d["sidechain_points"] = "in" if radial(scc) < radial(r["CA"].coord) - 0.5 else ("out" if radial(scc) > radial(r["CA"].coord) + 0.5 else "tangential")
    d["dist_antagonist_7BR3"] = round(min_dist(m7[p], lig_atoms), 1)
    track[p].update(d)

# --- 9U4W active pig GnRHR-GnRH-Gq
act = {}
for pid in ("9U4W",):
    f = DATA / f"{pid}.cif"
    if not f.exists():
        summary[pid] = "not downloaded"
        continue
    st = parser.get_structure(pid, f)
    ch, ma, stat = receptor_chain(st)
    # identify the peptide (shortest polymer chain) and G-alpha (chain with most contacts to receptor, excluding peptide)
    rec_at = [a for r in ma.values() for a in r]
    nsr = NeighborSearch(rec_at)
    info = {}
    for c in st[0]:
        if c.id == ch.id:
            continue
        res, s_ = chain_seq(c)
        if not res:
            continue
        ncont = sum(1 for r in res for a in r if nsr.search(a.coord, 4.5))
        info[c.id] = {"len": len(res), "contacts": ncont, "seq_start": s_[:12]}
    pep = min((c for c in info if info[c]["contacts"] > 0), key=lambda c: info[c]["len"])
    galpha = max((c for c in info if c != pep), key=lambda c: info[c]["contacts"])
    summary[pid] = {"receptor_chain": ch.id, "mapped": stat[0], "identical_to_human": stat[1],
                    "pig_vs_human_differences": stat[2], "peptide_chain": pep, "peptide_len": info[pep]["len"],
                    "galpha_chain": galpha, "partner_chains": info}
    pep_atoms = [a for a in st[0][pep].get_atoms()]
    ga_atoms = [a for a in st[0][galpha].get_atoms()]
    for p, r in ma.items():
        track[p]["dist_GnRH_9U4W"] = round(min_dist(r, pep_atoms), 1)
        track[p]["dist_Gq_9U4W"] = round(min_dist(r, ga_atoms), 1)
        track[p]["pig_residue"] = THREE[r.get_resname().capitalize()]
    # which GnRH residue is nearest
    for p, r in ma.items():
        if track[p]["dist_GnRH_9U4W"] <= 4.5:
            best = min(st[0][pep], key=lambda pr: min_dist(r, list(pr)))
            track[p]["nearest_GnRH_residue"] = f"{best.get_resname()}{best.id[1]}"

# --- AlphaFold
f = DATA / "AF-P30968.cif"
if f.exists():
    st = parser.get_structure("AF", f)
    af = {r.id[1]: r for r in st[0].get_residues()}
    def afd(p1, a1, p2, a2):
        return round(float(np.linalg.norm(af[p1][a1].coord - af[p2][a2].coord)), 2)
    # regions absent from the crystal structure: predicted geometry only, with the model confidence beside it
    summary["geometry_alphafold_predicted"] = {
        "C14_SG-C200_SG": afd(14, "SG", 200, "SG"), "C114_SG-C196_SG": afd(114, "SG", 196, "SG"),
        "K191_NZ_to_C14_SG": afd(191, "NZ", 14, "SG"), "K191_NZ_to_C200_SG": afd(191, "NZ", 200, "SG"),
        "plddt": {p: round(float(af[p]["CA"].get_bfactor()), 1) for p in (10, 14, 18, 191, 196, 200)}}
    for r in st[0].get_residues():
        if r.id[1] <= N and "CA" in r:
            assert THREE[r.get_resname().capitalize()] == seq[r.id[1] - 1]
            track[r.id[1]]["plddt"] = round(float(r["CA"].get_bfactor()), 1)
    summary["alphafold_mean_plddt"] = round(float(np.mean([track[i]["plddt"] for i in track])), 1)

# ---------------------------------------------------------------- conservation
gl = PairwiseAligner()
gl.substitution_matrix = substitution_matrices.load("BLOSUM62")
gl.open_gap_score, gl.extend_gap_score, gl.mode = -11, -1, "global"
orth = {}
for rec in SeqIO.parse(DATA / "gnrhr_reviewed.fasta", "fasta"):
    name = rec.id.split("|")[2]
    if "Fragment" in rec.description or name == "GNRHR_HUMAN":
        continue
    a = gl.align(seq, str(rec.seq))[0]
    col = {}
    for (qs, qe), (ts, te) in zip(*a.aligned):
        for q, t in zip(range(qs, qe), range(ts, te)):
            col[q + 1] = str(rec.seq)[t]
    ident = sum(1 for p, x in col.items() if x == seq[p - 1]) / N
    orth[name] = {"col": col, "identity": round(ident, 3), "len": len(rec.seq)}
summary["orthologs"] = {k: {"identity_to_human": v["identity"], "length": v["len"]} for k, v in orth.items()}
mamm = [k for k, v in orth.items() if v["identity"] >= 0.7]
summary["mammalian_set"] = mamm
for i in range(1, N + 1):
    col = [orth[k]["col"].get(i, "-") for k in mamm]
    track[i]["mammal_identical"] = f"{sum(1 for x in col if x == seq[i-1])}/{len(col)}"
    track[i]["mammal_column"] = "".join(col)
# the residue-191 indel: which orthologues lack it?
summary["position_191"] = {k: orth[k]["col"].get(191, "-") for k in orth}

# ---------------------------------------------------------------- variants
variants = {}


def add(pos, ref, alt, **kw):
    if not (1 <= pos <= N):
        return
    key = f"{ref}{pos}{alt}"
    v = variants.setdefault(key, {"pos": pos, "ref": ref, "alt": alt, "ref_matches_canonical": seq[pos - 1] == ref})
    for k, val in kw.items():
        if val not in (None, ""):
            v[k] = val


for v in uniprot_variants:
    add(v["pos"], v["ref"], v["alt"], uniprot_note=v["note"], in_uniprot_HH7="in HH7" in v["note"])
lit = yaml.safe_load(open(HERE / "variants_literature.yaml"))
for v in lit:
    mm = re.match(r"([A-Z])(\d+)([A-Z])$", v["variant"])
    add(int(mm.group(2)), mm.group(1), mm.group(3), lit_class=v["reported_class"],
        lit_mechanism=v.get("reported_mechanism"), lit_pmid=v["pmid"], lit_mechanism_pmid=v.get("mechanism_pmid"))
bad = [k for k, v in variants.items() if not v["ref_matches_canonical"]]
if bad:
    sys.exit(f"reference residue does not match canonical sequence for: {bad}")

# ClinVar
cv = json.load(open(DATA / "clinvar_summaries.json"))
cv_rows = []
for u, r in cv.items():
    title = r["title"]
    cls = r["germline_classification"]["description"]
    rs = r["germline_classification"]["review_status"]
    mm = re.search(r"\(p\.([A-Z][a-z]{2})(\d+)([A-Z][a-z]{2}|Ter|fs|del|=)", title)
    kind, pos = "other", None
    if r["obj_type"].startswith("copy number") or "GNRHR" not in title.split(":")[0]:
        kind = "CNV/multigene"
    elif mm:
        pos = int(mm.group(2))
        ref = THREE.get(mm.group(1))
        if mm.group(3) in THREE:
            kind = "missense"
            add(pos, ref, THREE[mm.group(3)], clinvar=cls, clinvar_review=rs, clinvar_id=r["accession"])
        elif mm.group(3) == "Ter":
            kind = "nonsense"
        elif mm.group(3) == "fs":
            kind = "frameshift"
        elif mm.group(3) == "=":
            kind = "synonymous"
        else:
            kind = "inframe"
        if ref and seq[pos - 1] != ref:
            kind += " (REF MISMATCH)"
    elif re.search(r"c\.\d+[+-]\d+", title):
        kind = "intronic/splice"
    cv_rows.append({"accession": r["accession"], "title": title, "kind": kind, "pos": pos, "classification": cls, "review_status": rs})
with open(OUT / "clinvar_gnrhr.tsv", "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(cv_rows[0]), delimiter="\t"); w.writeheader(); w.writerows(cv_rows)
plp = lambda c: c.lower().startswith(("pathogenic", "likely pathogenic"))
tab = collections.Counter((r["kind"], "P/LP" if plp(r["classification"]) else r["classification"] or "none") for r in cv_rows)
summary["clinvar"] = {"n_records": len(cv_rows), "by_kind_and_class": {f"{k[0]} | {k[1]}": n for k, n in sorted(tab.items())},
                      "ref_mismatches": [r["title"] for r in cv_rows if "MISMATCH" in r["kind"]]}

# gnomAD
gn = json.load(open(DATA / "gnomad.json"))["data"]["gene"]
summary["gnomad_constraint"] = gn["gnomad_constraint"]
summary["gnomad_canonical_transcript"] = gn["canonical_transcript_id"]
LOF = {"stop_gained", "frameshift_variant", "splice_donor_variant", "splice_acceptor_variant"}
lof_ac = lof_an = 0
lof_list, mis_n, hom_rows = [], 0, []
other_tx = collections.Counter(v["transcript_id"] for v in gn["variants"] if v["transcript_id"] != gn["canonical_transcript_id"])
summary["gnomad_variants_on_other_transcripts_skipped"] = dict(other_tx)
for v in gn["variants"]:
    if v["transcript_id"] != gn["canonical_transcript_id"]:
        continue  # protein consequence is not on the canonical (isoform 1) reading frame
    ac = sum((v[k] or {}).get("ac", 0) for k in ("exome", "genome"))
    an = max((v[k] or {}).get("an", 0) for k in ("exome", "genome"))
    an_sum = sum((v[k] or {}).get("an", 0) for k in ("exome", "genome"))
    hom = sum((v[k] or {}).get("homozygote_count", 0) for k in ("exome", "genome"))
    af = ac / an_sum if an_sum else 0
    if v["consequence"] in LOF and ac and v.get("lof") in ("HC", None):
        lof_list.append({"variant": v["variant_id"], "hgvsp": v["hgvsp"] or v["hgvsc"], "consequence": v["consequence"], "ac": ac, "af": af, "hom": hom, "loftee": v.get("lof")})
    mm = re.match(r"p\.([A-Z][a-z]{2})(\d+)([A-Z][a-z]{2})$", v["hgvsp"] or "")
    if v["consequence"] == "missense_variant" and mm and ac:
        mis_n += 1
        add(int(mm.group(2)), THREE[mm.group(1)], THREE[mm.group(3)], gnomad_ac=ac, gnomad_af=af, gnomad_hom=hom)
    if hom:
        hom_rows.append({"hgvsp": v["hgvsp"] or v["hgvsc"], "consequence": v["consequence"], "ac": ac, "af": round(af, 6), "hom": hom})
lof_list.sort(key=lambda x: -x["ac"])
# Hardy-Weinberg expectation for the alleles that have homozygotes: is homozygosity depleted?
hwe = []
for v in gn["variants"]:
    if v["transcript_id"] != gn["canonical_transcript_id"] or v["consequence"] != "missense_variant":
        continue
    for ds in ("exome", "genome"):
        d = v[ds]
        if d and d["an"] and d["ac"] / d["an"] >= 5e-4:
            q = d["ac"] / d["an"]
            hwe.append({"hgvsp": v["hgvsp"], "dataset": ds, "ac": d["ac"], "an": d["an"], "af": round(q, 5),
                        "homozygotes_observed": d["homozygote_count"], "homozygotes_expected_HWE": round(q * q * d["an"] / 2, 1)})
summary["gnomad_hwe_common_missense"] = hwe
summary["gnomad"] = {"n_missense_observed": mis_n, "n_pLoF_variants": len(lof_list),
                     "pLoF_cumulative_AF": sum(x["af"] for x in lof_list), "pLoF_homozygotes": sum(x["hom"] for x in lof_list),
                     "top_pLoF": lof_list[:8], "variants_with_homozygotes": sorted(hom_rows, key=lambda x: -x["af"])[:15]}
bad = [k for k, v in variants.items() if not v["ref_matches_canonical"]]
summary["variants_ref_mismatch_dropped"] = bad
for k in bad:
    variants.pop(k)

# ---------------------------------------------------------------- per-variant structural reasoning (rule-based, computed)
CHARGED, AROM, SMALL = set("DEKR"), set("FWY"), set("GAS")
VOL = dict(G=60, A=89, S=89, C=109, D=111, P=113, N=114, T=116, E=138, V=140, Q=144, H=153, M=163, I=167, L=167, K=169, R=174, F=190, Y=194, W=228)


def reason(v):
    p, ref, alt = v["pos"], v["ref"], v["alt"]
    t = track[p]
    out = []
    for s in special.get(p, []):
        out.append(s)
    if alt == "C" or ref == "C":
        out.append("gains a free cysteine" if alt == "C" else "loses a cysteine")
    if ref == "P":
        out.append("loss of proline")
    if alt == "P" and seg[p].startswith("TM"):
        out.append("proline introduced into a helix")
    if ref == "G":
        out.append("loss of glycine")
    buried = t.get("rsa_7BR3") is not None and t["rsa_7BR3"] <= 0.25
    inward = t.get("sidechain_points") == "in"
    if seg[p].startswith("TM") and buried and alt in CHARGED and ref not in CHARGED:
        out.append("charge introduced at a buried transmembrane position")
    if seg[p].startswith("TM") and buried and ref in CHARGED and (alt not in CHARGED or (ref in "DE") != (alt in "DE")):
        out.append("buried transmembrane charge lost or reversed")
    if buried and VOL[alt] - VOL[ref] >= 25:
        out.append(f"larger side chain (+{VOL[alt]-VOL[ref]} A^3) at a buried position with {t.get('neighbours_4.5A')} neighbours")
    if buried and VOL[ref] - VOL[alt] >= 40:
        out.append(f"cavity-forming truncation (-{VOL[ref]-VOL[alt]} A^3) at a buried position")
    if t.get("dist_GnRH_9U4W") is not None and t["dist_GnRH_9U4W"] <= 4.5:
        out.append(f"contacts GnRH in the active complex ({t['dist_GnRH_9U4W']} A, nearest {t.get('nearest_GnRH_residue')})")
    if t.get("dist_Gq_9U4W") is not None and t["dist_Gq_9U4W"] <= 4.5:
        out.append(f"contacts G-alpha-q in the active complex ({t['dist_Gq_9U4W']} A)")
    if t.get("dist_antagonist_7BR3") is not None and t["dist_antagonist_7BR3"] <= 4.5:
        out.append(f"lines the elagolix pocket ({t['dist_antagonist_7BR3']} A)")
    if not out:
        if t.get("rsa_7BR3") is None:
            out.append("residue not modelled in 7BR3; no structural call")
        elif seg[p].startswith("TM") and not buried and t.get("sidechain_points") == "out":
            out.append("lipid-facing transmembrane position; no structural mechanism evident")
        else:
            out.append("no rule fired")
    # coarse class
    txt = "; ".join(out)
    if "contacts GnRH" in txt:
        cls = "ligand-binding surface"
    elif "contacts G-alpha-q" in txt or "DRS" in txt or "N/DPxxY" in txt:
        cls = "activation switch / G-protein interface"
    elif "disulfide" in txt or "glycosylation" in txt or ("cysteine" in txt and not seg[p].startswith("TM")):
        cls = "extracellular fold (disulfide/glycan)"
    elif buried and seg[p].startswith("TM"):
        cls = "transmembrane core packing"
    elif buried:
        cls = "buried loop/terminus packing"
    else:
        cls = "surface / unresolved"
    return cls, txt


rows = []
for k, v in sorted(variants.items(), key=lambda kv: (kv[1]["pos"], kv[1]["alt"])):
    p = v["pos"]
    t = track[p]
    cls, txt = reason(v)
    rows.append({"variant": k, "pos": p, "uniprot_topology": topo[p], "gpcrdb_segment": seg[p], "generic_number": bw[p],
                 "in_uniprot_HH7": v.get("in_uniprot_HH7", ""), "lit_class": v.get("lit_class", ""),
                 "lit_mechanism": v.get("lit_mechanism", ""), "lit_pmid": v.get("lit_pmid", ""),
                 "lit_mechanism_pmid": v.get("lit_mechanism_pmid", ""),
                 "clinvar": v.get("clinvar", ""), "clinvar_review": v.get("clinvar_review", ""),
                 "gnomad_ac": v.get("gnomad_ac", ""), "gnomad_af": f"{v['gnomad_af']:.2e}" if "gnomad_af" in v else "",
                 "gnomad_hom": v.get("gnomad_hom", ""),
                 "rsa_7BR3": t.get("rsa_7BR3", ""), "neighbours": t.get("neighbours_4.5A", ""), "sidechain_points": t.get("sidechain_points", ""),
                 "dist_antagonist_7BR3": t.get("dist_antagonist_7BR3", ""), "dist_GnRH_9U4W": t.get("dist_GnRH_9U4W", ""),
                 "dist_Gq_9U4W": t.get("dist_Gq_9U4W", ""), "plddt": t.get("plddt", ""),
                 "mammal_identical": t.get("mammal_identical", ""), "mammal_column": t.get("mammal_column", ""),
                 "structural_class": cls, "structural_reasoning": txt})
with open(OUT / "variant_structure_table.tsv", "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0]), delimiter="\t"); w.writeheader(); w.writerows(rows)
with open(OUT / "residue_tracks.tsv", "w", newline="") as fh:
    cols = ["pos", "aa", "uniprot_topology", "gpcrdb_segment", "generic_number", "special"] + sorted({k for t in track.values() for k in t})
    w = csv.DictWriter(fh, fieldnames=cols, delimiter="\t"); w.writeheader()
    for i in range(1, N + 1):
        w.writerow({"pos": i, "aa": seq[i - 1], "uniprot_topology": topo[i], "gpcrdb_segment": seg[i], "generic_number": bw[i],
                    "special": "; ".join(special.get(i, [])), **track[i]})

# ---------------------------------------------------------------- aggregate tests
disease = [r for r in rows if r["in_uniprot_HH7"] or r["lit_class"] or plp(r["clinvar"])]
popn = [r for r in rows if r["gnomad_ac"] and not (r["in_uniprot_HH7"] or r["lit_class"] or plp(r["clinvar"]))]


def frac(rs, pred):
    rs = [r for r in rs if r["rsa_7BR3"] != ""]
    return [sum(1 for r in rs if pred(r)), len(rs)]


summary["sets"] = {"disease_missense": len(disease), "gnomad_only_missense": len(popn)}
summary["burial_comparison"] = {
    "disease_buried_rsa<=0.25": frac(disease, lambda r: r["rsa_7BR3"] <= 0.25),
    "gnomad_only_buried_rsa<=0.25": frac(popn, lambda r: r["rsa_7BR3"] <= 0.25),
    "all_modelled_residues_buried": [sum(1 for i in track if track[i].get("rsa_7BR3", 9) <= 0.25), sum(1 for i in track if "rsa_7BR3" in track[i])]}
# Fisher exact, computed without scipy
from math import comb


def fisher(a, b, c, d):
    n = a + b + c + d
    p0 = comb(a + b, a) * comb(c + d, c) / comb(n, a + c)
    tot = 0
    for x in range(max(0, a + c - (c + d)), min(a + b, a + c) + 1):
        px = comb(a + b, x) * comb(c + d, a + c - x) / comb(n, a + c)
        if px <= p0 * (1 + 1e-9):
            tot += px
    return tot


a, n1 = summary["burial_comparison"]["disease_buried_rsa<=0.25"]
c, n2 = summary["burial_comparison"]["gnomad_only_buried_rsa<=0.25"]
summary["burial_comparison"]["fisher_p_disease_vs_gnomad"] = fisher(a, n1 - a, c, n2 - c)
summary["disease_by_structural_class"] = dict(collections.Counter(r["structural_class"] for r in disease))
summary["disease_by_segment"] = dict(collections.Counter(re.sub(r"\d", "", r["gpcrdb_segment"]) if not r["gpcrdb_segment"].startswith("TM") else "TM" for r in disease))
summary["disease_conserved_all_mammals"] = [sum(1 for r in disease if r["mammal_identical"].split("/")[0] == r["mammal_identical"].split("/")[1]), len(disease)]
summary["gnomad_only_conserved_all_mammals"] = [sum(1 for r in popn if r["mammal_identical"].split("/")[0] == r["mammal_identical"].split("/")[1]), len(popn)]
tot_cons = sum(1 for i in track if track[i]["mammal_identical"].split("/")[0] == track[i]["mammal_identical"].split("/")[1])
summary["all_positions_conserved_all_mammals"] = [tot_cons, N]
# contact lists
summary["GnRH_contact_residues_9U4W_human_numbering"] = [f"{seq[i-1]}{i}({bw[i].split('x')[0]}):{track[i]['dist_GnRH_9U4W']}" for i in track if track[i].get("dist_GnRH_9U4W", 99) <= 4.0]
summary["Gq_contact_residues_9U4W_human_numbering"] = [f"{seq[i-1]}{i}({bw[i].split('x')[0] or seg[i]}):{track[i]['dist_Gq_9U4W']}" for i in track if track[i].get("dist_Gq_9U4W", 99) <= 4.0]
summary["antagonist_contact_residues_7BR3"] = [f"{seq[i-1]}{i}({bw[i].split('x')[0] or seg[i]}):{track[i]['dist_antagonist_7BR3']}" for i in track if track[i].get("dist_antagonist_7BR3", 99) <= 4.0]
# specific geometry checks used in the reviews
def atom_d(m, p1, a1, p2, a2):
    try:
        return round(float(np.linalg.norm(m[p1][a1].coord - m[p2][a2].coord)), 2)
    except KeyError:
        return None
summary["geometry_7BR3"] = {
    "C14_SG-C200_SG": atom_d(m7, 14, "SG", 200, "SG"), "C114_SG-C196_SG": atom_d(m7, 114, "SG", 196, "SG"),
    "E90_carboxylate_to_K121_NZ": min(filter(None, [atom_d(m7, 90, "OE1", 121, "NZ"), atom_d(m7, 90, "OE2", 121, "NZ")]), default=None),
    "E90_carboxylate_to_S124_OG": min(filter(None, [atom_d(m7, 90, "OE1", 124, "OG"), atom_d(m7, 90, "OE2", 124, "OG")]), default=None),
    "E90_carboxylate_to_W280_NE1": min(filter(None, [atom_d(m7, 90, "OE1", 280, "NE1"), atom_d(m7, 90, "OE2", 280, "NE1")]), default=None),
    "D98_carboxylate_to_K121_NZ": min(filter(None, [atom_d(m7, 98, "OD1", 121, "NZ"), atom_d(m7, 98, "OD2", 121, "NZ")]), default=None),
    "A171_CB_to_Y119_OH": atom_d(m7, 171, "CB", 119, "OH"),
    "K191_NZ_to_C14_SG": atom_d(m7, 191, "NZ", 14, "SG"), "K191_NZ_to_C200_SG": atom_d(m7, 191, "NZ", 200, "SG"),
    "last_residue_modelled": max(m7), "C_terminal_residue": f"{seq[-1]}{N}"}
json.dump(summary, open(OUT / "summary.json", "w"), indent=1, default=str)
print(json.dumps(summary, indent=1, default=str)[:6000])
