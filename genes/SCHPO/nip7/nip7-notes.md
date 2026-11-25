# nip7 (Q1MTQ9) — evidence and prediction assessment

Nip7 is an RNA-binding ribosome-biogenesis factor with pre-PUA and PUA domains. It associates with nascent 60S ribosomal subunits in the nucleolus and supports assembly of the large-subunit preribosome. The fission-yeast protein is present in structurally characterized early pre-60S particles; it is an assembly factor rather than a constitutive structural protein of the mature ribosome.

## Evidence and family boundary

The [2022 primary paper](https://pubmed.ncbi.nlm.nih.gov/36423630/) focuses on Fkbp39/nucleophosmin but reports multiple fission-yeast pre-60S particles. The [RCSB8ESQ metadata](https://www.rcsb.org/structure/8ESQ) explicitly identifies Q1MTQ9 as entity43, author chainl; the downloaded [entity response](nip7-8ESQ-entities.json) preserves the identity mapping. This directly supports the target’s occurrence in an early large-subunit precursor even though the article prose does not prominently name Nip7.

The PUA/pre-PUA architecture supports an RNA-binding assembly factor. It neither confers an RNA-cleavage or methyltransferase reaction nor turns Nip7 into a mature ribosomal constituent. PANTHER PTHR23415 has a mixed CKS/Nip7 name; that broad label is not evidence for kinase regulation by this protein. Falcon misses the target structural deposit and HDA nucleolar/cytosolic annotation and consequently understates the direct target evidence.

## External ProtNLM statements

[Exact retained output](nip7-protnlm-source.json). These are name/location claims, not emitted GO/EC predictions. CNN denotes overlap with existing supported annotation; it does not establish literal membership in the training set.

| Claim type | Verbatim output | Assessment | Evidence and interpretation |
|---|---|---|---|
| name | 60S ribosome subunit biogenesis protein NIP7 | CNN | The exact Q1MTQ9 protein is author chain l/entity43 in deposited pre-60S structure8ESQ linked to PMID:36423630. The name accurately identifies an assembly factor, not a mature ribosomal structural constituent. |

## Source quotations

## Research provenance

The genuine [Falcon report](nip7-deep-research-falcon.md) is retained with its provider metadata and artifact. Its conclusions were checked against the target record, exact accession and primary sources described above. Scientific uncertainties are recorded as UNC/UNDECIDED findings rather than a request for another reviewer to perform this assessment.

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

This re-review did not open or use any ProtNLM2 output.

### Identity
- Q1MTQ9 is the reviewed Swiss-Prot canonical entry for nip7 (SPCC320.11c), 180 aa, full length (PDB 8ESQ/8ESR chain l covers residues 1-180). It is not a fragment, isoform or alternative gene model. Domain architecture: N-terminal pre-PUA (PF17833) plus C-terminal PUA (PF03657 UPF0113; InterPro IPR002478). The budding-yeast ortholog is 181 aa [PMID:9271378 "NIP7 encodes a 181-amino-acid protein"].

### Phylogenetic placement
- PANTHER PTHR23415 is a mixed CKS/NIP7 family. In the PANTHER 19.0 classification, Q1MTQ9 is in **PTHR23415:SF4** ("60S RIBOSOME SUBUNIT BIOGENESIS PROTEIN NIP7 HOMOLOG"), together with S. cerevisiae NIP7 (Q08962, SGD:S000006132), mouse Nip7 (Q9CXK8) and Dictyostelium nip7 (B0G104). Human NIP7 (Q9Y221) is in SF34, which is also a NIP7 subfamily. The CKS proteins (suc1 P08463, CKS1, CKS1B, CKS2) are in SF29/SF42/SF48 and play no part in any inference here.
- PAINT node PTN000602113 (taxon Eukaryota) carries IBDs for nucleolus (donors human NIP7 and Trypanosoma Q389E3), preribosome LSU precursor (donor yeast NIP7), and ribosomal LSU biogenesis (donors yeast NIP7 and pombe nip7). PAINT did not propagate budding-yeast rRNA-processing terms. I treat that omission as deliberate and propose no NEW rRNA-processing term.
- Closest experimentally characterised relative: S. cerevisiae NIP7 (Q08962), which is in the same subfamily (SF4) and is the IBD donor. The repo has no review for it (genes/yeast has no NIP7 folder).

### Evidence on the target
- PDB 8ESQ (deposited with PMID:36423630) models Q1MTQ9 as entity 43/chain l in a fission-yeast pre-60S particle [file:SCHPO/nip7/nip7-8ESQ-entities.json "\"database_accession\": \"Q1MTQ9\""]. The paper's prose does not name Nip7; the IDA/EXP rows come from the PomBase curator's use of the structure.
- The ORFeome localization survey (PMID:16823372, abstract only) gives nucleolus plus cytoplasm/cytosol.

### Ortholog evidence (SF4 / NIP7 lineage)
- Budding yeast: Nip7 is essential, cosediments with free 60S but not with 80S or polysomes, is mostly nucleolar as a GFP fusion, and its depletion delays 27S pre-rRNA processing and causes a 60S deficit [PMID:9271378 "Delayed processing of 27S pre-rRNA appeared to be the cause of reduced synthesis of 25S rRNA relative to 18S rRNA"].
- Nip7 PUA domain RNA binding (yeast and Pyrococcus), with a polyuridine preference [PMID:18001138 "the PUA domain mediates Nip7 interaction with RNA"].
- Human NIP7 (SF34): nuclear, cosediments with pre-ribosomes, but knockdown mainly affects ITS1/18S processing [PMID:20798176]. Because of this divergence I used human data only for nucleolar localization.

### Changes vs previous version
- Same actions on all 15 rows (RNA binding ACCEPT; nucleus to nucleolus MODIFY; nucleolus ACCEPT; cytoplasm/cytosol KEEP_AS_NON_CORE; preribosome to LSU precursor MODIFY; ribosome assembly and LSU biogenesis to GO:1902626 MODIFY; GO:1902626 ACCEPT).
- Replaced label-only support (the PDB entity description) with the accession mapping, primary ortholog papers (PMID:9271378, PMID:18001138, PMID:20798176, added as references) and phylogenetic reasoning. Added propagation_review to the IBA MODIFY. Rewrote the description to separate target evidence from ortholog inference. Added suggested questions and experiments.

### Family review / modules
- interpro/panther/PTHR23415/PTHR23415-review.yaml lists Q1MTQ9 as the representative of a subfamily labelled "NIP7 and CKS proteins grouped by PANTHER". By PANTHER classification Q1MTQ9 is in the NIP7 subfamily SF4, not in a mixed NIP7/CKS group. The family review also lists human NIP7 as the representative of a separate "NIP7 homolog" branch, which is SF34 and distinct from SF4. I did not edit the family review (outside my scope).
- modules/: no module includes nip7 (the only hits are two unrelated deep-research artifacts). No pre-60S/ribosome-biogenesis module exists for yeast.
