# PCSK9 review notes

Deep research: the client reported a timeout after 600 s on 2026-10-09, so the review was done
manually from the GOA-cited publications cached in `publications/` and the UniProt record. The
provider in fact finished (run ended 2026-10-09T16:38) and `PCSK9-deep-research-falcon.md` was
written afterwards. It was checked against this review on 2026-10-11:

- It reaches the same two-part conclusion as the review's two core functions: the highest-
  confidence annotation is secreted regulator of LDLR endosomal trafficking and lysosomal
  degradation, and the only demonstrable enzymatic specificity is autocatalytic cleavage of
  pro-PCSK9 at VFAQ152/SIP153 during maturation. It is explicit that PCSK9 does not need to
  cleave LDLR, and that "proprotein convertase" must not be read as evidence that it digests
  LDLR proteolytically. That supports keeping protease-substrate process terms off this gene.
- It confirms the EGF-A interface sits on a surface of the subtilisin-like domain away from the
  catalytic site (Kwon et al. 2.4 A structure), that binding is calcium-dependent and about
  threefold stronger at pH 6 than pH 7, and that the retained prodomain occludes the active
  site in the secreted protein. This matches core function 1.
- It agrees that VLDLR and ApoER2 degradation is real but of uncertain human physiological
  weight, which is how the review grades those rows (secondary, not core).
- It notes furin cleavage near Arg218 as an inactivating second processing route, distinct from
  the activating autocleavage. The review treats the furin/PC5-6A row as a separate claim about
  PCSK9 as a substrate, not as its own catalytic activity, which is consistent.
- It adds the ARH dependence caveat: clathrin heavy chain is required for PCSK9-mediated LDLR
  degradation, while ARH was required in hepatocytes and lymphocytes but not fibroblasts, and
  ubiquitination, proteasome, macroautophagy and the tested ESCRT components were not. No
  annotation in this review depends on those, and it supports the review's caution about the
  intracellular trans-Golgi route relative to the circulating-PCSK9 route.

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
