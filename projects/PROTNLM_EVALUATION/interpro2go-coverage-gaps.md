---
title: ProtNLM2 "novel" hits are mostly InterPro2GO coverage gaps
---
# Why the "correct novel" ProtNLM2 hits are missed by standard pipelines

[← back to ProtNLM2 Evaluation](../PROTNLM_EVALUATION.md)

## Bottom line

The predictions we called "correct novel" for uncharacterized proteins are **likely
correct** (they have no experimental support — the assessment is domain/orthology-based)
and, more importantly, they are **not novel biology**. They are functions that follow
directly from the protein's domains but that the standard **InterPro2GO** pipeline
(`GO_REF:0000002`) does not emit. In each case the gap is an InterPro/InterPro2GO
coverage problem, not a discovery. Three distinct mechanisms account for the three
flagship examples — verified against the live InterPro API and the current InterPro2GO
release (`!version date: 2025/09/01`).

## The three mechanisms

### 1. No InterPro2GO mapping exists for the domain — olfactomedin (A0A8C9H4D2 / OLFML2A)

The protein carries the olfactomedin domain (`InterPro:IPR003112`, Pfam `PF02191/OLF`)
and sits in family `IPR050605` (Olfactomedin-like domain-containing protein). **Neither
entry has any GO term** (InterPro API `go_terms: null` for both; zero lines in
InterPro2GO). So the ECM-organization function ProtNLM2 predicts is simply not derivable
from InterPro2GO.

Why no mapping? The olfactomedin domain is **functionally promiscuous** — it occurs in
myocilin, the olfactomedins/noelins, gliomedin, and the latrophilin adhesion GPCRs, whose
functions diverge widely — so a single reliable domain→GO mapping cannot be assigned.
(Note: the 11 "olfactomedin"-keyword lines in InterPro2GO are all *olfactory*
receptor/marker entries — IPR000725, IPR004117, IPR009103, IPR036727 — homonyms, not the
olfactomedin domain.)

### 2. Mapping exists only on a superfamily entry the protein was not assigned — KilA-N (A2FPI7)

The Trichomonas protein is assigned the domain-level entries `IPR017880` (KilA, N-terminal)
and `IPR018004` (KilA/APSES_HTH) — **both have no GO term**. The DNA-binding function does
exist in InterPro2GO, but only on the **superfamily** entry `IPR036887` (HTH APSES-type
DNA-binding domain superfamily → `GO:0003677` DNA binding), which this protein was **not
assigned**. So the DNA-binding annotation that would apply to APSES/KilA-N transcription
factors never propagates to it. (A2FPI7 currently has **zero** GO annotations of any kind.)

