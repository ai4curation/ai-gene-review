# PP_1348 curation notes

- Q88N67 is a MutT-family Nudix hydrolase with explicit 8-oxo-GTP and
  8-oxo-dGTP hydrolysis reactions
  [file:PSEPK/PP_1348/PP_1348-uniprot.txt,
  "Reaction=8-oxo-dGTP + H2O = 8-oxo-dGMP + diphosphate + H(+)"]
- The two substrate-specific pyrophosphatase terms are accepted. Broad DNA
  repair is retained as non-core because nucleotide-pool sanitation prevents
  incorporation of damaged precursors rather than repairing DNA directly.
- Direct KT2440 biochemical or mutation-spectrum evidence remains absent.
- **The C-terminal half of the protein is unassessed.** Q88N67 is
  [file:PSEPK/PP_1348/PP_1348-uniprot.txt, "SQ   SEQUENCE   314 AA;"] long, but
  UniProt scopes the Nudix module to the N-terminal third
  [file:PSEPK/PP_1348/PP_1348-uniprot.txt, "FT   DOMAIN          1..129"], and all
  eight annotated substrate/Mg2+ binding residues fall inside that domain. The
  remainder carries a second, unrelated fold: a thiamine-phosphate-synthase/TenI
  TIM barrel
  [file:PSEPK/PP_1348/PP_1348-uniprot.txt, "DR   CDD; cd00564; TMP_TenI; 1."],
  [file:PSEPK/PP_1348/PP_1348-uniprot.txt, "DR   Pfam; PF02581; TMP-TENI; 1."],
  [file:PSEPK/PP_1348/PP_1348-uniprot.txt, "DR   SUPFAM; SSF51391; Thiamin phosphate synthase; 1."],
  [file:PSEPK/PP_1348/PP_1348-uniprot.txt, "DR   InterPro; IPR022998; ThiamineP_synth_TenI."],
  with the ThiE eggNOG group present alongside the Nudix one
  [file:PSEPK/PP_1348/PP_1348-uniprot.txt, "DR   eggNOG; COG0352; Bacteria."],
  [file:PSEPK/PP_1348/PP_1348-uniprot.txt, "DR   eggNOG; COG0494; Bacteria."].
  Every GOA molecular-function annotation on Q88N67 traces to Nudix/MutT
  signatures, so the TIM-barrel domain has no annotation of any kind. The two
  accepted pyrophosphatase activities are not in doubt; what is missing is any
  assessment of whether PP_1348 is bifunctional. No candidate activity is
  asserted here because no evidence addresses the domain - it is recorded as a
  `suggested_questions` entry instead, and it deserves a `knowledge_gaps` entry
  in the module, where PP_1348 is the MutT representative.
