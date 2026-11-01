# PSPPH_4093 (YajQ) — *Pseudomonas savastanoi* pv. *phaseolicola* 1448A — curation notes

UniProt **Q48EH2** (`Y4093_PSE14`), 159 aa, `OrderedLocusNames=PSPPH_4093`, NCBITaxon:264730.

**Deep research was unavailable for this gene.** No deep-research API keys exist in
this container, so `just deep-research` was not run and no
`-deep-research-<provider>.md` file was created. Everything below was assembled by
hand from the cached publications in `publications/`, from NCBI E-utilities and
QuickGO/EBI ontology queries, and from one WebFetch of the PMC page of
PMID:18836083 (the cached copy is abstract-only: `full_text_available: false`).
Where a statement rests on the PMC full text rather than the cached abstract, it is
marked **[full text, not quotable]** — those statements are not used as
`supporting_text` anywhere in the review, because a `supporting_text` value has to be
a verbatim substring of the cached file.

## What the gene is

A YajQ-family protein (UPF0234 / COG1666; Pfam PF04461, HAMAP MF_00632, InterPro
IPR007551 "YajQ/Smlt4090-like", PANTHER PTHR30476). The family is a bacterial
invention: "The protein YajQ, present in many bacterial genomes, is missing in
eukaryotes." [PMID:12381839] and "The protein is present in most bacteria, but not in
archaea or eukaryotes." [PMID:12943362]. The fold is two tandem four-stranded
antiparallel beta-sheet domains: "The polypeptide chain is folded into two domains
with identical folding topology." and "This structural motif is a characteristic
feature of many RNA-binding proteins." [PMID:12943362].

Nucleotide binding is the one family-level biochemical property with direct data.
*E. coli* YajQ was isolated as a nucleotide-binding protein and characterised by
NMR/ITC: "We used dye pseudoaffinity chromatography, two-dimensional gel
electrophoresis, and mass spectrometry to identify two novel Escherichia coli
nucleotide-binding proteins, YnaF and YajQ." and "In the absence of significant
similarities of YajQ to any solved structure, we determined its structural and
ligand-binding properties by NMR and isothermal titration calorimetry."
[PMID:12381839].

**The ligand is not conserved across the family**, which matters for how specific a
binding term can be. "Interestingly, affinity for cyclic di-GMP binding was only seen
in YajQ family proteins from P. aeruginosa (PA4395) and S. maltophilia (Smlt4090)
(Table S1). YajQ family proteins from E. coli, Clostridium sp. and B. cereus by
contrast exhibited a greater affinity for ATP and/or GTP than for any cyclic mono- or
di-nucleotide." [PMID:25329577]. In *Xanthomonas campestris* the YajQ protein XC_3703
is a c-di-GMP receptor that partners a LysR-family transcription factor and modulates
its promoter binding; the *P. aeruginosa* ortholog PA4395 also binds c-di-GMP and is
needed for adhesion and lung colonisation: "Genetic and functional analysis of YajQ
family members from the human pathogens Pseudomonas aeruginosa and Stenotrophomonas
maltophilia showed that they also specifically bound cyclic di-GMP and contributed to
virulence in model systems." [PMID:25329577].

So for Q48EH2 specifically: it is a *Pseudomonas* YajQ, and its closest characterised
relative (PA4395) binds c-di-GMP — but no ligand has been measured for Q48EH2 itself,
and the family splits on ligand within a single study. `GO:0000166 nucleotide binding`
is therefore as precise as the evidence for this protein allows; refining it to a
cyclic-di-GMP term would be an orthology extrapolation across a property the family
demonstrably does not conserve.

## What PMID:18836083 actually shows (the CACAO reference)

Qiao, Sun, Qiao & Mindich, *PNAS* 2008. Cached copy is abstract-only.

The host is *P. syringae* pv. *phaseolicola*; the virus is **bacteriophage phi6**, a
**dsRNA** phage of the *Cystoviridae*: "Bacteriophage Phi6 contains three dsRNA
genomic segments L, M, and S." [PMID:18836083]. The genome sits inside a core
particle: "The RNA is located inside a core particle composed of multiple copies of a
major structural protein, an RNA-dependent RNA polymerase, a hexameric NTPase, and an
auxiliary protein." [PMID:18836083].

**The transcribing entity is the viral polymerase, not YajQ.** "The virion RNA
polymerase in the core particle transcribes segments M and S in vitro."
[PMID:18836083]. The full text names it P2 and states that YajQ does not act on the
free enzyme at all — purified P2 is not stimulated by added YajQ **[full text, not
quotable]**.

