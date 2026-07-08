# PGAM2 (human) — gene review notes

UniProtKB: P15259 (PGAM2_HUMAN). HGNC:8889. Gene on chromosome 7.
Synonyms: PGAMM; "muscle-specific phosphoglycerate mutase"; "phosphoglycerate mutase isozyme M" (PGAM-M).

## Core biology (from PGAM2-uniprot.txt and Reactome)

- PGAM2 is the **muscle (M) subunit** of phosphoglycerate mutase, a member of the
  **cofactor-dependent phosphoglycerate mutase / histidine-phosphatase superfamily**
  (BPG-dependent PGAM subfamily). UniProt SIMILARITY: "Belongs to the phosphoglycerate
  mutase family. BPG-dependent PGAM subfamily."
- FUNCTION (UniProt): "Catalyzes the interconversion of 3- and 2-phosphoglycerate with
  2,3-bisphosphoglycerate as the primer of the reaction. Can also catalyze the
  interconversion of (2R)-2,3-bisphosphoglycerate and (2R)-3-phospho-glyceroyl phosphate,
  but with a reduced activity." → primary EC 5.4.2.11 (PGAM, GO:0004619); minor
  EC 5.4.2.4 (bisphosphoglycerate mutase, GO:0004082).
- Mechanism: phospho-histidine intermediate. ACT_SITE 11 = "Tele-phosphohistidine
  intermediate"; ACT_SITE 89 = "Proton donor/acceptor". Catalytic His at position 11 is
  the classic His-phosphatase-fold catalytic residue; 2,3-BPG is the required cofactor/primer.
- Reaction (Rhea:RHEA:15901): (2R)-2-phosphoglycerate = (2R)-3-phosphoglycerate. Reversible;
  step 8 of the glycolytic payoff phase (3-PG → 2-PG going toward pyruvate) and the reverse
  step in gluconeogenesis.
- Cytosolic. Human PGAM is a **dimer** of M (PGAM2) and B (PGAM1) subunits; muscle is
  essentially the PGAM2 homodimer (SUBUNIT: "Homodimer"). Reactome R-HSA-71445/71654:
  "erythrocytes express only PGAM1, while skeletal muscle expresses only PGAM2."
- TISSUE SPECIFICITY (UniProt, PubMed:2822696): "Expressed in the heart and muscle. Not
  found in the liver and brain." HPA: group-enriched heart muscle, skeletal muscle, tongue.

## Disease

- **Glycogen storage disease X (GSD10 / GSD X); muscle phosphoglycerate mutase deficiency**
  (MIM:261670). UniProt DISEASE: "characterized by myoglobinuria, increased serum creatine
  kinase levels, decreased phosphoglycerate mutase activity, myalgia, muscle pain, muscle
  cramps, exercise intolerance." Variants: Glu89Ala, Arg90Trp (PubMed:8447317), Gly97Asp
  (PubMed:10545043).
- Original clinical description: DiMauro et al. 1981 (PMID:6262916) — first human muscle
  PGAM deficiency: muscle PGAM activity 5.7% of lowest control in a patient with exercise
  intolerance and recurrent pigmenturia (myoglobinuria); residual activity was the brain
  (BB) isoenzyme, "suggesting a genetic defect of the M subunit which predominates in
  normal muscle." This grounds the IMP GO:0004619 / GO:0006096 annotations. The
  striated-muscle-contraction annotation (GO:0006941) from the same paper is a phenotype
  (exercise intolerance/cramps) rather than a direct role of PGAM2 in the contractile
  mechanism → MARK_AS_OVER_ANNOTATED.

## GO annotation assessment summary

Molecular function — CORE:
- GO:0004619 phosphoglycerate mutase activity: multiply supported (IBA, IEA×2, EXP, ISS, IMP).
  ACCEPT the well-grounded ones (IBA anchor; EXP PMID:4827367 isozyme/enzyme-marker; IMP
  PMID:6262916 deficiency). This is the core MF.
- GO:0004082 bisphosphoglycerate mutase activity (IEA GO_REF:0000120 EC 5.4.2.4; ISS
  GO_REF:0000024 from PGAM1 P18669): real minor/secondary activity per UniProt FUNCTION.
  ACCEPT but note it is the reduced-activity side reaction, not the core physiological role.
- GO:0016868 intramolecular phosphotransferase activity (IEA InterPro): correct parent
  (isomerase EC 5.4.2.-); a bit general → ACCEPT (IEA allowed to be broader).
