#!/usr/bin/env python3
"""
Analyze functional regions of Epe1:
1. C-terminal HP1/Swi6 binding region
2. Detailed comparison with active JmjC demethylases
3. Identification of missing catalytic machinery
"""

from Bio import SeqIO
from pathlib import Path
import json
import matplotlib.pyplot as plt
import numpy as np
import re

from uniprot_features import ligand_residues, parse_uniprot_json, parse_uniprot_txt

EPE1_TXT = Path(__file__).parent.parent / "Epe1-uniprot.txt"

def load_epe1_data():
    """Load Epe1 sequence and UniProt data."""
    data_dir = Path("data")
    
    # Load sequence
    with open(data_dir / "epe1_spombe.fasta") as f:
        epe1_record = next(SeqIO.parse(f, "fasta"))
    
    # Load UniProt JSON
    with open(data_dir / "epe1_uniprot.json") as f:
        uniprot_data = json.load(f)
    
    return str(epe1_record.seq), uniprot_data

def analyze_c_terminal_region(sequence, uniprot_data):
    """Analyze the C-terminal region for HP1/Swi6 binding."""
    print("\nC-terminal Region Analysis (HP1/Swi6 binding):")
    print("-" * 50)
    
    # The C-terminal region is important for heterochromatin localization
    # Typically the last 100-150 amino acids
    c_term_150 = sequence[-150:]
    c_term_100 = sequence[-100:]
    c_term_50 = sequence[-50:]
    
    results = {}
    
    # Analyze different C-terminal segments
    for length, c_term in [(150, c_term_150), (100, c_term_100), (50, c_term_50)]:
        print(f"\n  Last {length} residues (positions {len(sequence)-length+1}-{len(sequence)}):")
        
        # Composition analysis
        hydrophobic = sum(1 for aa in c_term if aa in "FWYLMIVA")
        aromatic = sum(1 for aa in c_term if aa in "FWY")
        basic = sum(1 for aa in c_term if aa in "KRH")
        acidic = sum(1 for aa in c_term if aa in "DE")
        
        print(f"    Hydrophobic: {hydrophobic} ({hydrophobic*100/len(c_term):.1f}%)")
        print(f"    Aromatic: {aromatic} ({aromatic*100/len(c_term):.1f}%)")
        print(f"    Basic: {basic} ({basic*100/len(c_term):.1f}%)")
        print(f"    Acidic: {acidic} ({acidic*100/len(c_term):.1f}%)")
        
        # Look for potential motifs
        # HP1 binding often involves PxVxL-like motifs
        pxvxl_pattern = re.compile(r"P.V.L")
        matches = list(pxvxl_pattern.finditer(c_term))
        if matches:
            print(f"    PxVxL-like motifs: {len(matches)}")
            for match in matches:
                abs_pos = match.start() + len(sequence) - length + 1
                print(f"      - Position {abs_pos}: {match.group()}")
        
        # Look for leucine-rich regions (often involved in protein-protein interactions)
        leucine_rich = re.compile(r"L.{0,3}L.{0,3}L")
        l_matches = list(leucine_rich.finditer(c_term))
        if l_matches:
            print(f"    Leucine-rich regions: {len(l_matches)}")
        
        results[f"c_term_{length}"] = {
            "hydrophobic_percent": hydrophobic*100/len(c_term),
            "aromatic_percent": aromatic*100/len(c_term),
            "basic_percent": basic*100/len(c_term),
            "acidic_percent": acidic*100/len(c_term),
            "pxvxl_motifs": len(matches),
            "leucine_rich": len(l_matches)
        }
    
    # Check for known functional regions from UniProt
    print("\n  UniProt annotated regions:")
    if "features" in uniprot_data:
        for feature in uniprot_data["features"]:
            if feature.get("type") == "Region":
                location = feature.get("location", {})
                start = location.get("start", {}).get("value")
                end = location.get("end", {}).get("value")
                description = feature.get("description", "")
                
                # Check if it's in C-terminal region
                if start and start > len(sequence) - 200:
                    print(f"    {description}: {start}-{end}")
    
    return results

