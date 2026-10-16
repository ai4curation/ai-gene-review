# cGlr1 (Cyclic GMP-AMP synthase-like receptor 1) research notes

UniProt: A1ZA55 (CGLR1_DROME) · FlyBase: FBgn0034047 · CG12970 · 378 aa
Family: Mab-21 family; cGAS/DncV-like nucleotidyltransferase. PANTHER PTHR10656:SF42
("CYCLIC GMP-AMP SYNTHASE-LIKE PROTEIN-RELATED"). InterPro Mab-21-like nucleotidyltransferase.

> Note: no external deep-research provider was available in this environment
> (`just deep-research DROME cGlr1 --provider perplexity` reported "Provider 'perplexity'
> not available. Available: falcon, openscientist"). These notes were written from the
> cached primary literature (PMID:34261127, PMID:34261128, PMID:37659413) and the UniProt
> record, with inline provenance. No `-deep-research-<provider>.md` file was fabricated.

## Core biology

cGLR1 is a cytosolic pattern-recognition receptor of the cGAS-like family. It is the
Drosophila functional analog of vertebrate cGAS, but it senses double-stranded RNA rather
than DNA, and produces the non-canonical cyclic dinucleotide 3'2'-cGAMP.

- Identified by a forward biochemical screen as a dsRNA sensor:
  [PMID:34261127 "used a forward biochemical screen to identify cGLR1 as a
  double-stranded RNA sensor in the model organism Drosophila melanogaster"].
- RNA recognition activates the nucleotidyltransferase to make 3'2'-cGAMP:
  [PMID:34261127 "We show that RNA recognition activates Drosophila cGLR1 to synthesize
  the novel product cG[3'-5']pA[2'-5']p (3'2'-cGAMP)"].
- Ligand specificity: long dsRNA (>30 bp), phosphorylation-independent:
  [PMID:34261127 "Dm-cGLR1 recognize dsRNAs longer than 30 bp"].
- Enzyme: nucleotidyltransferase using ATP + GTP, Mg2+/Mn2+ cofactor; two-step reaction
  via a linear pppA(2'-5')pG intermediate (UniProt CATALYTIC ACTIVITY / FUNCTION;
  Rhea:RHEA:68344, 68348, 68352). EC 2.7.7.-.
  [file:genes/DROME/cGlr1/cGlr1-uniprot.txt "Synthesizes 3',2'-cGAMP in a two-step
  reaction through production of the linear intermediate pppA(2'-5')pG"].
- Second messenger output activates dSTING and NF-κB (Relish):
  [PMID:34261127 "Genetic mutations to Sting and the NF-κB homologue Relish ablated"]
  the 3'2'-cGAMP-induced responses.
- In vivo antiviral role:
  [PMID:34261127 "3'2'-cGAMP induces an enhanced antiviral state in vivo that protects
  from viral infection"].

## Two-paper concordance (2021)

Holleufer et al. (abstract-only in cache) independently identified both cGLRs and confirmed
cGLR1 as the dsRNA-activated 3'2'-cGAMP producer:
[PMID:34261128 "cGLR1 is activated by"] double-stranded RNA to produce 3'2'-cGAMP, and both
cGLRs "activate Sting- and NF-κB-dependent antiviral immunity in response to infection with
RNA or DNA viruses" [PMID:34261128 "activate Sting- and NF-κB-dependent antiviral"].

## Cai et al. 2023 (Immunity, PMID:37659413)

- cGLR1-expressing flies produce 2'3'-cGAMP and 3'2'-cGAMP in vivo:
  [PMID:37659413 "only 2'3'-cGAMP and 3'2'-cGAMP were detected in the hemolymph of flies
  ectopically expressing cGLR1"] — supports both GO:0140700 (3'2'-cGAMP synthase) and
  GO:0061501 (2'3'-cGAMP synthase) IDA for cGLR1.
- CDN production is virus-induced and cGLR-dependent:
  [PMID:37659413 "systemic DCV infection resulted in the induction of 2′3′-cGAMP,
  3′2′-cGAMP and 2′3′-c-di-GMP"] — supports GO:0098586 cellular response to virus.
- cGLR1 also contributes to 2'3'-c-di-GMP production during infection:
  [PMID:37659413 "cGLR1 contributes to the production of 2′3′-c-di-GMP in the context of a
  viral infection in flies"].

## GO review summary

Signature molecular functions: 3'2'-cGAMP synthase (GO:0140700) and 2'3'-cGAMP synthase
(GO:0061501) activities, both dsRNA-activated (GO:0003725). Localization: cytosol
(GO:0005829). Biological processes: cGAS/STING signaling (GO:0140896), defense response to
virus (GO:0051607), (immune) response to exogenous dsRNA (GO:0043330, GO:1902615), cellular
response to virus (GO:0098586). All existing GOA annotations are well supported and specific;
the ND root-CC placeholder (GO:0005575) is superseded by the specific cytosol annotation.