**What YajQ does** is switch on early transcription of segment L: "Yet early in
infection, the transcription of L is highly active." and "A host protein encoded by
yajQ is responsible for the activation of L transcription." [PMID:18836083]. It does
this on the particle, through the major core structural protein P1, not on the
polymerase: "YajQ acts indirectly on the polymerase by binding to P1, the major
structural protein of the core." and "Previous studies have shown that the activity of
the polymerase in the core is controlled by the conformation of the core particle
structure." [PMID:18836083]. The follow-up paper states the same mechanism from the
particle side: "Transcription of genomic segment L is activated by the interaction of
host protein YajQ with the capsid structure." [PMID:20164238].

**YajQ is required for the phage, and the phage can escape the requirement.**
"Knockout mutants of yajQ do not support the replication of Phi6, although they do
support the replication of distantly related members of the Cystoviridae."
[PMID:18836083]; "Phi6 can mutate to independence of YajQ. This requires two mutations
in the gene for the RNA-dependent RNA polymerase." [PMID:18836083]. That the escape
mutations fall in the polymerase gene is itself evidence that YajQ's target is the
polymerase's regulation, not the chemistry.

**Gene attribution is exact, not an ortholog guess.** The PMC full text names the locus
**PSPPH_4093** as the *yajQ* ortholog, with wild-type strain LM2489 and knockout
LM4470 **[full text, not quotable]**. The experimental strain (LM2489) is not the
sequenced strain (1448A), but the paper itself supplies the 1448A locus tag, so the
CACAO row is attached to the protein the authors pointed at. This is the opposite of
batch 2's cross-isolate and adjacent-locus provenance failures.

**Localisation.** GFP-YajQ is diffuse in uninfected cells and becomes punctate only on
infection by YajQ-dependent phage: "Green fluorescent protein (GFP) fusions with YajQ
produce uniform fluorescence in uninfected cells and in cells infected with viruses not
dependent on YajQ.", "Punctate fluorescence develops when cells are infected with
YajQ-dependent viruses.", "It appears that the host protein binds to the infecting
particles and remains with them during the entire infection period." [PMID:20164238].
The uninfected pattern is direct support for the otherwise-electronic cytosol row, and
the infected pattern is independent support for virion binding.

## The two CACAO rows, and the term that was created from their paper

Both CACAO rows (dated 2025-04-25, IDA, PMID:18836083) carry the qualifier
`acts_upstream_of_or_within_positive_effect`:

| term | aspect | qualifier |
|---|---|---|
| GO:0039696 RNA-templated viral transcription | BP | acts_upstream_of_or_within_positive_effect |
| GO:1903902 positive regulation of viral life cycle | BP | acts_upstream_of_or_within_positive_effect |

GO:0039696 is defined as "A transcription process that uses viral RNA as a template."
and sits under GO:0019083 viral transcription / GO:0019080 viral gene expression
(QuickGO, queried 2026-11-01). It names the polymerase's own activity. By the
"who performs the step" rule, YajQ cannot be `involved_in` it — and the CACAO row does
not say it is. `acts_upstream_of_or_within_positive_effect` is a legal GO BP relation
and is exactly the relation for a product that influences a process from outside it,
so on this row the odd qualifier is the student *avoiding* the error, not committing
one.

The decisive finding is in the ontology, not the paper. **GO:0140181 "host-mediated
activation of viral RNA-templated transcription"** exists:

- definition: "A process in which a host organism initiates, promotes, or enhances the
  normal execution of viral RNA-templated transcription, the synthesis of either RNA on
  a RNA template."
- exact synonym: "positive regulation by host of viral RNA-templated transcription"
- `is_a GO:0043923` host-mediated activation of viral transcription, under the
  interspecies branch (GO:0044419 / GO:0035821 / GO:0044788 / GO:0044794)
- **created 2025-06-12**
- **its definition xref is PMID:18836083** — this paper
- **it has zero annotations** (QuickGO annotation search, 2026-11-01)

So the term was minted *from the very paper these rows cite*, two months after the rows
were made, and the rows were never moved onto it. GO:0140181 is one term that says
everything the two rows say between them, in the right relation (`involved_in`: all
1,425 annotations to the parent GO:0043923 use `involved_in`), on the right side of the
host/virus boundary, and at the right granularity (RNA-templated, which is what phi6
is). Both rows are therefore MODIFY to GO:0140181.

