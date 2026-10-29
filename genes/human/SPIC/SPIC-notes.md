# SPIC (Spi-C) curation notes

Human SPIC, UniProt Q8N5J4 (248 aa); mouse ortholog Spic, Q6P3D7. No deep-research
provider was available for this review; the notes below come from manual reading of
primary literature found via Europe PMC (queries `TITLE:"Spi-C"`, `TITLE:"Spic"`,
`(SPIC OR "Spi-C") AND macrophage`), each PMID checked against its Europe PMC/PubMed
title and cached with `ai-gene-review fetch-pmid`.

## Identity and domain architecture

- ETS-family transcription factor of the SPI subgroup (PU.1/SPI1, SPI-B, SPI-C).
  UniProt: ETS DNA-binding domain residues 111-194 (PROSITE PRU00237); "Binds DNA as a
  monomer"; "Belongs to the ETS family".
- Mouse Spi-C was cloned by yeast one-hybrid on the kappaY element; it "interacted with DNA
  similarly to PU.1 as judged by methylation interference, band-shift and site selection
  analysis, and activated transcription of a kappaY element reporter gene" [PMID:10187812].
- N-terminal acidic transactivation domain; "the transactivation activity is reduced to that
  of the DNA binding domain (DBD) alone when four aspartic acid residues are mutated to
  alanines" [PMID:12749910]. This is the mouse IMP behind the Ensembl-Compara IEA rows
  (GO:0000978, GO:0001228, GO:0045944) on human SPIC.
- Human SPI-C cDNA "displays 65% amino acid identity to the murine protein"; human mRNA
  "preferentially detected in foetal and adult spleen, lymph nodes and at lower levels in
  bone marrow and foetal liver" [PMID:12459275].

## Core biology: red pulp macrophage / iron-recycling macrophage lineage (mouse)

- Kohyama et al. 2009 Nature (PMID:19037245, verified; DOI 10.1038/nature07472):
  "Spic(-/-) mice have a cell-autonomous defect in the development of red pulp macrophages
  that is corrected by retroviral Spi-C expression in bone marrow cells, but have normal
  monocyte and other macrophage subsets." Spic-/- mice "fail to phagocytose these red blood
  cells efficiently, and develop an iron overload localized selectively to splenic red
  pulp". VCAM-1 is a direct target: "An Ets consensus element within the proximal VCAM-1
  promoter forms complexes with PU.1 and Spi-C in EMSA"; "Deletion of the Ets element
  within the VCAM-1 promoter eliminated reporter augmentation by both PU.1 and Spi-C".
  B cell development and antibody production were normal in Spic-/- mice.
- Haldar et al. 2014 Cell (PMID:24630724): heme induces Spic; "Bach1 is a transcriptional
  repressor of Spic that is inhibited by heme"; "Spic−/− mice were found to be deficient in
  F4/80hi VCAM1hi BMM in addition to the previously reported loss of RPM". Heme generates
  pre-RPM and RPM from monocytes in vivo. Retroviral Spic did not induce the Spic reporter
  ("arguing against auto-activation").
- Human relevance: heme-enriched extracellular vesicles from stored red cells induce SPIC in
  human monocytes [PMID:35663938] - expression evidence only.

## Other roles (mouse; peripheral to the core)

- Inflammation: TLR/NF-kB induce Spic in macrophages; "Spic downregulates pro-inflammatory
  cytokines and promotes iron efflux by regulating ferroportin expression in activated
  macrophages"; IFN-gamma/STAT1 block Spic [PMID:32610126].
- Stress erythropoiesis: erythrophagocytosis during inflammation induces SPI-C, which with
  TLR signalling "promoted the expression of Gdf15 and Bmp4" [PMID:31506384].
- B cells: Spi-C opposes PU.1/Spi-B. Spic heterozygosity rescues Spib-/- B cells; "Spi-B was
  shown to directly activate the Nfkb1 gene, whereas Spi-C was shown to repress this gene"
  [PMID:25769919]; Spi-B and Spi-C differentially regulate Bach2 [PMID:32457757]; RAG DSBs
  activate a SPIC/BCLAF1 complex that displaces PU.1 genome-wide and suppresses Syk
  [PMID:31644907]; Spi-C and PU.1 counterregulate Igκ and Rag1 [PMID:37195219]; Fcer2a
  (CD23) activated by PU.1, Spi-B and Spi-C [PMID:21057087]; Spi-C opposes PU.1 at IgH
  intronic enhancer and FcgammaRIIb promoter in pro-B cells [PMID:16887979]; SPI-C + STAT6
  cooperate on IgE germline (Iepsilon) transcription (overexpression, Y2H/co-IP)
  [PMID:16647686].
- Osteoclasts: Spi-C knockdown reduces RANKL-induced osteoclastogenesis; RANKL induces
  nuclear translocation of Spi-C [PMID:32341419] (single study, knockdown/overexpression).

So SPI-C acts both as activator (VCAM1, Fcer2a, kappaY reporter) and as a context-dependent
repressor/antagonist of PU.1 targets (Nfkb1, Rag1, Igκ, Syk). Whether repression is
intrinsic or via competition for PU-box sites (it lacks the PU.1 PEST/IRF4-PIP interaction:
"SPI-C and PIP were unable to form a distinct ternary complex" [PMID:12749910]) is unknown.

## Annotation decisions (summary)

- MF: DNA-binding TF activity, Pol II-specific (GO:0000981) and Pol II cis-regulatory
  sequence-specific DNA binding (GO:0000978) are core; activator activity (GO:0001228) accepted.
  General GO:0003700 / GO:0043565 -> MODIFY to the specific terms already carried.
- BP: GO:0006357 accepted; GO:0006355 -> MODIFY to GO:0006357; GO:0030154 cell
  differentiation -> MODIFY to GO:0030225 macrophage differentiation (Kohyama 2009, Haldar
  2014; cell-autonomous, rescued by retroviral expression; comparator: mouse PU.1 carries
  GO:0030225). No separate NEW row (covered by the MODIFY replacement).
  Iron homeostasis / erythrocyte clearance are consequences of the lineage SPI-C specifies,
  not steps SPI-C performs, so no NEW iron-homeostasis term.
- CC: nucleus, chromatin accepted.
- protein binding (HuRI Y2H: MEOX1, INTS11) removed as uninformative.

## Comparator / curation observations

- MGI has not annotated Kohyama 2009 / Haldar 2014 for mouse Spic (QuickGO, Oct 2026):
  mouse Spic carries only PMID:12749910 (NTNU_SB), PMID:16630543 (MGI) and phylogenetic/IEA
  rows. This looks like a curation gap in mouse, not a deliberate convention, since mouse
  Sfpi1/PU.1 (P17433) carries GO:0030225 macrophage differentiation.
