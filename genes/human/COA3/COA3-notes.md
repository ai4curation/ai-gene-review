# COA3 (CCDC56 / MITRAC12) — review notes

UniProtKB: Q9Y2R0. HGNC:24990. Human, 106 aa, mitochondrial inner membrane, single-pass
membrane protein. Synonyms: CCDC56 (coiled-coil domain-containing 56), MITRAC12
(mitochondrial translation regulation assembly intermediate of cytochrome c oxidase, 12 kDa).

## Function (verified)

COA3 is a small mitochondrial inner-membrane assembly factor for **respiratory chain
complex IV (cytochrome c oxidase)**. It is **non-catalytic**.

- Along with **COX14**, it is a **core component of the MITRAC complex** (mitochondrial
  translation regulation assembly intermediate of cytochrome c oxidase), which receives
  imported nuclear-encoded CIV subunits and couples them to newly mitochondria-synthesised
  MT-CO1 [UniProt FUNCTION/SUBUNIT; PMID:23260140].
- MITRAC **couples MT-CO1 (COX1) translation to complex IV assembly**: it stabilises
  newly synthesised MT-CO1 and coordinates its progression into the assembly pathway
  [PMID:23260140; PMID:26321642 "regulates mitochondrial translation of COX1 mRNA"].
- COA3 sits in an **early CIV assembly intermediate (COX1–COA3–COX14)** together with the
  IMS twin-CX9C protein CMC1 [PMID:28082314, "the cardiomyopathy proteins COA3 and COX14";
  "CMC1 stabilizes a COX1-COA3-COX14 complex before the incorporation of COX4"].
- UniProt curation of PMID:23260140: "Required for efficient translation of MT-CO1 and
  mitochondrial respiratory chain complex IV assembly." → supports both
  GO:0033617 (CIV assembly) and GO:0070131 (positive regulation of mitochondrial translation).

Caveat on translation regulation: Bourens & Barrientos (PMID:28082314) note "whereas
human COX14 and COA3 have been proposed to affect COX1 mRNA translation" — i.e. the
translation-regulation role is supported (IMP in PMID:23260140) but framed as a proposal
in later work; the primary, most robust role is **CIV assembly / MT-CO1 stabilisation**.

## Localisation (verified)

Mitochondrial inner membrane (GO:0005743), single-pass membrane protein
[UniProt SUBCELLULAR LOCATION, PMID:23260140]. Topology: matrix (2–57), TM helix (58–78),
IMS (79–106). Also captured as "mitochondrion" (GO:0005739) by HPA IDA and by the MitoCoP
high-confidence proteome (PMID:34800366).

Complex IV membership term: current **GO:0045277** (respiratory chain complex IV);
GO:0005751 is OBSOLETE. COA3 is a MITRAC assembly-factor, not a stable subunit of the
mature holoenzyme, so I did not assert holo-CIV membership in core_functions.

## Disease

Biallelic COA3 variants → **mitochondrial complex IV deficiency, nuclear type 14
(MC4DN14, MIM:619058)**: developmental delay, sensorimotor demyelinating polyneuropathy,
exercise intolerance, obesity, short stature; decreased CIV levels/activity
[PMID:25604084, variant Y72C].

## MF assessment

No catalytic MF. Existing MF annotations:
- GO:0005515 protein binding (IPI, x3 rows): uninformative bare protein-binding →
  MARK_AS_OVER_ANNOTATED (do not REMOVE per policy).
- GO:0044183 protein folding chaperone (IDA, PMID:28082314, FlyBase): a binding-type
  MF consistent with COA3 stabilising/chaperoning newly synthesised MT-CO1. Keep, but
  the gene's *core* evolved role is assembly-factor, and the primary MC4DN14 evidence
  frames COA3 as an assembly factor rather than a general chaperone. Retained as
  non-core MF; core_functions omits an MF (assembly factor with only binding-type MF).

## Core functions (authored)

- directly_involved_in GO:0033617 (mitochondrial respiratory chain complex IV assembly)
- directly_involved_in GO:0070131 (positive regulation of mitochondrial translation)
- located_in GO:0005743 (mitochondrial inner membrane)
No molecular_function asserted (non-catalytic; only binding/chaperone-type MF).
