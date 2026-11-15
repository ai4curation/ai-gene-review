# Curation Notes for Rat `Abhd11` (`UniProtKB:A0A8I6AS56`)

## 1. Gene Identity and Orthology

- **Gene / Accession**: *Rattus norvegicus* `Abhd11` (`RGD:1304681`, `UniProtKB:A0A8I6AS56`, unreviewed TrEMBL entry, 342 aa, `sv=1`), `PANTHER:PTHR46118:SF4` (`PROTEIN ABHD11`).
- **Active-site conservation**: Contains a 36-aa N-terminal extension relative to canonical 306-aa human `ABHD11` (`Q8NFV4` `sv=2`; internal `Met72` precedes conserved `78-RPLPLSYNLL-87`), placing the conserved oxyanion-hole motif at `100-HGLFG-104` (within `97-VLLHGLFGSK-106`), the nucleophilic elbow serine at **`Ser168`** (`164-LVGHSMGGK-172`, `166-GHSMG-170`), the beta-6 charge-relay aspartate at **`Asp192`** (`188-LVVVDISPA-196`), and the general-base histidine at **`His323`** (`319-PNAGHWVHS-327`) (`genes/human/ABHD11/ABHD11-bioinformatics/RESULTS.md`). Rat `Abhd11` is the 1:1 murine ortholog of mouse `Abhd11` (`UniProtKB:Q8K4F5`, ~95% identity across the mature chain) and human `ABHD11` (`UniProtKB:Q8NFV4`).

## 2. Targeted Literature Search for *Rattus norvegicus* `Abhd11` (`ND` Verification)

- **Literature search record**: Targeted PubMed and cached-corpus queries for `("Abhd11" OR "Wbscr21" OR "RGD:1304681" OR "A0A8I6AS56") AND ("rat" OR "Rattus norvegicus")` identified **zero** primary experimental publications assaying the rat `Abhd11` gene product directly in *Rattus norvegicus* cells or tissues; the UniProtKB `A0A8I6AS56` entry cites only the rat reference genome assembly (`Ensembl:ENSRNOP00000094705.1`) and automated ARBA/Pfam rules.
- **ND evaluation (`GO:0008150` `biological_process`, `ND`, `GO_REF:0000015`)**: Because no species-specific experimental literature in *Rattus norvegicus* identifies a biological process for rat `Abhd11`, the RGD `ND` annotation on `GO:0008150` strictly follows the GO `ND` evidence-code guideline (`projects/NO_DATA.md` Case N2, `nd_case: INFERABLE`) and is **`ACCEPT`**, supported by this documented literature search. No `BIOLOGY` `KnowledgeGap` is added because the physiological role (mitochondrial matrix OGDHc lipoyl deglutarylation maintaining 2-oxoglutarate/TCA cycle metabolism) is firmly established in direct human and mouse orthologs (`PMID:32792488`, `PMID:40664791`, `PMID:41184294`).

## 3. Annotation Review Summary

- **Kept (`ACCEPT`)**:
  - `GO:0005739` (`mitochondrion`, IBA, IEA, and 2x ISO from `MGI:MGI:1916008` and `UniProtKB:Q8NFV4`) and `GO:0005759` (`mitochondrial matrix`, IEA and ISO from `UniProtKB:Q8NFV4`): Soundly transferred from direct mammalian mitochondrial matrix proteomics and mitoplast protection data (`PMID:18614015`, `PMID:32792488`); per `projects/ORGANELLES.md`, both root `mitochondrion` and sub-compartment `mitochondrial matrix` are retained.
  - `GO:0045252` (`oxoglutarate dehydrogenase complex`, IEA and ISO from `UniProtKB:Q8NFV4`): Soundly transferred from 1:1 mammalian orthology (`PMID:32792488`).
  - `GO:0052689` (`carboxylic ester hydrolase activity`, IBA): Sound conserved active-site esterase activity supported by the intact `Ser168-Asp192-His323` catalytic triad (`PMID:27544863`, `PMID:32792488`).
  - `GO:0008150` (`biological_process`, ND): `ACCEPT` (`nd_case: INFERABLE`).
- **Refined (`MODIFY`)**:
  - `GO:0003824` (`catalytic activity`, IEA `InterPro:IPR000639`): Root-adjacent molecular function refined to `GO:0052689` (`carboxylic ester hydrolase activity`) already carried on the record.
- **Flagged (`MARK_AS_OVER_ANNOTATED`)**:
  - `GO:0006629` (`lipid metabolic process`, IBA from `SGD:S000003263`) and `GO:0016298` (`lipase activity`, IEA and ISO from `UniProtKB:Q8NFV4`): Propagated from yeast overexpression TAG shifts (`PMID:28465236`) and truncated recombinant in vitro DAG hydrolysis (`PMID:32579589`) that failed natural-substrate testing on full-length human ABHD11 (`PMID:27544863`) and showed unchanged endogenous 2-AG in `Abhd11` KO mice (`PMID:32579589`).
