# Sult1b1 notes

## Re-review 2026-10-10

**GOA changes.** Ten new rows seeded (all PENDING): nine ISO donor-split rows and one IBA
row. By term: GO:0004062 aryl sulfotransferase activity (ISO x2: donors RGD:12388849 and
human SULT1B1 UniProtKB:O43704); GO:0005737 cytoplasm (IBA, PANTHER:PTN007537669);
GO:0008146 sulfotransferase activity (ISO, O43704); GO:0042403 thyroid hormone metabolic
process (ISO x2: RGD:12388849, O43704); GO:0051923 sulfation (ISO x4: O43704
acts_upstream_of_or_within, mouse Sult1b1 MGI:MGI:2136282, RGD:12388849, O43704). No rows
retired.

**Actions.** All resolved consistently with their already-reviewed siblings:
- GO:0004062 (x2), GO:0042403 (x2), GO:0051923 (x4): ACCEPT, naming the donor
  (human SULT1B1 O43704, mouse Sult1b1 MGI:MGI:2136282, or RGD:12388849).
- GO:0008146 sulfotransferase activity (ISO, O43704): MODIFY -> GO:0004062, mirroring the
  existing GO:0008146 MODIFY rows (generic family parent replaced by the specific aryl
  sulfotransferase child; propagation_review TERM_SCOPING_PROBLEM / GRANULARITY_MISMATCH).
- GO:0005737 cytoplasm (IBA): KEEP_AS_NON_CORE, consistent with the ISO and EXP cytoplasm
  rows; rat Sult1b1 (RGD:3767 in WITH/FROM) is experimentally cytosolic (PMID:8530477).
No existing action changed.

**UniProt refresh.** The P52847 FUNCTION text was rewritten. The old quote ("...to catalyze
sulfate conjugation of dopamine, small phenols and thyroid hormones.") no longer exists; all
16 occurrences were replaced with the current verbatim text [UniProtKB:P52847 "Sulfotransferase
that utilizes 3'-phospho-5'-adenylyl sulfate (PAPS) as sulfonate donor to catalyze the sulfate
conjugation of dopamine, small phenols such as 1-naphthol and p-nitrophenol and thyroid
hormones, including 3,3'-diiodothyronine, triidothyronine (T3) and reverse triiodothyronine
(rT3) (PubMed:12773305, PubMed:8530477)"]. 0 stale remaining. status COMPLETE.

**Open questions.** RGD:12388849 is a rat RGD identifier used as an ISO donor into rat
Sult1b1; a curator may wish to confirm which rat gene/paralog it denotes.
