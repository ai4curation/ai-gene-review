# GNRHR variant-on-structure analysis

Question: where on the GnRH receptor do the variants reported in hypogonadotropic
hypogonadism 7 (HH7) fall, and what does the structure say about why each one loses
function?

Everything below is read from `results/` (written by the scripts); nothing is typed in
from memory. Residue numbers are those of UniProt P30968 (canonical isoform 1, 328
residues). Generic numbers are Ballesteros-Weinstein numbers from GPCRdb.

## How to reproduce

```
uv run --script 01_fetch_data.py        # downloads into data/ (git-ignored), writes data/manifest.json
uv run --script 02_variant_structure.py # writes results/*.tsv and results/summary.json
uv run --script 03_make_tables.py       # writes results/disease_variant_table.md
```

Inputs retrieved 2026-11-26 (`results/data_manifest.json`): UniProt P30968, GPCRdb
residue table, PDB 7BR3 (human GnRHR with elagolix, inactive, X-ray 2.79 A), PDB 9U4W
(pig GnRHR with GnRH and mini-Gq, active, cryo-EM 3.18 A), the AlphaFold model, the
reviewed GnRH receptor orthologues in UniProt, all 255 ClinVar records for the gene, and
gnomAD v4 variants and constraint. `variants_literature.yaml` is the one curated input:
22 variants with a published functional assay, each with its PMID and a sentence that was
checked to be verbatim in the cached paper.

## Checks on numbering and inputs

- All 41 disease-associated missense variants and all 392 gnomAD missense variants on the
  canonical transcript have a reference residue that matches the canonical sequence
  (`variants_ref_mismatch_dropped` is empty; no ClinVar protein change mismatched).
- gnomAD annotates 47 variants on ENST00000420975, the transcript of truncated isoform 2,
  whose reading frame differs after residue 175. They were skipped, because their protein
  consequences (for example "p.Lys217Ter") are not positions in isoform 1.
- 7BR3 is an engineered construct. Against the canonical sequence it carries P128K and
  has intracellular loop 3 (residues 243-256) replaced by a fusion protein. 40 residues
  are not modelled: 1-17, 66-73, 145-151 and 184-191. Lys191 and Cys14 are therefore
  absent from the only experimental human structure.
- 9U4W is the pig receptor (248 of 271 mapped residues identical to human). Distances to
  GnRH and to G-alpha-q are transferred to human numbering through a sequence alignment,
  so they are homology-based for the 23 positions that differ.
- The receptor ends at Leu328, the last residue of helix 7 modelled in 7BR3: there is no
  helix 8 or C-terminal tail.

## Result 1. Disease variants concentrate in the buried transmembrane core

| | buried (relative SASA <= 0.25 in 7BR3) | modelled |
|---|---|---|
| disease-associated missense | 30 | 39 |
| gnomAD-only missense | 170 | 304 |
| all modelled residues | 156 | 288 |

Fisher exact test, disease against gnomAD-only: p = 0.015. 34 of the 41 disease variants
are in transmembrane helices, 4 in extracellular loops, 2 in the N-terminus and 1 in an
intracellular loop. 37 of 41 are at positions identical in all ten mammalian orthologues,
against 201 of 354 gnomAD-only variants (210 of 328 positions overall).

The computed class of each disease variant (rule-based, from burial, side-chain volume
change, charge, proline or cysteine change, and distances in the two complexes):

| Computed class | n |
|---|---|
| transmembrane core packing | 19 |
| activation switch / G-protein interface | 6 |
| ligand-binding surface | 4 |
| extracellular fold (disulfide or glycan) | 3 |
| buried loop or terminus packing | 2 |
| surface / unresolved | 7 |

The full table is `results/disease_variant_table.md`.

What this supports: the dominant structural reason for loss of function is disruption of
helix packing (a charge, a proline or a much larger or smaller side chain at a buried
position), not loss of a GnRH contact. That is the structural counterpart of the
published finding that most disease mutants are misfolded and retained in the
endoplasmic reticulum, and many are rescued by pharmacoperones. Only four variants are
at residues that touch GnRH in the active complex: R38Q (3.6 A), Q174R (4.1 A), Y283H
(2.8 A) and Y284C (3.5 A).