- GO:0003824 catalytic activity (IEA InterPro): root-level, uninformative but not wrong.
  MARK_AS_OVER_ANNOTATED (root filler).
- GO:0005515 protein binding (IPI ×3: PMID:28514442 BioPlex2, PMID:33961781 BioPlex3,
  PMID:32296183 HuRI). Bare "protein binding" is uninformative. Per policy: do NOT REMOVE
  IPI protein-binding; MARK_AS_OVER_ANNOTATED. Note the recurrent BPGM (P07738) partner is
  biologically sensible (both act on 2,3-BPG / glycerate phosphates).
- GO:0042802 identical protein binding (IPI PMID:32296183, self P15259): consistent with
  the documented homodimer → ACCEPT (informative self-association / dimerisation).

Biological process:
- GO:0006096 glycolytic process (IEA GO_REF:0000120; IMP PMID:6262916): core. ACCEPT.
- GO:0061621 canonical glycolysis (IBA; IEA GO_REF:0000107; TAS Reactome): more specific
  glycolysis child, core. ACCEPT (IBA).
- GO:0006094 gluconeogenesis (IEA Ensembl; TAS Reactome R-HSA-70263): PGAM catalyses the
  reversible step also used in gluconeogenesis. Physiologically gluconeogenesis is
  liver/kidney (which express PGAM1, not PGAM2 — muscle does not do gluconeogenesis).
  Reaction chemistry is shared but the muscle isoform's physiological role is glycolysis.
  Keep the Reactome TAS as ACCEPT (reaction participates in the pathway) and KEEP_AS_NON_CORE
  for the Ensembl-orthology IEA (not the muscle isoform's core in-vivo role).
- GO:0007283 spermatogenesis (IEA Ensembl, from rat P16290): orthology-transfer, not a
  direct PGAM2 function; sperm express glycolytic enzymes but this is a phenotypic/context
  transfer. KEEP_AS_NON_CORE.
- GO:0046689 response to mercury ion (IEA Ensembl, rat P16290): PGAM M subunit is
  Hg-inhibitable (DiMauro 1981 used mercury inhibition to distinguish M vs BB isozymes),
  but "response to mercury ion" as a BP is an orthology artifact, not a core biological role
  → MARK_AS_OVER_ANNOTATED.
- GO:0006941 striated muscle contraction (IMP PMID:6262916): the deficiency causes
  exercise intolerance/cramps, but PGAM2 is not part of the contractile machinery; this is
  a downstream phenotype → MARK_AS_OVER_ANNOTATED.

Cellular component:
- GO:0005829 cytosol (IBA; IEA GO_REF:0000107; TAS Reactome ×2): core location. ACCEPT (IBA).
- GO:0005634 nucleus (IEA Ensembl; HDA PMID:21630459 sperm-nucleus proteome): proteomic
  detection in isolated sperm nuclei; likely soluble-enzyme contamination / not the site of
  its enzymatic action → MARK_AS_OVER_ANNOTATED.
- GO:0005654 nucleoplasm (IDA HPA immunofluorescence, GO_REF:0000052): HPA IF; abundant
  glycolytic enzyme, nuclear signal not linked to a nuclear function → MARK_AS_OVER_ANNOTATED.
- GO:1990917 ooplasm (IEA Ensembl, rat P16290): orthology transfer to oocyte cytoplasm;
  not established for human muscle isoform → KEEP_AS_NON_CORE (it is still cytoplasm).
- GO:0070062 extracellular exosome (HDA PMID:23533145 prostatic-secretion exosomes):
  high-throughput exosome proteome; ubiquitous cytosolic enzyme frequently co-purifies →
  MARK_AS_OVER_ANNOTATED.

## Interactome partners (from UniProt INTERACTION + IPI refs)
- BPGM P07738 (bisphosphoglycerate mutase) — recurrent, NbExp=6; biologically related enzyme.
- CLVS2 Q5SYC1, DYNC1LI1 Q9Y6G9, KATNAL1 Q9BW62 — Y2H/AP-MS partners, unclear functional link.
- PGAM2 P15259 self — homodimer.
These support only generic protein binding + identical protein binding; no informative
complex/adapter MF is warranted.

## Deep research
falcon deep-research provider is OUT OF CREDITS (HTTP 402) at review time; no
-deep-research-falcon.md was generated. Review grounded in UniProt (P15259), the seeded GOA,
cached PMIDs, and cached Reactome entries.
</content>
