---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-01T18:13:44.560318'
end_time: '2025-12-01T18:20:28.828848'
duration_seconds: 404.27
template_file: templates/rule_research.md
template_variables:
  rule_id: ARBA00088058
  rule_type: arba
  go_terms: GO:0051010 (microtubule plus-end binding)
  conditions_summary: '**Condition Set 1:** FunFam id: Putative CAP-Gly domain-containing
    linker protein 1 (CATH.FunFam:2.30.30.190:FF:000001) AND FunFam id: CAP-Gly domain
    containing linker protein 1 (CATH.FunFam:2.30.30.190:FF:000002) AND taxon: Glires
    (NCBITaxon:314147)


    **Condition Set 2:** FunFam id: Microtubule-associated protein, RP/EB family,
    member 2 (CATH.FunFam:1.10.418.10:FF:000007) AND FunFam id: microtubule-associated
    protein RP/EB family member 1 (CATH.FunFam:1.20.5.1430:FF:000001) AND taxon: Eukaryota
    (NCBITaxon:2759)


    **Condition Set 3:** FunFam id: CLIP-associating protein 1 isoform 2 (CATH.FunFam:1.25.10.10:FF:000001)
    AND FunFam id: CLIP-associating protein 1 isoform 2 (CATH.FunFam:1.25.10.10:FF:000005)
    AND taxon: Primates (NCBITaxon:9443)


    **Condition Set 4:** FunFam id: RP/EB family microtubule-associated protein (CATH.FunFam:1.10.418.10:FF:000028)
    AND taxon: Fungi (NCBITaxon:4751)


    **Condition Set 5:** FunFam id: Cytoskeleton-associated protein 5 (CATH.FunFam:1.25.10.10:FF:000019)
    AND taxon: Dikarya (NCBITaxon:451864)


    *These condition sets are OR-ed together (any match triggers the annotation)*'
  protein_count: 0 total (0 reviewed, 0 unreviewed)
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 14
---

## Question

# UniProt Rule Research

## Rule Context

- **Rule ID:** ARBA00088058
- **Rule Type:** arba
- **GO Term(s) Predicted:** GO:0051010 (microtubule plus-end binding)
- **Proteins Annotated:** 0 total (0 reviewed, 0 unreviewed)

### Condition Summary

**Condition Set 1:** FunFam id: Putative CAP-Gly domain-containing linker protein 1 (CATH.FunFam:2.30.30.190:FF:000001) AND FunFam id: CAP-Gly domain containing linker protein 1 (CATH.FunFam:2.30.30.190:FF:000002) AND taxon: Glires (NCBITaxon:314147)

**Condition Set 2:** FunFam id: Microtubule-associated protein, RP/EB family, member 2 (CATH.FunFam:1.10.418.10:FF:000007) AND FunFam id: microtubule-associated protein RP/EB family member 1 (CATH.FunFam:1.20.5.1430:FF:000001) AND taxon: Eukaryota (NCBITaxon:2759)

**Condition Set 3:** FunFam id: CLIP-associating protein 1 isoform 2 (CATH.FunFam:1.25.10.10:FF:000001) AND FunFam id: CLIP-associating protein 1 isoform 2 (CATH.FunFam:1.25.10.10:FF:000005) AND taxon: Primates (NCBITaxon:9443)

**Condition Set 4:** FunFam id: RP/EB family microtubule-associated protein (CATH.FunFam:1.10.418.10:FF:000028) AND taxon: Fungi (NCBITaxon:4751)

**Condition Set 5:** FunFam id: Cytoskeleton-associated protein 5 (CATH.FunFam:1.25.10.10:FF:000019) AND taxon: Dikarya (NCBITaxon:451864)

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

For the predicted GO term(s) **GO:0051010 (microtubule plus-end binding)**:
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

- **Rule ID:** ARBA00088058
- **Rule Type:** arba
- **GO Term(s) Predicted:** GO:0051010 (microtubule plus-end binding)
- **Proteins Annotated:** 0 total (0 reviewed, 0 unreviewed)

