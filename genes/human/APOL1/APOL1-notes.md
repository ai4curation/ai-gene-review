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


## Reviewer follow-up: evidence scope and biological context

This entry records the current assessment and supersedes the pending-draft statements in the initial journal sections. The original 22 assertions, the existing cation-channel NEW assertion, all three product definitions and every action remain unchanged: ten ACCEPT, eight UNDECIDED, two KEEP_AS_NON_CORE, two MODIFY and one NEW. The previously published history remains an immutable record, including its original wording; this follow-up receives a separate history record.

### Positive binding evidence and source provenance

The [PMID:12621437](https://pubmed.ncbi.nlm.nih.gov/12621437/) SRA interaction remains positive evidence for a real antagonist association. The explicit user instructions define REMOVE as unlikely correct on combined evidence and permit KEEP_AS_NON_CORE. Those instructions take precedence over the skill's generic-binding removal default. Genericity alone does not establish incorrectness, and no specific APOL1 molecular activity is invented merely from antagonist contact. This is a deliberate policy disagreement, not an unaddressed annotation.

For [PMID:22582013](https://pmc.ncbi.nlm.nih.gov/articles/PMC3754843/), the main text establishes FAM20C as a secretory protein kinase. The APOL1-specific interaction experiment remains unadjudicated; the primary supplementary-PDF link returned a download interstitial. The unchanged UniProt O14791 record separately reports APOL1 phosphorylation by FAM20C with PMID:26091039 and two IntAct interaction experiments. Targeted reading of the later paper's main Results and Methods describes the secreted phosphoproteome and kinase assays; its APOL1-specific target data were not exposed in the extracted body. This later curated PTM evidence corroborates a relationship but does not demonstrate inspection of the original 2012 IPI experiment. No false-interaction or wrong-gene conclusion is made. The CDC23 pair and microvesicle-specific APOL1 table retain their separate access limits.

### Electronic process mappings

The current official [lipid transport definition](https://amigo.geneontology.org/amigo/term/GO:0006869) includes directed lipid movement through transporters or pores. The APOL1 channel assays resolve ion passage, and the isolation studies establish particle membership; neither settles whether APOL1 additionally moves lipid cargo. UniProt proposes lipid exchange and reverse cholesterol transport with qualified wording. That possibility is acknowledged rather than contradicted.

The current [lipoprotein metabolic process definition and parent](https://amigo.geneontology.org/amigo/term/GO:0042157) concern metabolism of proteins with covalently attached lipid, under protein metabolic process. Membership in HDL or VLDL does not by itself settle this assertion. The current primary InterPro entry/API could not be read, so the IPR008405 mapping rationale remains unresolved. The family name is not evidence that an erroneous mapping was made. UNDECIDED in the explicit instructions covers an unclear assertion generally; inaccessible publications are a mandatory instance, not its exclusive meaning. These reasons identify what remains uncertain and do not assert that either process is impossible.

### Human disease and tissue context

The unchanged UniProt record reports expression in pancreas, lung, prostate, liver, placenta and spleen, and susceptibility to focal segmental glomerulosclerosis. The [original 2010 primary PubMed record](https://pubmed.ncbi.nlm.nih.gov/20647424/) was independently read at complete-abstract and Figure 1/3-caption scope: it reports APOL1 risk variants associated with FSGS and hypertension-attributed end-stage kidney disease and identifies G1/G2 in the captions. This external reading supports the standalone disease summary; no risk magnitude, universal penetrance, clinical advice or new renal GO assertion is introduced. The complete clinical Methods were not read, and no normal publication cache was created or substituted for this external scope. The new question separates cell-intrinsic renal injury from the circulating defense role.

### Core coverage and source-specific attachments

The first protozoan-defense refinement now quotes the original native/recombinant APOL1 add-back lysis result rather than background about sleeping sickness. Both refinements preserve the independently supported existing innate immune response term. The cation-channel core distinguishes acidic-pH lipid association from subsequent neutral-pH channel opening; this phase separation is explicit in PMID:25730870. Circulating HDL-associated APOL1 must not be described as an active channel on the particle. The exact human HDL isolation statement is attached to the core description for this delivery context, while its machine-readable active location remains membrane. The existing lipid-binding function is represented as the prerequisite phase of the same pore mechanism rather than a second independent activity; no HDL-to-channel activity edge or new lipid-cargo transport function is inferred.

No additional biological-process assertion is added. The existing protozoan-defense and innate-immune annotations capture the supported physiological synthesis; adding a separate killing-process term is not required to resolve this follow-up and would need its own hierarchy/comparator assessment. Historical chloride MF/transport remain UNDECIDED until the original 2005 constructs and conditions are directly compared with the later human mature-protein experiments. Reference assessments now identify each source's actual result and read boundary, replacing repeated generic text. Source caches and original annotation fields are unchanged.

### Final checks

The full gene validator, HTML renderer and new history validator passed. The sole generic-binding advisory is the explicit user-policy disagreement explained above. The preservation check confirmed all 22 original source assertions, the prior NEW assertion, all 23 actions and three products unchanged, with 14 published dependencies preserved. All nine PMID titles, 24 literal support instances and 15 availability flags passed independent mechanical checks. Final independent scientific consultation is recorded separately against the resulting files.
