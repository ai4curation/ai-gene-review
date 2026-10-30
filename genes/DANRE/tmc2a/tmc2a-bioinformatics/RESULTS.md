# tmc2a / tmc2b: identity, conserved synteny and public expression records

Scripts (run from the repo root; both query live APIs, nothing is hardcoded):

- `uv run python genes/DANRE/tmc2a/tmc2a-bioinformatics/pair_analysis.py tmc2a tmc2b TMC2` → `output.txt`
  (Ensembl REST: locations, Compara orthologues/paralogy node, canonical proteins, 15 protein-coding neighbours
  on each side of each copy with their gar and human orthologue positions, medaka co-orthologue locations).
- `uv run python genes/DANRE/tmc2a/tmc2a-bioinformatics/expression_compare.py tmc2a tmc2b` →
  `expression_output.txt` (ZFIN wild-type expression download and Bgee REST calls).

Run 2026-09-28. Results below are copied from those output files.

## Locations and Compara

- tmc2a chr5:55.22 Mb (+); tmc2b chr5:25.62 Mb (−); **same chromosome**, 29.6 Mb apart. tmc1 is at chr5:25.65 Mb,
  next to tmc2b.
- Ensembl Compara paralogy node joining them: **Osteoglossocephalai** (identity 67-69%).
- One gar orthologue for both (ENSLOCG00000009603, LG2:33.97 Mb). One medaka one-to-one orthologue for each, on
  **different medaka chromosomes** (tmc2a → chr12, tmc2b → chr9). Zebrafish-medaka identity (Compara, target %id):
  tmc2a 76.9%, tmc2b 67.6%.

## Protein identity (canonical Ensembl translations, global alignment, BLOSUM62)

| Pair | Identity | Similarity |
|---|---|---|
| tmc2a vs tmc2b | 68.4% | 78.7% |
| tmc2a vs gar TMC2 | 71.8% | 79.6% |
| tmc2b vs gar TMC2 | 67.2% | 76.9% |
| tmc2a vs human TMC2 | 56.6% | 71.2% |
| tmc2b vs human TMC2 | 56.0% | 69.8% |
| human TMC2 vs gar TMC2 | 58.6% | 72.1% |

tmc2b is further than tmc2a from both the gar and the medaka sequences: tmc2b has accumulated more change since the
duplication. The functional meaning, if any, is unknown.

## Conserved synteny

- The gar TMC2 anchor (LG2:33.97 Mb) sits next to the gar orthologue of tmc1 (LG2:33.9 Mb), in a block whose human
  orthologues are on 9q21 (70-77 Mb: TRPM3, KLF9, GDA, TMC1, ANXA1, RORB, TRPM6). Human TMC2 itself is on 20p13; so the
  fish and human arrangements differ (which one is ancestral is not tested here). None of the 60 neighbours
  maps within 5 Mb of human TMC2.
- **tmc2b** keeps that ancestral block: 14 of 30 neighbours have gar orthologues within 5 Mb of the gar anchor
  (carnmt1 through klf9, including tmc1).
- **tmc2a**: only 1 of 30 (prune2, gar LG2:34.7 Mb). But 12 further tmc2a neighbours map to gar LG2 at other positions
  (5.2-5.3 Mb and 40.5-46.3 Mb), and the tmc2a neighbourhood also contains human 9q21 genes (PRUNE2, GNA14, GNAQ at
  76.6-77.7 Mb; HNRNPK, NTRK2 at 84 Mb).
- **Both** neighbourhoods also contain a second, shared block: gar LG21 / human 9q34 (fbxw5, tmem203, tprn, anapc2
  near tmc2a; pnpla7b, mrpl41, dph7, paxx, abca2 near tmc2b; human 9:136.9-137.6 Mb).

Reading: the two zebrafish segments are each built from the same two ancestral blocks (gar LG2/human 9q21 and gar
LG21/human 9q34), which is the pattern expected for duplicated segments of one ancestral region. The tmc2a segment
has been rearranged relative to gar, so its micro-synteny around the gene itself is weak. The medaka copies are on
different chromosomes, as TGD ohnologs usually are; the zebrafish copies are on the same chromosome, which could
reflect a later rearrangement in the zebrafish lineage. This analysis does not by itself distinguish the TGD from a
large segmental duplication in the teleost stem; together with the PANTHER and Compara node placement it is
consistent with the TGD.

## Public expression records

- ZFIN (curated; ZDB-PUB-140813-4 and ZDB-PUB-260425-13): both copies in inner ear, otic vesicle and neuromast;
  tmc2a-only terms are crista and macula hair cells; tmc2b-only term is neuromast hair cell. This mirrors the
  published papers rather than adding independent data.
- Bgee: no calls for tmc2a; tmc2b neuromast hair cell (in situ) and low bulk RNA-seq calls in muscle and tail. Not
  hair-cell resolved; not interpreted.
