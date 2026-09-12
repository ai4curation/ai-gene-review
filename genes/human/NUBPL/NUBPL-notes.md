# NUBPL (IND1 homolog) — review notes

UniProt: Q8TB37 (NUBPL_HUMAN). HGNC:20278. Gene synonym C14orf127. 319 aa precursor
with an N-terminal mitochondrial transit peptide (residues 1-38); mature chain 39-319
(PRO_0000184950) [file:human/NUBPL/NUBPL-uniprot.txt "TRANSIT 1..38 /note=\"Mitochondrion\""].

## Identity / family

- RecName "Iron-sulfur cluster transfer protein NUBPL"; AltNames "IND1 homolog",
  "Nucleotide-binding protein-like", "huInd1" [file:human/NUBPL/NUBPL-uniprot.txt
  "RecName: Full=Iron-sulfur cluster transfer protein NUBPL"].
- Member of the Mrp/NBP35 ATP-binding proteins family — a P-loop NTPase family of
  Fe-S cluster carrier/assembly factors [file:human/NUBPL/NUBPL-uniprot.txt
  "Belongs to the Mrp/NBP35 ATP-binding proteins family"].
- InterPro/Pfam signatures: Mrp/NBP35 ATP-bd (IPR019591), NUBPL-like (IPR044304),
  P-loop NTPase (IPR027417), Mrp-like_CS (IPR000808); PANTHER PTHR42961
  "IRON-SULFUR PROTEIN NUBPL"; CDD cd02037 Mrp_NBP35 [file:human/NUBPL/NUBPL-uniprot.txt].

## Molecular function

- COFACTOR: binds 1 [4Fe-4S] cluster (ChEBI:49883) [file:human/NUBPL/NUBPL-uniprot.txt
  "Name=[4Fe-4S] cluster; Xref=ChEBI:CHEBI:49883" / "Note=Binds 1 [4Fe-4S] cluster."].
