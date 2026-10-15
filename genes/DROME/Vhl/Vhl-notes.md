# Vhl review notes

Accession: Q9V3C1. Planned FlyBase gene-group module (not yet committed to modules/ on main): dmel_vcb_ubiquitin_ligase (substrate receptor).

## Literature journal

- [PMID:11006129 "Biochemical studies have shown that Drosophila VHL protein binds to Elongins B and C directly, and via this Elongin BC complex, associates with Cul-2 and Rbx1."]; HIF-1alpha is the target.
- Sima export: [PMID:19587118 "CRM1-dependent nuclear export requires both oxygen-dependent hydroxylation of a specific prolyl residue (Pro850) in the ODDD, and the activity of the von Hippel Lindau tumor suppressor factor."]
- Trachea: [PMID:10851083], [PMID:19285057], [PMID:20516215 "dVHL regulates branch migration and lumen formation via its endocytic function"].
- Epithelial polarity via microtubules [PMID:20388653]; Mgr/prefoldin tubulin [PMID:22451918]; Trc8 interaction [PMID:12032852].

## Decisions

- Core MF GO:1990756 adaptor, contributes_to GO:0061630; GO:0030891; process GO:0043161 and GO:1900038.
- GO:1900037 -> MODIFY GO:1900038 (direction is negative).
- Transcription corepressor / regulation of transcription IBA (single human VHL donor) and derived IEA: MARK_AS_OVER_ANNOTATED (effects indirect via Sima).
- Protein binding: EloC row REMOVE (no informative binding term; captured by VCB complex); Trc8 row MODIFY to GO:0031625.

## Deep research (falcon, added after the initial review)

The falcon deep-research run finished after the initial commit and is now in `Vhl-deep-research-falcon.md`. Its synthesis is consistent with the annotation decisions above; no review actions were changed.
