# UFM1 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: P61960
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07c
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/UFM1/UFM1-ai-review.yaml](UFM1-ai-review.yaml)
- AIGR review HTML: present - [genes/human/UFM1/UFM1-ai-review.html](UFM1-ai-review.html)
- Gene notes: present - [genes/human/UFM1/UFM1-notes.md](UFM1-notes.md)
- GOA TSV: present - [genes/human/UFM1/UFM1-goa.tsv](UFM1-goa.tsv)
- UniProt record: present - [genes/human/UFM1/UFM1-uniprot.txt](UFM1-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/UFM1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/UFM1.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/UFM1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/UFM1.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: UFM1 (ubiquitin-fold modifier 1) is a small (85 aa precursor; 83 aa mature) metazoan- and plant-specific ubiquitin-like protein modifier. It is itself the covalent tag of the ufmylation pathway, not an enzyme. The precursor is processed at its C-terminus (removal of the Ser-Cys dipeptide) to expose Gly-83, which is then conjugated via an isopeptide bond to lysine residues of substrate proteins as a monomer or a lysine-linked polymer. Conjugation (ufmylation) proceeds through a dedicated enzymatic cascade analogous to ubiquitylation, comprising the E1-activating enzyme UBA5, the E2-conjugating enzyme UFC1, and the E3 ligase UFL1 (with its ER-membrane cofactor DDRGK1/UFBP1); it is reversed by the UFM1-specific proteases UFSP1 and UFSP2. The principal substrate is the 60S ribosomal protein RPL26 (uL24) on endoplasmic-reticulum-bound ribosomes, and ufmylation acts in co-translational protein biogenesis at the ER, recycling of 60S ribosomal subunits from the ER, reticulophagy (ER-phagy), the response to ER stress, and the DNA-damage response. UFM1 is found in the cytoplasm and nucleus, with its conjugation machinery enriched at the cytoplasmic surface of the ER. Loss of ufmylation causes hypomyelinating leukodystrophy (HLD14) and is essential for embryonic and brain development.
- Existing/core annotation action counts: ACCEPT: 12; KEEP_AS_NON_CORE: 27; MARK_AS_OVER_ANNOTATED: 3

## PN Consistency Summary

- **Consistency:** Strong. Notes/review/PN agree UFM1 is the modifier (not an enzyme), conjugated via Gly-83 isopeptide bond; principal substrate RPL26. Review ACCEPTs GO:0071569 (multiple), GO:1990592 (K69-linked ufmylation, IDA), cytoplasm; ER-stress/reticulophagy/brain-development/ER-signaling KEEP_AS_NON_CORE; two MARK_AS_OVER_ANNOTATED (neg reg apoptosis, neg reg nuclear import). No contradictions.
- **PN story / NEW pressure:** All PN assertions captured. The review's core MF GO:0031386 (protein tag activity; verified real) is a curatorial assignment NOT in GOA (UFM1 GOA MF rows are only GO:0005515 IPI) — this is the one defensible **ADD** candidate, well-justified for a UBL tag. GO:0006515 (verified) projected new_to_goa via RQC group is broad and not a direct fit for the modifier itself. Conclusion: ufmylation/ERphagy already captured; GO:0031386 a sound add at MF; GO:0006515 over-reaches.
- **Evidence alignment:** PN row 3 cites "28234446 / rev" (review article, not in review YAML); review uses PMID:15071506, 30626644, 25219498 etc. PN ERphagy row cites the screen (PMID:32160526, in notes). Core ufmylation evidence overlaps thematically; PN's family-review PMID is non-overlapping by design.
- **Verdict:** Consistent and complete; PN story fully captured. GO:0031386 protein tag activity is a justified MF add (curatorial, absent from GOA); GO:0006515 not warranted as a direct UFM1 term.

## Full Consistency Review

- **UniProt:** P61960 · **batch:** proteostasis-batch-2026-06-07c · **review status:** complete (core MF GO:0031386 protein tag activity; many IPI/protein-binding rows triaged)
- **PN placement:** `Translation|Cytosolic translation|Ribosome-associated QC|UFMylation`; `ALP|...|ERphagy|UFMylation of ER proteins`; `UPS|Ubiquitin and UBL proteins|ubiquitin-like modifier|UFM1` ; **PN-node mapping:** UFMylation type→GO:0071569; ERphagy→GO:0061709; UBL-modifier type & group→no_mapping (correct — UFM1 is the tag, not an enzyme); class→context-only GO:0019787.
- **Consistency:** Strong. Notes/review/PN agree UFM1 is the modifier (not an enzyme), conjugated via Gly-83 isopeptide bond; principal substrate RPL26. Review ACCEPTs GO:0071569 (multiple), GO:1990592 (K69-linked ufmylation, IDA), cytoplasm; ER-stress/reticulophagy/brain-development/ER-signaling KEEP_AS_NON_CORE; two MARK_AS_OVER_ANNOTATED (neg reg apoptosis, neg reg nuclear import). No contradictions.
- **PN story / NEW pressure:** All PN assertions captured. The review's core MF GO:0031386 (protein tag activity; verified real) is a curatorial assignment NOT in GOA (UFM1 GOA MF rows are only GO:0005515 IPI) — this is the one defensible **ADD** candidate, well-justified for a UBL tag. GO:0006515 (verified) projected new_to_goa via RQC group is broad and not a direct fit for the modifier itself. Conclusion: ufmylation/ERphagy already captured; GO:0031386 a sound add at MF; GO:0006515 over-reaches.
- **Mapping strategy:** PN appropriately gives the UBL-modifier nodes no_mapping (a tag is not a transferase) and keeps GO:0019787 as class context only — consistent with the review using GO:0031386. UFM1 does not change the node.
- **Evidence alignment:** PN row 3 cites "28234446 / rev" (review article, not in review YAML); review uses PMID:15071506, 30626644, 25219498 etc. PN ERphagy row cites the screen (PMID:32160526, in notes). Core ufmylation evidence overlaps thematically; PN's family-review PMID is non-overlapping by design.
- **Verdict:** Consistent and complete; PN story fully captured. GO:0031386 protein tag activity is a justified MF add (curatorial, absent from GOA); GO:0006515 not warranted as a direct UFM1 term.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07c
- review_yaml: genes/human/UFM1/UFM1-ai-review.yaml
- PN workbook rows: 3

## PN row 1: Translation | Cytosolic translation | Ribosome-associated QC | UFMylation
- UniProt: P61960
- In branches: TR, ALP, UPS
- PN-node mapping records (path + ancestors):
    - [type] Translation|Cytosolic translation|Ribosome-associated QC|UFMylation
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0071569 protein ufmylation]
        rationale: This PN RQC type denotes UFM1 conjugation in ribosome quality control. Protein ufmylation is the shared process target.
    - [group] Translation|Cytosolic translation|Ribosome-associated QC
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0006515 protein quality control for misfolded or incompletely synthesized proteins]
        rationale: The PN ribosome-associated quality-control group covers surveillance and disposal of stalled or defective nascent-chain translation products. GO lacks a dedicated ribosome-associated QC term in the local cache, so the broader protein-quality-control process is the best supported target.
    - [class] Translation|Cytosolic translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0002181 cytoplasmic translation]
        rationale: The PN class Cytosolic translation is centered on the cytoplasmic translation apparatus and process, but it also houses supporting machinery such as ribosome biogenesis factors. The GO process term is a useful high-level label for the class, but propagating it to all members would over-annotate genes whose PN placement is through assembly or maturation context rather than core cytoplasmic translation.
    - [branch] Translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0006412 translation]
        rationale: The PN Translation branch is organized around the translation apparatus and immediately associated cotranslational quality-control systems. GO translation is the closest high-level process label, but the PN branch also contains adjacent machinery such as ribosome biogenesis and nascent-chain handling. Keeping this relationship is useful for interpretation, but it is too broad to project safely onto every member.

