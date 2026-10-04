# ANKDD1B notes

## 2026-10-04 review (PAINT campaign, affinage provider)

- ANKDD1B (A6NHY2) is a 528-residue paralog of ANKDD1A, with 10 ankyrin repeats and a death domain. There is no functional literature, and affinage found none.
- **The single GOA row is signal transduction (InterPro IEA from the death domain):** MARK_AS_OVER_ANNOTATED, as for ANKDD1A (#4067). It is a domain-level inference with no data.
- No core function; WHOLLY_DARK gap. I added a question on whether it shares ANKDD1A's reported FIH1 interaction.

## 2026-10-04 round 2 (reviewer comments on #4068): PAINT and family analysis

- **Why there is no IBA.** ANKDD1B is in PANTHER PTHR24125 (subfamily SF1, ANKDD1B; ANKDD1A is SF0). (Round 4 correction: the entries CSV lists 4 representative proteins, not every member, and human ANKDD1A is not among them; see round 4 below.) I checked QuickGO for these proteins:
  - human ANKDD1B (A6NHY2): one IEA
  - mouse Ankdd1b (Q14DN9): IEA plus MGI ND rows
  - macaque ANKDD1A (Q9GKW8): one IEA
  - mimivirus L371 (Q5UQV3): none
  - human ANKDD1A (Q495B1): one IEA and a BioPlex protein-binding IPI. Q495B1 is assigned to PTHR24125 by the PAINT worklist (`projects/paint/human-no-IBA.tsv`), not by the entries CSV.
  - So no family member has an experimental functional annotation. "No IBA" means there is no donor evidence for PAINT to propagate, not that evidence was placed on another subtree. UniProt's PAN-GO line agrees: 0 phylogenetic annotations.
- **Negative claim now anchored on UniProt** (PE 4: Predicted; Pharos Tdark; PAN-GO 0) rather than only on the affinage null. The affinage reference_review now calls that record a null result.
- **Other fixes:**
  - HPA "Tissue enhanced (fallopian)" is added to the description.
  - The FIH1 question now cites PMID:30082910.
  - The reason states that MARK_AS_OVER_ANNOTATED is a gene-level judgment, not a challenge to the IPR000488 → GO:0007165 mapping (accepted for FAS/TNFRSF1A in projects/INTERPRO/suspect_interpro_mappings.tsv).
- **Caveat:** the InterPro PTHR24125 description mentions immune-regulatory roles, but it is LLM-generated and unchecked (`llm: true, checked: false` in the metadata), so it is not used.

## 2026-10-04 round 3 (reviewer comments on #4068)

- **Family files committed.** `interpro/panther/PTHR24125/` (entries.csv and metadata.yaml) existed only as an untracked local folder, so the survey above cited a file that wasn't in the repo. It is now committed with this review.
- **PAINT slice:** `just fetch-panther-paint PTHR24125` reports "0 node(s), no node-level annotations". There are no PTN nodes with any PAINT annotation in the family, which confirms that the absence of IBA reflects no curation or donor evidence.
- **Subfamilies:** PTHR24125 has three. SF0 is ANKDD1A, SF1 is ANKDD1B, and SF5 "ANKYRIN REPEAT PROTEIN" holds the giant-virus (Acanthamoeba polyphaga mimivirus) protein L371 (Q5UQV3).
- **PMID:30082910 quote:** the round-2 quote was verbatim from the paper's abstract (a different, longer sentence appears in the Results), and it validates after whitespace normalization. It is replaced anyway by the more mechanistic verbatim clause "the ankyrin repeat domain of ANKDD1A directly binds to the N-terminal domain of FIH1".
- **Provenance:** the family finding now carries its own provenance, a file: reference to the entries CSV.
- **Affinage reference_review:** `correctness` stays unset. The record is a null result with no citations, and no enum value fits a record that asserts nothing.

## 2026-10-04 round 4 (reviewer comments on #4068)

- **The entries CSV is a representative slice.** `PTHR24125-entries.csv` has 4 rows (human and mouse ANKDD1B, macaque ANKDD1A, mimivirus L371), but `PTHR24125-metadata.yaml` reports `proteins: 1495`. My member survey covers those four proteins plus human ANKDD1A via QuickGO and the worklist. It is not a complete enumeration.
- **PANTHER-source disagreement.** The repo's older PTHR24198 snapshot (`interpro/panther/PTHR24198/PTHR24198-entries.csv`, fetched 2026-05-04) places human ANKDD1A (Q495B1) in `PTHR24198:SF195 DEATH DOMAIN-CONTAINING PROTEIN`, and PTHR24198 has 49 PAINT IBD rows.
  - My reading is that the PTHR24125 placement is current:
    - the PTHR24125 snapshot is five months newer (2026-10-04);
    - the PAINT worklist assigns Q495B1 to PTHR24125;
    - `panther.obo` names PTHR24125:SF0 "ANKYRIN REPEAT AND DEATH DOMAIN-CONTAINING PROTEIN 1A";
    - the PTHR24198 IBD seeds are RAF/RIPK/MAP3K-type kinases, not ankyrin-death-domain proteins.
  - That is inference, not a check of the PTHR24198 tree. Per CLAUDE.md I keep both placements on record rather than re-point anything.
- **The no-donor claim now rests on the empty PAINT slice.** `just fetch-panther-paint PTHR24125` reports 0 annotated PTN nodes, and correspondingly there is no `PTHR24125-paint.tsv`. That file is only written when the slice is non-empty: about 2,900 committed families have one. The knowledge-gap boundary now says this rather than implying a complete member enumeration.