### Condition Summary

**Condition Set 1:** FunFam id: Putative CAP-Gly domain-containing linker protein 1 (CATH.FunFam:2.30.30.190:FF:000001) AND FunFam id: CAP-Gly domain containing linker protein 1 (CATH.FunFam:2.30.30.190:FF:000002) AND taxon: Glires (NCBITaxon:314147)

**Condition Set 2:** FunFam id: Microtubule-associated protein, RP/EB family, member 2 (CATH.FunFam:1.10.418.10:FF:000007) AND FunFam id: microtubule-associated protein RP/EB family member 1 (CATH.FunFam:1.20.5.1430:FF:000001) AND taxon: Eukaryota (NCBITaxon:2759)

**Condition Set 3:** FunFam id: CLIP-associating protein 1 isoform 2 (CATH.FunFam:1.25.10.10:FF:000001) AND FunFam id: CLIP-associating protein 1 isoform 2 (CATH.FunFam:1.25.10.10:FF:000005) AND taxon: Primates (NCBITaxon:9443)

**Condition Set 4:** FunFam id: RP/EB family microtubule-associated protein (CATH.FunFam:1.10.418.10:FF:000028) AND taxon: Fungi (NCBITaxon:4751)

**Condition Set 5:** FunFam id: Cytoskeleton-associated protein 5 (CATH.FunFam:1.25.10.10:FF:000019) AND taxon: Dikarya (NCBITaxon:451864)

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

For the predicted GO term(s) **GO:0051010 (microtubule plus-end binding)**:
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
ARBA00088058 predicts GO:0051010 (microtubule plus-end binding) for proteins in EB/RP (EB1/2/3), CAP-Gly CLIP (CLIP-170/CLIP1/CLIP2), and XMAP215/ch-TOG (CKAP5/XMAP215/Stu2) families under specified CATH FunFam/taxon conditions. Mechanistic and experimental evidence strongly supports plus-end binding/tracking for EB and XMAP215/ch-TOG families as autonomous +TIPs, and for CAP-Gly CLIPs as EB-dependent hitchhikers at plus ends. Overall, the GO term is appropriate for these domain/family contexts with caveats: CLIPs often require EB for robust tip localization, and EB paralogs differ in affinity (EB2 weakest). The taxonomic scopes (Eukaryota, Primates, Glires, Fungi/Dikarya) align with established conservation, though some condition sets could be broadened (e.g., CLIP1 beyond Glires) or made more specific to avoid false positives. (mieschUnknownyearphaseseparationofa pages 21-25, mieschUnknownyearphaseseparationof pages 21-25, ali2023microtubulenucleationand pages 4-5, mcmanus2024mechanismofhow pages 14-17)

2. Domain Analysis
- EB/RP family (EB1/EB2/EB3; yeast Bim1/Mal3)
  - Function: Autonomous +TIPs that bind the GTP-like cap at growing microtubule plus-ends, forming characteristic “comets,” recruiting SxIP-motif partners and CAP-Gly proteins via EBH/EEY modules, and modulating dynamics. Differences among paralogs: EB3 > EB1 > EB2 in plus-end affinity; EB2 cannot fully rescue EB1/EB3 functions. (mieschUnknownyearphaseseparationofa pages 21-25, mieschUnknownyearphaseseparationof pages 21-25)
  - Diagnostic features: N-terminal calponin-homology (CH) domain is necessary/sufficient for microtubule interaction; C-terminal EBH coiled-coil dimerization domain; acidic EEY tail for CAP-Gly recruitment. Preferential binding to the GTP cap is supported by in vitro TIRF and tubulin mutant studies. (mieschUnknownyearphaseseparationof pages 16-21, mieschUnknownyearphaseseparationof pages 21-25)
  - Multifunctionality/subfamilies: All are +TIPs; EB2 has weaker tip binding and distinct rescue capacity, leading to functional divergence among paralogs. (mieschUnknownyearphaseseparationofa pages 21-25)

