---
title: "Human BBSome Project"
---

# Human BBSome Project

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

(UniProt IDs to be confirmed from fetched records.)

## Deliverables

1. `modules/bbsome.yaml` — cell-component module (`ModuleReview`, `CELLULAR_COMPONENT`/
   `PROTEIN_COMPLEX`) describing BBSome composition, assembly, recruitment, and cargo
   trafficking, grounded in GO:0034464.
2. Per-gene `genes/human/<GENE>/<GENE>-ai-review.yaml` — full annotation reviews.
3. Per-gene `<GENE>-notes.md` research notes with cited provenance.

## Project Status

- [x] Define gene set (14 BBS-associated genes) and confirm scope (all BBS-associated)
- [ ] Fetch UniProt/GOA/publications for all genes
- [ ] Build `modules/bbsome.yaml` cell-component module
- [ ] Per-gene annotation reviews (0/14)
- [ ] Validate all (`just validate-all` / `linkml-validate`)
- [ ] Pathway/summary integration

## Key References

- Nachury MV et al. (2007) Cell — Identification of the BBSome as a ciliary coat complex.
- Loktev AV et al. (2008) Dev Cell — BBIP10/BBIP1 as the 8th BBSome subunit.
- Jin H et al. (2010) Cell — ARL6/BBS3 recruits the BBSome; coat polymerization.
- Klink BU et al. (2020) eLife / Singh SK et al. (2020) — Cryo-EM architecture of the BBSome.
- Seo S et al. (2010) PNAS — BBS chaperonins (MKKS/BBS6, BBS10, BBS12) + CCT mediate BBSome assembly.
- Nachury MV (2018) Phil Trans R Soc B — BBSome trafficking and ciliary GPCR retrieval.
