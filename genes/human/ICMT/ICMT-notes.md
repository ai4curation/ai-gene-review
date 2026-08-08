# ICMT (human) — gene review notes

UniProt: O60725 (ICMT_HUMAN); gene ICMT (synonym PCCMT); 284 aa; EC 2.1.1.100.

## Identity and core function

ICMT is **protein-S-isoprenylcysteine O-methyltransferase** (isoprenylcysteine carboxyl
methyltransferase; also "prenylated protein carboxyl methyltransferase" PPMT /
"prenylcysteine carboxyl methyltransferase" pcCMT). It catalyzes the **third and final step
of CAAX-box protein processing**: after (1) prenylation by farnesyltransferase or
geranylgeranyltransferase-I and (2) proteolytic removal of the -AAX by RCE1, ICMT
**carboxymethylates the now C-terminal prenylcysteine** using S-adenosyl-L-methionine (SAM),
producing the prenylcysteine methyl ester and S-adenosyl-L-homocysteine (SAH).

- UniProt FUNCTION: "Catalyzes the post-translational methylation of isoprenylated C-terminal
  cysteine residues." [file:human/ICMT/ICMT-uniprot.txt, ECO:0000269|PubMed:9614111]
- UniProt CATALYTIC ACTIVITY (Rhea RHEA:21672; EC 2.1.1.100): "[protein]-C-terminal
  S-[(2E,6E)-farnesyl]-L-cysteine + S-adenosyl-L-methionine = [protein]-C-terminal
  S-[(2E,6E)-farnesyl]-L-cysteine methyl ester + S-adenosyl-L-homocysteine."
  [file:human/ICMT/ICMT-uniprot.txt]
- Methyl esterification neutralizes the negative charge of the prenylcysteine and thereby
  increases membrane affinity. [PMID:19158273 "Methyl esterification neutralizes the negative
  charge of the prenylcysteine and thereby increases membrane affinity."]

Substrates include RAS and related small GTPases (Ras, Cdc42, RhoA, Rab1) and the gamma
subunits of heterotrimeric G proteins.
- [PMID:10441503 "the small monomeric G proteins and the gamma subunits of heterotrimeric G
  proteins"]
- [PMID:10441503 "comigrated with the small G proteins Ras, Cdc42, RhoA, and Rab1"]
- Also methylates certain RAB GTPases (RAB7, RAB8), where methylation is required for correct
  endomembrane localization, GTP loading and downstream NOTCH signaling.
  [PMID:29051265 "methylesterifies C-terminal prenylcysteine residues of CaaX proteins and
  some RAB GTPases"; "Thus, NOTCH signaling requires ICMT in part because it requires
  methylated RAB7 and RAB8."]

## Enzyme properties

- SAM-dependent methyltransferase; UniProt assigns SAM-binding residues (e.g. residue 190,
  197-200, 205, 210-213, 251) and a substrate-binding residue (247).
  [file:human/ICMT/ICMT-uniprot.txt]
- Belongs to the class VI-like SAM-binding methyltransferase superfamily, isoprenylcysteine
  carboxyl methyltransferase family. [file:human/ICMT/ICMT-uniprot.txt]
- Metalloenzyme: requires divalent cations for activity; 1,10-phenanthroline (metal chelator)
  strongly inhibits. Reactome models the active enzyme as ICMT:Zn2+.
  [PMID:10441503 "both membrane-bound PPMT from rat kidney and the recombinant bacterially
  expressed form of the enzyme required divalent cations for catalytic activity"; "We conclude
  from these data that metal ions are essential for the activity and the stabilization of PPMT."]
- Competitively inhibited by N-acetyl-S-trans,trans-farnesyl-L-cysteine (AFC).
  [file:human/ICMT/ICMT-uniprot.txt]

## Localization and topology

- Endoplasmic reticulum membrane; multi-pass (polytopic) membrane protein.
  [file:human/ICMT/ICMT-uniprot.txt SUBCELLULAR LOCATION]
- ICMT is NOT at the plasma membrane; restricted to the ER — so the final CAAX-modifying
  enzyme resides in membranes topologically removed from the CAAX-protein target (PM).
  [PMID:9614111 "Mammalian pcCMT was not expressed at the plasma membrane but rather restricted
  to the endoplasmic reticulum."]
- Live-cell topology: human ICMT traverses the ER membrane eight times, N and C termini in the
  cytosol; yeast ortholog Ste14p spans six times; mammalian ICMT has an N-terminal 2-TM
  extension likely regulatory. [PMID:19158273 "Icmt traverses the ER membrane eight times, with
  both N and C termini disposed toward the cytosol"; UniProt annotates 8 TRANSMEM helices,
  file:human/ICMT/ICMT-uniprot.txt]

## Biological role / disease relevance

- CAAX processing (incl. ICMT methylation) targets CAAX proteins to the plasma membrane.
  [PMID:9614111 "posttranslationally modify C-terminal CAAX motifs and thereby target CAAX
  proteins to the plasma membrane"]
- Methylation is required for plasma-membrane localization and function of RAS; ICMT is a
  validated anticancer target (KRAS-driven transformation; inhibitors such as cysmethynil).
  [reactome:R-HSA-9647977 "methylation is required for plasma membrane localization and function
  of RAS proteins, and disruption of ICMT ... inhibits ... KRAS-dependent transformation";
  reactome:R-HSA-9656775 (Cysmethynil binds ICMT:Zn2+)]
- Ubiquitously expressed; higher in cerebellum/putamen, Purkinje cells, pontine neurons.
  [file:human/ICMT/ICMT-uniprot.txt TISSUE SPECIFICITY]

## Annotation review summary

Core:
- MF **GO:0004671** protein C-terminal S-isoprenylcysteine carboxyl O-methyltransferase
  activity — strongly supported (IDA/TAS/IBA + UniProt EC 2.1.1.100 / Rhea).
- CC **GO:0005789** endoplasmic reticulum membrane — IDA/EXP/TAS + UniProt SubCell.
- BP **GO:0006481** C-terminal protein methylation — the reaction ICMT performs (final
  CAAX-processing methylation step).

Non-core / over-annotation calls:
- GO:0005783 endoplasmic reticulum: correct but less specific than ER membrane (kept).
- GO:0016020 membrane (IEA, InterPro): too general vs ER membrane → MARK_AS_OVER_ANNOTATED.
- GO:0005515 protein binding (IPI, PMID:32296183 HuRI Y2H): bare, uninformative,
  high-throughput two-hybrid partners with no functional relation to methyltransferase
  activity → MARK_AS_OVER_ANNOTATED.
- GO:0071469 cellular response to alkaline pH (IEA, ortholog transfer from rat Q9WVM4): single
  electronic ortholog inference, not part of ICMT's core biology → MARK_AS_OVER_ANNOTATED.
- GO:0006612 protein targeting to membrane (TAS, PMID:9614111): describes the downstream
  consequence of CAAX methylation on substrates, not ICMT's own molecular activity → kept as
  non-core.
</content>
