# matK (Maturase K) — Thlaspi arvense — review notes

UniProt: Q9GF35 · Plastid (chloroplast) genome-encoded · Taxon 13288 (*Thlaspi arvense*)
Family: intron maturase 2 family, MatK subfamily (HAMAP MF_01390)

## Function (homology-grounded; pennycress protein itself not assayed)
- MatK is the **only chloroplast-encoded intron maturase** retained in the plastid genome,
  typically encoded **within the intron of the trnK-UUU (lysine tRNA) gene**. It is a
  **trans-acting group II intron splicing factor**: it binds intron RNA and promotes
  excision of a conserved set of chloroplast **group IIA introns**.
  [file:THLAR/matK/matK-deep-research-falcon.md; UniProt Q9GF35 FUNCTION]
- Best-supported RNA targets (~7 group IIA introns): trnK-UUU (its own host intron),
  trnA, trnI, trnV, atpF, rpl2, and rps12 intron 2. In vitro, adding MatK increases
  splicing efficiency of rps12 intron 2; in vivo RIP shows association with multiple
  intron-containing transcripts. [file:THLAR/matK/matK-deep-research-falcon.md]
- Domain architecture: retains maturase "domain X" (RNA-binding/splicing) and a partial
  reverse-transcriptase-like region; lacks the endonuclease/mobility domains of canonical
  bacterial intron-encoded proteins — consistent with a dedicated splicing role.

## Localization
- Chloroplast **stroma** (soluble fraction in transplastomic tobacco), not membranes.
  [file:THLAR/matK/matK-deep-research-falcon.md]

## Essentiality / regulation
- matK knockouts could not be driven to homoplasmy in tobacco plastids → interpreted as
  essential. Developmentally regulated with mRNA-protein discordance.

## Applied note (DOE/BER-adjacent)
- matK is one of the most widely used **chloroplast DNA barcode / phylogenetic markers**
  (a distinct use from its protein maturase function). Relevant for germplasm /
  species identification in breeding programs, not for the bioenergy oil/biomass traits.

## Annotation review decisions
- GO:0005737 cytoplasm (IEA/ARBA) → **MODIFY → GO:0009570 chloroplast stroma**: matK is
  plastid-encoded and stroma-localized; generic "cytoplasm" is over-general and redundant
  with the chloroplast annotation.
- GO:0006397 mRNA processing (IEA/InterPro) → **ACCEPT**: several MatK targets are introns
  in protein-coding (mRNA) transcripts (atpF, rpl2, rps12).
- GO:0008380 RNA splicing (IEA/UniRule) → **MODIFY → GO:0000373 Group II intron splicing**:
  the precise, well-supported activity.
- GO:0009507 chloroplast (IEA) → **ACCEPT**: correct compartment.
- No MF annotation in GOA; the protein is an RNA-binding splicing factor → core MF
  GO:0003723 RNA binding.
