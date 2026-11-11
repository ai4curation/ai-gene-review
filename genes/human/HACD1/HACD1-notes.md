# HACD1 (Very-long-chain (3R)-3-hydroxyacyl-CoA dehydratase 1) review notes

UniProt: B0YJ81 (HACD1_HUMAN); gene HACD1, synonym PTPLA; also known as
cementum-attachment protein (CAP, isoform 2). HGNC:9639. Human, chr 10.

## Core molecular function

HACD1 is the muscle-enriched member of the human 3-hydroxyacyl-CoA dehydratase
(HACD1-4) family. It catalyzes the **third of the four reactions of the
microsomal (ER) fatty-acid elongation cycle**: dehydration of a
(3R)-3-hydroxyacyl-CoA to a (2E)-enoyl-CoA + H2O (EC 4.2.1.134; Rhea:45812).

- UniProt RecName: "Very-long-chain (3R)-3-hydroxyacyl-CoA dehydratase 1";
  `EC=4.2.1.134 {ECO:0000269|PubMed:18554506, ECO:0000269|PubMed:23933735}`
  [file:human/HACD1/HACD1-uniprot.txt].
- FUNCTION [Isoform 1]: "Catalyzes the third of the four reactions of the
  long-chain fatty acids elongation cycle... This enzyme catalyzes the
  dehydration of the 3-hydroxyacyl-CoA intermediate into trans-2,3-enoyl-CoA,
  within each cycle of fatty acid elongation" [file:human/HACD1/HACD1-uniprot.txt].
- CATALYTIC ACTIVITY: `Reaction=a very-long-chain (3R)-3-hydroxyacyl-CoA = a
  very-long-chain (2E)-enoyl-CoA + H2O; ... EC=4.2.1.134` — plus seven
  chain-length-specific Rhea reactions (C16 through C26)
  [file:human/HACD1/HACD1-uniprot.txt].

The elongation cycle (Reactome R-HSA-75876): activation (ACSL) → condensation
(ELOVL) → 3-ketoacyl-CoA reduction (KAR/HSD17B12) → **3-hydroxyacyl-CoA
dehydration (HACD1/2)** → trans-2-enoyl-CoA reduction (TECR). The four enzyme
families "differ in their tissue-specific expression patterns and in their
substrate preferences" [reactome:R-HSA-75876].

The best-fit GO MF term is **GO:0102158 very-long-chain (3R)-3-hydroxyacyl-CoA
dehydratase activity** (def: "Catalysis of the reaction: a very-long-chain
(3R)-3-hydroxyacyl-CoA = H2O + a very-long-chain (2E)-enoyl-CoA. This reaction is
the third (dehydration) step of the four-step fatty acid elongation cycle in the
endoplasmic reticulum"; go.db). It is a subclass of the more generic
GO:0018812 3-hydroxyacyl-CoA dehydratase activity (verified is-a in go.db);
GO:0102158 is the more specific, experimentally-matched term.

## Experimental evidence

- PMID:18554506 (Ikeda et al., FEBS Lett 2008; abstract-only cache,
  `full_text_available: false`): identified all four human HACD proteins as
  3-hydroxyacyl-CoA dehydratases via PHS1-shutoff yeast complementation and/or
  in-vitro 3-hydroxypalmitoyl-CoA dehydratase assays; "We also establish that
  HACD proteins interact with the condensation enzymes ELOVL1-7, with some
  preferences" [PMID:18554506]. UniProt cites this paper for FUNCTION,
  SUBCELLULAR LOCATION (ER membrane, multi-pass), CATALYTIC ACTIVITY, PATHWAY
  (fatty acid biosynthesis), BIOPHYSICOCHEMICAL PROPERTIES (KM=33.6 uM for
  3-hydroxypalmitoyl-CoA), and SUBUNIT (ELOVL interaction). The curator read the
  full text, which is not in our abstract-only cache.
- PMID:23933735 (Muhammad et al., Hum Mol Genet 2013; full text available):
  homozygous nonsense p.Tyr248Stop in HACD1 causes autosomal-recessive
  congenital myopathy (CFTD/CMYO11). The mutation "completely abrogates the
  enzymatic activity of dehydration of 3-hydroxyacyl-CoA, the third step in the
  elongation of very long-chain fatty acids (VLCFAs)"; directly assayed
  [14C]3-hydroxypalmitoyl-CoA → 2,3-trans-hexadecenoyl-CoA and found "The
  mutation completely abrogated the enzymatic activity" [PMID:23933735].
  Notably, patient serum VLCFA levels were "found to be normal" — consistent
  with a muscle-specific/partial defect and redundancy with HACD2, not a global
  VLCFA-synthesis failure.

## Subunit / interactions

- SUBUNIT: interacts with ELOVL-family condensation enzymes (ELOVL1), "may be
  part of a larger fatty acids elongase complex" [file:human/HACD1/HACD1-uniprot.txt,
  PMID:18554506].
- SUBUNIT: "Interacts with TECR" [file:human/HACD1/HACD1-uniprot.txt,
  PMID:38422897]. PMID:38422897 (Zhou et al., BBRC 2024; abstract-only cache):
  "we confirmed the critical interactions between TECR and HACD1/2" — HACD-TECR
  physically couples the dehydration (step 3) and reduction (step 4) steps of the
  cycle. GOA records this as a bare GO:0005515 protein-binding IPI.