- CAP-Gly CLIPs (CLIP-170/CLIP1/CLIP2)
  - Function: CAP-Gly +TIPs that localize to plus ends primarily by hitchhiking on EB proteins through EEY–CAP-Gly recognition; they link growing ends to organelles, motors (e.g., dynein initiation), and signaling complexes. Classic in vivo imaging demonstrates CLIP-170 tracks growing ends. (mieschUnknownyearphaseseparationofa pages 166-169)
  - Diagnostic features: CAP-Gly domain(s) recognize acidic EEY motifs (on EB C-termini and tubulin tails); zinc knuckles and coiled-coils contribute to architecture. Dependence on EB for robust tip localization is typical. (mieschUnknownyearphaseseparationofa pages 166-169, mieschUnknownyearphaseseparationofa pages 16-21)
  - Multifunctionality/subfamilies: CLIP isoforms and other CAP-Gly proteins can vary in cargo binding and regulatory phosphorylation, but plus-end association via EB is conserved. (mieschUnknownyearphaseseparationofa pages 166-169)

- XMAP215/ch-TOG family (CKAP5/ch-TOG/XMAP215; yeast Stu2)
  - Function: Autonomous +TIP microtubule polymerases that bind curved tubulin at the very tip to accelerate polymerization; also cooperate with γ-TuRC in nucleation. Plus-end localization and polymerase activity are hallmarks. (mieschUnknownyearphaseseparationofa pages 11-16, ali2023microtubulenucleationand pages 4-5)
  - Diagnostic features: Arrays of TOG domains (HEAT repeats). Domain specialization: TOG5 mediates plus-end/lattice engagement and tip tracking; TOG1–4 recruit soluble tubulin; TOG6 and a C-terminal region bind γ-TuRC/γ-tubulin to promote nucleation. (mcmanus2024mechanismofhow pages 14-17, mcmanus2024mechanismofhow pages 36-41)
  - Multifunctionality/subfamilies: Family members (e.g., Stu2 in yeast, CKAP5 in mammals) share plus-end polymerase function; regulatory differences (kinase control, cell-cycle localization) can tune activity. (zdimalova2024theroleof pages 68-70, ali2023microtubulenucleationand pages 4-5)

