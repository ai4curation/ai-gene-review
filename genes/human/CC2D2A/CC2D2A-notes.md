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


## 2026-10-04: PR 4209 external-source provenance clarification

The second required review response changes only the three PMID:22179047 NAS reasons. Each now identifies the selected external source inline as an author-uploaded copy of Chih et al., DOI 10.1038/ncb2410. Bare figure numbers are removed from those reasons, and the text explicitly separates the external construct, localization, purification and Sept2-control observations from the abstract-only canonical cache. The previously recorded [author-uploaded reproduction](https://www.researchgate.net/publication/51897621_A_ciliopathy_complex_at_the_transition_zone_protects_the_cilia_as_a_privileged_membrane_domain) and selected reading ranges remain the provenance. Earlier notes refer to caption labels in that reproduction; those historical labels are not asserted to be independently verified version-of-record figure numbering.

All 19 source assertions, actions, four products, nine references, core, eight verbatim anchors and their aggregate quote budgets are unchanged. No new source text, quotation or biological conclusion is added. The anchors verify their exact cached wording, not the separately described external details. The normal full-text-unavailable flag continues to describe the canonical cache. Prior notes and histories remain verbatim; a new standard EDIT record is for ROOT to create only after the focused peer and acceptance. The optional requests for longer quotations and broader Reactome rationale changes are outside this narrow required provenance correction; no quote-limit exception or new localization evidence is inferred.


## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

No ProtNLM2 output was opened or used. The ProtNLM2 benchmark target is the canonical product, not a fragment: Q9P2K1 (C2D2A_HUMAN, Swiss-Prot reviewed, 1,620 aa, sequence version 3) is the entry for this folder. Its displayed isoform 1 (Q9P2K1-4) corresponds to MANE Select ENST00000424120.6 / NP_001365544.1. The isoform, fragment and gene-model questions do not arise.

**Domain architecture (UniProt/InterPro).** The protein has an N-terminal disordered region (1-241, MobiDB-lite), coiled coils (439-493, 532-582), CC2D2AN-C2 (PF15625), a CEPT76/DRC7 peptidase-like TGL fold (PF24656), CEP76_C (PF24652), DUF5523, and a C2 domain (1025-1203, PROSITE PS50004). Zhang & Aravind found the TGL domain catalytically inactive in every member of the CC2D2A/MKS6 clade [PMID:22983010 "all representatives of the CC2D2A/MKS6 clade are inactive"]. No peptidase, transglutaminase or calcium-binding MF is asserted.

**Phylogenetic placement.** PANTHER puts PTHR20837 human and mouse CC2D2A in SF7, fly Cc2d2a (A1ZAV1) and worm MKS-6 (Q21303) in SF0, and CC2D2B in SF2 (interpro/panther/PTHR20837 entries and the member index). The PAINT IBD node PTN000464650 is at taxon Eukaryota and carries ciliary transition zone, protein localization to ciliary transition zone and non-motile cilium assembly. Human CC2D2A descends from it; CC2D2B does not get the terms. This fits [PMID:21725307 "Tmem67 and Cc2d2a orthologs are found in all Tectonic-possessing eukaryotes"]. Mouse Cc2d2a, the donor for all ISS and Compara rows, is in the same subfamily (SF7), so those transfers are phylogenetically justified.

**New primary literature used (now cached).**
- PMID:21725307 (Garcia-Gonzalo 2011, full text): Tctn1 interacts with Cc2d2a by TAP-MS and co-IP; Cc2d2a localizes to the TZ, including in Tctn1-/- MEFs; Cc2d2a-/- MEFs lose ciliary AC3, Pkd2 and Arl13b, and Smo even more strongly; ciliogenesis defects are tissue-specific ("Cc2d2a−/− MEFs can generate cilia").
- PMID:26485645 (Bachmann-Gagescu 2015, full text): human CC2D2A in hTERT-RPE1 cells is at the "ciliary base (basal body, accessory centriole) and also (partly) to the ciliary transition zone"; it interacts with NINL (Y2H, co-IP).
- PMID:18950740 (Gorden 2008, abstract): recombinant CC2D2A localizes to the basal body with CEP290 and interacts with CEP290 (Y2H, GST pull-down).
- PMID:21816947, PMID:29281629 (zebrafish): Cc2d2a sits at the connecting cilium/TZ, cilia persist, and opsin-carrier vesicles fail to fuse. Used as context only; no zebrafish-only term was transferred, and the fusion step is not attributed to CC2D2A.
- PMID:21422230 (C. elegans MKS-6 TZ localization, MKS/MKSR module), a PAINT seed.

**Changes to the review.**
- Three Reactome cytosol TAS rows changed from KEEP_AS_NON_CORE to MARK_AS_OVER_ANNOTATED. No experiment places CC2D2A in a soluble cytosolic pool, and the label is a Reactome compartment convention. They are not removed, because the protein is broadly cytoplasmic.
- Cytoplasm (SubCell IEA) stays KEEP_AS_NON_CORE. A MODIFY is impossible because GO puts the TZ, basal body and SDA under cilium, not cytoplasm (checked with runoak ancestors).
- Smoothened signaling (IEA, ISS) stays KEEP_AS_NON_CORE. The contribution is ciliary gating of Smo [PMID:21725307], with no transduction role.
- TZ, MKS complex, cilium assembly, protein localization to TZ and non-motile cilium assembly are still ACCEPTED. Reasons and support were rewritten around the phylogeny and the new mouse/human evidence. Cilium assembly passes the participation test: the protein is on the subdistal appendages it is needed to build, and transgene rescue restores the axoneme.
- NEW: ciliary basal body (GO:0036064, IDA, PMID:26485645 with human RPE1 data) and centriolar subdistal appendage (GO:0120103, ISS from mouse IMCD3 and macaque retina immunogold, PMID:24947469). These are location terms only. No NEW process or MF was added, and in particular no "vesicle fusion", "protein localization to cilium" or "regulation of smoothened signaling". The PAINT curators propagated only the three terms above from the mouse/worm donors, and that is treated as deliberate.
- Core functions are split in two: (1) MKS/TZ module subunit and (2) structural ciliogenesis at the mother centriole. GO:0120103 cannot be a core `locations` value because it is a protein-containing complex and not in the location enum, so it is kept as a NEW row only.
- Description rewritten as a project-independent summary. The falcon report is added as a LOW-relevance source-finding reference; it is not cited as support.

**Relative for next review.** Mouse Cc2d2a (Q8CFW7, MGI:1924487) is the same-subfamily (SF7) ortholog, a PAINT seed for PTN000464650, and the best-characterised relative (null mouse, rescue, immuno-EM, Tectonic complex). It has no review in the repo. C. elegans mks-6 (SF0) has a COMPLETE review at genes/worm/mks-6/.

**PANTHER family review (interpro/panther/PTHR20837/PTHR20837-review.yaml).** It lists only SF7 (horse and human) and refers to CC2D2B as "in the member inventory". There is no conflict over subfamily placement: SF7 is correct for Q9P2K1. The family review does omit that invertebrate CC2D2A orthologs (fly, worm) are split into SF0, separate from the CC2D2B subfamily SF2, and that the IBD node lies above both CC2D2A subfamilies.

**Modules.** modules/ciliary_transition_zone.yaml, modules/primary_cilium_life_cycle.yaml, and modules/dmel_ciliary_transition_zone.yaml for the fly ortholog.
