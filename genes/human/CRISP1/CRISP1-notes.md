# CRISP1 review notes

## 2026-07-18 — review initiation and source audit

- Seeded the human CRISP1 review with `just fetch-gene human CRISP1` (UniProt P54107). QuickGO returned six rows, each retained as a separate annotation group.
- Ran `just fetch-gene-pmids human CRISP1` while attempting `just deep-research-falcon human CRISP1 --fallback perplexity-lite`. Edison/Falcon returned HTTP 402 Payment Required and Perplexity returned HTTP 401 insufficient quota. No provider-named report was created; the evidence synthesis is recorded in `CRISP1-deep-research-manual.md`.
- CRISP1 is a 249-aa secreted CAP/CRISP-family glycoprotein precursor with a cleaved signal peptide and two annotated splice isoforms. Human tissue evidence places it in the epididymal duct lumen and epithelium, sperm, seminal plasma, and the postacrosomal sperm-head region `[PMID:8543280 "Immunohistochemical analysis showed that the human AEG-like molecule is located in the lumen and epithelium of distal ductus efferentes and epididymal ducts, and on the postacrosomal region of the sperm head."]`.
- The strongest direct human fertilization evidence comes from two studies. Antibody inhibition and recombinant-protein binding support a role after sperm-oolemma binding in gamete fusion `[PMID:11566719 "The antibody did not inhibit the occurrence of spontaneous or Ca(2+) ionophore-induced acrosome reaction, nor did it inhibit the ability of sperm to bind to the oolema, supporting a specific inhibition of the antibody at the sperm-egg fusion level."]`. Human hemizona and recombinant zona-protein assays support sperm-zona binding through ZP3 `[PMID:24334245 "Results revealed that rec-hCRISP1 mainly interacted with ZP3 in a dose-dependent and saturable manner, supporting the specificity of this interaction."]`.
- A newer biochemical study found that human CRISP1 interacts with PMCA4b through its N-terminal region and delays PMCA4b-mediated calcium extrusion `[PMID:37882330 "Human CRISP1 (hCRISP1) and hCRISP3 also interacted with PMCA4b via the N-terminal domain."]` `[PMID:37882330 "Interestingly, hCRISP1 and rCRISP4 delayed PMCA4b-mediated calcium extrusion but hCRISP3 did not."]`. This supports a direct human calcium-transport-regulatory annotation, while the physiological sperm context remains to be established.
- Mouse genetics supports a conserved but partly redundant reproductive role. Single Crisp1-null mice remain fertile but their sperm show reduced zona penetration and fusion in vitro `[PMID:18571638 "In vitro fertilization assays showed that Crisp1(-/-) sperm also exhibited a significantly reduced ability to penetrate both ZP-intact and ZP-free eggs."]`. Combined Crisp1/Crisp4 loss yields fertility and epididymal-epithelium phenotypes, but these mouse phenotypes are not transferred directly to human `[PMID:30510210 "the simultaneous lack of the two epididymal proteins results in clear fertility defects"]`.

## PAINT/IBA trace

- The cached PANTHER trace `interpro/panther/PTHR10334/PTHR10334-paint.tsv` places GO:0060090 molecular adaptor activity at broad node PTN000036124 using only MGI:MGI:1916536, mouse `Glipr1l1`.
- Mouse GLIPR1L1 is a GPI-anchored sperm/acrosomal organizer associated with IZUMO1. CRISP1 is a distinct secreted CRISP subfamily member for which direct human experiments establish ZP3 binding, gamete-fusion participation, and PMCA4b regulation, but not the GO-defined activity of bringing multiple macromolecules together.
- The molecular-adaptor IBA is therefore reviewed as `REMOVE` with `PROPAGATION_BAD`; the source supports its own target but not CRISP1. This does not remove CRISP1's well-supported reproductive functions.

## Annotation decisions and evidence boundaries

- Accept all three extracellular-region annotations. They agree with the signal peptide and direct recovery/localization in epididymal lumen, sperm, and seminal plasma.
- Keep the TAS sperm-egg-fusion annotation as `ACCEPT`; although its 1996 source was initially inferential, the later direct human study PMID:11566719 independently supports the term.
- Mark the HDA nucleus annotation `UNDECIDED`. The cached record for PMID:21630459 is abstract-only and does not name CRISP1, so the source-level peptide evidence and contamination controls cannot be checked. The annotation is not removed because the curator had access to information absent from the cache.
- Add `NEW` direct-human annotations for binding of sperm to zona pellucida (GO:0007339), sperm plasma membrane (GO:0097524), and negative regulation of calcium ion transmembrane transport (GO:1903170).
- Do not transfer rodent sperm-capacitation, CatSper, hyperactivation, cumulus-penetration, or epididymal-development phenotypes as direct human annotations. These remain mechanistic hypotheses and experimental priorities.

