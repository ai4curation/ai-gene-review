---
title: "Rhodotorula toruloides: carbon-source fitness defects and annotation gaps"
autolink_gene_symbols: false
---

# *Rhodotorula toruloides*: carbon-source fitness defects and annotation gaps

[Back to Fungal growth and knockout phenotype resources](../FUNGAL_PHENOTYPES.md)

**Bottom line:** in genome-wide transposon fitness data for the basidiomycete
yeast *R. toruloides*, 370 genes are needed for growth on a specific carbon
source but not on glucose, and 137 of them strongly (fitness ≤ −3 in at most
six of 20 carbon conditions). These fall into recognisable catabolic modules:
aromatic compounds (96 genes), branched-chain amino acids (22), pentoses and
polyols (9), fatty acids and acetate (5) and galactose (1). The method
recovers expected enzymes, such as galactokinase on galactose and
branched-chain keto acid dehydrogenase on leucine and valine. Of the 137
strong genes, 30 have no GO annotation in UniProt, and two current entries
look like fused gene models named after the wrong half: a
3-methylcrotonyl-CoA carboxylase entry called "Nup85" and an intradiol
dioxygenase entry called "ADP-ribose pyrophosphatase".
Joining the data to UniProt takes some work, because most accessions from the
source strain have been deleted from UniProtKB.

## Data

- **Fitness:** Kim et al. 2021 (PMID:33585414), supplement Table 2, sheet
  "RB-TDNA Seq". Gene fitness scores (log2 ratios; no t statistics) for 6,409
  genes with data, out of 8,344 rows, across 27 conditions. Seven conditions
  come from Coradetti et al. 2018 (PMID:29521624). Strain IFO0880 (NBRC 0880);
  gene ids `RTO4_<n>` are JGI protein ids from the IFO0880 v4 assembly.
- **Conditions:** three glucose controls, three glucose-plus-supplement media,
  nitrogen starvation (lipid mobilisation), and 20 alternative carbon sources:
  cellobiose, xylose, arabinose, mannose, galactose, L-lyxose, D-arabitol,
  L-arabitol, xylitol, D-ribulose, D-xylulose, acetate, lactate, oleic acid,
  p-coumarate, ferulate, benzoate, valine, leucine and phenylalanine.
- **Gene to protein mapping:** Coradetti et al. 2023 (PMID:37537586),
  supplement MOESM1, sheet "ProteinInfo", which maps every RTO4 id to a 2023
  UniProt accession and lists KOG/Pfam annotations and *S. cerevisiae*
  orthologs.

## Method

`scripts/rhoto_specific_phenotypes.py` calls a **specific defect** when a gene's
fitness in a carbon condition is ≤ −2 and its fitness in every glucose control
is > −1. 327 genes are excluded as sick on glucose. The thresholds are stricter
than the Fitness Browser's because there are no t statistics.
`scripts/rhoto_candidates.py` keeps the **strong** subset (strongest defect
≤ −3, defective in ≤ 6 carbon conditions) and assigns each gene to a module by
its strongest condition. A module records which growth condition needs the
gene, not what the gene does.

### Mapping to current UniProt entries

The 2023 accessions point at the IFO0880 proteome (UP000239560), now a
non-reference proteome. Of the 370 genes with a specific defect, 209 have a
2023 accession that has since been **deleted** from UniProtKB; their
sequences survive only in UniParc, with no identical active entry.
`scripts/rhoto_resolve_accessions.py` fetches each sequence from UniParc and
searches it with phmmer against the reference proteome (UP000199069, locus
tags `BN2166_*`):

| Call | Genes | Meaning |
|---|---|---|
| active | 161 | 2023 accession still in UniProtKB |
| same_gene | 146 | ≥ 90% identity over ≥ 80% of the query |
| same_gene_partial_model | 41 | ≥ 95% identity over a shorter span; the two assemblies' gene models differ in length |
| weak | 8 | lower identity; not used |
| no_hit | 14 | no significant match |

So 348 of 370 genes can be reviewed against a current UniProt entry.

## Modules

### Validation: expected enzymes are recovered

- **Galactose:** galactokinase (RTO4_13990, −4.4) and galactose-1-phosphate
  uridylyltransferase (RTO4_11332, −2.9) are needed on galactose only.
- **Branched-chain amino acids:** on leucine and/or valine, the genes needed
  are the 2-oxoisovalerate dehydrogenase E1α (RTO4_12566, −6.4), isovaleryl-CoA
  dehydrogenase (RTO4_10012), short/branched-chain acyl-CoA dehydrogenase
  (RTO4_14070), both 3-methylcrotonyl-CoA carboxylase subunits
  (RTO4_15694, RTO4_12867), methylglutaconyl-CoA hydratase (RTO4_16128),
  HMG-CoA lyase (RTO4_15693), 3-hydroxyisobutyrate dehydrogenase (RTO4_13694)
  and methylmalonate-semialdehyde dehydrogenase (RTO4_8975). That is most of
  the leucine and valine degradation routes, plus a Zn2Cys6 transcription
  factor (RTO4_15440, −6.4).
- **Pentoses and polyols:** xylose reductase (RTO4_9774, on L-lyxose and
  arabinose), two short-chain reductases (RTO4_9990, RTO4_8988) and an MFS
  transporter needed on D-ribulose, D-arabitol, xylitol and L-arabitol
  (RTO4_12976, −5.6).
