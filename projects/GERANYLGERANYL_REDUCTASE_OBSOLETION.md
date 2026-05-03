# Geranylgeranyl Reductase Activity — Obsoletion & Replacement

## Overview

A GO obsoletion proposal will obsolete `GO:0045550 geranylgeranyl reductase
activity` and replace it with `GO:0102067 geranylgeranyl diphosphate reductase
activity`. The replacement narrows the substrate from generic
"geranylgeranyl-X" to the diphosphate (GGDP), aligning the term with the
chlorophyll/tocopherol biosynthesis enzyme (plant/cyanobacterial CHLP /
ChlP / GGR) that catalyses the reduction of geranylgeranyl-(diphosphate or
chlorophyll) to phytyl form.

This project tracks the four experimental annotations on the upstream list and
queues per-gene reviews where useful — particularly the two human aldo-keto
reductase entries (AKR1C3, AKR1B10), which are likely a misuse of the
geranylgeranyl reductase term derived from in vitro substrate-screening data.

## Upstream tickets

- Annotation tracker: [geneontology/go-annotation#6394](https://github.com/geneontology/go-annotation/issues/6394)
- Ontology ticket: [geneontology/go-ontology#31963](https://github.com/geneontology/go-ontology/issues/31963)

## Obsoletion plan (per upstream)

| Obsoleted term | ID | Replacement |
|---|---|---|
| geranylgeranyl reductase activity | GO:0045550 | GO:0102067 geranylgeranyl diphosphate reductase activity |

The replacement term is substrate-specific (geranylgeranyl-**diphosphate**),
so any annotation that was made because the enzyme reduces a different
geranylgeranyl-conjugated substrate (e.g. free geranylgeraniol, geranylgeranyl
attached to a chlorophyll/tocopherol intermediate, or geranylgeranyl-CoA) is
not automatically a fit for the replacement and should be considered for
removal or remapping rather than a mechanical move.

## Affected experimental annotations (upstream list)

| # | Source | Accession | Symbol | Taxon | PMID | Evidence | Notes |
|---|---|---|---|---|---|---|---|
| 1 | TIGR | AGI_LocusCode:AT1G74470 | CHLP | NCBITaxon:3702 (Arabidopsis thaliana) | PMID:9492312 | IDA | Plant chlorophyll synthesis GGR — strong candidate to move cleanly to GO:0102067 |
| 2 | UniProt | UniProtKB:Q9ZS34 | CHLP | NCBITaxon:4097 | PMID:10398704 | NAS | Cyanobacterial/plant GGR ortholog — same family as #1; NAS evidence is weaker |
| 3 | UniProt | UniProtKB:P42330 | AKR1C3 | NCBITaxon:9606 (Homo sapiens) | PMID:21187079 | IDA | Aldo-keto reductase; geranylgeranyl reductase claim likely in-vitro side activity — flag for review |
| 4 | UniProt | UniProtKB:O60218 | AKR1B10 | NCBITaxon:9606 (Homo sapiens) | PMID:21187079 | IDA | Aldo-keto reductase; same paper as AKR1C3 — flag for review |

Group impact tally (from upstream): TIGR 1, UniProt 3.

## Mappings flagged for redirection

- `unirule2go`: UniRule:UR001995838 → GO:0045550
- `interpro2go`: IPR010253 (Geranylgeranyl reductase, plant/prokaryotic) → GO:0045550
- `interpro2go`: IPR011774 (Geranylgeranyl reductase, plant/cyanobacteria) → GO:0045550
- `interpro2go`: IPR023590 (Digeranylgeranylglycerophospholipid reductase) → GO:0045550

These are for upstream to redirect to GO:0102067 once the obsoletion is
applied. The plant/cyanobacterial CHLP/GGR family in IPR010253/IPR011774 is
substrate-correct for the replacement; IPR023590
(Digeranylgeranylglycerophospholipid reductase, archaeal lipid biosynthesis)
acts on a *digeranylgeranylglycerophospholipid* substrate that is not free
GGDP, so the IPR023590 mapping should be reviewed for whether GO:0102067 is
the right replacement.

## Impact on this repo

None of the four affected genes currently have an `*-ai-review.yaml` in this
repo (verified via `find genes -iname '*AKR1C3*' -o -iname '*AKR1B10*' -o
-iname '*CHLP*'` on 2026-05-03). This project is therefore primarily a
queueing exercise rather than a re-review of existing files.

## Scope

- Organism: human (AKR1C3, AKR1B10) plus Arabidopsis (CHLP) and a
  plant/cyanobacterial CHLP ortholog. The human entries are the highest-value
  candidates for review here because the AKR family is well-studied and the
  geranylgeranyl-reductase claim sits awkwardly against the established
  prostaglandin/steroid reductase function.
- GO branch: molecular function — reductase activity on prenyl/isoprenoid
  substrates.
- Type of fix: scientific — the obsoletion is not a pure rename; the
  substrate scope changes (anything → diphosphate). Some annotations that are
  IDA on GO:0045550 may not satisfy GO:0102067 if the experimental substrate
  was not GGDP, so each annotation needs evidence-grounded review rather than
  a mechanical relabel.

## Candidate genes for initial review

Listed in priority order. Each should be set up with
`just fetch-gene <organism> <gene>` before review begins.

1. **AKR1C3 (human, P42330)** — Aldo-keto reductase 1C3. The PMID:21187079
   IDA annotation to GO:0045550 should be evaluated against the actual
   substrate(s) tested. AKR1C3's well-characterised functions are
   prostaglandin / steroid 17-keto / 3α-hydroxysteroid reductase activities;
   any geranylgeranyl-reductase activity is likely in-vitro screening, not
   the in-vivo function. Likely outcome: REMOVE or MARK_AS_OVER_ANNOTATED on
   the GO:0045550 entry.
2. **AKR1B10 (human, O60218)** — Aldo-keto reductase 1B10. Same paper
   (PMID:21187079) and same critique as AKR1C3. Known primary function is
   retinal/farnesal reductase. Likely outcome similar to AKR1C3.
3. **CHLP (Arabidopsis, AT1G74470)** — Geranylgeranyl reductase in
   chlorophyll/tocopherol biosynthesis. PMID:9492312 IDA annotation. This is
   the canonical use of the term and the cleanest candidate to move to
   GO:0102067; useful as a positive control for the replacement.
4. **CHLP (taxon 4097, Q9ZS34)** — Plant/cyanobacterial CHLP ortholog.
   PMID:10398704 NAS evidence (lower-strength). Verify the taxon assignment
   and confirm orthology to the Arabidopsis CHLP before review.

## Proposed approach

1. **Wait for obsoletion to land before bulk-rewriting.** GO ontology
   ticket #31963 is still under discussion. AI Gene Review reviews can,
   however, proceed on the underlying biology now and just record the
   currently-live term ID; the action codes (ACCEPT vs MODIFY vs REMOVE) are
   what actually matter and those are independent of whether the obsoletion
   has been merged.
2. **Prioritise the human AKR pair.** AKR1C3 and AKR1B10 are the most
   scientifically interesting cases here — both are well-studied human
   enzymes whose IDA annotation to GO:0045550 deserves a critical evidence
   review rather than a mechanical remap. Start with AKR1C3.
3. **Use the plant CHLP as a positive control.** Reviewing the Arabidopsis
   CHLP entry is straightforward and helps confirm that GO:0102067 is the
   right replacement for genuine in-vivo GGR enzymes.
4. **Flag IPR023590 mapping question to upstream.** The
   digeranylgeranylglycerophospholipid reductase family does not act on free
   GGDP, so noting this on the upstream issue (or via a comment on
   #6394 / #31963) is a useful contribution even before any review work.

## Priority

Medium — the human AKR1C3 / AKR1B10 entries are interesting reviews on their
own merits, independent of the obsoletion timing. The plant CHLP entries are
lower priority and largely passive (will move cleanly to the replacement
term).

## Status

- 2026-05-03 — Project file created. Tracking upstream issue #6394 (opened
  2026-04-28). Obsoletion not yet applied. No reviews started; no genes from
  the upstream list are present in this repo yet.
