# LPAR3 literature notes

## Research provenance

- Project deep research was attempted on 2026-08-11 with `just deep-research human LPAR3 --provider perplexity`, but that generic recipe is not present in the current Justfile.
- The available provider-specific command, `just deep-research-perplexity human LPAR3`, was then run and failed with Perplexity HTTP 401 `insufficient_quota`. No provider file was produced or fabricated.
- Primary papers were identified through PubMed/PMC searches and fetched with the project `just fetch-pmid` tooling. All quotations below are copied from the resulting `publications/PMID_*.md` caches.

## Direct identity and ligand-response evidence

- PMID:10488122 is the foundational human clone. Exact abstract quote: “In this study, we isolated a human cDNA encoding a novel G-protein-coupled receptor, designated EDG7, and characterized it as a cellular receptor for LPA.”
- Ligand selectivity is receptor-subtype-specific in the Sf9 expression system: “LPAs with an unsaturated fatty acid but not with a saturated fatty acid induced an increase in the [Ca(2+)](i) of EDG7-expressing Sf9 cells, whereas LPAs with both saturated and unsaturated fatty acids elicited a Ca(2+) response in Sf9 cells expressing EDG4.” [PMID:10488122]
- Both calcium and cAMP responses were pertussis-toxin insensitive in that system: “Neither the EDG7- nor EDG4-transduced Ca(2+) response or cAMP accumulation was inhibited by pertussis toxin.” [PMID:10488122] This supports Gq-like signaling in the assay but does not exclude Gi coupling in other systems.
- The same paper gives a negative context boundary for MAPK: “In PC12 cells, EDG4 but not EDG2 or EDG7 mediated the activation of MAP kinase by LPA.” [PMID:10488122]
- Recombinant receptor pharmacology identified VPC12249 as nonselective between LPAR1 and LPAR3: “One compound with a bulky hydrophobic group (VPC12249) was a dual LPA1/LPA3 competitive antagonist.” [PMID:11723223] Results obtained with this antagonist alone cannot be assigned specifically to LPAR3.

## Historical HOFNH30 sequence / isoform boundary

- The historical HOFNH30 clone was described cautiously: “This receptor has 96% amino acid identity to the Jurkat-T cell-derived EDG7 and could be a splice variant.” [PMID:10891327]
- Its expression differed from EDG7 in the RT-PCR experiment: “RT-PCR analysis demonstrated that HOFNH30 mRNA is expressed in placenta whereas EDG7 mRNA shows highest expression in prostate.” [PMID:10891327]
- It was functional after heterologous expression: “When HOFNH30 was expressed in RBL-2H3 cells, LPA and phosphatidic acid (PA) induced a calcium mobilization response with EC(50) values of 13 nM and 3 microM, respectively.” [PMID:10891327]
- Boundary: the paper says HOFNH30 *could be* a splice variant. The cached reviewed UniProt Q9UBY5 record has no defined alternative-products/isoform section, so this old sequence must not be promoted to a confirmed current UniProt isoform without additional transcript reconciliation.

## Coupling, desensitization, phosphorylation, and trafficking

- Comparative receptor work in transfected C9 rat hepatocyte cells found: “Lysophosphatidic acid and phorbol myristate acetate were able to induce LPA1-3 phosphorylation, in time- and concentration-dependent fashions. It was also clearly observed that agonists and protein kinase C activation induced internalization of these receptors.” [PMID:26473723]
- That study also constrains ERK interpretation: “Activation of LPA1-3 receptors induced ERK 1/2 phosphorylation; this effect was markedly attenuated by inhibition of epidermal growth factor receptor tyrosine kinase activity, suggesting growth factor receptor transactivation in this effect.” [PMID:26473723]
- Newer T-REx HEK293 experiments directly show arrestin recruitment and clathrin-sensitive uptake: “Pitstop 2 (clathrin heavy chain inhibitor) markedly reduced LPA-induced receptor internalization; in contrast, phorbol ester-induced internalization was only delayed. LPA induced rapid β-arrestin-LPA3 receptor association.” [PMID:38928196]
- The mapped sites are explicit: “Phosphorylated residues were detected in the intracellular loop 3 (S221, T224, S225, and S229) and in the carboxyl terminus (S321, S325, S331, T333, S335, Y337, and S343).” [PMID:38928196]
- Mutational follow-up establishes functional relevance: “LPA and PMA-induced receptor interaction with β-arrestin 2 and LPA3 internalization were severely diminished in cells expressing the mutants.” [PMID:38791546]
- Species/context boundary: these are strong direct receptor-mechanism experiments using human LPAR3 constructs, but they are heterologous expression assays (Sf9, RBL-2H3, C9, PC12, or HEK293), not demonstrations that every downstream response occurs in native human tissues.

