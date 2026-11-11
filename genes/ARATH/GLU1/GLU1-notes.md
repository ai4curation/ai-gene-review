# GLU1 (At5g04140, Q9ZNZ7) curation notes

**Deep research could not be run** in this environment (no provider API keys). These notes
are built only from cached publications (`publications/PMID_*.md`) and the UniProt record
(`GLU1-uniprot.txt`). No `-deep-research-*.md` file exists for this gene.

## Identity

- Ferredoxin-dependent glutamate synthase 1 (Fd-GOGAT1; GLS1), 1622 aa with 105-aa transit
  peptide; glutamate synthase family; FMN and [3Fe-4S] cofactors by similarity (UniProt).
- Two Fd-GOGAT genes in Arabidopsis; only GLU1 is photorespiratory
  [PMID:22303256 "Arabidopsis contains two expressed genes for Fd-GOGAT ( Glu 1 (At5g04140) and Glu 2 (At2g41220)), but only mutation of the Glu 1 gene resulted in a photorespiratory phenotype ( Coschigano et al., 1998 )."].

## Activity and process

- Reaction: L-glutamine + 2-oxoglutarate + 2 reduced ferredoxin -> 2 L-glutamate
  (EC 1.4.7.1; UniProt, ECO:0000269 PubMed:19223513).
- Photorespiratory role from gls mutants [PMID:9596633 "Ferredoxin-dependent glutamate synthase (Fd-GOGAT) plays a major role in photorespiration in Arabidopsis, as has been determined by the characterization of mutants deficient in Fd-GOGAT enzyme activity (gls)."];
  T-DNA knockout confirmation [PMID:19223513 "We confirmed that a T-DNA insertion mutant (Salk_104286, termed glu1-202 ), in which the T-DNA has inserted into the 2nd exon of GLU1 , lacks Fd-GOGAT protein ( Figure 3A ) and exhibits reduced Fd-GOGAT activity ( Table 1 ) and photorespiratory chlorosis"].
- Also primary nitrogen assimilation in leaves [PMID:9596633 "Both the mutant analysis and gene regulation studies suggest that GLU1 plays a major role in photorespiration and also plays a role in primary nitrogen assimilation in leaves"];
  glu1 mutant accumulates photorespiratory ammonium and amides [PMID:19555410 "Phenotypic analysis revealed a high level of photorespiratory ammonium, glutamine/glutamate and asparagine/aspartate in the GLU1 mutant lacking the major ferredoxin-glutamate synthase"];
  [PMID:20307264 "An elevated glutamine level in the glu1-2 mutant was the most prominent of these changes."].
- Expression: leaf-predominant, induced by light and sucrose [PMID:9596633 "GLU1 mRNA was expressed at the highest levels in leaves, and its mRNA levels were specifically induced by light or sucrose."];
  promoter active in mesophyll and phloem [PMID:16034598 "White light, red light or sucrose induced GUS expression in the dark-grown seedlings in a pattern similar to the GLU1 mRNA accumulation in Arabidopsis."].

## Localization

- Chloroplast stroma (transit peptide; GFP; fractionation; stromal proteomes)
  [PMID:19223513 "Fd-GOGAT is a chloroplastic enzyme responsible for the reassimilation of photorespiratory ammonia as well as for primary nitrogen assimilation."].
- Minor mitochondrial pool [PMID:19223513 "We show that Fd-GOGAT is dual targeted to the mitochondria and the chloroplasts."],
  undetectable in FFE-purified mitochondria [PMID:19223513 "FFE-purified Col-0 shoot mitochondria and Landsberg erecta tissue culture mitochondria do not contain sufficient amounts of Fd-GOGAT to be detected by mass spectrometry or by protein gel blots using Fd-GOGAT antibodies"]
  [PMID:22303256 "This at least implies that the proteins are scarce in the mitochondrion which would again support a regulatory instead of a catalytic role."].

## Non-catalytic role: SHMT1 support ("enzyme activator activity")

- [PMID:19223513 "In the mitochondria, Fd-GOGAT interacts physically with SHMT1, and this interaction is necessary for photorespiratory SHMT activity."]
- Catalysis not needed [PMID:19223513 "Thus, we conclude that wild-type levels of photorespiratory SHMT activity require Fd-GOGAT expression (although not catalytic activity)"].
- Assessment: genetic (glu1-201 L1270F retains Fd-GOGAT activity but loses SHMT activity and
  co-IP with SHMT1; catalytically dead internal deletion rescues), co-IP and BiFC evidence from
  one lab. No in vitro reconstitution of SHMT activation. GO:0008047 enzyme activator activity
  ("directly interacts with the enzyme, but does not result in a covalent modification") fits
  the claim; kept as non-core moonlighting function. The generic protein binding (IPI, SHM1)
  row was modified to this term.

## Other

- ACR11 interacts with GLU1 in chloroplasts and controls Fd-GOGAT levels
  [PMID:27411448 "interacts with Glu1-encoded ferredoxin (Fd)-GOGAT in Arabidopsis chloroplasts."].
- 14-3-3 omega TAP co-purification (PMID:19452453) is a high-throughput protein binding call;
  removed as uninformative.

## Curation decisions (summary)

- Core MF GO:0016041 glutamate synthase (ferredoxin) activity; BP photorespiration,
  ammonia assimilation cycle, L-glutamate biosynthesis; CC chloroplast stroma.
- General MF terms (glutamate synthase activity, oxidoreductase terms) modified to GO:0016041.
- Mitochondrion/mitochondrial matrix and enzyme activator activity kept as non-core.
- Plasma membrane, chloroplast envelope, apoplast HDA marked over-annotated; mRNA binding
  marked over-annotated.
- No NEW annotations.