What it does not show: the rules cannot tell a folding defect from a signalling defect at
a buried position. Seven variants get no structural call: N10K is not modelled; T32I,
I37S, L137P and L166P are lipid-facing or only moderately buried; and R262Q and R262W sit
just outside the 4.5 A contact cutoff (see Result 2).

## Result 2. The three variant classes that the literature separates are structurally distinct

- **Partial loss of function, reduced affinity (N10K, G99E, Q106R).** All three are
  extracellular. Q106 sits in extracellular loop 1 at 5.8 A from GnRH and G99 at 6.8 A:
  near the hormone but not in contact, which fits a lowered affinity without loss of
  the fold. N10 is in the unmodelled N-terminus.
- **Partial loss of function, impaired coupling (R262Q).** R262 (6.30) is at the
  cytoplasmic end of helix 6, 32 A from GnRH and 5.2 A from G-alpha-q in the active
  complex. It does not touch the G protein itself, but its neighbours A261, K264 and
  T265 are within 4 A of G-alpha-q. The reported phenotype (normal binding, reduced
  phospholipase C activation) is what a residue at the edge of the G-protein interface
  would give. R262W is also classified pathogenic in ClinVar.
- **Complete loss of function.** These are the buried-core and motif variants: E90K
  (2.53, relative SASA 0.02), A129D (3.40), V134G (3.45), A171T (4.57, SASA 0.00), L266R
  (6.34), P282R (6.50) and the DRS-motif variants R139H and R139C (3.50, 3.7 A from
  G-alpha-q).

## Result 3. The crystal structure does not show a Glu90-Lys121 salt bridge

| Distance in 7BR3 | A |
|---|---|
| Glu90 carboxylate to Lys121 NZ | 9.85 |
| Glu90 carboxylate to Ser124 OG | 5.13 |
| Glu90 carboxylate to Trp280 NE1 | 5.10 |
| Asp98 carboxylate to Lys121 NZ | 2.92 |
| Cys114 SG to Cys196 SG | 1.86 |
| Ala171 CB to Tyr119 OH | 4.83 |

The E90K mutant has been explained as loss of an E90-K121 salt bridge (PMID:19095769,
PMID:22918878). In the human crystal structure the two side chains are 9.9 A apart, so
there is no such bridge in the antagonist-bound state; Lys121 instead pairs with Asp98
(2.9 A), and both contact the ligand. Glu90 is fully buried (relative SASA 0.02, ten
neighbours) at 5.1 A from Ser124 and Trp280, consistent with the alternative proposal
that it belongs to the conserved interhelical network (PMID:30476558). E90K therefore
puts a lysine into a buried polar pocket in the helix 2-3-6 interface. Caveats: 7BR3 is
one conformation, with elagolix bound and P128K introduced seven residues from Lys121.

Ala171 CB is 4.8 A from the Tyr119 hydroxyl, so a threonine at 171 could reach it, which
is the hydrogen bond proposed for A171T (PMID:12679486). A171V, classified likely
pathogenic in ClinVar, cannot form that bond but is still a larger side chain at a
position with zero solvent exposure, so the common factor is the packing, not the bond.

## Result 4. Lys191 and the Cys14-Cys200 bridge cannot be examined experimentally

Lys191 and Cys14 are not modelled in 7BR3. In the AlphaFold model the Cys14-Cys200
sulfurs are 2.05 A apart (a disulfide), but the confidence there is low (pLDDT 53.7 at
Cys14, 55.9 at Lys191, 32.8 at Asn10), so this is a prediction and not a measurement.
Across the orthologues, residue 191 is Lys only in human; it is Glu in bovine, sheep,
pig, yak, guinea pig, dog and horse, Gly in the brushtail possum, and absent in mouse
and rat. The pig sequence has Gly at 200, so the pig receptor used for 9U4W cannot form
a Cys14-Cys200 bridge. C200Y and Y108C (which is reported to capture Cys200 in an
aberrant bridge) both act on this region; the structures neither confirm nor refute the
proposed mechanism.

