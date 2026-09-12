# LMBRD1 (Q9NUN5) review notes

Deep research (falcon) was unavailable (HTTP 402, out of credits). This review is grounded in the
cached UniProt record (`LMBRD1-uniprot.txt`), the seeded GOA (`LMBRD1-goa.tsv`), and cached
publications in `publications/PMID_*.md` plus `reactome/R-HSA-*.md`.

## Core biology

LMBRD1 encodes LMBD1 (Lysosomal cobalamin transport escort protein LMBD1), a 540-aa, multi-pass
(9 predicted TM helices) glycosylated lysosomal membrane protein of the LIMR / LMBR1 family.

- Identified as the gene mutated in the **cblF** inborn error of vitamin B12 (cobalamin) metabolism;
  in cblF, free cobalamin accumulates in lysosomes, hindering its conversion to the cofactors
  adenosylcobalamin (AdoCbl) and methylcobalamin (MeCbl). [PMID:19136951 "In the cblF inborn error of
  vitamin B(12) metabolism, free vitamin accumulates in lysosomes, thus hindering its conversion to
  cofactors."] The paper concludes "LMBD1 is a lysosomal membrane exporter for cobalamin."
  [PMID:19136951 "suggests that LMBD1 is a lysosomal membrane exporter for cobalamin"]
- Disease: Methylmalonic aciduria and homocystinuria, cblF type (MAHCF, MIM:277380), autosomal
  recessive. (UniProt DISEASE.)

## Mechanism / partners

- **ABCD4 escort/targeting**: LMBD1 interacts with the half-ABC transporter ABCD4 (O14678) on the ER
  membrane and is required to translocate ABCD4 from the ER to lysosomes; loss of LMBD1 lysosomal
  targeting mislocalizes ABCD4. [PMID:27456980 "the translocation of ABCD4 from the endoplasmic
  reticulum to lysosomes requires, at least in part, the lysosomal membrane protein LMBD1"]. Confirmed
  by FRET / rescue in [PMID:28572511 "ABCD4 lysosomal targeting depends on co-expression of, and
  interaction with, LMBD1"].
- **Complex with ABCD4 + MMACHC** for vectorial handoff of lysosomal B12 to the cytosolic processing
  protein MMACHC (Q9Y4U1). [PMID:25535791 "the cytoplasmic vitamin B(12)-processing protein MMACHC
  also interacts with LMBD1 and ABCD4 with low nanomolar affinity"; "membrane-bound LMBD1 and ABCD4
  facilitate the vectorial delivery of lysosomal vitamin B(12) to cytoplasmic MMACHC"].
- **Who does the actual transport?** In vitro reconstitution shows **ABCD4 alone** (ATP-dependent)
  transports cobalamin across liposomal membranes, and **LMBD1 has no cobalamin transport activity**
  on its own. [PMID:33845046 "LMBD1 exhibited no cobalamin transport activity"; "LMBD1 itself had
  neither ATPase nor cobalamin transport activities"]. So LMBD1's core, verified role is as the
  lysosomal-membrane escort/chaperone that delivers and stabilizes ABCD4 (and organizes the
  LMBD1:ABCD4:MMACHC handoff), rather than as the catalytic transporter subunit.
- Reactome models the exporter as the **ABCD4:LMBRD1** complex; notes "ABCD4 by itself in liposomes can
  mediate RCbl transport, indicating that ABCD4, not LBRD1, is directly responsible for intracellular
  RCbl transport" and "LMBRD1 stabilizes ABCD4 in the lysosomal membrane". (reactome/R-HSA-5223313.)

## Localization

- Lysosome membrane: strong experimental support (EXP/IDA) in PMID:19136951, 27456980, 28572511,
  33845046; also IBA and UniProt SubCell IEA. This is the core CC.
- ER membrane (IDA, PMID:27456980): transient/biosynthetic — ABCD4 is escorted from here; part of the
  mechanism, non-core steady-state location.
- Plasma membrane / clathrin-coated vesicle / clathrin-coated endocytic vesicle / membrane (HDA):
  a minor pool at the plasma membrane is reported in the mouse ortholog (INSR endocytosis adaptor
  role, By similarity, Q8K0B2). Human evidence is ISS/IEA (from mouse) or a broad membrane proteome
  HDA. Non-core.

## Secondary / By-similarity functions (mouse ortholog Q8K0B2)

- Adaptor for clathrin-mediated endocytosis of the insulin receptor (INSR): AP-2 adaptor complex
  binding (GO:0035612), clathrin heavy chain binding (GO:0032050), insulin receptor internalization
  (GO:0038016), clathrin-dependent endocytosis (GO:0072583). All are ISS/IEA transferred from the
  mouse ortholog (Q8K0B2). YERL (232-235) and WTKF (294-297) motifs mediate AP-2 binding (UniProt
  MOTIF, By similarity). Keep as non-core (not the cobalamin function, transferred by similarity).
- Gastrulation (GO:0007369): "Essential for the initiation of gastrulation..." — By similarity to
  mouse (Q8K0B2). ISS/IEA. Non-core developmental role.

## Isoform 3 / NESI (microbial infection)

Isoform 3 (NESI, lacks 73 N-terminal aa) may facilitate assembly/nuclear export of hepatitis delta
virus large antigen (PMID:15956556, not in GOA). Not a GO annotation here; noted for completeness.

## GOA notes

- The GOA (`LMBRD1-goa.tsv`) has **40 annotation lines**. The ai-review stub has 38 review entries; it
  collapses the two PMID:25535791 IPI lines (one with_from O14678/ABCD4, one with_from Q9Y4U1/MMACHC)
  into a single entry. Both interactions are real (UniProt SUBUNIT). I keep the single stub entry and
  note both partners.
- MF terms present in GOA (F-aspect): GO:0015420 (ABC-type vitamin B12 transporter activity, IDA
  PMID:33845046), GO:0090482 (vitamin transmembrane transporter activity, IDA PMID:27456980),
  GO:0005515 (protein binding, several IPI), GO:0032050 (clathrin heavy chain binding, ISS/IEA),
  GO:0035612 (AP-2 adaptor complex binding, ISS/IEA). So an F-aspect term IS present.
- The MF transporter terms are complicated: PMID:33845046 (source of the GO:0015420 IDA) actually
  demonstrated the transporter activity resides in **ABCD4**, and that **LMBD1 has no transport
  activity**. So annotating "ABC-type vitamin B12 transporter activity" directly to LMBD1 as an
  enabled MF is an over-annotation (the complex/ABCD4 transports; LMBD1 is the escort). Same logic for
  GO:0090482 vitamin transmembrane transporter activity (IDA PMID:27456980 — that paper is about
  escorting ABCD4, not demonstrating LMBD1 transport). These are marked MARK_AS_OVER_ANNOTATED /
  contributes-to at the complex level rather than removed (LMBD1 is a bona fide subunit of the
  transporting complex).

## Core functions (my synthesis)

1. Lysosomal-membrane escort/chaperone that targets and stabilizes ABCD4 (protein localization to
   lysosome; GO:0061462) — verified experimentally.
2. Part of the LMBD1:ABCD4 complex that exports cobalamin from the lysosomal lumen to the cytosol
   (cobalamin transport GO:0015889 / vitamin transmembrane transport) — as a complex subunit; the
   catalytic transport is ABCD4's.
3. Localizes to the lysosomal membrane (GO:0005765).
