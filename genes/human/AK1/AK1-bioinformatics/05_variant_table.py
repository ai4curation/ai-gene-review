"""Merge the outputs of scripts 01-04 into one per-variant table (JSON + Markdown)."""
from __future__ import annotations

import csv
import json

from ak1_common import DATA, RESULTS, dump, uniprot_features

VOLUME = {"G": 60.1, "A": 88.6, "S": 89.0, "C": 108.5, "D": 111.1, "P": 112.7, "N": 114.1,
          "T": 116.1, "E": 138.4, "V": 140.0, "Q": 143.8, "H": 153.2, "M": 162.9, "I": 166.7,
          "L": 166.7, "K": 168.6, "R": 173.4, "F": 189.9, "Y": 193.6, "W": 227.8}
CHARGE = {"D": -1, "E": -1, "K": 1, "R": 1}


def main() -> None:
    cons = json.loads((RESULTS / "variant_consequences.json").read_text())
    struct = json.loads((RESULTS / "structure_mapping.json").read_text())
    conserv = json.loads((RESULTS / "conservation.json").read_text())
    pop = json.loads((RESULTS / "population.json").read_text())
    feats = uniprot_features()
    s1 = struct["structures"]["1Z83"]["residues"]
    s2 = struct["structures"]["2C95"]["residues"]
    af = struct["alphafold"]
    am_path = DATA / "alphamissense.csv"
    af["alphamissense"] = {}
    if am_path.exists():
        with am_path.open() as fh:
            for row in csv.DictReader(fh):
                af["alphamissense"][row["protein_variant"]] = (float(row["am_pathogenicity"]), row["am_class"])
    popmap = {r["cdna"]: r for r in pop["reported_disease_variants"]}
    rows = []
    for v in cons["variants"]:
        pos = v.get("first_changed_residue")
        r1, r2 = s1.get(str(pos)), s2.get(str(pos))
        c = conserv["positions"][str(pos)]
        binding = [f"{f['ligand']} ({f['start']}" + (f"-{f['end']})" if f['end'] != f['start'] else ")")
                   for f in feats if f["type"] == "BINDING" and f["start"] <= pos <= f["end"]]
        sse = [f["type"].lower() + f" {f['start']}-{f['end']}" for f in feats
               if f["type"] in ("HELIX", "STRAND", "TURN") and f["start"] <= pos <= f["end"]]
        row = {
            "cdna": v["cdna"], "computed_protein": v.get("hgvs_p"), "reported_protein": v["reported_protein"],
            "class": v.get("class"), "source": v["source"], "position": pos,
            "domain": r1["domain"], "secondary_structure_uniprot": sse,
            "uniprot_binding_site": binding,
            "min_dist_to_Ap5A_1Z83_A": r1["min_dist_to_ligand_A"],
            "faces_1Z83": " ".join(x for x in (r1["closest_ligand_group"], r1["closest_ligand_half"]) if x),
            "min_dist_to_Ap4A_2C95_A": r2["min_dist_to_ligand_A"],
            "relative_sasa_1Z83": r1["relative_sasa"],
            "sidechain_polar_partners_1Z83": r1["sidechain_polar_partners"],
            "n_neighbour_residues_4A": r1["n_neighbour_residues_4A"],
            "alphafold_plddt": af["plddt"].get(str(pos)),
            "vertebrate_orthologs_identical": f"{c['orthologs_identical']}/{c['orthologs_n']}",
            "family_panel_identical": f"{c['family_identical']}/{c['family_n']}",
            "family_panel_residues": c["family_residues"],
            "gnomad_v4": popmap.get(v["cdna"], {"in_gnomad_v4": None}),
        }
        if v.get("class") == "missense":
            ref, alt = v["ref_aa"], v["alt_aa"]
            row["side_chain_volume_change_A3"] = round(VOLUME[alt] - VOLUME[ref], 1)
            row["charge_change"] = CHARGE.get(alt, 0) - CHARGE.get(ref, 0)
            am = af.get("alphamissense", {}).get(f"{ref}{pos}{alt}")
            row["alphamissense"] = {"score": am[0], "class": am[1]} if am else None
        if v.get("class") in ("frameshift", "nonsense"):
            row["native_residues_retained"] = v.get("residues_of_native_sequence_retained")
            row["stop_codon_number"] = v.get("stop_codon_number")
            row["nmd_predicted"] = v.get("nmd_predicted")
            lost = [f"{f['ligand']} {f['start']}" + (f"-{f['end']}" if f['end'] != f['start'] else "")
                    for f in feats if f["type"] == "BINDING" and f["end"] >= pos]
            row["uniprot_binding_sites_at_or_after_change"] = lost
        rows.append(row)
    # benign comparators: missense variants seen homozygous in gnomAD
    benign = []
    for m in pop["missense_with_homozygotes"]:
        p3 = m["hgvsp"]
        import re
        mm = re.fullmatch(r"p\.([A-Za-z]{3})(\d+)([A-Za-z]{3})", p3)
        from ak1_common import THREE
        one = {v: k for k, v in THREE.items()}
        ref, pos, alt = one[mm.group(1)], mm.group(2), one[mm.group(3)]
        r1 = s1[pos]; c = conserv["positions"][pos]
        am = af.get("alphamissense", {}).get(f"{ref}{pos}{alt}")
        benign.append({"protein": p3, "homozygotes": m["homozygotes"], "allele_frequency": m["allele_frequency"],
                       "domain": r1["domain"], "min_dist_to_Ap5A_1Z83_A": r1["min_dist_to_ligand_A"],
                       "relative_sasa_1Z83": r1["relative_sasa"],
                       "vertebrate_orthologs_identical": f"{c['orthologs_identical']}/{c['orthologs_n']}",
                       "family_panel_identical": f"{c['family_identical']}/{c['family_n']}",
                       "alphamissense": {"score": am[0], "class": am[1]} if am else None})
    dump({"disease_variants": rows, "homozygous_population_missense": benign}, "variant_table.json")

    lines = ["| cDNA (NM_000476.3) | Protein (computed) | Class | Domain | UniProt binding site | Dist. to Ap5A (A) | Faces | rSASA | Vertebrate orthologues identical | Family panel identical | AlphaMissense | gnomAD v4 AC/AN (hom) | Source |",
             "|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in rows:
        g = r["gnomad_v4"]
        gs = f"{g['allele_count']}/{g['allele_number']} ({g['homozygotes']})" if g.get("in_gnomad_v4") else "absent"
        am = r.get("alphamissense")
        ams = f"{am['score']:.2f} {am['class']}" if am else "n/a"
        lines.append(f"| {r['cdna']} | {r['computed_protein']} | {r['class']} | {r['domain']} | "
                     f"{'; '.join(r['uniprot_binding_site']) or '-'} | {r['min_dist_to_Ap5A_1Z83_A']} | {r['faces_1Z83']} | "
                     f"{r['relative_sasa_1Z83']} | {r['vertebrate_orthologs_identical']} | {r['family_panel_identical']} | "
                     f"{ams} | {gs} | {r['source']} |")
    lines += ["", "| Population missense seen homozygous | Homozygotes | AF | Domain | Dist. to Ap5A (A) | rSASA | Vertebrate orthologues identical | Family panel identical | AlphaMissense |",
              "|---|---|---|---|---|---|---|---|---|"]
    for b in benign:
        am = b["alphamissense"]
        lines.append(f"| {b['protein']} | {b['homozygotes']} | {b['allele_frequency']:.2e} | {b['domain']} | "
                     f"{b['min_dist_to_Ap5A_1Z83_A']} | {b['relative_sasa_1Z83']} | {b['vertebrate_orthologs_identical']} | "
                     f"{b['family_panel_identical']} | {(f'{am['score']:.2f} {am['class']}') if am else 'n/a'} |")
    (RESULTS / "variant_table.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))
    for r in rows:
        print(r["computed_protein"], "| partners:", r["sidechain_polar_partners_1Z83"], "| sse:", r["secondary_structure_uniprot"],
              "| vol", r.get("side_chain_volume_change_A3"), "chg", r.get("charge_change"),
              "| NMD", r.get("nmd_predicted"), "retained", r.get("native_residues_retained"), "| fam", r["family_panel_residues"])


if __name__ == "__main__":
    main()