## Result 5. Population data: recessive, with two frequent partial-loss alleles that are not depleted as homozygotes

gnomAD v4 constraint: pLI 0.02, observed/expected loss of function 0.50 (0.33-0.78),
observed/expected missense 0.96. The gene tolerates heterozygous loss of function, as
expected for a recessive disorder. 40 high-confidence predicted loss-of-function
variants have a cumulative allele frequency of 7.3e-05 and no homozygotes.

| Allele | gnomAD exome allele frequency | homozygotes observed | expected under Hardy-Weinberg |
|---|---|---|---|
| Q106R | 0.00366 | 8 | 9.8 |
| R262Q | 0.00155 | 7 | 1.8 |
| P146S | 0.00109 | 3 | 0.9 |

Q106R and R262Q are the two alleles reported as partial loss of function and as the
most frequent in patients. Their homozygotes are present in gnomAD at about the number
expected for Q106R and above it for R262Q. The expectation uses the pooled frequency and
ignores population structure, which inflates observed homozygotes, so "above expected"
is not evidence of anything. The robust statement is the negative one: homozygosity for
these alleles is not depleted in a population database. Either the genotype is
incompletely penetrant, or it causes a mild or reversible phenotype that does not
exclude people from such cohorts. gnomAD has no phenotypes, so this analysis cannot say
which.

P146S (34.50, 3.6 A from G-alpha-q, conserved in all ten mammals) is listed by UniProt
as an HH7 variant, has conflicting classifications in ClinVar, and has four homozygotes
in gnomAD (three in exomes, as in the table, and one in genomes). Position alone would predict a coupling defect; the frequency argues against
a fully penetrant recessive allele. No functional assay was found for it.

## Contact lists (human numbering)

- GnRH, within 4 A in 9U4W: Pro29, Arg38 (1.35), Asp98 (2.61), Trp101 (2.64), Asn102
  (2.65), Lys121 (3.32), Met125 (3.36), Phe178 (4.64), Phe193, Gln195, Val197, Thr198,
  Thr215 (5.42), Leu219 (5.46), Tyr283 (6.51), Tyr284 (6.52), Gly287 (6.55), Tyr290
  (6.58), Trp291 (6.59), Met296, Leu297, Asn305 (7.35), His306 (7.36), Phe309 (7.39).
- G-alpha-q, within 4 A in 9U4W: Met76 (2.39), Asp138 (3.49), Arg139 (3.50), Ala142,
  Ile143, Pro146, Leu147, Ser151, Asn152, Ile258, Ala261 (6.29), Lys264, Thr265 and the
  C-terminal Leu328.
- Elagolix, within 4 A in 7BR3: Ile21, Pro22, Leu23, Gln25, Gly26, Asn27 (the receptor
  N-terminus), Asp98, Asn102, Ile103, Lys121, Thr215, Phe216, Leu219, Tyr283, Leu286,
  Gly287, Met296, Leu297, Asn305, Phe308.

## Limits

- Ascertainment: the disease set is not a random sample. Variants are in ClinVar and in
  the literature partly because they were found to affect function, and transmembrane
  variants are easier to call pathogenic, so the burial enrichment describes the reported
  set and is not an unbiased estimate of where damaging variants fall.

- All distances are between heavy atoms. 9U4W is deposited with hydrogens; an earlier
  version of the script kept them on the GnRH and G-alpha-q side, which made those
  distances up to 0.8 A too short. Corrected 2026-11-26.

- One inactive human structure and one active pig structure; no human active structure
  and no structure of any mutant.
- Relative SASA is computed on the receptor chain alone, so lipid-facing residues count
  as exposed.
- The structural classes are rules, not energies. No stability calculation (FoldX,
  Rosetta) was run.
- Conservation uses ten reviewed mammalian sequences aligned pairwise to human.
