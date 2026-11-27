# /// script
# requires-python = ">=3.11"
# dependencies = ["biopython==1.85", "numpy==2.3.2"]
# ///
"""Structural context of KRT9 variant positions.

1. Experimental-structure check for the target (data/experimental_structure_check_*.json).
2. AlphaFold model: per-residue pLDDT (CA B-factor), summarised per domain and at variant sites.
3. Homology templates: every X-ray entry returned by the RCSB search for human intermediate
   filament proteins in which a chain (>= --min-chain residues) aligns to the KRT9 rod and has a
   parallel coiled-coil partner chain in the asymmetric unit. For each template residue mapped
   to a KRT9 position: side-chain contact with the partner chain (heavy-atom distance < 4.0 A;
   CA is used for glycine), relative side-chain-inclusive SASA in the dimer and in the isolated
   chain (Shrake-Rupley, probe 1.4 A; maximum ASA values of Tien et al. 2013), interchain salt
   bridges (Lys NZ / Arg NE,NH1,NH2 / His ND1,NE2 to Asp OD / Glu OE < 4.0 A) and interchain
   hydrogen-bond candidates (side-chain N/O to partner N/O <= 3.5 A), intrachain salt bridges.

Outputs: results/05_alphafold_plddt_by_domain.tsv, 05_alphafold_plddt_per_residue.tsv,
         05_templates.tsv, 05_template_residues.tsv, 05_variant_structure_map.tsv,
         05_variant_structure_summary.tsv, 05_heptad_vs_contact.tsv, 05_structure_summary.json
Usage: uv run 05_structure.py [--accession P35527] [--tag KRT9]
"""
from __future__ import annotations

import argparse
import warnings
from collections import Counter, defaultdict

import numpy as np
from Bio.Align import PairwiseAligner, substitution_matrices
from Bio.PDB import MMCIFParser, NeighborSearch
from Bio.PDB.Model import Model
from Bio.PDB.SASA import ShrakeRupley
from Bio.PDB.Structure import Structure

from common import (CACHE, DATA, RESULTS, THREE2ONE_UPPER, architecture, domain_of, dump_json, gene_name,
                    load_json, read_tsv, write_tsv)

warnings.filterwarnings("ignore")
MAX_ASA = {"A": 129, "R": 274, "N": 195, "D": 193, "C": 167, "E": 223, "Q": 225, "G": 104, "H": 224,
           "I": 197, "L": 201, "K": 236, "M": 224, "F": 240, "P": 159, "S": 155, "T": 172, "W": 285,
           "Y": 263, "V": 174}  # Tien et al. 2013 (PLoS One 8:e80635), theoretical values
BACKBONE = {"N", "CA", "C", "O", "OXT"}
POS_ATOMS = {("LYS", "NZ"), ("ARG", "NE"), ("ARG", "NH1"), ("ARG", "NH2"), ("HIS", "ND1"), ("HIS", "NE2")}
NEG_ATOMS = {("ASP", "OD1"), ("ASP", "OD2"), ("GLU", "OE1"), ("GLU", "OE2")}
CONTACT = 4.0
HBOND = 3.5
BURIED_RSA = 0.25


def one(resname: str) -> str:
    if resname == "MSE":
        return "M"
    return THREE2ONE_UPPER.get(resname, "X")


def chain_residues(chain):
    out = []
    for res in chain:
        het = res.id[0]
        if het == "W" or (het != " " and res.get_resname() != "MSE"):
            continue
        if one(res.get_resname()) == "X" or "CA" not in res:
            continue
        out.append(res)
    return out


def heavy(res):
    return [a for a in res if a.element != "H"]


def side_atoms(res):
    sc = [a for a in heavy(res) if a.get_id() not in BACKBONE]
    return sc if sc else [res["CA"]]


def label(res) -> str:
    return f"{res.get_parent().id}:{one(res.get_resname())}{res.id[1]}"


def align_to_target(aligner, tseq: str, cseq: str):
    """Local alignment; returns (pairs [(target_pos1, chain_idx0)], identity over pairs)."""
    aln = aligner.align(tseq, cseq)[0]
    pairs = []
    for (ts, te), (cs, ce) in zip(*aln.aligned):
        for k in range(te - ts):
            pairs.append((ts + k + 1, cs + k))
    ident = sum(1 for t, c in pairs if tseq[t - 1] == cseq[c]) / len(pairs) if pairs else 0.0
    n_blocks = len(aln.aligned[0])
    return pairs, ident, n_blocks, aln.score


