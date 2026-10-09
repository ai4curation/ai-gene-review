# EloB (Elongin B) review notes

Accession: Q7KSB2 (expected accession; `just fetch-gene DROME EloB` resolved to O44226, which also has GOA rows; refetched with `--alias EloB` on Q7KSB2). Planned FlyBase gene-group module (not yet committed to modules/ on main): dmel_vcb_ubiquitin_ligase.

## Literature journal

- VCB-Cul2 [PMID:11006129] (quotes as in EloC notes).
- Wing veins: [PMID:24204884 "Among heterozygous EloBEP3132 females, 28.8% showed a truncated L5 vein"].
- Ago-2 degradation by viral ligase: [PMID:30308158 "Compared to control cells, knockdown of either Cul2 or EloB stabilized Ago-2 protein levels by CrPV infection"].
- JAK/STAT via Socs36E-Cul5 [PMID:23885117]; muscle screen [PMID:25088419]; Dora TDMD [PMID:40328417].

## Decisions

- Core: contributes_to GO:0061630 in GO:0030891 VCB complex (no own MF asserted; EloB is the ubiquitin-like stabilizer of EloC); second core function in the Elongin complex.
- ARBA general complexes MODIFY to GO:0030891 / GO:0031462; viral process MARK_AS_OVER_ANNOTATED; positive regulation of catabolism non-core.

## Deep research (falcon, added after the initial review)

The falcon deep-research run finished after the initial commit and is now in `EloB-deep-research-falcon.md`. Its synthesis is consistent with the annotation decisions above; no review actions were changed.

## Revision after PR #4471 review

- GO:0016032 viral process is now KEEP_AS_NON_CORE rather than MARK_AS_OVER_ANNOTATED: GO uses this term for host products that take part in a viral life cycle (CrPV-1A co-opts the host Cul2-EloBC ligase), matching the precedent in genes/ECOLI/DnaJ. This replaces the earlier viral-process decision above.
- GO:0140535 is now MODIFY to all four supported complexes (VCB, Elongin, Cul2-RING, Cul3-RING), not VCB alone.
