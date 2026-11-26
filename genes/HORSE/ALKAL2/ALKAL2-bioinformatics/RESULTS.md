# Horse ALKAL2 (F6XWZ3) gene-model comparison

Script: `compare_gene_models.py` (PEP 723; run with `uv run --script compare_gene_models.py`).
Raw output: `compare_gene_models_output.txt`. Inputs: UniProt flat files for horse F6XWZ3
(gene folder), the three other horse ALKAL2 entries (A0A3Q2I4Q6, A0A9L0SHF3, A0A3Q2L2L8),
human ALKAL2 (Q6UX46) and human ALKAL1 (Q6UXT8), downloaded from rest.uniprot.org on 2026-10-21.

## Gene models

All four horse entries come from one Ensembl gene, ENSECAG00000029965 (chromosome 15).
Ensembl marks transcript ENSECAT00000009339 (protein ENSECAP00000007098 = F6XWZ3, 271 aa)
as canonical. A0A3Q2I4Q6 (152 aa) is the model that matches RefSeq XP_001503231.2 and the
human product length (152 aa).

- A0A3Q2I4Q6 found in F6XWZ3 at residue 120 (F6XWZ3 N-terminal extension = 119 residues).
- The 119-residue extension is 65% Arg/Gly/Ala/Pro and has no counterpart in human ALKAL2
  (whose residue 1 is the initiator Met of the signal peptide). In F6XWZ3 the hydrophobic
  signal-peptide segment (MRGPGRPLLLGLLLVLGAAG...) therefore starts at Met120 rather than at
  the N-terminus.
- A0A9L0SHF3 (261 aa) carries the same extension and a C-terminus that diverges after the
  ...CTIPA motif (CLLKSVRRCER instead of YYKRCARLLTRLAVSPVCMEG), so the human C134/C147
  disulfide positions are not conserved in register: the augmentor domain is disrupted.
- A0A3Q2L2L8 (197 aa) carries a shorter, different upstream extension.

## Alignment to human

- F6XWZ3 vs human_ALKAL2_Q6UX46: query 120-270, ref 1-149, identity 129/149 = 86.6%
- F6XWZ3 vs human_ALKAL1_Q6UXT8: query 123-270, ref 6-128, identity 73/117 = 62.4%
  (so F6XWZ3 is the ALKAL2 ortholog, not ALKAL1, consistent with PANTHER PTHR28676:SF2).
- The four augmentor-domain cysteines forming the two intramolecular disulfides of human
  ALKAL2 (C111-C147, C125-C134) are conserved in F6XWZ3 (C232, C246, C255, C268).
- Human C66 (the primate-specific interchain disulfide cysteine) aligns to Tyr186 in F6XWZ3:
  horse ALKAL2 lacks the dimerizing cysteine, as expected for a non-primate.

## Interpretation

F6XWZ3 is the full ALKAL2 coding sequence (augmentor domain intact) preceded by an in-frame
119-residue N-terminal extension that is most likely an annotation artefact (upstream
start codon/exon in the Ensembl model). The functional product is expected to be the
152-aa protein represented by A0A3Q2I4Q6, i.e. F6XWZ3 residues 120-271.
