# ARHGEF9 review notes

ARHGEF9 (collybistin; human UniProt O43307) has two distinguishable activities: a Dbl-family exchange-factor activity associated with cellular CDC42 activation, and membrane recruitment of the inhibitory-synapse scaffold gephyrin. Recruitment is not simply a downstream readout of CDC42 activation. Rodent experiments separate these activities using exchange-deficient and lipid-binding mutants. Three current UniProt products are retained without assigning historical reagents to a specific present-day accession.

## Human exchange-factor evidence

The original [hPEM-2 study, PMID:10559246](https://pubmed.ncbi.nlm.nih.gov/10559246/) identifies the human KIAA0424 clone AB007884. The original Methods and targeted Results were read through an author-uploaded copy. HA-hPEM-2 expression in COS7 cells was assessed using GTPase effector pull-downs; NIH3T3 cells supplied a morphology assay. CDC42 activation was observed under those conditions, without corresponding Rac or RhoA activation. Purified GTPases calibrated the binding probes: the study was not a purified hPEM-2 nucleotide-exchange kinetic experiment. Its historical approximately 70-kDa construct has not been assigned to one of the current O43307 isoform identifiers.

This source, the conserved DH domain and the target-specific CDC42 GEF summary in [Reactome R-HSA-9013159](https://reactome.org/content/detail/R-HSA-9013159) support retaining the broad existing GEF annotations. The Reactome summary explicitly distinguishes established GEFs, candidate GEFs and negative observations; an interaction screen cited there is not treated as an exchange assay. [R-HSA-9012999](https://reactome.org/content/detail/R-HSA-9012999) describes the GDP/GTP cycle. The already-present regulation process is associated with the exchange activity; no additional biological process is proposed.

## Membrane recruitment and assay species

For [PMID:15215304](https://pubmed.ncbi.nlm.nih.gov/15215304/), published PDF pages 5816–5818 supplied cloning Methods and initial splice-form Results. Human and rat cDNA cloning are separately described. The functional myc-CB2/CB3 constructs explicitly derive from postnatal rat brain, and mouse cortical neurons are a distinct assay host. The human splice-form and disease observations do not make every functional assay a human-protein experiment. The remaining Results and supplements were not completely read.

For [PMID:20345913](https://pubmed.ncbi.nlm.nih.gov/20345913/), Methods and target Results/Figure captions were read. The exchange-deficient NE232–233AA construct retains gephyrin recruitment, whereas the PH-domain RR303–304NN lipid-binding mutant retains association with gephyrin but fails to recruit it to the membrane. Forebrain conditional Cdc42 loss provides a separate mouse genetic test. Cb construct provenance refers back to prior work without an explicit accession in the inspected Methods, so a host species is not substituted for reagent identity. The complete Discussion and supplemental experiments were not audited.

For [PMID:25082542](https://pubmed.ncbi.nlm.nih.gov/25082542/), indexed original Results and protein-purification Methods describe conformational control of collybistin. Rat recombinant proteins are explicit in the structural work. Targeted Results and Figures 3–5 link neuroligin-2-dependent activation, phosphoinositide interactions and gephyrin membrane recruitment. This does not independently resolve the species of every tagged construct used in each cellular panel. A complete supplementary audit is not claimed.

For [PMID:25678704](https://pubmed.ncbi.nlm.nih.gov/25678704/), the full abstract and all seven main Figure captions were read. Figure 1 distinguishes human disease-associated R290H from corresponding rat R237H/R297H constructs used in assays. Rat wild-type collybistin recruits gephyrin to the plasma membrane in COS7 cells; the mutant is defective. The mutation retains exchange-associated activity and gephyrin association but impairs phosphoinositide binding and neuronal gephyrin clustering. Figure 3's mouse-brain gephyrin source and Figure 7's rat neuronal cultures are separate from the rat collybistin construct identity. Full original Methods remain outside this read scope.

One new molecular-function annotation is proposed: [GO:0043495 protein-membrane adaptor activity](https://amigo.geneontology.org/amigo/term/GO:0043495), anchored to the species-explicit 2015 study as ISS from rat UniProt Q9QX73. This term describes positioning a protein or complex at a membrane by binding that partner and a membrane component, matching gephyrin/lipid recruitment. It is distinct from nucleotide exchange. The proposal does not assert a direct human IDA, a new biological process, exclusive membrane specificity, or a current human isoform mapping.

## Existing source assertions

All 28 original annotations and three alternative products are preserved. The completed review accepts 18 and leaves ten source-specific binding assertions uncertain. The HuRI study [PMID:32296183](https://pubmed.ncbi.nlm.nih.gov/32296183/) provides general assay and validation methods, but its exact ARHGEF9 partner records have not been read. Those partners are VEZF1, TSGA10IP, ZNF410 isoform Q86VK4-3, FAM90A1, TBC1D22B and FANCL. The separate [PMID:32814053 network](https://pubmed.ncbi.nlm.nih.gov/32814053/) supplies YWHAG, SETDB1 isoform Q15047-2, LMO3 isoform Q8TAP4-4 and KAT5 assertions; only its normal abstract is available in the inspected record. Uninspected pair-level results remain uncertain under the user-supplied review criteria. General assay quality, presumed compartment separation and generic term informativeness do not establish that an individual interaction is wrong. Gephyrin recruitment does not replace the evidence for a different partner.

The current [Human Protein Atlas target summary](https://www.proteinatlas.org/ENSG00000131089-ARHGEF9/subcellular) reports a human cytosolic pool. Its human-cell summary states: “Localized to the cytosol.” HPA055291 reports this location in A-431 and U-251MG cells; the distinct mouse NIH3T3 panel reports nucleoplasm, so those species-specific observations are not collapsed. This is location corroboration, not an independent measurement of exchange activity at that site or an audit of every historical image. The inherited cytosol annotation can be accepted while its exact PAINT placement remains unread. The p75NTR, RhoA/B/C and GABA-conductance Reactome location sources do not expose an independently inspected ARHGEF9 participant graph; acceptance of the location rests on separately identified target evidence and does not confer RAC/RHOA exchange or ion-channel activity.

Actual seeded PAINT nodes PTN002911494 and PTN002911496 are retained with unresolved historical tracing. Donor number and target self-inclusion are not failure criteria. The mouse ISS donor Q3UTH8 is independently identifiable as Arhgef9. Rodent neuronal localization and recruitment support the conserved postsynaptic claims, with their species and product limits explicit.

## Research and completion boundary

The configured deep-research attempt failed without producing a provider report; no provider-branded text has been authored. One ordinary five-reference fetch was interrupted at 45.022 seconds with zero outputs and an unrecorded return code. Hosted Source41 recovery subsequently produced five normal abstract-only records. All five identifiers, titles, complete abstracts and byte-identical raw copies were checked before their exclusive import. These normal records do not contain the separately inspected original Methods or Figure captions; their full-text-unavailable flags remain true. Original raw GOA, UniProt and existing publication/Reactome caches are immutable.


## Original text access

The human hPEM-2 Methods were read in the [author-uploaded original](https://www.researchgate.net/publication/12742192_Identification_and_Characterization_of_hPEM-2_a_Guanine_Nucleotide_Exchange_Factor_Specific_for_Cdc42). The 2004 cloning/initial isoform sections were read on pages 5816–5818 of the [published PDF](https://discovery.ucl.ac.uk/9558/1/9558.pdf). The 2010 Methods and target Results were read on pages 1173–1181 of the [published article](https://d-nb.info/1273231163/34). The 2014 structural and recruitment sections were read in the [indexed primary article](https://pmc.ncbi.nlm.nih.gov/articles/PMC4195776/) and [author-uploaded original](https://www.researchgate.net/publication/264387786_A_conformational_switch_in_collybistin_determines_the_differentiation_of_inhibitory_postsynapses). These access routes do not change the normal cache flags or the narrower reading limits stated above.

## Checkable original-body locator

The positive control in [PMID:25678704, Figure 1D caption](https://pubmed.ncbi.nlm.nih.gov/25678704/) states that with Myc-ΔSH3CbII, “GFP-Gephyrin forms microclusters at the plasma membrane.” Figure 1A explicitly identifies the corresponding rat constructs. Figures 3 and 4 separately establish gephyrin association and lipid binding. This short original-caption quotation is an external source excerpt recorded here; it is absent from the immutable abstract-only normal cache. The NEW annotation uses ISS from rat Q9QX73 rather than claiming direct human IDA.

## Completion checks

The complete review passes the gene validator with no gene advisories and renders successfully. The source audit preserves all 28 original assertions and three products; 43 literal quotation instances, 44 availability flags and seven PMID titles match their actual sources. All five Source41 records match the exact recovered archive, and original raw inputs and existing caches remain unchanged. Final independent annotation consultation is recorded separately.


## Reviewer follow-up: interaction evidence and CDC42 specificity

The ten partner-specific protein-binding assertions are corroborated by the
unchanged UniProt INTERACTION block, which lists all ten partners with three
experiments each. This is positive curated evidence, not evidence of a false
interaction. The exact original HuRI and neurodegeneration-network pair records
and controls remain unread. Their UNDECIDED actions therefore express unresolved
source-specific assessment; they do not reject the interactions. The explicit
instructions supplied for this task require UNDECIDED when relevant publications
cannot be assessed and define REMOVE through unlikely correctness. That instruction
takes precedence over the skill's generic-binding removal default. Genericity alone
does not establish incorrectness, and gephyrin experiments cannot supply an
informative replacement for these different partners.

The broad ARBA small-GTPase regulation annotation is refined to
[GO:0032489 regulation of Cdc42 protein signal transduction](https://amigo.geneontology.org/amigo/term/GO:0032489).
The current official definition and hierarchy were read: the term is a biological
process under regulation of Rho protein signaling, itself under the seeded broad
small-GTPase regulation term. The [original human hPEM-2 result](https://pubmed.ncbi.nlm.nih.gov/10559246/)
selectively activates CDC42 rather than Rac or RhoA. The exchange factor performs
the regulatory step; this is not an inference from necessity alone. The core uses
the specific process instead of simultaneously retaining its parent. The original
Reactome pathway annotation remains broad and unchanged. Human protein was tested
in cellular activation assays; this is not a claim of purified human exchange kinetics.

The description now includes the developmental/epileptic encephalopathy and
hyperekplexia context recorded in the normal UniProt disease section and the
[gephyrin-clustering paper](https://pubmed.ncbi.nlm.nih.gov/15215304/).
Detailed synaptic mechanisms remain supported chiefly by the separately documented
rat constructs and mouse neuronal experiments; no newly read human synaptic assay
or isoform-specific mechanism is claimed by the shorter biological summary.

PI3P binding remains part of the supported membrane-adaptor mechanism. No additional
NEW assertion is proposed in this follow-up: the existing adaptor MF and its lipid
interaction evidence are retained, and a distinct lipid-specific annotation can be
assessed separately with its precise donor, construct and transfer scope. This is
a scope choice, not a claim that lipid binding and adaptor activity are GO synonyms.
All original source objects, the existing NEW adaptor assertion, three product
definitions and immutable source files are preserved.
