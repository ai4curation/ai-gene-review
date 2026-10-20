# Source-record defects for TAIR

12 open defect(s), generated from `source_defects` blocks in this repository's reviews. Do not edit by hand.

## 1. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:O81223 enables GO:0004723 calcium-dependent protein serine/threonine phosphatase activity (ISS, PMID:9632394)
- **Field:** GO_ID
- **Change:** delete the record asserting GO:0004723
- **Recorded in:** `genes/ARATH/CBL4/CBL4-ai-review.yaml`

This 1998 ISS row (no With/From) gives CBL4/SOS3 (O81223, AT5G24270) calcium-dependent protein serine/threonine phosphatase activity on the basis of its similarity to the calcineurin B regulatory subunit, made when SOS3 was cloned (PMID:9632394). In fungi and animals the phosphatase activity belongs to the catalytic calcineurin A subunit, not to calcineurin B, so the transfer does not hold even for a true calcineurin B ortholog. Plants have no calcineurin A homolog, no phosphatase partner of SOS3 has been found, and SOS3 instead binds and activates the SOS2 (CIPK24) protein kinase. We suggest withdrawing the row.

> However, as yet, no protein phosphatase has been found to interact with SOS3. Instead, SOS3 was found to interact with and activate a protein kinase encoded by SOS2.
> — PMID:10725350

> no genes similar to CNA have been identified from plants, yet
> — PMID:10725350

## 2. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:O81223 part_of GO:0005955 calcineurin complex (ISS, PMID:9632394)
- **Field:** GO_ID
- **Change:** delete the record asserting GO:0005955
- **Recorded in:** `genes/ARATH/CBL4/CBL4-ai-review.yaml`

This 1998 ISS row (no With/From) places CBL4/SOS3 (O81223, AT5G24270) in the calcineurin complex, on the cloning-time hypothesis that SOS3 acts through a calcineurin-like phosphatase (PMID:9632394). The calcineurin complex is the calcineurin A/B phosphatase heterodimer; plants have no calcineurin A, and the SOS3 effector identified since is the SOS2 (CIPK24) kinase, with which SOS3 forms a kinase complex. We suggest withdrawing the row.

> Our results imply that plant salt tolerance may be mediated not by a calcineurin-like protein phosphatase but, rather, by the SOS3/SOS2 kinase complex.
> — PMID:10725350

## 3. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:O81223 acts_upstream_of_or_within GO:0042539 hypotonic salinity response (IMP, PMID:9405721)
- **Field:** GO_ID
- **Change:** GO:0042539 → GO:0042538 (hyperosmotic salinity response)
- **Recorded in:** `genes/ARATH/CBL4/CBL4-ai-review.yaml`

This IMP row annotates CBL4/SOS3 (O81223, AT5G24270) to GO:0042539 hypotonic salinity response, defined as a response to a decrease in salt concentration. The cited paper (Liu and Zhu 1997) isolates sos3 as a mutant hypersensitive to Na+ and Li+ stress and assays growth inhibition on added NaCl, i.e. a response to an increase in salt concentration. The term should be GO:0042538 hyperosmotic salinity response; the qualifier and evidence can stay as they are.

> which is hypersensitive to Na+ and Li+ stresses
> — PMID:9405721

> results in plant hypersensitivity toward NaCl inhibition
> — PMID:9405721

## 4. WRONG_GENE_PRODUCT (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:F4JLB7 enables GO:0005515 protein binding (IPI, PMID:11752391)
- **Field:** DB_Object_ID
- **Change:** UniProtKB:F4JLB7 → UniProtKB:Q1G3K8 (RIC7 CRIB-motif protein encoded by AT4G28556)
- **Likely cause:** SYMBOL_COLLISION
- **Recorded in:** `genes/ARATH/F4JLB7/F4JLB7-ai-review.yaml`

