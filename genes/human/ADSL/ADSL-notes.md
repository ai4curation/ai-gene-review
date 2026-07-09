# ADSL (adenylosuccinate lyase) — review notes

UniProtKB:P30566 (PUR8_HUMAN). HGNC:291. EC 4.3.2.2. Chromosome 22q13.1.
Lyase 1 family, adenylosuccinate lyase subfamily.

Deep research status: falcon provider out of credits (HTTP 402); no
`-deep-research-falcon.md` generated. Review grounded in the cached UniProt
record, the seeded GOA, cached publications (PMID_10888601, 11428554, 16973378,
19405474, 27590927), and the two cached Reactome entries. PMID:19405474 is the
only one with full text available in the cache; the others are abstract-only.

## Core biology

ADSL is a **homotetrameric** cytosolic enzyme that catalyses **two distinct
beta-elimination (fumarate-releasing) reactions** in purine metabolism, both in
the same active site (three subunits contribute residues to each of the four
active sites):

1. **SAICAR lyase** (de novo IMP branch): (S)-2-(5-amino-1-(5-phospho-D-ribosyl)
   imidazole-4-carboxamido)succinate (SAICAR) → AICAR + fumarate.
   Rhea:RHEA:23920 → GO:0070626.
2. **Adenylosuccinate (S-AMP) lyase** (IMP→AMP branch): N6-(1,2-dicarboxyethyl)-
   AMP (SAMP) → AMP + fumarate. Rhea:RHEA:16853 → GO:0004018.

Both activities reside at the same active site; a single competitive inhibitor
(APBADP) blocks both, showing the two substrates occupy the same site
[PMID:19405474 full text].

Key verbatim support:
- UniProt FUNCTION: "Catalyzes two non-sequential steps in de novo AMP synthesis"
  and "converts succinyladenosine monophosphate (SAMP) to AMP and fumarate."
- PMID:19405474: "Adenylosuccinate lyase (EC 4.3.2.2) catalyzes two β-elimination
  reactions in the de novo synthesis of purines: the cleavage of adenylosuccinate
  (SAMP)1 to AMP and fumarate; and the conversion of 5-aminoimidazole-4-
  (N-succinylocarboxamide ribonucleotide) (SAICAR) to 5-aminoimidazole-4-
  carboxamide ribonucleotide (AICAR) and fumarate."
- PMID:19405474: "ASL, a catalyst of key reactions in purine biosynthesis, is
  normally a homotetramer in which three subunits contribute to each of four
  active sites."
- Reactome R-HSA-73800 / R-HSA-73828: "The active form of this enzyme is a
  cytosolic tetramer" and it mediates both reactions in vivo.

## Localization

Cytosol. IDA (HPA immunofluorescence, GO_REF:0000052), TAS (Reactome), IBA. Also
reported to associate with the purinosome (multi-enzyme DNPS complex) under some
metabolic conditions [Reactome R-HSA-73800; PMID:27590927].

## Disease

Adenylosuccinate lyase deficiency (ADSLD; MIM:103050), autosomal recessive.
Accumulation of dephosphorylated substrates SAICA-riboside (SAICAr) and
succinyladenosine (S-Ado); psychomotor/mental retardation, epilepsy, autistic
features. S-Ado/SAICAr ratio in CSF correlates with severity [PMID:10888601].
Many characterised missense variants reduce activity (PMID:19405474 etc).

## Annotation assessment summary

MF (core):
- GO:0004018 SAMP lyase — IDA x3 (PMID:19405474, 16973378) + IBA + IEA → ACCEPT (core).
- GO:0070626 SAICAR lyase — IDA (PMID:27590927) + IBA + IEA → ACCEPT (core).
- GO:0003824 catalytic activity (IEA/InterPro) — too general; MARK_AS_OVER_ANNOTATED
  (parent of the two specific MFs already present).
- GO:0042802 identical protein binding (IDA PMID:16973378; IEA) — homotetramer, so
  self-association is real, but bare-binding term is uninformative vs the enzymatic
  MFs and complex CC → KEEP_AS_NON_CORE (IDA), IEA duplicate KEEP_AS_NON_CORE.

CC (core = cytosol):
- GO:0005829 cytosol — IDA/TAS/IBA → ACCEPT.
- GO:0032991 protein-containing complex (IDA PMID:16973378) — homotetramer =
  protein-containing complex; correct but very general → KEEP_AS_NON_CORE.

BP:
- GO:0006189 'de novo' IMP biosynthetic process (IEA) — ACCEPT core (SAICAR→AICAR
  is step 2/2 of the IMP de novo pathway; UniProt PATHWAY).
- GO:0044208 'de novo' AMP biosynthetic process (IBA + IEA) — ACCEPT core (SAMP→AMP
  is AMP-from-IMP step 2/2; UniProt PATHWAY).
- GO:0006164 purine nucleotide biosynthetic process (IC PMID:10888601) — ACCEPT
  (correct, general parent).
- GO:0006167 AMP biosynthetic process (IDA PMID:11428554; IEA) — ACCEPT/KEEP; the
  IDA in blood cells measures AMP-producing activity.
- GO:0009152 purine ribonucleotide biosynthetic process (IEA InterPro) — ACCEPT
  (correct general parent).
- GO:0044209 AMP salvage (IEA Ensembl, GO_REF:0000107) — MISLEADING. ADSL's AMP
  production (SAMP→AMP) is part of DE NOVO synthesis (and the purine nucleotide
  cycle), not the salvage (hypoxanthine/adenine phosphoribosyltransferase) pathway.
  → MARK_AS_OVER_ANNOTATED (Ensembl ortholog electronic transfer, biologically off).
- GO:0006177 GMP biosynthetic process (IEA Ensembl) — REMOVE. GMP is made from IMP
  by IMPDH + GMPS; ADSL is not on the GMP branch. Wrong IEA ortholog transfer.
- GO:0097294 'de novo' XMP biosynthetic process (IEA Ensembl) — REMOVE. XMP is made
  from IMP by IMPDH; ADSL not involved. Wrong IEA ortholog transfer.
- GO:0009060 aerobic respiration (IEA Ensembl) — REMOVE. ADSL is a cytosolic purine
  biosynthesis enzyme; fumarate release is not participation in aerobic respiration.
  Over-propagated ortholog IEA.
- GO:0001666 response to hypoxia (IEA Ensembl) — REMOVE. No evidence ADSL itself is
  a hypoxia-response effector; electronic ortholog transfer, not supportable.
- GO:0007584 response to nutrient (IEA Ensembl) — REMOVE. Electronic ortholog
  transfer; not supportable for human ADSL.
- GO:0042594 response to starvation (IEA Ensembl) — REMOVE. Same.
- GO:0014850 response to muscle activity (IEA Ensembl) — REMOVE. ADSL is highly
  expressed in muscle and participates in the purine nucleotide cycle there, but
  "response to muscle activity" (a stimulus-response BP) is not a supportable
  molecular role for ADSL from an electronic ortholog transfer. Over-propagation.

The GO_REF:0000107 (Ensembl Compara) block of stimulus/response and off-pathway
biosynthesis terms is the classic over-propagation cluster and is treated as such.
