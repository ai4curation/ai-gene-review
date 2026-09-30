# LPAL2 literature and product-status notes

## Research provenance

- On 2026-08-11, the repository's Falcon deep-research recipe was attempted with
  `just deep-research-falcon human Q16609 --alias LPAL2`. The client completed
  setup and launched, but returned no report; the stalled run was stopped. No
  `LPAL2-deep-research-falcon.md` file was created. An initial attempt using the
  generic `just deep-research` name also failed because this checkout has no such
  recipe. Per repository policy, neither failure was represented as a provider
  report.
- Decisive papers were fetched with the project `fetch-pmid` recipe and assessed
  directly from the resulting cache: PMID:8148351, PMID:7749817, and
  PMID:36010685. The two early papers are abstract-only; PMID:36010685 has cached
  PMC full text.

## Identity, locus, and expression

The original locus paper called the gene *apolipoprotein(a)-related gene C* and
explicitly left open whether the two related loci were genes or pseudogenes:

> "we analyzed overlapping human genomic yeast artificial chromosome clones,
> which revealed a cluster of four highly homologous genes encoding
> apolipoprotein(a), plasminogen, and two apolipoprotein(a)-related genes (rg) or
> pseudogenes."

[PMID:8148351, abstract; full text unavailable]

The same abstract provides RNA-level evidence in liver:

> "Hybridization analysis and reverse transcriptase polymerase chain reaction
> showed that one of these novel genes, designated apolipoprotein(a)rg-C, has a
> domain structure similar to apolipoprotein(a) and is transcribed in human
> liver."

[PMID:8148351, abstract; full text unavailable]

This establishes locus identity and transcription. It does not establish an
endogenous protein, secretion, incorporation into an Lp(a) particle, or any
apolipoprotein(a)/plasminogen biochemical activity.

## Transcript architecture and historical Q16609 product model

The follow-up transcript paper derived a short open reading frame from human
liver RNA:

> "We have isolated the human liver transcript derived from one of these genes,
> designated apo(a)-related gene C, that encodes a polypeptide of 132 amino acids
> composed of a secretion signal and a single kringle domain."

[PMID:7749817, abstract; full text unavailable]

Crucially, the same abstract documents the splice defect and premature stops:

> "Analysis of genomic sequence shows that the predicted exon at this site lacks
> a canonical splice donor site. This results in \"exon skipping\" during
> maturation of the mRNA, causing a coding frame shift and the presence of
> premature stop codons."

[PMID:7749817, abstract; full text unavailable]

The evidence is sequence analysis of a transcript and a predicted 132-aa ORF,
not detection of the corresponding endogenous polypeptide. UniProt models this
historical ORF as Q16609 but marks protein existence as `PE   5: Uncertain;` and
cautions, `Could be the product of a pseudogene.` It also states, `This protein
is however much shorter and does not contain any peptidase region.`
[file:human/LPAL2/LPAL2-uniprot.txt, current reviewed Q16609 record]

Current NCBI Gene nomenclature is **LPAL2, lipoprotein(a) like 2 (pseudogene)**,
GeneID 80350, gene type `PSEUDO`. RefSeq's current summary states:

> "This gene is similar to the lipoprotein, Lp(a) gene, but all transcripts
> produced by this gene contain a truncated open reading frame and are candidates
> for nonsense-mediated decay. Consequently, this gene is considered to be a
> pseudogene. Alternative splicing results in multiple transcript variants."

[NCBI Gene:80350 / NCBI Datasets gene record for human LPAL2, accessed
2026-08-11]

Together, the sources support a transcribed pseudogene with a historical
single-kringle ORF model. They do not currently support confident existence of a
stable endogenous Q16609 protein.

## RNA-level functional evidence

The 2022 HCC paper explicitly studies a noncoding RNA rather than Q16609 protein:

> "In the current study, we found that the pseudogene-derived lncRNA LPAL2 is
> downregulated in hepatocellular carcinoma (HCC) tissues, and further showed
> that elevated LPAL2 expression is positively correlated with survival
> outcome."

[PMID:36010685, abstract; cached full text available]

Its perturbation evidence is also RNA-directed:

> "We found that the knockdown of LPAL2 in HA22T and Huh7 cell lines accelerated
> cell growth, migration, and invasion"

> "Furthermore, MMP9 mRNA and protein were upregulated in LPAL2-depleted HA22T
> and Huh7 cell lines"

[PMID:36010685, Results sections 3.2 and 3.3; cached full text available]

The authors summarize the entity boundary directly:

> "Our collective results indicate that LPAL2 acts as a tumor-suppressor lncRNA
> in HCC."

[PMID:36010685, Discussion; cached full text available]

These findings may be relevant to an RNA-aware review of LPAL2, but they cannot
be assigned to the hypothetical Q16609 protein or used to infer a protein
molecular function.

## High-throughput interaction records

PMID:25416956 describes `a systematic map of ?14,000 high-quality human binary
protein-protein interactions.` The GOA row identifies VAC14 as the candidate
Q16609 partner, but the paper does not provide LPAL2-specific evidence of
endogenous protein production or physiological co-localization.
[PMID:25416956, abstract; cached full text available; LPAL2-goa.tsv for the
Q16609--VAC14 association]

PMID:32814053 reports an interactome that `connects ∼5,000 human proteins via
∼30,000 candidate interactions and is generated by systematic yeast two-hybrid
interaction screening`. GOA identifies HIP1, CLSTN1 isoform 2, CCK, CASP6, and
RAN as the five partners collapsed into the normalized Q16609 row. These remain
screen-derived candidate contacts and do not resolve the product-existence
problem.
[PMID:32814053, abstract; full text unavailable; LPAL2-goa.tsv for partner
identities]

## Functional boundary for subsequent curation

- Do not transfer LPA's lipoprotein-particle assembly, lipid transport,
  plasminogen competition, antifibrinolytic, protease, or receptor-binding
  functions to LPAL2. Homology and a single predicted kringle do not establish
  any of those activities.
- The 132-aa Q16609 sequence contains only a predicted signal peptide and one
  kringle; UniProt explicitly says it lacks a peptidase region.
- RNA expression and lncRNA knockdown phenotypes are evidence about LPAL2
  transcripts. They are not protein-existence evidence and should not be used as
  support for protein-centric GO annotations.
- Until direct endogenous protein evidence is found, any localization inferred
  from the predicted signal peptide and any interaction-screen rows require an
  explicit putative-product caveat.
