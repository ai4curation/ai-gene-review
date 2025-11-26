---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-11-25T17:34:40.309141'
end_time: '2025-11-25T17:39:29.652090'
duration_seconds: 289.34
template_file: templates/rule_research.md
template_variables:
  rule_id: ARBA00026249
  rule_type: arba
  go_terms: GO:0004791 (thioredoxin-disulfide reductase (NADPH) activity)
  conditions_summary: '**Condition Set 1:** InterPro id: Thioredoxin reductase (InterPro:IPR005982)
    AND InterPro id: Pyridine nucleotide-disulphide oxidoreductase, class-II, active
    site (InterPro:IPR008255) AND InterPro id: FAD/NAD(P)-binding domain (InterPro:IPR023753)


    **Condition Set 2:** FunFam id: Thioredoxin reductase (CATH.FunFam:3.50.50.60:FF:000064)
    AND taxon: Eukaryota (NCBITaxon:2759)


    **Condition Set 3:** FunFam id: Thioredoxin reductase 1, cytoplasmic (CATH.FunFam:3.30.390.30:FF:000004)
    AND FunFam id: Thioredoxin reductase (CATH.FunFam:3.50.50.60:FF:000190) AND taxon:
    Rattus (NCBITaxon:10114)


    *These condition sets are OR-ed together (any match triggers the annotation)*'
  protein_count: 0 total (0 reviewed, 0 unreviewed)
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 15
---

## Question

# UniProt Rule Research

## Rule Context

- **Rule ID:** ARBA00026249
- **Rule Type:** arba
- **GO Term(s) Predicted:** GO:0004791 (thioredoxin-disulfide reductase (NADPH) activity)
- **Proteins Annotated:** 0 total (0 reviewed, 0 unreviewed)

### Condition Summary

**Condition Set 1:** InterPro id: Thioredoxin reductase (InterPro:IPR005982) AND InterPro id: Pyridine nucleotide-disulphide oxidoreductase, class-II, active site (InterPro:IPR008255) AND InterPro id: FAD/NAD(P)-binding domain (InterPro:IPR023753)

**Condition Set 2:** FunFam id: Thioredoxin reductase (CATH.FunFam:3.50.50.60:FF:000064) AND taxon: Eukaryota (NCBITaxon:2759)

**Condition Set 3:** FunFam id: Thioredoxin reductase 1, cytoplasmic (CATH.FunFam:3.30.390.30:FF:000004) AND FunFam id: Thioredoxin reductase (CATH.FunFam:3.50.50.60:FF:000190) AND taxon: Rattus (NCBITaxon:10114)

*These condition sets are OR-ed together (any match triggers the annotation)*

---

## Research Objective

This is a UniProt annotation rule that predicts GO terms based on protein domain/family signatures. Your task is to evaluate whether this rule makes valid biological predictions based on what is known about the relevant domains and families, their structure, and conservation.

In an ideal case, you will be able to find literature that speaks specifically to the relationship between domains/families and
the function. Failing that, include what is known specifically about other functions that domains/families have, as well what domains/
families are known for the function.

## Research Questions

### 1. Domain/Signature Context

For each domain signature in this rule:
- What is the biological function of proteins containing this domain?
- Is this domain diagnostic for the predicted function?
- Are there known subfamilies with different functions?
- Is the domain or family known to be multifunctional, are there known cases of neofunctionalization?

### 2. GO Term Appropriateness

For the predicted GO term(s) **GO:0004791 (thioredoxin-disulfide reductase (NADPH) activity)**:
- Is this GO term appropriate for proteins matching these conditions?
- Is the term too broad? (e.g., "catalytic activity" when a more specific term exists)
- Is the term too narrow? (e.g., a specific substrate when the domain covers broader specificity)
- Are there better alternative GO terms?

### 3. Literature Support

- What experimental evidence supports this functional annotation?
- Are there key papers describing this protein family/enzyme?
- Are there any contradictory findings in the literature?
- Is this a well-established function or more speculative?

### 4. Taxonomic Considerations

