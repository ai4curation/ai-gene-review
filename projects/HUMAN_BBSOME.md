---
title: "Human BBSome Project"
maturity: MATURE
tags: [BIOLOGY_DOMAIN]
species: [human]
genes: [BBS1, BBS2, ARL6, BBS4, BBS5, MKKS, BBS7, TTC8, BBS9, BBS10, BBS12, LZTFL1, BBIP1, CCDC28B]
manifest:
  slides:
    - href: HUMAN_BBSOME/slides/HUMAN_BBSOME-slides.html
      description: AI generated
  artifacts:
    - href: https://claude.ai/artifact/LHycMPW3frEEecc1J3b1Yr
      title: Project brief
---

# Human BBSome Project

**Bottom line:** the BBSome is the eight-subunit coat that sorts signalling
receptors into and out of the primary cilium, and its loss causes Bardet–Biedl
syndrome. We reviewed every existing GO annotation for the 14 BBS-associated
human genes (the eight core subunits, the ARL6 recruiter, the LZTFL1 and
CCDC28B regulators, and the MKKS/BBS10/BBS12 assembly chaperonins) and built a
reusable [BBSome module](../modules/bbsome.html). All 14 reviews and the module
validate. The main corrections were demoting the pervasive `protein binding`
IPI rows in favour of BBSome membership (GO:0034464) or specific MF terms,
treating the three chaperonin-like BBS proteins as assembly factors rather than
subunits, and removing two over-propagated BBS2 IEA localizations.

We did this because the BBSome is a well-bounded complex with a strong
structural literature, which makes it a clean test of whether per-gene review
recovers the division of labour inside a complex (cargo recognition,
membrane recruitment, assembly) instead of copying one generic
"cilium" story onto every subunit.

## Overview

The **BBSome** is an octameric protein complex (GO:0034464) that functions as a
coat-like adaptor for ciliary membrane-protein trafficking. It recognizes signaling
receptor cargo (e.g. GPCRs such as SSTR3, MCHR1, the Hedgehog effectors SMO and GPR161)
and couples them to the intraflagellar transport (IFT) machinery, mediating both
import into and, especially, retrieval/export out of the primary cilium across the
transition zone. BBSome dysfunction causes **Bardet–Biedl syndrome (BBS)**, a
pleiotropic ciliopathy featuring retinal degeneration, obesity, polydactyly, renal
anomalies, hypogonadism, and cognitive impairment.

This project reviews the GO annotations of the BBS-associated genes and builds a
reusable **cell-component module** for the BBSome under `modules/bbsome.yaml`.

## Complex architecture

- **Core BBSome (octamer):** BBS1, BBS2, BBS4, BBS5, BBS7, TTC8 (BBS8), BBS9, BBIP1 (BBS18).
  BBS2/BBS7/BBS9 form a β-propeller/GAE/platform core; BBS1 is the principal cargo/ARL6
  interaction subunit; BBS4 and BBS8 (TPR subunits) and BBS5 (PH-domain, PtdIns binding)
  and the small BBIP1 stabilize the assembly.
- **Membrane recruiter:** ARL6 (BBS3), an Arf-like small GTPase that, in its GTP-bound
  state, recruits the BBSome to the ciliary membrane and polymerizes the coat.
- **Trafficking regulator:** LZTFL1 (BBS17) regulates BBSome ciliary entry/retrieval and
  associates with the complex in the cytoplasm.
- **BBS chaperonin complex (assembly factors, not BBSome subunits):** MKKS (BBS6),
  BBS10, BBS12 — three chaperonin-like proteins that, with CCT/TRiC, assemble the BBSome
  core. CCDC28B is an accessory modifier of BBSome ciliary localization.

> Note: Other "BBS" loci (e.g. IFT27/BBS19, IFT172/BBS20, MKS1/BBS13, CEP290/BBS14,
> SDCCAG8/BBS16, WDPCP/BBS15, C8orf37/BBS21, TRIM32/BBS11) belong primarily to the IFT,
> transition-zone, or other ciliary modules and are out of scope for this BBSome-centric
> project (candidates for separate IFT / transition-zone modules).

## Genes for Review

| # | HGNC | BBS locus | UniProt | Role |
|---|------|-----------|---------|------|
| 1 | BBS1 | BBS1 | Q8NFJ9 | Core subunit; principal cargo/ARL6 interface |
| 2 | BBS2 | BBS2 | Q9BXC9 | Core subunit; β-propeller core |
| 3 | ARL6 | BBS3 | Q9H0F7 | Arf-like GTPase; membrane recruitment of BBSome |
| 4 | BBS4 | BBS4 | Q96RK4 | Core subunit; TPR adaptor |
| 5 | BBS5 | BBS5 | Q8N3I7 | Core subunit; PH domains, phosphoinositide binding |
| 6 | MKKS | BBS6 | Q9NPJ1 | Chaperonin-like; BBSome assembly |
| 7 | BBS7 | BBS7 | Q8IWZ6 | Core subunit; β-propeller core |
| 8 | TTC8 | BBS8 | Q8TAM2 | Core subunit; TPR adaptor |
| 9 | BBS9 | BBS9 | Q3SYG4 | Core subunit; platform/scaffold |
| 10 | BBS10 | BBS10 | Q8TAM1 | Chaperonin-like; BBSome assembly |
| 11 | BBS12 | BBS12 | Q6ZW61 | Chaperonin-like; BBSome assembly |
| 12 | LZTFL1 | BBS17 | Q9NQ48 | Regulates BBSome ciliary trafficking |
| 13 | BBIP1 | BBS18 | A8MTZ0 | Core subunit; complex stabilization |
| 14 | CCDC28B | — | Q9BUN5 | Accessory modifier of BBSome ciliary localization |