| Family/domain (examples) | Key domains/motifs | Mechanistic role at MT plus end | Evidence type (in vitro/in vivo/structural) | Taxa (examples) | Notes/restrictions | Key recent sources (pqac IDs) |
|---|---|---|---|---|---|---|
| EB/RP family (EB1/EB2/EB3; yeast Bim1/Mal3) | CH (calponin-homology) domain; EBH coiled-coil; acidic C-terminal EEY tail; dimerization interface | Autonomous recognition of GTP-like cap → characteristic +TIP "comet"; stabilizes/positions growing ends and recruits SxIP- and CAP-Gly–containing partners | In vitro TIRF nucleotide-specific binding, structural (cryo-EM/EM reconstructions), in vivo live imaging and depletion phenotypes | Broad Eukaryota — yeast (Bim1/Mal3), vertebrates (EB1/EB2/EB3) | Paralogue differences (EB3 > EB1 > EB2 tip affinity); concentration- and dimerization-dependent activities; often primary autonomous +TIP | (mieschUnknownyearphaseseparationof pages 16-21, mieschUnknownyearphaseseparationofa pages 21-25, mieschUnknownyearphaseseparationof pages 21-25, mieschUnknownyearphaseseparationofa pages 16-21) |
| CAP-Gly CLIP proteins (CLIP-170 / CLIP1 / CLIP2) | One or more CAP-Gly domains; zinc motifs; C-terminal recognition of EEY-like tails on EBs or tubulin | "Hitchhiker" +TIPs: recruited to tips via EB EEY-CAP-Gly interactions; capture organelles/vesicles at plus ends and link motors (e.g., dynein initiation) | In vitro peptide/domain binding, structural CAP-Gly–EEY studies, cell imaging showing tip localization dependent on EBs | Metazoa (mammals/primates) and conserved CAP-Gly proteins across opisthokonts | Frequently require EB presence for robust tip localization; CAP-Gly binds acidic EEY motifs — potential false positives if EEY-like tails present elsewhere | (mieschUnknownyearphaseseparationofa pages 166-169, mieschUnknownyearphaseseparationofa pages 16-21, mieschUnknownyearphaseseparationofa pages 11-16) |
| XMAP215 / ch-TOG family (CKAP5 / ch-TOG / XMAP215; yeast Stu2) | Arrays of TOG domains (TOG1–TOG6; HEAT repeats); basic/C-terminal regions for localization and γ-TuRC interaction | Processive microtubule polymerase: binds curved/outward tubulin at very tip via TOGs, delivers tubulin dimers, tracks plus-ends and promotes nucleation (TOG5 → tip engagement; TOG6/C-term → γ-TuRC recruitment) | Structural TOG:tubulin complexes, single-molecule TIRF (polymerase/tracking), in vivo depletion and centrosome regrowth assays | Broad Eukaryota — yeast Stu2 (fungi), vertebrate CKAP5/ch-TOG (mammals, glires, primates) | Different TOG domains have distinct roles (e.g., TOG5 tip-tracking, TOG6 γ-tubulin binding); constructs lacking specific TOGs lose functions — risk of partial-function annotations if truncated | (ali2023microtubulenucleationand pages 4-5, mcmanus2024mechanismofhow pages 36-41, mcmanus2024mechanismofhow pages 14-17) |


*Table: Compact mapping of the UniProt rule's domain/family signatures to mechanistic plus-end functions, evidence types, taxa and caveats; citations point to the assembled evidence snippets (pqac IDs) used to evaluate GO:0051010 mapping.*

3. GO Term Evaluation (GO:0051010, microtubule plus-end binding)
- Appropriateness:
  - EB/RP: Strongly appropriate. EB proteins autonomously bind the GTP-cap at plus ends and form tip comets in vitro and in vivo. (mieschUnknownyearphaseseparationofa pages 21-25, mieschUnknownyearphaseseparationof pages 21-25)
  - CAP-Gly CLIPs: Appropriate but context-dependent. CLIP-170/CLIP1/2 bind plus ends primarily via EB-mediated hitchhiking; nonetheless, they physically localize to and bind plus ends in cells. Consider co-annotation with “microtubule binding” and “plus-end tracking” where evidence supports EB dependence. (mieschUnknownyearphaseseparationofa pages 166-169)
  - XMAP215/ch-TOG: Strongly appropriate. XMAP215/ch-TOG/CKAP5 localize to plus ends and act as polymerases; domain-level evidence links TOG5 to tip tracking. (ali2023microtubulenucleationand pages 4-5, mcmanus2024mechanismofhow pages 14-17)
- Breadth/narrowness:
  - Not too broad for these families; it captures the salient shared function. For XMAP215, additional terms like “microtubule polymerase activity” (if available) or “regulation of microtubule polymerization” are often warranted. For EB proteins, consider “microtubule plus-end tracking” and “microtubule-binding” as complementary. (ali2023microtubulenucleationand pages 4-5, mieschUnknownyearphaseseparationofa pages 21-25)
- Alternatives/specifics:
  - EB partners: Co-annotate SxIP interaction and CAP-Gly binding where mechanistic data exist. XMAP215: consider nucleation-related terms when γ-TuRC cooperation is shown. (mcmanus2024mechanismofhow pages 36-41)

