# PCSK9 review notes

Deep research: `just deep-research-falcon human PCSK9` was attempted on 2026-10-09 and failed
(provider timed out after 600 s). The review was done manually from the GOA-cited publications
cached in `publications/` and the UniProt record.

## Core biology (with provenance)

- Autocatalytic intramolecular prodomain cleavage [PMID:14622975 "Narc 1 undergoes autocatalytic
  intramolecular processing at the site LVFAQ/, resulting in the cleavage of its prosegment and the
  generation of an active proteinase"]
- Binding to LDLR EGF-A, pH dependence, recycling block and lysosomal rerouting [PMID:17452316
  "Recombinant human PCSK9 interacted in a sequence-specific manner with the first epidermal growth
  factor-like repeat (EGF-A) in the EGF homology domain of the human LDLR."; "As a consequence, the
  LDLR is rerouted from the endosome to the lysosome where it is degraded."]
- Secreted PCSK9 acts from plasma [PMID:17080197 "We conclude that secreted PCSK9 associates with the
  LDLR and reduces hepatic LDLR protein levels."]
- LDLR-family degradation is non-catalytic [PMID:18039658 "Such PCSK9-induced degradation does not
  require its catalytic activity."]
- Plasma PCSK9 associates with LDL/HDL but not VLDL [PMID:18197702 "When PCSK9 protein was incubated
  with total serum, it partially associated with LDL and HDL but not with VLDL."] - used to remove
  the ortholog-transferred VLDL particle binding annotation.
- Loss-of-function lowers LDL-C [PMID:17170371 "In African-Americans two nonsense mutations resulting
  in loss of function of PCSK9 are associated with a 30% to 40% reduction of plasma low-density
  lipoprotein cholesterol."]

## Curation decisions worth flagging

- Core MF is LDL particle receptor binding (GO:0050750), not peptidase activity: the serine
  endopeptidase activity is real but self-directed (autoprocessing), and LDLR degradation is
  catalysis-independent.
- GO:0032802 LDL receptor catabolic process modified to GO:0032805 positive regulation of it.
- UNDECIDED: GO:0002091 (PMID:18799458) and GO:0141110 (PMID:16912035), abstract-only, basis not
  verifiable.
- Development terms derived from expression patterns (PMID:12552133) marked over-annotated.

## Disease alignment

dismech `Autosomal_Dominant_Hypercholesterolemia_3` (gain of function) now binds the PCSK9-LDLR
binding node to GO:0050750 with modifier INCREASED (allele-specific: D374Y), and its LDLR
catabolism node to GO:0032802 INCREASED - consistent with core function 1 here.
