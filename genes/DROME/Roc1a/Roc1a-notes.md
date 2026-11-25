# Roc1a (RING-box protein 1A; Rbx1 ortholog) review notes

Accession: Q9W5E1. Planned FlyBase gene-group module (not yet committed to modules/ on main): dmel_scf_slimb_ubiquitin_ligase and dmel_vcb_ubiquitin_ligase (catalytic core with Cul1 / Cul2). Reviewed once covering both.

## Literature journal

- Own E3 activity: purified Roc proteins tested "using a previously described in vitro assay that detects E2- and GST-Roc-dependent polyubiquitin formation in the absence of either Cullin or a particular substrate" and [PMID:18698375 "Roc1a and Roc2 displayed high E3 ligase activity, whereas Roc1b showed a weaker ability to promote poly-ubiquitylation"].
- Cullin specificity: [PMID:18698375 "we show that Drosophila Roc proteins bind specific Cullins: Roc1a binds Cul1-4"].
- SCF/Ci: [PMID:12062088 "This suggests that Slimb and Roc1a function in the same SCF complex to target Ci but that a different RING-H2 protein acts with Slimb to target Arm."]; however Roc1a is essential for Arm stability in S2 cells [PMID:22359584 "we find that Roc1/Roc1a is essential for regulating Armadillo stability"].
- Non-redundancy with Roc1b/Roc2 [PMID:15331761]; yeast Hrt1 complementation [PMID:11500045].
- VHL complex: [PMID:11006129 "Like human VHL, Drosophila VHL complex containing Cul-2, Rbx1, Elongins B and C, exhibits E3 ubiquitin ligase activity."]
- CrPV-1A hijacks Cul2-Rbx1-EloBC [PMID:30308158].

## Decisions

- Own activity shown, so core MF is GO:0061630 ubiquitin protein ligase activity as molecular_function (not contributes_to), in both SCF (GO:0019005) and Cul2-RING (GO:0031462) core functions. The scaffold/adaptor subunits (Cul1, SkpA, Cul2, EloB, EloC) and receptors use contributes_to GO:0061630.
- GO:0004842 -> MODIFY to GO:0061630; GO:0016567 -> MODIFY to GO:0000209; GO:0006508 -> MODIFY to GO:0031146 (batch rule for correct-but-general terms).
- GO:0031461 CRL complex and GO:0006511 accepted because Roc1a acts in Cul1-4 ligases (as precise as warranted).
- GO:0016032 viral process: MARK_AS_OVER_ANNOTATED (viral hijacking of the host ligase).
- Protein binding (Ufd1-like): REMOVE.

## Deep research (falcon, added after the initial review)

The falcon deep-research run finished after the initial commit and is now in `Roc1a-deep-research-falcon.md`. Its synthesis is consistent with the annotation decisions above; no review actions were changed.

## Revision after PR #4471 review

- GO:0016032 viral process is now KEEP_AS_NON_CORE rather than MARK_AS_OVER_ANNOTATED: GO uses this term for host products that take part in a viral life cycle (CrPV-1A co-opts the host Cul2-EloBC ligase), matching the precedent in genes/ECOLI/DnaJ. This replaces the earlier viral-process decision above.
- The PMID:11006129 positive-regulation row now names GO:0043161 as the direct process; zinc-binding and polyubiquitination quotes retargeted; reason explains GO:0000209 rather than GO:0070979.