## PN row 2: Autophagy-Lysosome Pathway | Autophagy substrate selection | Marking substrates for selective autophagy | ERphagy | UFMylation of ER proteins
- UniProt: P61960
- In branches: TR, ALP, UPS
- Notes: The UFM for UFMylation to target ER sheets for autophagy.
- PN references (titles):
    - A Genome-wide ER-phagy Screen Highlights Key Roles of Mitochondrial Metabolism and ER-Resident UFMylation - ScienceDirect
- PN-node mapping records (path + ancestors):
    - [subtype] Autophagy-Lysosome Pathway|Autophagy substrate selection|Marking substrates for selective autophagy|ERphagy|UFMylation of ER proteins
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0061709 reticulophagy]
        rationale: This PN subtype captures a specific ER-cargo marking mechanism used in ERphagy. Because GO uses reticulophagy for ER autophagy, this subtype can propagate to reticulophagy.
    - [type] Autophagy-Lysosome Pathway|Autophagy substrate selection|Marking substrates for selective autophagy|ERphagy
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0061709 reticulophagy]
        rationale: The PN ERphagy marking category captures factors that mark ER cargo for selective autophagic turnover. GO uses reticulophagy for this pathway, so propagation to reticulophagy is appropriate.
    - [group] Autophagy-Lysosome Pathway|Autophagy substrate selection|Marking substrates for selective autophagy
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN taxonomy container. The descendants mix components, regulators, context labels, and mechanistic leaves, so propagation should come only from narrower curated nodes.
    - [class] Autophagy-Lysosome Pathway|Autophagy substrate selection
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad substrate-selection container. GO has useful targets for specific receptor, cargo-adaptor, and selective-autophagy leaves, but this class mixes marking, recognition, receptor regulation, and unknown roles and should not propagate as one term.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## PN row 3: Ubiquitin Proteasome System | Ubiquitin and UBL proteins | ubiquitin-like modifier | UFM1
- UniProt: P61960
- In branches: TR, ALP, UPS
- Signature domains: IPR005375
- Auxiliary domains: (none)
- PN references (titles):
    - 28234446 / rev
