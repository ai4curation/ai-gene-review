# TRIM16 (EBBP, estrogen-responsive B box protein) review notes

UniProt: O95361 (TRIM16_HUMAN). TRIM/RBCC family. EC=2.3.2.27 (with ECO:0000269|PubMed:22629402 - experimental).

## Domain architecture - KEY: TRIM16 LACKS a canonical RING domain
- B-box zinc finger(s): ZN_FING 72-122 [UniProt FT]
- Coiled-coil (homodimerization)
- C-terminal B30.2/SPRY domain: DOMAIN 355-553 [UniProt FT]
- InterPro: B30.2/SPRY, B-box; PANTHER "B-BOX DOMAIN CONTAINING". No RING-HC.
- UniProt: "Auto-ubiquitinates via its B-Boxes" {ECO:0000269|PubMed:22629402} -> unusual; ligase activity attributed to B-boxes, not a RING.

## E3 ligase activity - experimentally claimed but atypical
- UniProt FUNCTION: "E3 ubiquitin ligase that plays an essential role in the organization of autophagic response and ubiquitination upon lysosomal and phagosomal damages." {ECO:0000269|PubMed:22629402, 27693506, 30143514}
- EC=2.3.2.27 with experimental evidence {ECO:0000269|PubMed:22629402}.
- PMID:22629402 "TRIM16 acts as an E3 ubiquitin ligase and can heterodimerize with other TRIM family members" - in vitro autoubiquitination via B-boxes.
- DECISION: The GO:0061630 ubiquitin protein ligase activity with EXP evidence (PMID:22629402) is experimentally supported per UniProt -> ACCEPT (do not REMOVE; the curator/UniProt assert experimental ligase activity even though it lacks a RING). However, the EC-based IEA assignment (GO_REF:0000003) assumes RING-type and is weaker -> KEEP_AS_NON_CORE / note. The task warns to be careful with catalytic claims for TRIM16 because it lacks a canonical RING; but UniProt explicitly cites experimental evidence, so ACCEPT the EXP one and frame core function as autophagy receptor/scaffold + atypical B-box ligase.

## Core functions (modern view)
1. Autophagy receptor/scaffold for damaged endomembranes (lysophagy) and protein aggregates. Interacts with Galectin-3/LGALS3 (ULK1-dependent) to direct autophagy of damaged endomembranes; scaffolds p62/SQSTM1, ATG16L1, LC3B/MAP1LC3B, BECN1; regulates p62-KEAP1-NRF2 signaling (modulates NRF2 ubiquitination/stability); protects against oxidative-stress-induced cell death from endomembrane damage. [PMID:27693506 "TRIM16 and Galectin-3 Co-direct Autophagy in Endomembrane Damage Homeostasis"; UniProt FUNCTION]
   - NOTE: The TRIM16 GOA stub does NOT currently contain an autophagy BP term (e.g. GO:0006914). The autophagy/lysophagy role is the modern core function but is captured in UniProt FUNCTION, not in the existing GOA annotations to be reviewed. -> propose new term / cover in core_functions.
2. Phosphorylated by ULK1 (PMID:27693506).
3. Older "EBBP" literature functions (mostly tumor-suppressor/differentiation/RA, in neuroblastoma and keratinocytes):
   - Tumor suppressor: inhibits cytoplasmic vimentin and nuclear E2F1 in neuroblastoma (PMID:20729920).
   - Positive regulator of keratinocyte differentiation (PMID:11919186).
   - Enhances IL-1beta secretion / positive regulation of IL-1beta production; binds IL-1 and NACHT domain (NALP1) (PMID:16575408).
   - Regulates retinoid signaling: positive regulation of RA receptor signaling, restores retinoid sensitivity via histone acetylation (PMID:16636064, PMID:19147277).
   - Response to retinoic acid (IEP, PMID:16636064), response to growth hormone (PMID:11919186).
   - DNA binding (IDA, PMID:16636064) and positive regulation of DNA-templated transcription (IDA, PMID:16636064/19147277): TRIM16 reported to act in nucleus on transcription; this is from EBBP-era work. These are real IDA annotations -> ACCEPT/KEEP_AS_NON_CORE; do not REMOVE experimental annotations.
   - PML body localization (IDA, PMID:16636064).

## Localization
- Cytoplasm (IDA, EXP PMID:27693506; multiple older IDA). Core.
- Cytosol (IDA HPA). 
- PML body (IDA PMID:16636064): nuclear body; older EBBP work.

## Notes on specific annotations
- GO:0061630 ubiquitin protein ligase activity EXP (PMID:22629402): ACCEPT (experimentally supported autoubiquitination via B-boxes, per UniProt EC ECO:0000269).
- GO:0061630 ubiquitin protein ligase activity IEA EC (GO_REF:0000003): KEEP_AS_NON_CORE (EC mapping assumes RING; redundant with the EXP one).
- protein binding (GO:0005515) IPI: VIM (P08670), E2F1 (Q01094), TINF2 (Q9BSI4), TRIM16L (Q309B1 x3), MAP1LC3B (O95166, PMID:25127057), IL1B/NALP1 (P29466, PMID:16575408). Bare protein binding -> KEEP_AS_NON_CORE.
- GO:0019966 interleukin-1 binding (IPI PMID:16575408): specific MF; older EBBP work. KEEP_AS_NON_CORE.
- GO:0032089 NACHT domain binding (IPI PMID:16575408): binds NALP1 NACHT domain. KEEP_AS_NON_CORE.
- GO:0003677 DNA binding (IDA PMID:16636064): KEEP_AS_NON_CORE (older work; TRIM16 lacks a classic DBD but reported to bind DNA/act in transcription).
- GO:0045893 positive regulation of DNA-templated transcription (IDA x2): KEEP_AS_NON_CORE (EBBP-era retinoid/transcription role).
- GO:0048386 positive regulation of RA receptor signaling (IDA): KEEP_AS_NON_CORE.
- GO:0032526 response to retinoic acid (IEP), GO:0060416 response to growth hormone (IDA): KEEP_AS_NON_CORE (response/context terms).
- GO:0032731 positive regulation of IL-1beta production (IMP PMID:16575408): KEEP_AS_NON_CORE.
- GO:0045618 positive regulation of keratinocyte differentiation (IDA PMID:11919186): KEEP_AS_NON_CORE.
- GO:0008270 zinc ion binding (IEA): KEEP_AS_NON_CORE (B-box coordinates Zn).
- GO:0016605 PML body (IDA): KEEP_AS_NON_CORE.

## GO IDs verified relevant
- GO:0061630 ubiquitin protein ligase activity (atypical B-box, experimentally claimed)
- GO:0006914 autophagy (core modern function - not in current GOA stub; propose)
- GO:0005737 cytoplasm / GO:0005829 cytosol (core CC)
