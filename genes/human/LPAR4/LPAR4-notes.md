# LPAR4 literature notes

## Research provenance

- Project deep research was attempted with `just deep-research-perplexity human LPAR4 --timeout 120` on 2026-08-11. The provider returned HTTP 401 `insufficient_quota` ("You exceeded your current quota"), all providers failed, and no `LPAR4-deep-research-perplexity.md` file was produced. This notes file records the manual primary-literature audit; no provider output was fabricated.
- Literature was identified from the reviewed UniProt Q99677 record, GOA/Reactome provenance, PubMed/Europe PMC searches, and citation chaining. Publication text was fetched with the project's `fetch-pmid` tooling and all quotations below were checked against the local caches.

## Identity and nomenclature

- The gene product is the reviewed 370-aa human lysophosphatidic acid receptor 4, Q99677. Historical names include GPR23, P2Y9, and P2Y5-like; these names predate its LPA deorphanization and should not be read as evidence of nucleotide receptor activity.
- The first GPR23 report established identity and genomic location: “This resulted in the isolation of genes GPR21, GPR22 and GPR23.” It mapped GPR23 to “chromosome X, region q13-q21.1.” [PMID:9073069, abstract]
- The independent P2Y5-like cloning study isolated “a complete clone and identified a 1113 base pair open reading frame encoding a new G-coupled receptor that we have called P2Y5-like.” Crucially, “None of the 40 nucleotides and nucleosides tested was able to elicit a response in any of four functional assays: inositol phosphate formation, stimulation or inhibition of cAMP formation, and extracellular acidification measured with a microphysiometer.” [PMID:9223435, abstract] This is a direct boundary against treating historical P2Y9 nomenclature as demonstrated purinergic function.

## Direct human receptor and ligand evidence

- The decisive deorphanization result was direct membrane binding: “Membrane fractions of RH7777 cells transiently expressing p2y9/GPR23 displayed a specific binding for 1-oleoyl-LPA with a Kd value of around 45 nm.” [PMID:12724320, abstract]
- Ligand pharmacology was not generic lipid binding: “Competition binding and reporter gene assays showed that p2y9/GPR23 preferred structural analogs of LPA with a rank order of 1-oleoyl- > 1-stearoyl- > 1-palmitoyl- > 1-myristoyl- > 1-alkyl- > 1-alkenyl-LPA.” [PMID:12724320, abstract]
- In a separate engineered human-receptor system, “In Chinese hamster ovary cells expressing the human GPR23, LPA induced an increase in cellular cyclic adenosine monophosphate (cAMP) and calcium levels.” [PMID:20482379, abstract]
- The 2010 pharmacology screen used both signaling and binding formats: “Here we report the identification of novel GPR23 agonists, inverse agonists, and a negative modulator from 2 high-throughput screens, a beta-lactamase reporter screen, and a [3H]LPA-binding screen.” [PMID:20482379, abstract]
- A related assay paper established engineered constitutive activity rather than native basal signaling: “This report describes how a tetracycline-inducible system was utilized in conjunction with a sensitive β-lactamase reporter gene to develop an assay in which constitutive activity of the receptor could be monitored.” [PMID:21050927, abstract]

## Coupling is assay- and cell-context dependent

- In the founding CHO-cell experiment, “1-oleoyl-LPA induced an increase in intracellular Ca2+ concentration and stimulated adenylyl cyclase activity.” [PMID:12724320, abstract] This supports calcium and Gs/adenylyl-cyclase outputs for recombinant human LPAR4 but does not establish their quantitative importance in every native human cell.
- In rat B103 neuroblastoma transfectants, “we observed G(q/11)-dependent calcium mobilization, but LPA did not affect adenylyl cyclase activity.” [PMID:17172642, abstract] The difference from CHO cells is positive evidence that cyclic-nucleotide direction and coupling weights are context-sensitive.
- The same B103 study concluded: “Thus, our results demonstrated that LPA(4) as well as LPA(1) couple to G(q/11) and G(12/13), whereas LPA(4) differs from LPA(1) in that it does not couple to G(i/o).” [PMID:17172642, abstract] This is strong heterologous coupling evidence, not a direct native-human Gi/o exclusion.
- LPA also produced “neurite retraction, cell aggregation, and cadherin-dependent cell adhesion, which involved Rho-mediated signaling pathways” in those transfectants. [PMID:17172642, abstract] These cell behaviors support a G12/13-Rho branch in that system; the proposed neurodevelopmental role remains an inference from a rat cell line.

## Motility and developmental boundaries

