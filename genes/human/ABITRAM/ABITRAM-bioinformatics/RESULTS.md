# Pairwise Sequence Identity Analysis for PANTHER:PTHR13651 (PROTEIN ABITRAM)

## Method and Provenance
- **Script**: `genes/human/ABITRAM/ABITRAM-bioinformatics/pairwise_identity.py`
- **Biopython version**: `1.85` (`Bio.Align.PairwiseAligner`, `mode="global"`)
- **Parameters**: Needleman-Wunsch global alignment with `BLOSUM62` substitution matrix, `open_gap_score = -10.0`, `extend_gap_score = -0.5` (EMBOSS `needle` standard parameters).
- **Denominator definitions**:
  - **Global % Identity (`identical / aln_len`)**: Identical aligned residues divided by full global alignment length including terminal and internal gaps (primary reported figure).
  - **Aligned-Residue % Identity (`identical / ungapped_cols`)**: Identical aligned residues divided by residue-to-residue aligned columns excluding gaps (captures conservation across the shared `IPR039169` / `PF01597` barrel-sandwich hybrid core when terminal tail lengths differ).

## Input Sequences (`PANTHER:PTHR13651:SF0`)

| Accession | Symbol | Organism | Length (aa) | Seq Version | Source |
|---|---|---|---:|---:|---|
| `UniProtKB:Q9NX38` | `ABITRAM` | *Homo sapiens* | 181 | 1 | `genes/human/ABITRAM/ABITRAM-uniprot.txt` |
| `UniProtKB:Q80ZQ9` | `Abitram` | *Mus musculus* | 193 | 2 | `genes/mouse/Abitram/Abitram-uniprot.txt` |
| `UniProtKB:D4AE08` | `Abitram` | *Rattus norvegicus* | 193 | 1 | `genes/rat/Abitram/Abitram-uniprot.txt` |
| `UniProtKB:Q1LU93` | `abitram` | *Danio rerio* | 177 | 1 | `genes/DANRE/abitram/abitram-uniprot.txt` |
| `UniProtKB:Q9VFR1` | `abitram` | *Drosophila melanogaster* | 214 | 1 | `genes/DROME/abitram/abitram-uniprot.txt` |
| `UniProtKB:P34452` | `F54F2.7` | *Caenorhabditis elegans* | 157 | 2 | `genes/worm/F54F2.7/F54F2.7-uniprot.txt` |
| `UniProtKB:Q54TD9` | `abitram` | *Dictyostelium discoideum* | 175 | 1 | `genes/human/ABITRAM/ABITRAM-bioinformatics/inputs/non_chordate_outgroups.fasta` |
| `UniProtKB:Q581S9` | `Q581S9` | *Trypanosoma brucei* | 197 | 1 | `genes/human/ABITRAM/ABITRAM-bioinformatics/inputs/non_chordate_outgroups.fasta` |

## Global Pairwise % Identity Matrix (`identical / aln_len`)

| Member | `Q9NX38` | `Q80ZQ9` | `D4AE08` | `Q1LU93` | `Q9VFR1` | `P34452` | `Q54TD9` | `Q581S9` |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `Q9NX38` (*H. sapiens*) | 100.0% | 80.8% | 83.4% | 68.0% | 34.5% | 27.0% | 29.9% | 27.8% |
| `Q80ZQ9` (*M. musculus*) | 80.8% | 100.0% | 89.6% | 65.8% | 33.6% | 21.9% | 29.3% | 28.2% |
| `D4AE08` (*R. norvegicus*) | 83.4% | 89.6% | 100.0% | 66.3% | 35.4% | 24.2% | 29.1% | 27.3% |
| `Q1LU93` (*D. rerio*) | 68.0% | 65.8% | 66.3% | 100.0% | 33.3% | 25.7% | 29.5% | 29.0% |
| `Q9VFR1` (*D. melanogaster*) | 34.5% | 33.6% | 35.4% | 33.3% | 100.0% | 23.7% | 25.7% | 25.0% |
| `P34452` (*C. elegans*) | 27.0% | 21.9% | 24.2% | 25.7% | 23.7% | 100.0% | 23.7% | 24.5% |
| `Q54TD9` (*D. discoideum*) | 29.9% | 29.3% | 29.1% | 29.5% | 25.7% | 23.7% | 100.0% | 22.7% |
| `Q581S9` (*T. brucei*) | 27.8% | 28.2% | 27.3% | 29.0% | 25.0% | 24.5% | 22.7% | 100.0% |

