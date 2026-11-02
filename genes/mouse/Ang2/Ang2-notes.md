# Ang2 notes

## 2026-10-16: AngII-sourced rows (issue #4246)

- The six MGI rows citing PMID:25313067 and PMID:28096417 were moved from UNDECIDED to REMOVE after reading the full text of both. Each paper uses angiotensin II only as an outside stimulus and never studies angiogenin-related protein. [PMID:25313067 "C57/B6 mice on high-NaCl diet received continuous infusion of AII (1 μg/kg per min, s.c. for 48 h), and WNK4 levels were measured."] Angiotensin II is a cleavage product of angiotensinogen (Agt), so these rows come from reading "AngII" as "Ang2".

## Follow-up (not handled in #4246)

- `GO:0071333 cellular response to glucose stimulus` (IDA, PMID:17670746) is still UNDECIDED. The paper is about angiopoietin-2, which is the unrelated gene *Angpt2*, so this looks like a second name confusion of the same kind. [PMID:17670746 "High glucose increases angiopoietin-2 transcription in microvascular endothelial cells"] The cached copy is abstract-only, so the full text needs to be read before the row is moved to REMOVE. The references list also includes PMID:16045902, a paper on macrophage angiopoietin-2 that points to the same confusion.
