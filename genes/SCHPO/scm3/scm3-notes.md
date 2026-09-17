# scm3 (SPAPB1A10.02) - Gene Review Notes

## Gene Overview
- **Full name**: CENP-A histone chaperone scm3
- **UniProt ID**: Q9HDY7
- **Organism**: Schizosaccharomyces pombe (fission yeast)
- **Domains**: Scm3/HJURP (IPR018465), Histone-fold (IPR009072), Scm3 Pfam (PF10384)
- **Human ortholog**: HJURP (Holliday junction recognition protein)

## Core Function Summary
Scm3 is the dedicated CENP-A/Cnp1 histone chaperone in S. pombe. Its primary function is to
mediate the stable deposition of the histone H3 variant CENP-A (Cnp1) into centromeric chromatin,
which is essential for kinetochore assembly and proper chromosome segregation.

### Key structural domains:
1. **N-terminal CENP-A binding domain** - Interacts specifically with Cnp1/CENP-A [PMID:19217403, PMID:19217404]
2. **Mis16-binding domain (Mis16-BD)** (~aa 270-305) - Interacts with Mis16 for centromere targeting [PMID:38084929]
3. **C-terminal cysteine-rich domain (CYS)** - Binds zinc, essential for centromere localization [PMID:38084929]

## Key Literature Findings

### PMID:19217403 (Williams et al. 2009)
- Scm3 is required for centromeric localization of Cnp1
- Scm3 localizes at centromeres independently of Cnp1
- Mis16-Mis18 complex required for Scm3 centromere localization
- Scm3 dissociates from centromeres during mitosis (like Mis16/Mis18)
- Inactivation of Scm3 leads to H3 and H2A/H2B invading centromeres
- In S. pombe, Scm3 acts as a Cnp1 assembly/maintenance factor (not a nucleosome component as proposed in budding yeast)

### PMID:19217404 (Pidoux et al. 2009)
- Scm3 co-affinity purifies with Cnp1/CENP-A
- Scm3 associates with CENP-A in vitro
- Scm3 localizes independently of intact CENP-A chromatin
- Differentially released from chromatin compared to CENP-A
- Required for integrity of subkinetochore chromatin
- Model: Scm3 acts as a CENP-A receptor, cooperating with Mis16 and Mis18

### PMID:26275423 (Thakur et al. 2015)
- ChIP-seq mapping of inner kinetochore proteins
- Scm3 is highly enriched throughout the centromeric central domain
- Enriched except at tRNA genes
- Weakly enriched in H3-rich heterochromatin (outer repeats)
- No evidence for preferred kinetochore assembly sites

### PMID:38084929 (Folco et al. 2024)
- CYS domain binds zinc in vitro
- CYS is essential for Scm3 centromere localization and function
- Disrupting CYS prevents centromere localization and compromises kinetochore integrity
- CYS alone can localize to centromere (weakly), enhanced with Mis16-BD
- CYS likely binds centromeric DNA (independent of Mis16 interaction)
- Overexpression of truncated Scm3 (with CYS but lacking CENP-A binding) causes toxicity and kinetochore loss

### PMID:16823372 (Matsuyama et al. 2006)
- Large-scale protein localization study
- Scm3 detected in both nucleus and cytoplasm/cytosol (HDA evidence)

## Protein-Protein Interactions
- **Cnp1/CENP-A (SPBC1105.17)**: Direct binding via N-terminal domain [PMID:19217403, PMID:19217404]
- **Mis16 (SPCC970.12)**: Interaction via Mis16-BD for centromere targeting [PMID:19217404]
- **Mis18 (SPCC1672.10)**: Part of the Mis18 holocomplex pathway [PMID:19217403]
- **Self-interaction (SPAPB1A10.02)**: Reported IPI with itself [PMID:19217403]

## Annotation Review Considerations
- "protein binding" (GO:0005515) annotations should be replaced with more specific terms
- Histone chaperone activity is well-supported experimentally
- Zinc ion binding is supported by the CYS domain characterization
- The protein heterodimerization IEA may relate to histone fold but needs evaluation
- Scm3 is NOT a stable nucleosome component in S. pombe (unlike what was proposed for budding yeast)

## 2026-09-01 refresh and evidence audit

- Refetched UniProt and QuickGO data with `just fetch-gene SCHPO scm3 --force`.
  Three retired generic protein-binding rows supported by PMID:19217403 were removed
  from the review because they are no longer present in GOA.
- QuickGO returned three PMID:19217403 annotations to GO:0034506 that differ only by
  annotation extension (`existence_overlaps` cell-cycle terms). The repository TSV
  does not represent extensions, so these became byte-identical rows. This exposed
  the projection bug fixed and merged separately in PR #2913; the post-merge refetch
  now retains one projected row without bypassing the fetch wrapper.
- The two PMID:19217404 protein-binding annotations remain distinct because their
  WITH/FROM partners differ: Cnp1 (PomBase:SPBC1105.17) and Mis18
  (PomBase:SPCC970.12). They are now represented separately in the YAML. Cnp1 binding
  is modified to the informative histone binding term; the generic Mis18
  binding term is retained as over-annotated rather than treated as a separate activity.
- Corrected an evidence overstatement: PMID:19217403 reports no Scm3-H4 interaction
  in the yeast two-hybrid experiment, but that passage does not establish a negative
  result for Scm3-H3 binding.
- Replaced the core-function support from the secondary deep-research synthesis with
  verbatim evidence from PMID:19217403, PMID:19217404, and PMID:38084929. The four
  primary functional/localization papers were manually adjudicated and recorded in
  `reference_review`.
- No OpenScientist job was launched: the core function, principal localization, and
  zinc-dependent targeting mechanism are directly covered by accessible full-text
  primary studies, leaving no focused unresolved hypothesis that would improve this
  review.
- PR review follow-up added GO:0019237 `centromeric DNA binding` as a `NEW` IDA
  annotation from PMID:38084929. Because the GO term already exists, this belongs in
  `existing_annotations` with `action: NEW`, not in `proposed_new_terms`, which is
  reserved for ontology terms that do not yet exist.
- Replaced the PMID:19217404 chromatin-assembly support with the paper's direct
  incorporation result, and refined the Cnp1 IPI replacement to GO:0042393 `histone
  binding` so that the recommendation does not claim chaperone activity from binding
  evidence alone.
- Verified the second PMID:19217404 IPI partner against PomBase: SPCC970.12 is Mis18,
  not Mis16 (whose systematic identifier is SPCC1672.10), and corrected the review
  prose accordingly.
