# ANKRD31 notes

- All 8 human GOA rows derive from mouse Ankrd31 (A0A140LI88): ISS, plus UniProt SubCell IEA. The mouse IMP/EXP rows come from the two 2019 Mol Cell co-founding papers [PMID:31003867 Boekhout, full text; PMID:31000436 Papanikos, abstract].
- Mechanism: ANKRD31 binds the REC114 PH domain directly (crystal structure) and stabilizes REC114 on axes and in the PAR. Losing only the REC114 contact phenocopies the null [PMID:37976262].
- **Sign:** the null has "delayed and/or fewer recombination sites but, paradoxically, more DSBs", and PAR DSBs are lost. GO:1903343 (positive regulation) → MODIFY to GO:1903341 (sign-neutral).
- Pairing (GO:0007129) is a downstream consequence of the DSB defect. Kept as non-core: MGI annotates MEI4, IHO1 and SPO11 to it by IMP (comparator check via QuickGO), while REC114 and MEI1 carry none.
- Human: heterozygous POI variants weaken REC114 binding [PMID:34257419].
- Epididymis [PMID:34820371]: reports junction-protein interactions and a BEB defect, which sits uneasily with "no somatic defects" in PMID:31003867. Noted; no GO drawn.
- No IBAs; PAN-GO 0.

## Round 2 (reviewer, PR #4114)

- NEW GO:0030674 protein-macromolecule adaptor activity (ISS from mouse), now the core MF. Basis: direct REC114 PH binding (crystal), several partners (including IHO1 per UniProt), and separation-of-function alleles that lose only the REC114 contact and phenocopy the null.
- Cited three papers that had been uncited:
  - PMID:32461690: PAR hyperaccumulation requires ANKRD31 and is linked to mo-2 arrays.
  - PMID:37431931: IHO1, TOPOVIBL and ANKRD31 share a REC114 PH surface.
  - PMID:38580643: ANKRD31 is a complementary route to IHO1-HORMAD1 seeding.
- The question and experiment are reworded so they build on PMID:32461690 instead of re-asking what it answered.
- Core locations now include chromatin. The GO:0007129 reason names acts_upstream_of_or_within as the accurate qualifier.
- Affinage reference_review: verification is scoped to the rows used. Its PMID:41706353 row lists 2023, but the record is 2026.
