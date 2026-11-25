# ARG3 (YJL088W, P05150) notes

- Ornithine carbamoyltransferase, EC 2.1.3.3: "Reaction=carbamoyl phosphate + L-ornithine = L-citrulline + phosphate +" [UniProt:P05150]; gene cloned: "The yeast arg3 gene, coding for ornithine carbamoyltransferase" [PMID:7029528].
- Location: soluble (cytosolic) in S. cerevisiae, in contrast to the mitochondrial acetylated-cycle enzymes [PMID:205532]. UniProt: "SUBCELLULAR LOCATION: Cytoplasm." Mammalian, Neurospora and S. pombe OTCases are mitochondrial, so the IBA "mitochondrion" (PTN000150427) is a compartment mismatch for budding yeast -> REMOVE with propagation_review.
- Epiarginase regulation: "In the presence of ornithine and arginine, ornithine carbamoyltransferase (OTCase) and arginase form a one-to-one enzyme complex in which the activity of OTCase is inhibited whereas arginase remains catalytically active" [PMID:12679340]. Complex term GO:1903269 accepted; bare protein binding IPI to CAR1 removed as uninformative (interaction itself is real).

## Curation decisions
- Core MF GO:0004585; BP GO:0006526 + GO:0019240 (citrulline is the direct product); CC GO:0005829.
- Generic IEA (amino acid metabolic process; carboxyl/carbamoyltransferase) MODIFY to specific; amino acid binding over-annotated.


## 2026-10-26 systematic fungal annotation audit

Reviewed all 22 existing rows and the core functions with the review and annotation-reviewer workflows. Preserved every machine-sourced term, evidence code, qualifier, source identifier, WITH/FROM entry and row order. No new annotations were added in this audit.

Budding-yeast OTC is cytosolic, unlike pombe and mammalian OTC. PMID:205532 fractionation and PMID:1313366 targeting comparisons support the compartment distinction. PMID:12679340 demonstrates arginase-OTC regulatory complex and altered ornithine affinity in interface mutants, supporting amino-acid binding. Bare protein binding is removed under the current policy without denying the physical interaction. Urea-cycle participation is contextual; the regulatory inhibition limits claims of simultaneous net cycling.

Normal publication caching completed. Normal Falcon research with Perplexity-lite fallback was attempted for this gene; authentication/quota failures prevented a generated report. Manual review used the actual cached primary sources and curated UniProt, and no provider-named research file was fabricated. Per-gene attempts and validation logs are in `.cache/module-audit-logs/arginine-yeast-ARG3-*`. Abstract-only or bibliographic-only sources are distinguished from full text in reference reviews; unavailable source details are not treated as experimental refutations.

Actions: ACCEPT 17, MODIFY 3, REMOVE 2. Record sections were backfilled; focused schema/reference validation passed on the initial complete panel. Final targeted checks and HTML rendering are recorded in the audit logs.
