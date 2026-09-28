# APOL1 review notes

## Scope and source access — 2026-09-28

The normal gene seed contains 22 GO assertions and three alternative products. The original identifiers, evidence, references, qualifiers and supporting entities are preserved. The original eight PMID records and two Reactome records are now available through the normal fetch workflow. Existing cache versions were preserved when recovered copies differed. These are review notes, not an automated research report.

The installed Falcon research client with its configured fallback failed without producing a report. Manual reading covers all original annotation objects; UniProt function, interaction and localization sections; the complete cached abstracts for PMIDs 12621437, 16020735, 17154273, 17192540, 22516433 and 9325276; the main text of PMID 22582013; and the abstract plus target-record search of PMID 25416956. The latter search did not expose the APOL1–CDC23 pair. Both normal Reactome summaries were read completely. Unread supplements and exact pair records remain explicit evidence limits.

## Serum defense and membrane activity

[PMID:12621437, Apolipoprotein L-I is the trypanosome lytic factor of human serum](https://pubmed.ncbi.nlm.nih.gov/12621437/) describes APOL1-dependent serum killing and interaction with trypanosome SRA. The cached abstract supports an actual antagonist interaction; it does not justify a particular enzymatic or adaptor activity for APOL1. The observed interaction is retained outside the core synthesis under the supplied action criteria. The local generic-binding policy advisory will be documented rather than treated as evidence that the interaction is false.

[PMID:17192540, Human Trypanosoma evansi infection linked to a lack of apolipoprotein L-I](https://pubmed.ncbi.nlm.nih.gov/17192540/) provides human loss-of-function and rescue evidence: “Trypanolytic activity was restored by the addition of recombinant APOL1.” Its official PubMed identifier, title, DOI and abstract were checked independently. This supports an extracellular innate-defense effector. APOL1 membrane activity supplies the mechanistic participation evidence; necessity alone is not used to invent a process annotation.

The two original antibacterial assertions cite these trypanosome experiments. The official definitions distinguish [GO:0140367 antibacterial innate immune response](https://amigo.geneontology.org/amigo/term/GO:0140367) from [GO:0042832 defense response to protozoan](https://amigo.geneontology.org/amigo/term/GO:0042832). Both rows are refined to the latter, preserving their original source and evidence. This concerns the organisms actually studied, without asserting that APOL1 has no other pathogen-related effects.

## Ion selectivity remains a source-comparison question

[PMID:16020735, Apolipoprotein L-I promotes trypanosome lysis by forming pores in lysosomal membranes](https://pubmed.ncbi.nlm.nih.gov/16020735/) reports anion conductance, chloride influx and parasite lysosomal swelling. Its normal cache is abstract-only. These are actual source statements, not an annotation invented from the title. Membrane interaction and targeting are supported independently of the unresolved selectivity question.

The later [PMID:25730870 primary record](https://pubmed.ncbi.nlm.nih.gov/25730870/) reports pH-dependent cation conductance by full-length recombinant APOL1. The official abstract and Figures 1–3 captions were inspected, as was the indexed primary introduction contrasting earlier truncated material with full-length protein. Full Methods have not yet been read. One normal local fetch failed without a cache output; exact normal source recovery is pending. The historical chloride rows remain UNDECIDED while construct and pH differences are evaluated. No assumption is made that a later result automatically invalidates an earlier assay.

The official [GO:0005261 monoatomic cation channel activity](https://amigo.geneontology.org/amigo/term/GO:0005261) definition was inspected as a possible additional molecular function. It is not yet asserted in this draft. There is no APOL1/O14791 match in the current local GO-CAM index. A final channel-function synthesis awaits the additional primary record and independent scientific consultation.

## Particle carriage, mapped processes and unresolved records

[PMID:9325276](https://pubmed.ncbi.nlm.nih.gov/9325276/) directly identifies APOL1 in human immunoisolated HDL; the official PubMed record was checked. [PMID:17154273](https://pubmed.ncbi.nlm.nih.gov/17154273/) explicitly identifies apoL-I among VLDL proteins. The proteomic forms reported there are not automatically equivalent to UniProt sequence isoforms. HDL membership is central to the circulating defense pool; VLDL membership is retained as a secondary context.

The two InterPro process mappings, lipid transport and lipoprotein metabolism, remain unresolved. Association with a carrier and binding to membrane lipid do not by themselves demonstrate movement of lipid cargo or an APOL1-performed metabolic step. PAINT lipid-binding and membrane assertions are independently supported by APOL1 experiments. Their actual ancestral node PTN001422588 is preserved with unresolved detailed tracing; target self-inclusion is legitimate, and donor count is not a confidence measure.

[Reactome R-HSA-2168889](https://reactome.org/content/detail/R-HSA-2168889) explicitly includes APOL1 in human-serum TLF-1. HPR performs hemoglobin binding in this event. [R-HSA-8952289](https://reactome.org/content/detail/R-HSA-8952289) describes FAM20C substrates, but its summary does not expose an APOL1-specific ER-lumen entity. That source-specific compartment assertion remains uncertain; secretory passage is not excluded.

The FAM20C interaction in [PMID:22582013](https://pubmed.ncbi.nlm.nih.gov/22582013/), the CDC23 screen pair in [PMID:25416956](https://pubmed.ncbi.nlm.nih.gov/25416956/), and the microvesicle detection in [PMID:22516433](https://pubmed.ncbi.nlm.nih.gov/22516433/) await their APOL1-specific data. A kinase-centered title does not establish wrong-gene attribution. An unread proteomics table does not establish contamination.

The draft has 22 individually considered original assertions, no PENDING rows and no NEW rows. Source closure, final core synthesis, independent consultation, validation and publication remain separate tasks.


## Final source closure and channel synthesis — 2026-09-28

The earlier draft/pending statements above are historical. Source40 recovered PMID:25730870 through the normal publication fetcher; its unchanged abstract-only cache is now canonical. Root verified its PubMed identity and read targeted indexed [primary Results and Methods](https://pmc.ncbi.nlm.nih.gov/articles/PMC4352821/): the reagent is N-terminally tagged mature human O14791, residues 28–398, produced in bacteria. Bilayer reversal measurements distinguish cations from chloride. This identifies the assayed protein independently of the expression host. Direct PMC opening returned a browser check; indexed passages supplied the bounded body access. Supplementary Methods and the original 2005 construct protocol remain unread.

The final draft adds one IDA molecular function, [GO:0005261 monoatomic cation channel activity](https://amigo.geneontology.org/amigo/term/GO:0005261). Its definition requires passive cation passage through a membrane pore, matching the direct assay. The original chloride MF is a sibling, not an ancestor or descendant. No NEW biological process is added. The core uses the protozoan-defense refinement already proposed for two original rows: APOL1 performs membrane disruption, while human deficiency/rescue provides complementary physiological evidence. A missing GO-CAM match is not treated as evidence of a gap.

All 22 original assertions and three alternative products remain intact: 10 ACCEPT, eight UNDECIDED, two KEEP_AS_NON_CORE and two MODIFY, plus the single NEW MF. Source-specific chloride uncertainty is retained despite the independently supported cation function. The two unread interaction records remain uncertain solely because their target-level data are uninspected. The real SRA antagonist contact remains non-core under the user-supplied ActionEnum; this deliberately takes precedence over the skill preference to REMOVE an uninformative generic-binding term. Informativeness does not supply grounds for inventing a more specific APOL1 activity.