This PMID:11752391 (Wu et al. 2001, RIC7) annotation is attached to F4JLB7 (AT4G28560), an LRR protein without a CRIB motif. The paper's RIC7 is a CRIB-motif ROP effector. All published RIC7 cloning and RT-PCR primers from this and two later RIC7 studies map to the adjacent, oppositely oriented locus AT4G28556 (UniProtKB:Q1G3K8) and to none of the AT4G28560 transcript. Both loci carry the TAIR symbol RIC7. Please check the cloned sequence and, if it confirms this, move the annotation to AT4G28556 / Q1G3K8.

> None of the six primers has an exact 3′ match of 14 or more bases in the AT4G28560 transcript NM_118998.1.
> — file:ARATH/Q1G3K8/Q1G3K8-bioinformatics/RESULTS.md

> contain a CRIB (for Cdc42/Rac-interactive binding) motif required for their specific interaction with GTP-bound Rop1.
> — PMID:11752391

## 5. WRONG_GENE_PRODUCT (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:F4JLB7 acts_upstream_of_or_within GO:0009860 pollen tube growth (IMP, PMID:11752391)
- **Field:** DB_Object_ID
- **Change:** UniProtKB:F4JLB7 → UniProtKB:Q1G3K8 (RIC7 CRIB-motif protein encoded by AT4G28556)
- **Likely cause:** SYMBOL_COLLISION
- **Recorded in:** `genes/ARATH/F4JLB7/F4JLB7-ai-review.yaml`

This PMID:11752391 (Wu et al. 2001, RIC7) annotation is attached to F4JLB7 (AT4G28560), an LRR protein without a CRIB motif. The paper's RIC7 is a CRIB-motif ROP effector. All published RIC7 cloning and RT-PCR primers from this and two later RIC7 studies map to the adjacent, oppositely oriented locus AT4G28556 (UniProtKB:Q1G3K8) and to none of the AT4G28560 transcript. Both loci carry the TAIR symbol RIC7. Please check the cloned sequence and, if it confirms this, move the annotation to AT4G28556 / Q1G3K8.

> None of the six primers has an exact 3′ match of 14 or more bases in the AT4G28560 transcript NM_118998.1.
> — file:ARATH/Q1G3K8/Q1G3K8-bioinformatics/RESULTS.md

> contain a CRIB (for Cdc42/Rac-interactive binding) motif required for their specific interaction with GTP-bound Rop1.
> — PMID:11752391

## 6. WRONG_GENE_PRODUCT (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:F4JLB7 located_in GO:0016324 apical plasma membrane (IDA, PMID:11752391)
- **Field:** DB_Object_ID
- **Change:** UniProtKB:F4JLB7 → UniProtKB:Q1G3K8 (RIC7 CRIB-motif protein encoded by AT4G28556)
- **Likely cause:** SYMBOL_COLLISION
- **Recorded in:** `genes/ARATH/F4JLB7/F4JLB7-ai-review.yaml`

This PMID:11752391 (Wu et al. 2001, RIC7) annotation is attached to F4JLB7 (AT4G28560), an LRR protein without a CRIB motif. The paper's RIC7 is a CRIB-motif ROP effector. All published RIC7 cloning and RT-PCR primers from this and two later RIC7 studies map to the adjacent, oppositely oriented locus AT4G28556 (UniProtKB:Q1G3K8) and to none of the AT4G28560 transcript. Both loci carry the TAIR symbol RIC7. Please check the cloned sequence and, if it confirms this, move the annotation to AT4G28556 / Q1G3K8.

> None of the six primers has an exact 3′ match of 14 or more bases in the AT4G28560 transcript NM_118998.1.
> — file:ARATH/Q1G3K8/Q1G3K8-bioinformatics/RESULTS.md

> contain a CRIB (for Cdc42/Rac-interactive binding) motif required for their specific interaction with GTP-bound Rop1.
> — PMID:11752391

