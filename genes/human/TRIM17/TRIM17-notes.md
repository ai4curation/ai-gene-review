# TRIM17 (terf, testis RING finger protein, RNF16) review notes

UniProt: Q9Y577 (TRIM17_HUMAN). EC=2.3.2.27. RING-type E3 ubiquitin transferase. TRIM/RBCC family.
Has a genuine RING-HC domain (CDD: RING-HC_TRIM17_C-IV; InterPro Znf-RING), B-box, coiled-coil, B30.2/SPRY.
Tissue: almost exclusively testis.

## Core functions (UniProt FUNCTION + experimental)
1. RING-type E3 ubiquitin ligase; autoubiquitinated. [PMID:19358823; UniProt EC; RING-HC]
   - GO:0004842 ubiquitin-protein transferase (IDA PMID:19358823), GO:0051865 protein autoubiquitination (IDA PMID:19358823), GO:0061630 (IBA, IEA EC), ARBA IEA transferase/autoubiq.
2. Regulator of neuronal apoptosis: ubiquitinates and degrades the anti-apoptotic MCL1 to initiate neuronal death. Also regulates NFAT transcription factors NFATC3/NFATC4 by preventing their nuclear localization (inhibiting their transcriptional activity). [UniProt FUNCTION; PMID:22023800 (MCL1/neuronal apoptosis) - not in stub]
3. Selective autophagy modulation: inhibits autophagic degradation of diverse targets while contributing to autophagy of midbodies; autophagy-inhibitory activity involves MCL1 which TRIM17 assembles into complexes with BECN1. [PMID:27562068 "TRIM17 contributes to autophagy of midbodies while actively sparing other targets from degradation"]
   - GO:0006914 autophagy (IDA PMID:25127057), GO:0032880 regulation of protein localization (IMP PMID:25127057), GO:0030674 protein-macromolecule adaptor activity (IPI PMID:25127057 with O75385=ULK1, Q8IYI6? - actually O75385 = ULK1; Q8IYI6 = ?). Adaptor activity captures scaffold role.
4. Prevents TRIM28 E3 ligase activity / its ubiquitination of anti-apoptotic BCL2A1, by interacting with TRIM28. [PMID:19358823? actually PMID:30042493 per UniProt; the BCL2A1 finding cited to PubMed:19358823 in FUNCTION]. TRIM44 stabilizes TRIM17/terf (PMID:19358823).
5. Stimulates degradation of ZWINT -> negative regulation of cell proliferation (PMID:22023800).
6. Decreases TRIM41-mediated degradation of ZSCAN2 -> stimulates alpha-synuclein/SNCA transcription in neurons (By similarity). [Note: task mentions ZSCAN21; UniProt says ZSCAN2 for human via similarity to mouse Q7TPM3 where it's Zscan21/Zipro1.]

## Localization
- Cytoplasm (IBA, IEA, EXP PMID:27562068). Core.
- Lysosome (IEA SubCell, EXP PMID:27562068): consistent with autophagy role.

## Notes on specific annotations
- GO:0045087 innate immune response (IBA): family-level phylogenetic inference; TRIM17's documented roles are apoptosis/autophagy/proliferation, not innate immunity. Weakly supported for TRIM17 specifically. KEEP_AS_NON_CORE (or MARK_AS_OVER_ANNOTATED). I'll KEEP_AS_NON_CORE per guideline not to overrule IBA without strong grounds, but note it's not a documented TRIM17 function. Actually it's an over-propagated family IBA -> MARK_AS_OVER_ANNOTATED is defensible. Use KEEP_AS_NON_CORE to be conservative.
- GO:0010468 regulation of gene expression (IBA): TRIM17 regulates NFAT/transcription indirectly (via localization/degradation). KEEP_AS_NON_CORE.
- GO:0004842/GO:0061630 ubiquitin ligase/transferase: core. ACCEPT.
- protein binding (GO:0005515) IPI: TRIM39 (Q9HCM9 x several), TRIM41 (Q8WV44), HGS (O14964), MEOX2 (Q6FHY5), MCL1 (Q07820? no), BECN1 (O75385? no - O75385=ULK1), and PMID:25127057 set (O75385, Q8IYI6, O95166=LC3B, Q13501=SQSTM1, Q14457=BECN1, Q9H492=MAP1LC3A). Bare protein binding -> KEEP_AS_NON_CORE.
  - PMID:25127057 IPI Q14457 = BECN1; O75385 = ULK1; Q13501 = SQSTM1; O95166 = GABARAPL2/LC3? ; Q9H492 = MAP1LC3A; Q8IYI6 = ? These are autophagy machinery.
- GO:0030674 protein-macromolecule adaptor activity (IPI PMID:25127057): scaffold linking MCL1/BECN1/autophagy machinery. ACCEPT (informative MF for the autophagy-regulatory scaffold).
- GO:0008270 zinc ion binding (IEA): RING/B-box. KEEP_AS_NON_CORE.

## GO IDs verified relevant
- GO:0061630 / GO:0004842 ubiquitin ligase/transferase (core MF)
- GO:0051865 protein autoubiquitination
- GO:0006914 autophagy (core BP - regulation of selective autophagy)
- GO:0030674 protein-macromolecule adaptor activity
- GO:0005737 cytoplasm / GO:0005764 lysosome (CC)