- In mouse embryonic fibroblasts, Lpar4 loss shifted LPA signaling and motility: “LPA(4) deficiency potentiated Akt and Rac but decreased Rho activation induced by LPA. Reconstitution of LPA(4) converted LPA(4)-negative cells into a less motile phenotype.” [PMID:18843048, abstract]
- Human evidence in that paper was ectopic and disease-cell based: “ectopic expression of LPA(4) strongly inhibited migration and invasion of human cancer cells.” [PMID:18843048, abstract] It supports receptor capacity to restrain motility but is not proof of a universal normal-tissue role.
- A separate fibrosarcoma model gave the opposite directional output: “We further provide evidence that LPA(4) signaling in fibrosarcoma cells regulates invadopodia formation downstream of ATX, a process mediated through the activation of EPAC by cyclic AMP and subsequent Rac1 activation.” [PMID:20484039, abstract] LPAR4 knockdown also supported a role in invasion and metastasis in that model. Together, these cancer-cell studies show that LPAR4 effects on motility are strongly context dependent rather than universally suppressive.
- The knockout boundary matters: “Although LPA(4)-deficient mice displayed no apparent abnormalities, LPA(4)-deficient mouse embryonic fibroblasts (MEFs) were hypersensitive to LPA-induced cell migration.” [PMID:18843048, abstract] Later tissue-specific or sensitized phenotypes should not be rewritten as a gross constitutive developmental requirement from this first model.
- Cardiac differentiation evidence spans human and mouse PSC cultures: “During in vitro differentiation of mouse and human PSCs toward cardiac lineage, LPAR4 expression peaked after 3-7 days of differentiation in cardiac progenitors and then declined.” [PMID:33160074, abstract]
- The functional differentiation result was also culture-based: “Sequential stimulation and inhibition of LPAR4 using these agents enhanced the in vitro efficiency of cardiac differentiation from mouse and human PSCs.” The injury-repair result was explicitly murine: “Importantly, in vivo, this sequential stimulation and inhibition of LPAR4 reduced the infarct size and rescued heart dysfunction in mice.” [PMID:33160074, abstract] These data support a transient progenitor context and a mouse repair model, not a constitutive core function of adult human LPAR4.

## Tissue, interactions, trafficking, isoforms, and variants

- The founding study reported: “Quantitative real-time PCR demonstrated that mRNA of p2y9/GPR23 was significantly abundant in ovary compared with other tissues.” [PMID:12724320, abstract] The reviewed UniProt record summarizes “High expression in ovary” and non-detection in the surveyed thalamus, putamen, caudate, frontal cortex, pons, hypothalamus, and hippocampus. This is assay- and tissue-panel context, not proof of absence from every neural cell state.
- GOA/IntAct contains three partner-level IPI rows from PMID:39083597: RAMP1 (O60894), RAMP2 (O60895), and RAMP3 (O60896). The screen context is explicit: “All potential GPCR-RAMP interacting pairs were expressed ectopically, solubilized and analyzed using the multiplexed suspension bead array (SBA) strategy.” [PMID:39083597, introduction]
- The library screen also used “one biological replicate of each of the four unique GPCR-containing samples (each GPCR alone and each GPCR with each of the three RAMPs) in two replicates. Each replicate represented one detection scheme.” [PMID:39083597, results] Thus the LPAR4-RAMP rows support screen-level complex detection, but the audited evidence does not show an endogenous LPAR4-RAMP complex or a functional effect on LPAR4 trafficking, surface delivery, ligand selectivity, or signaling.
- No direct LPAR4 internalization, desensitization, or β-arrestin trafficking study was identified in the audited primary set. RAMP proteins can regulate trafficking for some GPCRs, but that general property must not be transferred to LPAR4 without receptor-specific functional evidence.
- The reviewed UniProt Q99677 record contains no `ALTERNATIVE PRODUCTS` section, so no reviewed protein isoform is established here. Its three `CONFLICT` features are sequence-source discrepancies—“V -> A (in Ref. 8; AAH69996)”, “F -> L (in Ref. 3; AAB66322)”, and “I -> V (in Ref. 8; AAH95538)”—not demonstrated functional alleles or isoform-specific biology.

## Reference-level conclusions for later annotation review

- Core evidence supports an LPA-binding plasma-membrane GPCR with direct ligand binding and recombinant calcium/adenylyl-cyclase responses.
- Gq/11 and G12/13-Rho coupling are well supported in heterologous cells; Gs/cAMP behavior varies by cellular system, and the rat B103 result must not be treated as a universal native-human Gi/o exclusion.
- Motility suppression, cardiac progenitor differentiation, and mouse injury/development phenotypes are important bounded outputs, not additional receptor molecular activities.
- RAMP1/2/3 are high-throughput interaction candidates. Functional consequences and endogenous human complexes remain open questions.
- No reviewed isoform-specific function or experimentally reconciled functional variant was found; historical nucleotide-receptor names and sequence conflicts should not be overinterpreted.
