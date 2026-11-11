# rps-3A (F56F3.5; UniProt P48154) - manual literature review

No deep-research API was available; this summary was compiled manually from the
UniProt record, cached publications and PubMed searches (October 2026).

## Identity and family

- C. elegans rps-3A (ORF F56F3.5, WBGene00004470) encodes the 257-aa small
  ribosomal subunit protein eS1 (40S ribosomal protein S3a)
  [file:worm/rps-3A/rps-3A-uniprot.txt "Belongs to the eukaryotic ribosomal protein eS1 family."].
- Domain/family signatures: HAMAP MF_03122 (Ribosomal_eS1_euk), InterPro
  IPR001593/IPR018281/IPR027500, Pfam PF01015 (Ribosomal_S3Ae), PROSITE PS01191,
  PANTHER PTHR11830 ("40S RIBOSOMAL PROTEIN S3A").
- UniProt (HAMAP-rule) states it is a "Component of the small ribosomal subunit"
  and that its subcellular location is Cytoplasm.
- A C-terminal disordered, basic/acidic region (237-257) is predicted by MobiDB-lite.

## Experimental structural evidence in C. elegans

- Sehgal et al. 2024 (PMID:39209556) determined a 2.63 A cryo-EM structure of the
  C. elegans 80S ribosome purified by sucrose gradient fractionation in the
  presence of cycloheximide [PMID:39209556 "We purified ribosomes from C. elegans
  via sucrose gradient fractionation."]. All ribosomal proteins were modelled
  except stalk proteins, eL28 and RACK-1 [PMID:39209556 "We also modeled the
  ribosomal proteins, with the exceptions of those bound to the P- and L-stalks
  (uL10/P0, P1, P2, uL1, uL11), eL28, and RACK-1"]. eS1 (rps-3A) is therefore part
  of the modelled 40S subunit; the UniProt entry cross-references the
  corresponding PDB entries 9BH5 and 9CAI (EM, chain AB, residues 1-257).
- The ribosomes were enriched for actively translating particles carrying tRNAs,
  consistent with eS1 being part of translating cytosolic ribosomes.

## Phenotypic / other data

- Audhya et al. 2005 (PMID:16247027) used RNAi of several ribosomal proteins as a
  general translation-inhibition control. The paper names "RPS-1, -3, -5, -11, -18,
  and -23"; it does not mention RPS-3A/F56F3.5 explicitly, so it should not be
  taken as data on this gene. Depletion caused sterility and osmotically sensitive
  embryos but no cytokinesis defect [PMID:16247027 "Depletions of six different
  ribosomal subunits (RPS-1, -3, -5, -11, -18, and -23) each resulted in penetrant
  sterility (unpublished data)."].
- No gene-specific biochemical study of C. elegans rps-3A was found by PubMed
  search ("rps-3A elegans" returned no hits).

## Orthology context

- eS1/RPS3A in yeast and mammals is a core 40S protein positioned near the mRNA
  entry/exit region on the solvent side of the head/platform; extra-ribosomal
  roles reported for mammalian RPS3A (e.g. apoptosis, transformation) have not been
  examined in C. elegans.

## Conclusions for GO

- Core: structural constituent of ribosome (MF); part of cytosolic small
  ribosomal subunit (CC); cytoplasmic translation (BP).