## Detailed Pairwise Alignment Statistics (All 28 Unique Pairs)

| Protein A | Protein B | Identical / Aln Len | Global % Identity | Identical / Ungapped Cols | NW Score |
|---|---|---:|---:|---:|---:|
| `Q9NX38` (ABITRAM) | `Q80ZQ9` (Abitram) | 156/193 | **80.8%** | 156/181 (86.2%) | 794.0 |
| `Q9NX38` (ABITRAM) | `D4AE08` (Abitram) | 161/193 | **83.4%** | 161/181 (89.0%) | 824.0 |
| `Q9NX38` (ABITRAM) | `Q1LU93` (abitram) | 123/181 | **68.0%** | 123/177 (69.5%) | 661.0 |
| `Q9NX38` (ABITRAM) | `Q9VFR1` (abitram) | 77/223 | **34.5%** | 77/172 (44.8%) | 297.0 |
| `Q9NX38` (ABITRAM) | `P34452` (F54F2.7) | 50/185 | **27.0%** | 50/153 (32.7%) | 148.5 |
| `Q9NX38` (ABITRAM) | `Q54TD9` (abitram) | 58/194 | **29.9%** | 58/162 (35.8%) | 236.0 |
| `Q9NX38` (ABITRAM) | `Q581S9` (Q581S9) | 59/212 | **27.8%** | 59/166 (35.5%) | 169.0 |
| `Q80ZQ9` (Abitram) | `D4AE08` (Abitram) | 173/193 | **89.6%** | 173/193 (89.6%) | 917.0 |
| `Q80ZQ9` (Abitram) | `Q1LU93` (abitram) | 127/193 | **65.8%** | 127/177 (71.8%) | 661.5 |
| `Q80ZQ9` (Abitram) | `Q9VFR1` (abitram) | 76/226 | **33.6%** | 76/181 (42.0%) | 290.0 |
| `Q80ZQ9` (Abitram) | `P34452` (F54F2.7) | 43/196 | **21.9%** | 43/154 (27.9%) | 122.0 |
| `Q80ZQ9` (Abitram) | `Q54TD9` (abitram) | 60/205 | **29.3%** | 60/163 (36.8%) | 230.0 |
| `Q80ZQ9` (Abitram) | `Q581S9` (Q581S9) | 59/209 | **28.2%** | 59/181 (32.6%) | 182.0 |
| `D4AE08` (Abitram) | `Q1LU93` (abitram) | 128/193 | **66.3%** | 128/177 (72.3%) | 676.0 |
| `D4AE08` (Abitram) | `Q9VFR1` (abitram) | 80/226 | **35.4%** | 80/181 (44.2%) | 313.5 |
| `D4AE08` (Abitram) | `P34452` (F54F2.7) | 48/198 | **24.2%** | 48/152 (31.6%) | 131.0 |
| `D4AE08` (Abitram) | `Q54TD9` (abitram) | 60/206 | **29.1%** | 60/162 (37.0%) | 233.0 |
| `D4AE08` (Abitram) | `Q581S9` (Q581S9) | 57/209 | **27.3%** | 57/181 (31.5%) | 180.0 |
| `Q1LU93` (abitram) | `Q9VFR1` (abitram) | 74/222 | **33.3%** | 74/169 (43.8%) | 299.5 |
| `Q1LU93` (abitram) | `P34452` (F54F2.7) | 49/191 | **25.7%** | 49/143 (34.3%) | 132.5 |
| `Q1LU93` (abitram) | `Q54TD9` (abitram) | 56/190 | **29.5%** | 56/162 (34.6%) | 229.0 |
| `Q1LU93` (abitram) | `Q581S9` (Q581S9) | 62/214 | **29.0%** | 62/160 (38.8%) | 165.0 |
| `Q9VFR1` (abitram) | `P34452` (F54F2.7) | 53/224 | **23.7%** | 53/147 (36.1%) | 152.0 |
| `Q9VFR1` (abitram) | `Q54TD9` (abitram) | 58/226 | **25.7%** | 58/163 (35.6%) | 188.0 |
| `Q9VFR1` (abitram) | `Q581S9` (Q581S9) | 60/240 | **25.0%** | 60/171 (35.1%) | 159.0 |
| `P34452` (F54F2.7) | `Q54TD9` (abitram) | 45/190 | **23.7%** | 45/142 (31.7%) | 114.0 |
| `P34452` (F54F2.7) | `Q581S9` (Q581S9) | 52/212 | **24.5%** | 52/142 (36.6%) | 108.0 |
| `Q54TD9` (abitram) | `Q581S9` (Q581S9) | 48/211 | **22.7%** | 48/161 (29.8%) | 133.0 |