def sasa_by_residue(chains) -> dict:
    s = Structure("x"); m = Model(0); s.add(m)
    for ch in chains:
        m.add(ch.copy())
    for ch in m:
        for res in list(ch):
            if res.id[0] == "W" or (res.id[0] != " " and res.get_resname() != "MSE"):
                ch.detach_child(res.id)
    ShrakeRupley(probe_radius=1.4).compute(m, level="R")
    return {(ch.id, res.id): res.sasa for ch in m for res in ch}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--accession", default="P35527")
    ap.add_argument("--tag", default="KRT9")
    ap.add_argument("--min-chain", type=int, default=30)
    ap.add_argument("--min-identity", type=float, default=0.25)
    ap.add_argument("--min-pairs", type=int, default=25)
    ap.add_argument("--min-partner-contacts", type=int, default=10)
    a = ap.parse_args()

    entry = load_json(DATA / f"uniprot_{a.accession}.json")
    tseq = entry["sequence"]["value"]
    arch = architecture(entry)
    heptad = {int(r["position"]): r["heptad"] for r in read_tsv(RESULTS / f"01_{a.tag}_heptad_register.tsv")}
    merged = read_tsv(RESULTS / "02_variants_merged.tsv")
    dvars = defaultdict(list)
    for r in merged:
        if r["disease_set"] == "yes" and r["position"]:
            dvars[int(r["position"])].append(r["variant"])
    kers = {k["primaryAccession"]: k for k in load_json(DATA / "human_keratins.json")}
    iff = {k["primaryAccession"]: k for k in load_json(DATA / "human_if_family.json")}
    parser = MMCIFParser(QUIET=True)

    # ---------------------------------------------------------------- AlphaFold
    afmeta = load_json(DATA / f"alphafold_{a.accession}.json")
    af_rows, af_dom, af_sum = [], [], {}
    for m in afmeta:
        st = parser.get_structure("af", CACHE / f"{m['modelEntityId']}.cif")
        ch = next(iter(st[0]))
        plddt = {res.id[1]: res["CA"].get_bfactor() for res in ch}
        af_seq = "".join(one(res.get_resname()) for res in ch)
        af_sum = {"model": m["modelEntityId"], "version": m["latestVersion"], "tool": m["toolUsed"],
                  "model_created": m["modelCreatedDate"], "global_plddt_api": m["globalMetricValue"],
                  "sequence_identical_to_canonical": af_seq == tseq,
                  "mean_plddt": float(np.mean(list(plddt.values())))}
        for pos, aa in enumerate(tseq, start=1):
            af_rows.append({"position": pos, "residue": aa, "domain": domain_of(pos, arch),
                            "heptad": heptad.get(pos, ""), "plddt": plddt.get(pos, ""),
                            "disease_variants": dvars.get(pos, [])})
        for s in arch + [{"name": "full length", "start": 1, "end": len(tseq)}]:
            vals = np.array([plddt[p] for p in range(s["start"], s["end"] + 1)])
            af_dom.append({"domain": s["name"], "start": s["start"], "end": s["end"], "n": len(vals),
                           "mean_plddt": float(vals.mean()), "min_plddt": float(vals.min()),
                           "max_plddt": float(vals.max()),
                           "fraction_plddt_ge_90": float((vals >= 90).mean()),
                           "fraction_plddt_ge_70": float((vals >= 70).mean()),
                           "fraction_plddt_lt_50": float((vals < 50).mean())})
    write_tsv(af_rows, RESULTS / "05_alphafold_plddt_per_residue.tsv")
    write_tsv(af_dom, RESULTS / "05_alphafold_plddt_by_domain.tsv")

    # ---------------------------------------------------------------- templates
    aligner = PairwiseAligner()
    aligner.mode = "local"
    aligner.substitution_matrix = substitution_matrices.load("BLOSUM62")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -1

    def keratin_of(uniprot_ids, chain_seq):
        """Human keratin a chain corresponds to: by UniProt id, else by >=90% identical local alignment
        (covers constructs deposited against an unreviewed accession)."""
        for u in uniprot_ids:
            if u in kers:
                return kers[u]
        best = None
        for k in kers.values():
            pairs, ident, _, _ = align_to_target(aligner, k["sequence"]["value"], chain_seq)
            if len(pairs) >= a.min_chain and ident >= 0.9 and (best is None or ident > best[0]):
                best = (ident, k)
        return best[1] if best else None

    rc = load_json(DATA / "rcsb_if_entries.json")
    tmpl_rows, res_rows, skipped = [], [], []
    method_counts = Counter()
    for ent in rc["entries"]:
        method = ent["exptl"][0]["method"] if ent.get("exptl") else "unknown"
        method_counts[method] += 1
        if method != "X-RAY DIFFRACTION":
            continue
        pid = ent["rcsb_id"]
        chain_info = {}
        for pe in ent["polymer_entities"]:
            ids = pe["rcsb_polymer_entity_container_identifiers"]
            for c in ids["auth_asym_ids"]:
                chain_info[c] = {"uniprot": ids.get("uniprot_ids") or [],
                                 "description": (pe.get("rcsb_polymer_entity") or {}).get("pdbx_description", ""),
                                 "entity_length": len(pe["entity_poly"]["pdbx_seq_one_letter_code_can"])}
        if_chains = [c for c, i in chain_info.items()
                     if any(u in iff for u in i["uniprot"]) and i["entity_length"] >= a.min_chain]
        if not if_chains:
            skipped.append({"entry": pid, "reason": f"no intermediate filament chain >= {a.min_chain} residues"})
            continue
        model = parser.get_structure(pid, CACHE / f"{pid}.cif")[0]
        chains = {ch.id: ch for ch in model}
        cres = {cid: chain_residues(ch) for cid, ch in chains.items()}
        atoms_all = [at for cid in chains for res in cres[cid] for at in heavy(res)]
        ns = NeighborSearch(atoms_all)
        res_index = {cid: {res.id: i for i, res in enumerate(cres[cid])} for cid in chains}
        used_any = False
        for cid in if_chains:
            if cid not in chains or len(cres[cid]) < a.min_chain:
                continue
            cseq = "".join(one(r.get_resname()) for r in cres[cid])
            pairs, ident, n_blocks, score = align_to_target(aligner, tseq, cseq)
            tpos = [t for t, _ in pairs]
            doms = Counter(domain_of(t, arch) for t in tpos)
            if len(pairs) < a.min_pairs or ident < a.min_identity:
                skipped.append({"entry": pid, "chain": cid, "reason":
                                f"alignment to target too weak ({len(pairs)} pairs, identity {ident:.2f})"})
                continue
            if not any(d.startswith("Coil") for d in doms):
                skipped.append({"entry": pid, "chain": cid, "reason": "aligned region is outside the target rod coils"})
                continue
            # partner = other chain with most residue-residue contacts
            contact_pairs = defaultdict(set)
            for at in (x for res in cres[cid] for x in heavy(res)):
                for other in ns.search(at.coord, CONTACT):
                    ores = other.get_parent(); och = ores.get_parent().id
                    if och != cid and ores.id in res_index[och]:
                        contact_pairs[och].add((at.get_parent().id, ores.id))
            if not contact_pairs:
                skipped.append({"entry": pid, "chain": cid, "reason": "no other chain within 4 A in the asymmetric unit"})
                continue
            partner = max(contact_pairs, key=lambda k: len(contact_pairs[k]))
            cp = contact_pairs[partner]
            if len(cp) < a.min_partner_contacts or len(cres[partner]) < a.min_chain:
                skipped.append({"entry": pid, "chain": cid, "reason":
                                f"best partner chain {partner} has only {len(cp)} residue contacts or is too short"})
                continue
            xi = np.array([res_index[cid][x] for x, _ in cp]); yi = np.array([res_index[partner][y] for _, y in cp])
            slope = float(np.corrcoef(xi, yi)[0, 1]) if len(set(xi)) > 1 and len(set(yi)) > 1 else 0.0
            if slope <= 0.5:
                skipped.append({"entry": pid, "chain": cid, "reason":
                                f"best partner chain {partner} is not parallel (index correlation {slope:.2f})"})
                continue
            ci, pi = chain_info[cid], chain_info.get(partner, {"uniprot": [], "description": ""})
            c_ker = keratin_of(ci["uniprot"], cseq)
            p_ker = keratin_of(pi["uniprot"], "".join(one(r.get_resname()) for r in cres[partner]))
            c_if = next((iff[u] for u in ci["uniprot"] if u in iff), None)
            same_entity = ci["uniprot"] == pi["uniprot"] and ci["description"] == pi["description"]
            if c_ker and c_ker["keratin_type"] == "I" and not same_entity and p_ker and p_ker["keratin_type"] == "II":
                tclass = "keratin type I chain in type I/type II heterodimer"
            elif c_ker and c_ker["keratin_type"] == "II":
                skipped.append({"entry": pid, "chain": cid, "reason":
                                "type II keratin chain: used only as the partner of the type I chain"})
                used_any = True
                continue
            else:
                tclass = "non-keratin intermediate filament homodimer (remote template)"
            useq = c_if["sequence"]["value"] if c_if else ""
            num_ok = sum(1 for r in cres[cid] if 0 < r.id[1] <= len(useq) and useq[r.id[1] - 1] == one(r.get_resname()))
            sasa_d = sasa_by_residue([chains[cid], chains[partner]])
            sasa_m = sasa_by_residue([chains[cid]])
            partner_atoms = [at for res in cres[partner] for at in heavy(res)]
            pns = NeighborSearch(partner_atoms)
            others_atoms = [at for oc in chains if oc not in (cid, partner) for res in cres[oc] for at in heavy(res)]
            ons = NeighborSearch(others_atoms) if others_atoms else None
            self_atoms = [at for res in cres[cid] for at in heavy(res)]
            sns = NeighborSearch(self_atoms)
            tmpl_id = f"{pid}:{cid}"
            n_contact = 0
            for t, c in pairs:
                res = cres[cid][c]
                aa = one(res.get_resname())
                sc = side_atoms(res)
                near = {}
                for at in sc:
                    for o in pns.search(at.coord, CONTACT):
                        d = float(np.linalg.norm(at.coord - o.coord))
                        k = label(o.get_parent())
                        near[k] = min(near.get(k, 9.9), d)
                mind = min((float(np.linalg.norm(at.coord - o.coord)) for at in sc
                            for o in pns.search(at.coord, 12.0)), default="")
                salt, hb, intra_salt = set(), set(), set()
                for at in sc:
                    key = (res.get_resname(), at.get_id())
                    for o in pns.search(at.coord, CONTACT):
                        ok = (o.get_parent().get_resname(), o.get_id())
                        if (key in POS_ATOMS and ok in NEG_ATOMS) or (key in NEG_ATOMS and ok in POS_ATOMS):
                            salt.add(label(o.get_parent()))
                        d = float(np.linalg.norm(at.coord - o.coord))
                        if at.element in ("N", "O") and o.element in ("N", "O") and d <= HBOND:
                            hb.add(f"{at.get_id()}-{label(o.get_parent())}.{o.get_id()}")
                    for o in sns.search(at.coord, CONTACT):
                        if o.get_parent() is res:
                            continue
                        ok = (o.get_parent().get_resname(), o.get_id())
                        if (key in POS_ATOMS and ok in NEG_ATOMS) or (key in NEG_ATOMS and ok in POS_ATOMS):
                            intra_salt.add(label(o.get_parent()))
                third = set()
                if ons:
                    for at in sc:
                        for o in ons.search(at.coord, CONTACT):
                            third.add(label(o.get_parent()))
                rsa_d = sasa_d[(cid, res.id)] / MAX_ASA[aa]
                rsa_m = sasa_m[(cid, res.id)] / MAX_ASA[aa]
                contact = bool(near)
                n_contact += contact
                res_rows.append({
                    "template": tmpl_id, "template_class": tclass, "alignment_blocks": n_blocks,
                    "target_position": t,
                    "target_residue": tseq[t - 1], "target_domain": domain_of(t, arch),
                    "target_heptad": heptad.get(t, ""), "template_residue": aa,
                    "template_resnum": res.id[1], "identical": aa == tseq[t - 1],
                    "sidechain_contacts_partner": contact,
                    "partner_residues_within_4A": sorted(near), "min_sidechain_distance_to_partner": mind,
                    "rsa_in_dimer": rsa_d, "rsa_isolated_chain": rsa_m, "rsa_lost_on_dimerisation": rsa_m - rsa_d,
                    "buried_in_dimer": rsa_d < BURIED_RSA,
                    "interchain_salt_bridges": sorted(salt), "interchain_hbond_candidates": sorted(hb),
                    "intrachain_salt_bridges": sorted(intra_salt),
                    "sidechain_contacts_other_chains": sorted(third),
                    "target_disease_variants": dvars.get(t, [])})
            used_any = True
            tmpl_rows.append({
                "template": tmpl_id, "entry": pid, "chain": cid, "template_class": tclass,
                "title": ent["struct"]["title"], "resolution_A": (ent["rcsb_entry_info"]["resolution_combined"] or [""])[0],
                "release_date": ent["rcsb_accession_info"]["initial_release_date"][:10],
                "pubmed": (ent.get("rcsb_primary_citation") or {}).get("pdbx_database_id_PubMed", ""),
                "chain_uniprot": ci["uniprot"], "chain_gene": gene_name(c_if) if c_if else "",
                "chain_description": ci["description"], "partner_chain": partner,
                "partner_uniprot": pi["uniprot"], "partner_description": pi["description"],
                "partner_keratin_gene": gene_name(p_ker) if p_ker else "",
                "n_residues_observed": len(cres[cid]),
                "author_numbering_matches_uniprot_fraction": num_ok / len(cres[cid]),
                "template_first_resnum": cres[cid][pairs[0][1]].id[1], "template_last_resnum": cres[cid][pairs[-1][1]].id[1],
                "target_start": min(tpos), "target_end": max(tpos), "n_aligned_pairs": len(pairs),
                "alignment_blocks": n_blocks, "identity_to_target": ident, "alignment_score": score,
                "target_domains_covered": ",".join(f"{k}:{v}" for k, v in doms.most_common()),
                "partner_residue_contacts": len(cp), "parallel_index_correlation": slope,
                "n_mapped_residues_with_partner_contact": n_contact,
                "n_disease_positions_covered": sum(1 for t in set(tpos) if t in dvars)})
        if not used_any:
            skipped.append({"entry": pid, "reason": "no chain passed the template criteria"})
    tmpl_rows.sort(key=lambda r: (r["template_class"], r["target_start"], r["template"]))
    write_tsv(tmpl_rows, RESULTS / "05_templates.tsv")
    res_rows.sort(key=lambda r: (r["target_position"], r["template"]))
    write_tsv(res_rows, RESULTS / "05_template_residues.tsv")
    vmap = [r for r in res_rows if r["target_disease_variants"]]
    write_tsv(vmap, RESULTS / "05_variant_structure_map.tsv")

    # ---------------------------------------------------------------- summaries
    def klass(r):
        if r["template_class"].startswith("keratin type I"):
            return "keratin heterodimer"
        # remote templates are summarised only when they align to the target without gaps
        return "non-keratin IF" if r["alignment_blocks"] == 1 else "non-keratin IF (gapped alignment, not summarised)"

    hv = []
    for kc in ("keratin heterodimer", "non-keratin IF"):
        sub = [r for r in res_rows if klass(r) == kc and r["target_heptad"]]
        for h in "abcdefg":
            x = [r for r in sub if r["target_heptad"] == h]
            if x:
                hv.append({"template_set": kc, "target_heptad": h, "n_residue_observations": len(x),
                           "fraction_sidechain_contacting_partner": sum(r["sidechain_contacts_partner"] for r in x) / len(x),
                           "mean_rsa_in_dimer": float(np.mean([r["rsa_in_dimer"] for r in x])),
                           "mean_rsa_lost_on_dimerisation": float(np.mean([r["rsa_lost_on_dimerisation"] for r in x]))})
        for name, hs in (("a+d", "ad"), ("e+g", "eg"), ("b+c+f", "bcf")):
            x = [r for r in sub if r["target_heptad"] in hs]
            if x:
                hv.append({"template_set": kc, "target_heptad": name, "n_residue_observations": len(x),
                           "fraction_sidechain_contacting_partner": sum(r["sidechain_contacts_partner"] for r in x) / len(x),
                           "mean_rsa_in_dimer": float(np.mean([r["rsa_in_dimer"] for r in x])),
                           "mean_rsa_lost_on_dimerisation": float(np.mean([r["rsa_lost_on_dimerisation"] for r in x]))})
    write_tsv(hv, RESULTS / "05_heptad_vs_contact.tsv")

    plddt = {r["position"]: r["plddt"] for r in af_rows}
    vsum = []
    for pos in sorted(dvars):
        obs = [r for r in res_rows if r["target_position"] == pos]
        row = {"position": pos, "residue": tseq[pos - 1], "domain": domain_of(pos, arch),
               "heptad": heptad.get(pos, ""), "disease_variants": dvars[pos],
               "alphafold_plddt": plddt.get(pos, "")}
        for kc, tag in (("keratin heterodimer", "keratin"), ("non-keratin IF", "nonkeratin")):
            x = [r for r in obs if klass(r) == kc]
            row[f"{tag}_templates"] = [r["template"] for r in x]
            row[f"{tag}_template_residues"] = sorted({r["template_residue"] for r in x})
            row[f"{tag}_n_obs"] = len(x)
            row[f"{tag}_n_contact_partner"] = sum(r["sidechain_contacts_partner"] for r in x)
            row[f"{tag}_mean_rsa_dimer"] = float(np.mean([r["rsa_in_dimer"] for r in x])) if x else ""
            row[f"{tag}_n_buried"] = sum(r["buried_in_dimer"] for r in x)
            row[f"{tag}_n_interchain_salt_bridge"] = sum(1 for r in x if r["interchain_salt_bridges"])
            row[f"{tag}_n_interchain_hbond"] = sum(1 for r in x if r["interchain_hbond_candidates"])
            row[f"{tag}_n_intrachain_salt_bridge"] = sum(1 for r in x if r["intrachain_salt_bridges"])
        h = row["heptad"]
        row["heptad_class"] = ("core (a/d)" if h in ("a", "d") else "flanking (e/g)" if h in ("e", "g") else
                               "outer (b/c/f)" if h else "not in a coil segment")
        nobs = row["keratin_n_obs"] + row["nonkeratin_n_obs"]
        ncon = row["keratin_n_contact_partner"] + row["nonkeratin_n_contact_partner"]
        row["structural_class"] = ("no template coverage" if nobs == 0 else
                                   "interface (side chain contacts partner in majority of templates)"
                                   if ncon * 2 > nobs else
                                   "interface in a minority of templates" if ncon else
                                   "no partner contact in any template")
        vsum.append(row)
    write_tsv(vsum, RESULTS / "05_variant_structure_summary.tsv")

    cov = Counter()
    for r in tmpl_rows:
        cov[r["template_class"]] += 1
    covered = {kc: sorted({r["target_position"] for r in res_rows if klass(r) == kc})
               for kc in ("keratin heterodimer", "non-keratin IF")}

    def ranges(ps):
        out, start, prev = [], None, None
        for p in ps:
            if start is None:
                start = prev = p
            elif p == prev + 1:
                prev = p
            else:
                out.append(f"{start}-{prev}"); start = prev = p
        if start is not None:
            out.append(f"{start}-{prev}")
        return out

    dump_json({
        "experimental_structure_check": load_json(DATA / f"experimental_structure_check_{a.accession}.json"),
        "alphafold": af_sum,
        "rcsb_entries_by_method": dict(method_counts), "n_templates_by_class": dict(cov),
        "target_ranges_covered": {k: ranges(v) for k, v in covered.items()},
        "disease_positions": sorted(dvars),
        "disease_positions_covered_by_keratin_heterodimer": sorted(set(dvars) & set(covered["keratin heterodimer"])),
        "disease_positions_covered_only_by_nonkeratin": sorted((set(dvars) & set(covered["non-keratin IF"])) -
                                                                set(covered["keratin heterodimer"])),
        "disease_positions_without_template": sorted(set(dvars) - set(covered["keratin heterodimer"]) -
                                                     set(covered["non-keratin IF"])),
        "parameters": {"contact_cutoff_A": CONTACT, "hbond_cutoff_A": HBOND, "buried_rsa_threshold": BURIED_RSA,
                       "min_identity": a.min_identity, "min_pairs": a.min_pairs,
                       "min_partner_contacts": a.min_partner_contacts},
        "skipped": skipped,
    }, RESULTS / "05_structure_summary.json")
    print(f"templates: {len(tmpl_rows)}; residue rows: {len(res_rows)}; skipped: {len(skipped)}")


if __name__ == "__main__":
    main()