Corpus context on the qualifier, supplied by the batch-3 coordinator and
consistent with what is seen here: on GO:0098672 all five CACAO rows dated
2018-2019 use `involved_in` and all ten dated 2025-2026 use
`acts_upstream_of_or_within_positive_effect`, with one gene (A0A220GHA5)
annotated by CACAO three times and flipping relation between 2019 and 2025; the
same chronological split appears on GO:0044659. The hedge is therefore a change
in the 2025 campaign's practice, not a per-row judgement. These two rows are
dated 2025-04-25 and sit in that cohort, so the fact that the hedge happens to
be the correct relation for GO:0039696 is not evidence that anyone chose it for
that reason.

The qualifier verdict differs between the rows:

- **GO:0039696**: qualifier is *correct* for the term as written. The term is wrong for
  YajQ (wrong actor), the qualifier is the hedge that makes it survivable. Not a
  WRONG_QUALIFIER defect; filed as a WRONG_TERM defect instead.
- **GO:1903902**: the term is itself a positive-regulation term and YajQ does the
  regulating, so `involved_in` is correct and
  `acts_upstream_of_or_within_positive_effect` stacks a second regulation layer on a
  regulation term. This *is* the AcrIIA5 WRONG_QUALIFIER shape, and both defects are
  filed.

## GONUTS

Re-checked 2026-11-01 as the project page asks. `gowiki.tamu.edu` no longer returns
"temporarily offline": it returns **HTTP 410 Gone** with the page "GONUTS, the GO wiki,
has been retired" and a pointer to geneontology.org (EcoliWiki and OMP remain up).
The per-paper and per-protein CACAO pages are gone for good, so the project's standing
plan to "re-check the abstract-only rows when GONUTS returns" cannot be carried out.
PMC full text, where the publisher allows it, is the only remaining route to what a
CACAO student read.

## Other rows

- `GO:0000166 nucleotide binding`, IEA, GO_REF:0000120, UniRule UR000032397 +
  PANTHER PTN002411992. Correct and at the right granularity (see the ligand-splitting
  argument above). UniProt: "Nucleotide-binding protein." and "Belongs to the YajQ
  family." (both `ECO:0000255|HAMAP-Rule:MF_00632`), grounded in the *E. coli* ITC/NMR
  work [PMID:12381839].
- `GO:0005829 cytosol`, IEA, GO_REF:0000118, TreeGrafter. No TM segment, no signal
  peptide in the record; GFP-YajQ is uniformly distributed in uninfected cells
  [PMID:20164238]. Accept.

## Proposed addition

`GO:0046790 virion binding` ("Binding to a virion, either by binding to components of
the capsid or the viral envelope") as a NEW molecular-function row, IDA. This is the
mechanistic step YajQ itself performs: it binds P1, a core capsid protein
[PMID:18836083], shown by formaldehyde cross-linking of YajQ-bound core particles
**[full text, not quotable]**, and GFP-YajQ co-localises with and stays on infecting
particles [PMID:20164238]. It is an informative alternative to bare `GO:0005515`,
which this gene does not carry and should not acquire.

## Open questions

- Does Q48EH2 bind c-di-GMP like PA4395, or ATP/GTP like *E. coli* YajQ? Nothing
  measures the ligand for this protein.
- Does Q48EH2 have a LysR-type partner in *P. savastanoi*, and is the phi6 interaction
  a repurposing of a P1-shaped surface the cell normally uses on a host protein?
- Is the native cellular role of YajQ in this organism related to the phage function at
  all? phi6 exploits the protein; the knockout's own phenotype in the absence of phage
  is not described in either phi6 paper.

## Ontology query record (2026-11-01)

Plain-text record of the live queries behind the judgements above, for citation.

QuickGO reports that GO:0140181 host-mediated activation of viral RNA-templated
transcription was created on 2025-06-12, carries PMID:18836083 as its definition
xref, and had zero annotations when queried on 2026-11-01.

All 1425 annotations to its parent GO:0043923 host-mediated activation of viral
transcription use the involved_in qualifier.

GO:0039696 RNA-templated viral transcription is defined as a transcription process
that uses viral RNA as a template, and its ancestors are GO:0019083 viral
transcription, GO:0019080 viral gene expression and GO:0016032 viral process, so the
term names the activity of whatever polymerase does the transcribing.

GO:0140181 is not a descendant of GO:1903902 positive regulation of viral life cycle;
it sits in the interspecies branch under GO:0043923, GO:0044794, GO:0044788,
GO:0035821 and GO:0044419, so replacing GO:1903902 with it is a lateral correction
rather than a refinement.

gowiki.tamu.edu returned HTTP 410 Gone with the page title GONUTS, the GO wiki, has
been retired.

The UniProt record for Q48EH2 declares no transmembrane segment and no signal
peptide, its only sequence feature being the full-length chain PRO_0000261963, which
is consistent with the cytosolic assignment.
