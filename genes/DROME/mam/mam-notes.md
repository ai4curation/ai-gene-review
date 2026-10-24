# mam (mastermind) — curation notes (DROME, P21519)

## Session 2026-09-30 (Notch signaling module)

Deep research: first falcon attempt hit Edison 429 rate limiting; the relaunch produced
`mam-deep-research-falcon.md` (used for corroboration of the ternary-complex role).

### Key findings
- Drosophila Mam forms the ternary complex with NICD and Su(H) at E(spl) [PMID:11390662].
- Mam lengthens CSL dwell time at Notch-ON targets [PMID:29478922].
- Mam binds >100 polytene chromosome sites [PMID:8725234]; chromatin binding partly depends on
  Nipped-A (SAGA/Tip60) [PMID:16508010].
- Dominant-negative truncations phenocopy Notch loss (lateral inhibition failure) [PMID:10545243].
- Notch-independent requirement in ovarian follicle stem cells [PMID:19474148 "This suggests an
  unconventional role for Mam in FSCs that is independent of Notch signaling."].

### PANTHER / IBA problem
UniProt DR PANTHER: PTHR16431 ("NEUROGENIC PROTEIN MASTERMIND") / PTHR16431:SF1 ("NEUROGENIC
PROTEIN MASTERMIND"). The cached family table (interpro/panther/PTHR16431) shows this family is
otherwise composed of Mis18 proteins (human MIS18A Q9NYP9, OIP5 O43482, mouse Oip5/Mis18a,
S. pombe mis18 Q9P802 — which is even placed in SF1 with mam). The PAINT node PTN001046424 carries
IBDs for GO:0000775 centromeric region and GO:0034080 CENP-A containing chromatin assembly seeded
only by Mis18 genes (MGI:MGI:1913828, PomBase:SPCC970.12). These propagate to mam as IBA; REMOVED
with propagation_review (PROPAGATION_BAD / WRONG_ORTHOLOG_OR_PARALOG). Nucleus and chromatin IBAs
from the same node are correct for mam on independent evidence and were kept.

### Decisions
- Core MF: GO:0003713 transcription coactivator activity (nucleus; in GO:1990433).
- NEW: GO:0007221 (IDA, PMID:11390662).
- MARK_AS_OVER_ANNOTATED: GO:0016607 nuclear speck (InterPro2GO; mammalian MAML detail).
