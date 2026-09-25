# A4GALT (Q9NPC4) review notes

Human **A4GALT** = Lactosylceramide 4-alpha-galactosyltransferase, a.k.a. Gb3/CD77
synthase, alpha-1,4-galactosyltransferase (Alpha4Gal-T1), P1/Pk synthase,
globotriaosylceramide synthase. EC 2.4.1.228. UniProt Q9NPC4, HGNC:18149,
chr 22q13.2, 353 aa, glycosyltransferase family 32 (CAZy GT32).

## Core molecular function

A4GALT is the enzyme that **initiates the globo-series glycosphingolipid branch**.
It transfers galactose from UDP-alpha-D-galactose, in an alpha-1,4 linkage, onto the
4-position of the terminal beta-galactose of **lactosylceramide (LacCer)**, producing
**globotriaosylceramide (Gb3Cer / CD77 / P^k antigen)** + UDP + H+.

- EC and reaction from UniProt: `EC=2.4.1.228 {ECO:0000269|PubMed:10748143}`; Rhea
  RHEA:11924 [file:human/A4GALT/A4GALT-uniprot.txt, "EC=2.4.1.228 {ECO:0000269|PubMed:10748143}"].
- UniProt FUNCTION: "Catalyzes the transfer of galactose from UDP-alpha-D-galactose in
  an alpha1,4 linkage to lactosylceramide ... to produce
  globotriaosylceramide/globoside Gb3Cer ... also known as P(k) antigen or CD77"
  [file:human/A4GALT/A4GALT-uniprot.txt].
- Expression-cloning paper (Kojima et al. 2000): "the extracts of the transfectant
  cells showed alpha1, 4-galactosyltransferase activity only on lactosylceramide and
  galactosylceramide" [PMID:10748143 abstract].