This is the one case where the GO annotation tracker shows **active curator curation** of the
family: [geneontology/go-annotation#1188](https://github.com/geneontology/go-annotation/issues/1188)
(closed 2015) records that *S. pombe* bqt4, which carries the APSES domain (`IPR003163`), is
**not** a transcription factor — it anchors DNA to the nuclear envelope. The InterPro curator
**deleted the transcription-factor GO terms** from the entry (keeping DNA binding) and alerted
PROSITE/UniRule, because PROSITE `PS51299` was auto-assigning DNA-binding GO/keywords from this
domain. The lesson generalises: the APSES/KilA-N domain is **functionally heterogeneous** (fungal
transcription factors, DNA-anchoring proteins, phage/eukaryotic KilA-N proteins), so curators keep
its GO deliberately sparse and conservative — which is why the domain-level entries A2FPI7 carries
have no GO at all.

### 3. Protein matched only an unintegrated Pfam; the InterPro entry that carries the mapping was not assigned — MCM-4 (A0A061AL94)

Here the InterPro2GO mapping is **rich and present**: `IPR001208` (MCM domain) →
DNA binding + ATP binding, and `IPR008047` (Mini-chromosome maintenance complex protein 4)
→ DNA binding, DNA helicase activity, ATP binding, DNA replication initiation, MCM complex.
But the *C. elegans* protein was assigned **only Pfam `PF21128` (WHD_MCM4)**, which is
**unintegrated into InterPro** and carries **no GO term** (InterPro API: `integrated: null`,
`go_terms: null`). Because it never matched the InterPro MCM entries, InterPro2GO had
nothing to key on — even though fully-assigned MCM4 orthologs receive the whole nucleus /
MCM-complex / replication annotation set.

## Was a mapping *removed*?

Curator-driven changes to InterPro2GO are reported on the GO annotation tracker
([geneontology/go-annotation](https://github.com/geneontology/go-annotation/)), so that is the
authoritative place to check. Searching it:

- **olfactomedin — no issues.** No record of any mapping ever being added or removed → this is a
  never-mapped **coverage gap**, not a removal. (Consistent with domain promiscuity: the
  olfactomedin domain spans myocilin, olfactomedins, gliomedin, and latrophilins.)
- **MCM-4 — no relevant issues.** No tracker record for the MCM *domain* mapping → the miss is an
  **assignment/integration gap** (unintegrated Pfam `PF21128`, unassigned InterPro MCM entry), not
  a removal.
- **KilA-N / APSES — yes, a documented curator removal.**
  [go-annotation#1188](https://github.com/geneontology/go-annotation/issues/1188) (2015) removed
  the transcription-factor GO terms from the APSES domain entry `IPR003163` because the domain is
  functionally heterogeneous (see mechanism 2 above). DNA binding was retained; only the
  overreaching TF terms were pruned. This is exactly the conservative curation that leaves the
  domain-level KilA-N entries GO-sparse.

More broadly, InterPro2GO mappings *are* unstable and are removed in bulk from time to time — e.g.
a PANTHER 10.0 update left 332 InterPro entries signature-less, removing 522 InterPro2GO mappings
and ~178,926 protein GO annotations (Sangrador-Vegas et al., *GO annotation in InterPro: why
stability does not indicate accuracy in a sea of changing annotations*, Database 2016,
[PMC4799721](https://pmc.ncbi.nlm.nih.gov/articles/PMC4799721/)). But for our three examples the
tracker shows the dominant cause is **conservative non-coverage** (never mapped, or TF terms
actively pruned), not accidental loss.

## Systematic view: this is the [PFAM project](../PFAM.md) finding at gene level

The [Pfam → GO mapping project](../PFAM.md) quantifies exactly this gap across all of Pfam:
InterPro2GO is deliberately conservative, and **82.6% of Pfam-A families (24,888) have zero GO via
InterPro** — including canonical, well-understood domains (SH2, EGF, Kringle, Actin). ~18k of the
uncovered families are *named and tractable*. The three ProtNLM2 "novel" hits here are concrete,
gene-level instances of that gap: ML function prediction is filling the ~18k-family space where
InterPro has abstained. The PFAM project's conclusion — that new value comes from *annotating
where InterPro abstained*, not from splitting lumped entries — is the flip side of the same coin.

## Curation implication

- ProtNLM2's value on uncharacterized proteins is largely in **filling InterPro2GO coverage
  gaps**, not discovering unknown biology — useful, but it should be framed as "likely
  correct, domain-derivable, currently un-emitted by InterPro2GO," and confirmed by a curator.
- Two concrete upstream fixes worth raising with InterPro: integrate `PF21128` (or ensure
  *C. elegans* MCM-4 matches an MCM InterPro entry), and consider whether the APSES/KilA-N
  DNA-binding mapping should propagate from the superfamily to the domain-level entries.

## Verification

- InterPro REST API (`/api/entry/interpro/<id>`, `/api/entry/pfam/PF21128`): confirmed
  `go_terms: null` for IPR003112, IPR050605, IPR017880; rich GO on IPR008047; PF21128
  unintegrated with no GO.
- Current InterPro2GO release (`rules/arba/_interpro2go.txt`, version 2025/09/01): 0 mapping
  lines for IPR017880/IPR018004/IPR003112/IPR050605; IPR001208 and IPR008047 present.

Sources: [InterPro2GO (EBI)](https://www.ebi.ac.uk/GOA/InterPro2GO) ·
[GO_REF:0000002](https://geneontology.org/GO_REF/0000002.html) ·
[Sangrador-Vegas et al. 2016 (PMC4799721)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4799721/)