## 7. WRONG_GENE_PRODUCT (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:P42760 enables GO:2001147 camalexin binding (IDA, PMID:21631432)
- **Field:** DB_Object_ID
- **Change:** check UniProtKB:P42760 (alternatives in the explanation)
- **Likely cause:** LEGACY_ALIAS
- **Recorded in:** `genes/ARATH/GSTF6/GSTF6-ai-review.yaml`

PMID:21631432 reports heterocyclic-ligand binding "uniquely" for GSTF2 and GSTF3. In the phi-GST nomenclature, GSTF3 is At2g02930 (Q9SLM6). This annotation is instead on GSTF6 (At1g02930, P42760), whose only link to the name is the legacy alias "AtGSTF3". QuickGO returns this paper's binding IDAs for GSTF2 (P46422) and GSTF6 but none for Q9SLM6, the pattern expected from mapping the paper's "GSTF3" through the alias. We could not read the full text. Please check it: if GSTF3 was assayed, move the annotation to Q9SLM6; if only GSTF2 bound the ligand, delete this row. The abstract names GSTF3 only for the heterocyclics and attributes camalexin and quercetin-3-O-rhamnoside binding to GSTF2, so deletion is the more likely outcome for this ligand.

> Uniquely, when overexpressed in bacteria, family members GSTF2 and GSTF3 bound a series of heterocyclic compounds
> — PMID:21631432

> GSTF2 also selectively bound the indole-derived phytoalexin camalexin, as well as the flavonol quercetin-3-O-rhamnoside
> — PMID:21631432

## 8. WRONG_GENE_PRODUCT (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:P42760 enables GO:2001227 quercitrin binding (IDA, PMID:21631432)
- **Field:** DB_Object_ID
- **Change:** check UniProtKB:P42760 (alternatives in the explanation)
- **Likely cause:** LEGACY_ALIAS
- **Recorded in:** `genes/ARATH/GSTF6/GSTF6-ai-review.yaml`

PMID:21631432 reports heterocyclic-ligand binding "uniquely" for GSTF2 and GSTF3. In the phi-GST nomenclature, GSTF3 is At2g02930 (Q9SLM6). This annotation is instead on GSTF6 (At1g02930, P42760), whose only link to the name is the legacy alias "AtGSTF3". QuickGO returns this paper's binding IDAs for GSTF2 (P46422) and GSTF6 but none for Q9SLM6, the pattern expected from mapping the paper's "GSTF3" through the alias. We could not read the full text. Please check it: if GSTF3 was assayed, move the annotation to Q9SLM6; if only GSTF2 bound the ligand, delete this row. The abstract names GSTF3 only for the heterocyclics and attributes camalexin and quercetin-3-O-rhamnoside binding to GSTF2, so deletion is the more likely outcome for this ligand.

> Uniquely, when overexpressed in bacteria, family members GSTF2 and GSTF3 bound a series of heterocyclic compounds
> — PMID:21631432

> GSTF2 also selectively bound the indole-derived phytoalexin camalexin, as well as the flavonol quercetin-3-O-rhamnoside
> — PMID:21631432

## 9. WRONG_EVIDENCE_CODE (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9ZVD0 enables GO:0003677 DNA binding (ISS, PMID:11402159)
- **Field:** Evidence_Code
- **Change:** delete the record asserting ECO:0000250
- **Recorded in:** `genes/ARATH/SERRATE/SERRATE-ai-review.yaml`

This 2003 TAIR row asserts DNA binding for SERRATE (Q9ZVD0, AT2G27100) by ISS, citing the SE cloning paper (PMID:11402159), but has no With/From entry naming a characterized homolog. The cloning paper noted a single C2H2-type zinc finger and speculated about chromatin modification; a motif observation of this kind is not a sequence-similarity transfer. Later biochemical work shows that the SE N-terminal and zinc-finger regions bind RNA and DCL1, and SE associates with chromatin through RNA polymerase II complexes rather than by binding DNA itself. We suggest withdrawing the row.

