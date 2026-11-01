# A0A2I0M3K7 (Columba livia TRUB2 gene model): sequence completeness and evolutionary placement

Analysis date: 2026-10-21. Script: `compare_to_trub2.py` (run with `uv run --script compare_to_trub2.py`);
raw output in `compare_to_trub2-output.txt` and `compare_to_trub2-results.json`.

## Method

- Pigeon sequence read from the local UniProt flat file (`A0A2I0M3K7-uniprot.txt`, 142 aa, sequence version 1).
- Human TRUB2 (O95900, 331 aa) and E. coli TruB (P60340, 314 aa) fetched from UniProt REST.
- Pigeon vs human: local Smith-Waterman, BLOSUM62, gap open -10, extend -0.5.
- E. coli vs human: global alignment with the same scoring, used to map E. coli TruB D48 (the
  conserved catalytic aspartate of the TruB family) onto human TRUB2.

## Results

- The pigeon sequence aligns to human TRUB2 residues 178-307 (pigeon residues 1-128), with 72.7% identity over 128 aligned residues.
- Pigeon Met1 corresponds to human TRUB2 Met178; the pigeon gene model has no counterpart of human TRUB2 residues 1-177.
- E. coli TruB D48 (context HTGALDPLATG) maps to human TRUB2 D98 (context VGHRLDAQASG).
- UniProt O95900 annotates human TRUB2 D98 as the active-site nucleophile (ACT_SITE 98, by similarity to TRUB1 Q9Y606), consistent with this mapping.
- The catalytic aspartate position (human D98) lies outside the region covered by the pigeon sequence, so A0A2I0M3K7 lacks the catalytic aspartate.
- The missing N-terminal region also includes human TRUB2 residues 1-10, which UniProt O95900 annotates as a predicted mitochondrial transit peptide (ECO:0000255).

## Evolutionary placement (from repository files, not new computation)

- UniProt places A0A2I0M3K7 in PANTHER PTHR13195:SF0 (PSEUDOURIDYLATE SYNTHASE TRUB2, MITOCHONDRIAL) and InterPro IPR039048 (Trub2), the same subfamily as human TRUB2.
- The PAINT file `interpro/panther/PTHR13195/PTHR13195-paint.tsv` has one annotated node, PTN000324318 (taxon:33213, Bilateria), seeded only by human TRUB2 (O95900).
- PAINT node PTN000324318 asserts pseudouridine synthase activity (GO:0009982), mRNA pseudouridine synthesis (GO:1990481), positive regulation of mitochondrial translation (GO:0070131) and mitochondrial matrix (GO:0005759).
- PAINT node PTN000324318 does not assert tRNA pseudouridine(55) synthase activity (GO:0160148) or mitochondrial tRNA pseudouridine synthesis (GO:0070902), although human TRUB2 carries both by IMP (PMID:33023933).

## Interpretation

A0A2I0M3K7 is an N-terminally truncated gene model (unassembled WGS contig AKCR02000043) of the
pigeon TRUB2 ortholog. Gene-level function can be inferred from PTHR13195:SF0 membership and the
Bilateria PAINT node, but the 142-aa polypeptide as modelled cannot itself be catalytically complete.
No full-length pigeon TRUB2 entry exists in UniProt (query gene:TRUB2 AND organism_id:8932 on
2026-10-21 returned only A0A2I0M3K7).