def compare_with_active_demethylases(epe1_seq):
    """Detailed comparison with active JmjC demethylases."""
    print("\nDetailed Comparison with Active JmjC Demethylases:")
    print("-" * 50)
    
    # JmjC domain boundaries and Fe(II) ligands from UniProt features:
    # Epe1 from its flat file, comparators from data/kdm*.json
    epe1_feats = parse_uniprot_txt(EPE1_TXT)
    records = {"Epe1": epe1_feats}
    for path in sorted(Path("data").glob("kdm*.json")):
        rec = parse_uniprot_json(path)
        if rec["jmjc"] is not None:
            records[rec["entry_name"]] = rec

    print("\n  Key catalytic residues in active demethylases:")
    print("  " + "-" * 45)
    
    comparison_data = {}
    for protein_name, rec in records.items():
        start, end = rec["jmjc"]
        analysis = analyze_jmjc_residues(rec["sequence"][start - 1:end], protein_name)
        analysis["jmjc"] = rec["jmjc"]
        analysis["fe_ligands"] = ligand_residues(rec)
        comparison_data[protein_name] = analysis

    # Print comparison table
    print("\n  Summary Table:")
    print("  " + "-" * 65)
    print(f"  {'Protein':<15} {'JmjC':<11} {'His':<5} {'K/S':<9} {'Fe ligands (UniProt)':<22}")
    print("  " + "-" * 65)

    for protein, data in comparison_data.items():
        dom = f"{data['jmjc'][0]}-{data['jmjc'][1]}"
        akg = f"{data['lysine_count']}/{data['serine_count']}"
        ligs = ", ".join(data["fe_ligands"]) or "none"
        print(f"  {protein:<15} {dom:<11} {data['histidine_count']:<5} {akg:<9} {ligs:<22}")

    return comparison_data

def analyze_jmjc_residues(jmjc_seq, protein_name):
    """Analyze key residues in JmjC domain."""
    analysis = {
        "protein": protein_name,
        "length": len(jmjc_seq),
        "histidine_count": jmjc_seq.count('H'),
        "lysine_count": jmjc_seq.count('K'),
        "serine_count": jmjc_seq.count('S'),
        "aspartate_count": jmjc_seq.count('D'),
        "glutamate_count": jmjc_seq.count('E'),
        "has_hxd_motif": False,
        "hxd_positions": []
    }
    
    # Check for HXD/HXE motifs
    hxd_pattern = re.compile(r"H.[DE]")
    matches = list(hxd_pattern.finditer(jmjc_seq))
    
    if matches:
        analysis["has_hxd_motif"] = True
        analysis["hxd_positions"] = [m.start() for m in matches]
    
    return analysis

def identify_missing_residues(epe1_jmjc, comparison_data):
    """Identify which critical residues are missing in Epe1."""
    print("\nMissing Catalytic Machinery in Epe1:")
    print("-" * 50)
    
    # Calculate average values from active demethylases
    active_proteins = [p for p in comparison_data.keys() if p != "Epe1" and p.startswith("KDM")]
    
    if active_proteins:
        avg_histidines = np.mean([comparison_data[p]["histidine_count"] for p in active_proteins])
        avg_lysines = np.mean([comparison_data[p]["lysine_count"] for p in active_proteins])
        
        epe1_data = comparison_data["Epe1"]
        
        print(f"\n  Epe1 vs Active Demethylases (average):")
        print(f"    Histidines: {epe1_data['histidine_count']} vs {avg_histidines:.1f}")
        print(f"    Lysines: {epe1_data['lysine_count']} vs {avg_lysines:.1f}")
        
        # Check specific positions
        print("\n  Critical residue analysis:")
        
        # Fe(II) ligands as annotated by UniProt for each protein
        print("    Fe(II) ligands (UniProt FT BINDING):")
        print(f"      Epe1: {', '.join(epe1_data['fe_ligands']) or 'none'}")
        for p in active_proteins:
            print(f"      {p}: {', '.join(comparison_data[p]['fe_ligands']) or 'none'}")

        # α-ketoglutarate binding
        print("    α-ketoglutarate binding:")
        if epe1_data["lysine_count"] >= 3:
            print(f"      ✓ Sufficient lysines present ({epe1_data['lysine_count']})")
        else:
            print(f"      ? Low lysine count ({epe1_data['lysine_count']})")
    
    return None

