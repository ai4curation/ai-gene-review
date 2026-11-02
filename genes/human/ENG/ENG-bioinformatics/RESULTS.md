# ENG reproducible source-context analysis

The visible Python replay independently reconstructs 106 raw QuickGO records, 105 normal TSV rows and 104 seeded annotation objects. Source indices 14 and 75 retain two raw contexts each; the former has different dates/extensions and the latter different tissue/input extensions. None of those raw contexts is replaced by a fabricated new source assertion. Five NOT annotations and three `contributes_to` annotations are preserved.

Official human P17813-1 is 658 residues. Applying the recorded VSP_004233 substitution to its exact sequence reproduces the 625-residue P17813-2 FASTA. The signal peptide, mature-chain boundary and transmembrane segment remain separate processing/topology features. The computation does not assert equivalent cytoplasmic-tail functions or equate soluble experimental constructs to natural products.

The human PANTHER leaf's ungapped MSA sequence equals the official 658-residue sequence. Each of the three imported IBA annotations has an exact matching ancestral IBD on the target's path, including the original node and evidence set. This verifies ancestry and provenance; it does not settle the specific vasculogenesis-stage interpretation. Target self-evidence is legitimate and is not treated as circular.

Current Q63961 records are joined by exact term and negation to the imported mouse-derived annotations. These are present-day applicability checks, not recovered historical Ensembl or manual-transfer decisions. The source-specific mouse experiments and access gaps remain the basis of the scientific reviews.

ARBA00090009 has a sufficient first OR clause matching IPR058899, PTHR14002 and Euarchontoglires in the frozen human record. The other OR clauses are not asserted to match. The official target-matched HPA XML gives supported main plasma-membrane localization, and the SL-0039 mapping explicitly gives GO:0005886. These are inspected database assertions; no HPA image pixels were viewed.

Run the command in [README](README.md) to reproduce the full machine-readable result. `--check` compares independently computed results with the saved expectation. The script generates zero scientific annotation decisions and does not perform new sequence-function prediction or original-data reanalysis.