## Deliverables

1. `modules/bbsome.yaml` — cell-component module (`ModuleReview`, `CELLULAR_COMPONENT`/
   `PROTEIN_COMPLEX`) describing BBSome composition, assembly, recruitment, and cargo
   trafficking, grounded in GO:0034464.
2. Per-gene `genes/human/<GENE>/<GENE>-ai-review.yaml` — full annotation reviews.
3. Per-gene `<GENE>-notes.md` research notes with cited provenance.

## Project Status

- [x] Define gene set (14 BBS-associated genes) and confirm scope (all BBS-associated)
- [x] Fetch UniProt/GOA/publications for all genes
- [x] Build `modules/bbsome.yaml` cell-component module (passes `linkml-validate` + term-validator)
- [x] Per-gene annotation reviews (14/14)
- [x] Validate all (module + all 14 gene reviews `✓ Valid`)
- [ ] Pathway/summary integration (optional follow-up)

### Review summary (completed 2026-06-14; counts re-derived from the review YAMLs 2026-09-26)

All 14 gene reviews are complete and validate cleanly. Each gene received a
standalone `description`, full per-annotation review (action + summary + reason),
`core_functions`, `suggested_questions`/`suggested_experiments`, `reference_review`
blocks, and a `<GENE>-notes.md` research journal with cited provenance.

| Gene | Ann (+NEW) | ACCEPT | Non-core | Over-ann. | MODIFY | REMOVE |
|------|-----------|--------|----------|-----------|--------|--------|
| BBS1 | 60 | 26 | 7 | 23 | 4 | 0 |
| BBS2 | 67 | 16 | 24 | 25 | 0 | 2 |
| ARL6 | 38 | 11 | 21 | 6 | 0 | 0 |
| BBS4 | 110 | 42 | 37 | 31 | 0 | 0 |
| BBS5 | 44 | 18 | 12 | 14 | 0 | 0 |
| MKKS | 60 (+1) | 5 | 21 | 32 | 2 | 0 |
| BBS7 | 48 (+1) | 15 | 18 | 14 | 1 | 0 |
| TTC8 | 45 | 23 | 10 | 12 | 0 | 0 |
| BBS9 | 48 (+1) | 20 | 13 | 13 | 2 | 0 |
| BBS10 | 12 (+2) | 5 | 4 | 3 | 0 | 0 |
| BBS12 | 12 (+1) | 3 | 3 | 6 | 0 | 0 |
| LZTFL1 | 24 | 13 | 2 | 9 | 0 | 0 |
| BBIP1 | 22 (+3) | 11 | 8 | 3 | 0 | 0 |
| CCDC28B | 6 | 4 | 0 | 2 | 0 | 0 |

**Cross-cutting findings:**
- The pervasive uninformative `protein binding` (GO:0005515) IPI annotations were
  consistently flagged (`MARK_AS_OVER_ANNOTATED`), with the real biology captured by
  BBSome membership (GO:0034464) or specific MF terms (e.g. BBS1→`small GTPase binding`
  for the ARL6/BBS3-GTP interaction).
- The chaperonin-like assembly factors (MKKS/BBS6, BBS10, BBS12) are correctly treated as
  **assembly factors, not structural BBSome subunits**; their core MF is now the
  non-obsolete GO:0044183 (`protein folding chaperone`) — the obsolete GO:0051082
  (`unfolded protein binding`) surfaced during review was replaced here and in the module.
- A recurring `RNA Pol II transcription factor binding` (GO:0061629) annotation derived
  from a BBS7-centric study (PMID:22302990) was flagged as MISCITED/DISPUTED across the
  scaffold subunits.
- BBS2 had two over-propagated electronic (IEA) annotations (`microvillus`, `stereocilium`)
  removed as biologically unsupported.

## Key References

- Nachury MV et al. (2007) Cell — Identification of the BBSome as a ciliary coat complex.
- Loktev AV et al. (2008) Dev Cell — BBIP10/BBIP1 as the 8th BBSome subunit.
- Jin H et al. (2010) Cell — ARL6/BBS3 recruits the BBSome; coat polymerization.
- Klink BU et al. (2020) eLife / Singh SK et al. (2020) — Cryo-EM architecture of the BBSome.
- Seo S et al. (2010) PNAS — BBS chaperonins (MKKS/BBS6, BBS10, BBS12) + CCT mediate BBSome assembly.
- Nachury MV (2018) Phil Trans R Soc B — BBSome trafficking and ciliary GPCR retrieval.