def create_visualization(comparison_data):
    """Create visualization of the analysis."""
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # Plot 1: Residue composition comparison
    proteins = list(comparison_data.keys())
    histidines = [comparison_data[p]["histidine_count"] for p in proteins]
    lysines = [comparison_data[p]["lysine_count"] for p in proteins]
    
    x = np.arange(len(proteins))
    width = 0.35
    
    ax1 = axes[0, 0]
    ax1.bar(x - width/2, histidines, width, label='Histidines', color='blue', alpha=0.7)
    ax1.bar(x + width/2, lysines, width, label='Lysines', color='green', alpha=0.7)
    ax1.set_xlabel('Protein')
    ax1.set_ylabel('Count')
    ax1.set_title('His and Lys counts in each UniProt JmjC domain')
    ax1.set_xticks(x)
    ax1.set_xticklabels(proteins, rotation=45, ha='right')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Highlight Epe1
    epe1_idx = proteins.index("Epe1")
    ax1.axvspan(epe1_idx - 0.5, epe1_idx + 0.5, alpha=0.2, color='red')
    
    # Plot 2: number of Fe(II) ligands each protein's UniProt entry annotates
    ax2 = axes[0, 1]
    n_fe = [len(comparison_data[p]["fe_ligands"]) for p in proteins]
    colors = ['red' if p == "Epe1" else 'green' for p in proteins]
    ax2.bar(range(len(proteins)), n_fe, color=colors, alpha=0.7)
    ax2.set_ylabel('Annotated Fe(II) ligands')
    ax2.set_title('Fe(II) ligands in UniProt FT BINDING')
    ax2.set_ylim([0, max(n_fe) + 1])
    ax2.set_xticks(range(len(proteins)))
    ax2.set_xticklabels(proteins, rotation=45, ha='right')
    ax2.grid(True, alpha=0.3)

    # Plot 3: Domain length comparison
    ax3 = axes[1, 0]
    lengths = [comparison_data[p]["length"] for p in proteins]
    colors = ['red' if p == "Epe1" else 'blue' for p in proteins]
    ax3.bar(range(len(proteins)), lengths, color=colors, alpha=0.7)
    ax3.set_ylabel('Domain Length (aa)')
    ax3.set_title('JmjC Domain Lengths')
    ax3.set_xticks(range(len(proteins)))
    ax3.set_xticklabels(proteins, rotation=45, ha='right')
    ax3.grid(True, alpha=0.3)
    
    # Plot 4: Summary text
    ax4 = axes[1, 1]
    ax4.axis('off')
    
    # Build summary based on actual analysis data
    epe1_data = comparison_data.get("Epe1", {})
    
    summary_lines = ["Computed from UniProt features:", ""]
    summary_lines.append(f"• Epe1 JmjC {epe1_data['jmjc'][0]}-{epe1_data['jmjc'][1]}")
    summary_lines.append(f"  Fe ligands: {', '.join(epe1_data['fe_ligands']) or 'none'}")
    comp_counts = [len(v["fe_ligands"]) for k, v in comparison_data.items() if k != "Epe1"]
    if comp_counts:
        summary_lines.append(f"• Comparators: {min(comp_counts)}-{max(comp_counts)} annotated Fe ligands")
    summary_lines.append("")
    summary_lines.append(f"• Epe1 JmjC histidines: {epe1_data.get('histidine_count', 0)}")
    summary_lines.append("")
    summary_lines.append("No activity verdict is drawn from sequence alone.")

    summary_text = "\n".join(summary_lines)
    
    ax4.text(0.1, 0.5, summary_text, fontsize=11, verticalalignment='center')
    
    plt.tight_layout()
    
    # Save figure
    results_dir = Path("results")
    results_dir.mkdir(exist_ok=True)
    fig_path = results_dir / "epe1_analysis_summary.png"
    plt.savefig(fig_path, dpi=300, bbox_inches='tight')
    print(f"\n✓ Visualization saved to {fig_path}")
    
    return fig_path