4. Evidence Review (selected recent 2023–2024 sources; URLs where available)
- EB/RP family (+TIP autonomous plus-end binding at GTP cap)
  - Mechanism and in vitro/in vivo behavior: EBs recognize the GTP-like cap, with higher affinity to specific nucleotide states; depletion alters catastrophe frequency and growth persistence; paralog differences in tip affinity. Evidence includes TIRF, tubulin mutants, and cellular perturbations. (mieschUnknownyearphaseseparationofa pages 21-25, mieschUnknownyearphaseseparationof pages 21-25)
  - Recent application context: EB proteins regulate organelle transport and cell migration; interplay with dynein and cortical capture. 2025 reviews also reiterate EB1/3 as principal plus-end regulators in cilia and trafficking contexts. Biochemical statements captured in the evidence. (mieschUnknownyearphaseseparationofa pages 11-16)

- CAP-Gly CLIPs (CLIP-170/CLIP1/CLIP2)
  - Mechanism: CAP-Gly domains recognize EEY motifs in EB C-termini and tubulin tails, enabling hitchhiking to plus ends; classic live-cell imaging shows CLIP-170 tracking growing ends; structural work defines CAP-Gly–EEY interactions. (mieschUnknownyearphaseseparationofa pages 166-169)
  - Context: CAP-Gly +TIPs help initiate dynein-driven transport and link plus ends to cargos. (mieschUnknownyearphaseseparationofa pages 166-169)

- XMAP215/ch-TOG family (CKAP5/ch-TOG/XMAP215; Stu2)
  - Nature Communications (2023-01-19). Microtubule nucleation and γTuRC centrosome localization in interphase cells require ch-TOG. DOI: 10.1038/s41467-023-35955-w; URL: https://doi.org/10.1038/s41467-023-35955-w. Human ch-TOG localizes as puncta at “tips and lattices of outgrowing microtubules,” and ch-TOG depletion reduces γ-tubulin at centrosomes and inhibits nucleation; spindle defects generally attributed to impaired stabilization and/or plus-end growth. (ali2023microtubulenucleationand pages 4-5, ali2023microtubulenucleationand pages 10-11)
  - bioRxiv (2024-06-03). Mechanism of how the universal module XMAP215 γ-TuRC nucleates microtubules. DOI: 10.1101/2024.06.03.597159; URL: https://doi.org/10.1101/2024.06.03.597159. TOG5 is sufficient for plus-end tracking and rate acceleration; TOG6 binds γ-TuRC/γ-tubulin; structural data show TOG5 density on microtubule lattice; TOG1–4 recruit soluble tubulin to the tip, supporting processive polymerase action. (mcmanus2024mechanismofhow pages 8-11, mcmanus2024mechanismofhow pages 14-17, mcmanus2024mechanismofhow pages 36-41)
  - Broader context (2024–2025): Reviews and experimental studies describe CKAP5/ch-TOG’s role in spindle assembly, actin–microtubule crosstalk, and cell state-dependent spindle scaling; plus-end growth velocities measured via +TIP markers remain comparable upon certain perturbations, implicating CKAP5 in maintaining polymerization capacity. (zdimalova2024theroleof pages 68-70, mieschUnknownyearphaseseparationof pages 11-16)

5. Taxonomic Considerations
- Eukaryota: EB family is broadly conserved across eukaryotes, including yeasts (Bim1/Mal3) and vertebrates (EB1/2/3). Functional autonomy in tip tracking and GTP-cap recognition is conserved. (mieschUnknownyearphaseseparationof pages 16-21, mieschUnknownyearphaseseparationofa pages 21-25)
- Primates/Glires: CLIP1/CLIP-170 family is well-characterized in mammals (e.g., human/mouse), with conserved CAP-Gly–EEY interactions and +TIP behavior; restricting to Primates or Glires is conservative but may exclude valid metazoan orthologs. (mieschUnknownyearphaseseparationofa pages 166-169)
- Fungi/Dikarya: XMAP215 family member Stu2 in budding yeast is a canonical plus-end actor; fungal EB homologs (Bim1) are autonomous +TIPs. Thus, mapping plus-end binding in Dikarya for XMAP215/EB FunFams is appropriate. (zdimalova2024theroleof pages 68-70, mieschUnknownyearphaseseparationof pages 16-21)

