# mus304 (Drosophila ATRIP) review notes

## Identity
- UniProt Q9VVN4 (ATRIP_DROME); coiled-coil ATRIP-family protein; partner of MEI-41 (ATR).

## Literature journal
- Checkpoint: [PMID:10733527 "We have used this assay to show that the mutagen-sensitive gene mus304 is also required for this checkpoint."]
- Repair and genome stability: [PMID:10733527 "Similar to mei-41, mus304 is required for chromosome break repair and for genomic stability."]
- Localization: [PMID:10733527 "When expressed in tissue culture, epitope-tagged MUS304 is cytoplasmic, although we cannot rule out the possibility that a small amount of this protein is active in the nucleus."]
- Syncytial cycles: [PMID:10733527 "In three of six mus304 embryos examined, interphase failed to lengthen until cycle 14 and interphase 14 was interrupted by a premature mitosis 14."]
- Telomeres: [PMID:16203987 "the ATR-regulated pathway includes its partner ATR-interacting protein but not the Chk1 kinase"]
- Complex: UniProt mei-41 entry, "SUBUNIT: Interacts with mus304." (PubMed:14729967).

## Curation decisions
- Core: adaptor subunit of ATR-ATRIP complex in DNA damage checkpoint signaling (MF GO:0030674 by analogy with the human ATRIP review).
- Nucleus (NAS, yeast paper): initially non-core, upgraded to ACCEPT after deep research (see below).
- Meiotic phenotypes kept as non-core; imaginal disc development over-annotated.
- PMID:10559981 is an S. pombe Rad3-Rad26 paper.

## Deep research (falcon) update
- Nuclear pool after damage (Chiolo et al. 2011): [file:DROME/mus304/mus304-deep-research-falcon.md "after irradiation, GFP-tagged fly ATRIP/Mus304 formed foci within the HP1a-marked heterochromatin domain"]. Nucleus is therefore upgraded to ACCEPT and used as the core-function location.
- The deep research also notes that no direct purified Mus304-MEI-41 binding study was found; complex membership rests on UniProt's interaction record and the genetic data.
