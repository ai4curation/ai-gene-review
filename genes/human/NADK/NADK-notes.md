# NADK (human) — review notes

UniProt: O95544 (NADK_HUMAN), gene symbol NADK, HGNC:29831, GeneID 65220, chromosome 1p36.33.
446 aa, ~49 kDa. EC 2.7.1.23. Evidence at protein level (PE 1).

## Core identity and function

NADK is the human **cytosolic NAD kinase** — the enzyme that phosphorylates NAD(+)
using ATP to make NADP(+). This is the committed, de novo route to the cellular
NADP(H) pool.

- UniProt RecName: `Full=NAD kinase; EC=2.7.1.23; AltName: Full=Poly(P)/ATP NAD kinase`
  [file:human/NADK/NADK-uniprot.txt].
- Catalytic activity (UniProt, from PubMed:11594753):
  `Reaction=NAD(+) + ATP = ADP + NADP(+) + H(+)` (Rhea:RHEA:18629; EC 2.7.1.23)
  [file:human/NADK/NADK-uniprot.txt].
- Cofactor: `Name=a divalent metal cation` (ChEBI:60240) — a divalent metal cation is
  required per subunit [file:human/NADK/NADK-uniprot.txt]. Reactome models this as Zn2+:
  "NADK is tetrameric and requires one divalent metal such as Zn2+ per subunit to
  function correctly" [Reactome:R-HSA-197198].
- Reactome physiological framing: "Cytosolic NAD+ kinase (NADK) catalyses the transfer
  of a phosphate group from ATP to NAD+, forming NADP+. This is the only way to generate
  NADP+ in all living organisms." [Reactome:R-HSA-197198].

## Primary experimental characterization — PMID:11594753 (Lerner et al. 2001)

This is the cloning + biochemical characterization paper, and is the source of the IDA
NAD+ kinase activity annotation, the TAS cytosol annotation, and the NAS phosphorylation /
ATP-metabolic-process annotations. Cache is **abstract-only** (`full_text_available: false`).

- "NADP is essential for biosynthetic pathways, energy, and signal transduction. Its
  synthesis is catalyzed by NAD kinase." [PMID:11594753].
- Human cDNA identified, amplified from a fibroblast cDNA library, functionally
  overexpressed in *E. coli*; encodes a ~49 kDa protein [PMID:11594753].
- "The catalytically active homotetramer is highly selective for its substrates, NAD and
  ATP." [PMID:11594753] — establishes the tetrameric, substrate-specific enzyme; supports
  IDA GO:0003951 NAD+ kinase activity.
- Substrate specificity: "It did not phosphorylate the nicotinic acid derivative of NAD
  (NAAD) suggesting that the potent calcium-mobilizing pyridine nucleotide NAADP is
  synthesized by an alternative route." [PMID:11594753]. So human NADK makes NADP(+) but
  NOT NAADP.
- Tissue distribution: "The gene is expressed in most human tissues, but not in skeletal
  muscle." [PMID:11594753]; UniProt: "Widely expressed but not detected in skeletal
  muscle." [file:human/NADK/NADK-uniprot.txt]. Kinetics (UniProt, from PubMed:11594753):
  KM 3.3 mM ATP, KM 0.54 mM NAD, Vmax 6.7 µmol/min/mg [file:human/NADK/NADK-uniprot.txt].

## Localization

Cytosolic. GOA carries: IBA is_active_in cytosol (GO:0005829, GO_REF:0000033), TAS
located_in cytosol from Reactome (R-HSA-197198), and TAS located_in cytosol from
UniProt/PMID:11594753. Reactome explicitly calls it "Cytosolic NAD+ kinase"
[Reactome:R-HSA-197198]. (The mitochondrial NAD kinase in humans is a separate gene,
NADK2/MNADK, not this locus.)

## Structure / family

