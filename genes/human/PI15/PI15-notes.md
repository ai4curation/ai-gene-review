# PI15 review notes

## 2026-07-18 — retrieval and research boundary

- `just fetch-gene human PI15` retrieved reviewed UniProt O43692 and five current GOA groups.
- `just fetch-gene-pmids human PI15` confirmed the two PMID-backed GOA sources, PMID:8882727 and PMID:23533145.
- The configured Falcon/Edison deep-research request failed with HTTP 402, and the `perplexity-lite` fallback failed with HTTP 401 because provider quota was exhausted. No provider-named report was created; manual synthesis is recorded in `PI15-deep-research-manual.md`.
- Additional direct sources were cached manually: PMID:9473672, PMID:29900129, and PMID:30638862.

## Protein identity, processing, and secretion

- Human PI15 is a 258-aa CAP/CRISP-family precursor. UniProt assigns a signal peptide (1–19), propeptide (20–60), mature chain (61–258), and SCP/CAP domain (71–211).
- PI15 was purified from serum-free T98G glioblastoma conditioned medium as p25TI, a 25-kDa trypsin-binding protein with weak inhibitory activity. [PMID:8882727 Purification and identification of a novel and four known serine proteinase inhibitors secreted by human glioblastoma cells, "p25TI showed weak inhibitory activity against trypsin in reverse"]
- The cloned cDNA encodes a 258-aa precursor with predicted signal peptide, propeptide, and mature chain, consistent with the N-terminal protein sequencing. [PMID:9473672 cDNA cloning of a novel trypsin inhibitor with similarity to pathogenesis-related proteins, and its frequent expression in human brain cancer cells, "The cDNA consisted of 1440 nucleotides and encoded a sequence of 258 amino acids."]
- PI15 was detected in plasma and strongly elevated in a subset of cholangiocarcinoma patients; levels fell after tumor resection. This independently confirms a circulating extracellular pool in disease but establishes biomarker utility, not an oncogenic mechanism. [PMID:30638862 Peptidase inhibitor 15 as a novel blood diagnostic marker for cholangiocarcinoma, "Plasma PI15 levels in CCA patients were obviously reduced (p = .0014) after surgery."]

## Molecular activity

- Direct reverse-zymography evidence establishes weak inhibition of trypsin and supports `serine-type endopeptidase inhibitor activity` rather than generic `protein binding` or an inferred catalytic activity. [PMID:8882727, "p25TI showed weak inhibitory activity against trypsin in reverse"]
- During *Chlamydia trachomatis* infection, PI15 enters the inclusion lumen and binds the inactive CPAF serine-protease zymogen. [PMID:29900129 Peptidase Inhibitor 15 (PI15) Regulates Chlamydial CPAF Activity, "PI15 was transported into the chlamydial inclusion lumen"] [PMID:29900129, "We show that PI15 binds to the CPAF zymogen"]
- Recombinant PI15 has a biphasic concentration-dependent effect: low concentrations promote CPAF processing/activity, while high concentrations inhibit CPAF activity. [PMID:29900129, "we detected enhanced CPAF protease activity in the presence of very low concentrations of rPI15"] [PMID:29900129, "increasing concentrations of rPI15 inhibited CPAF protease activity"]
- The authors propose that oligomeric PI15 brings CPAF zymogens into proximity for autoprocessing. This is compatible with `molecular adaptor activity`, but the evidence is infection-context-specific and the bridging geometry remains a model rather than a direct stoichiometric demonstration. [PMID:29900129, "the oligomerizing properties of PI15 may position CPAF zymogens in close proximity"]

## Biological-process evidence

- Both PI15 depletion and overexpression impair production of infectious chlamydial progeny; PI15 depletion reduces CPAF maturation, and the growth phenotype is not significant for a CPAF-deficient mutant. [PMID:29900129, "We observed decreased CPAF activation if PI15 levels were reduced"]
- These genetic perturbations support a context-specific `host-mediated perturbation of symbiont process` annotation. They do not establish that supporting infection is PI15's normal evolved physiological role.
- A chicken ortholog is a developmental marker in thyroid/pancreatic mesoderm, but the abstract does not demonstrate a causal activity and should not be transferred as a human developmental function.
- The physiological human extracellular protease target, normal tissue process, and relevance of the CPAF mechanism outside infection remain unknown.

## Existing-annotation decisions

- Accept the PAINT and automated extracellular-region annotations: direct purification from conditioned medium, signal-peptide processing, and plasma detection all support secretion.
- Modify the direct experimental `extracellular region` annotation to the more informative `extracellular space` term.
- Keep `extracellular exosome` as non-core. The HDA source detected PI15 in pooled EPS-urine exosome proteomics, but the publication notes that proteins in these preparations can also exist as soluble forms or contaminants; exosome cargo is not PI15's defining location.
- Keep `molecular adaptor activity` as non-core because direct PI15 experiments independently support an adaptor-like CPAF-zymogen-clustering model during infection. The PAINT propagation itself is unsafe: its sole experimental seed is the divergent sperm paralog mouse Glipr1l1, not PI15.
- Add direct `serine-type endopeptidase inhibitor activity`, concentration-dependent positive and negative regulation of endopeptidase activity, and host-mediated perturbation of a symbiont process.
- Do not annotate cholangiocarcinoma development or tumor suppression: PI15 is a biomarker in that study, and causal tumor biology was not tested.