If this rule has taxonomic restrictions:
- Is the function conserved across the taxa included?
- Are there taxa that should be excluded (different function)?
- Are there taxa that could be included but are currently excluded?

### 5. Rule Logic Assessment

- Do the domain combinations make biological sense?
- Are there redundant conditions that could be removed?
- Could false positives arise from these conditions?

## Output Format

Please provide your findings in a narrative format with citations. Structure your response as:

1. **Executive Summary** - Brief assessment of rule validity
2. **Domain Analysis** - What each domain/signature represents
3. **GO Term Evaluation** - Assessment of the predicted annotation
4. **Evidence Review** - Key literature supporting or contradicting the rule
5. **Recommendations** - Suggested improvements or concerns

Be sure to include citations for all statements.

## Output

Question: You are an expert researcher providing comprehensive, well-cited information.

Provide detailed information focusing on:
1. Key concepts and definitions with current understanding
2. Recent developments and latest research (prioritize 2023-2024 sources)
3. Current applications and real-world implementations
4. Expert opinions and analysis from authoritative sources
5. Relevant statistics and data from recent studies

Format as a comprehensive research report with proper citations. Include URLs and publication dates where available.
Always prioritize recent, authoritative sources and provide specific citations for all major claims.

# UniProt Rule Research

## Rule Context

- **Rule ID:** ARBA00026249
- **Rule Type:** arba
- **GO Term(s) Predicted:** GO:0004791 (thioredoxin-disulfide reductase (NADPH) activity)
- **Proteins Annotated:** 0 total (0 reviewed, 0 unreviewed)

### Condition Summary

**Condition Set 1:** InterPro id: Thioredoxin reductase (InterPro:IPR005982) AND InterPro id: Pyridine nucleotide-disulphide oxidoreductase, class-II, active site (InterPro:IPR008255) AND InterPro id: FAD/NAD(P)-binding domain (InterPro:IPR023753)

**Condition Set 2:** FunFam id: Thioredoxin reductase (CATH.FunFam:3.50.50.60:FF:000064) AND taxon: Eukaryota (NCBITaxon:2759)

**Condition Set 3:** FunFam id: Thioredoxin reductase 1, cytoplasmic (CATH.FunFam:3.30.390.30:FF:000004) AND FunFam id: Thioredoxin reductase (CATH.FunFam:3.50.50.60:FF:000190) AND taxon: Rattus (NCBITaxon:10114)

*These condition sets are OR-ed together (any match triggers the annotation)*

---

## Research Objective

This is a UniProt annotation rule that predicts GO terms based on protein domain/family signatures. Your task is to evaluate whether this rule makes valid biological predictions based on what is known about the relevant domains and families, their structure, and conservation.

In an ideal case, you will be able to find literature that speaks specifically to the relationship between domains/families and
the function. Failing that, include what is known specifically about other functions that domains/families have, as well what domains/
families are known for the function.

## Research Questions

### 1. Domain/Signature Context

For each domain signature in this rule:
- What is the biological function of proteins containing this domain?
- Is this domain diagnostic for the predicted function?
- Are there known subfamilies with different functions?
- Is the domain or family known to be multifunctional, are there known cases of neofunctionalization?

### 2. GO Term Appropriateness

For the predicted GO term(s) **GO:0004791 (thioredoxin-disulfide reductase (NADPH) activity)**:
- Is this GO term appropriate for proteins matching these conditions?
- Is the term too broad? (e.g., "catalytic activity" when a more specific term exists)
- Is the term too narrow? (e.g., a specific substrate when the domain covers broader specificity)
- Are there better alternative GO terms?

### 3. Literature Support

- What experimental evidence supports this functional annotation?
- Are there key papers describing this protein family/enzyme?
- Are there any contradictory findings in the literature?
- Is this a well-established function or more speculative?

### 4. Taxonomic Considerations

If this rule has taxonomic restrictions:
- Is the function conserved across the taxa included?
- Are there taxa that should be excluded (different function)?
- Are there taxa that could be included but are currently excluded?