## High-throughput interaction-screen boundary and curator deference

- The PMID:32296183 annotation represents a large systematic binary interactome screen, not a targeted LPAR3 study. Exact methods/results quote: “To map the reference interactome, we performed nine screens of Space III, followed by pairwise verification by quadruplicate retesting and sequence confirmation.”
- The authors also state: “the majority of PPIs in HuRI were found in only one screen”. [PMID:32296183]
- The many IntAct/GOA LPAR3 partners should therefore retain their exact partner-level provenance and receive curator deference as experimentally screened binary contacts, while remaining non-core candidate interactions unless supported by targeted validation, endogenous co-localization, and a receptor-signaling consequence.

## Tissue context and reproductive physiology

- The reviewed UniProt Q9UBY5 record provides tissue-expression context: “Most abundantly expressed in prostate, testes, pancreas, and heart, with moderate levels in lung and ovary. No detectable expression in brain, placenta, liver, skeletal muscle, kidney, spleen, thymus, small intestine, colon, or peripheral blood leukocytes.” This is a curated database statement from the cached UniProt record, not a direct mechanistic experiment, and “no detectable expression” remains assay- and source-dependent. Its canonical-record placenta statement differs from the older HOFNH30 RT-PCR result above; that tension may reflect sequence, assay, or transcript-definition differences and does not establish HOFNH30 as a current isoform.
- The same UniProt function comment cautiously states: “May play a role in the development of ovarian cancer.” This is a database-level disease association and should not be treated as a demonstrated normal molecular function or as proof of an LPAR3-specific cancer mechanism.
- In vivo reproductive evidence comes from the mouse ortholog: “Targeted deletion of LPA3 in mice resulted in significantly reduced litter size, which could be attributed to delayed implantation and altered embryo spacing.” [PMID:15875025]
- The two reproductive defects had separable consequences and pathway rescue: “Exogenous administration of PGE2 or carbaprostacyclin (a stable analogue of PGI2) into LPA3-deficient female mice rescued delayed implantation but did not rescue defects in embryo spacing.” [PMID:15875025]
- The upstream pathway observation was: “An enzyme demonstrated to influence implantation, cyclooxygenase 2 (COX2) (ref. 5), was downregulated in LPA3-deficient uteri during pre-implantation.” [PMID:15875025] Together with reduced PGE2/PGI2 and selective rescue of implantation timing, this links mouse Lpar3 signaling to uterine COX2-prostaglandin biology while showing that embryo spacing requires an additional or distinct downstream mechanism.
- Species boundary: PMID:15875025 is a targeted **mouse Lpar3 knockout** study. It establishes strong mammalian ortholog physiology but does not by itself demonstrate an equivalent implantation or spacing phenotype for human LPAR3.

## Reference-level conclusions for later annotation review

- High-confidence core: human LPAR3 is an LPA-responsive class-A GPCR; unsaturated LPA species are favored in the foundational assay; calcium mobilization and modulation of adenylyl cyclase are directly demonstrated.
- Coupling should be assay-bounded. The foundational and 2024 calcium/ERK experiments are pertussis-toxin insensitive, whereas receptor-focused reviews describe both Gq/11 and Gi/o coupling; direct claims about a specific G alpha family require matching primary evidence.
- Trafficking is now experimentally supported: ligand-induced phosphorylation, β-arrestin-2 association, and clathrin-sensitive internalization have direct evidence.
- Mouse knockout evidence establishes an in vivo role for Lpar3 in implantation timing and embryo spacing, with COX2-prostaglandin signaling accounting for the timing defect but not the spacing defect; transfer to human reproductive physiology requires direct evidence.
- Do not transfer LPAR1/LPAR2-specific PDZ scaffolds, antagonism, signaling, or tissue phenotypes to LPAR3. Likewise, dual LPAR1/LPAR3 pharmacology cannot establish an LPAR3-specific native phenotype by itself.
