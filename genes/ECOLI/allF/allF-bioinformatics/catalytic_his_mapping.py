# /// script
# requires-python = ">=3.11"
# dependencies = ["biopython>=1.84", "numpy", "pyhmmer==0.12.3", "pyyaml", "tmtools==0.3.0"]
# ///
"""Where is the succinyl-CoA synthetase (SCS) alpha catalytic histidine in AllF?

Five analyses, all on data fetched at run time (UniProt REST, InterPro API,
RCSB PDB). No result is hardcoded. The fixed inputs are the accessions, PDB
ids, domain windows, report windows and residues of interest named in
PARAMETERS below; the catalytic histidine position is read from the UniProt
ACT_SITE feature of SucD.

1. sequence: literal residues and histidine positions.
2. profile: the Pfam PF00549 (CoA-ligase) match column that holds the SucD
   catalytic His, read for AllF and its paralogs (pyhmmer hmmsearch).
3. structure: TM-align (tmtools) of the SucD C-terminal domain onto the two
   SCS-like lobes of the AllF crystal structure 3DMY; which AllF residue, if
   any, superposes on the catalytic His; the power-helix N-termini; the
   alpha-C/beta-C pair against the 3DMY dimer; a rigid transplant of CoA.
4. family: the same profile column over every UniProtKB member of InterPro
   IPR061301 (AllF family) and every reviewed member of IPR005810 (SCS alpha).
5. counts of UniProtKB entries that carry the AllG domain (PF06545) in one
   chain with an AllF or AllH domain.

Usage:  uv run catalytic_his_mapping.py [--skip-family] > results.yaml
"""
import collections
import gzip
import io
import re
import statistics
import sys
import time
import urllib.parse
import urllib.request

import numpy as np
import pyhmmer
import yaml
from Bio.PDB import NeighborSearch, PDBParser
from Bio.SeqUtils import seq1
from tmtools import tm_align

PARAMETERS = {
    "sucd": "P0AGE9",
    "allf": "Q47208",
    "paralogs": {"P77187": "E. coli YahF", "Q8ZR75": "Salmonella Typhimurium FdrA"},
    "pfam": "PF00549",
    "allf_structure": "3DMY",
    "scs_structures": ["2SCU", "1CQI", "1JKJ"],  # chain A = SucD, chain B = SucC
    # AllF windows (UniProt numbering = 3DMY author numbering, checked below)
    "allf_lobe1": [174, 299],
    "allf_lobe2": [300, 502],
    "allf_rossmann_permuted": [[503, 555], [101, 190]],
    # SucD windows, UniProt P0AGE9 numbering
    "sucd_n_domain": [2, 123],
    "sucd_c_domain": [124, 289],
    # SucC C-terminal domain, PDB chain B numbering
    "succ_c_domain_pdb": [239, 385],
    "allf_residues_of_interest": [293, 389, 467],
    # report windows (inputs, not results)
    "allf_report_segments": [[286, 300], [383, 392], [462, 476]],
    "allf_lobe2_pairing_window": [462, 476],
    # N-terminus of the phosphate-binding (power) helix: SucD, UniProt numbering, and AllF lobe 2
    "sucd_power_helix_nterm": [153, 156],
    "allf_lobe2_power_helix_nterm": [338, 341],
    "allf_insert_his": 389,
    "family_queries": {
        "allf_family_IPR061301": "xref:interpro-IPR061301",
        "scs_alpha_reviewed_IPR005810": "(xref:interpro-IPR005810) AND (reviewed:true)",
    },
    "insert_motif": "G[KR]PHPM",
    # UniProtKB entries carrying the AllG domain (PF06545) together with an AllF or AllH domain
    "fusion_queries": {
        "PF06545_AllG": "xref:pfam-PF06545",
        "PF06545_AllG_and_PF02629_CoA_binding": "(xref:pfam-PF06545) AND (xref:pfam-PF02629)",
        "PF06545_AllG_and_PF00549_CoA_ligase": "(xref:pfam-PF06545) AND (xref:pfam-PF00549)",
        "PF06545_AllG_and_PF27530_AllF_HMA": "(xref:pfam-PF06545) AND (xref:pfam-PF27530)",
        "PF06545_AllG_and_PF11392_AllH": "(xref:pfam-PF06545) AND (xref:pfam-PF11392)",
    },
}
P = PARAMETERS


