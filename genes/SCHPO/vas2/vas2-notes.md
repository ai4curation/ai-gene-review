# vas2 evidence notes

Vas2 (Aps1) is the sigma subunit of the heterotetrameric AP-1 clathrin adaptor complex. It associates with the gamma subunit Apl4 and contributes to assembly and membrane recruitment of AP-1 at the Golgi and endosomal system. The complex sorts membrane-protein cargo into intracellular transport carriers and supports exit of cargo such as the v-SNARE Syb1 from endosomes.

## Identity and prediction provenance

PomBase primary symbol vas2, locus SPAP27G11.06c, current UniProt Q9P7N2. The supplied pre-release post-processed-2026_02_28k.xml is the source of the reviewed claims; its placeholder sequence, taxonomy and dates are not biological metadata. The current UniProt sequence is not established as the model input. Current API availability and published-list inclusion are separate properties; all biological judgments here concern the preserved original claims.

## Primary evidence inspected

- [PMID:16823372 ORFeome cloning and global analysis of protein localization in the fission yeast Schizosaccharomyces pombe.] "Next, we determined the localization of 4,431 proteins, corresponding to approximately 90% of the fission yeast proteome, by tagging each ORF with the yellow fluorescent protein."
- [PMID:19624755 Deletion mutants of AP-1 adaptin subunits display distinct phenotypes in fission yeast.] "In pull-down assay, Apm1 binds Apl2 even in the absence of Aps1 and Apl4, and Apl4 binds Aps1 even in the absence of Apm1 and Apl2. Consistently, the deletion of any subunit generally caused the disassociation of the heterotetrameric complex from endosomes, although some subunits weakly localized to endosomes. In addition, the deletion of individual subunits caused similar endosomal accumulation of v-SNARE synaptobrevin Syb1. Altogether, results suggest that the four subunits are all essential for the heterotetrameric complex formation and for the AP-1 function in exit transport from endosomes."

## Evidence limits and adjudication

- GO:0005634 (KEEP_AS_NON_CORE): Retain the reported nuclear signal from the tagged-protein screen as an ancillary localization. It does not establish a nuclear AP-1 cargo-sorting mechanism and is not the principal functional location supported by endosomal trafficking experiments.
- GO:0010496 (REMOVE): GO:0010496 means movement between cells, as verified in QuickGO. The experimentally established Vas2/AP-1 pathway sorts cargo between compartments inside a cell. This ARBA assertion conflates intercellular and intracellular transport and lacks an independent intercellular mechanism.
- GO:0030276 (KEEP_AS_NON_CORE): Retain the curator-mediated orthology transfer for clathrin association in the AP-1 context. The decisive target evidence establishes adaptor-complex assembly; it does not demonstrate that isolated sigma subunit is the principal direct clathrin-binding interface.

Primary reports are interpreted at the species, assay and subunit level. Abstract-only experimental annotations are not rejected because a title foregrounds another subunit. PAINT asserts inheritance from a curated ancestral node; donor count and target self-inclusion are not objections. ARBA overlap is recorded only as provenance, never as biological validation. CNN and LSP reflect established biological knowledge, without asserting training-data membership.

The full original function paragraph and all atomic claims are assessed in [vas2-protnlm-function-review.md](vas2-protnlm-function-review.md).

## Provider report appraisal

The late Falcon report was inspected after the wrapper timeout. It misses the target Aps1 pull-down and deletion experiments in PMID:19624755, so its statement that direct Vas2-binding evidence was not found is incomplete. Target Apl4-Aps1 association and AP-1 exit-transport evidence are prioritized over pathway-only Apm1 observations.

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 files were not opened or used for this pass.

### Identity
- The benchmark accession Q9P7N2 is the canonical, reviewed Swiss-Prot product of vas2/aps1 (SPAP27G11.06c), AP1S1_SCHPO, 162 aa. It is not an isoform, a fragment or an alternative gene model. InterPro shows the PTHR11753 match covering residues 3-145, and the AP-1 sigma signature (IPR044733) and Clat_adaptor_s (PF01217) are both present.

