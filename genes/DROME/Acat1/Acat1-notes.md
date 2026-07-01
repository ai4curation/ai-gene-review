# Acat1 (Drosophila melanogaster) research notes

UniProt: Q9W3N9 (unreviewed / TrEMBL). Gene: Acat1 / CG10932 / FBgn0029969, X chromosome.
Protein: 410 aa, thiolase-like superfamily (Thiolase family). EC 2.3.1.9 asserted.
Ortholog of human ACAT1 (P24752), mitochondrial acetoacetyl-CoA thiolase ("T2").

## Identity and orthology

- UniProt SubName: "Acetyl-CoA acetyltransferase 1, isoform A/B"; EC=2.3.1.9 (and generic 2.3.1.-, 2.3.-.-)
  asserted from EMBL translation. [file:Acat1-uniprot.txt lines 6-10]
- SIMILARITY: "Belongs to the thiolase-like superfamily. Thiolase family." (ARBA/RuleBase).
  [file:Acat1-uniprot.txt line 185-186]
- Two thiolase Pfam domains: Thiolase N-terminal (PF00108, 25..281) and Thiolase C-terminal
  (PF02803, 290..409). CDD cd00751 thiolase; TIGR01930 AcCoA-C-Actrans. FunFam matches
  "acetyl-CoA acetyltransferase, mitochondrial". PANTHER PTHR18919:SF156 "ACETYL-COA
  ACETYLTRANSFERASE, MITOCHONDRIAL". [file:Acat1-uniprot.txt lines 224-241]
- Active-site residues annotated (PIRSR): Cys109 (acyl-thioester intermediate), His368 and Cys396
  (proton acceptors) — the canonical thiolase Cys-His-Cys catalytic triad. [file:Acat1-uniprot.txt
  lines 256-264]
