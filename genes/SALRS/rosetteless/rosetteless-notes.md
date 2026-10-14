# rosetteless (Salpingoeca rosetta, F2U5Y1 / PTSG_03555) — notes

Automated deep research was not available in this session (no provider API
keys configured), so there is no `-deep-research-*.md` file. These notes were
compiled manually from the cached full text of the primary papers.

## Identity

- UniProt F2U5Y1 (TrEMBL, unreviewed), ORF PTSG_03555, EMBL EGD82922.1.
- UniProt's submitted name "Lung surfactant protein A" comes from the genome
  project's EMBL record (`ECO:0000313|EMBL:EGD82922.1`). It is a
  similarity-based label; nothing links this protein functionally to animal
  surfactant protein A (SFTPA1/2). The name used in the literature is
  Rosetteless (Rtls).
- The locus-to-gene mapping: the mapped mutation disrupts "a splice donor in
  the gene EGD82922" [PMID:25299189 "by disrupting a splice donor in the gene EGD82922, was the only one predicted to cause a coding change"].
- Domain architecture: signal peptide, two C-type lectin-like domains
  (Pfam PF00059 x2; SMART CLECT x2), Ser/Thr-rich mucin-like stretches, two
  internal repeats [PMID:25299189 "The rtls gene encodes a 119 kDa protein with an N-terminal signal peptide and two C-type lectin-like domains (CTLDs; Figure 5A)."].
- Carbohydrate binding has not been tested [PMID:25299189 "because the CTLDs of Rtls have not yet been shown to bind sugar moieties, we follow the convention of the field and provisionally refer to Rtls as a C-type lectin-like protein"].

## Genetics

- Forward genetic screen (Levin et al. 2014). The rtls^l1 allele is a T-to-C
  change in the splice donor of intron 7, causing mis-splicing and ~25%
  protein levels. Mutants make normal chains and grow normally but never form
  rosettes [PMID:25299189 "Rosetteless cultures did not form rosettes in ACM, but otherwise appeared in wild type, forming normal chain colonies"].
- No complementation was possible in 2014 [PMID:25299189 "The lack of transgenic approaches in choanoflagellates meant that we could not complement the rtlsl1 mutation nor delete the rtls gene in wild-type cells."].
- Blocking antibody against Rtls inhibits rosette development in wild type
  without affecting growth [PMID:25299189 "Treatment with anti-Rtls resulted in significant inhibition of rosette formation relative to negative controls"].
- Independent CRISPR allele (rtls^PTS1, premature termination) reproduces
  the phenotype [PMID:32496191 "rtlsPTS1 is an independent mutation that prevents the development of rosettes"].
- Knocked out again with a selection-based pipeline (2025; abstract only in cache) [PMID:41037400 "We inactivated three known S. rosetta multicellular developmental regulators (rosetteless, couscous, and jumble)"].

## Localisation

- Secreted; in rosettes it forms a thick layer at the basal poles, filling
  the rosette interior [PMID:25299189 "In rosettes, Rtls (cyan) was detected as a thick layer associated with the basal poles of the cells."].
- In single cells and chains, weak membrane-associated patches and material
  deposited on the substrate [PMID:25299189 "Rtls was detected in membrane-associated patches (arrowheads) in wild-type single cells and chains, but not in Rosetteless cells"].
- The CRISPR mutant lacks secreted Rtls at the basal end [PMID:32496191 "Mutations in rosetteless prevent the secretion of Rosetteless protein at the basal end of cells and into the interior or rosettes."].
- Treated as an ECM component by later work [PMID:30556809 "the localization of Rosetteless protein to the rosette interior suggests that it functions as part of the extracellular matrix (ECM)"].

## Relationship to jumble and couscous

- In the glycosyltransferase mutants, Rtls still reaches the basal pole but
  is not upregulated or secreted after rosette induction [PMID:30556809 "In both Jumble and Couscous cells, Rosetteless protein properly localized to the basal pole, but its expression did not increase nor was it secreted upon treatment with RIFs, as normally occurs in wild type cells"].
  Rtls is itself predicted to be heavily glycosylated [PMID:30556809 "Rosetteless has mucin-like Ser/Thr repeats that are predicted sites of heavy glycosylation and two C-type lectin domains that would be expected to bind to sugar moieties"].

## GO modelling issues

- GOA has no annotations at all for F2U5Y1 (checked 2026-09-30).
- No GO term exists for clonal rosette/colony development in a unicellular
  organism. `GO:0007275` multicellular organism development is not
  taxon-restricted away from choanoflagellates, but GO places *Dictyostelium*
  sorocarp development (`GO:0030587`) outside it (under `GO:0099120`
  socially cooperative development and `GO:0048856` anatomical structure
  development), so using `GO:0007275` for a colony would be a modelling
  decision, not an obvious fit. Proposed an NTR instead.
- MF: the protein's role looks structural (an extracellular layer joining
  cells), but no biochemical activity has been measured. `GO:0005201`
  extracellular matrix structural constituent is used in core_functions as
  an inference, flagged in knowledge_gaps; it is not asserted as an
  annotation.