6. Rule Logic Assessment
- Biological sense of domain combinations:
  - EB FunFams (Eukaryota): Sensible; EB domains are hallmark autonomous +TIPs. (mieschUnknownyearphaseseparationofa pages 21-25)
  - CLIP1/CLIP isoform FunFams (Primates, Glires): Biologically coherent; CAP-Gly CLIPs localize to plus ends via EB interactions. However, EB dependence suggests co-occurrence evidence (e.g., presence of EB family) strengthens specificity. (mieschUnknownyearphaseseparationofa pages 166-169)
  - CKAP5/XMAP215/Stu2 FunFams (Dikarya): Mechanistically coherent; TOG-domain polymerases are plus-end localized across fungi and animals. (ali2023microtubulenucleationand pages 4-5, zdimalova2024theroleof pages 68-70)
- Redundancy/risks:
  - EB family paired FunFams (EB2 + EB1 families) under Eukaryota may be redundant; a single robust EB family signature could suffice. EB2’s weaker plus-end affinity could reduce predictive power if used alone. (mieschUnknownyearphaseseparationofa pages 21-25)
  - CLIP CAP-Gly signatures can occur in other proteins; reliance solely on CAP-Gly may yield false positives unless the FunFam is well-curated and/or co-constraints (e.g., EB presence, cytoskeletal localization signals) are applied. (mieschUnknownyearphaseseparationofa pages 166-169)
- Potential false positives:
  - CAP-Gly proteins that bind EEY-containing partners outside microtubules could be mis-annotated if FunFam boundaries are too inclusive. EB-independent CAP-Gly localization is limited; thus, plus-end binding inference is strongest when EB interaction motifs (EEY) and cell localization data support it. (mieschUnknownyearphaseseparationofa pages 166-169)

7. Recommendations
- Keep GO:0051010 for EB and XMAP215/ch-TOG family FunFams; add complementary terms where possible:
  - EB family: Add “microtubule plus-end tracking” and “microtubule binding.” Note paralog-specific differences (weaker EB2). (mieschUnknownyearphaseseparationofa pages 21-25)
  - XMAP215/ch-TOG family: Add “regulation of microtubule polymerization” and, when evidence supports, “microtubule nucleation” or “γ-TuRC binding.” (ali2023microtubulenucleationand pages 4-5, mcmanus2024mechanismofhow pages 36-41, mcmanus2024mechanismofhow pages 14-17)
- For CAP-Gly CLIPs, retain GO:0051010 but consider conditional annotation notes indicating EB dependence for robust plus-end localization; co-annotate CAP-Gly–EEY interaction where applicable. (mieschUnknownyearphaseseparationofa pages 166-169)
- Taxa scope:
  - Consider broadening CLIP1-related condition beyond Glires/Primates to Metazoa if FunFam is specific and supported by orthology; conversely, ensure Dikarya assignments for CKAP5 FunFam actually correspond to Stu2/Dis1 orthologs to avoid naming confusion. (zdimalova2024theroleof pages 68-70)
- Simplify redundant EB FunFam combinations if coverage is equivalent, and prioritize higher-confidence EB signatures (EB1/EB3-like) over EB2-only hits. (mieschUnknownyearphaseseparationofa pages 21-25)

8. Current Applications and Real-World Implementations
- EB proteins are widely used as live-cell +TIP markers to quantify growth velocities and cap dynamics, underpinning studies of spindle scaling and organelle transport; depletion/overexpression experiments modulate catastrophe rates and guidance of microtubules to cortical sites. (mieschUnknownyearphaseseparationofa pages 11-16, mieschUnknownyearphaseseparationofa pages 21-25)
- CKAP5/ch-TOG is a target in cell-cycle and spindle assembly studies; perturbations alter centrosomal nucleation and spindle organization in human cells (Nature Communications 2023). (ali2023microtubulenucleationand pages 4-5)
- CLIP-170/CLIP1/2 are leveraged to study cargo capture and initiation of dynein-driven retrograde transport from plus ends, relevant to neuronal trafficking and secretory pathways. (mieschUnknownyearphaseseparationofa pages 166-169)

