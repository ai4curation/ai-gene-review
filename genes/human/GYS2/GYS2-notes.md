# GYS2 (Glycogen synthase 2, liver; UniProtKB:P54840) — review notes

## Provenance note
Falcon deep-research provider was out of credits (HTTP 402) at review time, so no
`GYS2-deep-research-falcon.md` was generated. This review is grounded in the UniProt
record (`GYS2-uniprot.txt`), the seeded GOA (`GYS2-goa.tsv`), cached publications
(`publications/PMID_1731614.md`, `publications/PMID_9691087.md`), and cached Reactome
entries (`reactome/R-HSA-*.md`). Both cached PMIDs are abstract-only
(`full_text_available: false`).

## Core biology
GYS2 is the **liver isoform of glycogen synthase** (EC 2.4.1.11), the committed,
rate-limiting enzyme of hepatic glycogen chain elongation. It uses **UDP-glucose** as the
glucosyl donor and adds glucose units in **alpha-1,4 linkage** to the non-reducing ends of
a growing glycogen chain that has been primed by glycogenin (GYG1/GYG2); the branching
enzyme GBE1 introduces the alpha-1,6 branch points [file:human/GYS2/GYS2-uniprot.txt
"Extends the primer composed of a few glucose units formed by glycogenin by adding new
glucose units to it"; "transfers the glycosyl residue from UDP-Glc to the non-reducing end
of alpha-1,4-glucan"].

Catalytic reaction (Rhea:RHEA:18549):
`[(1->4)-alpha-D-glucosyl](n) + UDP-alpha-D-glucose = [(1->4)-alpha-D-glucosyl](n+1) + UDP + H(+)`
[file:human/GYS2/GYS2-uniprot.txt].

### Regulation
- **Allosterically activated by glucose-6-phosphate**; **phosphorylation is inhibitory**
  (reduces activity toward UDP-glucose). When non-phosphorylated the enzyme does not
  require G6P; when phosphorylated it does [file:human/GYS2/GYS2-uniprot.txt "Allosteric
  activation by glucose-6-phosphate"; "Phosphorylation reduces the activity towards
  UDP-glucose"].
- Multisite inhibitory phosphorylation by GSK3A/GSK3B (Ser-641/645/649/653), primed by
  CK2 at Ser-657; dephosphorylation by PP1 activates the enzyme (by similarity to muscle
  GYS1/P13807, P13834).

### Localization / complex
- **Cytosolic**; part of the glycogen synthase (GS)–glycogenin heterooctamer (GS tetramer +
  2 glycogenin dimers); ComplexPortal CPX-26492 (GYG1-GYS2) and CPX-26494 (GYG2-GYS2)
  [file:human/GYS2/GYS2-uniprot.txt].
- **Tissue specificity: liver** (at protein level) [PMID:1731614; file:human/GYS2/GYS2-uniprot.txt].

### Minor phosphoglucose-incorporation activity (GO:0061547)
GYS2 (like muscle GYS1) can occasionally transfer the glucosyl moiety of a
glucose-phosphate, incorporating phosphomonoesters into glycogen at a very low rate (~1 per
10,000 glucose residues); laforin (EPM2A) normally removes these phosphate groups. This is
the basis of the GO:0061547 "glycogen synthase activity, transferring glucose-1-phosphate"
annotation and of Reactome R-HSA-3780994 [reactome/R-HSA-3780994.md]. Real but minor;
kept as non-core would be defensible, but it is a genuine molecular capability so ACCEPT.

### Disease
Biallelic loss-of-function mutations in GYS2 cause **glycogen storage disease type 0, liver
(GSD 0a; MIM:240600)** — fasting ketotic hypoglycemia with low lactate/alanine, and
postprandial hyperglycemia/hyperlactatemia; hepatic glycogen is deficient. Seven missense
variants characterized in COS7 cells showed severely impaired GS activity
[PMID:9691087].

## Annotation decisions summary
- **GO:0004373** alpha-1,4-glucan glucosyltransferase (UDP-glucose donor) activity — ACCEPT
  across all evidence (IBA, IEA, EXP, IMP, ISS, IDA). Core MF.
- **GO:0005978** glycogen biosynthetic process — ACCEPT across all evidence. Core BP.
- **GO:0061547** glycogen synthase activity, transferring glucose-1-phosphate — ACCEPT
  (IEA/ARBA; TAS/Reactome). Real minor side activity (phosphoglucose incorporation).
- **GO:0005829** cytosol — ACCEPT (IEA, TAS×10, ISS). Canonical location.
- **GO:0005737** cytoplasm — ACCEPT (IBA, ISS). Broader parent, correct.
- **GO:0009749** response to glucose — KEEP_AS_NON_CORE (ISS from yeast Gsy2 P17625; plausible
  but peripheral to the core catalytic role and not experimentally verified in human).
- **GO:0005856** cytoskeleton, **GO:0005938** cell cortex, **GO:0030864** cortical actin
  cytoskeleton — MARK_AS_OVER_ANNOTATED. All three are ISS transfers from *S. cerevisiae*
  glycogen synthase Gsy2 (P17625), reflecting the yeast enzyme's association with cortical
  actin patches. Human liver GYS2 is a soluble cytosolic enzyme in a GS–glycogenin complex;
  there is no evidence it localizes to the (cortical actin) cytoskeleton or cell cortex.
  Over-propagated from a distant fungal ortholog.
