# ASZ1 notes

## 2026-10-05 review (PAINT, affinage)

- GASZ is germ-cell specific, with ANK repeats, a SAM domain and a bZIP-like region [PMID:12040005 "The full-length cDNA sequence corresponding to this EST encodes a novel protein containing four ankyrin (ANK) repeats, a sterile-alpha motif (SAM), and a putative basic leucine zipper (bZIP) domain."].
- Mouse knockout [PMID:19730684 "Knockout of Gasz in mice results in a dramatic downregulation of MILI, and phenocopies the zygotene-pachytene spermatocyte block and male sterility defect observed in MILI null mice."]. Retrotransposons are derepressed and piRNAs reduced. The authors also say the meiotic apoptosis "may be retrotransposon-independent", so meiotic division is kept as non-core rather than marked over-annotated.
- Mitochondrial outer membrane [PMID:26711429 "Taken together, these data demonstrate that GASZ interacts with itself at the mitochondrial outer membrane, likely through the SAM and ZIP domains."]. I added this as NEW ISO; PLD6 (MitoPLD) carries the term by IDA.
- Fly Gasz and Daedalus anchor Armi at mitochondria [PMID:31123065]. piRNA processing (GO:0034587) is not proposed as NEW: mouse Gasz carries no such term (MGI annotated TE silencing and meiosis), and the scaffold role in mammals is not yet shown. Raised as a suggested question.
- 11 GO:0005515 IPIs were removed under policy: 10 HuRI Y2H membrane-protein partners and one SARS-CoV-2 protein.
- PMID:19730684 has an erratum (PLoS Genet 2009 Dec). It is a correction, not a retraction; its body text could not be retrieved.

## 2026-10-05 revision (reviewer round 1)

- I had not adjudicated the central mitofusion finding of PMID:26711429. GASZ binds MFN1/MFN2 through its SAM/ZIP domains [PMID:26711429 "Indeed, we found that GASZ interacted with two key GTPases in mitochondrial fusion, MFN1 and MFN2, both in vitro in GST pull‐down assays (Fig EV5 A) and in Co‐IP (Fig 5 A) and in testes in vivo (Fig 5 B)."], and overexpression speeds PAGFP-measured fusion. Added NEW GO:0010636 positive regulation of mitochondrial fusion (ISO from mouse). The regulation term is used rather than GO:0008053 because GASZ promotes MFN-mediated fusion and is not a fusogen. Comparators: PLD6 (IDA), MIEF1 (IMP) and MSTO1 (IMP).
- MF: none is asserted. The evidence is binding (self, MFN1/2, nuage piRNA factors) plus MILI stabilization. No adaptor or scaffold experiment shows GASZ bridging two partners in mammals; the bridging evidence is from fly Gasz. Recorded as an MF_DARK knowledge gap.
- ISO rows now carry supporting_entities UniProtKB:Q8VD46.
- The description now says six ankyrin repeats, matching human UniProt ANK 1-6; the 2002 mouse paper described four.