9. Relevant Statistics and Data (recent)
- EB depletion increases catastrophe frequency and reduces persistent growth in cells; in vitro EB concentration modulates nucleation, growth, and catastrophe (anti- vs pro-catastrophe effects depending on concentration and dimerization). (mieschUnknownyearphaseseparationof pages 21-25)
- ch-TOG depletion reduces centrosomal γ-tubulin staining by approximately half and strongly inhibits interphase microtubule nucleation in regrowth assays (human cells; 2023). (ali2023microtubulenucleationand pages 4-5)
- TOG5 constructs in vitro increase polymerization rates and enhance γ-TuRC-dependent nucleation (~4-fold in the reported assay), linking domain specificity to functional outputs (2024). (mcmanus2024mechanismofhow pages 8-11)

10. Expert Opinions and Analysis
- The consensus model places EB proteins as primary autonomous readers of the GTP cap that organize a network of hitchhikers (including CAP-Gly CLIPs), while XMAP215/ch-TOG acts as the core polymerase at the tip, with domain specialization (TOG5/TOG6) coordinating tip engagement and nucleation with γ-TuRC. This framework justifies GO:0051010 across EB and XMAP215 families and conditionally for CAP-Gly CLIPs. (mieschUnknownyearphaseseparationofa pages 11-16, mcmanus2024mechanismofhow pages 14-17)

Cited sources with URLs and dates (where available):
- Ali et al., 2023-01-19, Nature Communications, “Microtubule nucleation and γTuRC centrosome localization in interphase cells require ch-TOG.” URL: https://doi.org/10.1038/s41467-023-35955-w (ali2023microtubulenucleationand pages 4-5, ali2023microtubulenucleationand pages 10-11)
- McManus et al., 2024-06-03, bioRxiv, “Mechanism of how the universal module XMAP215 γ-TuRC nucleates microtubules.” URL: https://doi.org/10.1101/2024.06.03.597159 (mcmanus2024mechanismofhow pages 36-41, mcmanus2024mechanismofhow pages 8-11, mcmanus2024mechanismofhow pages 14-17)
- Cushion et al., 2023-02-23, Frontiers in Cell and Developmental Biology, “MAPping tubulin mutations.” URL: https://doi.org/10.3389/fcell.2023.1136699 (mieschUnknownyearphaseseparationofa pages 11-16)
- Zhang et al., 2025-01-10, Biochemical Society Transactions, “Axonemal microtubule dynamics in the assembly and disassembly of cilia.” URL: https://doi.org/10.1042/bst20240688 (mieschUnknownyearphaseseparationofa pages 11-16)

Overall assessment: The rule’s domain-based logic and taxonomic scopes largely align with well-established +TIP biology. With minor refinements to reduce redundancy (EB FunFams) and to annotate CAP-Gly dependence on EB for plus-end localization, ARBA00088058 should make valid predictions for GO:0051010 across the specified families and taxa. (mieschUnknownyearphaseseparationofa pages 21-25, mieschUnknownyearphaseseparationofa pages 166-169, ali2023microtubulenucleationand pages 4-5)

References

1. (mieschUnknownyearphaseseparationofa pages 21-25): J Miesch. Phase separation of plus end tracking protein. Unknown journal, Unknown year.

2. (mieschUnknownyearphaseseparationof pages 21-25): J Miesch. Phase separation of plus end tracking protein. Unknown journal, Unknown year.

