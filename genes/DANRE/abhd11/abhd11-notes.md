# Curation Notes for Zebrafish `abhd11` (`UniProtKB:Q6DRD9`)

## 1. Gene Identity and Active-Site Conservation

- **Gene / Accession**: *Danio rerio* `abhd11` (synonym `wbscr21`), `ZFIN:ZDB-GENE-040724-199`, `UniProtKB:Q6DRD9` (`ABHDB_DANRE`, reviewed Swiss-Prot entry, 317 aa, `sv=1`), `PANTHER:PTHR46118:SF4` (`PROTEIN ABHD11`).
- **Active-site and presequence architecture**: Encodes a predicted 20-aa N-terminal mitochondrial transit peptide (`FT TRANSIT 1..20`, mature chain `21..317`), conserved oxyanion-hole motif `76-HGLGG-80`, nucleophilic elbow serine **`Ser142`** (`140-GHSMG-144`, `FT ACT_SITE 142`), conserved beta-6 charge-relay aspartate **`Asp166`** (`LIAVDISPV`, corresponding to `Asp113` of *E. coli* YbfF `PDB:3BF7` `PMID:18215690` and `Asp156` of human `Q8NFV4`), and general-base histidine **`His297`** (`PNAGHWIHA`, `FT ACT_SITE 297`) (`genes/human/ABHD11/ABHD11-bioinformatics/RESULTS.md`). Note that UniProt `FT ACT_SITE 238` on beta-7 is an automated `ECO:0000250` projection rather than the conserved beta-6 carboxylate.

## 2. Literature and Orthology Assessment

- **Zebrafish literature**: UniProt `Q6DRD9` cites Amsterdam et al. 2004 (`PMID:15256591`, a large-scale retroviral insertional mutagenesis screen of early zebrafish embryonic development) and the NIH Zebrafish Gene Collection (`ZGC`) mRNA submission as nucleotide sequence sources. No direct biochemical or sub-organellar enzymatic study has assayed purified zebrafish `abhd11` in *Danio rerio*.
- **Conserved jawed-vertebrate orthology**: Zebrafish `abhd11` is the 1:1 teleost ortholog of human `ABHD11` (`UniProtKB:Q8NFV4`) and mouse `Abhd11` (`UniProtKB:Q8K4F5`), which localize to the mitochondrial matrix (`GO:0005759`), associate with the 2-oxoglutarate dehydrogenase complex (`GO:0045252`), and act as glutaryl-lipoyl thioesterases protecting OGDHc-E2 (`DLST`) lipoylation (`PMID:32792488`, `PMID:40664791`).

## 3. Annotation Actions Summary

- **`ACCEPT`**:
  - 4x `GO:0005739` (`mitochondrion`: IBA, IEA, and 2x ISS from `UniProtKB:Q8K4F5` and `UniProtKB:Q8NFV4`) and 2x `GO:0005759` (`mitochondrial matrix`: IEA and ISS from `UniProtKB:Q8NFV4`): Retained together per `projects/ORGANELLES.md`.
  - `GO:0045252` (`oxoglutarate dehydrogenase complex`, `part_of`, ISS from `UniProtKB:Q8NFV4`): Soundly transferred across 1:1 jawed-vertebrate orthology (`PMID:32792488`).
  - `GO:0052689` (`carboxylic ester hydrolase activity`, IBA): Sound conserved active-site esterase chemistry supported by the intact `Ser142-Asp166-His297` catalytic triad (`PMID:27544863`, `PMID:32792488`).
- **`MARK_AS_OVER_ANNOTATED`**:
  - `GO:0006629` (`lipid metabolic process`, IBA from `SGD:S000003263`), `GO:0016298` (`lipase activity`, ISS from `UniProtKB:Q8NFV4`), and `GO:0120516` (`diacylglycerol lipase activity`, IEA `RHEA:33275`/`38507`/`48596` with `UNIPROT` `source_defects`): Over-propagated from yeast overexpression TAG changes (`PMID:28465236`) and truncated human in vitro DAG hydrolysis (`PMID:32579589`) contradicted by full-length substrate profiling (`PMID:27544863`) and unchanged 2-AG in `Abhd11` KO mice (`PMID:32579589`).