> suggests a role for the SE gene product in regulating changes in gene expression via chromatin modification
> — PMID:11402159

> SE uses its N-terminal domain to bind to RNA and requires both N-terminal and ZnF domains to bind to DCL1.
> — PMID:23921632

## 10. WRONG_EVIDENCE_CODE (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9ZVD0 enables GO:0003700 DNA-binding transcription factor activity (ISS, PMID:11118137)
- **Field:** Evidence_Code
- **Change:** delete the record asserting ECO:0000250
- **Recorded in:** `genes/ARATH/SERRATE/SERRATE-ai-review.yaml`

This 2003 TAIR row asserts DNA-binding transcription factor activity for SERRATE (Q9ZVD0, AT2G27100) by ISS, but it has no With/From entry, so no characterized homolog is named and the sequence-similarity inference cannot be checked. The cited reference (Riechmann et al. 2000) is a genome-wide census of Arabidopsis transcription-factor families, not a characterization of an SE homolog; SE was presumably counted because of its single C2H2-type zinc finger. SE belongs to the ARS2 family of RNA effector proteins, whose characterized members act in RNA processing, not as sequence-specific DNA-binding transcription factors, so no valid ISS source for this activity exists. We suggest deleting the row (or, if TAIR wishes to keep it, supplying the With/From homolog so it can be assessed).

> Belongs to the ARS2 family.
> — file:ARATH/SERRATE/SERRATE-uniprot.txt

> We show that recombinant HYL1 and SE proteins accelerate the rate of DCL1-mediated cleavage of pre- and pri-miR167b substrates and promote accurate processing.
> — PMID:18632569

## 11. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9ZVD0 part_of GO:0005846 nuclear cap binding complex (IPI, PMID:24137006)
- **Field:** GO_ID
- **Change:** GO:0005846 → GO:0140262 (mRNA cap binding complex binding)
- **Recorded in:** `genes/ARATH/SERRATE/SERRATE-ai-review.yaml`

This IPI row makes SERRATE (Q9ZVD0, AT2G27100) part_of the nuclear cap binding complex because it binds both CBC subunits, CBP20 (AT5G44200) and CBP80/ABH1 (AT2G13540) (PMID:24137006). The nuclear cap binding complex is the CBP20/CBP80 heterodimer; SE is an associated partner, as ARS2 is in the metazoan CBC-ARS2 assembly, not a subunit. The IPI evidence fits the molecular function mRNA cap binding complex binding (GO:0140262), with the qualifier changed from part_of to enables; human SRRT/ARS2 carries that term.

> using Bimolecular Fluorescence Complementation (BiFC), pull-down and co-immunoprecipitation experiments, we show that both subunits of AtCBC, AtCBP20 and AtCBP80 interact with AtSE.
> — PMID:24137006

> SE/ARS2 executes its function in conjunction with the nuclear cap-binding complex (CBC), which consists of two subunits (CBP20 and CBP80)
> — PMID:30152752

## 12. WRONG_REFERENCE (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9SIV0 acts_upstream_of_or_within GO:0050832 defense response to fungus (IDA, PMID:32213638)
- **Field:** DB:Reference
- **Change:** check PMID:32213638 (alternatives in the explanation)
- **Likely cause:** UNKNOWN
- **Recorded in:** `genes/ARATH/SUR1/SUR1-ai-review.yaml`

This SUR1 (At2g20610, Q9SIV0) IDA for defense response to fungus (GO:0050832) is keyed to PMID:32213638 (Liu et al. 2020, ODR1/bHLH57 and seed dormancy). The full text (PMC7268807) contains no SUR1 genotype and no fungal or pathogen assay. Its accession list omits At2g20610, and QuickGO shows this as the paper's only annotation. The reference appears to be mis-keyed. Please identify the intended paper, or delete the row.

> we report the characterization of two ABA-related seed dormancy regulators in Arabidopsis
> — PMID:32213638
