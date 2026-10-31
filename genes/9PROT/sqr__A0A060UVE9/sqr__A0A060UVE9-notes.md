# sqr (A0A060UVE9, AFERRI_11118): curation notes

- TrEMBL entry, Acidithiobacillus ferrivorans. The name, EC 1.8.5.4 and membrane location
  come from ARBA rules. PE 3. Folder named `sqr__A0A060UVE9` because 9PROT is a shared
  multi-species mnemonic and `sqr` is a common symbol with paralogs (sqr2) in the same genome.
- **Type I (SqrA)**: 94.4% identical to the characterized A. ferrooxidans SQR AFE_1792
  (B7JBP8), the closest of the five targets, with the C128/C160/C356 triad conserved
  (`file:ACIF2/AFE_1792/AFE_1792-bioinformatics/RESULTS.md`).
- Paralog sqr2 (AFERRI_20483, A0A060UMZ1, 435 aa) is *not* Type I. It is 28.6% identical to
  B7JBP8 and 89.0% identical to the A. thiooxidans Type V-like A0A543Q349 (computed ad hoc
  with the same aligner settings as RESULTS.md).
- A. ferrivorans RNA-seq [PMID:26956550] studied inorganic sulfur oxidation pathways. Only the
  abstract is cached, and it does not name this locus. Not used as support.

## Annotation decisions
- GO:0070224 (EC IEA): ACCEPT.
- GO:0016020: MODIFY to GO:0005886 plasma membrane.
- GO:0016491: TOO_GENERAL.

## CMMMech claim check
functional_role (tetrahedrite-concentrate): "Membrane-bound sulfide-quinone reductase (EC
1.8.5.4; sqr) in Acidithiobacillus ferrivorans catalyzing oxidation of sulfide to elemental
sulfur/polysulfide coupled to quinone reduction during acidophilic sulfide bioleaching".
- Activity: strong orthology inference, not measured. Role during bioleaching: not shown for
  this gene. Read it as a representative homolog, not as demonstrated function.
