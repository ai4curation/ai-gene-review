# /// script
# requires-python = ">=3.11"
# dependencies = ["pyfamsa==0.7.0"]
# ///
"""Conservation of KRT9 residues among human keratins and KRT9 orthologs; cross-keratin hotspots.

Alignments are built with FAMSA (pyfamsa, default parameters):
  typeI      all reviewed human type I keratins (UniProt)            -> paralog conservation
  orthologs  KRT9 + PANTHER least-diverged orthologs (UniProt seqs)  -> ortholog conservation
  keratins   all reviewed human type I and type II keratins          -> disease-variant lookup
Disease variants of the other keratins are UniProt 'Natural variant' features whose note starts
with "in <disease>"; nothing about them is taken from memory.

Outputs: results/04_alignment_*.fasta, 04_conservation_per_residue.tsv,
         04_variant_conservation.tsv, 04_hotspot_columns.tsv, 04_conservation_summary.json
Usage: uv run 04_conservation.py [--accession P35527] [--tag KRT9]
"""
from __future__ import annotations

import argparse
import math
from collections import Counter, defaultdict

from pyfamsa import Aligner, Sequence

from common import (DATA, RESULTS, aln_maps, architecture, domain_of, dump_json, gene_name, load_json,
                    natural_variants, read_tsv, seg, write_tsv)


def align(named: list[tuple[str, str]]) -> dict[str, str]:
    msa = Aligner().align([Sequence(n.encode(), s.encode()) for n, s in named])
    return {m.id.decode(): m.sequence.decode() for m in msa}


def write_fasta(aln: dict[str, str], path) -> None:
    with open(path, "w") as fh:
        for k, v in aln.items():
            fh.write(f">{k}\n")
            for i in range(0, len(v), 80):
                fh.write(v[i:i + 80] + "\n")