def fetch(url, binary=False, tries=4):
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "python-urllib"})
            with urllib.request.urlopen(req, timeout=180) as r:
                data = r.read()
                return (data if binary else data.decode()), dict(r.headers)
        except Exception as e:  # noqa: BLE001
            err = e
            time.sleep(5 * (i + 1))
    raise RuntimeError(f"could not fetch {url}: {err}")


def parse_fasta(txt):
    out, name = {}, None
    for line in txt.splitlines():
        if line.startswith(">"):
            name = line[1:].split()[0]
            out[name] = []
        elif name:
            out[name].append(line.strip())
    return {k: "".join(v) for k, v in out.items()}


def uniprot_seq(acc):
    return next(iter(parse_fasta(fetch(f"https://rest.uniprot.org/uniprotkb/{acc}.fasta")[0]).values()))


# ---------------------------------------------------------------- profile
ABC = pyhmmer.easel.Alphabet.amino()


def load_hmm(pfam):
    raw, _ = fetch(f"https://www.ebi.ac.uk/interpro/wwwapi/entry/pfam/{pfam}?annotation=hmm", binary=True)
    if raw[:2] == b"\x1f\x8b":
        raw = gzip.decompress(raw)
    with pyhmmer.plan7.HMMFile(io.BytesIO(raw)) as f:
        return f.read()


def column_maps(hmm, seqs):
    """name -> best-scoring domain: score, range, {match column: (position, residue)},
    {position: 'insert after column N'}."""
    block = pyhmmer.easel.DigitalSequenceBlock(
        ABC, [pyhmmer.easel.TextSequence(name=k.encode(), sequence=v).digitize(ABC) for k, v in seqs.items()])
    best = {}
    for hits in pyhmmer.hmmsearch(hmm, block, E=1e-3, domE=1, incdomE=1):
        for h in hits:
            name = h.name.decode() if isinstance(h.name, bytes) else h.name
            for d in h.domains:
                al = d.alignment
                cols, ins, hp, sp = {}, {}, al.hmm_from, al.target_from
                for hc, tc in zip(al.hmm_sequence, al.target_sequence):
                    if hc != "." and tc != "-":
                        cols[hp] = (sp, tc.upper())
                    elif hc == "." and tc != "-":
                        ins[sp] = hp - 1
                    if hc != ".":
                        hp += 1
                    if tc != "-":
                        sp += 1
                rec = {"score": round(d.score, 1), "from": al.target_from, "to": al.target_to,
                       "cols": cols, "ins": ins}
                if name not in best or rec["score"] > best[name]["score"]:
                    best[name] = rec
    return best


# -------------------------------------------------------------- structure
PARSER = PDBParser(QUIET=True)
NONSTD = {"MSE": "M", "NEP": "H"}


def structure(pdb):
    txt, _ = fetch(f"https://files.rcsb.org/download/{pdb}.pdb")
    return PARSER.get_structure(pdb, io.StringIO(txt))


def one(r):
    return NONSTD.get(r.get_resname()) or seq1(r.get_resname())


def chain(s, ch, lo=-99, hi=9999):
    return [r for r in s[0][ch]
            if "CA" in r and (r.id[0] == " " or r.get_resname() in NONSTD) and lo <= r.id[1] <= hi]


def ca(res):
    return np.array([r["CA"].coord for r in res], float)


def tf(a, xyz):
    return (a.u @ np.asarray(xyz, float).T).T + a.t


def align(mob, tgt):
    """TM-align mobile CA trace onto target; return alignment and
    {index in mob: (target residue, CA-CA distance after superposition)}."""
    a = tm_align(ca(mob), ca(tgt), "".join(map(one, mob)), "".join(map(one, tgt)))
    x, y, pairs, i, j = tf(a, ca(mob)), ca(tgt), {}, 0, 0
    for c1, c2 in zip(a.seqxA, a.seqyA):
        if c1 != "-" and c2 != "-":
            pairs[i] = (tgt[j], float(np.linalg.norm(x[i] - y[j])))
        i += c1 != "-"
        j += c2 != "-"
    return a, pairs


def fit_stats(a, pairs, mob):
    d = np.array([v[1] for v in pairs.values()])
    return {"tm_normalised_by_mobile": round(float(a.tm_norm_chain1), 2),
            "tm_normalised_by_target": round(float(a.tm_norm_chain2), 2),
            "rmsd": round(float(a.rmsd), 1), "aligned": len(pairs), "within_5A": int((d < 5).sum()),
            "identical_within_5A": sum(one(mob[i]) == one(v[0]) for i, v in pairs.items() if v[1] < 5)}


