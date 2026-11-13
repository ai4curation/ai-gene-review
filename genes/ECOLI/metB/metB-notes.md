# metB (P00935) review notes

## 2026-11-13 full review (methionine_biosynthesis module, trans-sulfuration step 1)

No deep-research file was present; literature was gathered from the UniProt record references and a
EuropePMC search for E. coli cystathionine gamma-synthase papers. New cached publications: PMID:9843488,
PMID:14503880, PMID:22855027, PMID:19370061, PMID:15581575 (all abstract-only in the cache).

### Core biology

- Purified MetB catalyses gamma-replacement of O-succinyl-L-homoserine (OSHS) by L-cysteine
  [PMID:2405903 "The Km values for the replacement reaction were calculated to be 1.0 mM for O-succinyl-L-homoserine and 0.05 mM for L-cysteine with maximal velocity of 700 min-1."].
- Tetramer, one PLP per subunit [PMID:2405903 "The active form is a tetramer with subunits of about 40,000 daltons and one pyridoxal phosphate cofactor per monomer."];
  1.5 A structure of the alpha4 tetramer [PMID:9843488].
- First step of bacterial trans-sulfuration
  [PMID:14503880 "in the first step of the bacterial transsulfuration pathway"].

### Side activity (promiscuous-activity tiers, projects/ENZYME_SPECIFICITY.md)

- Gamma-elimination of OSHS to succinate, 2-oxobutanoate and NH3 in the absence of cysteine
  [PMID:14503880 "The enzyme also catalyzes a competing gamma-elimination reaction, in which L-OSHS is hydrolyzed to succinate, NH(3), and alpha-ketobutyrate"].
  kcat/Km 1350 M-1 s-1 vs 9.8 x 10^4 for replacement (about 70-fold lower); described as "futile"
  [PMID:22855027 "In the absence of L-Cys, the enzyme catalyzes the futile α,γ-elimination of L-OSHS"].
- No GO row exists for OSHS gamma-elimination, so no action needed. If one were proposed it would be a
  genuine mechanistic side reaction of the same active site with no known physiological use; at most
  KEEP_AS_NON_CORE, more likely MARK_AS_OVER_ANNOTATED. Not proposed as NEW.
- The IBA cystathionine gamma-lyase row (GO:0004123) is a different reaction (cleavage of cystathionine).
  No measurement on E. coli MetB found. E. coli lacks reverse trans-sulfuration; its cystathionine
  cleavage enzyme is the beta-lyase MetC. Marked as over-annotation (activity not excluded, nothing shows
  it is used).

### PAINT reading (interpro/panther/PTHR11808/PTHR11808-paint.tsv)

- PTN000211711 (taxon Bacteria): GO:0003962, seeds P00935 (this gene) and P9WGB7 (Mtb MetB). Sound.
- PTN000211591: GO:0004123 and GO:0019344 seeded by CGLs (CTH, CYS3, C8VM61, O05394) and Mtb MetB.
  A fungal loss (IRD, NOT) exists at PTN000928751, but none for the enterobacterial CGS branch, so the
  lyase and cysteine-biosynthesis claims leak into E. coli MetB. Cysteine biosynthesis REMOVED (wrong
  direction: MetB consumes cysteine [PMID:19370061 places CGS+CBL in the bacterial forward pathway, CGL in
  the fungal/animal reverse pathway]).
- PTN000211590 (family root): cytoplasm, PLP binding, obsolete transsulfuration. Fine; transsulfuration
  MODIFIED to GO:0071269 L-homocysteine biosynthetic process as in STR2/cbl1 reviews.

### Module notes

- PANTHER (UniProt DR): PTHR11808 (TRANS-SULFURATION ENZYME FAMILY MEMBER), subfamily PTHR11808:SF75
  (CYSTATHIONINE GAMMA-SYNTHASE). NCBIfam TIGR02080 O_succ_thio_ly / IPR011821.
- Substrate is O-succinyl-L-homoserine, matching the MetA (succinyl) slot of the module.
- NEW row: GO:0071266 'de novo' L-methionine biosynthetic process (IC from GO:0003962).