- **Fatty acids and acetate:** the isocitrate lyase family member RTO4_14022
  is needed on oleic acid (−5.5) and acetate (−3.7), as expected for the
  glyoxylate cycle. Its current UniProt name is *methyl*isocitrate lyase; the
  phenotype favours isocitrate lyase, and the entry is worth checking.

### Aromatic catabolism

Benzoate, p-coumarate, ferulate and phenylalanine together account for 96 of
the 137 strong genes. Many are probably general stress genes (respiratory
chain, ESCRT, actin regulators), since benzoate and p-coumarate are also weak
acids. The strongest hits, though, carry domains that fit a fungal
β-ketoadipate pathway. That is an inference from domain annotations, not an
established function:

| Gene | Strongest defects | Domain evidence | Current UniProt | GO terms |
|---|---|---|---|---|
| RTO4_9789 | benzoate −11.4, p-coumarate −5.0 | HD domain; KEGG K06950 | A0A0K3CMN6, "HD domain containing protein" | 0 |
| RTO4_12623 | benzoate −7.5, p-coumarate −5.7 | Intradiol ring-cleavage dioxygenase (PF00775) | A0A0K3C7C1, "ADP-ribose pyrophosphatase" | 2 |
| RTO4_10304 | benzoate −7.1 | Cytochrome P450 | A0A0K3CMI5 | 4 |
| RTO4_11658 | benzoate −8.1 | Zn2Cys6 transcription factor | A0A0K3CRQ3, "predicted protein" | 4 |
| RTO4_12620 | benzoate −5.8, p-coumarate −3.9 | Carboxymuconolactone decarboxylase (PF02627) plus α/β hydrolase (PF12697) | A0A0K3CEH3, "alpha/beta hydrolase" | 0 |
| RTO4_12621 | benzoate −5.7, p-coumarate −4.2 | Dimeric α/β barrel | A0A0K3CAC0, "Uncharacterized protein" | 0 |
| RTO4_13090 | p-coumarate −6.6, benzoate −5.7, ferulate −4.1 | Succinyl-CoA:3-ketoacid CoA-transferase | A0A0K3CAS9 | 2 |
| RTO4_15228, RTO4_9065 | p-coumarate −5.5 and −5.9 | 3-oxoacyl-CoA thiolases | A0A0K3CDS0, A0A0K3C8E1 | 4 each |
| RTO4_14934 | p-coumarate −7.1, ferulate −3.5 | α/β hydrolase | A0A0K3CGB7 | 0 |

RTO4_12620, RTO4_12621 and RTO4_12623 sit at consecutive reference loci
(BN2166_0014570, _0014580, _0014600), so they probably form a gene cluster.
RTO4_9789, the strongest defect in the whole matrix, has no functional
annotation.

## Annotation problems the fitness data exposes

- **A0A0K3CAZ0** (RTO4_12867; leucine −3.4): a 1,419-residue entry carrying
  both biotin carboxylase domains (IPR005481, IPR011764, IPR005482, biotin
  attachment IPR000089) and a Nucleoporin Nup85-like domain (IPR011502). It
  is named "Nuclear pore complex protein Nup85" and annotated to both
  methylcrotonoyl-CoA carboxylase activity and the nuclear pore. This looks
  like a gene model that fuses two neighbouring genes. The IFO0880 protein
  that carries the phenotype matches it at 99.7% identity over 95% of its own
  length, and the leucine-specific defect points to the MCC α subunit, not
  to Nup85.
- **A0A0K3C7C1** (RTO4_12623): a 781-residue entry named "ADP-ribose
  pyrophosphatase" that carries α/β-hydrolase and DUF676 domains alongside
  intradiol ring-cleavage dioxygenase domains (IPR000627, IPR015889). Its GO
  terms are the dioxygenase's. The aromatic-specific defect fits the
  dioxygenase; the name fits neither domain set.
- **A0A0K3CD57** (RTO4_14022): named methylisocitrate lyase; the oleate and
  acetate phenotype fits isocitrate lyase. Both GO terms are present.
- **30 of the 137 strong genes have no GO annotation**, mostly in the aromatic
  module (25 of 96).

## Caveats

- These are fitness scores without t statistics; single-condition defects
  near −2 include noise (tubulin and histone H1 appear on single pentose
  conditions).
- A fitness defect shows that a gene is needed in a condition, not that it
  takes part in the pathway (see `CLAUDE.md`). Regulators, transporters and
  stress genes all score.
- Module assignment uses the strongest condition only; genes defective on
  both aromatic and pentose conditions are placed by the worse one.

## Next steps

1. Review the aromatic cluster (RTO4_12620, RTO4_12621, RTO4_12623), RTO4_9789
   and the mis-named carboxylase A0A0K3CAZ0 as gene reviews. These would be
   the first *R. toruloides* entries in this repository. A UniProt species
   folder would be `genes/RHOTO/`.
2. Report the two apparently fused gene models (A0A0K3CAZ0, A0A0K3C7C1) to
   UniProt.
3. Add t statistics if the authors' per-replicate data become available, and
   repeat with the Fitness Browser specificity criteria.

## Files

- `scripts/rhoto_specific_phenotypes.py` → `data/rhoto_specific_defects.tsv`
  (370 genes)
- `scripts/rhoto_resolve_accessions.py` (needs `uv run --with pyhmmer`) →
  `data/rhoto_accession_resolution.tsv`
- `scripts/rhoto_candidates.py` → `data/rhoto_candidates.tsv` (137 genes)

Run them in that order from the repository root. Downloads (supplements from
Europe PMC and the UniProt reference proteome) are cached in
`tmp/fungal_phenotypes/`.