### 5. Rule Logic Assessment

- Do the domain combinations make biological sense?
- Are there redundant conditions that could be removed?
- Could false positives arise from these conditions?

## Output Format

Please provide your findings in a narrative format with citations. Structure your response as:

1. **Executive Summary** - Brief assessment of rule validity
2. **Domain Analysis** - What each domain/signature represents
3. **GO Term Evaluation** - Assessment of the predicted annotation
4. **Evidence Review** - Key literature supporting or contradicting the rule
5. **Recommendations** - Suggested improvements or concerns

Be sure to include citations for all statements.

1. Executive Summary

Assessment: ARBA00026249 is largely valid. When the specific thioredoxin reductase (TrxR) family signature (InterPro: IPR005982) is combined with a pyridine nucleotide–disulfide oxidoreductase class-II active site (IPR008255) and a Rossmann-type FAD/NAD(P)-binding domain (IPR023753), and/or CATH FunFams explicitly centered on TrxR, the rule captures proteins whose conserved architecture and catalytic mechanism align with GO:0004791 (thioredoxin-disulfide reductase (NADPH) activity). Recent structural and mechanistic reviews reinforce that TrxRs are FAD-dependent homodimers within the pyridine nucleotide–disulfide oxidoreductase family and, in eukaryotes, commonly possess a C‑terminal Cys–Sec redox center mediating thioredoxin reduction via NADPH, matching the GO term. However, generic family features and non‑TrxR, TR‑like oxidoreductases exist (e.g., YpdA/Bdr, FNR-like relatives), emphasizing the importance of the TrxR-specific signature and the eukaryote/rodent FunFam filters to avoid false positives. The rule’s taxon constraints (Eukaryota; Rattus) and FunFam use increase specificity. Overall, the annotation is appropriate but should avoid reliance on broad oxidoreductase motifs alone (ardini2024the"doorstoppocket" pages 1-3, maia2023selenium—morethanjust pages 15-17, shoor2021thioredoxinreductasefrom pages 12-15, shoor2021thioredoxinreductasefrom pages 15-18).

2. Domain Analysis

