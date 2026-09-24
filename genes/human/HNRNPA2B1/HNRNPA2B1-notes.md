# HNRNPA2B1 review notes

## Why this gene was selected

Two standing claims about HNRNPA2B1 sit outside its uncontested hnRNP biology: that it is a nuclear
"reader" of the m6A RNA modification, and that it is a nuclear DNA sensor initiating innate immune
signalling. A 2026 RNA Biology paper attacks the first. The question for curation was what GOA
actually carries for each.

## First: what does GOA actually carry?

Checked directly in `HNRNPA2B1-goa.tsv`:

- **The m6A reader term is present.** `GO:1990247 N6-methyladenosine-containing RNA reader activity`,
  `enables`, **IDA**, PMID:26321680. So there is a real annotation to adjudicate, not a hypothetical one.
- **The DNA-sensor claim is absent.** PMID:31320558 (Wang, Wen & Cao, *Science* 2019, "Nuclear
  hnRNPA2B1 initiates and amplifies the innate immune response to DNA viruses") appears in the GOA
  file **twice, both times as EXP evidence for localisation only**: `GO:0005634 nucleus` and
  `GO:0005737 cytoplasm`. There is no DNA-binding term other than the telomeric ones, no
  pattern-recognition-receptor term, no interferon-production term, no innate-immune-response term on
  this gene at all. UniProt, by contrast, states the innate-immunity role in its FUNCTION comment
  ("Also plays a role in the activation of the innate immune response (PubMed:31320558). Mechanistically,
  senses the presence of viral DNA in the nucleus..."). **That asymmetry is the finding** — GO curators
  have taken the localisation from that paper and declined to take the function. No annotation edit is
  needed; it is recorded in the `reason` on the nucleus and cytoplasm annotations and raised in
  `suggested_questions`.

No 2025-26 paper independently re-tests the DNA-sensor claim. What exists builds on it rather than
testing it: PMID:41134667 (Cell Rep 2025, U1 snRNA promotes hnRNPA2B1 dimerisation —
[PMID:41134667 "U1 interacts with the nuclear DNA sensor hnRNPA2B1 to facilitate its dimerization,
nucleocytoplasmic translocation, and downstream TBK1-IRF3 signaling activation"]) and PMID:40689679
(mBio 2025, mtDNA sensing during SFTSV infection). Both assume the role. The 2019 paper is not
retracted and carries no notice in its PubMed record; I have marked its `reference_review.correctness`
as `UNVERIFIED` rather than `VERIFIED`, because I could confirm the identifier and title but not an
independent replication of the central claim.

## The m6A reader question

### The 2026 paper (PMID:41662154, Park et al., RNA Biol 23(1):1-28, 2026)

Verified on PubMed; DOI 10.1080/15476286.2026.2627781; full text cached. MD simulation plus
microscale thermophoresis, using the RRM1-RRM2 fusion construct from Wu et al.

[PMID:41662154 "the binding affinity is nearly identical and slightly less favourable to the
unmodified sequence"] and, on the mechanism,
[PMID:41662154 "This can be attributed to the strong interactions conferred by AGG and UAG motifs
rather than adenine or m6A in the GGACU motif"], with the bottom line
[PMID:41662154 "Our study suggests that HNRNPA2B1 is not a (selective) reader but has high affinity
for m6A in a sequence-dependent manner."] In the discussion:
[PMID:41662154 "either adenine or m6A at the fifth position, irrespective of their conformations with
respect to the protein, do not contribute much to the binding"]. The experimental leg:
[PMID:41662154 "bind with nearly equal affinity to the RRM domains of HNRNPA2B1"] (~10 nM difference,
< 0.1 kcal/mol, the methylated one slightly worse).

### This is not a lone 2026 paper

Following its reference [5] led to Wu et al., *Nat Commun* 9:420 (2018), PMID:29379020, verified —
crystal structures of the tandem RRMs on several RNA substrates:
[PMID:29379020 "elucidating specific recognitions of AGG and UAG motifs by RRM1 and RRM2 domains,
respectively"] and the explicit conclusion
[PMID:29379020 "our studies in combination with bioinformatic analysis suggest that hnRNP A2/B1 may
mediate effects of m6A through a"] ... [PMID:29379020 "instead of acting as a direct"] "reader" of m6A
modification (the quoted words in the original are typeset with curly quotes around "m6A switch" and
"reader", so the verbatim span is broken around them).

Two independent methods, eight years apart, reach the same conclusion.

### What the original annotation rests on

PMID:26321680 (Alarcón et al., Cell 2015, verified) is the IDA:
[PMID:26321680 "We find that the RNA-binding protein HNRNPA2B1 binds m(6)A-bearing RNAs in vivo and in
vitro and its biochemical footprint matches the m(6)A consensus motif."] and
[PMID:26321680 "We propose HNRNPA2B1 to be a nuclear reader of the m(6)A mark"].

Note the logic: the CLIP footprint *matching* the m6A consensus is the evidence for reading. But the
METTL3 consensus GGAC overlaps the AGG/UAG motifs HNRNPA2B1 prefers on sequence grounds alone, so the
footprint overlap is fully explained without any methyl-specific recognition.

### Position taken

`GO:1990247` → **MARK_AS_OVER_ANNOTATED**, not REMOVE. Reasons for stopping short of removal:
1. It is an IDA and I have not read the full Alarcón text; project rules forbid removing an
   experimental annotation on that basis.
2. The binding is real. HNRNPA2B1 does bind m6A-containing transcripts and does mediate m6A-dependent
   effects on splicing and pri-miRNA processing. What fails is the *selectivity* the word "reader"
   asserts, via the "m6A switch" alternative (methylation changes RNA structure, exposing the motif).
3. The 2026 measurements used an isolated RRM1-RRM2 fusion, not full-length protein with its
   low-complexity domain, and a single GGACU context. Recorded as a limitation in the reference review.

The downstream process annotations are **kept as ACCEPT**: `GO:0031053 primary miRNA processing` and
`GO:0000398 mRNA splicing, via spliceosome` survive the demotion, because HNRNPA2B1 can recruit
Microprocessor to pri-miRNAs it binds by sequence without reading the mark. This is the point of
separating the MF from the BP.

## Other curation decisions

- `GO:0003676 nucleic acid binding` (IEA, InterPro RRM) → **MODIFY** to `GO:0003723 RNA binding`.
- `GO:0016020 membrane` (HDA, PMID:19946888) → **MARK_AS_OVER_ANNOTATED**. No TM segment, no anchor,
  no signal peptide; an abundant phase-separating RBP in a membrane fraction is a preparation artefact.
- `GO:0032392 DNA geometric change` (ISS) → **MARK_AS_OVER_ANNOTATED**. The term asserts an induced
  change in twist or writhe of duplex DNA. What was observed is that hnRNP A2 binds ssDNA and protects
  the telomeric repeat from nuclease: [PMID:15659580 "hnRNP A2 protected the telomeric repeat sequence,
  but not the complementary sequence, against DNase digestion"]. Binding is not a topological activity.
- The telomere cluster (`GO:0043047`, `GO:0098505`, `GO:0000781`, `GO:1904358`, `GO:0070182`) →
  **KEEP_AS_NON_CORE**. Real, and mechanistically coherent — the ssDNA telomere repeat matches the same
  consensus as the A2RE RNA element [PMID:15659580 "Both the hnRNP A2-binding cis-acting element for
  the cytoplasmic RNA trafficking element, A2RE, and the ssDNA telomere repeat match a consensus
  sequence for binding to a second sequence-specific site identified by mutational analysis."] — but
  demonstrated largely in rat brain protein and peripheral to the hnRNP function.
- `GO:0070182 DNA polymerase binding` (ISS) is the weakest annotation on the gene; kept rather than
  removed because a curator made the similarity judgment and I did not inspect the source, but
  explicitly excluded from core.
- Bare `GO:0005515 protein binding` (16 IPI rows) → **MARK_AS_OVER_ANNOTATED**.
- `GO:0140693 molecular condensate scaffold activity` (IDA, PMID:29358076) → **ACCEPT**, core. The LC
  domain is the disease-relevant module: [PMID:23455423 "Wild-type hnRNPA2 (the most abundant isoform
  of hnRNPA2B1) and hnRNPA1 show an intrinsic tendency to assemble into self-seeding fibrils, which is
  exacerbated by the disease mutations."]

## Core functions asserted

Four, none of which depends on the m6A or DNA-sensor questions:
pre-mRNA intronic binding → splicing; A2RE 3'-UTR binding → mRNA transport/export;
LC-domain condensate scaffolding; miRNA binding → primary miRNA processing.

## What I could not resolve

Whether full-length HNRNPA2B1, in a condensate, discriminates m6A. Every negative result so far comes
from isolated RRM constructs in dilute solution. And whether the 2019 DNA-sensor result replicates —
I found no independent test of it, only work that assumes it.
