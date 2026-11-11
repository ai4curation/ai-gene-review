# SCO2678 (Q9L243) sequence re-review, 2026-10-20

Script: `motif_scan_rereview.py` (raw output in `motif_scan_rereview.out`), run on the
171-aa sequence in the cached UniProt record. Domain data were taken from the InterPro
REST API (`/entry/all/protein/uniprot/Q9L243`) and KEGG REST (`get sco:SCO2675..SCO2681`)
on 2026-10-20.

## Domain and family placement

- InterPro returns a single signature for Q9L243: Pfam PF18143 (HAD_SAK_2, "HAD domain in Swiss Army Knife RNA repair proteins"), residues 9-155. No InterPro entry, no PANTHER family/subfamily, no CATH/SUPERFAMILY or NCBIfam signature is integrated for this protein.
- No PANTHER family is listed, so there is no PAINT node and no IBA-backed placement for this protein.
- The Pfam family description: Family of HAD domain phophoesterases observed in large eukaryotic proteins with predicted role in RNA repair. The founding paper (PMID:27536007) defines it from eukaryotic multidomain proteins and describes it as a previously uncharacterized HAD family; no member is experimentally characterized.
- eggNOG assigns COG1877; NCBI COG names COG1877 Trehalose-6-phosphate phosphatase (OtsB). NCBI's own COG database has no assignment for SCO2678. OtsB proteins are about 260 aa with a cap domain; SCO2678 is 171 aa and carries only the PF18143 HAD core, so this eggNOG assignment is a distant superfamily-level grouping and is not used to transfer trehalose-6-phosphate phosphatase activity.

## HAD catalytic motifs (positions in Q9L243)

| Motif | Expected | Found |
|---|---|---|
| I | hhhDxD (nucleophile Asp + acid/base Asp) | LLFL**D13**V**D15**GP (residues 9-17) |
| II | hhhh(S/T) | VWA**T67**T68 (residues 64-68) |
| III | Lys | K106 (GLHW**K106**TRP) |
| IV | hhh(D/G)D (Mg2+ ligands) | FIWV**D123D124** (residues 119-124) |

All four core HAD motifs are present in the expected N-to-C order with typical spacing, so the protein is predicted to retain the aspartyl-phosphate HAD phosphoryl-transfer mechanism. This is a prediction from motif conservation, not an activity measurement.

## Export signals

- Maximum 15-residue Kyte-Doolittle mean over the N-terminal region is 1.18 (start residue 9), below the values typical of a signal-peptide h-region; the N-terminus is MTSSSERPLLFLDVDGPLIPF.
- No twin-arginine (RR) motif and no lipobox in the N-terminus; motif I (D13/D15) lies inside the region a signal peptide would occupy.
- Conclusion: no evidence for export; the "Secreted protein" name in UniProt is a machine-generated label (ECO:0008006) and is not supported by the sequence.

## Genomic context (KEGG)

SCO2678 (forward strand, 2918653..2919168) is flanked by SCO2677 (EttA-like ABC ATPase,
complement strand) and SCO2679 (putative lipoprotein, complement strand); further
downstream lie SCO2680 (TIR_2) and SCO2681 (NB-ARC/TPR STAND NTPase). No RNA ligase,
polynucleotide kinase, or other RNA-repair gene is adjacent, so the neighbourhood does
not corroborate an RNA-repair role. The strand arrangement does not suggest a shared
operon with either neighbour.
