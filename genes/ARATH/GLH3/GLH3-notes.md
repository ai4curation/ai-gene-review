# GLH3 (AT5G55720, Q9FM66) notes

## Identity

- TAIR gene aliases (gene_aliases_20260930.txt): AT5G55720 has the symbols GLH3 and
  ATPLL14. GLH3 maps to this locus only.
- UniProt Q9FM66 (PLY21_ARATH), "Putative pectate lyase 21", 392 aa. UniProt
  lists no GLH3 gene-name synonym, so a UniProt search by symbol finds nothing.
  The record was located through its Araport cross-reference (`xref:araport-AT5G55720`).
- Folder created with `just fetch-gene ARATH Q9FM66 --alias GLH3`.

## Deep research

`just deep-research-falcon ARATH GLH3 --fallback perplexity-lite` failed on
2026-10-19: no provider API keys (EDISON, PERPLEXITY, OPENAI, ASTA) were set in the
session environment. The literature below was gathered manually through PubMed
searches ("glassy hair Arabidopsis trichome"; "At5g55720 OR PLL14"; papillae with
pectate lyase/pectin and trichome; Kirik V [Author] AND trichome since 2018).

## Literature

### Cloning of GLH3 (PMID:42555921, Rickerd et al. 2026, Plant Physiol)

Only the abstract is cached. PMC13540736 returned no full text through PubMed
Central, so the methods (alleles, enzyme assays, constructs) were not reviewed.

- Mutant phenotype: [PMID:42555921 "Papillae do not develop in the Arabidopsis glassy hair3 (glh3) mutant."]
- Gene identity: [PMID:42555921 "Cloning of the GLH3 gene revealed that a member of the pectate lyase gene family is required for papillae formation."]
- Expression: [PMID:42555921 "GLH3 pectate lyase expression is trichome-specific in leaves, and it precedes the appearance of papillae."]
- Regulation: [PMID:42555921 "The transcriptional Mediator complex containing Med25 and Med16 subunits activates GLH3 gene expression in trichomes."]
- Localization: [PMID:42555921 "Following transport to the apoplast through a canonical secretion pathway, the GLH3-GFP fusion protein accumulates in papillae."]
- Model: [PMID:42555921 "Focused accumulation of the GLH3 pectate lyase in papillae suggests that papillae formation is driven by focal pectin hydrolysis."]
- Pectin link: [PMID:42555921 "Trichome overexpression of another pectin metabolism gene, pectin methylesterase QRT1, prevented papillae formation."]

The abstract does not say whether pectate lyase activity was assayed on GLH3 protein.

### Original glh screen (PMID:24014871, Suo et al. 2013, J Exp Bot; full text cached)

- glh3 was one of five new GLH loci. [PMID:24014871 "Complementation tests within this group showed that the mutants were affected in five different genes: GLH1, GLH2, GLH3, GLH4, and GLH5."]
- The phenotype is limited to papillae: [PMID:24014871 "Trichomes in glh1 and glh3 mutants displayed cell-wall defects restricted to papillae formation."] and [PMID:24014871 "We did not detect a significant change in trichome cellulose in glh1 and glh3 mutants."]
- The allele was weak in this study: [PMID:24014871 "The most transparent glh1 and glh2 trichomes showed the strongest defects in papillae development, while the weaker glassy mutants glh3 and glh4 showed a moderate decrease in papillae density and coverage."]
  This differs from the 2026 abstract ("Papillae do not develop"). The 2026 paper may
  have used other alleles or measures; this cannot be checked without its full text.
- Extra branching: [PMID:24014871 "In contrast, glh3 mutants formed more trichome branches exhibiting 29% four-branched and 1% five-branched trichomes."]
  It is not known whether the GLH3 lesion itself causes this. The 2026 abstract does not mention it.
- Genetic interaction with HDG2: [PMID:24014871 "This additive double-mutant phenotype suggested that the HDG2 and GLH3 genes promote papillae formation independently and that the GLH3 gene is not a probable target of the HDG2 transcription factor."]
- Papillae function: [PMID:24014871 "Taken together, our data suggested that GLH genes promote papillae development and that papillae confer light-reflective properties on trichomes."]

### Upstream regulators (the other GLH genes)

- GLH1 = MED25 (PMID:28889249, full text cached).
- GLH2 = MED16 (PMID:30535640, abstract only). Mediator subunits MED2, MED14 and MED15a
  also give glassy trichomes.
- The 2026 abstract places GLH3 downstream of MED25/MED16, which joins the regulators to
  their effector.

## Sequence and family

- PL1 family (Pfam PF00544, InterPro IPR045032, PANTHER PTHR31683:SF18). It has a
  signal peptide (1-21, ECO:0000255) and two predicted N-glycosylation sites.
- Bioinformatics (`GLH3-bioinformatics/RESULTS.md`): GLH3 keeps the catalytic Arg (R269)
  and the three Ca2+-binding Asp residues of the A. nidulans pectate lyases plyA and plyB
  (the PAINT IBD seeds), at about 35% identity. No sign of a pseudoenzyme.
- PAINT: IBD for GO:0030570 at PTN001271105, seeded by A. nidulans plyA/plyB.
- PMR6 (PMID:12215508, abstract only) is another Arabidopsis pectate lyase-like gene,
  cached as a candidate plant comparator. It was set aside: the abstract reports changed
  cell wall composition and powdery mildew resistance in pmr6 mutants, but no measured
  enzyme activity, so it does not give the plant PL1 activity reference that
  `GLH3-bioinformatics/RESULTS.md` asks for.

## GO term checks (OLS, 2026-10-19)

- GO:1905499 trichome papilla formation: exists and is not obsolete. Its parents are
  cell projection assembly and cellular component assembly involved in morphogenesis.
  QuickGO: carried by MED16, MED25 and ECR/CER10 (IMP, PMID:24014871, TAIR,
  acts_upstream_of_or_within). These are the regulators and a wax/VLCFA enzyme. GLH3 is the
  secreted effector found in the papillae, so it does some of the work of building
  the structure, which the participation test requires.
- GO:0090396 "leaf papilla" is a GO cellular component term defined as part of the
  leaf papilla cell (PO:0025167), an epidermal outgrowth cell. It is not a trichome
  cell-wall papilla, so it is not used.
- GO:0009505 plant-type cell wall and GO:0048046 apoplast are both part_of descendants
  of GO:0005576 extracellular region (checked in the local go.db, 2026-10-20). Apoplast
  is part_of extracellular region directly. Plant-type cell wall is_a cell wall, is_a
  external encapsulating structure, part_of extracellular region. Neither is an is_a
  descendant. Cell wall is not part_of apoplast in GO, so both are listed.
- No "cell wall pectin catabolic process" term exists. GO:0045490 pectin catabolic
  process is the most specific catabolic term.

## Curation gaps

- No experimental GO annotations yet. PMID:42555921 supports trichome papilla
  formation (IMP), plant-type cell wall / papilla localization (GFP) and trichome
  expression.
- UniProt Q9FM66 lacks the gene names GLH3 and PLL14 and the 2026 functional data.
