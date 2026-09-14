# S. pombe vms1 (O74977): VLRF1 catalytic-site conservation

## Question

S. pombe `vms1` has **no** experimental molecular-function annotation (GOA carries
`GO:0003674 molecular_function` with evidence `ND`). Its only biological-process
annotation is an IBA to `GO:0036503 ERAD pathway`. The Vms1/ANKZF1 family's
best-characterised activity is instead cleavage of polypeptidyl-tRNA on stalled
60S ribosome-nascent-chain complexes, which in human ANKZF1 depends on a single
catalytic glutamine in the VLRF1 (Vms1-like release factor 1) domain.

Does S. pombe vms1 retain that catalytic glutamine, i.e. is it plausibly a
catalytically competent family member rather than a degenerate pseudoenzyme?

## Method

`vlrf1_catalytic_conservation.py` performs global BLOSUM62 pairwise alignments
(Biopython `PairwiseAligner`, gap open -11 / extend -1) of full-length UniProt
sequences and projects the human ANKZF1 catalytic position onto each ortholog:

| Accession | Protein | UniProt `ACT_SITE` |
|---|---|---|
| Q9H8Y5 | human ANKZF1 | 246 (Q246L abolishes polypeptidyl-tRNA cleavage) |
| Q04311 | *S. cerevisiae* Vms1 | 295 |
| O74977 | *S. pombe* vms1 | 249 (rule-inferred, PROSITE PRU01389) |

Human ANKZF1 is used as the reference because it is the only family member whose
catalytic residue has direct mutagenesis evidence in UniProt.

Reproduce with:

```bash
cd genes/SCHPO/vms1/vms1-bioinformatics
uv run python vlrf1_catalytic_conservation.py
```

FASTA inputs were downloaded from `https://rest.uniprot.org/uniprotkb/<ACC>.fasta`.

## Results

```
Reference: Q9H8Y5 (human ANKZF1), 726 aa
  annotated catalytic site 246: AKRGTA[Q]GLRDAR

Q04311 (S. cerevisiae Vms1), 632 aa  [alignment score 242.0]
  UniProt ACT_SITE           : 295  RKQGGS[Q]SAMDNA
  aligned to Q9H8Y5:246      : 295  RKQGGS[Q]SAMDNA
  alignment agrees with ACT_SITE annotation: yes
  residue at aligned position: Q

O74977 (S. pombe vms1), 600 aa  [alignment score 313.0]
  UniProt ACT_SITE           : 249  RKQGGS[Q]GAADNT
  aligned to Q9H8Y5:246      : 249  RKQGGS[Q]GAADNT
  alignment agrees with ACT_SITE annotation: yes
  residue at aligned position: Q
```

## Interpretation

- The alignment independently reproduces the UniProt `ACT_SITE` call for both
  yeasts: human ANKZF1 Q246 aligns to *S. cerevisiae* Q295 and *S. pombe* Q249.
- The glutamine is present in S. pombe vms1, in an `RKQGGSQ` motif that is
  identical to the *S. cerevisiae* Vms1 context and corresponds to the
  eRF1 GGQ-motif position repurposed in the VLRF1 clade.
- Conclusion: **S. pombe vms1 retains the catalytic residue required for
  polypeptidyl-tRNA cleavage in this family.** There is no evidence here of
  pseudoenzyme degeneration in the fission-yeast ortholog.

## Caveats

- Residue conservation supports catalytic competence but does not demonstrate
  it. No fission-yeast biochemistry for vms1 has been published; the proposed
  molecular-function annotation should therefore rest on sequence/ortholog
  evidence (ISS-level), not be asserted as experimentally established.
- Only three sequences were compared (the two model yeasts and human). This is
  a targeted check of one residue, not a family-wide phylogenetic analysis.
- Global pairwise alignment of full-length, domain-shuffled proteins can be
  unreliable outside conserved cores; the agreement between the projected
  position and the independently annotated `ACT_SITE` in both queries is the
  control that the projection is trustworthy here.
