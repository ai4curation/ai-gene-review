# GPD1 (human) — gene review notes

UniProt: P21695 (GPDA_HUMAN). HGNC:4455. EC 1.1.1.8. 349 aa, ~37.5 kDa.

## Identity and core function

GPD1 is the **cytosolic NAD-dependent glycerol-3-phosphate dehydrogenase** (also called
alpha-glycerophosphate dehydrogenase, GPD-C / GPDH-C). It catalyses the reversible,
NAD+-dependent interconversion of dihydroxyacetone phosphate (DHAP) and sn-glycerol
3-phosphate (G3P).

- Reaction (UniProt CATALYTIC ACTIVITY): "sn-glycerol 3-phosphate + NAD(+) =
  dihydroxyacetone phosphate + NADH + H(+)" ; EC=1.1.1.8; Rhea:RHEA:11092
  [file:human/GPD1/GPD1-uniprot.txt].
- Direction note: UniProt writes the reaction as G3P + NAD+ = DHAP + NADH and annotates
  "PhysiologicalDirection=left-to-right; Xref=Rhea:RHEA:11093" [file:human/GPD1/GPD1-uniprot.txt],
  which is the **oxidative** direction (G3P -> DHAP). The predominant cellular role of cytosolic
  GPD1, however, is the **reductive** direction DHAP + NADH -> G3P + NAD+ (Reactome R-HSA-75889,
  "DHAP is converted to G3P by GPD1/GPD1L"; "GPD1/GPD1L reduces dihydroxyacetone phosphate with NADH").
  This regenerates cytosolic NAD+ and supplies G3P as the glycerol backbone for
  glycerolipid/triglyceride synthesis and the glycerol-phosphate shuttle.
- The enzyme is strictly **NAD+**-preferring: KM=140 uM for NAD vs KM=1070 mM for NADP
  ("KM=140 uM for NAD"; "KM=1070 mM for NADP" [file:human/GPD1/GPD1-uniprot.txt]). The ~10,000-fold
  higher KM for NADP means the dual-cofactor [NAD(P)+] term (GO:0047952) overstates cofactor
  breadth; GO:0141152 (NAD+) is the precise catalytic term.
- KM=92 uM for glycerol 3-phosphate [file:human/GPD1/GPD1-uniprot.txt].

## Cellular role / pathway context

GPD1 is the cytosolic half of the **glycerol-3-phosphate (glycerophosphate) shuttle**
(GO:0006127). Together with the mitochondrial inner-membrane FAD-dependent
GPD2 it transfers reducing equivalents from cytosolic NADH into the mitochondrial
ubiquinone pool. GPD1 also sits at the branch point feeding G3P into glycerolipid /
glycerophospholipid / triacylglycerol biosynthesis. Reactome models the DHAP->G3P step:
"Dihydroxyacetone phosphate (DHAP) is converted to glycerol-3-phosphate (G3P) by
glycerol-3-phosphate dehydrogenase (GPD1)... The active forms of both enzymes are
homodimers." [reactome:R-HSA-75889]. GPD1 is also placed in Reactome "Synthesis of PA"
(R-HSA-1483166) [file:human/GPD1/GPD1-uniprot.txt DR line].

## Structure / subunit

- **Homodimer** (SUBUNIT: "Homodimer. {ECO:0000269|PubMed:16460752}" [file:human/GPD1/GPD1-uniprot.txt]),
  confirmed by X-ray crystallography (PDB 1WPQ, 1X0V, 1X0X, 6E8Y, 6E8Z, 6E90, 6PYP).
  NAD-binding Rossmann fold (N-terminal) + C-terminal substrate/catalytic domain.
- NAD(+) binding residues 10-15, 41, 97, 153, 269, 296, 298; substrate residues 120, 269-270;
  proton-acceptor active site at residue 204 [file:human/GPD1/GPD1-uniprot.txt FT lines].
- Activity regulation: "Inhibited by zinc ions and sulfate. {ECO:0000269|PubMed:16460752}"
  [file:human/GPD1/GPD1-uniprot.txt].

## Localization

- **Cytoplasm / cytosol** (SUBCELLULAR LOCATION: "Cytoplasm {ECO:0000269|PubMed:7772607}"
  [file:human/GPD1/GPD1-uniprot.txt]). Consistent GOA cytosol IBA (GO:0005829) and Reactome TAS.
- Detected in **urinary extracellular exosomes** by large-scale LC-MS/MS proteomics
  [PMID:19056867]; this is a proteome-detection location, not a site of catalytic function.
  The paper is a general urinary-exosome proteome ("profile the proteome of human urinary
  exosomes ... identified 1132 proteins") and does not assign a function to GPD1.

## Disease

Biallelic GPD1 variants cause **transient infantile hypertriglyceridemia (HTGTI, MIM 614480)**,
autosomal recessive, with hepatomegaly, fatty liver and hepatic fibrosis (UniProt DISEASE;
[PMID:22226083], [PMID:24549054] — variants VAL-54, LYS-124, ALA-197, ILE-223, PRO-229).
This is consistent with GPD1's central role in hepatic glycerolipid metabolism.

## Interaction annotation

GOA has a bare **protein binding** IPI (GO:0005515) from the human binary interactome
(HuRI) Y2H screen [PMID:32296183], reporting a GPD1–FAM25A interaction (UniProt INTERACTION:
"P21695; B3EWG3: FAM25A; NbExp=3" [file:human/GPD1/GPD1-uniprot.txt]). FAM25A is a small
uncharacterised protein; this high-throughput binary interaction has no established
functional meaning for GPD1. Per curation policy, bare "protein binding" IPI is not removed
but marked as over-annotated (uninformative MF).

## Curation decisions (summary)

Core MF: **GO:0141152 glycerol-3-phosphate dehydrogenase (NAD+) activity** (verified current,
EC 1.1.1.8; GO:0004367 is OBSOLETE — do NOT use).
Core BP: glycerol-3-phosphate metabolic process (GO:0006072), glycerol-3-phosphate
biosynthetic process (GO:0046167, physiological direction), glycerol-3-phosphate shuttle
(GO:0006127).
Core CC: cytosol (GO:0005829).

Actions:
- ACCEPT: GO:0006072 (IBA); GO:0006072 (IEA InterPro); GO:0051287 NAD binding (IEA);
  GO:0141152 (IEA GO_REF:0000120); GO:0141152 (TAS PMID:7772607); GO:0005829 cytosol (IBA);
  GO:0005829 cytosol (TAS Reactome).
- MODIFY: GO:0047952 [NAD(P)+] activity (IBA) -> GO:0141152 (NAD+) — enzyme is NAD+-specific.
- KEEP_AS_NON_CORE: GO:0042803 protein homodimerization (structurally real subunit info);
  GO:0046168 glycerol-3-phosphate catabolic process (reverse/oxidative direction);
  GO:0005737 cytoplasm (IEA SubCell, less precise than cytosol);
  GO:0005737 cytoplasm (EXP PMID:7772607, less precise than cytosol).
- MARK_AS_OVER_ANNOTATED: GO:0005975 carbohydrate metabolic process (too generic);
  GO:0016616 (parent oxidoreductase class, less informative than specific MF);
  GO:0005515 protein binding (bare, HuRI Y2H); GO:0070062 extracellular exosome (MS detection).

No REMOVE actions used (all IEAs here are defensible parents/duplicates rather than
clearly wrong; experimental/bare-binding annotations are per policy not removed).
