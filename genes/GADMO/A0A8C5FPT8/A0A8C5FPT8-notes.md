# A0A8C5FPT8 (Gadus morhua tbc1d14) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

No ProtNLM2 files or prediction-evidence folders were consulted.

### Identity and gene model
- All ten cod UniProt entries named tbc1d14 are transcripts of one Ensembl gene,
  ENSGMOG00000018292 on chromosome 17 [file:GADMO/A0A8C5FPT8/A0A8C5FPT8-bioinformatics/RESULTS-rereview.md].
  None is reviewed in UniProt, so no reviewed canonical cod entry exists.
- A0A8C5FPT8 (709 aa) is an alternative gene model. It shares 97% identity with the sister model
  A0A8C5FCB4 (750 aa) but has a non-conserved N-terminus (MHFFLTRNYLL...). It also has a
  non-conserved 48-residue C-terminal tail (TDRDGRTDGRG...FYGGLAT) in place of the conserved
  ...QKDQERSSPVLRR end that matches human TBC1D14. The TBC domain (388-596), the TRAPP-binding
  segment and the arginine- and glutamine-finger residues (R457/Q493, equivalent to human
  R472/Q508) are all present.

### Orthology vs PANTHER placement
- PANTHER (via UniProt) places tetrapod TBC1D14 in PTHR47219:SF21. Teleost and coelacanth tbc1d14,
  including this protein, are placed in SF15 ("TBC1 DOMAIN FAMILY MEMBER 12 ISOFORM X1").
- A MAFFT and NJ panel puts the cod tbc1d14 models in the TBC1D14 clade: 60-66% identity to
  TBC1D14 orthologs, 54-58% to TBC1D12 orthologs, and 51% to the separate cod TBC1D12-like gene
  LOC115530985. The SF15 placement therefore looks like an HMM mis-assignment. The consequence is
  that cod receives the TreeGrafter GAP and small GTPase binding terms from PTN009208344 (a
  RABGAP1-seeded lineage), but not the TBC1D14-clade PAINT terms (PTN000538677 recycling endosome
  and autophagosome; PTN008586039 regulation of autophagosome assembly).
- Disagreement with interpro/panther/PTHR47219/PTHR47219-review.yaml: that review records the cod
  target as TBC1D12-like and calls paralog identity unresolved. The re-review tree resolves it
  as TBC1D14.

### Literature (human ortholog)
- [PMID:22613832 "TBC1D14 binds specifically to both Rab11a and 11b but not to any of the other 55 Rabs tested"]
- [PMID:22613832 "We then performed a GAP assay screen using a panel of 47 Rabs loaded with [32P]GTP but were unable to detect GAP activity with either recombinant GST-TBC1D14"]
- [PMID:22613832 "Amino acid starvation causes TBC1D14 to relocalize from REs to the"] Golgi complex.
- [PMID:26711178 "We also demonstrate that TBC1D14 is required for activation of RAB1 through its TRAPP‐binding ability."]
- [PMID:26711178 "We show here TBC1D14 acts as a negative regulator of autophagy by modulating the contribution of both RE and Golgi membranes to the growing autophagosome through its interaction with Rab11 and TRAPPIII."]

### Changes from the previous review
- GTPase activator activity: changed from UNDECIDED to MARK_AS_OVER_ANNOTATED. The ortholog
  shows no GAP activity across 47 Rabs, and the term reaches cod through a mis-placed subfamily.
- Enzyme binding: changed from MARK_AS_OVER_ANNOTATED to MODIFY, with replacements small GTPase
  binding and protein kinase binding (ULK1).
- Cytoplasmic vesicle: changed from ACCEPT to MODIFY, with replacement recycling endosome.
- Added NEW GO:2000785 regulation of autophagosome assembly. It is supported by the TBC1D14-clade
  PAINT node and by ortholog mechanism, not by phenotype alone.
- Vacuole is still over-annotated. Vesicle-mediated transport and small GTPase binding are
  still accepted.
- Core function location changed to recycling endosome. The description was rewritten.
