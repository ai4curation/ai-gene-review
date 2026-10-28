# pstS (GOX0537, UniProtKB:Q5FTI1) — Gluconobacter oxydans 621H

## Identity

- UniProtKB:Q5FTI1 (Q5FTI1_GLUOX), TrEMBL, 329 aa, ordered locus GOX0537, reference
  proteome UP000006375, NCBITaxon:290633 (G. oxydans strain 621H).
- Name assigned by rule, not by experiment: `DE RecName: Full=Phosphate-binding protein
  PstS {ECO:0000256|ARBA:ARBA00021889, ECO:0000256|PIRNR:PIRNR002756}`. The PIRNR
  (PIRSF002756 PstS) system is a curated UniRule, so family membership is well grounded
  even though the entry is unreviewed and `PE 3: Inferred from homology`.
- Signatures: PIRSF002756 PstS; NCBIfam TIGR00975 (3a0107s03, phosphate ABC transporter
  substrate-binding protein); InterPro IPR005673 (Phosphate ABC transporter,
  substrate-binding protein PstS); Pfam PF12849 (PBP_like_2, FT DOMAIN 25..299);
  PANTHER PTHR42996:SF1 PHOSPHATE-BINDING PROTEIN PSTS; CDD cd13565 PBP2_PstS.
- No gene name in the record (`GN OrderedLocusNames=GOX0537`); the symbol `pstS` is the
  one used throughout the Barstow-lab G. oxydans literature for the orthologous locus,
  and is used here for the folder and `gene_symbol`.

## Function

The record places the protein in the PstSCAB phosphate importer:

- [file:GLUOX/pstS/pstS-uniprot.txt "Part of the ABC transporter complex PstSACB involved in
  phosphate import."] (`CC FUNCTION`, ECO:0000256|ARBA + ECO:0000256|PIRNR:PIRNR002756)
- [file:GLUOX/pstS/pstS-uniprot.txt "The complex is composed of two ATP-binding proteins (PstB),
  two transmembrane proteins (PstC and PstA) and a solute-binding protein (PstS)."]
  (`CC SUBUNIT`)

That subunit composition is exactly the one GO:0055052 describes ("consisting of 5
subunits: two ATP-binding subunits, two membrane spanning subunits, and one
substrate-binding subunit"), so the GOA row on the parent term GO:0043190 is refined to
GO:0055052 in the review.

Localization: the entry carries **no** `CC SUBCELLULAR LOCATION` and no SignalP feature,
but (i) G. oxydans is a diderm alphaproteobacterium, so it has a periplasm; (ii) the
PBP domain starts at residue 25 (`FT DOMAIN 25..299`), leaving an N-terminal extension
`MFHRVGFIARGLAVALVVMVFGTAHSA` with the canonical tripartite Sec signal architecture
(basic n-region `MFHR`, long apolar h-region, small-residue `AHSA|ATLT` c-region/cleavage
site) and no lipobox cysteine; and (iii) the primary literature on this very system calls
PstS periplasmic [PMID:40425722 "The transmembrane sub-units PstA and PstC bind to the
periplasmic phosphate-binding protein, PstS, and to the cytoplasmic signaling protein,
PstB"]. A `NEW` IC row for GO:0042597 periplasmic space is therefore added. (Note the same
sentence mis-describes PstB, the ABC ATPase, as "the cytoplasmic signaling protein" — see
below.)

## Phosphate signalling and the bioleaching phenotype

In Pst-containing bacteria the transporter doubles as the sensor arm of the Pho regulon:

- [PMID:34795278 "Under phosphate-limiting conditions, the PstSCAB phosphate transporter
  will activate the histidine kinase PhoR, which in turn phosphorylates the transcription
  factor PhoB and activates the pho regulon, enabling phosphate solubilization and
  uptake"]
- [PMID:34795278 "In its natural environment, G. oxydans produces biolixiviants to liberate
  phosphate from minerals, not metals"]
- [PMID:34795278 "We speculate that by disrupting pstSCAB or PhoR, we prevent G. oxydans from
  sensing when there is adequate phosphate in its environment and when to stop producing
  biolixiviants."]

Knockouts of the operon in the *G. oxydans B58* background de-repress acid production and
improve leaching:

- [PMID:34795278 "The most acidic biolixiviant was produced by a disruption in the phosphate
  transport gene δpstC at pH 2.09. In fact, 4 of the 11 mutant strains that produced a more
  acidic biolixiviant were disrupted in genes involved in the phosphate-specific transport
  system (δpstA, δpstB, δpstC, and δpstS)."]
- [PMID:40425722 "ΔpstB raised bioleaching by 29.3% over wild-type, while ΔpstS raised
  bioleaching by 30.1%."]
- [PMID:40307501 "The analysis shows that ΔpstS, P112:mgdh mutant biolixiviant increases
  magnesium leaching by an average of 12% over all samples taken between 24 and 96"]

### Why none of this becomes a GO annotation here

1. **Strain.** All of the knockout work is in *G. oxydans B58* (locus tags `GO_nnnn`), not in
   strain 621H, whose GOX0537 product is the protein reviewed here. The two are orthologous
   but the phenotype has not been demonstrated for this accession.
2. **Necessity, not participation.** Deleting `pstS` raises acidification and leaching; that
   is loss of a repressive input, i.e. the gene is *required for* normal shutdown of
   acidogenesis. Under the CLAUDE.md `NEW` bar, being required for an outcome is not doing
   the work of it. The acid is made by the PQQ-dependent membrane glucose dehydrogenase, and
   the regulatory step (if it follows the E. coli paradigm) is executed by PhoR/PhoB with
   PstSCAB–PhoU as the input. No `NEW` regulatory process term is asserted; it is raised as
   a suggested question/experiment instead.
3. Mineral dissolution and REE/Mg release are chemistry performed by the secreted organic
   acid on the ore, not by the protein, so no bioleaching-related process term is proposed.

## Notes on the sources (not source defects)

- [PMID:40425722] describes "pstS, which encodes a phosphate signaling protein; and pstC,
  pstA, and pstB, which encode an ABC-type phosphate transporter", and elsewhere calls PstB
  "the cytoplasmic signaling protein". In the standard architecture (and in this entry's own
  `CC SUBUNIT`), PstS is the periplasmic substrate-binding protein and PstB is the ABC
  ATPase; signalling is a property of the assembled PstSCAB–PhoU–PhoR system, not of PstB
  alone. This is a looseness in the publication's prose, not a database record defect, so it
  is recorded here rather than in `review.source_defects`.
- CMMMech `data/records/dunite.yaml` and `data/records/allanite-concentrate.yaml` give
  Q5FTI1 the `functional_role` "Phosphate-binding protein PstS (GOX0537) associated with
  phosphate-transport regulation of organic-acid biolixiviant production." The protein-level
  part (periplasmic phosphate binding) is supported; the regulatory role is an inference from
  B58 deletion phenotypes and is not established for this protein, and the leaching numbers
  come from a combined ΔpstS + P112:mgdh strain that does not isolate pstS. CMMMech already
  marks that evidence `supports: partial`, which is the right reading. No edit was made to
  CMMMech.
