# IRAK2 notes

## Literature search (2026-11-04)

No deep-research provider was available. Sources checked:

- UniProt O43187 flat file (FUNCTION, SUBUNIT, DOMAIN, CAUTION).
- All GOA-cited publications cached via `just fetch-gene-pmids human IRAK2` (14 PMIDs; full text for
  18636090, 20485341, 21903422, 21988832, 28514442, 33961781, 36865541, 38605168, 38961291; abstract
  only for 10383454, 11544529, 17878161, 30256449, 9374458).
- Reactome cached entries for the TAS rows; sibling reviews IRAK1, IRAK4, MYD88. Context only, not
  evidence: GO-CAM gomodel:59cc772c00000000 (IL-1 signalling module/GO-CAM review proposed in
  ai4curation/ai-gene-review#5904).

Queries (grep over cached text): "IRAK2", "IRAK-2", "kinase activity", "autophosphorylat",
"NLRP3", "inflammasome", "caspase-1", "nucle", "mitochond".

## Findings

- Myddosome component: IRAK2 death domain binds the MyD88-IRAK4 DD assembly, forming the top layer
  [PMID:20485341 "Instead, IRAK2 DD interacts with the MyD88: IRAK4 complex."];
  [PMID:20485341 "It contains approximately four layers, with MyD88 at the bottom two layers, IRAK4 in the middle layer and IRAK2 at the top layer."].
- Phosphorylated by IRAK4, then engages TRAF6
  [PMID:20485341 "It has been shown that once phosphorylated, IRAK1 or IRAK2 leaves the Myddosome and interacts with TRAF6 to elicit Lys63-linked polyubiquitination and downstream signaling 40,41."].
- Drives TRAF6 ubiquitination and NF-kB activation downstream of TLRs, as a non-catalytic adaptor in the human study
  [PMID:17878161 "Expression of IRAK-2, but not IRAK-1, led to TRAF6 ubiquitination, an event critical for NFkappaB activation."].
- IL-1 signalling: [PMID:9374458 "Two additional proximal mediators were identified that are required for IL-1R-induced NF-kappaB activation: IRAK-2, a Pelle family member, and MyD88"].
- Kinase activity is contested. Human: [PMID:10383454 "Although IRAK-M and IRAK-2 exhibit only a negligible autophosphorylation activity, they can reconstitute the IL-1 response in a 293 mutant cell line lacking IRAK."];
  UniProt CAUTION: Asn-335 replaces the catalytic Asp. Later mouse work (summarised in PMID:36865541)
  reports atypical kinase activity and autophosphorylation at S136/T140:
  [PMID:36865541 "Instead of a pseudokinase, IRAK2 can be classified as an atypical kinase, due substitution of residues 333 (Asp to Asn) and 351 (Asp to His) in its kinase domain (24, 78)."].
  GOA carries no kinase activity annotation for IRAK2; none is proposed here.
- Inflammasome: [PMID:36865541 "IRAK1-deficient mouse macrophages fails to activate caspase-1, whereas IRAK2-deficient cells behave like wild type controls (23)."]
  This contradicts the NAS annotation to NLRP3 inflammasome complex assembly.
- Redundancy with IRAK1: [PMID:38961291 "IRAK1 and IRAK2 appeared to be redundant, as double (but not single) knockouts abolished all responses to LPS"].
- Nuclear and mitochondrial translocation reported in mouse cells (PMID:36865541), non-core.
