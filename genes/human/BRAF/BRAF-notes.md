# BRAF notes

## 2026-05-13 Falcon deep research integration

Falcon synthesis supports BRAF as a RAF-family serine/threonine kinase and
MAP3K in the canonical RAS-RAF-MEK-ERK cascade
[file:human/BRAF/BRAF-deep-research-falcon.md "BRAF is a RAF-family **serine/threonine protein kinase** that functions as the MAP3K tier in the canonical **RAS–RAF–MEK1/2–ERK1/2** cascade"]. UniProt independently supports the same core pathway placement via MEK phosphorylation
[file:human/BRAF/BRAF-uniprot.txt "Phosphorylates MAP2K1, and thereby activates the MAP kinase signal"].

The core review should emphasize cytosolic autoinhibited BRAF and plasma-membrane
active RAF dimers, while treating nuclear, mitochondrial, endomembrane, and
downstream cancer/transcription/metabolic phenotypes cautiously unless the cited
source directly tests BRAF
[file:human/BRAF/BRAF-deep-research-falcon.md "Evidence in this corpus supports **cytosolic autoinhibited complexes** and **plasma-membrane-associated active dimers**, but does **not** provide direct support for nuclear, Golgi/endomembrane, or mitochondrial localization for BRAF"].

Unresolved GOA rows were converted from PENDING to ACCEPT, KEEP_AS_NON_CORE,
MODIFY, REMOVE, or MARK_AS_OVER_ANNOTATED according to whether they support the
core RAF/MAPK kinase function, a peripheral regulatory context, a wrong kinase
tier, or a mutant/cancer-specific overextension.

## 2026-09-30 protein-binding backfill review

Reviewed the 106 GO:0005515/IPI rows added by the qualifier/supporting-entity
backfill. The batch was almost entirely interaction-table evidence: broad
AP-MS/BioPlex/kinome maps, BRAF/MEK inhibitor studies, and a mutation-directed
neoPPI screen. Generic protein-binding rows were either refined to GO:0071889
for 14-3-3 isoforms, GO:0031267 for HRAS, or GO:0046982 for direct RAF/KSR
heterodimerization when the supporting entity and paper justified a specific
molecular function; otherwise they were removed as uninformative rather than
treated as BRAF core molecular functions. All PMID caches were present; one
mouse KSR1 row from PMID:22510884 stayed UNDECIDED because the KSR1-specific
IntAct support was not visible in the cached article body.
