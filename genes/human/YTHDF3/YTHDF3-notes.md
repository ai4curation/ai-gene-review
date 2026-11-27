# YTHDF3 (Q7Z739) — review notes

Reviewed as one half of a paired batch with **ALKBH1**. The pairing is not thematic convenience:
a 2025 EMBO J paper proposes that YTHDF3 is the *reader* of N6-methyladenine (6mA) in genomic
**DNA** and that it recruits ALKBH1 to erase it. Both genes therefore rest on the same contested
premise — that mammalian genomic 6mA is a real, regulated mark.

## 1. The canonical and well-supported function: cytoplasmic m6A RNA reader

YTHDF3 is one of three paralogous cytoplasmic YTH-domain m6A "reader" proteins (YTHDF1/2/3, or
DF1/DF2/DF3). Its YTH domain binds N6-methyladenosine in mRNA; its N-terminal intrinsically
disordered region drives condensation. GOA carries `GO:1990247 N6-methyladenosine-containing RNA
reader activity` with IBA, IEA and **six** independent IDA annotations spanning 2012–2020. This
is as well-supported as molecular functions get, and I treat it as the core function.

Note on two of those IDAs whose *abstracts* foreground a paralog: PMID:24284625 is titled for
YTHDF2, but the cached full text shows GST-YTHDF3 expression constructs and a rabbit anti-YTHDF3
antibody in the methods — i.e. YTHDF3 was directly assayed. This is exactly the situation CLAUDE.md
warns about, and it is a reason to defer to the curator, not to suspect mis-attribution.

## 2. The intra-field dispute: does YTHDF3 promote translation, or only degradation?

GOA carries **both sides of this dispute**, and it is worth stating plainly.

**For translation promotion** (2017, two papers published back-to-back in Cell Research):

> [PMID:28106072 "Here, we report that YTHDF3 promotes protein synthesis in synergy with YTHDF1, and affects methylated mRNA decay mediated through YTHDF2."]
> [PMID:28106076 "In this study, we show that YTHDF3 promotes translation, thus playing an important role in the initial stages of translation."]
> [PMID:28106076 "We found that YTHDF3 interacts with the ribosomal proteins"]

These underlie `GO:0045727 positive regulation of translation` (IMP), `GO:0045948 positive
regulation of translational initiation` (IDA) and `GO:0043022 ribosome binding` (IDA).

**Against** (2020, Zaccara & Jaffrey, Cell — the "unified model"):

> [PMID:32492408 "In contrast to the prevailing model, we show that DF proteins bind the same m6A-modified mRNAs rather than different mRNAs."]
> [PMID:32492408 "Furthermore, we find that DF proteins do not induce translation in HeLa cells."]
> [PMID:32492408 "Instead, the DF paralogs act redundantly to mediate mRNA degradation and cellular differentiation."]
> [PMID:32492408 "The ability of DF proteins to regulate stability and differentiation becomes evident only when all three DF paralogs are depleted simultaneously."]

That paper is the source of the GOA row `NOT|involved_in GO:0045948` (IDA) — a *negative*
assertion of the same term that PMID:28106076 asserts positively.

**Position taken.** `GO:0045948` is marked `UNDECIDED` on both rows: the positive and the negated
annotation contradict each other, both are IDA, both come from competent labs, and neither can be
adjudicated from the cached record. Recording this as a live disagreement is more informative than
picking a winner. `GO:0045727` and `GO:0043022` are kept but demoted to non-core, since the
redundancy result means that whatever translation effect exists is not the paralog's defining
activity. The degradation arm (`GO:0061157`, `GO:0043488`) is what both camps agree on, so that
is what is marked core.

A note on redundancy and "core": the unified model implies that single-gene phenotypes understate
YTHDF3's contribution, because DF1/2/3 compensate. That is an argument for keeping the reader
activity core even though YTHDF3 knockdown alone is often mild.

## 3. Condensate biology

> [PMID:31292544 "The resulting mRNA-YTHDF complexes then partition into different endogenous phase-separated compartments, such as P-bodies, stress granules or neuronal RNA granules."]
> [PMID:32451507 "Here, we show that m6A-modified mRNAs are enriched in SGs, and that m6A-binding YTHDF proteins are critical for SG formation."]
> [PMID:32451507 "Depletion of YTHDF1/3 inhibits SG formation and recruitment of mRNAs to SGs."]

Real and mechanistically coherent (multivalent m6A scaffolds + low-complexity domains), but
downstream of the reader activity and stress-conditional, hence non-core. GOA's
`GO:0070925 organelle assembly` from PMID:31292544 is far too general for what was shown;
the specific granule-assembly terms (`GO:0034063`, `GO:0033962`) are the right level.

## 4. The m1A-reader claim — a second instance of the same methodological pattern

> [PMID:32194978 "among them, YTH domain-containing protein 3 (YTHDF3), could bind directly to m1A-carrying RNA"]
> [PMID:32194978 "YTHDF3 could promote IGF1R mRNA degradation and thus inhibit IGF1R protein expression along with its downstream matrix metallopeptidase 9 signaling pathway, consequently decreasing migration and invasion of trophoblast."]