- Steffensen et al. 2000: "Expression of full coding constructs of alpha4Gal-T1 in
  insect cells revealed it encoded P(k) but not P(1) synthase activity" [PMID:10747952
  abstract]; the p (null) phenotype maps to loss-of-function A4GALT mutations
  ("A single homozygous missense mutation, M183K, was found in six Swedish individuals
  of the rare p phenotype").

The current specific GO MF term is **GO:0050512 lactosylceramide 4-alpha-galactosyltransferase
activity** (OLS def: "beta-D-galactosyl-(1,4)-D-glucosylceramide + UDP-galactose =
alpha-D-galactosyl-(1,4)-beta-D-galactosyl-(1,4)-D-glucosylceramide + UDP"), which exactly
matches the Gb3-synthase reaction. The broader GO:0008378 galactosyltransferase activity
is a correct-but-general parent (IDA in GOA); GO:0016758 hexosyltransferase activity is a
still-more-general IEA parent.

## Additional (acceptor-broadened) activities

Beyond the canonical LacCer→Gb3 reaction, the enzyme also (per UniProt CATALYTIC ACTIVITY /
FUNCTION):
- Transfers Gal to **galactosylceramide** (GalCer) → Ga2 (KM 132 uM; secondary, in vitro)
  [PMID:10748143].
- Synthesizes the **P1 glycan** epitope on paragloboside/neolacto (nLc4) and on complex-type
  N-glycans [PMID:26773500, PMID:33460651 — abstract-only, not cached locally].
- The **Q211E** variant broadens acceptor specificity to make the **NOR antigen**
  (Gal-alpha1,4-GalNAc on Gb4) and increases catalytic efficiency; underlies NOR
  polyagglutination syndrome [MIM:111400] (PubMed:22965229, 26773500, 33460651 —
  not cached locally). These are captured in UniProt but not (yet) as separate GO terms.

These extended activities are real but the **core** annotated MF remains Gb3/CD77 synthase.

## Cellular location

Golgi apparatus membrane; single-pass **type II** membrane protein (N-terminal cytoplasmic
tail 1-22, TM 23-43 signal-anchor, lumenal catalytic domain 44-353)
[file:human/A4GALT/A4GALT-uniprot.txt, "SUBCELLULAR LOCATION: Golgi apparatus membrane"; and
"Single-\nCC       pass type II membrane protein"]. Kojima et al.: "predicted a type II
membrane protein with 19 amino acids of cytoplasmic domain, 26 amino acids of transmembrane
region, and a catalytic domain" [PMID:10748143]. The GOA `GO:0016020 membrane` IDA and
`GO:0000139 Golgi membrane` (TAS/IEA/NAS) annotations are consistent; Golgi membrane is the
specific correct compartment.

## Biological process

Gb3 is the **root structure of the neutral globo-series glycosphingolipids** and the P1PK
(and GLOB) blood-group system. UniProt: "Globoside Gb3Cer/P(k)/CD77 is a root structure in
biosynthesis pathway of neutral glycosphingolipids of the globo-series"
[file:human/A4GALT/A4GALT-uniprot.txt]. Reactome R-HSA-9846477 "A4GALT transfers galactose to
LacCer ... starts the biosynthesis of globo series glycolipids". Core BP =
**GO:0006688 glycosphingolipid biosynthetic process** (IBA + TAS + NAS). The narrower
GO:0001576 globoside biosynthetic process technically begins at the Gb4 tetrasaccharide core
(one step downstream of A4GALT's Gb3 product), so GO:0006688 is the appropriate core BP.

## Physiology / disease relevance (context, not core)

- **Shiga toxin / verotoxin receptor**: Gb3/CD77 is the cell-surface receptor for Shiga toxins;
  expressing A4GALT confers toxin sensitivity. UniProt FUNCTION (Microbial infection):
  "P1 and Pk antigens are targeted by Shiga toxins (also called verotoxins), as a way to enter
  the cell". Kojima: "Transfection of the cDNA into L cells resulted in the constitution of
  sensitivity to the apoptosis with Shiga-like toxins (verotoxins)" [PMID:10748143]. This
  underlies the IEA `GO:0015643 toxic substance binding` (Ensembl) in the UniProt DR block —
  note that term is NOT in the GOA TSV, so it is not among the 15 seeded annotations.
- **Fabry disease**: Gb3 is the substrate that accumulates when the downstream lysosomal
  enzyme GLA (alpha-galactosidase A) is deficient; A4GALT itself is not mutated in Fabry.
- **Blood groups / transfusion**: A4GALT loss-of-function → rare p (null) phenotype;
  Q211E → NOR polyagglutination [MIM:111400].
- **Cancer / EMT**: A4GALT-made globo-GSLs modulate epithelial-mesenchymal transition and
  E-cadherin adhesion (PMID:29572228, not cached).

## GOA annotation-review summary (15 seeded annotations)

Molecular function:
- GO:0050512 lactosylceramide 4-alpha-galactosyltransferase activity — the specific correct MF.
  EXP (PMID:10748143) → ACCEPT (core). Two Reactome TAS + one IEA (RHEA/EC) → ACCEPT/KEEP as
  corroborating.
- GO:0008378 galactosyltransferase activity — correct but general parent. Three IDA
  (PMID:10747952 x2, 10748143) and one IBA. Keep IDAs (experimental, not removable); general —
  KEEP_AS_NON_CORE (GO:0050512 is the informative term).
- GO:0016758 hexosyltransferase activity — general IEA parent (ARBA). KEEP_AS_NON_CORE.

Cellular component:
- GO:0000139 Golgi membrane — correct specific compartment. TAS (Reactome), IEA (SubCell),
  NAS (PMID:10748143). ACCEPT the TAS as core location; keep the others.
- GO:0016020 membrane — general parent of Golgi membrane; IDA (PMID:10748143).
  KEEP_AS_NON_CORE (experimental, not removable; but Golgi membrane is more informative).

Biological process:
- GO:0006688 glycosphingolipid biosynthetic process — correct core BP. IBA, TAS, NAS. ACCEPT.
- GO:0007009 plasma membrane organization — IDA acts_upstream_of_or_within (PMID:10747952,
  MGI). Indirect/downstream consequence of Gb3 synthesis on membrane microdomains, not a direct
  molecular role of the enzyme. Experimental so not removable → KEEP_AS_NON_CORE.

## Core functions chosen

1. MF: GO:0050512 lactosylceramide 4-alpha-galactosyltransferase activity (Gb3/CD77 synthase).
2. CC/location: GO:0000139 Golgi membrane.
3. BP: GO:0006688 glycosphingolipid biosynthetic process (globo-series initiation).

All term ids verified current & non-obsolete via OLS (2026-07).

## 2026-09-25 re-review for CLINGEN_MENDELIAN

This section supersedes the earlier annotation-action summary and its duplicated
counts. All **15** existing YAML rows were reviewed: **12 ACCEPT, 2 MODIFY,
1 UNDECIDED**. The source annotation identifiers, evidence codes and reference IDs
are unchanged. No NEW GO annotation is proposed.

### Mendelian mechanism and acceptor specificity

[ClinGen CCID:008831](https://search.clinicalgenome.org/kb/gene-validity/CGGV:assertion_7e3a8df0-77f1-4395-b501-63a96016e515-2025-05-30T170000.000Z)
classifies the A4GALT–A4GALT-congenital disorder of glycosylation association as
Definitive, autosomal recessive (May 30, 2025). Its phenotype is the **p-null blood
group**, with variable clinical consequences; this is not evidence that A4GALT
is an enzyme of the general N-glycan assembly pathway. The primary genetic
and functional evidence is consistent with loss of enzyme activity:
[PMID:10993874, *Molecular basis for the p phenotype*, "P251L and M183K mutations
showed complete loss of enzyme function"]. The ClinGen report was read live on
2026-09-25.

The **wild-type** enzyme makes both P(k) and P1. The earlier notes correctly
mention P1 capacity but the old review description was ambiguous about whether
P1 depended on Q211E. Direct recombinant-enzyme experiments resolve this:
[PMID:26773500, *Human Gb3/CD77 synthase reveals specificity toward two or four
different acceptors depending on amino acid at position 211, creating P(k), P1
and NOR blood group antigens*, "the consensus enzyme synthesizes both the P(k)
and P1 antigens, while its p.Q211E variant additionally synthesizes the NOR
antigen"]. P1 synthesis modifies paragloboside in the **neolacto** series; P1 is
not made by extending Gb3. The two core-function entries now describe distinct
LacCer-to-Gb3 and paragloboside-to-P1 reactions, rather than repeating the same
Gb3 reaction as both an activity and a pathway entry.

Q211E is a separate, specificity-broadening mechanism. The original NOR study
found the mutation in heterozygous NOR-positive donors and demonstrated NOR
production after transfection [PMID:22965229, *A single point mutation in the
gene encoding Gb3/CD77 synthase causes a rare inherited polyagglutination
syndrome*, "Cells transfected with the vector encoding the Gb3/CD77 synthase
with Glu at position 211 expressed both P1 and NOR antigens."]. It must not be
conflated with recessive p-null deficiency.

### N-glycan acceptors and toxin receptors

The full text of PMID:33460651 was retrieved by the publication cache and read.
Purified catalytic domains and transfected CHO-Lec2 cells establish that
A4GALT can modify complex N-glycan acceptors; CHO-Lec2 cells lack endogenous
A4GALT and are deficient in CMP-sialic acid transport. The experiments establish
capacity, while its quantitative endogenous contribution in normal human
tissues remains a question. [PMID:33460651, *Human Gb3/CD77 synthase produces P1
glycotope-capped N-glycans, which mediate Shiga toxin 1 but not Shiga toxin 2 cell
entry*, "both enzymes produce P1 glycotopes on N-glycoproteins, with the mutein
exhibiting elevated activity."] The receptors are **glycan products** of the
enzyme, so toxin binding should not be assigned to the enzyme itself.

No new N-glycosylation or toxin-entry process annotation is proposed from this
study. Its experimentally demonstrated acceptor breadth is stated in the
biological description and reference findings without asserting that every
cellular consequence of those glycans is an evolved core A4GALT function.

### Annotation decisions and evidence limits

- GO:0008378 galactosyltransferase activity (three rows) is **ACCEPT**. It
  describes the core catalytic activity and covers both P(k) and P1 chemistry;
  a broader valid term is not automatically a peripheral function.
- GO:0016758 hexosyltransferase activity is **MODIFY** to GO:0035250
  UDP-galactosyltransferase activity. This specifies the UDP-galactose donor
  while retaining the demonstrated acceptor breadth.
- GO:0016020 membrane is **MODIFY** to GO:0000139 Golgi membrane using the
  combined UniProt and Reactome localization evidence. The original
  PMID:10748143 topology prediction is not represented as a Golgi imaging assay.
- All specific Gb3-synthase, glycosphingolipid-biosynthesis and Golgi-membrane
  rows are **ACCEPT**.
- GO:0007009 plasma membrane organization is **UNDECIDED**. The PMID:10747952
  cache is abstract-only. Its abstract establishes P(k) synthesis and surface
  expression; it does not identify a membrane-organization experiment.
  PubMed, DOI/publisher retrieval and a full-title web search did not provide
  usable full text. The previous claim that this is an indirect effect on
  membrane microdomains was speculation, as was using the source relationship
  type to justify a decision. The experimental annotation is not rejected on
  incomplete evidence; a precise follow-up question is recorded in the YAML.

All seven discussed GO definitions were checked through the live QuickGO REST
API on 2026-09-25 (GO:0050512, GO:0007009, GO:0006688, GO:0000139, GO:0008378,
GO:0016758, GO:0001576). The existing GO:0006688 remains appropriate;
GO:0001576 explicitly starts at the tetrasaccharide globoside core and is not
substituted for A4GALT's Gb3-forming step. Both original Reactome references were
opened live; R-HSA-9846477 identifies A4GALT as catalyst, LacCer and UDP-Gal as
inputs, Gb3 as product, and Golgi membrane as the enzyme compartment. Searching
`gocams/index.tsv` for A4GALT and Q9NPC4 returned no cached model entry.

Primary sources added to the cache: PMID:10993874, PMID:22965229,
PMID:26773500 (abstracts), and PMID:33460651 (PMC full text). No cached source
was hand-edited. The original two publications remain abstract-only.

A live QuickGO inspection of all 40 descendants of GO:0008378 found no
P1/paragloboside-specific or general alpha-1,4-galactosyltransferase term.
GO:0035250 UDP-galactosyltransferase activity was separately definition-checked
and used for the P1 core reaction and the hexosyltransferase refinement. The
LacCer-specific GO:0050512 is inappropriate for the paragloboside reaction.

### Automated research execution and validation

`just deep-research-falcon human A4GALT --fallback perplexity-lite` was launched
concurrently with `just fetch-gene-pmids human A4GALT`, as required by the review
workflow. An initial environment-install race was retried after installation
completed. The actual provider run then terminated: Falcon timed out after
600 seconds, and the automatic perplexity-lite fallback returned HTTP 401
`insufficient_quota`. No provider research artifact was produced or invented.
The manual literature synthesis and source checks are documented above; the
review decisions rely on the primary evidence rather than a generated summary.

`just validate human A4GALT` passed without review warnings after the final
ontology refinement. The history record passed `just validate-history`, the
updated review rendered with `just render human A4GALT`, and `git diff --check`
passed. All 15 source assertion rows remain present; only reviewer-authored
content changed.

### PR 3127 follow-up, 2026-09-25

The independent reviewer correctly requested structured treatment of the old negative P1 finding. PMID:10747952 now has a per-finding OVERTURNED assessment with PMID:26773500 as superseding evidence and its verbatim quote; the P(k) and p-null findings are not rejected. The three galactosyltransferase rows now consistently refine to the donor-specific GO:0035250, with source-specific summaries. Final decisions: 9 ACCEPT, 5 MODIFY, 1 UNDECIDED. Description wording states N-glycan acceptor capacity directly; experimental scope remains in the reference assessment. The broad membrane refinement remains based on combined curated localization; an abstract-only topology prediction does not establish that the original IDA code is erroneous. No late Falcon report or surviving A4GALT research process was present when checked after the review.
