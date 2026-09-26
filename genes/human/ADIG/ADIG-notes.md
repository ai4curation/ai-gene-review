# ADIG (adipogenin / SMAF1, Q0VDE8) — review notes

2026-09-26. PAINT no-IBA backlog. Deep research provider: affinage.

## Headline

Every one of ADIG's 16 GO annotations is non-experimental (5 IBA, 2 IEA, 9 ISS), and all of
them descend from mouse Adig (UniProtKB:Q8R400 / MGI:MGI:2675492). So this is a pure
propagation review. What makes it worth doing carefully is that **the donor set was
re-adjudicated in 2025 and GOA has not caught up**.

## The recall gap in the deep-research file

The affinage record's own trust gates passed (accession matches Q0VDE8, no non-human organism
token, pairwise self-evaluation `win`, faith 100%). Its citations are all real and on-topic —
precision is fine. **Recall is not.** Its most important dated finding, the seipin cryo-EM
work, is listed with `PMIDs: —` and journal `bioRxiv`:

> [file:genes/human/ADIG/ADIG-deep-research-affinage.md "Adig directly interacts with seipin to form a rigid complex"]

That preprint (PMID:39211078, bioRxiv 2024-07-26) **published in Science on 2025-11-06** as
PMID:41196993, doi 10.1126/science.adr9755 — resolved via the NCBI esearch API, not from
memory. Note the dates: the affinage record's own `affinage_run_date` is 2026-06-09, seven
months *after* the Science paper appeared, so this is not a stale-snapshot problem — the
published version was available and was not retrieved. This is a recurring pattern in the
campaign: the gates certify that what affinage returned is real, never that it returned
everything, so partners, family members and paralogs have to be searched independently.

Consequence: affinage's `mechanism_profile` still says

> [file:genes/human/ADIG/ADIG-deep-research-affinage.md "**localization:** GO:0005811 lipid droplet"]

which this review declines, for the reasons below.

## What PMID:41196993 settles

It is unusual in that it explicitly set out to adjudicate ADIG's contested localization:

> [PMID:41196993 "We next assessed the subcellular location of Adig because previous reports suggest different locations, including the plasma membrane (2), nuclei (3), and the surface of LDs (4)."]

Three orthogonal assays — EGFP fused at either terminus against ER-mCherry-KDEL; APEX2
electron microscopy at near-endogenous levels in Adig-KO adipocytes; digitonin protease
protection — converge:

> [PMID:41196993 "Thus, Adig is a single-pass ER protein with a cytosolic C-terminal tail"]

UniProt has already absorbed this (Q0VDE8: "Endoplasmic reticulum membrane ... Single-pass
membrane protein", TRANSMEM 14..38, and SUBUNIT "Forms a dodecameric complex with seipin
(BSCL2)"). GOA has not.

Mechanism:

> [PMID:41196993 "The most enriched protein with substantial sequence coverage was seipin"]
> [PMID:41196993 "Adig selectively bound to the dodecameric form and enhanced seipin assembly by bridging and stabilizing adjacent subunits."]
> [PMID:41196993 "Thus, when expressed with Adig, seipin appeared to form functional seipin-Adig complexes rather than seipin aggregates."]

## Nucleus: removed

Both nucleus rows trace to one 2005 result:

> [PMID:15567149 "Transfection and localization studies of a SMAF1-EGFP fusion construct indicate nuclear localization, suggestive of a possible regulatory role."]

ADIG is 80 aa / ~10 kDa — far below the passive nuclear-pore diffusion limit — so an EGFP
fusion in the nucleoplasm says nothing about the endogenous protein, and the authors
themselves wrote "suggestive". PMID:41196993 named this claim and replaced it. These are
ISS/IBA rows, not experimental ones, so REMOVE here is not overruling a curator who read a
full text I cannot see.

## Lipid droplet: modified, not accepted

This one is more interesting than it looks. The LD location rests on

> [PMID:26427354 "immunolocalization studies using HA-tagged Smaf1 reveal enrichment at adipocyte lipid droplets"]

i.e. an overexpressed tagged construct. But PMID:41196993 goes further than simply not
reproducing it — live-cell tracking shows the Adig-bound species is *specifically* the one
that does not dock at droplets:

> [PMID:41196993 "they formed stable contacts with seipin complexes without Adig, while seipin-Adig complexes moved rapidly through their vicinity"]

So ADIG acts *on* droplet formation from the ER, in trans through seipin, rather than residing
on the droplet. MODIFY → GO:0005789.

## The missing half of the annotation set

**There is not one molecular function term among the 16 annotations.** For a protein whose
entire biology is a structural protein–protein interaction, that is the largest gap. Added as
NEW (all ISS from PMID:41196993, since the structures are mouse/human seipin–Adig):

- GO:0044877 protein-containing complex binding — and note it is *oligomer-state selective*,
  which generic protein binding could never express.
- GO:0031334 positive regulation of protein-containing complex assembly — bridging adjacent
  subunits is doing the work of assembly, so the participation test is met.
- GO:0050821 protein stabilization — the definition's anti-aggregation clause is met literally.

GO has **no seipin complex term** (OLS returns nothing for "seipin complex"), so `in_complex`
had to be left empty; filed under `proposed_new_terms` with parent GO:0140534.

## Tension worth flagging

Acute siRNA knockdown gave a negative result:

> [PMID:26427354 "Smaf1 does not have a major role in adipocyte triglyceride accumulation, lipolysis or insulin-stimulated pAkt induction"]

whereas germline knockout does:

> [PMID:33691105 "Data from Adig-deficient cells suggest that Adig is required for adipogenesis."]
> [PMID:33691105 "Adig-/- mice are leaner than wild-type mice when fed a high-fat diet and when crossed with Ob/Ob hyperphagic mice"]

Recorded on the GO:0019915 row rather than suppressed. Plausibly developmental vs. acute
requirement, or slow seipin oligomer turnover — captured in suggested_experiments as a degron
experiment.

## Human relevance

All the functional work is rodent, but PMID:33691105 notes a GWAS association of the ADIG
locus with BMI-adjusted leptin levels, which is the one piece of direct human evidence and the
reason the ISS transfers are worth making rather than leaving the human gene bare.

## Outcome

19 rows: 11 ACCEPT, 3 MODIFY, 3 NEW, 2 REMOVE. `just validate human ADIG` passes.
