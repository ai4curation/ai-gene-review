# Manual literature synthesis for human PI15 (O43692)

## Scope and evidence boundary

The configured automated deep-research providers were unavailable on 2026-07-18 (Falcon/Edison HTTP 402; Perplexity-lite HTTP 401). This manual synthesis uses the reviewed human UniProt record, the local GOA and PANTHER exports, and six repository-cached publications. The strongest direct evidence defines PI15 as a processed secreted CAP-family protein with weak serine-protease inhibitor activity. A later infection study establishes a specialized concentration-dependent interaction with chlamydial CPAF, but the normal human physiological target and process remain unknown.

## Core biochemical function

PI15 encodes a 258-aa precursor with a signal peptide, a propeptide removed before the mature N terminus, and a CAP/SCP domain. The protein was isolated from serum-free conditioned medium of human T98G glioblastoma cells by trypsin-affinity chromatography and showed weak inhibition in trypsin reverse zymography. [PMID:8882727, "p25TI showed weak inhibitory activity against trypsin in reverse"] The cDNA study independently supported precursor organization and expression in neural tumor cells. [PMID:9473672, "The cDNA consisted of 1440 nucleotides and encoded a sequence of 258 amino acids."]

These experiments justify `serine-type endopeptidase inhibitor activity` and extracellular-space localization. The activity is weak compared with classical inhibitors, and neither the physiological human protease target nor inhibition constants have been established. CAP-family membership alone should not be used to broaden the target spectrum.

## Concentration-dependent CPAF regulation

In *Chlamydia trachomatis*-infected human cells, endogenous and tagged PI15 localizes inside the chlamydial inclusion lumen, co-localizes with CPAF aggregates, and co-immunoprecipitates with the inactive CPAF zymogen. [PMID:29900129, "PI15 was transported into the chlamydial inclusion lumen"] [PMID:29900129, "We show that PI15 binds to the CPAF zymogen"]

The biochemical effect is biphasic. Low recombinant PI15 concentrations enhance CPAF protease activity and promote zymogen processing, whereas increasing concentrations inhibit CPAF. [PMID:29900129, "we detected enhanced CPAF protease activity in the presence of very low concentrations of rPI15"] [PMID:29900129, "increasing concentrations of rPI15 inhibited CPAF protease activity"] The proposed activating mechanism is adaptor-like: oligomeric PI15 may bring CPAF zymogens into proximity for autocatalysis. [PMID:29900129, "the oligomerizing properties of PI15 may position CPAF zymogens in close proximity"] Because simultaneous bridging was inferred rather than resolved structurally, `molecular adaptor activity` is best retained as a context-specific non-core activity, not presented as PI15's established constitutive core mechanism.

PI15 knockdown reduces CPAF maturation and infectious progeny formation; PI15 overexpression also impairs progeny formation, and the perturbation is CPAF dependent. This supports host-mediated perturbation of a symbiont process. It does not imply that promotion of chlamydial replication is the normal evolved purpose of PI15.

## Localization and disease context

Direct purification from conditioned medium, a cleaved signal peptide, and detection in patient plasma establish an extracellular soluble pool. In cholangiocarcinoma, tumor and plasma PI15 were elevated in a subset of patients and plasma concentrations fell after surgery. [PMID:30638862, "Plasma PI15 levels in CCA patients were obviously reduced (p = .0014) after surgery."] This supports secretion and biomarker potential but does not establish a causal role in carcinogenesis.

PI15 was also identified by HDA proteomics in EPS-urine exosome preparations. The source study itself cautions that proteins detected after exosome enrichment may also exist as soluble forms and that complex clinical fluids contain contaminants. Exosome localization should therefore remain non-core pending vesicle-protection or immunocapture evidence.

## PAINT propagation assessment

The PTHR10334 PAINT export shows that `molecular adaptor activity` at node PTN000036124 has a single experimental seed, mouse Glipr1l1 (MGI:MGI:1916536). That sperm/acrosome paralog has an IZUMO1-complex role, not a PI15 protease-regulatory mechanism. The PAINT route is therefore an unsafe paralog transfer even though a separate direct PI15 paper makes the same broad GO term defensible in the chlamydial-inclusion context.

## Curation-ready conclusion

PI15 is a secreted, processed CAP-family serine-protease inhibitor. Its core demonstrated activity is weak inhibition of serine-type endopeptidases in extracellular space. In chlamydial infection it enters the inclusion lumen, binds CPAF zymogen, and concentration-dependently promotes or inhibits CPAF activation, producing an infection-specific adaptor/regulatory role. Normal human substrates, physiological processes, oligomeric structure, and bona fide exosome incorporation remain open.