- PMID:32296183 (HuRI reference interactome, Nature 2020; systematic Y2H):
  high-throughput binary interactions (with CPLX4/Q7Z7G2, IL10RA/Q13651,
  RNF170-5/Q96K19-5, TECR/Q9NZ01, TMEM106C/Q9BVX2). These are recorded as bare
  GO:0005515 protein-binding IPI. HuRI is a large-scale screen; most partners are
  not functionally characterized for HACD1.

## Disease

- Congenital myopathy 11 (CMYO11; MIM:619967), autosomal recessive: biallelic
  loss-of-function HACD1 variants (PMID:23933735, PMID:32426512, PMID:33354762).
  Presents with severe neonatal hypotonia, motor delay; non-progressive with
  improvement in childhood; muscle biopsy shows type-1 fiber smallness (fiber-type
  disproportion) [PMID:23933735].

## Isoform 2 (CAP / cementum-attachment protein)

- Isoform 2 (B0YJ81-2) uses VSP_035363 + VSP_035364, lacks the C-terminal
  catalytic region, and is "Catalytically inactive since it lacks the active
  site but may have an alternative function" [file:human/HACD1/HACD1-uniprot.txt].
- Isoform 2 is implicated in cementum formation / hydroxyapatite crystal
  nucleation and cell-substrate adhesion (PMID:22067203, PMID:25263524). The
  corresponding GO terms (GO:0046848 hydroxyapatite binding, GO:0071529 cementum
  mineralization, GO:0010811 positive regulation of cell-substrate adhesion,
  GO:0065003 protein-containing complex assembly, GO:0019899 enzyme binding)
  appear in the UniProt DR GO block but are **NOT** in the 17 GOA annotations
  seeded here, so they are out of scope for this review. If added later, they
  should be tagged `isoform: B0YJ81-2` and treated as non-core (isoform-2
  moonlighting function, distinct from the canonical enzymatic role).

## Annotation review decisions (summary)

- Core MF: GO:0102158 (VLC (3R)-3-hydroxyacyl-CoA dehydratase activity) — the
  two EXP annotations (18554506, 23933735) and the IEA(120) ACCEPTED; the
  generic GO:0018812 IBA/EXP and the Rhea-derived GO:0080023 "(2E)-enoyl-CoA
  hydratase activity" IEA MODIFIED to GO:0102158 (same reaction, correct
  direction/specificity).
- Core BP: GO:0030497 fatty acid elongation, GO:0042761 very long-chain fatty
  acid biosynthetic process (both IBA) ACCEPTED.
- Core location: GO:0005789 ER membrane (IBA, IEA, EXP, TAS) ACCEPTED.
- Non-core BP: GO:0006633 fatty acid biosynthetic process (general parent),
  GO:0030148 sphingolipid biosynthetic process (downstream), GO:0035338
  long-chain fatty-acyl-CoA biosynthetic process (Reactome pathway framing).
- GO:0005515 protein binding (two IPI): MARK_AS_OVER_ANNOTATED — bare, uninformative
  MF term; not removed per experimental/IPI policy.


## 2026-11-12: primary-source reassessment

This dated reassessment supersedes the earlier action summary and its
reaction-direction, indirect-pathway and generic-binding rationales. The earlier
notes are retained as the prior curation record. Evidence access and its limits
are documented in [the manual research report](HACD1-deep-research-manual.md).

Fresh QuickGO retrieval yields 22 source rows and 21 distinct review contexts.
Five HuRI partner contexts are now separate. The HACD1–TECR annotation from
PMID:38422897 has two source-provider/date rows (IntAct and UniProt); both remain
in the downloaded TSV and map to one shared annotation context. No source row
has a target isoform, NOT flag or annotation extension. Do not convert a partner
isoform, such as RNF170-5, into an HACD1 target-isoform flag.

The reassessed draft has 15 ACCEPT and six KEEP_AS_NON_CORE actions, with no
PENDING or NEW annotation. Supported generic binding follows the ClinGen policy.
The five HuRI edges were checked in original author portal data and separately
against IntAct curation. Those assays do not establish a physiological ER role
for each partner. PMID:38422897 explicitly supports HACD1–TECR association, but
its isolated stable complex and modeled active sites concern HACD2. We make no
HACD1 substrate-channeling or adaptor-function assertion.

GO:0080023 defines the dehydration reaction despite its hydratase label.
Changing it for reaction direction would be wrong. Its Rhea-supported reaction
scope and the generic dehydratase activity remain appropriate; the specific
VLCFA enzyme-class annotation is already present. The prior PAINT granularity
failure claim is removed. The retained IBD and independent functional evidence
are respected; the actual tree/MSA was not independently retrieved.

The original PMID:18554506 directly tests C16 substrate, human HACD1 ER
localization and rescue of PHS1-suppressed yeast, including sphingolipid synthesis.
This supports catalytic participation in fatty-acid and sphingolipid precursor
biosynthesis. Pathway breadth does not by itself make those existing annotations
non-core. Neither that assay nor PMID:23933735 supplies a measured C18–C26
substrate panel. Retaining the established VLCFA enzyme-class annotation does
not imply otherwise.

Canonical HACD1-288, CAP140 and p.Tyr248Stop remain distinct. CAP lacks the
canonical catalytic region, but an independently inspected negative CAP
activity assay is not claimed. CAP mineralization annotations are absent from
this fresh GOA set; no NEW mineralization, differentiation or adhesion
annotation is introduced from the separate CAP literature.

All 18 inherited supporting-text occurrences and the seven existing
record-section fields are preserved. Source fields were seeded by the project
pipeline and are not edited as biological judgments. The draft remains DRAFT;
canonical validation, history scaffolding and PR delivery still follow.