• InterPro: IPR005982 (Thioredoxin reductase)
  – Functional role: Defines TrxR family membership within the pyridine nucleotide–disulfide oxidoreductase superfamily; TrxRs are FAD-containing homodimers using NADPH to reduce thioredoxin via N- and C-terminal redox centers (Cys–Sec pair in high‑MW eukaryotic enzymes). This domain is the primary determinant for TrxR catalytic function (URL: https://doi.org/10.1021/acs.jmedchem.4c00669, Sep 2024; https://doi.org/10.3390/molecules29010120, Dec 2023) (ardini2024the"doorstoppocket" pages 1-3, maia2023selenium—morethanjust pages 15-17).
  – Diagnostic value: High. TrxR-specific sequence/structural features (long C‑terminal arm; in many eukaryotes, the -GCUG motif) distinguish TrxR from related oxidoreductases; however, the broader fold is shared with GR/Lpd/TGR (ardini2024the"doorstoppocket" pages 1-3, ardini2024the"doorstoppocket" pages 37-39).
  – Subfamilies/multifunctionality: Eukaryotic high‑MW TrxRs include isoforms (TrxR1 cytosolic, TrxR2 mitochondrial) and the fusion enzyme TGR (TrxR–Grx) capable of TrxR and glutaredoxin/glutathione reductase activities; parasitic flatworms rely on TGR as an essential enzyme (URL: https://doi.org/10.1021/acs.jmedchem.4c00669, Sep 2024) (ardini2024the"doorstoppocket" pages 1-3, ardini2024the"doorstoppocket" pages 37-39, brandstaedter2018kineticcharacterizationof pages 1-4, brandstaedter2018kineticcharacterizationof pages 17-20).

• InterPro: IPR008255 (Pyridine nucleotide–disulphide oxidoreductase, class-II, active site)
  – Functional role: Encodes the canonical class-II dithiol/disulfide redox chemistry of the family. Found across TrxR, glutathione reductase (GR), lipoamide dehydrogenase, and related enzymes; thus, it captures mechanism but not substrate specificity (URL: https://doi.org/10.1021/acs.jmedchem.4c00669, Sep 2024) (ardini2024the"doorstoppocket" pages 37-39).
  – Diagnostic value: Moderate. Supports family membership but is insufficient alone to assert TrxR activity; must be paired with TrxR-specific signatures (shoor2021thioredoxinreductasefrom pages 15-18).

• InterPro: IPR023753 (FAD/NAD(P)-binding domain)
  – Functional role: Rossmann-like dinucleotide-binding fold for FAD and NADPH; ubiquitous in flavoenzymes. TrxR’s catalytic cycle requires these cofactors (URL: https://doi.org/10.3390/molecules29010120, Dec 2023) (maia2023selenium—morethanjust pages 15-17).
  – Diagnostic value: Low alone. Broad across many oxidoreductases; contributes when combined with IPR005982 and IPR008255 (shoor2021thioredoxinreductasefrom pages 15-18).

• CATH FunFams: 3.50.50.60:FF:000064 (Thioredoxin reductase), 3.30.390.30:FF:000004 (Thioredoxin reductase 1, cytoplasmic), 3.50.50.60:FF:000190
  – Functional role: Capture TrxR structural families and in some cases specific isoform contexts (e.g., cytosolic TrxR1). The conserved “doorstop pocket” at the re‑face of FAD and active-site motifs are shared across TrxR/TGR and related family members, but pocket shape/electrostatics vary by isoform, aiding subclass delineation (URL: https://doi.org/10.1021/acs.jmedchem.4c00669, Sep 2024) (ardini2024the"doorstoppocket" pages 37-39, ardini2024the"doorstoppocket" pages 1-3).
  – Diagnostic value: High when FunFams are curated on experimentally characterized TrxRs; in combination with eukaryote/rat taxa, these families enrich for true TrxR function and reduce bacterial TR-like off-targets (shoor2021thioredoxinreductasefrom pages 15-18).

Known subfamilies and neofunctionalization
• High-MW Sec-containing TrxRs (mammals, many metazoans) versus low-MW Cys enzymes (bacteria, some lower eukaryotes); TGR fusions are multifunctional (TrxR + Grx/GR). Partner specificity and cofactor-binding asymmetry can differ between subfamilies (URL: https://doi.org/10.3390/molecules29010120, Dec 2023; https://doi.org/10.1002/2211-5463.13289, Sep 2021) (maia2023selenium—morethanjust pages 15-17, shoor2021thioredoxinreductasefrom pages 12-15, shoor2021thioredoxinreductasefrom pages 22-29). Non‑TrxR relatives with TR-like folds (e.g., YpdA/Bdr; TR-like FNRs) illustrate potential for neofunctionalization within the broader fold (shoor2021thioredoxinreductasefrom pages 15-18).

3. GO Term Evaluation

• Appropriateness: GO:0004791 (thioredoxin-disulfide reductase (NADPH) activity) precisely matches the canonical reaction catalyzed by TrxR: NADPH-dependent reduction of thioredoxin disulfide via FAD and redox-active cysteine/selenocysteine centers, as detailed in recent structural and mechanistic reviews (URL: https://doi.org/10.3390/molecules29010120; https://doi.org/10.1021/acs.jmedchem.4c00669) (maia2023selenium—morethanjust pages 15-17, ardini2024the"doorstoppocket" pages 1-3).
• Breadth vs. specificity: The term is neither too broad nor too narrow for bona fide TrxRs across high‑MW and low‑MW enzymes, including TGRs that retain TrxR activity. It should not be assigned from generic family motifs alone; the TrxR-specific signature (IPR005982) or TrxR-focused FunFams should be present (shoor2021thioredoxinreductasefrom pages 15-18, ardini2024the"doorstoppocket" pages 37-39).
• Alternative/Additional terms: Depending on curation scope, consider adding enabling terms such as “FAD binding” and “thioredoxin binding,” but these are not substitutes for the catalytic function. Cellular component and isoform-specific annotations (e.g., cytosol for TrxR1; mitochondrion for TrxR2) would require additional evidence not covered by this rule (ardini2024the"doorstoppocket" pages 1-3, ardini2024the"doorstoppocket" pages 37-39).

4. Evidence Review

Key concepts and definitions (current understanding)
• TrxRs are FAD-dependent homodimeric pyridine nucleotide–disulfide oxidoreductases that use NADPH to reduce thioredoxin via conserved redox centers. Eukaryotic high‑MW enzymes often possess a C‑terminal Cys–Sec pair (-GCUG) that enhances nucleophilicity and supports efficient catalysis; the catalytic cycle cycles selenolate/selenenylsulfide states (URL: https://doi.org/10.3390/molecules29010120, Dec 2023) (maia2023selenium—morethanjust pages 15-17).
• The family shares a conserved FAD site and a regulatory/druggable “doorstop pocket” controlling NADPH/NADP+ entry/exit; pocket presence is universal across the family but shows isoform- and species-specific features exploitable for selectivity (URL: https://doi.org/10.1021/acs.jmedchem.4c00669, Sep 2024) (ardini2024the"doorstoppocket" pages 37-39, ardini2024the"doorstoppocket" pages 1-3).

Recent developments (2023–2024) and latest research
• Doorstop pocket as a druggable site: Medicinal chemistry now targets the doorstop pocket, first demonstrated in Schistosoma mansoni TGR to block catalytic cycling by restricting required aromatic side-chain motion for NADPH exchange, leading to potent anti‑schistosomal inhibitors (URL: https://doi.org/10.1021/acs.jmedchem.4c00669, Sep 2024) (ardini2024the"doorstoppocket" pages 1-3, ardini2024the"doorstoppocket" pages 37-39).
• Updated perspectives on selenium’s role: 2023 synthesis emphasizes the mechanistic impact of Sec in high‑MW TrxRs, including stronger nucleophilicity and unique selenenyl-sulfide chemistry in the C‑terminal motif (URL: https://doi.org/10.3390/molecules29010120, Dec 2023) (maia2023selenium—morethanjust pages 15-17).
• Structural-functional diversification and partner specificity in bacteria: 2021 structural work shows asymmetric NADPH binding and limited cross-functionality (e.g., weak FNR activity) for Bacillus cereus TrxR, underscoring caution in inferring function based solely on fold-level similarity (URL: https://doi.org/10.1002/2211-5463.13289, Sep 2021) (shoor2021thioredoxinreductasefrom pages 12-15, shoor2021thioredoxinreductasefrom pages 22-29).

Current applications and real-world implementations
• Anti-parasitic targeting of TGR: Platyhelminths rely on a single TGR for both Trx and GSH systems; the doorstop pocket has enabled development of new TGR inhibitors surpassing current schistosomiasis treatments in preclinical profiling (URL: https://doi.org/10.1021/acs.jmedchem.4c00669, Sep 2024) (ardini2024the"doorstoppocket" pages 1-3).

Expert opinions and analysis
• Reviews emphasize TrxR/TGR as compelling but challenging targets due to covalent inhibition liabilities at the Sec motif and the need to exploit structural features like the doorstop pocket for selectivity across isoforms/species (URL: https://doi.org/10.1021/acs.jmedchem.4c00669, Sep 2024; https://doi.org/10.3390/molecules29010120, Dec 2023) (ardini2024the"doorstoppocket" pages 1-3, maia2023selenium—morethanjust pages 15-17).

Relevant statistics and data
• Structural universality of the doorstop pocket has been mapped across multiple solved structures (various PDBs) and taxa; isoform comparisons show conserved presence with differing shape/electrostatics (URL: https://doi.org/10.1021/acs.jmedchem.4c00669, Sep 2024) (ardini2024the"doorstoppocket" pages 37-39).
• Asymmetric/half-of-sites NADPH occupancy has been directly observed crystallographically in B. cereus and S. aureus TrxRs, informing kinetic models and partner specificity (URL: https://doi.org/10.1002/2211-5463.13289, Sep 2021) (shoor2021thioredoxinreductasefrom pages 22-29, shoor2021thioredoxinreductasefrom pages 12-15).

Contradictory findings/nuance
• TrxR-like folds can underpin enzymes with alternative physiological roles (e.g., YpdA/Bdr, and TrxR-like FNRs), which could be mis-annotated as TrxR if only generic family motifs or Rossmann domains are used. This argues for retaining the TrxR-specific signature/FunFam/taxonomy filters in rule logic (URL: https://doi.org/10.1002/2211-5463.13289, Sep 2021) (shoor2021thioredoxinreductasefrom pages 15-18).
• TGR multifunctionality means that proteins may show multiple related activities (TrxR, GR, Grx), but TrxR activity is preserved, supporting GO:0004791 while cautioning against overinterpreting additional functions from this rule alone (URL: https://doi.org/10.1111/febs.14357, Feb 2018) (brandstaedter2018kineticcharacterizationof pages 1-4, brandstaedter2018kineticcharacterizationof pages 17-20).

5. Taxonomic Considerations

• Eukaryota focus: High‑MW Sec-containing TrxRs are characteristic of mammals (TrxR1 cytosolic; TrxR2 mitochondrial) and TGR. Assigning GO:0004791 within Eukaryota given TrxR-specific signatures is appropriate and consistent with conserved mechanism (URL: https://doi.org/10.3390/molecules29010120, Dec 2023) (maia2023selenium—morethanjust pages 15-17).
• Rattus restriction (TrxR1 cytoplasmic FunFam): Rodent cytosolic TrxR1s match the high‑MW Sec-containing subgroup; the FunFam constraint supports correct isoform mapping (URL: https://doi.org/10.1021/acs.jmedchem.4c00669, Sep 2024) (ardini2024the"doorstoppocket" pages 37-39).
• Exclusions and inclusions: Bacterial proteins with TR-like folds (e.g., YpdA/Bdr; TR-like FNRs) should be excluded unless the TrxR-specific signature is present, given risk of alternative physiological roles. Parasitic platyhelminths and nematodes with TGR are relevant to the TrxR family and possess thioredoxin-disulfide reductase activity, but TGRs are multifunctional; annotation remains valid for GO:0004791 (URLs: https://doi.org/10.1021/acs.jmedchem.4c00669; https://doi.org/10.1111/febs.14357) (ardini2024the"doorstoppocket" pages 1-3, brandstaedter2018kineticcharacterizationof pages 1-4).

6. Rule Logic Assessment

• Biological sense of domain combinations: Yes. IPR005982 anchors TrxR specificity; IPR008255 and IPR023753 capture catalytic chemistry and FAD/NADPH cofactor usage typical of TrxR. The CATH FunFams targeted to TrxR (and TrxR1 cytosolic) plus Eukaryota/Rattus filters add precision (ardini2024the"doorstoppocket" pages 1-3, ardini2024the"doorstoppocket" pages 37-39).
• Redundancy: IPR023753 is broad; its inclusion is supportive but not essential if IPR005982 and a TrxR-focused FunFam are present. However, its presence does little harm and reflects required cofactor-binding architecture (maia2023selenium—morethanjust pages 15-17, shoor2021thioredoxinreductasefrom pages 15-18).
• Potential false positives: Risk arises if only IPR008255 and IPR023753 are met without IPR005982 or TrxR-focused FunFams, due to related oxidoreductases (e.g., GR/Lpd/YpdA/FNR-like) sharing these features. The rule’s OR-logic branches using FunFams with Eukaryota/Rattus constraints appropriately mitigate this (shoor2021thioredoxinreductasefrom pages 15-18, shoor2021thioredoxinreductasefrom pages 12-15).

7. Recommendations

• Retain IPR005982 as the core determinant and require it whenever possible; treat annotations that lack IPR005982 but have only IPR008255 + IPR023753 as insufficient for GO:0004791 unless a TrxR-focused FunFam and appropriate taxonomy are also satisfied (shoor2021thioredoxinreductasefrom pages 15-18).
• Keep Eukaryota/Rattus constraints in FunFam-based branches; these reduce bacterial false positives from TR-like but functionally distinct oxidoreductases (shoor2021thioredoxinreductasefrom pages 15-18, shoor2021thioredoxinreductasefrom pages 12-15).
• Optionally enrich annotations with enabling terms when supported (e.g., FAD binding; thioredoxin binding) and with isoform/location terms only when orthogonal evidence exists (not from this rule alone) (ardini2024the"doorstoppocket" pages 1-3, ardini2024the"doorstoppocket" pages 37-39).
• Document in rule notes the recognized subfamily diversity (high‑MW Sec vs low‑MW Cys; TGR fusion) and the doorstop pocket as a conserved structural hallmark across the family, supporting confidence in TrxR family assignment when these signatures are present (ardini2024the"doorstoppocket" pages 1-3, ardini2024the"doorstoppocket" pages 37-39, maia2023selenium—morethanjust pages 15-17).

Cited sources (with URLs and dates)
• Ardini M et al. The “Doorstop Pocket” In Thioredoxin Reductases—An Unexpected Druggable Regulator of the Catalytic Machinery. Journal of Medicinal Chemistry. Sep 2024. URL: https://doi.org/10.1021/acs.jmedchem.4c00669 (ardini2024the"doorstoppocket" pages 1-3, ardini2024the"doorstoppocket" pages 37-39).
• Maia LB et al. Selenium—More than Just a Fortuitous Sulfur Substitute in Redox Biology. Molecules. Dec 2023. URL: https://doi.org/10.3390/molecules29010120 (maia2023selenium—morethanjust pages 15-17).
• Brandstaedter C et al. Kinetic characterization of wild‑type and mutant human thioredoxin glutathione reductase defines its reaction and regulatory mechanisms. FEBS J. Feb 2018. URL: https://doi.org/10.1111/febs.14357 (brandstaedter2018kineticcharacterizationof pages 1-4, brandstaedter2018kineticcharacterizationof pages 17-20).
• Shoor M et al. Thioredoxin reductase from Bacillus cereus exhibits distinct reduction and NADPH‑binding properties. FEBS Open Bio. Sep 2021. URL: https://doi.org/10.1002/2211-5463.13289 (shoor2021thioredoxinreductasefrom pages 12-15, shoor2021thioredoxinreductasefrom pages 15-18, shoor2021thioredoxinreductasefrom pages 22-29).

References

1. (ardini2024the"doorstoppocket" pages 1-3): Matteo Ardini, Sammy Y. Aboagye, Valentina Z. Petukhova, Irida Kastrati, Rodolfo Ippoliti, Gregory R. J. Thatcher, Pavel A. Petukhov, David L. Williams, and Francesco Angelucci. The "doorstop pocket" in thioredoxin reductases─an unexpected druggable regulator of the catalytic machinery. Journal of medicinal chemistry, 67:15947-15967, Sep 2024. URL: https://doi.org/10.1021/acs.jmedchem.4c00669, doi:10.1021/acs.jmedchem.4c00669. This article has 10 citations and is from a highest quality peer-reviewed journal.

2. (maia2023selenium—morethanjust pages 15-17): Luisa B. Maia, Biplab K. Maiti, Isabel Moura, and José J. G. Moura. Selenium—more than just a fortuitous sulfur substitute in redox biology. Molecules, 29:120, Dec 2023. URL: https://doi.org/10.3390/molecules29010120, doi:10.3390/molecules29010120. This article has 49 citations and is from a poor quality or predatory journal.

3. (shoor2021thioredoxinreductasefrom pages 12-15): Marita Shoor, Ingvild Gudim, Hans‐Petter Hersleth, and Marta Hammerstad. Thioredoxin reductase from <i>bacillus cereus</i> exhibits distinct reduction and nadph‐binding properties. FEBS Open Bio, 11:3019-3031, Sep 2021. URL: https://doi.org/10.1002/2211-5463.13289, doi:10.1002/2211-5463.13289. This article has 6 citations and is from a peer-reviewed journal.

4. (shoor2021thioredoxinreductasefrom pages 15-18): Marita Shoor, Ingvild Gudim, Hans‐Petter Hersleth, and Marta Hammerstad. Thioredoxin reductase from <i>bacillus cereus</i> exhibits distinct reduction and nadph‐binding properties. FEBS Open Bio, 11:3019-3031, Sep 2021. URL: https://doi.org/10.1002/2211-5463.13289, doi:10.1002/2211-5463.13289. This article has 6 citations and is from a peer-reviewed journal.

5. (ardini2024the"doorstoppocket" pages 37-39): Matteo Ardini, Sammy Y. Aboagye, Valentina Z. Petukhova, Irida Kastrati, Rodolfo Ippoliti, Gregory R. J. Thatcher, Pavel A. Petukhov, David L. Williams, and Francesco Angelucci. The "doorstop pocket" in thioredoxin reductases─an unexpected druggable regulator of the catalytic machinery. Journal of medicinal chemistry, 67:15947-15967, Sep 2024. URL: https://doi.org/10.1021/acs.jmedchem.4c00669, doi:10.1021/acs.jmedchem.4c00669. This article has 10 citations and is from a highest quality peer-reviewed journal.

6. (brandstaedter2018kineticcharacterizationof pages 1-4): Christina Brandstaedter, Karin Fritz‐Wolf, Stine Weder, Marina Fischer, Beate Hecker, Stefan Rahlfs, and Katja Becker. Kinetic characterization of wild‐type and mutant human thioredoxin glutathione reductase defines its reaction and regulatory mechanisms. The FEBS Journal, 285:542-558, Feb 2018. URL: https://doi.org/10.1111/febs.14357, doi:10.1111/febs.14357. This article has 27 citations.

7. (brandstaedter2018kineticcharacterizationof pages 17-20): Christina Brandstaedter, Karin Fritz‐Wolf, Stine Weder, Marina Fischer, Beate Hecker, Stefan Rahlfs, and Katja Becker. Kinetic characterization of wild‐type and mutant human thioredoxin glutathione reductase defines its reaction and regulatory mechanisms. The FEBS Journal, 285:542-558, Feb 2018. URL: https://doi.org/10.1111/febs.14357, doi:10.1111/febs.14357. This article has 27 citations.

8. (shoor2021thioredoxinreductasefrom pages 22-29): Marita Shoor, Ingvild Gudim, Hans‐Petter Hersleth, and Marta Hammerstad. Thioredoxin reductase from <i>bacillus cereus</i> exhibits distinct reduction and nadph‐binding properties. FEBS Open Bio, 11:3019-3031, Sep 2021. URL: https://doi.org/10.1002/2211-5463.13289, doi:10.1002/2211-5463.13289. This article has 6 citations and is from a peer-reviewed journal.

## Citations

1. shoor2021thioredoxinreductasefrom pages 15-18
2. shoor2021thioredoxinreductasefrom pages 12-15
3. brandstaedter2018kineticcharacterizationof pages 1-4
4. brandstaedter2018kineticcharacterizationof pages 17-20
5. shoor2021thioredoxinreductasefrom pages 22-29
6. https://doi.org/10.1021/acs.jmedchem.4c00669,
7. https://doi.org/10.3390/molecules29010120,
8. https://doi.org/10.1002/2211-5463.13289,
9. https://doi.org/10.3390/molecules29010120;
10. https://doi.org/10.1021/acs.jmedchem.4c00669
11. https://doi.org/10.1111/febs.14357,
12. https://doi.org/10.1021/acs.jmedchem.4c00669;
13. https://doi.org/10.1111/febs.14357
14. https://doi.org/10.3390/molecules29010120
15. https://doi.org/10.1002/2211-5463.13289