- SIMILARITY: "Belongs to the NAD kinase family." [file:human/NADK/NADK-uniprot.txt].
- InterPro NADK signatures: IPR002504 (NADK), IPR017437 (ATP-NAD_kinase PpnK-type C),
  IPR017438 (ATP-NAD_kinase N); Pfam PF01513, PF20143; PANTHER PTHR20275 NAD KINASE.
  [file:human/NADK/NADK-uniprot.txt]. Basis of the InterPro IEA (GO:0019674) and PANTHER
  IBA annotations.
- Crystal / cryo-EM structures: PDB 3PFN (2.7 Å), 8KGC, 9CR3/9CR4/9CRA
  [file:human/NADK/NADK-uniprot.txt].

## Regulation

N-terminal serine phosphocluster (Ser46, Ser48, Ser50, Ser55, Ser64) documented by
large-scale phosphoproteomics [file:human/NADK/NADK-uniprot.txt, MOD_RES entries citing
PubMed:18669648, 19690332, 23186163, 24275569]. NADK activity is known from the broader
literature to be under signaling control (e.g. S6K1 phosphorylation, oxidative stress),
consistent with this phosphocluster, though the specific regulatory kinase is not
annotated in this UniProt record.

## Protein interactions (basis of the GO:0005515 IPI annotations)

All GO:0005515 "protein binding" IPI annotations derive from high-throughput
interaction/proteomics screens, not from studies of NADK's enzymatic mechanism:

- PMID:15161933 — global 14-3-3(zeta)-binding proteome (14-3-3 affinity column + MS);
  partner YWHAZ (P63104). Abstract-only. Consistent with the Ser phosphocluster / 14-3-3
  regulation model but the screen itself only reports a binding event.
- PMID:16189514 (Rual 2005, CCSB-HI1 Y2H) — partner Q8TBB1 (LNX1); high-throughput Y2H.
- PMID:25416956 (Rolland 2014 interactome map) — partner O00560 (SDCBP).
- PMID:28514442 (Huttlin 2017, BioPlex 2.0 AP-MS) — partner P63104 (YWHAZ).
- PMID:29892012 (interactome perturbation framework) — partner Q8TBB1 (LNX1).
- PMID:31515488 (variant PPI disruption screen) — partner O00560 (SDCBP).
- PMID:32296183 (HuRI, Luck 2020) — partners O00560 (SDCBP), Q49AN0 (CRY2), Q8TBB1
  (LNX1), Q9H5Z6-2 (FAM124B).
- PMID:33961781 (Huttlin 2021, BioPlex 3.0 AP-MS) — partner P63104 (YWHAZ).

UniProt INTERACTION block lists CRY2, FAM124B, LNX1, SDCBP, YWHAZ
[file:human/NADK/NADK-uniprot.txt]. None of these establishes a specific,
biologically-interpretable molecular function for NADK beyond the catalytic activity, so
the bare GO:0005515 annotations are over-annotations (kept per policy — experimental IPI,
not removed).

## Curation summary

- Core MF: **GO:0003951 NAD+ kinase activity** (IDA, PMID:11594753) + **GO:0005524 ATP
  binding** (substrate; UniProt KW). Metal-ion binding (GO:0046872, divalent cation
  cofactor) is real but a supporting KW.
- Core BP: **GO:0006741 NADP+ biosynthetic process**; also NAD+ metabolic process
  (GO:0019674) as the upstream substrate side.
- Core CC: **GO:0005829 cytosol**.
- Over-annotations: the 8 bare GO:0005515 "protein binding" IPIs (MARK_AS_OVER_ANNOTATED);
  GO:0035774 positive regulation of insulin secretion (IEA/Ensembl ortholog transfer,
  KEEP_AS_NON_CORE — indirect/organismal, not NADK's direct molecular function);
  GO:0016310 phosphorylation and GO:0046034 ATP metabolic process (NAS, generic parents of
  the specific NAD-kinase reaction — MARK_AS_OVER_ANNOTATED / generalized).
</content>