def column_stats(aln: dict[str, str], target: str, col: int) -> dict:
    tres = aln[target][col]
    others = [s[col] for k, s in aln.items() if k != target]
    nongap = [x for x in others if x != "-"]
    c = Counter(nongap)
    n = len(nongap)
    ent = -sum((v / n) * math.log2(v / n) for v in c.values()) if n else ""
    return {"n_other_sequences": len(others), "n_aligned": n,
            "gap_fraction": 1 - n / len(others) if others else "",
            "identity_to_target": (c[tres] / n) if n else "",
            "entropy_bits": ent,
            "consensus": c.most_common(1)[0][0] if n else "",
            "residue_counts": ",".join(f"{a}:{v}" for a, v in c.most_common())}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--accession", default="P35527")
    ap.add_argument("--tag", default="KRT9")
    ap.add_argument("--boundary-window", type=int, default=20)
    a = ap.parse_args()

    entry = load_json(DATA / f"uniprot_{a.accession}.json")
    seq = entry["sequence"]["value"]
    arch = architecture(entry)
    tname = gene_name(entry)
    kers = load_json(DATA / "human_keratins.json")
    by_gene = {gene_name(k): k for k in kers}
    type1 = [k for k in kers if k["keratin_type"] == "I"]
    orth = load_json(DATA / "panther_orthologs.json")

    aln1 = align([(gene_name(k), k["sequence"]["value"]) for k in type1])
    alnk = align([(gene_name(k), k["sequence"]["value"]) for k in kers])
    onamed = [(tname, seq)]
    ometa = []
    for o in orth["orthologs"]:
        e = orth["entries"].get(o["accession"])
        if not e:
            ometa.append({**o, "used": False, "reason": "accession not resolved in UniProt"})
            continue
        nm = f"{o['species']}_{o['accession']}"
        onamed.append((nm, e["sequence"]["value"]))
        ometa.append({**o, "used": True, "name": nm, "length": e["sequence"]["length"],
                      "entry_type": e["entryType"], "organism": e["organism"]["scientificName"]})
    alno = align(onamed)
    write_fasta(aln1, RESULTS / "04_alignment_typeI.fasta")
    write_fasta(alnk, RESULTS / "04_alignment_keratins.fasta")
    write_fasta(alno, RESULTS / "04_alignment_orthologs.fasta")

    r2c1, _ = aln_maps(aln1[tname])
    r2ck, _ = aln_maps(alnk[tname])
    r2co, _ = aln_maps(alno[tname])

    # disease variants of every keratin, indexed by column of the all-keratin alignment
    col_hits = defaultdict(list)
    for g, k in by_gene.items():
        r2c, _ = aln_maps(alnk[g])
        for v in natural_variants(k):
            if not v["disease"] or v["start"] != v["end"]:
                continue
            col_hits[r2c[v["start"]]].append({"gene": g, "type": k["keratin_type"], "position": v["start"],
                                              "ref": v["ref"], "alts": "/".join(v["alts"]),
                                              "disease": v["disease"], "feature_id": v["feature_id"]})
    hot_rows = []
    for col, hits in col_hits.items():
        genes = sorted({h["gene"] for h in hits})
        tpos = next((p for p, c in r2ck.items() if c == col), None)
        hot_rows.append({"alignment_column": col, f"{tname}_position": tpos or "",
                         f"{tname}_residue": seq[tpos - 1] if tpos else "",
                         f"{tname}_domain": domain_of(tpos, arch) if tpos else "",
                         "n_keratin_genes_with_disease_variant": len(genes),
                         "n_disease_variants": len(hits), "genes": genes,
                         "variants": [f"{h['gene']}:{h['ref']}{h['position']}{h['alts']}({h['disease']})" for h in hits]})
    hot_rows.sort(key=lambda r: (-r["n_keratin_genes_with_disease_variant"], -r["n_disease_variants"]))
    for i, r in enumerate(hot_rows, start=1):
        r["rank_by_genes"] = i
    write_tsv(hot_rows, RESULTS / "04_hotspot_columns.tsv")
    hot_by_col = {r["alignment_column"]: r for r in hot_rows}

    heptad = {int(r["position"]): r["heptad"] for r in read_tsv(RESULTS / f"01_{a.tag}_heptad_register.tsv")}
    per_res = []
    for pos, aa in enumerate(seq, start=1):
        p = column_stats(aln1, tname, r2c1[pos])
        o = column_stats(alno, tname, r2co[pos])
        k = column_stats(alnk, tname, r2ck[pos])
        hits = [h for h in col_hits.get(r2ck[pos], []) if h["gene"] != tname]
        per_res.append({
            "position": pos, "residue": aa, "domain": domain_of(pos, arch), "heptad": heptad.get(pos, ""),
            "typeI_n_aligned": p["n_aligned"], "typeI_gap_fraction": p["gap_fraction"],
            "typeI_identity": p["identity_to_target"], "typeI_entropy_bits": p["entropy_bits"],
            "typeI_consensus": p["consensus"], "typeI_residue_counts": p["residue_counts"],
            "all_keratin_identity": k["identity_to_target"], "all_keratin_n_aligned": k["n_aligned"],
            "all_keratin_consensus": k["consensus"],
            "ortholog_n_aligned": o["n_aligned"], "ortholog_identity": o["identity_to_target"],
            "ortholog_residue_counts": o["residue_counts"],
            "aligned_residues_other_keratins": ",".join(
                f"{g}:{alnk[g][r2ck[pos]]}" for g in ("KRT10", "KRT14", "KRT16", "KRT17", "KRT12", "KRT1", "KRT5")
                if g in alnk),
            "n_other_keratin_genes_with_disease_variant_at_column": len({h["gene"] for h in hits}),
            "other_keratin_disease_variants": [f"{h['gene']}:{h['ref']}{h['position']}{h['alts']}({h['disease']})"
                                               for h in hits],
            "hotspot_rank_by_genes": hot_by_col.get(r2ck[pos], {}).get("rank_by_genes", ""),
        })
    write_tsv(per_res, RESULTS / "04_conservation_per_residue.tsv")

    merged = read_tsv(RESULTS / "02_variants_merged.tsv")
    dpos = defaultdict(list)
    for r in merged:
        if r["disease_set"] == "yes" and r["position"]:
            dpos[int(r["position"])].append(r["variant"])
    vrows = [{**per_res[p - 1], "disease_variants_at_position": dpos[p]} for p in sorted(dpos)]
    write_tsv(vrows, RESULTS / "04_variant_conservation.tsv")

    # region summaries
    c1a, c2 = seg(arch, "Coil 1A"), seg(arch, "Coil 2")
    w = a.boundary_window
    him = set(range(c1a["start"], c1a["start"] + w)); htm = set(range(c2["end"] - w + 1, c2["end"] + 1))
    coil = {p for s in arch if s["name"].startswith("Coil") for p in range(s["start"], s["end"] + 1)}
    groups = {f"helix initiation segment (first {w} of Coil 1A)": him,
              f"helix termination segment (last {w} of Coil 2)": htm,
              "other rod coil residues": coil - him - htm,
              "disease-variant positions": set(dpos)}
    for s in arch:
        groups[s["name"]] = set(range(s["start"], s["end"] + 1))

    def mean(vals):
        vals = [v for v in vals if v != ""]
        return sum(vals) / len(vals) if vals else ""

    summ = []
    for name, ps in groups.items():
        sub = [per_res[p - 1] for p in sorted(ps)]
        summ.append({"region": name, "n_residues": len(sub),
                     "mean_typeI_identity": mean([r["typeI_identity"] for r in sub]),
                     "mean_all_keratin_identity": mean([r["all_keratin_identity"] for r in sub]),
                     "mean_ortholog_identity": mean([r["ortholog_identity"] for r in sub]),
                     "n_invariant_in_typeI": sum(1 for r in sub if r["typeI_identity"] == 1.0),
                     "n_positions_with_other_keratin_disease_variant":
                         sum(1 for r in sub if r["n_other_keratin_genes_with_disease_variant_at_column"] > 0)})
    write_tsv(summ, RESULTS / "04_region_conservation.tsv")

    def cons_string(positions):
        return "".join(per_res[p - 1]["typeI_consensus"] or "-" for p in positions)

    dump_json({
        "n_typeI": len(type1), "typeI_genes": sorted(gene_name(k) for k in type1),
        "n_keratins": len(kers), "alignment_lengths": {"typeI": len(aln1[tname]), "keratins": len(alnk[tname]),
                                                       "orthologs": len(alno[tname])},
        "orthologs": ometa, "panther_version": orth.get("panther_version"),
        "n_keratin_disease_variant_columns": len(hot_rows),
        "top_hotspot_columns": hot_rows[:10],
        "typeI_consensus_helix_initiation_segment": cons_string(sorted(him)),
        "target_helix_initiation_segment": "".join(seq[p - 1] for p in sorted(him)),
        "typeI_consensus_helix_termination_segment": cons_string(sorted(htm)),
        "target_helix_termination_segment": "".join(seq[p - 1] for p in sorted(htm)),
    }, RESULTS / "04_conservation_summary.json")
    print("wrote 04_*")


if __name__ == "__main__":
    main()
