# PTA1 (S. cerevisiae, Q01329, SGD:S000000041) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: PTA1 is the closest experimentally characterised relative of S. pombe pta1
(Q10222). Both are in PANTHER subfamily PTHR15245:SF20 (SYMPLEKIN) per the UniProt
cross-references (`DR PANTHER; PTHR15245:SF20; SYMPLEKIN`). SGD PTA1 is a donor to PAINT
node PTN000391745, which propagates only `GO:0005847` CPF complex (IBA) — PAINT did not
propagate any process or function term from this node to the gene. No ProtNLM2 output was
consulted.

### Deep research

`just deep-research-falcon yeast PTA1 --fallback perplexity-lite` failed: falcon failed,
and the perplexity-lite fallback timed out after 600 s. No deep-research file was produced.
The review below is built from the cached publications (publications/PMID_*.md) and the
UniProt record.

### What is experimentally established in S. cerevisiae

- **CF II / CPF subunit.** Pta1 is the 90-kDa fourth subunit of CF II
  [PMID:10523662 "In this report, we show by protein sequencing and immunoreactivity that
  the fourth subunit of CF II is Pta1, an essential 90-kDa protein originally implicated in
  tRNA splicing."]. In modern nomenclature it is in the phosphatase module of CPF
  [PMID:29074584 "the phosphatase module contains seven subunits (Pta1, Ref2, Pti1, Swd2,
  Glc7, Ssu72, and Syc1)"], and it is also the organising subunit of the separate APT
  complex [PMID:30247719 "a 14-subunit CPF complex with all subunits except Syc1, and a
  7-subunit APT complex"].
- **Required for both cleavage and poly(A) addition in extracts** (pta1-1, pta1-2 ts
  alleles), rescued by purified CF II [PMID:10523662]. Caveat: in a fully recombinant
  reconstituted system Pta1 is dispensable for the chemical reactions [PMID:30737185 "We
  show that yeast Pta1 is not required for the cleavage and polyadenylation reactions
  themselves in our fully reconstituted system."]. So Pta1's role is as a scaffold /
  regulator of CPF in vivo, not a catalytic or minimal-core requirement.
- **Scaffold.** Different regions bind Ssu72, Pti1 and Ysh1 [PMID:19188448]; N-terminus
  (1-300) binds Ssu72 and Pap1 N-terminus [PMID:22575652]; C-terminus binds Ysh1/Syc1
  (mutually exclusive) [PMID:29074584, PMID:30247719]. Loss of Pta1 lowers levels of other
  CF II subunits [PMID:10523662].
- **Regulation by phosphorylation.** Glc7 dephosphorylates Pta1; phosphorylated Pta1 cannot
  rescue polyadenylation [PMID:16137619].
- **Transcription.** Pta1 is on chromatin near poly(A) signals and snoRNA genes
  [PMID:12819204]; pta1-Δ75 is defective in snoRNA termination, CTD Ser5-P
  dephosphorylation and gene looping but not mRNA 3'-end processing [PMID:19188448]; gene
  looping requires Pta1 [PMID:16319194]. Conflict: Lidschreiber et al. 2018 summarise
  PMID:12819204 as showing Ref2, Pta1, Pti1 do NOT regulate sn/snoRNA termination, whereas
  the 12819204 abstract says "Ref2 and Pta1 similarly affect at least one snoRNA
  transcript". I therefore did not add a NEW exosome-dependent (snoRNA) termination term;
  raised as a question instead.
- **tRNA.** pta1-1 accumulates end-trimmed intron-containing pre-tRNAs, but splicing
  endonuclease activity is normal [PMID:1508188] and the cause is unknown [PMID:10523662].
  Treated as an indirect phenotype (MARK_AS_OVER_ANNOTATED), matching the treatment of the
  ISO-propagated row in genes/SCHPO/pta1.

### Comparator check for NEW mRNA 3'-end processing

QuickGO (2026-10-21): other non-catalytic yeast CPF subunits carry mRNA processing
experimentally — CFT2 (Q12102) GO:0006397 IDA, FIP1 (P45976) GO:0006397 IDA, PTI1
(P39927) GO:0006397 IMP; human SYMPK (Q92797, same subfamily) carries GO:0031124 mRNA
3'-end processing IDA. PTA1 has no mRNA processing annotation at all in current GOA
(cache/go/terms.csv lists GO:0006378 mRNA polyadenylation as obsolete, likely the former
annotation). Pta1 does work in the process as the scaffold of CPF (structure case), so
NEW GO:0031124 with IMP from PMID:10523662 is proposed.

### MF

Bare protein binding rows: MODIFY to GO:0140378 protein complex scaffold activity where
the paper maps Pta1 as an organising scaffold (PMID:19188448, PMID:12819204); REMOVE for
high-throughput or single-pair two-hybrid rows. GO:0030674's own comment directs complex
scaffolds to GO:0140378.