def main():
    print("=" * 60)
    print("Functional Regions Analysis of Epe1")
    print("=" * 60)
    
    # Load data
    epe1_seq, uniprot_data = load_epe1_data()
    print(f"\nEpe1 protein length: {len(epe1_seq)} aa")
    
    # 1. Analyze C-terminal region
    c_term_results = analyze_c_terminal_region(epe1_seq, uniprot_data)
    
    # 2. Compare with active demethylases
    comparison_data = compare_with_active_demethylases(epe1_seq)
    
    # 3. Identify missing residues
    identify_missing_residues(None, comparison_data)
    
    # 4. Create visualization
    fig_path = create_visualization(comparison_data)
    
    # 5. Save detailed results
    results_dir = Path("results")
    results_dir.mkdir(exist_ok=True)
    
    results_file = results_dir / "functional_regions_analysis.txt"
    with open(results_file, "w") as f:
        f.write("Functional Regions Analysis of Epe1\n")
        f.write("=" * 60 + "\n\n")
        
        f.write("1. JmjC Domain Analysis (UniProt features):\n")
        f.write("-" * 40 + "\n")
        epe1_data = comparison_data["Epe1"]
        f.write(f"Position: {epe1_data['jmjc'][0]}-{epe1_data['jmjc'][1]} ({epe1_data['length']} aa)\n")
        f.write(f"Histidines: {epe1_data['histidine_count']}\n")
        f.write(f"Fe(II) ligands (FT BINDING): {', '.join(epe1_data['fe_ligands']) or 'none'}\n")
        f.write("\n2. C-terminal Region Analysis:\n")
        f.write("-" * 40 + "\n")
        c100 = c_term_results["c_term_100"]
        f.write(f"Last 100 residues:\n")
        f.write(f"  Hydrophobic: {c100['hydrophobic_percent']:.1f}%\n")
        f.write(f"  Basic: {c100['basic_percent']:.1f}%\n")
        f.write(f"  Acidic: {c100['acidic_percent']:.1f}%\n")
        f.write(f"  PxVxL motifs: {c100['pxvxl_motifs']}\n")
        f.write(f"  Leucine-rich regions: {c100['leucine_rich']}\n")
        
        f.write("\n3. Comparison with Active Demethylases (UniProt features):\n")
        f.write("-" * 40 + "\n")
        for protein, data in comparison_data.items():
            f.write(f"{protein}: JmjC {data['jmjc'][0]}-{data['jmjc'][1]}; "
                    f"histidines {data['histidine_count']}; "
                    f"Fe ligands {', '.join(data['fe_ligands']) or 'none'}\n")
        comp = [len(v["fe_ligands"]) for k, v in comparison_data.items() if k != "Epe1"]
        if comp:
            f.write(f"\nAnnotated Fe(II) ligands: Epe1 {len(epe1_data['fe_ligands'])}; "
                    f"comparators {min(comp)}-{max(comp)}.\n")
        f.write("\nC-terminal composition is reported above; it is not by itself\n")
        f.write("evidence of HP1/Swi6 binding (Raiymbek et al. 2020 map the Swi6 site to 434-600).\n")

    print(f"\n✓ Detailed results saved to {results_file}")

if __name__ == "__main__":
    main()