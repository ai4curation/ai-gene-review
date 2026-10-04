# CC2D2A: paired human–horse review notes

## Biological evidence

Mouse loss-of-function, rescue and microscopy connect CC2D2A to mother-centriole appendages, ciliary assembly and transition-zone elaboration. Loss disrupts cilia-dependent Shh signaling and embryonic laterality/neural development. These developmental roles arise through ciliary organization.

- [PMID:24947469: Ciliopathy-associated gene Cc2d2a promotes assembly of subdistal appendages on the mother centriole during cilia biogenesis.](https://pubmed.ncbi.nlm.nih.gov/24947469/) — full text cached.
- [PMID:22179047: A ciliopathy complex at the transition zone protects the cilia as a privileged membrane domain.](https://pubmed.ncbi.nlm.nih.gov/22179047/) — abstract cached; full-text availability must be checked separately.

## Exact horse model

Horse N-terminal deletions align within the human predicted disordered1–241region, while the long coiled-coil/C2 architecture is retained. This supports broad ciliary/developmental transfer. Renal tubule ciliation defects alone do not resolve the more specific kidney-development claim, which remains UNC.

The reproducible alignment, source paths and hashes are in [the paired comparison](../../HORSE/CC2D2A/CC2D2A-bioinformatics/RESULTS.md). Current UniProt sequences have not been proven identical to the original ProtNLM input sequences. Sequence anomalies are therefore recorded as model/transfer limitations, not as proven wrong-input pipeline errors.

## Evidence gaps

Confirm the horse transcript model and distinguish renal morphogenesis from renal cilia/homeostasis. A calcium-binding molecular activity should not be invented solely from the C2 domain label.

## Review scope and checks

Every seeded annotation receives a current assessment. UNDECIDED marks unresolved source-specific or biological evidence; these are initial reviews rather than a claim that every original experimental assay has been independently reproduced or verified. The human Edison report is retained as a research synthesis and source-finding aid; decisive YAML excerpts cite primary publications, source records or reproducible analysis. The validator advisory to cite the deep-research file is deliberately not satisfied by citing AI prose as biological proof.


## 2026-10-04: ClinGen cohort reassessment

This reassessment preserves the initial paired human–horse review from [PR #2990](https://github.com/ai4curation/ai-gene-review/pull/2990), its CREATE history, the horse comparison and both Falcon research files. The existing human source is Q9P2K1 (HGNC:29253; NCBI Gene:57545), 1,620 amino acids, with four recorded alternative products. The displayed UniProt product is Q9P2K1-4; its displayed name is not used to renumber the source isoforms. The frozen ClinGen association remains autosomal recessive ciliopathy, Definitive, SOP9. No disease classification or horse prediction was revised.

All 19 existing source assertions were reassessed with their original identifiers, evidence types, donors and qualifiers preserved. The two Smoothened/Hedgehog assertions become non-core: mouse neural-tube patterning is consistent with impaired ciliary signaling, while the direct structural work is ciliary-base organization. The remaining 13 accepted assertions describe conserved ciliary localization, complex membership, assembly and protein localization; four broad compartment assertions remain non-core. No annotation was removed and none was added.

For [PMID:24947469](https://www.nature.com/articles/ncomms5207), the complete nonduplicated cached Results, Discussion and Methods were read. The knockout eliminates shared exons and is validated at RNA/protein level. Mouse fibroblast axoneme formation is rescued by a mouse transgene; mother centrioles and selected proximal markers remain. The paper reports an escaping fraction of knockout cells, so cilia loss is not absolute. Endogenous immuno-EM in mouse IMCD3 cells and macaque retina places CC2D2A at subdistal appendages. These structures are adjacent to, and are not synonyms for, the transition zone. RAB8A becomes diffuse despite comparable total protein. The proposed direct ODF2 contact and microtubule-binding surface are hypotheses, not established binding activities. No figure pixels or supplements were independently reanalyzed.

For [PMID:22179047](https://www.nature.com/articles/ncb2410), the complete normal abstract explicitly supports the mutually dependent transition-zone localization of CC2D2A, B9D1 and TMEM231. Official article and PDF body access attempts ended at an authorization redirect. The original NAS assertions are retained with curator deference and the independent conserved biological context; no new species/construct/control claim is inferred from the title or abstract. Its cache remains abstract-only. Mouse and macaque evidence is not mislabeled as direct human experimentation.

The three Reactome summaries were read individually. RAB3IP exchange activity, CEP164-mediated recruitment and the larger transition-zone event do not assign those molecular activities to every component with a cytosolic location projection. PAINT rows retain their ancestral assertions without reconstructing an uninspected IBD or judging support by donor count.

The single core describes physical organization and conserved assembly/localization processes. No specific molecular-function term is invented where the direct molecular mechanism remains unresolved. In particular, no calcium-binding, transglutaminase, motor, GEF or general microtubule-polymerase activity is asserted. Existing pathway and compartment terms are sufficient; no new process term or redundant parent/child proposal was added. Short cache-verbatim anchors replace the repeated long quotations in the initial review. Source-specific access limits and remaining mechanistic questions are recorded separately from acceptance of well-supported broad biology.

All 19 annotations have decisions (13 ACCEPT and six KEEP_AS_NON_CORE). The repository status remains DRAFT because validation advises referencing the available Falcon report. That report is preserved as a source-finding aid; AI-generated prose is not substituted for the primary biological evidence. This advisory is disclosed rather than satisfied by an unsupported citation. Normal checks and the distinct scientific review are recorded in the session provenance.


## 2026-10-04: PR 4209 evidence-anchor follow-up

The required review response restores bounded verbatim evidence at the five named annotation positions: RPGR overlap, escaping knockout fibroblasts, the RAB8A abundance control, and the two transition-zone NAS assertions. The core microscopy anchor now includes the SDA location. These excerpts identify specific findings; the adjacent reasons and source contexts retain the species, anatomical and perturbation limits. Their substring checks do not independently validate the complete biological interpretation. All 19 machine assertions and actions, four products, nine reference identities and core terms remain unchanged.

The earlier access limitation is partly resolved by an [author-uploaded primary reproduction](https://www.researchgate.net/publication/51897621_A_ciliopathy_complex_at_the_transition_zone_protects_the_cilia_as_a_privileged_membrane_domain) of Chih and colleagues, DOI 10.1038/ncb2410. Selected Results, Fig. 2/Fig. 4 captions and Methods identify mouse CC2D2A NM_172274 and IMCD3 experiments. They distinguish reciprocal complex-localization effects from Sept2 dependence. No direct CC2D2A–Sept2 interaction is established. The normal PMID:22179047 cache remains abstract-only; external access does not change its bytes or flag. Figures, supplements and the complete article were not independently inspected. The new provenance narrows the earlier access question, which is removed from the biological questions.

The core description is shortened to biological organization and the unresolved interaction architecture. No molecular-function term is added. The existing reasons preserve curator-supported cytosolic projections without assigning the catalytic activities of other Reactome participants. No new localization experiment is inferred.

The previous EDIT history's sections list includes suggested_experiments although no such block was authored. That existing record is preserved verbatim; this follow-up records the correction and will use accurate section names in its own standard history after acceptance. The existing notes above remain a historical journal, including the earlier access state. Canonical caches, Falcon files, old histories, horse files and frozen inventories are unchanged.
