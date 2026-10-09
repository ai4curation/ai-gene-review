# Cul2 (Cullin-2) review notes

Accession: Q9V9R2. Module: dmel_vcb_ubiquitin_ligase (Cul2-Roc1a catalytic core).

## Literature journal

- VCB-Cul2 [PMID:11006129]; Roc1a binds Cul1-4 [PMID:18698375].
- JAK/STAT with Socs36E: [PMID:26277564 "We demonstrated that loss of Cul2 in the follicle cells significantly increased nuclear STAT protein levels, which resulted in additional cells acquiring invasive properties."]
- Ovarian niche Dpp [PMID:26206612]; testis germline enclosure [PMID:25459658]; NMJ and female germline [PMID:21869472]; CrPV-1A [PMID:30308158].

## Decisions

- Core MF GO:0160072 scaffold, contributes_to GO:0061630; GO:0031462. Same pattern as Cul1.
- SCF ubiquitin ligase complex and SCF-dependent catabolism IBA rows (node PTN000231993, all Cul1 donors): REMOVE as over-propagation to the Cul2 paralog.
- General terms MODIFY: GO:0006511/GO:0030163 -> GO:0043161; GO:0031461 -> GO:0031462.
- GO:0016567 ACCEPT (fly evidence shows ubiquitination without chain type; as precise as warranted), same as Vhl.

## Deep research (falcon, added after the initial review)

The falcon deep-research run finished after the initial commit and is now in `Cul2-deep-research-falcon.md`. Its synthesis is consistent with the annotation decisions above; no review actions were changed.
