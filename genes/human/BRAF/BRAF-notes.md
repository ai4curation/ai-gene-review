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


## 2026-10-24 ORGANELLES batch 2 (mitochondrion rows)

- Rows: GO:0005739 IBA (GO_REF:0000033, PTN000584576, is_active_in) and GO:0005739 IEA (GO_REF:0000107 from mouse Braf P28028). Both KEEP_AS_NON_CORE, unchanged; stale "PENDING"/line-number text removed and the check recorded. No sub-compartment rows.
- PAINT: interpro/panther/PTHR44329/PTHR44329-paint.tsv has the GO:0005739 IBD at PTN000584576 with donors MGI:MGI:88065 and MGI:MGI:88190. QuickGO shows these are mouse Araf (IDA PMID:12931191) and mouse Braf (IDA PMID:16116448).
- Ensembl projection: mouse Braf's mitochondrion row is that MGI IDA (PMID:16116448), so the IEA is not circular.
- PMID:16116448 (full text cached; Bag1 knockout): [PMID:16116448 "We have previously observed that most of the B-Raf but also C-Raf kinase immunoreactivity in postmitotic motoneurons are localized at mitochondria"] and [PMID:16116448 "a complex between Akt, B-Raf and Hsp70 is disrupted and B-Raf and Akt kinase loose their contact with mitochondria"]. Supports a recruited, Bag1-dependent pool at the mitochondrial surface (BAD phosphorylation context).
- Rule 4: peripheral recruitment only; BRAF has no transit peptide or membrane anchor, and no cached study fractionates it to the outer membrane. Stays at the root (same reasoning as TRAF3 in batch 1). Added PMID:16116448 to references.
