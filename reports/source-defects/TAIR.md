# Source-record defects for TAIR

6 open defect(s), generated from `source_defects` blocks in this repository's reviews. Do not edit by hand.

## 1. WRONG_GENE_PRODUCT (PROBABLE, NOT_REPORTED)

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

## 2. WRONG_GENE_PRODUCT (PROBABLE, NOT_REPORTED)

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

## 3. WRONG_GENE_PRODUCT (PROBABLE, NOT_REPORTED)

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

## 4. WRONG_GENE_PRODUCT (PROBABLE, NOT_REPORTED)

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

## 5. WRONG_GENE_PRODUCT (PROBABLE, NOT_REPORTED)

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

## 6. WRONG_REFERENCE (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9SIV0 acts_upstream_of_or_within GO:0050832 defense response to fungus (IDA, PMID:32213638)
- **Field:** DB:Reference
- **Change:** check PMID:32213638 (alternatives in the explanation)
- **Likely cause:** UNKNOWN
- **Recorded in:** `genes/ARATH/SUR1/SUR1-ai-review.yaml`

This SUR1 (At2g20610, Q9SIV0) IDA for defense response to fungus (GO:0050832) is keyed to PMID:32213638 (Liu et al. 2020, ODR1/bHLH57 and seed dormancy). The full text (PMC7268807) contains no SUR1 genotype and no fungal or pathogen assay. Its accession list omits At2g20610, and QuickGO shows this as the paper's only annotation. The reference appears to be mis-keyed. Please identify the intended paper, or delete the row.

> we report the characterization of two ABA-related seed dormancy regulators in Arabidopsis
> — PMID:32213638