### Evolutionary grounding
- `vas2-bioinformatics/panther_subfamily_rereview.py` queries the PANTHER 19 geneinfo service live. Its results are in RESULTS-rereview.md and panther_subfamily_rereview.tsv. Q9P7N2 is in PTHR11753:SF5 "AP COMPLEX SUBUNIT SIGMA", the same subfamily as S. cerevisiae APS1 (P35181). The human AP-1 sigma paralogs are in separate subfamilies: AP1S1 in SF14, AP1S2 in SF45 and AP1S3 in SF18. AP-2, AP-3 and AP-4 sigma chains are in SF6, SF2/SF12 and SF57. Subfamily-specific properties of the vertebrate AP-1 sigma chains are therefore not transferred. The mammalian gamma/sigma1 dileucine-binding result (PMID:17360967) is cited only as a mechanism shared by AP-1 sigma chains.
- PAINT: the only PTHR11753 node in the cached PAINT table is PTN000204281, the family root. It carries vesicle-mediated transport and intracellular membrane-bounded organelle. The curators did not propagate AP-1 complex membership or clathrin binding from this node. That makes sense at a node that spans AP-1 to AP-4, and I treat the omission as deliberate.
- Family review `interpro/panther/PTHR11753/PTHR11753-review.yaml` uses vas2 as its reference protein. It assigns no subfamily-level claim, and the GO:0030121 scope is UNRESOLVED. The SF5 placement found here does not disagree with it.

### Literature
- Target-specific evidence is still only Ma et al. 2009 (PMID:19624755; abstract only in the cache): Apl4 binds Aps1 independently of Apm1 and Apl2, every subunit is needed for heterotetramer formation and endosomal association, and Syb1 accumulates in endosomes in each deletion. The localization rows come from the ORFeome YFP screen (PMID:16823372). The falcon report adds the VPA-sensitivity context, based on Zhang 2013 (not cached), and Apm1-only phenotypes from Kita 2004 and Jaiseng 2012. I did not transfer those to Vas2.
- QuickGO for yeast APS1 (P35181), checked 2026-10-21, has no GO:0030276 clathrin binding annotation. Its annotations are AP-1 complex (IDA/EXP/NAS, PMID:10564262), protein-binding IPIs to other AP-1 subunits, an IMP process annotation, and electronic and propagated rows. The PomBase ISO clathrin binding row (with SGD:S000004160) therefore has no visible donor today.

### Changes from the previous review
- nucleus (HDA, IEA): KEEP_AS_NON_CORE changed to MARK_AS_OVER_ANNOTATED. The only source is a high-throughput fusion screen, and a small sigma adaptin fused to YFP can diffuse into the nucleus. No AP-1 nuclear role is known.
- cytoplasm (EXP, IEA): ACCEPT changed to MODIFY, with cytosol as the replacement. The term is correct but general, and the gene already carries cytosol, Golgi and endosome.
- cytosol (HDA): ACCEPT changed to KEEP_AS_NON_CORE. This is the soluble pool, not where the complex acts.
- protein transport (IEA): ACCEPT changed to MODIFY, with GO:0099638 as the replacement, since GO:0099638 is_a GO:0015031.
- vesicle-mediated transport (IBA, IEA): ACCEPT changed to MODIFY, with GO:0042147 and GO:0099638 as replacements. Both are descendants (verified with OLS hierarchicalAncestors). The PAINT node placement is sound, and the change only reflects the more specific IDA evidence on the target.
- clathrin binding (ISO): KEEP_AS_NON_CORE changed to MARK_AS_OVER_ANNOTATED. The donor term is no longer present, clathrin binding is a complex-level property (the beta-adaptin clathrin box), and PAINT does not propagate it.
- Unchanged: AP-1 adaptor complex (ACCEPT x3), endosome and Golgi (ACCEPT), clathrin-coated vesicle membrane (ACCEPT), clathrin-cargo adaptor activity (ACCEPT; contributes_to is the precise form), the endosome-to-Golgi and endosome-to-plasma-membrane IDA processes (ACCEPT, deferring to the full-text curation), and intercellular transport (REMOVE; ARBA rule, a between-cells term that does not apply to a unicellular fungus).
- Description and core function rewritten without YAML anchors. clathrin-coated vesicle membrane was added to the core locations. Suggested questions and experiments were added.

### Relative to review next
- S. cerevisiae APS1 (P35181, SGD:S000004160) is an ortholog in the same PANTHER subfamily (SF5), with experimental AP-1 membership (PMID:10564262). The repo has no review of it (genes/yeast/ has no APS1). The vertebrate AP1S1 review (genes/human/AP1S1) is in a different subfamily (SF14).

### Modules
- No module includes vas2. The nearest is modules/dmel_clathrin_adaptor_coats.yaml (Drosophila AP-1/AP-2/AP-3 coats, a family-level analogue), with modules/ldl_receptor_mediated_endocytosis.yaml and modules/synaptic_vesicle_endocytosis.yaml as AP-2 context only.