def numbering_offset(res, seq):
    """Offset to add to the PDB residue number to get the UniProt position."""
    score = {o: sum(1 for r in res if 0 < r.id[1] + o <= len(seq) and seq[r.id[1] + o - 1] == one(r))
             for o in (-1, 0, 1)}
    off = max(score, key=score.get)
    return off, score[off], len(res)


def tag(r, off=0):
    return f"{one(r)}{r.id[1] + off}"


def main():
    skip_family = "--skip-family" in sys.argv
    out = {"parameters": PARAMETERS}

    # ---- 1. sequences
    seqs = {acc: uniprot_seq(acc) for acc in [P["sucd"], P["allf"], *P["paralogs"]]}
    sucd, allf = seqs[P["sucd"]], seqs[P["allf"]]
    flat, _ = fetch(f"https://rest.uniprot.org/uniprotkb/{P['sucd']}.txt")
    act = [int(x) for x in re.findall(r"^FT   ACT_SITE\s+(\d+)", flat, re.M)]
    if len(act) != 1 or sucd[act[0] - 1] != "H":
        raise RuntimeError(f"expected one histidine ACT_SITE on SucD, got {act}")
    his = act[0]
    out["sequence"] = {
        "lengths": {k: len(v) for k, v in seqs.items()},
        "sucd_catalytic_his_from_uniprot_act_site": his,
        "sucd_context": {f"{his - 3}-{his + 5}": sucd[his - 4:his + 5]},
        "allf_segments": {f"{a}-{b}": allf[a - 1:b] for a, b in P["allf_report_segments"]},
        "allf_residues_of_interest": {n: allf[n - 1] for n in P["allf_residues_of_interest"]},
        "histidine_positions": {k: [i + 1 for i, c in enumerate(v) if c == "H"] for k, v in seqs.items()},
    }

    # ---- 2. profile column of the catalytic His
    hmm = load_hmm(P["pfam"])
    maps = column_maps(hmm, seqs)
    col = [c for c, (p, _) in maps[P["sucd"]]["cols"].items() if p == his]
    if len(col) != 1:
        raise RuntimeError("SucD catalytic His is not on a match column of the profile")
    col = col[0]
    prof = {"hmm": f"{hmm.name if isinstance(hmm.name, str) else hmm.name.decode()} ({hmm.accession if isinstance(hmm.accession, str) else hmm.accession.decode()}), {hmm.M} match columns",
            "column_of_sucd_catalytic_his": col, "per_protein": {}}
    for acc, m in maps.items():
        win = "".join(m["cols"].get(c, (None, "-"))[1] for c in range(col - 6, col + 7))
        pos, res = m["cols"].get(col, (None, "-"))
        prof["per_protein"][acc] = {"domain": f"{m['from']}-{m['to']}", "bit_score": m["score"],
                                    "residue_at_column": f"{res}{pos}",
                                    f"window_columns_{col - 6}_{col + 6}": win}
    prof["allf_residues_of_interest"] = {}
    inv = {p: c for c, (p, _) in maps[P["allf"]]["cols"].items()}
    for n in P["allf_residues_of_interest"]:
        m = maps[P["allf"]]
        if n in inv:
            state = f"match column {inv[n]}"
        elif n in m["ins"]:
            state = f"insert after match column {m['ins'][n]}"
        else:
            state = f"outside the {P['pfam']} domain ({m['from']}-{m['to']})"
        prof["allf_residues_of_interest"][f"{allf[n - 1]}{n}"] = state
    out["profile"] = prof

    # ---- 3. structure
    s3 = structure(P["allf_structure"])
    A, B = chain(s3, "A"), chain(s3, "B")
    off3, ok3, n3 = numbering_offset(A, allf)
    if off3 != 0:
        raise RuntimeError("3DMY numbering is not UniProt numbering")
    lobe = {1: P["allf_lobe1"], 2: P["allf_lobe2"]}
    sel = lambda ch, w: [r for r in ch if w[0] <= r.id[1] <= w[1]]  # noqa: E731
    byno = lambda ch, n: next(r for r in ch if r.id[1] == n)  # noqa: E731
    heavy = [at for ch in s3[0] for r in ch for at in r if r.id[0] != "W"]
    ns = NeighborSearch(heavy)
    at_label = lambda at: f"{at.get_parent().get_parent().id}:{at.get_parent().get_resname()}{at.get_parent().id[1]}:{at.get_id()}"  # noqa: E731
    st = {"allf_structure": {"pdb": P["allf_structure"], "chain_A_ordered_residues": n3,
                             "identical_to_uniprot_at_same_number": ok3,
                             "first_and_last_ordered_residue": [A[0].id[1], A[-1].id[1]]},
          "per_scs_structure": {}}
    # insert histidine against the lobe 2 power-helix N-terminus, within each chain of 3DMY (no superposition)
    side = lambda r: [at for at in r if at.get_id() not in ("N", "CA", "C", "O")]  # noqa: E731
    hw = P["allf_lobe2_power_helix_nterm"]
    st["allf_insert_his_to_lobe2_power_helix_nterm"] = {}
    for cid, ch in (("A", A), ("B", B)):
        h = byno(ch, P["allf_insert_his"])
        e = {}
        for q in range(hw[0], hw[1] + 1):
            t = byno(ch, q)
            d, x, y = min((float(np.linalg.norm(x.coord - y.coord)), x.get_id(), y.get_id())
                          for x in side(h) for y in t)
            e[tag(t)] = {"closest_side_chain_atom_pair": f"{x}-{y} {d:.1f} A",
                         "closest_side_chain_atom_to_backbone_N": round(float(min(
                             np.linalg.norm(x.coord - t["N"].coord) for x in side(h))), 1)}
        st["allf_insert_his_to_lobe2_power_helix_nterm"][f"chain_{cid}_{tag(h)}"] = e
    for pdb in P["scs_structures"]:
        s = structure(pdb)
        alpha, beta = chain(s, "A"), chain(s, "B")
        off, ok, n = numbering_offset(alpha, sucd)
        aC = [r for r in alpha if P["sucd_c_domain"][0] <= r.id[1] + off <= P["sucd_c_domain"][1]]
        aN = [r for r in alpha if P["sucd_n_domain"][0] <= r.id[1] + off <= P["sucd_n_domain"][1]]
        bC = sel(beta, P["succ_c_domain_pdb"])
        hi = next(i for i, r in enumerate(aC) if r.id[1] + off == his)
        rec = {"sucd_numbering": {"uniprot_minus_pdb": off, "identical": ok, "residues": n},
               "catalytic_residue_name_in_pdb": aC[hi].get_resname(), "alpha_c_domain_onto": {}}
        for k, w in lobe.items():
            tgt = sel(A, w)
            a, pairs = align(aC, tgt)
            r = fit_stats(a, pairs, aC)
            # the catalytic His and the unaligned run that contains it
            r["allf_residue_paired_with_catalytic_his"] = (
                f"{tag(pairs[hi][0])} ({pairs[hi][1]:.1f} A)" if hi in pairs else None)
            lo = hi
            while lo - 1 >= 0 and lo - 1 not in pairs:
                lo -= 1
            up = hi
            while up + 1 < len(aC) and up + 1 not in pairs:
                up += 1
            if hi not in pairs:
                r["unpaired_sucd_run_containing_his"] = (
                    f"{aC[lo].id[1] + off}-{aC[up].id[1] + off} " + "".join(one(x) for x in aC[lo:up + 1]))
                flank = [i for i in (lo - 1, up + 1) if i in pairs]
                r["flanking_pairs"] = [f"{tag(aC[i], off)}>{tag(pairs[i][0])} ({pairs[i][1]:.1f} A)" for i in flank]
            rev = {v[0].id[1]: (i, v[1]) for i, v in pairs.items()}
            hc = tf(a, aC[hi]["CA"].coord)
            ne = tf(a, aC[hi]["NE2"].coord)
            roi = {}
            for nres in P["allf_residues_of_interest"]:
                if not w[0] <= nres <= w[1]:
                    continue
                t = byno(A, nres)
                e = {"ca_distance_to_superposed_his_ca": round(float(np.linalg.norm(t["CA"].coord - hc)), 1),
                     "closest_atom_to_superposed_his_NE2": round(float(min(np.linalg.norm(x.coord - ne) for x in t)), 1)}
                e["paired_sucd_residue"] = (f"{tag(aC[rev[nres][0]], off)} ({rev[nres][1]:.1f} A)"
                                            if nres in rev else None)
                roi[tag(t)] = e
            r["allf_residues_of_interest"] = roi
            # every histidine of the AllF structure (both chains), nearest first, in this frame
            allhis = []
            for cid, residues in (("A", A), ("B", B)):
                for t in residues:
                    if t.get_resname() == "HIS" and "CA" in t:
                        allhis.append((round(float(min(np.linalg.norm(x.coord - ne) for x in t)), 1),
                                       round(float(np.linalg.norm(t["CA"].coord - hc)), 1), f"{cid}:{tag(t)}"))
            r["all_allf_histidines_to_superposed_his"] = [
                {"residue": n, "closest_atom_to_superposed_his_NE2": d, "ca_distance_to_superposed_his_ca": c}
                for d, c, n in sorted(allhis)]
            if k == 1:
                # dimer frame: histidine placed through lobe 1 of chain A, insert histidine of chain B
                t = byno(B, P["allf_insert_his"])
                r["chain_B_insert_his_in_this_frame"] = {
                    "residue": tag(t),
                    "ca_distance_to_superposed_his_ca": round(float(np.linalg.norm(t["CA"].coord - hc)), 1),
                    "closest_atom_to_superposed_his_NE2": round(float(min(np.linalg.norm(x.coord - ne) for x in t)), 1)}
            dist = np.linalg.norm(ca(A) - hc, axis=1)
            r["nearest_allf_ca_to_superposed_his_ca"] = [f"{tag(A[i])} {dist[i]:.1f} A" for i in np.argsort(dist)[:3]]
            near = sorted(((float(np.linalg.norm(x.coord - ne)), at_label(x)) for x in ns.search(ne.astype("f"), 4.0)
                           if x.get_parent().get_parent().id == "A"))
            r["chain_A_atoms_within_4A_of_superposed_his_NE2"] = [f"{lab} {d:.1f} A" for d, lab in near]
            if k == 2:
                pw = P["allf_lobe2_pairing_window"]
                r[f"allf_{pw[0]}_{pw[1]}_paired_with_sucd"] = " ".join(
                    f"{tag(byno(A, q))}>{tag(aC[rev[q][0]], off) if q in rev else '-'}"
                    for q in range(pw[0], pw[1] + 1))
            # power-helix N-terminus: the four SucD residues that begin the helix
            sw = P["sucd_power_helix_nterm"]
            ph = [i for i, x in enumerate(aC) if sw[0] <= x.id[1] + off <= sw[1]]
            r[f"sucd_{sw[0]}_{sw[1]}_power_helix_pairs"] = [
                f"{tag(aC[i], off)}>{tag(pairs[i][0])} ({pairs[i][1]:.1f} A)" if i in pairs else f"{tag(aC[i], off)}>-"
                for i in ph]
            rec["alpha_c_domain_onto"][f"allf_lobe{k}_{w[0]}_{w[1]}"] = r
        # beta C-domain onto each lobe
        rec["beta_c_domain_onto"] = {
            f"allf_lobe{k}": fit_stats(*align(bC, sel(A, w)), bC) for k, w in lobe.items()}
        # alpha-C + beta-C pair against lobe 1 + lobe 2, in trans and in cis
        rec["alpha_c_plus_beta_c_pair_onto"] = {}
        for lab, c1, c2 in (("chainA_lobe1_plus_chainB_lobe2", A, B), ("chainA_lobe1_plus_chainA_lobe2", A, A)):
            mob = aC + bC
            a, pairs = align(mob, sel(c1, lobe[1]) + sel(c2, lobe[2]))
            r = fit_stats(a, pairs, mob)
            r["pairs_within_5A_from_beta_c"] = sum(1 for i, v in pairs.items() if i >= len(aC) and v[1] < 5)
            rec["alpha_c_plus_beta_c_pair_onto"][lab] = r
        # rigid CoA transplant through the N-domain fit onto the permuted AllF Rossmann-like domain
        perm = [r for w in P["allf_rossmann_permuted"] for r in sel(A, w)]
        a, pairs = align(aN, perm)
        r = fit_stats(a, pairs, aN)
        r["sample_pairs"] = " ".join(f"{tag(aN[i], off)}>{tag(v[0])}" for i, v in list(pairs.items())[::12])
        own = NeighborSearch([at for ch in s[0] for x in ch for at in x
                              if x.id[0] == " " or x.get_resname() in NONSTD])
        coa = [x for x in s[0]["A"] if x.get_resname() == "COA"]
        if coa:
            lig = coa[0]
            xyz = tf(a, np.array([at.coord for at in lig])).astype("f")
            r["coa_atoms"] = len(lig)
            for cut in (2.2, 3.0):
                r[f"coa_atoms_within_{cut}A_of_3DMY_atoms"] = sum(1 for c in xyz if ns.search(c, cut))
                r[f"native_site_control_within_{cut}A"] = sum(1 for at in lig if own.search(at.coord, cut))
            r["clashing_3DMY_residues_within_2.2A"] = sorted(
                {at_label(q).rsplit(":", 1)[0] for c in xyz for q in ns.search(c, 2.2)})
        else:
            r["coa_atoms"] = 0
        rec["n_domain_onto_permuted_allf_rossmann_and_coa_transplant"] = r
        st["per_scs_structure"][pdb] = rec
    out["structure"] = st

    # ---- 4. family survey
    if not skip_family:
        fam = {}
        for lab, q in P["family_queries"].items():
            txt, hdr = fetch("https://rest.uniprot.org/uniprotkb/stream?format=fasta&query=" + urllib.parse.quote(q))
            fs = parse_fasta(txt)
            m = column_maps(hmm, fs)
            cnt = collections.Counter()
            for name in fs:
                if name not in m:
                    cnt["no_domain_hit"] += 1
                elif col not in m[name]["cols"]:
                    cnt["column_not_covered"] += 1
                else:
                    cnt[m[name]["cols"][col][1]] += 1
            motif, placement = 0, collections.Counter()
            for name, sq in fs.items():
                mm = re.search(P["insert_motif"], sq)
                if not mm:
                    continue
                motif += 1
                hp = mm.start() + 4  # 1-based position of the motif histidine
                if name in m:
                    if hp in m[name]["ins"]:
                        placement[f"insert after match column {m[name]['ins'][hp]}"] += 1
                    elif hp in {p for p, _ in m[name]["cols"].values()}:
                        placement["match column"] += 1
                    else:
                        placement["outside best domain"] += 1
            lens = [len(v) for v in fs.values()]
            fam[lab] = {
                "query": q, "uniprot_release": hdr.get("X-UniProt-Release") or hdr.get("x-uniprot-release"),
                "entries": len(fs), "unique_sequences": len(set(fs.values())),
                "length_min_median_max": [min(lens), statistics.median(lens), max(lens)],
                "residue_at_catalytic_his_column": dict(cnt.most_common()),
                "entries_with_his_at_column": {
                    n.split("|")[1] if "|" in n else n:
                    fs[n][m[n]["cols"][col][0] - 6:m[n]["cols"][col][0] + 5]
                    for n in fs if n in m and m[n]["cols"].get(col, (0, ""))[1] == "H"} if lab.startswith("allf") else "all listed above",
                f"entries_with_motif_{P['insert_motif']}": motif,
                "motif_histidine_profile_state": dict(placement.most_common()),
            }
        out["family"] = fam

    # ---- 5. single-chain co-occurrence of the AllG domain with AllF and AllH domains
    if not skip_family:
        counts = {}
        for lab, q in P["fusion_queries"].items():
            _, hdr = fetch("https://rest.uniprot.org/uniprotkb/search?size=1&fields=accession&query="
                           + urllib.parse.quote(q))
            counts[lab] = int(hdr.get("X-Total-Results") or hdr.get("x-total-results"))
        txt, _ = fetch("https://rest.uniprot.org/uniprotkb/stream?format=fasta&query="
                       + urllib.parse.quote(P["fusion_queries"]["PF06545_AllG_and_PF00549_CoA_ligase"]))
        fs = parse_fasta(txt)
        m = column_maps(hmm, fs)
        lens = [len(v) for v in fs.values()]
        out["allg_domain_co_occurrence"] = {
            "uniprotkb_entry_counts": counts,
            "PF06545_AllG_and_PF00549_CoA_ligase_entries": {
                "length_min_median_max": [min(lens), statistics.median(lens), max(lens)],
                "residue_at_catalytic_his_column": dict(collections.Counter(
                    m[n]["cols"][col][1] if n in m and col in m[n]["cols"] else "not_covered"
                    for n in fs).most_common()),
            },
        }

    yaml.safe_dump(out, sys.stdout, sort_keys=False, width=110, allow_unicode=True)


if __name__ == "__main__":
    main()
