# rasp (Rasp / Skinny hedgehog / Sightless / Central missing, Q9VZU2) curation notes

Deep research: falcon runs timed out this session; notes are from cached publications.

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
