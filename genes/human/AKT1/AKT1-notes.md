# AKT1 notes

## PN proteostasis review - 2026-06-03

Falcon deep research was already present and used for the re-review. It supports the core AKT1
function as a PI3K-regulated serine/threonine kinase rather than a proteostasis-specific protein
[file:human/AKT1/AKT1-deep-research-falcon.md "AKT1 is a **serine/threonine protein kinase** (PKB)"].

The Proteostasis PN projection places AKT1 under chaperone-mediated autophagy regulation and maps it
to `GO:1904715 negative regulation of chaperone-mediated autophagy` as more specific than the
existing broad GOA annotation to `GO:0010507 negative regulation of autophagy`
[file:projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv "AKT1 GO:1904715 negative regulation of chaperone-mediated autophagy more_specific_than_existing_goa"].
The parent PN type is mapped to the directional GO term because it records inhibitory CMA roles
[file:projects/PROTEOSTASIS/mappings/autophagy_lysosome_pathway.yaml "This PN type explicitly records inhibitory roles for CMA"].
The narrower "Modulator of LAMP2A multimerization" subtype is useful triage context but has no direct
GO mapping by itself, so I did not create a LAMP2A-specific GO assertion
[file:projects/PROTEOSTASIS/mappings/autophagy_lysosome_pathway.yaml "curation_status: no_mapping"].

The CMA projection is supported by Arias et al. 2015. The paper identifies a lysosomal
mTORC2/PHLPP1/Akt axis in which Akt1 inhibits CMA; Akt inhibition or Akt1 loss increases CMA reporter
activity and LAMP-2A translocation-complex assembly [PMID:26118642 "Overall, these results support an inhibitory effect of Akt1 on CMA"].
Mechanistically, the authors connect Akt activity to GFAP phosphorylation and LAMP-2A complex
dynamics, which supports a regulation term rather than direct CMA substrate delivery machinery
[PMID:26118642 "Inhibition of Akt activity in isolated lysosomes lead to a similar dose-dependent increase"].

Existing GOA already has broad autophagy/proteolysis annotations. The older reporter assay supports
AKT1 as an autophagy inhibitor because AKT1 knockdown increased LC3 reporter release
[PMID:18387192 "Knockdown of AKT1 resulted in an increase of dNGLUC release"].
Macroautophagy evidence remains non-core and context dependent; in mammary epithelial detachment,
PI3K-AKT-MTORC1 activation was not enough to suppress autophagy
[PMID:23778976 "not sufficient to suppress detachment-induced autophagy in MECs"].

Other proteostasis-adjacent AKT1 annotations are substrate or stress contexts, not core functions.
AKT phosphorylation of Rac1 supports FBXL19-mediated ubiquitination and degradation
[PMID:23512198 "Protein kinase AKT-mediated phosphorylation of Rac1 at serine(71) was essential"].
AKT/CHIP/tau work supports a substrate-specific negative regulation of protein ubiquitination
[PMID:18292230 "Akt also prevents CHIP-induced tau ubiquitination"].
The heat response annotation is also non-core: Akt suppression increases thermosensitivity, but the
paper attributes acquired thermotolerance primarily to Hsp72/JNK regulation
[PMID:10958679 "Suppression of Akt or ERK1 and -2 kinases increased cell thermosensitivity"].

Curation decision: retain AKT1 core functions as PI3K-regulated kinase activity and PH-domain
phosphoinositide binding. Add `GO:1904715 negative regulation of chaperone-mediated autophagy` as a
`NEW` non-core proposed annotation supported by PMID:26118642 and the PN projection. Do not make AKT1
a core proteostasis or direct CMA machinery gene, and do not add a new ontology term.