- The Fe-S cluster is bound via a conserved CXXC motif; mutagenesis of Cys-244 and
  Cys-247 (C->A double mutant) causes a defect in complex I assembly
  [file:human/NUBPL/NUBPL-uniprot.txt "MUTAGEN 244 ... Defect in complex I assembly;
  when associated with A-247."]. The primary paper: "huInd1 can bind an Fe/S cluster
  via a conserved CXXC motif in a labile fashion" [PMID:19752196 abstract].
- ATP-binding P-loop: BINDING 75..82 ligand ATP (CHEBI:30616), ECO:0000255
  [file:human/NUBPL/NUBPL-uniprot.txt "BINDING 75..82 /ligand=\"ATP\""]. Sequence has
  the classic Walker-A/P-loop "GKGGVGKS" at ~res 74-81 (SQ line). Keywords include
  ATP-binding and Nucleotide-binding [file:human/NUBPL/NUBPL-uniprot.txt "KW ...
  ATP-binding ... Nucleotide-binding"].
- GO:0140663 "ATP-dependent FeS chaperone activity" is defined as "Binding to and
  delivering metal ions to a target protein, driven by ATP hydrolysis" (OLS/GO). This
  is the most specific MF term matching NUBPL's role as an Fe-S cluster carrier that
  delivers the cluster to Complex I subunits. It is currently only IEA (InterPro).

## Biological process

- Function (UniProt): "Iron-sulfur cluster transfer protein involved in the assembly of
  the mitochondrial membrane respiratory chain NADH dehydrogenase (Complex I) ... May
  deliver one or more Fe-S clusters to complex I subunits" (ECO:0000269|PubMed:19752196)
  [file:human/NUBPL/NUBPL-uniprot.txt "Iron-sulfur cluster transfer protein involved in
  the assembly of the mitochondrial membrane respiratory chain NADH dehydrogenase"].
- Primary evidence (PMID:19752196, Sheftel et al., MCB 2009): huInd1 is "critically
  required for the assembly of complex I". RNAi knockdown → "strong decreases in complex
  I protein and activity levels, remodeling of respiratory supercomplexes, and alteration
  of mitochondrial morphology"; loss of specific peripheral-arm subunits (NDUFS1, NDUFV1,
  NDUFS3, NDUFA13) with a 450-kDa membrane-arm subcomplex; iron associated with complex I
  reflects dependence on huInd1 [PMID:19752196 abstract, full text not cached].
- Core BP: GO:0032981 mitochondrial respiratory chain complex I assembly; the Fe-S
  delivery step also justifies GO:0016226 iron-sulfur cluster assembly.
- GO:0007005 mitochondrion organization (IMP, PMID:19752196): supported by the observed
  "alteration of mitochondrial morphology" on knockdown, but this is a downstream/
  pleiotropic consequence of loss of Complex I rather than a direct core function — keep
  as non-core.

## Localization

- Mitochondrion (SUBCELLULAR LOCATION), ECO:0000269|PubMed:19752196
  [file:human/NUBPL/NUBPL-uniprot.txt "SUBCELLULAR LOCATION: Mitochondrion"]. IDA in GOA
  from PMID:19752196 and HPA (GO_REF:0000052). Multiple Reactome TAS + ARBA IEA place it
  in the mitochondrial matrix (GO:0005759), consistent with a matrix-soluble assembly
  factor acting on the peripheral (matrix) arm of Complex I.
- HTP mitochondrion annotation from PMID:34800366 (high-confidence human mitochondrial
  proteome) — corroborating high-throughput localization.

## Interactions

- IntAct: NUBPL interacts with NUBP2 (Q9Y5Y2; NbExp=6) and KDM8/JMJD5 isoform
  (Q8N371-3; NbExp=3) [file:human/NUBPL/NUBPL-uniprot.txt "Q8TB37; Q9Y5Y2: NUBP2" /
  "Q8TB37; Q8N371-3: KDM8"]. GOA carries these as two bare GO:0005515 "protein binding"
  IPI rows from PMID:32296183 (HuRI binary interactome). NUBP2 is a cytosolic
  Fe-S-cluster (CIA) NBP35-family paralog; a Y2H interaction with NUBPL does not
  establish a specific mitochondrial molecular function, so bare "protein binding" is an
  over-annotation.
- Reactome (R-HSA-6788523, R-HSA-6788556): NUBPL transfers the [4Fe-4S] cluster to
  Complex I subunits (NDUFS1/S2/S7/S8 and NDUFV1/V2); process requires the HSPA9:HSCB
  co-chaperone (Maio et al. 2017) [reactome/R-HSA-6788523.md].

## Disease

- Mitochondrial complex I deficiency, nuclear type 21 (MC1DN21; MIM:618242), autosomal
  recessive; variants incl. G56R, D105Y, L193F [file:human/NUBPL/NUBPL-uniprot.txt
  "Mitochondrial complex I deficiency, nuclear type 21 (MC1DN21)"]. Confirms the
  physiological requirement of NUBPL for Complex I in humans (PMID:20818383, PMID:23553477).

## Reactome pathway

- DR Reactome R-HSA-6799198 "Complex I biogenesis" [file:human/NUBPL/NUBPL-uniprot.txt
  "Reactome; R-HSA-6799198; Complex I biogenesis."].

## Curation decisions (summary)

- MF core: GO:0051539 (4Fe-4S binding, IDA PMID:19752196) ACCEPT — genuine, experimentally
  supported cofactor binding. GO:0140663 (ATP-dependent FeS chaperone activity) captures
  the carrier/delivery activity; IEA accepted as the specific MF. GO:0051536 (parent
  Fe-S binding, IEA) MARK_AS_OVER_ANNOTATED (redundant parent of 0051539). GO:0005524
  ATP binding (IEA-KW): KEEP_AS_NON_CORE (P-loop present; ancillary to the chaperone
  cycle). Bare GO:0005515 protein binding IPI: MARK_AS_OVER_ANNOTATED (per policy, never
  REMOVE an IPI).
- BP core: GO:0032981 complex I assembly (IMP + IBA + IEA) ACCEPT. GO:0016226 Fe-S
  cluster assembly (IBA + IEA) ACCEPT (the Fe-S delivery step). GO:0007005 mitochondrion
  organization (IMP) KEEP_AS_NON_CORE (secondary morphology effect).
- CC: mitochondrion / mitochondrial matrix — ACCEPT the experimental IDA
  (GO:0005739, PMID:19752196) and matrix TAS/IEA; keep the broad IBA/IEA mitochondrion as
  non-core relative to the specific matrix localization.
- NUBPL is NOT a structural subunit of Complex I; do not assign NADH dehydrogenase
  (GO:0008137) activity.
