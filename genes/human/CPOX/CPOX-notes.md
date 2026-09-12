# CPOX (human) — curation notes

UniProt: P36551 (HEM6_HUMAN). Gene: CPOX (syn. CPO, CPX). HGNC:2321. 454 aa precursor.

Deep research note: falcon deep-research was OUT OF CREDITS (HTTP 402) at review time, so
there is no `CPOX-deep-research-falcon.md`. This review is grounded in the UniProt record
(`CPOX-uniprot.txt`), the seeded GOA (`CPOX-goa.tsv`), and the cached publications listed
below.

## Function (well established)

CPOX is the **oxygen-dependent coproporphyrinogen-III oxidase (EC 1.3.3.3)** that catalyses
the **sixth step of heme biosynthesis**: the aerobic oxidative decarboxylation of the
propionate side chains on rings A and B of coproporphyrinogen III to vinyl groups, forming
protoporphyrinogen IX. Reaction (RHEA:18257): coproporphyrinogen III + O2 + 2 H+ ->
protoporphyrinogen IX + 2 CO2 + 2 H2O.

- [PMID:8159699 "Coproporphyrinogen oxidase (EC 1.3.3.3) catalyzes the sixth step in the heme biosynthetic pathway, the oxidation of coproporphyrinogen III to protoporphyrinogen IX"] — cloning + functional expression in E. coli gave a "17-fold increase in coproporphyrinogen activity over endogenous activity" (EXP evidence for MF).
- UniProt FUNCTION: "Catalyzes the aerobic oxidative decarboxylation of propionate groups of rings A and B of coproporphyrinogen-III to yield the vinyl groups in protoporphyrinogen-IX and participates to the sixth step in the heme biosynthetic pathway."
- Human enzyme is uniquely **oxygen-dependent** (aerobic CPO family); anaerobes use HemN (radical-SAM, unrelated).

## Localization

Mitochondrial **intermembrane space**, associated with the inner membrane. Human localization
to the IMS is inferred from the homologous rat enzyme (Reactome; UniProt ISS from Q3B7D0).
- [PMID:8407975 "mammalian coproporphyrinogen oxidase is mitochondrial enzyme"] — activity mainly in mitochondria of transfected cells.
- HPA IDA (GO_REF:0000052) and mitochondrial-proteome MS (PMID:34800366) both place it in mitochondrion.

## Structure / subunit

Functions as a **homodimer**. Crystal structure (PDB 2AEX, 1.58 Å) solved; metal- and
cofactor-independent mechanism.
- [PMID:16176984 "In the biologically active dimer (K(D) = 5 x 10(-7) M), one monomer rotates relative to the second by approximately 40 degrees"] — IDA for protein homodimerization; residues 392–418 (exon 6) needed for dimerization; K404E harderoporphyria mutation impairs 2nd decarboxylation cycle.

## Disease

- **Hereditary coproporphyria (HCP; MIM 121300)** — acute hepatic porphyria; many missense/deletion mutations catalogued (e.g. PMID:9888388, systematic mutation update).
- **Harderoporphyria (HARPO; MIM 618892)** — rare erythropoietic variant; homozygous H327R (PMID:21103937) or K404E (PMID:7757079).

## GOA review summary

Core, strongly supported:
- MF GO:0004109 coproporphyrinogen oxidase activity (EXP/IDA/IBA/IEA/TAS) — ACCEPT.
- BP GO:0006783 heme biosynthetic process (IBA/IEA/TAS) — ACCEPT.
- CC GO:0005758 mitochondrial intermembrane space (ISS/TAS/IEA) — ACCEPT; GO:0005739 mitochondrion (IDA/HTP/TAS) — ACCEPT.

Reasonable but broader / peripheral:
- GO:0006779 porphyrin-containing compound biosynthetic process — broader parent of heme biosynthesis; KEEP_AS_NON_CORE.
- GO:0006785 heme B biosynthetic process (IDA from PMID:7987309) — heme b IS the product of this pathway; the cited paper is gene-organization/exon-6 skipping, an odd choice for a heme-b IDA, but the biology is correct; KEEP (heme b is the specific heme made via protoporphyrin IX). Keep as accurate downstream process; not the most direct term (protoporphyrinogen IX biosynthesis is more direct) — MARK non-core.
- GO:0005737 cytoplasm (IBA is_active_in) — IMS is the accurate compartment; cytoplasm is too broad/imprecise for this mito-IMS enzyme; MARK_AS_OVER_ANNOTATED.
- GO:0005743 mitochondrial inner membrane (IEA/Ensembl ortholog) — CPO is IMS-associated with inner membrane; plausible but the primary curated location is IMS; KEEP_AS_NON_CORE.
- GO:0016020 membrane (IEA/Ensembl) — uninformative broad CC; MARK_AS_OVER_ANNOTATED.

Ortholog-transferred stress/metal responses (all IEA from rat/mouse ortholog via Ensembl,
GO_REF:0000107) — response to iron ion, lead ion, insecticide, arsenic, methylmercury. These
are electronic transfers of environmental/toxicant response phenotypes from the rodent
ortholog; they are peripheral and not demonstrated for human CPOX; KEEP_AS_NON_CORE
(they are plausible ortholog transfers, not clearly wrong, so not REMOVE).

- GO:0042802 identical protein binding (IEA/Ensembl) — CPO is a homodimer, so identical
  protein binding is biologically true; but "identical protein binding" is a weak binding
  term. There is a directly supported, more informative IDA term GO:0042803 protein
  homodimerization activity from PMID:16176984. MODIFY GO:0042802 -> GO:0042803.
- GO:0042803 protein homodimerization activity (IDA PMID:16176984) — ACCEPT (directly shown
  by crystallography/AUC). Non-core relative to catalysis but well supported.
