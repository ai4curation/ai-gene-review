# Pnkd: exact selected product and same-gene reference

Selected B4F7D2 has 369 residues; reference D3ZXB0 has 424 residues.

Biopython PairwiseAligner global BLOSUM62, gap open -10, extension -0.5.

| Reference interval | Selected interval | Identical residues |
|---|---|---|
| 1–79 | 1–79 | 79 |
| 119–379 | 80–340 | 251 |
| 395–406 | 341–352 | 6 |
| 408–424 | 353–369 | 2 |

Reference feature mapping (sequence coverage does not establish retained function):

| Reference feature | Interval | Mapped / length | Identical |
|---|---|---|---|
| Transmembrane: Helical | 74–92 | 6 / 19 | 6 |
| Domain: Metallo-beta-lactamase | 168–330 | 163 / 163 | 163 |

A shared segment does not establish that a truncated product folds, is expressed, localizes, or catalyzes the full-length reaction.

Inputs are the sibling frozen ProtNLM source and same-gene reference JSON files. Reproduce with `UV_NO_SYNC=1 uv run python compare_sequences.py` from this directory.

## Re-run 2026-10-20: target sequence read from the UniProt record

The analysis script was revised so it reads the target sequence from the gene's UniProt record rather than from the ProtNLM2 source file, and was re-run; `results.json` and related outputs now reflect this re-run. The original results above are kept unchanged for the record.

Target B4F7D2 has 369 residues. Biopython PairwiseAligner global BLOSUM62, gap open -10, extension -0.5.

### Protein alignments (reference blocks vs target blocks, 1-based)

| Reference | Length | Identical to B4F7D2 | Aligned blocks (ref start-end : target start-end) |
|---|---|---|---|
| D3ZXB0 (rat, 424 aa model) | 424 | 338 | 1-79:1-79; 119-379:80-340; 395-406:341-352; 408-424:353-369 |
| Q69ZP3 | 385 | 336 | 1-340:1-340; 356-367:341-352; 369-385:353-369 |
| Q69ZP3-2 | 142 | 101 | 1-79:1-79; 80-81:167-168; 82-84:200-202; 85-89:260-264; 90-116:302-328; 117-132:332-347; 133-138:359-364; 139-142:366-369 |
| Q69ZP3-3 | 424 | 336 | 1-79:1-79; 119-379:80-340; 395-406:341-352; 408-424:353-369 |
| Q69ZP3-4 | 360 | 269 | 1-2:1-2; 22-24:3-5; 25-42:8-25; 43-54:65-76; 55-315:80-340; 331-342:341-352; 344-360:353-369 |
| Q8N490 | 385 | 327 | 1-341:1-341; 355-379:342-366; 383-385:367-369 |
| Q8N490-2 | 142 | 99 | 1-79:1-79; 80-81:167-168; 82-84:200-202; 85-85:248-248; 86-90:252-256; 91-116:303-328; 117-125:332-340; 126-134:346-354; 135-140:364-369 |
| Q8N490-3 | 361 | 265 | 1-2:1-2; 21-42:3-24; 43-47:41-45; 48-55:69-76; 56-317:80-341; 331-355:342-366; 359-361:367-369 |
| Q8N490-4 | 325 | 257 | 1-8:1-8; 9-281:69-341; 295-319:342-366; 323-325:367-369 |
| NP_001128222.1 (rat RefSeq isoform 1) | 385 | 338 | 1-340:1-340; 356-367:341-352; 369-385:353-369 |

### Rat isoform 1 versus B4F7D2

B4F7D2 is identical to rat RefSeq NP_001128222.1 (isoform 1, 385 aa) over residues 1-328; after that the two C-termini are unrelated.

- B4F7D2 tail (41 aa): `VRPGGWEGRGGKPGPHPASTYHCPARACKLFLELWPLTAGV`
- Isoform 1 tail (57 aa): `CPSTLGEERAYNPFLRTHCLALQEALGPGPGPTSDDGCSRAQLLEELRRLKDMHKSK`

### Zn(2+) ligands (mouse Q69ZP3 positions, by similarity to HAGH)

| Mouse position | Mouse | B4F7D2 |
|---|---|---|
| 172 | H | H |
| 174 | H | H |
| 176 | D | D |
| 177 | H | H |
| 229 | H | H |
| 253 | D | D |
| 291 | H | H |

### Origin of the divergent tail (nucleotide level)

The BC168228 CDS (source of B4F7D2) matches the NM_001134750 CDS up to CDS nucleotide 984, then diverges. The first 36 divergent cDNA bases (`GTGAGGCCTGGGGGATGGGAGGGTCGGGGTGGGAAA`) are found at offset 43 of genomic window JAXUCZ010000009.1:83384150-83384400, preceded by `AAGAGCACA`.

A probe offset >= 0 that begins with GT immediately after the exon end means the cDNA reads straight from the exon into the downstream intron (intron retention), so the B4F7D2 tail is intron-encoded rather than an alternative coding exon.

Shared sequence does not establish that the B4F7D2 product is expressed, folds, localizes, or catalyses the reaction of the full-length protein.
