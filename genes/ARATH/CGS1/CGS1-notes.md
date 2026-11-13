# CGS1 (P55217, At3g01120, MTO1) review notes

## 2026-11-13 full review (methionine_biosynthesis module, trans-sulfuration step 1)

No deep-research file present. Literature from UniProt references and GOA-cited PMIDs; newly cached
PMID:25146485, PMID:10558994, PMID:12121993, PMID:9002610 (abstract-only).

### Activity and substrate

- Physiological substrate O-phospho-L-homoserine (OPH):
  [PMID:9531508 "the gamma-replacement of the phosphoryl substituent of O-phosphohomoserine by cysteine"];
  Km 2.5 mM OPH, 460 uM Cys, Vmax 33.6 U/mg.
- UniProt (curated, ECO:0000269 PMID:9531508): OPH > OSH >> OAH. So GO:0003962 (defined with OSH) is
  genuinely catalysed, but the physiological reaction (EC 2.5.1.160, RHEA:80891) has no GO term.
  Proposed new term: O-phospho-L-homoserine-dependent cystathionine gamma-synthase activity.
- Gamma-elimination negligible: [PMID:9531508 "about 1/2700 as fast as the gamma-replacement reaction and approx. 1/1500 as fast as the gamma-elimination catalysed by the E. coli enzyme"].
  Contrast with E. coli MetB (see genes/ECOLI/metB notes).
- Complements E. coli metB: [PMID:9002610 "Cells expressing CGS1 can grow on medium lacking Met and contain CGS enzyme activity."]

### Location (plastid; projects/ORGANELLES.md does not cover plastids, judged by analogy)

- Transit peptide predicted [PMID:9002610] and shown functional with Ex1:GFP; mature N-terminus Ala91
  [PMID:25146485]. Chloroplast proteomics (PMID:18431481) and sub-plastid AT_CHLORO (PMID:20061580, stroma).
- Kept both chloroplast and stroma rows (organelle claim is informative; stroma supported by
  fractionation + soluble tetramer with no TM). Core location: chloroplast stroma.

### Regulation

- mto1 (PMID:12232133) over-accumulates Met; later shown to be CGS1 exon-1 mutations disrupting
  Met-triggered mRNA destabilisation [PMID:10558994 "an amino acid sequence encoded by the first exon of CGS acts in cis to destabilize its own mRNA"];
  motif mapped [PMID:12121993]. IMP row accepted (TAIR attribution backed by later cloning).

### Other

- Selenium volatilisation (PMID:14618405, Brassica juncea overexpression): KEEP_AS_NON_CORE.
- PANTHER (UniProt DR): PTHR43379 (CYSTATHIONINE GAMMA-SYNTHASE), subfamily PTHR43379:SF1
  (CYSTATHIONINE GAMMA-SYNTHASE 1, CHLOROPLASTIC-RELATED). InterPro IPR044639 (CGS1/2). PAINT node
  PTN002458772 (GO:0071265, seed AT3G01120) is recorded with taxon:2 in the local PAINT slice, which looks
  odd for a plant-seeded node; not investigated further.
- Module note: plant CGS uses O-phospho-L-homoserine, not an acylated homoserine, so it does not fit a
  MetA/MetX-coupled slot; it couples to homoserine kinase.
