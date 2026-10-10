# NEUCR hog-1 notes

## 2026-10-10

### Setup

- Started from `origin/main` on `codex/neucr-hog-1-fungal-mapk`.
- Ran `just fetch-gene NEUCR hog-1`; this seeded 14 GOA rows for UniProt `Q96TL5`.
- Ran `just fetch-gene-pmids NEUCR hog-1`; the imported GOA rows are GO_REF/file-derived and had no direct PMIDs.
- Attempted `just deep-research-falcon NEUCR hog-1 --fallback perplexity-lite`; no provider/API key was available, so there is no provider deep-research file for this gene. I used cached primary papers, the cached UniProt record, PANTHER/PAINT data, and manual literature search instead.

### Identity

`hog-1`, synonym `os-2`, is Neurospora crassa ORF `NCU07024` and UniProt `Q96TL5`, annotated as MAP kinase hog-1, EC 2.7.11.24, in PANTHER family `PTHR24055` MITOGEN-ACTIVATED PROTEIN KINASE. UniProt records the canonical HOG1-subfamily MAPK features: a protein kinase domain spanning residues 20-299, ATP-binding sites, catalytic Asp141, and the MAPK TxY motif at Thr171/Tyr173.

### Cached primary evidence

- PMID:11823187 cloned `os-2`, showed that it encodes a HOG1-like MAPK, showed complementation of the Saccharomyces cerevisiae `hog1` osmosensitivity phenotype, sequenced three null alleles, built an `os-2` replacement mutant, and showed that `os-2` mutants are high-salt-sensitive and phenylpyrrole-resistant while wild-type `os-2` restores both growth on 4% NaCl and fungicide sensitivity.
- PMID:16278449 detected OS-2 phosphorylation in Neurospora wild-type mycelia after iprodione, fludioxonil, or KCl exposure, and the band was absent in `os-2` null mutants. This directly supports activation of Q96TL5 as a stress-activated p38/HOG-type MAPK.
- PMID:16524903 measured lower turgor in `os-1` and `os-2` mutants and abnormal hyperosmotic ion fluxes, supporting the pathway's role in Neurospora turgor regulation downstream of osmotic stress.
- PMID:16990038 is abstract-only in the cache but reports OS-2-dependent induction of glycerol synthesis, gluconeogenesis, and catalase genes after osmotic stress, fludioxonil, and heat shock; it also reports OS-1-dependent OS-2 phosphorylation under low osmotic stress/fludioxonil and OS-1-independent activation under heat or higher osmotic stress.
- PMID:17392518 places the response regulator RRG-1 upstream of OS-2: OS-2 phosphorylation increases in wild type after NaCl or fludioxonil but is nearly absent in `rrg-1` mutants; `os-2`, `os-4`, and `rrg-1` mutants also share a female-fertility/protoperithecial defect.
- PMID:17984065 shows rhythmic activation of OS-2 by the Neurospora circadian clock and connects the HOG/osmosensing cascade to daily preparation for hyperosmotic stress and desiccation.
- PMID:17986782 is abstract-only in the cache and reports osmotic-stress induction of several clock-controlled genes in an OS-2-dependent manner.
- PMID:18948219 is abstract-only in the cache and places the ATF-1 transcription factor downstream of OS-2 for fludioxonil/NaCl induction of `cat-1` and `ccg-1`.

### PAINT / IBA review

- `PTN000622075` is the broad MAPK-family PAINT node. The IBA rows it contributes to Q96TL5 are only `protein serine/threonine kinase activity`, nucleus, and cytoplasm. They are generic but safe for a catalytically intact HOG1-subfamily MAPK; the node is not transferring a clade-specific ERK/JNK/p38 pathway term onto the wrong fungal branch.
- `PTN001172058` is the fungal HOG/Sty1 node. Its `stress-activated MAPK cascade` and `osmosensory signaling pathway` transfers match direct Neurospora evidence from PMID:11823187, PMID:16278449, and PMID:17392518. The `cellular response to oxidative stress` transfer is safe by the node placement and fungal comparators, but the cached Q96TL5 papers here directly emphasize osmotic, fungicide, turgor, and developmental signaling more than an OS-2 oxidative-stress step, so I kept that row as non-core.
- Short `WITH/FROM` lists on the `PTN001172058` rows are not evidence of weak support: the PAINT curator is asserting inheritance from the fungal HOG/Sty1 node, not a pairwise transfer from the extant seed count.

### Newer-paper sweep

Manual search did not turn up a newer paper that changes the core interpretation of Neurospora HOG-1/OS-2. PMID:31736884 is a 2019 phosphoproteomics study of early plant-cell-wall recognition that discusses phosphorylation across MAPK pathways, including HOG1/OS-2 in the osmosensing pathway, but it is broad pathway context rather than a direct OS-2 functional dissection. PMID:33138786 is a 2020 clustering analysis of large-scale Neurospora deletion phenotypes; it includes the OS-2/p38 MAPK pathway in a broad phenomics context but likewise does not motivate a new GO action for Q96TL5.

### Row decisions

- Accepted the IBA/IEA/ISS catalytic rows for `protein kinase activity`, `protein serine/threonine kinase activity`, `MAP kinase activity`, and `protein serine kinase activity`. The parents are less specific than MAP kinase activity but not misleading.
- Accepted `ATP binding` as a non-core ATP-dependent kinase-domain property.
- Accepted nucleus and cytoplasm from both IBA and UniProt-SubCell IEA, consistent with HOG-family MAPK nucleocytoplasmic signaling.
- Accepted `osmosensory signaling pathway` and `stress-activated MAPK cascade`; they are core HOG/OS pathway functions.
- Kept `cellular response to oxidative stress` as non-core, not removed: the `PTN001172058` placement is appropriate, and fungal HOG/Sty1 comparators support oxidative-stress signaling even though the cached Neurospora evidence is more direct for osmotic/fungicide signaling.