- DIOPT: Silva et al. 2022 call CG10932 "the orthologue of the human mitochondrial acetoacetyl-CoA
  thiolase ACAT1, CG10932 (DIOPT score level of homology and conservation: 15 of 15)".
  [PMID:35177854 "the orthologue of the human mitochondrial acetoacetyl-CoA thiolase ACAT1, CG10932
  (DIOPT score level of homology and conservation: 15 of 15"]
- Reactome (fly): R-DME-70895 Branched-chain amino acid catabolism; R-DME-77108 Utilization of Ketone
  Bodies; R-DME-77111 Synthesis of Ketone Bodies. [file:Acat1-uniprot.txt lines 209-211]

## Key experimental fly paper: Silva et al. 2022, Nat Metab (PMID:35177854, full text available)

This is the only substantive functional study in Drosophila. It uses fly Acat1 (CG10932) directly:

- Acat1 is "a key enzyme of KB oxidation", the fly ACAT1 ortholog; RNAi knockdown in adult mushroom
  body (MB) neurons was used. [PMID:35177854 "we targeted a key enzyme of KB oxidation17,18, the
  orthologue of the human mitochondrial acetoacetyl-CoA thiolase ACAT1, CG10932"]
- Function in vivo: "In neurons, during starvation, KBs are used by ACAT1 to generate acetyl-CoA in
  the mitochondria for energy". [PMID:35177854 "In neurons, during starvation, KBs are used by ACAT1
  to generate acetyl-CoA in the mitochondria for energy"] => this is ketone-body CATABOLISM / ketolysis
  (acetoacetyl-CoA -> 2 acetyl-CoA), i.e. the OXIDATION direction, consistent with human T2 ketolysis.
- Phenotype: "Downregulation of ACAT1 expression in the adult MB induced a strong memory impairment in
  starved flies". [PMID:35177854 "Downregulation of ACAT1 expression in the adult MB induced a strong
  memory impairment in starved flies"] Confirmed with a second non-overlapping RNAi.
- Expression: "the expression levels of ACAT1 and Sln, the genes required for K-AM in neurons, did not
  change in the heads of starved wild-type flies". [PMID:35177854 "the expression levels of ACAT1 and
  Sln, the genes required for K-AM in neurons, did not change in the heads of starved wild-type flies"]

IMPORTANT curation note: In this paper, ketone-body *synthesis* (ketogenesis) in cortex glia is
attributed to "the successive actions of a thiolase, the HMGS and the HMG-CoA lyase" — the thiolase
step of ketogenesis is described generically, and the gene tested/assayed as ACAT1/CG10932 is the
NEURONAL KB-OXIDATION (catabolism) enzyme, not a demonstrated ketogenic enzyme. So the GOA NAS
annotations (PMID:35177854) to "ketone body biosynthetic process" (GO:0046951) and "ketone
biosynthetic process" (GO:0042181) are, if anything, the LESS well-supported reading of this paper for
Acat1; the paper's direct evidence for CG10932 is ketone-body OXIDATION/catabolism. (Thiolase chemistry
is reversible, so the enzyme can in principle act in both ketogenesis and ketolysis, as in mammals; but
the fly experimental evidence here is for the catabolic/oxidation role.)

## GOA annotations to review (Acat1-goa.tsv)

MF:
- GO:0003985 acetyl-CoA C-acetyltransferase activity — IBA (GO_REF:0000033); IEA (EC:2.3.1.9,
  GO_REF:0000003); ISS from human P24752 (GO_REF:0000024). CORE. Multiple concordant lines.
- GO:0016453 C-acetyltransferase activity — ISS (parent of GO:0003985). Non-core (less specific).
- GO:0016746 acyltransferase activity — IEA InterPro (broad parent). Non-core.
- GO:0016747 acyltransferase activity, transferring groups other than amino-acyl groups — IEA InterPro.
  Non-core.
(metal ion binding GO:0046872 IEA-UniProtKB-KW appears in the UniProt DR block but NOT in goa.tsv, so
it is not in existing_annotations to review. T2 is K+-activated; a "potassium ion binding" would be more
apt than generic metal binding, but neither is in the GOA set here.)

CC:
- GO:0005739 mitochondrion — IBA (is_active_in), HDA (PMID:19317464 LOPIT organelle proteomics), ISM
  (PMID:22758915 peroxisome-inventory prediction). CORE localization. Human T2 is mitochondrial matrix;
  fly ortholog expected same. LOPIT (PMID:19317464) is direct MS-based organelle mapping in embryos.
- GO:0005777 peroxisome — ISM (PMID:22758915). This is a computational targeting-signal prediction from
  a Drosophila peroxisomal-proteome inventory. The human ortholog is exclusively mitochondrial matrix;
  no experimental support for peroxisomal Acat1 in fly. Some thiolases (ACAA1) are peroxisomal, but the
  ACAT1/T2 subfamily is mitochondrial. Treat as low-confidence prediction -> KEEP_AS_NON_CORE or
  MARK_AS_OVER_ANNOTATED. The paper is abstract-only; it says "The subcellular localization of five of
  these predicted peroxisomal proteins was confirmed" — not stated whether Acat1 was among the confirmed
  five, so verification is not possible from cache -> lean UNDECIDED/over-annotated. Choosing
  MARK_AS_OVER_ANNOTATED given strong contrary evidence for mitochondrial matrix localization of the T2
  subfamily.

BP:
- GO:0042182 ketone catabolic process — ISS from P24752. Correct direction (ketolysis). Non-core parent
  of ketone body catabolic process.
- GO:0046952 ketone body catabolic process — ISS from P24752. CORE (ketolysis; matches Silva 2022 neuronal
  KB oxidation).
- GO:0006550 L-isoleucine catabolic process — ISS from P24752. CORE (T2 uniquely cleaves 2-methyl-branched
  2-methylacetoacetyl-CoA, final step of Ile catabolism).
- GO:0006085 acetyl-CoA biosynthetic process — ISS from P24752. Reaction-level product (thiolysis yields
  acetyl-CoA); non-core. Matches Silva 2022 "to generate acetyl-CoA".
- GO:0046951 ketone body biosynthetic process — NAS (PMID:35177854). Ketogenesis direction. Weakly
  supported for Acat1 specifically by this paper (see note above); thiolase can act in ketogenesis in
  mammals. KEEP_AS_NON_CORE (plausible but not the direct evidence).
- GO:0042181 ketone biosynthetic process — NAS (PMID:35177854). Broad parent of GO:0046951. Same as above,
  KEEP_AS_NON_CORE.

## Synthesis

Acat1 (CG10932) is the single Drosophila ortholog of human mitochondrial acetoacetyl-CoA thiolase (T2,
ACAT1, EC 2.3.1.9). It is a thiolase-family enzyme with the canonical Cys-His-Cys catalytic triad,
predicted mitochondrial, that catalyzes the reversible acetoacetyl-CoA <-> 2 acetyl-CoA thiolysis/
condensation at the heart of ketone-body metabolism and the final thiolytic step of L-isoleucine
catabolism. Direct fly evidence (Silva et al. 2022) shows it is required in mushroom body neurons for
ketone-body oxidation to generate acetyl-CoA for energy, sustaining memory under starvation.

It is NOT the cholesterol-esterifying sterol O-acyltransferase (SOAT1/SOAT2, EC 2.3.1.26, "ACAT" in the
cholesterol-metabolism literature). No cholesterol/sterol O-acyltransferase or ER-localization
annotations are present in the fly GOA set (unlike the human record, where a SOAT1 name-collision
mis-annotation had to be removed) — so no SOAT/cholesterol flag is needed here, but I note the distinction
in the description per the ortholog convention.

Core functions:
1. MF GO:0003985 acetyl-CoA C-acetyltransferase activity; directly_involved_in GO:0046952 ketone body
   catabolic process; location GO:0005739 mitochondrion.
2. MF GO:0003985; directly_involved_in GO:0006550 L-isoleucine catabolic process; location GO:0005739.