## Key Comparisons Referenced in Curation Notes

- **Human `ABITRAM` vs Mouse `Abitram`** (`Q9NX38` vs `Q80ZQ9`): **80.8%** global identity (156/193 columns; 86.2% [156/181] over aligned residue columns).
- **Human `ABITRAM` vs Rat `Abitram`** (`Q9NX38` vs `D4AE08`): **83.4%** global identity (161/193 columns; 89.0% [161/181] over aligned residue columns).
- **Rat `Abitram` vs Mouse `Abitram`** (`D4AE08` vs `Q80ZQ9`): **89.6%** global identity (173/193 columns; 89.6% [173/193] over aligned residue columns).
- **Zebrafish `abitram` vs Human `ABITRAM`** (`Q1LU93` vs `Q9NX38`): **68.0%** global identity (123/181 columns; 69.5% [123/177] over aligned residue columns).
- **Zebrafish `abitram` vs Mouse `Abitram`** (`Q1LU93` vs `Q80ZQ9`): **65.8%** global identity (127/193 columns; 71.8% [127/177] over aligned residue columns).
- **Zebrafish `abitram` vs Rat `Abitram`** (`Q1LU93` vs `D4AE08`): **66.3%** global identity (128/193 columns; 72.3% [128/177] over aligned residue columns).
- ***Drosophila* `abitram` vs Human `ABITRAM`** (`Q9VFR1` vs `Q9NX38`): **34.5%** global identity (77/223 columns; 44.8% [77/172] over aligned residue columns).
- ***Drosophila* `abitram` vs Mouse `Abitram`** (`Q9VFR1` vs `Q80ZQ9`): **33.6%** global identity (76/226 columns; 42.0% [76/181] over aligned residue columns).
- ***C. elegans* `F54F2.7` vs Human `ABITRAM`** (`P34452` vs `Q9NX38`): **27.0%** global identity (50/185 columns; 32.7% [50/153] over aligned residue columns).
- ***C. elegans* `F54F2.7` vs Mouse `Abitram`** (`P34452` vs `Q80ZQ9`): **21.9%** global identity (43/196 columns; 27.9% [43/154] over aligned residue columns).
- ***Dictyostelium* `abitram` vs Mouse `Abitram`** (`Q54TD9` vs `Q80ZQ9`): **29.3%** global identity (60/205 columns; 36.8% [60/163] over aligned residue columns).
- ***Trypanosoma* `Q581S9` vs Mouse `Abitram`** (`Q581S9` vs `Q80ZQ9`): **28.2%** global identity (59/209 columns; 32.6% [59/181] over aligned residue columns).