This supports `GO:0003723 RNA binding` (IDA), `GO:0043488` (IMP) and
`GO:1901163 regulation of trophoblast cell migration` (IMP).

Caveat worth recording: the premise that mRNA carries abundant m1A had already been substantially
deflated the year before —

> [PMID:31719534 "These results demonstrate that high-stoichiometry m1A sites are exceedingly rare in mRNAs and that previous mappings of m1A to 5'UTRs were the result of antibody cross-reactivity to the 5' cap."]

The m1A-seq used in PMID:32194978 is the technique that paper challenges. The binding and
degradation experiments themselves are not overturned by this, and none of the annotations is
removed — but a reader annotation whose substrate is transcriptome-wide-rare is weak ground for
"core". This is the **third** time in this two-gene batch that an antibody-based mapping method
turns out to be the load-bearing element of a substrate assignment (6mA-DIP for DNA 6mA,
m1A-seq for mRNA m1A, and pyridine-borane sequencing for RNA f5C in PMID:41219180).

## 5. The DNA 6mA reader claim — and the fact that GO has not taken the bait

The 2025 EMBO J paper proposes:

> [PMID:40715766 "Compared with ALKBH1, YTHDF3 preferentially recognizes and binds to 6mA-modified DNA with different conformations."]
> [PMID:40715766 "Here, we found that YTHDF3 increases the 6mA demethylase activity of ALKBH1 in genomic DNA with different conformations, including dsDNA."]
> [PMID:40715766 "In summary, YTHDF3 is a novel genomic DNA reader and guides ALKBH1 to remove 6mA in human genomic DNA."]

Its own abstract concedes the problem it is trying to solve:

> [PMID:40715766 "Therefore, the demethylase activity of ALKBH1 toward 6mA in genomic DNA, especially dsDNA, remains largely debated."]

**Explicitly recorded finding: this claim has not entered GOA.** A live QuickGO query for
`UniProtKB:Q7Z739` (2026) returns 17 distinct GO terms — P-body, RNA binding, mRNA binding,
protein binding, cytoplasm, cytosol, cytoplasmic stress granule, cytoplasmic stress granule
assembly, ribosome binding, regulation of mRNA stability, positive regulation of translation,
positive regulation of translational initiation, negative regulation of type I interferon-mediated
signaling pathway, mRNA destabilization, organelle assembly, regulation of trophoblast cell
migration, and N6-methyladenosine-containing RNA reader activity. **None of them is a DNA-binding,
chromatin or 6mA term.** No `GO:0003677 DNA binding`, no methylated-DNA-binding term, nothing.

That restraint is correct on the current evidence, and it is worth recording as a positive
observation rather than an omission. The reasons not to annotate it are the same as for ALKBH1:

- The mark being "read" is itself contested. Mammalian genomic 6mA is attributed to bacterial
  and RNA contamination, antibody non-specificity and nucleotide-salvage misincorporation
  (PMID:32206710, PMID:32203414, PMID:35113693), and animals appear to have lost the AMT1
  writer lineage entirely (PMID:41254163).
- The result is not independent: the corresponding/senior authorship of PMID:40715766 overlaps
  with PMID:30017583, the original human-genomic-6mA paper. It extends a programme rather than
  replicating it from outside.
- A YTH domain binding a *deoxy*adenosine mark would be a striking departure from the entire
  structural literature on YTH aromatic-cage recognition of m6A in RNA, and would warrant
  structural confirmation before annotation.

If genomic 6mA is independently confirmed in mammals, `GO:0003677` plus a methylated-DNA-binding
term would become appropriate for YTHDF3. Until then, recording the claim in `reason` and
`suggested_questions` — as done here — is the right level of commitment.

## 6. Other annotations

- `GO:0005515 protein binding` (six IPI rows: HIV-1 capsid from PMID:22190034, YTHDF1/Q9BYJ9 from
  four interactome studies, FAF1/Q9UNN5 from PMID:32296183) — all marked
  `MARK_AS_OVER_ANNOTATED` per project guidance. The YTHDF1 interaction is biologically real and
  is captured functionally by the translation and granule annotations; the bare term adds nothing.
- `GO:0060339 negative regulation of type I interferon-mediated signaling pathway` (ISS + IEA from
  mouse Ythdf3, Q8BYK6) — retained as non-core; an antiviral/innate-immunity role downstream of
  m6A-dependent mRNA turnover rather than a distinct activity.
- `GO:0003723 RNA binding` — a true but generic parent of the informative m6A-reader term this
  gene already carries; kept non-core.

## 7. Bottom line

YTHDF3's core function is what it has always been: a **cytoplasmic m6A reader that, redundantly
with YTHDF1 and YTHDF2, binds m6A-modified mRNAs and directs them to destabilisation**. The
translation-promoting role is genuinely disputed and GOA carries both sides, including an explicit
`NOT` annotation. The newly proposed DNA-6mA-reader role has not entered GOA and should not until
the existence of the substrate is settled independently.
