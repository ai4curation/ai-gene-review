# MOH1 (YBL049W / P38191) — Bioinformatics analysis

Reproducible sequence/domain analysis to ground functional inference for a dark
gene. All numbers below are produced by the scripts in `scripts/` from the input
sequence in `data/`; nothing is hardcoded. Re-run with `just all`.

## Objectives

1. Verify the Yippee/Mis18/Cereblon (CULT) zinc-binding domain and the four
   putative Zn-coordinating cysteines annotated by UniProt (C45, C48, C101, C104).
2. Quantify sequence conservation of MOH1 versus the five human orthologs
   (YPEL1–YPEL5) and test whether the Zn-cysteines are conserved.
3. Assess whether there is any sequence-level evidence for catalytic activity.

## Methods

- **Input**: MOH1 sequence P38191 (`data/MOH1.fasta`, 138 aa).
- **Zinc-ligand scan** (`scripts/analyze_yippee.py`): enumerates all Cys/His and
  finds all C-x(2)-C pairs by regex; reports the candidate Yippee zinc site
  (two CxxC pairs + inter-pair spacer).
- **Conservation** (`scripts/conservation.py`): global BLOSUM62 pairwise
  alignment (Biopython `PairwiseAligner`) of MOH1 against each human YPEL; reports
  percent identity over aligned columns and whether each probed query position is
  identical/similar/gapped in the homolog.
- **Orthologs** (`scripts/fetch_orthologs.py`): live download of reviewed human
  YPEL1–5 from UniProt (O60688, Q96QA6, P61236, Q96NS1, P62699).
- **Negative control**: yeast pyruvate kinase CDC19 (P00549), a non-Yippee
  protein, run through both scripts to confirm they are not hardcoded.

## Results

### 1. Yippee zinc site (from `results/moh1_yippee.txt`)

```
length                    138
cysteine_positions        [45, 48, 97, 101, 104, 135, 137]
CxxC_pairs                [(45, 48), (101, 104)]
candidate_zinc_site       C45-x2-C48 ... C101-x2-C104
inter_pair_spacer_residues 52
predicted_zn_ligand_count 4
```

MOH1 contains exactly the two CxxC motifs that define the Yippee zinc site:
**C45-x2-C48 … C101-x2-C104**, separated by 52 residues. This is the canonical
Yippee signature (Cys-X₂-Cys-X₅₂-Cys-X₂-Cys) reported in the literature for the
family and matches the four UniProt Zn(2+)-binding features (positions 45, 48,
101, 104) exactly. The additional cysteines (97, 135, 137) do not form the
site.

### 2. Ortholog conservation (from `results/conservation.tsv`)

| Human ortholog | length | % identity to MOH1 | C45 | C48 | C101 | C104 |
|---|---|---|---|---|---|---|
| YPEL1 (O60688) | 119 | 44.0 | = | = | = | = |
| YPEL2 (Q96QA6) | 119 | 44.0 | = | = | = | = |
| YPEL3 (P61236) | 119 | 44.8 | = | = | = | = |
| YPEL4 (Q96NS1) | 127 | 44.2 | = | = | = | = |
| YPEL5 (P62699) | 121 | 37.3 | = | = | = | = |

- MOH1 is a **bona fide, moderately conserved (~37–45% identity) ortholog** of
  the human YPEL family across the Yippee domain.
- **All four zinc-binding cysteines are perfectly conserved** in every human
  ortholog (`=` in every cell), strongly supporting a structural Zn(2+) site
  retained from yeast to human.
- Notably, **YPEL5 (P62699) is the *least* identical** of the five (37.3%), yet
  it is (a) the PANTHER seed for the IBA "ubiquitin ligase complex" annotation
  and (b) the human gene shown to functionally complement moh1Δ (PMID:28173693).
  So MOH1 is the yeast representative of the whole family rather than a specific
  1:1 ortholog of any single human YPEL.

### 3. Evidence regarding catalytic activity

The Yippee fold (two four-stranded β-meanders coordinating one Zn²⁺ at the apex,
forming a cradle-shaped pocket) is a **structural/binding scaffold, not a
recognized catalytic fold**. The sequence contains no canonical catalytic motif
and no EC number is assigned in UniProt/GOA. The conserved cysteines are the
Zn-structural ligands, not a catalytic dyad/triad. **There is no sequence-level
evidence for enzymatic activity**; the family is best described as a putative
zinc-dependent protein/nucleic-acid interaction module of unknown biochemical
output.

### 4. Negative control (from `results/control_yippee.txt`, `results/control_conservation.tsv`)

Yeast pyruvate kinase CDC19 (P00549, 500 aa) returns
`candidate_zinc_site NONE (fewer than two CxxC pairs)` and its residues at the
probed positions do not match the YPEL cysteines (mostly gaps). This confirms the
scripts compute results from the actual input rather than emitting a fixed answer.

## Conclusions

- **Confirmed**: MOH1 is a Yippee-family protein with an intact, evolutionarily
  conserved zinc-binding site (C45/C48/C101/C104); the UniProt Zn features and the
  PROSITE Yippee domain call are corroborated independently here.
- **Confirmed**: MOH1 is a genuine ortholog of the human YPEL1–5 family
  (~37–45% identity), the single yeast member of a family that expanded to five
  paralogs in humans.
- **Inconclusive / unknown (correctly so)**: the analysis provides **no**
  evidence for a specific molecular *function* (catalytic or otherwise) beyond
  zinc binding. The biochemical activity and direct partners of MOH1 remain
  undetermined by sequence analysis — consistent with its status as a
  functionally dark gene.

## Reproducibility checklist

- [x] No script uses hardcoded inputs or outputs (all read `data/*.fasta`, write `results/*`).
- [x] Scripts tested on an independent input (CDC19 / P00549 negative control): Yippee scan correctly returns NO site; conservation probe correctly returns non-matching positions.
- [x] Analyses completed as expected.
- [x] Direct script outputs are in `results/`.
- [x] Summary includes provenance and justification; uncertainty (catalytic activity, specific MF) explicitly flagged as unresolved.

## Tools & data

- Biopython 1.87 (`PairwiseAligner`, BLOSUM62); Python ≥3.11; requests.
- UniProt REST API (sequences downloaded live).
- Reference sequence: UniProt P38191 (MOH1_YEAST).
