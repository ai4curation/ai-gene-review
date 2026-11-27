# RNR1 (YER070W, P21524) notes

Review context: module `dntp_de_novo_synthesis` (class Ia RNR large subunit; EC 1.17.4.1; ADP/GDP/CDP/UDP reduction).

## Evidence journal
- R1 carries active site and effector sites [PMID:10716984 "The R1 protein is the business end of the enzyme containing the active site and the binding sites for allosteric effectors."]; holoenzyme alpha2-beta-beta' with Rnr2/Rnr4 [PMID:10716984 "both polypeptides of the Rnr2p/Rnr4p heterodimer cosediment at 9.7 S"].
- Recombinant Y1 activity [PMID:10535923 "The specific activity of Y1 isolated from yeast and E. coli is 0.03 micromol.min(-1).mg(-1)"].
- Rnr3 has <1% of Rnr1 activity [PMID:11893751 "The in vitro activity of Rnr3 was less than 1% of the Rnr1 activity."].
- Cytoplasmic; stays cytoplasmic after damage, small subunits move [PMID:12732713 "After genotoxic stress, Rnr1 remains in the cytoplasm"]; [PMID:18851834 "the large subunit Rnr1 is cytoplasmic"].
- Structures with substrates/effectors [PMID:16537479]; alpha6 hexamer [PMID:21336276 "we report the X-ray structure of S. cerevisiae RR1 (Yeast RR1) α6"]; C-terminal CX2C regenerates neighbouring active site [PMID:17277086]; Sml1 allosteric inhibitor [PMID:27155231].
- Multicopy RNR1 rescues mip1 (mtDNA polymerase) mutants [PMID:8552025 "an increased supply of dNTPs in mitochondria can stimulate the mtDNA polymerase activity"].

## Curation observations
- YeastPathways RCA GO:0106387 'de novo' GMP biosynthetic process (from PWY-7222-1) is a frame mis-mapping: REMOVE.
- Nuclear HDA (PMID:22842922) conflicts with dedicated localization studies: MARK_AS_OVER_ANNOTATED.
- 11 protein-binding IPI rows removed per policy (Rnr2, Rnr4, Sml1 partners); holoenzyme captured by GO:0005971.
