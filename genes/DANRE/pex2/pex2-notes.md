# pex2 notes

## 2026-05-09 review notes

Reviewed GOA, UniProt E7F4V8, PMID:34016526, and PANTHER family cache. The core role is peroxisomal ubiquitin-protein transferase activity supporting peroxisome organization/import quality control; disease-model phenotypes and starvation/pexophagy context were treated as non-core when broader than the gene product activity.

## Re-review 2026-09-29

The previous review was fully templated: one UniProt FUNCTION quote (a version that no longer matches the refreshed record) repeated under every term. All 16 rows rewritten with mechanism-specific evidence. Cached and cited PMID:35768507 (cryo-EM of the Pex2-Pex10-Pex12 retrotranslocon) and PMID:27597759 (PEX2 as the pexophagy E3).

- Resolved the three PENDING rows. Two are additional GO:0007031 peroxisome organization IMP rows from PMID:34016526 (different ZFIN genotypes / qualifiers) -> ACCEPT, matching the existing IMP row; one is a GO:0061630 ubiquitin protein ligase activity ISS with yeast Pex2 (P32800) as donor -> ACCEPT, matching the other two ligase rows.
- GO:0061630 now argued from structure rather than from the FUNCTION line: [PMID:35768507 "The three ring finger domains form a cytosolic tower, with ring finger 2 (RF2) positioned above the channel pore."] and [PMID:35768507 "monoubiquitylated by RF2 to enable extraction into the cytosol"]. This also explains why the ligase activity and the receptor-recycling process are the same event.
- GO:0016562 receptor recycling ACCEPT as the correctly scoped process; GO:0016558 protein import into peroxisome matrix kept non-core as its parent, with the explicit argument that Pex2 neither binds cargo nor translocates matrix proteins.
- GO:0000425 pexophagy and GO:1990928 response to amino acid starvation kept non-core but now supported by the paper that established them [PMID:27597759 "the peroxisomal E3 ubiquitin ligase peroxin 2 (PEX2) is the causative agent for mammalian pexophagy"; "We identify PEX5 and PMP70 as substrates of PEX2 that are ubiquitinated during amino acid starvation."], with the reason stating that these are conditional deployments of the same catalytic activity and have no zebrafish counterpart.
- GO:0008270 / GO:0046872 kept non-core as RING-domain cofactor binding [file:DANRE/pex2/pex2-uniprot.txt "The RING-type zinc-fingers that catalyze PEX5 receptor ubiquitination are positioned above the pore on the cytosolic side of the complex."]; GO:0016567 protein ubiquitination kept non-core as the substrate-free generic parent.
- The IMP rows rest on an abstract-only cache; the abstract states the zebrafish pex2 disruption and the ZS phenotype [PMID:34016526 "By disrupting the zebrafish pex2 gene, we established a disease model for ZS and found that it exhibits pathological features and metabolic changes similar to those observed in human patients."] and UniProt records the same disruption phenotype, so the curator's rows were accepted rather than re-adjudicated from the abstract.
- Description rewritten as standalone mechanism-level biology; core_functions restated; suggested_questions and suggested_experiments added (both were absent).
