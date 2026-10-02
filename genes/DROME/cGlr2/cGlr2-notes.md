# cGlr2 (Cyclic GMP-AMP synthase-like receptor 2) research notes

UniProt: A8DYP7 (CGLR2_DROME) · FlyBase: FBgn0050424 · CG30424 · 459 aa (isoform F)
Family: Mab-21 family; cGAS/DncV-like nucleotidyltransferase. PANTHER PTHR10656:SF42.
EC 2.7.7.86 (2',3'-cGAMP synthase) and EC 2.7.7.-. Zn-binding (residue 263).

> Note: no external deep-research provider was available in this environment
> (`just deep-research` reported perplexity unavailable; only falcon/openscientist).
> These notes were written from the cached primary literature (PMID:34261128 abstract-only;
> PMID:37659413 full text) and the UniProt record, with inline provenance. No
> `-deep-research-<provider>.md` file was fabricated.

## Core biology

cGLR2 is a second Drosophila cGAS-like receptor that acts alongside cGLR1 in antiviral innate
immunity. Like cGLR1 it is a cytosolic Mab-21/cGAS-like nucleotidyltransferase that makes
cyclic dinucleotide (CDN) second messengers from ATP and GTP, which activate dSTING and the
NF-κB factor Relish. Its distinctive product is 2'3'-c-di-GMP; it also produces both cGAMP
isomers.

- Identified with cGLR1 as inducing Sting/NF-κB antiviral immunity:
  [PMID:34261128 "We show that cGLR1 and cGLR2 activate Sting- and NF-κB-dependent antiviral"]
  immunity in response to RNA or DNA viruses.
- Product profile (Holleufer, abstract): cGLR2 produces a combination of 2'3'-cGAMP and
  3'2'-cGAMP; its activating stimulus was unresolved at the time:
  [PMID:34261128 "produces a combination of 2'3'-cGAMP and 3'2'-cGAMP in response to an"]
  as-yet-unidentified stimulus.
- Enzyme (UniProt): catalyzes GTP + ATP -> 3'2'-cGAMP, -> 2'3'-cGAMP (EC 2.7.7.86), and
  -> pppGp(2'-5')A intermediate; Mg2+/Mn2+ cofactor.
  [file:genes/DROME/cGlr2/cGlr2-uniprot.txt "Nucleotidyltransferase that catalyzes the
  formation of cyclic GMP-AMP from ATP and GTP and plays a key role in antiviral innate
  immunity"].
- Nucleic-acid (dsRNA) sensing (Cai 2023): dsRNA facilitates cGLR2 CDN synthesis and the
  paper models cGLR2 as a nucleic-acid sensor:
  [PMID:37659413 "activation is enhanced most strongly in the presence of dsRNA"];
  [PMID:37659413 "providing a structural explanation for the role of cGLR2 as a nucleic acid
  sensor"]. Note the strongest in vitro binding/structural data are for the D.
  pseudoananassae / D. bipectinata orthologs; the endogenous activating ligand of D.
  melanogaster cGLR2 in vivo remains formally unidentified
  [PMID:37659413 "The ligand activating cGLR2 is still unknown"].
- Distinctive product 2'3'-c-di-GMP:
  [PMID:37659413 "we confirmed that 2′3′-c-di-GMP is major product of Drosophila cGLR2"];
  cGLR2-expressing flies produce all CDN isomers:
  [PMID:37659413 "were detected in the hemolymph of flies ectopically expressing cGLR2"].
- Virus-induced, cGLR-dependent CDN production in vivo:
  [PMID:37659413 "systemic DCV infection resulted in the induction of 2′3′-cGAMP,
  3′2′-cGAMP and 2′3′-c-di-GMP"].

## GO review summary

Signature molecular functions: cyclic-dinucleotide (cGAMP) synthase activities —
2'3'-cGAMP synthase (GO:0061501, incl. EC 2.7.7.86 IEA) and 3'2'-cGAMP synthase
(GO:0140700), plus (distinctively) 2'3'-c-di-GMP synthesis for which there is no dedicated
GO term. dsRNA binding (GO:0003725) supported by Cai 2023 (with the ortholog/ligand caveat
above). Localization: cytosol (GO:0005829). Processes: cGAS/STING signaling (GO:0140896),
defense response to virus (GO:0051607), cellular response to virus (GO:0098586).

The IMP annotation GO:1902615 "immune response involved in response to exogenous dsRNA"
(from PMID:34261128) asserts a dsRNA-specific trigger that is firmly established for cGLR1
but not for cGLR2: the source paper itself states cGLR2's activating stimulus is
unidentified, and dsRNA-facilitation for cGLR2 was shown later (Cai 2023) mainly in
orthologs. It is flagged as an over-annotation (the cGLR2 antiviral role is better captured
by GO:0051607 / GO:0140896 / GO:0098586, which are all retained).