- PN-node mapping records (path + ancestors):
    - [type] Ubiquitin Proteasome System|Ubiquitin and UBL proteins|ubiquitin-like modifier|UFM1
        status=no_mapping scope= GO=[]
        rationale: Reviewed manually as a UPS source node. No single GO term is appropriate for direct propagation from this PN label without narrower context or gene-level evidence.
    - [group] Ubiquitin Proteasome System|Ubiquitin and UBL proteins|ubiquitin-like modifier
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a ubiquitin-like modifier protein bucket. The modifier identity is taxonomy context, not a safe GO annotation target for the modifier genes as a group.
    - [class] Ubiquitin Proteasome System|Ubiquitin and UBL proteins
        status=context_only scope=too_broad_to_propagate GO=[GO:0019787 ubiquitin-like protein transferase activity]
        rationale: This class groups ubiquitin, UBL modifiers, UBX/UBL-domain proteins, and UBL-containing enzymes. The branch is UPS-relevant but too mixed to propagate as a single GO annotation.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (4)
- GO:0006515 protein quality control for misfolded or incompletely synthesized proteins | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Translation|Cytosolic translation|Ribosome-associated QC
- GO:0071569 protein ufmylation | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Translation|Cytosolic translation|Ribosome-associated QC|UFMylation
- GO:0061709 reticulophagy | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Autophagy-Lysosome Pathway|Autophagy substrate selection|Marking substrates for selective autophagy|ERphagy
- GO:0061709 reticulophagy | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Autophagy-Lysosome Pathway|Autophagy substrate selection|Marking substrates for selective autophagy|ERphagy|UFMylation of ER proteins

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