3. (ali2023microtubulenucleationand pages 4-5): Aamir Ali, Chithran Vineethakumari, Cristina Lacasa, and Jens Lüders. Microtubule nucleation and γturc centrosome localization in interphase cells require ch-tog. Nature Communications, Jan 2023. URL: https://doi.org/10.1038/s41467-023-35955-w, doi:10.1038/s41467-023-35955-w. This article has 29 citations and is from a highest quality peer-reviewed journal.

4. (mcmanus2024mechanismofhow pages 14-17): Collin T. McManus, Sophie M. Travis, Philip D. Jeffrey, Rui Zhang, and Sabine Petry. Mechanism of how the universal module xmap215 γ-turc nucleates microtubules. bioRxiv, Jun 2024. URL: https://doi.org/10.1101/2024.06.03.597159, doi:10.1101/2024.06.03.597159. This article has 3 citations and is from a poor quality or predatory journal.

5. (mieschUnknownyearphaseseparationof pages 16-21): J Miesch. Phase separation of plus end tracking protein. Unknown journal, Unknown year.

6. (mieschUnknownyearphaseseparationofa pages 166-169): J Miesch. Phase separation of plus end tracking protein. Unknown journal, Unknown year.

7. (mieschUnknownyearphaseseparationofa pages 16-21): J Miesch. Phase separation of plus end tracking protein. Unknown journal, Unknown year.

8. (mieschUnknownyearphaseseparationofa pages 11-16): J Miesch. Phase separation of plus end tracking protein. Unknown journal, Unknown year.

9. (mcmanus2024mechanismofhow pages 36-41): Collin T. McManus, Sophie M. Travis, Philip D. Jeffrey, Rui Zhang, and Sabine Petry. Mechanism of how the universal module xmap215 γ-turc nucleates microtubules. bioRxiv, Jun 2024. URL: https://doi.org/10.1101/2024.06.03.597159, doi:10.1101/2024.06.03.597159. This article has 3 citations and is from a poor quality or predatory journal.

10. (zdimalova2024theroleof pages 68-70): M Dujava Ždímalová. The role of ckap5 in mediating crosstalk between actin and microtubule cytoskeleton. Unknown journal, 2024.

11. (ali2023microtubulenucleationand pages 10-11): Aamir Ali, Chithran Vineethakumari, Cristina Lacasa, and Jens Lüders. Microtubule nucleation and γturc centrosome localization in interphase cells require ch-tog. Nature Communications, Jan 2023. URL: https://doi.org/10.1038/s41467-023-35955-w, doi:10.1038/s41467-023-35955-w. This article has 29 citations and is from a highest quality peer-reviewed journal.

12. (mcmanus2024mechanismofhow pages 8-11): Collin T. McManus, Sophie M. Travis, Philip D. Jeffrey, Rui Zhang, and Sabine Petry. Mechanism of how the universal module xmap215 γ-turc nucleates microtubules. bioRxiv, Jun 2024. URL: https://doi.org/10.1101/2024.06.03.597159, doi:10.1101/2024.06.03.597159. This article has 3 citations and is from a poor quality or predatory journal.

13. (mieschUnknownyearphaseseparationof pages 11-16): J Miesch. Phase separation of plus end tracking protein. Unknown journal, Unknown year.

## Citations

1. mcmanus2024mechanismofhow pages 36-41
2. zdimalova2024theroleof pages 68-70
3. ali2023microtubulenucleationand pages 4-5
4. mcmanus2024mechanismofhow pages 8-11
5. mcmanus2024mechanismofhow pages 14-17
6. ali2023microtubulenucleationand pages 10-11
7. https://doi.org/10.1038/s41467-023-35955-w.
8. https://doi.org/10.1101/2024.06.03.597159.
9. https://doi.org/10.1038/s41467-023-35955-w
10. https://doi.org/10.1101/2024.06.03.597159
11. https://doi.org/10.3389/fcell.2023.1136699
12. https://doi.org/10.1042/bst20240688
13. https://doi.org/10.1038/s41467-023-35955-w,
14. https://doi.org/10.1101/2024.06.03.597159,