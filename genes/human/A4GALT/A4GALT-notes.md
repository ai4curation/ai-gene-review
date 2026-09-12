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
