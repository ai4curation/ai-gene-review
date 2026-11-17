# proB (Q88Q07) — Pseudomonas putida KT2440 glutamate 5-kinase

## Summary

proB (PP_0691) encodes the reviewed cytoplasmic glutamate 5-kinase (EC 2.7.2.11)
that catalyzes the first committed step of L-proline biosynthesis: ATP-dependent
phosphorylation of L-glutamate to L-glutamyl 5-phosphate. The acyl-phosphate
product is subsequently reduced by ProA to L-glutamate 5-semialdehyde, which
cyclizes non-enzymatically to P5C (glutamate-to-P5C branch).

- Reaction: L-glutamate + ATP = L-glutamyl 5-phosphate + ADP
  [file:PSEPK/proB/proB-uniprot.txt "Reaction=L-glutamate + ATP = L-glutamyl 5-phosphate + ADP"]
- Pathway: Amino-acid biosynthesis; L-proline biosynthesis
  [file:PSEPK/proB/proB-uniprot.txt "PATHWAY: Amino-acid biosynthesis; L-proline biosynthesis"]
- Localization: Cytoplasm
  [file:PSEPK/proB/proB-uniprot.txt "SUBCELLULAR LOCATION: Cytoplasm"]

## PUA domain and the RNA-binding over-annotation

ProB carries a C-terminal PUA domain (UniProt FT DOMAIN 280..358; InterPro
IPR002478 / IPR036974; Pfam PF01472; HAMAP-Rule MF_00456). In glutamate
5-kinase this PUA domain is an allosteric proline-feedback regulatory module,
not a nucleic-acid-binding element.

The IEA annotation GO:0003723 (RNA binding; DR GO;GO:0003723; F:RNA binding;
IEA:InterPro; GO_REF:0000002) is propagated purely from the PUA domain signature.
PUA -> RNA-binding is a well-known over-propagated InterPro inference for
metabolic ProB proteins, and there is no evidence that ProB binds RNA in vivo.
Initially marked MARK_AS_OVER_ANNOTATED; changed to REMOVE (2026-11-02) so the
row matches the same PUA-derived IEA in the E. coli proB review, which removes
it on the basis of the E. coli ProB PUA-dissection and structure papers
[PMID:16337196 "We propose that the PUA domain modulates the function of the AAK domain"].

## 2026-11-02 completion pass (module bacterial_glutamate_to_p5c_biosynthesis)

- No gene-level deep-research provider file exists for Q88Q07 and no provider
  API keys were available in this session; the review rests on the reviewed
  UniProt record, the PTHR43654 PAINT data and the experimentally grounded
  E. coli ProB ortholog (genes/ECOLI/proB). No Q88Q07-specific experimental
  literature was found in the cached publications.
- Cytosol (TreeGrafter IEA) changed from KEEP_AS_NON_CORE to ACCEPT: it is the
  compartment where the kinase acts and matches the PTN000115542 cytosol IBD
  and the E. coli proB review.
- GOA for Q88Q07 carries no IBA rows in the current snapshot; the module's
  phylogenetic grounding uses PTN000115542 from the committed PAINT slice.


## 2026-11-07 evidence re-audit

All original annotation payloads and row order are preserved. No NEW annotation was added. The catalytic reaction and proline-biosynthetic participation remain supported. KT2440 chemistry and localization are conserved-role inferences supported by curated HAMAP, not newly identified target assays.

The normal Falcon research attempt failed with HTTP 403 authentication/access error; no provider report was fabricated. Manual source review used the protected existing caches and normally fetched new publications.

PMID:39514317 (full text) challenges required ProA–ProB channeling: heterologous kinase replacements and overexpressed alternative reductases support E. coli growth; failed crosslinking alone is not universal proof of no interaction. ProA is reduced glutamyl-phosphate chemistry; spontaneous GSA cyclization supplies P5C. The computed GP half-life and diffusion times are calculations, not intracellular measurements. Native-locus monomeric-GFP fusions show dispersed cytoplasmic localization. Expression/purification used engineered BL21 derivatives, while growth experiments used K-12 BW25113 derivatives. No matched-protein complex requirement is imposed.

PMID:37511294 (full text) overturns the previous claim that no ProB binds RNA. K-12 ASKA-derived proB was recloned into pET21a with C-terminal His tag, expressed in BL21-Gold(DE3), and tested by SELEX/competition EMSA. Estimated KD >>10 micromolar, no mapped binding site, no established native target or RNA-regulatory function. The KT2440 RNA-binding row is UNDECIDED; E. coli binding neither proves nor excludes this target transfer.

Existing abstract-only primary caches were not refreshed. Curated experimental annotations remain supported where independent evidence agrees; no target-table detail was invented. Complete validation, ontology snapshots and preservation proof are in the member-review audit and ignored existing-review logs.


## PR6160 evidence follow-up (2026-11-07 UTC)

Re-read full PMID:37511294 and the InterPro provenance. Retained RNA-binding UNDECIDED: direct E. coli SELEX/competition EMSA is positive but weak, the PUA binding site was not mapped, and this target was not assayed. Accessibility of that paper does not resolve cross-species conservation; no physiological role is required merely to establish binding. This is an InterPro IEA, not a PAINT RNA assertion.
