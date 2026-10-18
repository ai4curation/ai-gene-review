#!/usr/bin/env python3
"""
Analyze structural features of Epe1 JmjC domain.
Predict secondary structure and identify key structural elements.
"""

from Bio import SeqIO
from pathlib import Path
import requests
import json
import matplotlib.pyplot as plt
import numpy as np

from uniprot_features import ligand_residues, parse_uniprot_txt

EPE1_TXT = Path(__file__).parent.parent / "Epe1-uniprot.txt"

def predict_secondary_structure(sequence):
    """
    Simple secondary structure prediction based on amino acid propensities.
    This is a simplified method - ideally would use more sophisticated tools.
    """
    # Chou-Fasman propensities (simplified)
    helix_formers = set("AELMQK")
    helix_breakers = set("PGNDS")
    sheet_formers = set("VFIYW")
    sheet_breakers = set("PEGDK")
    
    structure = []
    window_size = 5
    
    for i in range(len(sequence)):
        window_start = max(0, i - window_size // 2)
        window_end = min(len(sequence), i + window_size // 2 + 1)
        window = sequence[window_start:window_end]
        
        helix_score = sum(1 for aa in window if aa in helix_formers) - sum(1 for aa in window if aa in helix_breakers)
        sheet_score = sum(1 for aa in window if aa in sheet_formers) - sum(1 for aa in window if aa in sheet_breakers)
        
        if helix_score > sheet_score and helix_score > 0:
            structure.append('H')  # Helix
        elif sheet_score > 0:
            structure.append('E')  # Sheet
        else:
            structure.append('C')  # Coil
    
    return ''.join(structure)

def analyze_jmjc_structural_features(jmjc_seq, jmjc_start):
    """Analyze structural features of JmjC domain."""
    print("\nStructural Features of Epe1 JmjC Domain:")
    print("-" * 50)
    
    # Secondary structure prediction
    ss_pred = predict_secondary_structure(jmjc_seq)
    
    helix_count = ss_pred.count('H')
    sheet_count = ss_pred.count('E')
    coil_count = ss_pred.count('C')
    
    print(f"\n  Predicted secondary structure composition:")
    print(f"    α-helix: {helix_count} ({helix_count*100/len(ss_pred):.1f}%)")
    print(f"    β-sheet: {sheet_count} ({sheet_count*100/len(ss_pred):.1f}%)")
    print(f"    Coil/loop: {coil_count} ({coil_count*100/len(ss_pred):.1f}%)")
    
    # Identify β-strands (characteristic of JmjC fold)
    # JmjC domains typically have 8 β-strands forming a β-barrel
    beta_regions = []
    in_beta = False
    start = 0
    
    for i, ss in enumerate(ss_pred):
        if ss == 'E' and not in_beta:
            in_beta = True
            start = i
        elif ss != 'E' and in_beta:
            in_beta = False
            if i - start >= 3:  # Minimum length for β-strand
                beta_regions.append((start, i))
    
    print(f"\n  Predicted β-strands: {len(beta_regions)}")
    if beta_regions:
        print("    Positions:")
        for i, (start, end) in enumerate(beta_regions[:8], 1):  # Show first 8
            print(f"      β{i}: {start+jmjc_start}-{end+jmjc_start} ({end-start} aa)")
    
    # Check for metal-binding pocket characteristics
    print("\n  Metal-binding pocket analysis:")
    
    # Look for histidines and their spacing
    histidine_positions = [i for i, aa in enumerate(jmjc_seq) if aa == 'H']
    
    if len(histidine_positions) >= 2:
        print(f"    Histidine positions: {[p+jmjc_start for p in histidine_positions]}")
        
        # Check spacing between histidines
        if len(histidine_positions) >= 2:
            spacings = [histidine_positions[i+1] - histidine_positions[i] 
                       for i in range(len(histidine_positions)-1)]
            print(f"    Spacing between histidines: {spacings}")
            
            # Typical Fe(II) coordination requires His residues ~15-25 aa apart
            good_spacing = any(15 <= s <= 30 for s in spacings)
            if good_spacing:
                print("    ✓ Histidine spacing compatible with Fe(II) coordination")
            else:
                print("    ✗ Unusual histidine spacing for Fe(II) coordination")
    
    # Hydrophobic core analysis
    hydrophobic_core = sum(1 for aa in jmjc_seq if aa in "VLIMFYW")
    print(f"\n  Hydrophobic core residues: {hydrophobic_core} ({hydrophobic_core*100/len(jmjc_seq):.1f}%)")
    
    return {
        "helix_percent": helix_count*100/len(ss_pred),
        "sheet_percent": sheet_count*100/len(ss_pred),
        "beta_strands": len(beta_regions),
        "histidine_positions": histidine_positions,
        "hydrophobic_percent": hydrophobic_core*100/len(jmjc_seq)
    }

def compare_structural_features():
    """Compare structural features with known JmjC structures."""
    print("\nComparison with Known JmjC Structures:")
    print("-" * 50)
    
    # Typical JmjC domain features (from literature/PDB structures)
    typical_features = {
        "beta_strands": "8 (forming β-barrel)",
        "alpha_helices": "2-4 surrounding β-barrel",
        "Fe_coordination": "HX(D/E)...H motif",
        "aKG_binding": "Basic pocket (K/R)",
        "fold": "Double-stranded β-helix (DSBH)"
    }
    
    print("\n  Canonical JmjC domain features:")
    for feature, description in typical_features.items():
        print(f"    {feature}: {description}")
    
    # Epe1's Fe(II) site, read from UniProt features rather than a motif search
    feats = parse_uniprot_txt(EPE1_TXT)
    print("\n  Epe1 Fe(II) site (UniProt FT BINDING, Fe ligand):")
    print(f"    Annotated ligands: {', '.join(ligand_residues(feats))}")
    for pos, expected, found in feats["caution_positions"]:
        print(f"    CC CAUTION: catalytic {expected} at {pos} replaced by {found}"
              f" (sequence has {feats['sequence'][pos - 1]} at {pos})")

def visualize_domain_architecture():
    """Create a visual representation of Epe1 domain architecture."""
    # Load Epe1 sequence
    from pathlib import Path
    from Bio import SeqIO
    with open(Path("data") / "epe1_spombe.fasta") as f:
        for record in SeqIO.parse(f, "fasta"):
            epe1_seq = str(record.seq)
            break
    
    feats = parse_uniprot_txt(EPE1_TXT)
    jmjc_start, jmjc_end = feats["jmjc"]
    protein_length = len(epe1_seq)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 8))

    # Only the UniProt-annotated JmjC domain is drawn as a domain; the flanking
    # regions are unannotated sequence, not assigned functions.
    domains = [
        {"name": "N-terminal region", "start": 1, "end": jmjc_start - 1, "color": "lightgray"},
        {"name": "JmjC (UniProt)", "start": jmjc_start, "end": jmjc_end, "color": "lightblue"},
        {"name": "C-terminal region", "start": jmjc_end + 1, "end": protein_length, "color": "lightgray"},
    ]

    ax1.set_xlim(0, protein_length)
    ax1.set_ylim(0, 1)
    for domain in domains:
        width = domain["end"] - domain["start"]
        rect = plt.Rectangle((domain["start"], 0.3), width, 0.4,
                             facecolor=domain["color"], edgecolor='black', linewidth=1)
        ax1.add_patch(rect)
        mid = (domain["start"] + domain["end"]) / 2
        ax1.text(mid, 0.5, domain["name"], ha='center', va='center', fontsize=10)

    ax1.set_xlabel("Amino acid position")
    ax1.set_title(f"Epe1 ({feats['accession']}) domain architecture from UniProt features")
    ax1.set_yticks([])
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    ax1.spines['left'].set_visible(False)

    # JmjC detail: mark each annotated position with the residue actually present
    ax2.set_xlim(jmjc_start, jmjc_end)
    ax2.set_ylim(0, 1)
    marks = [(p, "Fe ligand", "tab:blue") for p in feats["fe_ligands"]]
    marks += [(p, f"binding: {lig}", "tab:green") for p, lig in feats["binding"]
              if p not in feats["fe_ligands"]]
    marks += [(p, f"CAUTION: {exp}->{fnd}", "tab:orange") for p, exp, fnd in feats["caution_positions"]]
    marks += [(p, "MUTAGEN", "tab:purple") for p, _ in feats["mutagen"]]
    for i, (pos, label, color) in enumerate(sorted(marks)):
        residue = epe1_seq[pos - 1]
        y = 0.25 + 0.12 * (i % 5)
        ax2.axvline(x=pos, color=color, linestyle='--', alpha=0.6)
        ax2.text(pos, y, f"{residue}{pos}\n{label}", ha='center', fontsize=7, color=color)
    ax2.set_xlabel("Amino acid position")
    ax2.set_title(f"JmjC domain detail ({jmjc_start}-{jmjc_end}): UniProt BINDING, CAUTION and MUTAGEN positions")
    ax2.set_yticks([])
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    ax2.spines['left'].set_visible(False)
    
    plt.tight_layout()
    
    # Save figure
    results_dir = Path("results")
    fig_path = results_dir / "epe1_domain_architecture.png"
    plt.savefig(fig_path, dpi=300, bbox_inches='tight')
    print(f"\n✓ Domain architecture figure saved to {fig_path}")
    
    return fig_path

