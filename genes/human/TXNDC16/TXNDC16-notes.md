# TXNDC16 (Q9P2K2) review notes

## Identity
- Thioredoxin domain-containing protein 16; alias ERp90, KIAA1344. HGNC:19965. 825 aa precursor (signal peptide 1-27; chain 28-825).
- Large soluble ER-luminal glycoprotein of the PDI family with multiple (five) potential thioredoxin (Trx)-like domains. UniProt annotates one Trx domain 392-495, N-glycosylation at N460, intramolecular disulfide 449-456.
- C-terminal sequence has a MASKED, NON-FUNCTIONAL KDEL-like ER-retrieval motif (816-819), which permits partial secretion.
- UniProt has NO FUNCTION block and NO redox-active CXXC feature: the catalytic status is uncertain/likely redox-inactive.

## Key functional evidence

### PMID:21359175 (Riemer et al. 2011, "Identification of the PDI-family member ERp90 as an interaction partner of ERFAD") — full text cached
- "we identify the previously uncharacterized PDI-family member ERp90. In cultured human cells, we find ERp90 to be a soluble ER-luminal glycoprotein that comprises five potential thioredoxin (Trx)-like domains."
- "Mature ERp90 contains 10 cysteine residues, of which at least some form intramolecular disulfides. **While none of the Trx domains contain a canonical Cys-Xaa-Xaa-Cys active-site motif**, other conserved cysteines could endow the protein with redox activity."
- "ERp90 co-immunoprecipitates with ERFAD, a flavoprotein involved in ER-associated degradation (ERAD), through what is most likely a direct interaction. We propose that the function of ERp90 is related to substrate recruitment or delivery to the ERAD retrotranslocation machinery by ERFAD."
- ERFAD = FOXRED2 (UniProt Q8IWF2). The IPI protein binding annotation (PMID:21359175, with FOXRED2) is the functionally meaningful interaction (ERAD context), unlike typical HT captures, but is still a bare protein binding term.

### PMID:25122923 (Harz et al. 2014, "Secretion and immunogenicity of the meningioma-associated antigen TXNDC16") — abstract only cached
- "TXNDC16 was previously found to be an endoplasmic reticulum (ER)-luminal glycoprotein."
- "we show an additional ER-associated localization of TXNDC16 in the cytosol ... We were able to show TXNDC16 secretion in different human cell lines due to masked and therefore nonfunctional ER retrieval motif."
- "A previously indicated exosomal TXNDC16 secretion could not be confirmed in HEK293 cells." -> casts doubt on the exosome (PMID:19199708 HDA) localization.
- Meningioma-associated antigen; autoantibodies in patient sera; secreted serum protein in circulating immune complexes. Basis of the GO:0005576 extracellular region (EXP/IEA Secreted) annotations.

### PMID:19199708 (parotid gland exosome MudPIT proteomics) — HDA extracellular exosome
- High-throughput proteomic detection in exosomes. Note PMID:25122923 could NOT confirm exosomal secretion in HEK293; treat as non-core / uncertain.

## Redox/catalytic status
- No canonical CXXC in any Trx domain -> likely a redox-inactive / pseudo-thioredoxin scaffold (like the b-type PDI domains), possibly contributing to substrate recruitment/delivery rather than direct thiol-disulfide catalysis. Do NOT assert protein disulfide isomerase activity as a confirmed core MF; the evidence does not support a catalytic CXXC.

## GOA assessment
- GO:0005788 ER lumen (IEA SubCell + EXP PMID:25122923 + IDA PMID:21359175) — ACCEPT (primary localization).
- GO:0005576 extracellular region (IEA Secreted + EXP PMID:25122923) — KEEP_AS_NON_CORE (secreted due to masked KDEL; real but secondary).
- GO:0005515 protein binding (IPI, PMID:21359175, FOXRED2/ERFAD) — KEEP_AS_NON_CORE (functionally meaningful ERAD interaction but bare protein binding term; suggest a more informative MF if ERAD adapter role confirmed).
- GO:0070062 extracellular exosome (HDA, PMID:19199708) — KEEP_AS_NON_CORE / uncertain; exosomal secretion was not confirmed in a later study (PMID:25122923).

## Core function summary
TXNDC16/ERp90 is an ER-luminal PDI-family glycoprotein lacking a canonical CXXC redox motif; its best-supported role is as an interaction partner of the ERAD flavoprotein ERFAD/FOXRED2, proposed to function in substrate recruitment/delivery to the ERAD retrotranslocation machinery. It is partly secreted (masked KDEL) and is a meningioma-associated antigen. Core MF is not a confirmed catalytic oxidoreductase activity; propose no strong catalytic MF. BP = likely ERAD-related (proposed). CC = ER lumen (primary).
