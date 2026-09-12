# COS9 (YKL219W) — curation notes

*S. cerevisiae* gene, SGD standard name **COS9**, systematic **YKL219W**, UniProt **P36034**,
SGD:S000001702. Member of the DUP240/**COS** (COnserved Sequence) subtelomeric multigene family.
This is an **understudied ("dark") gene**: there is essentially **no COS9-specific experimental
characterization**. What is "known" about COS9 is (a) sequence/domain-based, and (b) inferred by
homology (ISS) from the experimentally-studied paralog **COS5** (see below). These notes carefully
separate COS9-specific evidence from family-level evidence.

## Identity / genomic context

- Subtelomeric location on chromosome XI (YKL219W). The COS family resides in subtelomeric regions
  of 9 of the 16 yeast chromosomes and comprises COS1–COS10 and COS12 (plus pseudogenes)
  [PMID:25942624 "found in subtelomeric regions within 9 of the 16 yeast chromosomes"; "The 11 COS
  genes, COS1 – COS10 and COS12, are remarkably similar at both the protein and nucleotide level"].
- 407 aa protein, MW ~48.5 kDa (UniProt P36034).

## Domain / sequence analysis (inline, from UniProt P36034 + own counts)

- **Family:** UniProt "Belongs to the DUP/COS family" {ECO:0000305}; InterPro **IPR001142** (Yeast
  membrane protein DUP/COS), Pfam **PF00674 (DUP)** ×2 copies. InterPro describes this family as
  "uncharacterized integral membrane proteins from yeast that contain internal duplications … of
  unknown function" (InterPro API for IPR001142, retrieved 2026-07). The 2× DUP Pfam hit reflects the
  internal duplication that gives the family its name (DUP = DUPlicated).
- **Topology:** UniProt annotates 3 predicted TM helices (75–95, 98–118, 261–281) by sequence analysis
  (ECO:0000255). The literature model for the family is **4 membrane-spanning segments** bridging 2
  small extracellular loops with large cytosolic N- and C-terminal tails [PMID:25942624 "predicted to
  form 4 membrane spanning segments that bridge 2 small extracellular loops and larger cytosolic N and
  C-terminal tails"]. Multi-pass membrane protein is well supported; exact TM count (3 vs 4) is a
  prediction-dependent detail.
- **Lysine content (own count on P36034 sequence):** 34 Lys / 407 = **8.4%**, consistent with the
  family observation that "Cos proteins also have a very high proportion of lysines (9% of all
  residues)" [PMID:25942624]. Two lysines (K93, K102) fall within predicted TM segments; most are in
  the cytosolic tails. This abundance of lysines is the structural basis for the family's heavy
  ubiquitination and the proposed "supply Ub in trans" mechanism — but note this is a **family-level
  mechanistic inference**; COS9's own ubiquitination sites have not been mapped.
- **TMD composition:** the family model invokes "atypical" polar/arginine residues in the TMDs as
  functionally important for cargo trapping [PMID:25942624 "Cos proteins have many residues within
  their TMDs that are atypical for such hydrophobic stretches"]. COS9's UniProt-predicted TM segments
  are largely hydrophobic with a couple of embedded lysines; a full TMD-polarity analysis was not the
  focus here.
- No catalytic domain, no signal peptide beyond the membrane-integration signals; molecular function
  is **not** assignable from domains (the family is enzymatically uncharacterized).

## What is KNOWN vs NOT-known

### KNOWN (well-supported for COS9 specifically)
- **Membrane / multi-pass membrane protein.** Domain/topology-defensible (DUP/COS integral membrane
  family; 3 predicted TM helices). GOA GO:0016020 (membrane, IEA UniProtKB-SubCell). Higher-resolution
  location for COS9 itself is inferred, not measured.

### KNOWN-by-homology (ISS from COS5; biologically plausible but not COS9-measured)
- **Endosome localization** (GO:0005768) and **MVB-sorting role** (GO:0043328, protein transport to
  vacuole involved in ubiquitin-dependent protein catabolic process via the MVB pathway). Both are GOA
  ISS annotations with `WITH/FROM: SGD:S000003922`, which is **COS5 (YJR161C)** — the experimentally
  characterized paralog — citing PMID:25942624. SGD's own COS9 summary echoes this:
  the COS family "provides ubiquitin in trans for nonubiquitinated cargo proteins" in the MVB pathway
  (yeastgenome.org locus S000001702, retrieved 2026-07).
- **Family (not COS9-specific) experimental basis** [PMID:25942624]: Cos proteins are highly
  ubiquitinated (Rsp5-dependent, with Sna3/Bsd2), self-associate into endosomal microdomains
  ("Cos corral"), trap Ub-cargo and GPI-anchored proteins, and are themselves sorted into MVB
  intralumenal vesicles; COS expression is induced under nutrient (niacin/NAD+) stress via Sir2
  de-repression of subtelomeric loci. **These experiments used the whole-family cosΔ deletion and
  Cos5 as representative; single-gene tests were done for COS1, COS2, COS4, COS5, COS6 — NOT COS9.**

### NOT known (genuine COS9 gaps)
- **Molecular function is unknown** (GOA has ND for MF, GO:0003674). The DUP/COS family has no assigned
  catalytic/binding activity; the proposed role is a structural/adaptor "supply Ub in trans / cargo
  corral" activity that has not been given a specific validated MF term even at the family level.
- **Whether COS9 is functionally equivalent to COS5** (vs specialized/pseudogene-like/redundant) is
  untested. Given the extreme sequence similarity across the family and the whole-family redundancy
  seen in cosΔ, COS9 most parsimoniously shares the family role, but its individual contribution,
  cargo preferences, expression pattern, and whether it is expressed at meaningful levels are open.
- **Phenotype:** SGD notes overexpression of COS9 causes decreased vegetative growth rate
  (yeastgenome.org S000001702); no single-deletion loss-of-function phenotype specific to COS9 is
  documented (family redundancy). BioGRID-ORCS: 0 hits in 10 CRISPR screens (UniProt DR line),
  consistent with dispensability/redundancy.

## Paralog disambiguation
- **COS5 (YJR161C, SGD:S000003922)** is the ISS source and the experimentally studied representative.
- Do NOT attribute Cos5-specific assay results (e.g. the 33-Lys→Arg Cos5KR mutant, GST-CTD Rsp5
  binding for Cos4/5/6, FRET self-association of Cos5) to COS9 as if measured on COS9. They inform the
  family model and justify homology-based (ISS) annotation, not experimental (IDA/IPI) annotation of
  COS9.

## Annotation-review reasoning (summary)
- GO:0016020 membrane (IEA) — ACCEPT; domain-defensible, core (it is a multi-pass membrane protein).
- GO:0005768 endosome (ISS from COS5) — KEEP_AS_NON_CORE / ACCEPT as homology-based; plausible steady-
  state compartment; not COS9-measured. Keep (do not REMOVE — never REMOVE a well-supported homology
  annotation on paralog grounds).
- GO:0043328 MVB protein transport to vacuole (ISS from COS5) — KEEP_AS_NON_CORE; represents the
  family role imputed to COS9 by homology. This is the best current statement of what COS9 probably
  does, but it is a process (not a molecular function) and is homology-based. Retain.
- GO:0003674 molecular_function ND — ACCEPT (accurately records that MF is unknown).

## Provenance
- PMID:25942624 (MacDonald et al., Dev Cell 2015) — primary family paper; full text cached.
- SGD locus pages S000001702 (COS9) and S000003922 (COS5), yeastgenome.org, retrieved 2026-07.
- InterPro IPR001142 API, retrieved 2026-07.
- UniProt P36034 (cached COS9-uniprot.txt).