def main():
    print("=" * 60)
    print("Structural Features Analysis")
    print("=" * 60)
    
    data_dir = Path("data")
    results_dir = Path("results")
    results_dir.mkdir(exist_ok=True)
    
    # Load Epe1 sequence
    with open(data_dir / "epe1_spombe.fasta") as f:
        epe1_record = next(SeqIO.parse(f, "fasta"))
    
    epe1_seq = str(epe1_record.seq)
    
    # JmjC domain boundaries from the UniProt FT DOMAIN feature
    feats = parse_uniprot_txt(EPE1_TXT)
    jmjc_start, jmjc_end = feats["jmjc"]
    jmjc_seq = epe1_seq[jmjc_start-1:jmjc_end]

    print(f"\nAnalyzing JmjC domain (positions {jmjc_start}-{jmjc_end})")
    print(f"Length: {len(jmjc_seq)} aa")
    
    # Analyze structural features
    structural_features = analyze_jmjc_structural_features(jmjc_seq, jmjc_start)
    
    # Compare with known structures
    compare_structural_features()
    
    # Create visualization
    visualize_domain_architecture()
    
    # Save results
    results_file = results_dir / "structural_analysis.txt"
    with open(results_file, "w") as f:
        f.write("Structural Features Analysis\n")
        f.write("=" * 60 + "\n\n")
        
        f.write("JmjC Domain Structural Features:\n")
        f.write(f"- Position: {jmjc_start}-{jmjc_end}\n")
        f.write(f"- Length: {len(jmjc_seq)} aa\n")
        f.write(f"- Predicted α-helix: {structural_features['helix_percent']:.1f}%\n")
        f.write(f"- Predicted β-sheet: {structural_features['sheet_percent']:.1f}%\n")
        f.write(f"- Predicted β-strands: {structural_features['beta_strands']}\n")
        f.write(f"- Hydrophobic core: {structural_features['hydrophobic_percent']:.1f}%\n")
        
        f.write("\nUniProt-annotated active-site features:\n")
        f.write(f"- Fe(II) ligands (FT BINDING): {', '.join(ligand_residues(feats))}\n")
        for pos, expected, found in feats["caution_positions"]:
            f.write(f"- CC CAUTION: catalytic {expected} at {pos} replaced by {found} "
                    f"(sequence has {epe1_seq[pos - 1]} at {pos})\n")
        f.write("\nNote: secondary-structure values are a crude Chou-Fasman-style\n")
        f.write("propensity estimate; no conclusion about fold or activity is drawn\n")
        f.write("from them.\n")

    print(f"\n✓ Results saved to {results_file}")

if __name__ == "__main__":
    main()