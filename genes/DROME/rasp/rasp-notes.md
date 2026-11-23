# rasp (Rasp / Skinny hedgehog / Sightless / Central missing, Q9VZU2) curation notes

Deep research: `rasp-deep-research-falcon.md` (falcon; the wrapper reported a 600 s timeout but the run completed later). Folded in as an EDIT; its conclusions agree with the review and it is cited in the core function.

## Literature journal

- ski encodes an acyltransferase required for Hh N-terminal palmitoylation
  [PMID:11486055 "Hh proteins from ski mutant cells retain carboxyl-terminal cholesterol modification but lack amino-terminal palmitate modification"]
- sit acts in Hh-producing cells
  [PMID:11509241 "sit acts in the cells that produce Hh, but does not affect hh transcription, Hh cleavage, or the accumulation of Hh protein"]
- rasp is a segment-polarity gene; MBOAT homology
  [PMID:11861468 "Molecular analysis reveals that rasp encodes a multipass transmembrane protein that has homology to a family of membrane bound O-acyl transferases."]
- cmn (= rasp) acts independently of cholesterol modification
  [PMID:11748147 "cmn regulates the activity of Hh in a manner that is independent of cholesterol modification"]
- Spitz palmitoylation
  [PMID:16459296 "In cultured cells, Rasp promotes palmitate addition to the N-terminal cysteine residue of Spitz"]

## Curation decisions

- Core MF protein-cysteine S-palmitoyltransferase activity (thioester intermediate then S-to-N shift;
  consistent with human HHAT review); BP N-terminal peptidyl-L-cysteine N-palmitoylation, patched ligand
  maturation (here correct: palmitoylation is a Hh PTM), EGFR ligand maturation.
- palmitoyltransferase / acyltransferase activity MODIFY -> GO:0019706; Reactome cytosol MODIFY -> ER;
  membrane MODIFY -> ER membrane.

## Review-bot follow-up (PR #4478)

- GO:0019706 specifies an S-linked product; Rasp/HHAT form an N-linked amide (GO:0018009). Following the
  human HHAT review, GO:0016409 rows are now ACCEPT, GO:0016746 rows MODIFY -> GO:0016409, the core MF is
  GO:0016409, and the two experimental GO:0019706 rows are kept ACCEPT with the S- vs N-chemistry caveat.
  Core location changed to ER membrane to match the membrane MODIFY.
