---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-11-25T18:17:21.323218'
end_time: '2025-11-25T18:25:14.934627'
duration_seconds: 473.61
template_file: templates/rule_research.md
template_variables:
  rule_id: ARBA00089174
  rule_type: arba
  go_terms: GO:1990845 (adaptive thermogenesis)
  conditions_summary: '**Condition Set 1:** FunFam id: N-fatty-acyl-amino acid synthase/hydrolase
    PM20D1 (CATH.FunFam:1.10.150.900:FF:000003) AND FunFam id: N-fatty-acyl-amino
    acid synthase/hydrolase PM20D1 (CATH.FunFam:3.40.630.10:FF:000027) AND taxon:
    Eukaryota (NCBITaxon:2759)


    **Condition Set 2:** FunFam id: Transient receptor potential cation channel subfamily
    V member 1 (CATH.FunFam:1.10.287.70:FF:000074) AND FunFam id: Transient receptor
    potential cation channel subfamily V member 1 (CATH.FunFam:1.25.40.20:FF:000018)
    AND taxon: Mus (NCBITaxon:862507)


    *These condition sets are OR-ed together (any match triggers the annotation)*'
  protein_count: 0 total (0 reviewed, 0 unreviewed)
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 10
---

## Question

# UniProt Rule Research

## Rule Context

- **Rule ID:** ARBA00089174
- **Rule Type:** arba
- **GO Term(s) Predicted:** GO:1990845 (adaptive thermogenesis)
- **Proteins Annotated:** 0 total (0 reviewed, 0 unreviewed)

### Condition Summary

**Condition Set 1:** FunFam id: N-fatty-acyl-amino acid synthase/hydrolase PM20D1 (CATH.FunFam:1.10.150.900:FF:000003) AND FunFam id: N-fatty-acyl-amino acid synthase/hydrolase PM20D1 (CATH.FunFam:3.40.630.10:FF:000027) AND taxon: Eukaryota (NCBITaxon:2759)

**Condition Set 2:** FunFam id: Transient receptor potential cation channel subfamily V member 1 (CATH.FunFam:1.10.287.70:FF:000074) AND FunFam id: Transient receptor potential cation channel subfamily V member 1 (CATH.FunFam:1.25.40.20:FF:000018) AND taxon: Mus (NCBITaxon:862507)

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

For the predicted GO term(s) **GO:1990845 (adaptive thermogenesis)**:
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

- **Rule ID:** ARBA00089174
- **Rule Type:** arba
- **GO Term(s) Predicted:** GO:1990845 (adaptive thermogenesis)
- **Proteins Annotated:** 0 total (0 reviewed, 0 unreviewed)

### Condition Summary

**Condition Set 1:** FunFam id: N-fatty-acyl-amino acid synthase/hydrolase PM20D1 (CATH.FunFam:1.10.150.900:FF:000003) AND FunFam id: N-fatty-acyl-amino acid synthase/hydrolase PM20D1 (CATH.FunFam:3.40.630.10:FF:000027) AND taxon: Eukaryota (NCBITaxon:2759)

**Condition Set 2:** FunFam id: Transient receptor potential cation channel subfamily V member 1 (CATH.FunFam:1.10.287.70:FF:000074) AND FunFam id: Transient receptor potential cation channel subfamily V member 1 (CATH.FunFam:1.25.40.20:FF:000018) AND taxon: Mus (NCBITaxon:862507)

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

For the predicted GO term(s) **GO:1990845 (adaptive thermogenesis)**:
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

Plan and approach: I first defined the biological context for the GO term and the two condition sets (PM20D1 FunFams and TRPV1 FunFams) and then gathered evidence on mechanistic links to adaptive thermogenesis, prioritizing recent work. I assessed domain specificity, taxonomic scope, and rule logic, and compiled a compact evidence table to support the final recommendations.

1. Executive Summary
This rule attempts to assign GO:1990845 (adaptive thermogenesis) based on two alternative domain/FunFam conditions: (i) PM20D1 FunFams across Eukaryota, and (ii) TRPV1 FunFams restricted to Mus. The second condition (TRPV1 in Mus) has stronger direct evidence for a role in adipose thermogenesis via PRDM16/UCP1-dependent pathways in mice, including at thermoneutrality; however, the effect is context-dependent and mediated by both peripheral adipose and possibly neuronal mechanisms, warranting careful scope and qualifiers (e.g., regulation of thermogenesis) (baskaran2017trpv1activationcounters pages 6-11, baskaran2024trpv1activationantagonizes pages 1-2, baskaran2024trpv1activationantagonizes pages 8-10, baskaran2017trpv1activationcounters pages 19-22, baskaran2024trpv1activationantagonizes pages 10-12, baskaran2024trpv1activationantagonizes pages 15-16, baskaran2017trpv1activationcounters pages 29-36, baskaran2024trpv1activationantagonizes pages 14-15). The first condition (PM20D1 FunFams) is supported by data that PM20D1 controls circulating N-acyl amino acids that can uncouple mitochondria and promote UCP1-independent thermogenesis and cold tolerance in mice; emerging human genetic associations exist. Yet these data are primarily in mammalian contexts, and broad Eukaryota propagation risks false positives in taxa lacking adaptive thermogenesis (simoes2025bidirectionalshiftsin pages 1-2, sponton2018multifacetedrolesof pages 2-3). Overall, the rule’s biology is plausible but should be taxonomically restricted (at least Mammalia) and the GO assignment should likely be “regulation of adaptive thermogenesis” rather than direct participation, with additional qualifiers for evidence context.

2. Domain Analysis
- PM20D1 FunFams (N-fatty-acyl-amino acid synthase/hydrolase, M20 family): PM20D1 is a secreted bidirectional enzyme regulating tissue and circulating levels of N-acyl amino acids (NAAs). NAAs can bind mitochondria and act as uncouplers of respiration in brown adipocytes independent of UCP1, thereby modulating thermogenesis. Mouse data show that altering PM20D1 expression bidirectionally impacts cold tolerance and BAT respiration, and that a BALB/c promoter variant elevates Pm20d1 expression and increases UCP1-independent BAT mitochondrial respiration; human promoter variants associate with BMI/metabolic syndrome. These findings support a role for the PM20D1 family in thermogenic regulation via lipid mediator production. However, the M20 peptidase superfamily is multifunctional with subfamilies of different enzymatic specificities; PM20D1’s thermogenesis linkage appears specific to this enzyme rather than diagnostic of the whole superfamily (simoes2025bidirectionalshiftsin pages 1-2, sponton2018multifacetedrolesof pages 2-3). URL and date: Molecular Medicine (2025-08), https://doi.org/10.1186/s10020-025-01345-9 (simoes2025bidirectionalshiftsin pages 1-2).
- TRPV1 FunFams (TRP channel subfamily V member 1): TRPV1 is a heat/capsaicin-gated cation channel expressed in adipose tissue and other sites. In mice, TRPV1 activation (e.g., dietary capsaicin) increases BAT/iWAT thermogenic programming via Ca2+→CaMKII/AMPK→SIRT1 activation leading to PRDM16 deacetylation and UCP1 upregulation, protecting against diet-induced obesity. Evidence includes genetic TRPV1 knockout (loss of effect), and at thermoneutrality, capsaicin’s anti-obesity action requires both PRDM16 and UCP1. This supports a TRPV1→PRDM16→UCP1 axis in murine adipose thermogenesis, though context (ambient vs thermoneutrality) and tissue specificity are important (baskaran2017trpv1activationcounters pages 6-11, baskaran2024trpv1activationantagonizes pages 1-2, baskaran2024trpv1activationantagonizes pages 8-10, baskaran2017trpv1activationcounters pages 19-22, baskaran2024trpv1activationantagonizes pages 10-12, baskaran2024trpv1activationantagonizes pages 15-16, baskaran2017trpv1activationcounters pages 29-36, baskaran2024trpv1activationantagonizes pages 14-15). URLs and dates: Int J Obes (2017-01), https://doi.org/10.1038/ijo.2017.16 (baskaran2017trpv1activationcounters pages 6-11); Pharmaceuticals (2024-08), https://doi.org/10.3390/ph17081098 (baskaran2024trpv1activationantagonizes pages 1-2, baskaran2024trpv1activationantagonizes pages 8-10).
- Multifunctionality and subfamilies: Both families are multifunctional. PM20D1 is one member within an enzymatically diverse M20 superfamily; only PM20D1’s NAA metabolism ties it to thermogenesis. TRPV1 belongs to a sensory ion channel family with roles in nociception, vasoregulation, and central circuits; domain presence alone is not diagnostic for adipose thermogenic function (sponton2018multifacetedrolesof pages 2-3, baskaran2017trpv1activationcounters pages 6-11).

| Entity | Family/Domain context | Mechanism related to thermogenesis | Species/Taxon | Experimental context | Key finding (1–2 sentences) | Year | Citation ID |
|---|---|---|---|---|---|---:|---|
| TRPV1 (Baskaran 2017) | Transient receptor potential vanilloid 1 (TRP channel) | TRPV1 activation → Ca2+ influx → CAMKII/AMPK → SIRT1 activation → PRDM16 deacetylation → PPARγ/PGC‑1α → ↑UCP1 and BAT thermogenesis | Mouse (Mus musculus) | In vivo capsaicin feeding; TRPV1 knockout mice; BAT molecular assays; metabolic cage measurements | Capsaicin-induced TRPV1 activation increases BAT thermogenic program and opposes diet‑induced obesity in WT but not TRPV1‑/- mice. | 2017 | (baskaran2017trpv1activationcounters pages 6-11) |
| TRPV1 (Baskaran 2024) | TRPV1 (TRP channel) | TRPV1 → SIRT1 → PRDM16 → ↑UCP1 transcription; effects require PRDM16 and UCP1 at thermoneutrality | Mouse (Mus musculus) | In vivo capsaicin feeding at thermoneutrality; UCP1 KO and adipose‑specific PRDM16 KO mice; in vitro reporter assays | Capsaicin activation of TRPV1 counters HFD‑induced obesity at thermoneutrality via PRDM16‑dependent upregulation of UCP1; effect is absent in UCP1 or adipose PRDM16 knockouts. | 2024 | (baskaran2024trpv1activationantagonizes pages 1-2, baskaran2024trpv1activationantagonizes pages 8-10) |
| Beige adipocytes (review) | Thermogenic beige fat context (UCP1-dependent and UCP1-independent mechanisms) | Describes UCP1‑independent thermogenic pathways (e.g., SERCA2b/Ca2+ cycling, creatine cycling) and places lipokines/NAAs in thermogenic signaling | Mouse / Human (review) | Synthesis of multiple experimental studies and mechanisms | Beige adipocytes can perform significant UCP1‑independent thermogenesis (e.g., SERCA2b Ca2+ cycling); NAAs/other lipokines are recognized contributors to non‑UCP1 thermogenic pathways. | 2018 | (sponton2018multifacetedrolesof pages 2-3) |
| PM20D1 (Simoes 2025) | N‑fatty‑acyl‑amino acid synthase/hydrolase (PM20D1; secreted M20 peptidase family) | PM20D1 synthesizes/degrades N‑acyl amino acids (NAAs) that bind mitochondria and act as UCP1‑independent uncouplers | Mouse (in vivo) and human genetic associations | Mouse in vivo genetics (promoter variant, tissue overexpression/knockdown), brown adipocyte respiration assays, human variant association analyses | PM20D1 expression controls circulating/tissue NAAs and modulates cold tolerance and mitochondrial uncoupling in a UCP1‑independent manner; human PM20D1 variants associate with BMI and metabolic syndrome. | 2025 | (simoes2025bidirectionalshiftsin pages 1-2) |


*Table: Compact summary of experimental evidence linking TRPV1 and PM20D1 families to adaptive thermogenesis, showing mechanisms, species, experimental context, concise findings, and source IDs for rapid rule assessment.*

3. GO Term Evaluation (GO:1990845, adaptive thermogenesis)
- Appropriateness for PM20D1: The mechanistic link is indirect—PM20D1 regulates NAAs that can uncouple mitochondria and enhance thermogenesis in adipocytes. Mouse in vivo data show effects on cold tolerance and BAT respiration via UCP1-independent uncoupling. Thus, an annotation such as “regulation of adaptive thermogenesis” (positive/negative as appropriate) better reflects PM20D1’s modulatory role than assigning adaptive thermogenesis as a primary process term. Broad Eukaryota propagation is not appropriate, since adaptive thermogenesis is a mammalian physiological program; a Mammalia restriction is advisable (simoes2025bidirectionalshiftsin pages 1-2, sponton2018multifacetedrolesof pages 2-3).
- Appropriateness for TRPV1: In mice, TRPV1 activation can increase UCP1 expression and adipose thermogenesis, with genetic dependency on PRDM16 and UCP1 in thermoneutral settings. This supports “regulation of adaptive thermogenesis,” likely positive regulation in adipose tissue. However, TRPV1 has context-dependent roles and extensive extra-adipose functions, so qualifier specificity (e.g., adipose tissue, peripheral TRPV1) and taxon (Mus/Mammalia) should be applied (baskaran2017trpv1activationcounters pages 6-11, baskaran2024trpv1activationantagonizes pages 1-2, baskaran2024trpv1activationantagonizes pages 8-10, baskaran2017trpv1activationcounters pages 19-22, baskaran2024trpv1activationantagonizes pages 10-12, baskaran2024trpv1activationantagonizes pages 15-16, baskaran2017trpv1activationcounters pages 29-36, baskaran2024trpv1activationantagonizes pages 14-15).
- Scope: GO:1990845 is an organism-level physiological process; for protein-centric annotation, regulation terms are often more precise. Where possible, pair with molecular function/child biological processes: for PM20D1, appropriate lipid metabolic process annotations; for TRPV1, cation channel activity and calcium signaling-related processes, alongside regulation of thermogenesis (sponton2018multifacetedrolesof pages 2-3).

4. Evidence Review
- PM20D1 and NAAs: Mouse genetics show that PM20D1 level changes (promoter variant, tissue-specific modulation) bidirectionally alter cold tolerance and BAT mitochondrial respiration in a UCP1-independent fashion, consistent with NAAs acting as mitochondrial uncouplers. Human variants associate with BMI/metabolic syndrome, suggesting translational relevance, though direct human mechanistic confirmations in adipose tissues remain limited (simoes2025bidirectionalshiftsin pages 1-2). Publication: Molecular Medicine (2025-08), URL: https://doi.org/10.1186/s10020-025-01345-9 (simoes2025bidirectionalshiftsin pages 1-2). Background context on UCP1-independent thermogenesis and lipid mediators is provided by authoritative review (Endocrinology 2018-07) (sponton2018multifacetedrolesof pages 2-3).
- TRPV1, PRDM16, and UCP1: Foundational murine data demonstrate that capsaicin’s metabolic and thermogenic effects require TRPV1 and engage SIRT1/PRDM16 pathways to upregulate UCP1, protecting against diet-induced obesity. At thermoneutrality, the anti-obesity effects of capsaicin require both PRDM16 and UCP1, further supporting a direct role in adipose adaptive thermogenesis programs. These results are robust in mice, but their generalization to other taxa or to all TRPV1 homologs is not justified (baskaran2017trpv1activationcounters pages 6-11, baskaran2024trpv1activationantagonizes pages 1-2, baskaran2024trpv1activationantagonizes pages 8-10, baskaran2017trpv1activationcounters pages 19-22, baskaran2024trpv1activationantagonizes pages 10-12, baskaran2024trpv1activationantagonizes pages 15-16, baskaran2017trpv1activationcounters pages 29-36, baskaran2024trpv1activationantagonizes pages 14-15). Publications: Int J Obes (2017-01), https://doi.org/10.1038/ijo.2017.16 (baskaran2017trpv1activationcounters pages 6-11); Pharmaceuticals (2024-08), https://doi.org/10.3390/ph17081098 (baskaran2024trpv1activationantagonizes pages 1-2, baskaran2024trpv1activationantagonizes pages 8-10).
- Contradictory/limiting points: The relative contributions of UCP1-dependent and -independent mechanisms can vary with temperature and depot, and classic mouse studies show context-dependent obesity phenotypes in UCP1 deficiency; this underscores the need for careful contextualization and argues against blanket annotation beyond mouse adipose biology (sponton2018multifacetedrolesof pages 2-3, baskaran2024trpv1activationantagonizes pages 15-16, baskaran2024trpv1activationantagonizes pages 14-15).

5. Taxonomic Considerations
- PM20D1 condition set (Eukaryota): Adaptive thermogenesis is a mammalian trait. Although PM20D1 homologs exist broadly, evidence linking PM20D1 to adaptive thermogenesis pertains to mice and human associations. Expanding annotation to Eukaryota invites false positives (e.g., plants, fungi, invertebrates). Recommended restriction: Mammalia; optionally Vertebrata with caution (simoes2025bidirectionalshiftsin pages 1-2, sponton2018multifacetedrolesof pages 2-3).
- TRPV1 condition set (Mus): Mouse-specific thermogenesis data are strong. Extending beyond Mus should be evidence-based; other mammals likely share mechanisms, but interspecies differences and central-peripheral balance should be considered (baskaran2017trpv1activationcounters pages 6-11, baskaran2024trpv1activationantagonizes pages 1-2, baskaran2024trpv1activationantagonizes pages 8-10).

6. Rule Logic Assessment
- Biological sense of domain combinations: 
  • PM20D1 FunFams: Mechanistically plausible via NAA-driven uncoupling; however, the FunFam capture may include homologs not engaging adipose thermogenesis; enzyme function is upstream and modulatory rather than constitutive of the process (simoes2025bidirectionalshiftsin pages 1-2).
  • TRPV1 FunFams: Clear mechanistic links in mouse adipose tissue to PRDM16/UCP1; however, TRPV1 is widely expressed and multifunctional, so the annotation should be constrained to regulatory context rather than core thermogenic process (baskaran2017trpv1activationcounters pages 6-11, baskaran2024trpv1activationantagonizes pages 1-2, baskaran2024trpv1activationantagonizes pages 8-10, baskaran2017trpv1activationcounters pages 29-36).
- Redundant conditions: The two condition sets refer to unrelated mechanisms (lipid mediator enzyme versus ion channel). They are not redundant but both connect to thermogenesis regulation in mice.
- Potential false positives: 
  • PM20D1 across Eukaryota risks spurious annotations in non-mammalian systems lacking adaptive thermogenesis; within mammals, paralogs or distant M20 family members may be misclassified by FunFam and lack NAA synthase/hydrolase activity (sponton2018multifacetedrolesof pages 2-3, simoes2025bidirectionalshiftsin pages 1-2).
  • TRPV1 FunFams could annotate channels studied mainly in nociception with no demonstrated adipose thermogenic regulation in certain species or tissues, especially outside mouse contexts (baskaran2017trpv1activationcounters pages 6-11, baskaran2024trpv1activationantagonizes pages 1-2, baskaran2024trpv1activationantagonizes pages 8-10).

7. Recommendations
- GO granularity: Replace or complement GO:1990845 with a regulation term such as “positive regulation of adaptive thermogenesis” or “regulation of adaptive thermogenesis,” as the evidence indicates upstream modulation rather than direct execution of the process (both PM20D1 and TRPV1) (simoes2025bidirectionalshiftsin pages 1-2, baskaran2017trpv1activationcounters pages 6-11, baskaran2024trpv1activationantagonizes pages 1-2, baskaran2024trpv1activationantagonizes pages 8-10, sponton2018multifacetedrolesof pages 2-3).
- Taxonomic restriction: 
  • PM20D1 condition set: Restrict to Mammalia (ideally Rodentia and Primates) until broader evidence emerges. Avoid Eukaryota-level propagation (simoes2025bidirectionalshiftsin pages 1-2, sponton2018multifacetedrolesof pages 2-3).
  • TRPV1 condition set: Retain Mus restriction, with option to extend to Mammalia if corroborating mammalian evidence is curated (baskaran2017trpv1activationcounters pages 6-11, baskaran2024trpv1activationantagonizes pages 1-2, baskaran2024trpv1activationantagonizes pages 8-10).
- Evidence qualifiers: For PM20D1, consider adding “UCP1-independent mechanism” in the evidence note; for TRPV1, add “PRDM16/UCP1-dependent” and “demonstrated at thermoneutrality in mice” to contextualize the annotation (simoes2025bidirectionalshiftsin pages 1-2, baskaran2024trpv1activationantagonizes pages 1-2, baskaran2024trpv1activationantagonizes pages 8-10).
- Domain specificity checks: For PM20D1 FunFams, verify that the FunFam truly resolves PM20D1 orthologs (secreted M20D1-like enzymes) rather than general M20 metallopeptidases to avoid neofunctionalization-induced misannotations (simoes2025bidirectionalshiftsin pages 1-2).
- Alternate/adjacent terms: Pair with molecular and pathway annotations: lipid metabolic process/NAAs for PM20D1; calcium-mediated signaling and cation channel activity for TRPV1; optionally, “browning of adipose tissue” is not a GO term, but “beige fat cell differentiation” may serve as a related process if supported by direct evidence (baskaran2017trpv1activationcounters pages 29-36, sponton2018multifacetedrolesof pages 2-3).

Cited sources, URLs, and dates (selection):
- Baskaran et al., Int J Obes (2017-01-01 online): https://doi.org/10.1038/ijo.2017.16 (TRPV1→SIRT1/PRDM16→UCP1; anti-obesity via thermogenesis in mice) (baskaran2017trpv1activationcounters pages 6-11, baskaran2017trpv1activationcounters pages 19-22, baskaran2017trpv1activationcounters pages 29-36).
- Baskaran et al., Pharmaceuticals (2024-08-12): https://doi.org/10.3390/ph17081098 (TRPV1 activation counters obesity at thermoneutrality via PRDM16 and UCP1 requirement) (baskaran2024trpv1activationantagonizes pages 1-2, baskaran2024trpv1activationantagonizes pages 8-10, baskaran2024trpv1activationantagonizes pages 10-12, baskaran2024trpv1activationantagonizes pages 15-16, baskaran2024trpv1activationantagonizes pages 14-15).
- Simoes et al., Molecular Medicine (2025-08-08): https://doi.org/10.1186/s10020-025-01345-9 (PM20D1 variants modulate NAAs, UCP1-independent BAT respiration, and cold tolerance; human associations) (simoes2025bidirectionalshiftsin pages 1-2).
- Sponton & Kajimura, Endocrinology (2018-07-01): https://doi.org/10.1210/en.2018-00371 (review of UCP1-independent thermogenesis pathways, contextualizing lipid mediator roles) (sponton2018multifacetedrolesof pages 2-3).

Limitations and open questions
- Central TRPV1 neurons may influence thermoregulatory circuits, but specific evidence for central TRPV1 suppressing adipose thermogenesis is not included in the curated set used here; annotations should therefore be limited to peripheral/adipose TRPV1 mechanisms demonstrated in mice (baskaran2017trpv1activationcounters pages 6-11, baskaran2024trpv1activationantagonizes pages 1-2, baskaran2024trpv1activationantagonizes pages 8-10).
- Human translational evidence for PM20D1→thermogenesis remains largely associative; caution is warranted before broad cross-species propagation (simoes2025bidirectionalshiftsin pages 1-2).

Conclusion
UniProt Rule ARBA00089174 targets biologically plausible links between PM20D1/NAAs and TRPV1 and adaptive thermogenesis, but it should: (a) narrow taxonomic scope (especially for PM20D1, not Eukaryota-wide), (b) refine the GO assignment to regulation of adaptive thermogenesis with contextual qualifiers, and (c) ensure FunFam specificity aligns with PM20D1 orthology (not generic M20 peptidases) to minimize false positives (simoes2025bidirectionalshiftsin pages 1-2, sponton2018multifacetedrolesof pages 2-3, baskaran2017trpv1activationcounters pages 6-11, baskaran2024trpv1activationantagonizes pages 1-2, baskaran2024trpv1activationantagonizes pages 8-10).

References

1. (baskaran2017trpv1activationcounters pages 6-11): P. Baskaran, V. Krishnan, Kevin D. Fettel, Peng Gao, Zhiming Zhu, Jun Ren, and B. Thyagarajan. Trpv1 activation counters diet-induced obesity through sirtuin-1 activation and prdm-16 deacetylation in brown adipose tissue. International Journal of Obesity, 41:739-749, Jan 2017. URL: https://doi.org/10.1038/ijo.2017.16, doi:10.1038/ijo.2017.16. This article has 222 citations and is from a highest quality peer-reviewed journal.

2. (baskaran2024trpv1activationantagonizes pages 1-2): Padmamalini Baskaran, Noah Gustafson, and Nicolas Chavez. Trpv1 activation antagonizes high-fat diet-induced obesity at thermoneutrality and enhances ucp-1 transcription via prdm-16. Pharmaceuticals, 17:1098, Aug 2024. URL: https://doi.org/10.3390/ph17081098, doi:10.3390/ph17081098. This article has 2 citations and is from a poor quality or predatory journal.

3. (baskaran2024trpv1activationantagonizes pages 8-10): Padmamalini Baskaran, Noah Gustafson, and Nicolas Chavez. Trpv1 activation antagonizes high-fat diet-induced obesity at thermoneutrality and enhances ucp-1 transcription via prdm-16. Pharmaceuticals, 17:1098, Aug 2024. URL: https://doi.org/10.3390/ph17081098, doi:10.3390/ph17081098. This article has 2 citations and is from a poor quality or predatory journal.

4. (baskaran2017trpv1activationcounters pages 19-22): P. Baskaran, V. Krishnan, Kevin D. Fettel, Peng Gao, Zhiming Zhu, Jun Ren, and B. Thyagarajan. Trpv1 activation counters diet-induced obesity through sirtuin-1 activation and prdm-16 deacetylation in brown adipose tissue. International Journal of Obesity, 41:739-749, Jan 2017. URL: https://doi.org/10.1038/ijo.2017.16, doi:10.1038/ijo.2017.16. This article has 222 citations and is from a highest quality peer-reviewed journal.

5. (baskaran2024trpv1activationantagonizes pages 10-12): Padmamalini Baskaran, Noah Gustafson, and Nicolas Chavez. Trpv1 activation antagonizes high-fat diet-induced obesity at thermoneutrality and enhances ucp-1 transcription via prdm-16. Pharmaceuticals, 17:1098, Aug 2024. URL: https://doi.org/10.3390/ph17081098, doi:10.3390/ph17081098. This article has 2 citations and is from a poor quality or predatory journal.

6. (baskaran2024trpv1activationantagonizes pages 15-16): Padmamalini Baskaran, Noah Gustafson, and Nicolas Chavez. Trpv1 activation antagonizes high-fat diet-induced obesity at thermoneutrality and enhances ucp-1 transcription via prdm-16. Pharmaceuticals, 17:1098, Aug 2024. URL: https://doi.org/10.3390/ph17081098, doi:10.3390/ph17081098. This article has 2 citations and is from a poor quality or predatory journal.

7. (baskaran2017trpv1activationcounters pages 29-36): P. Baskaran, V. Krishnan, Kevin D. Fettel, Peng Gao, Zhiming Zhu, Jun Ren, and B. Thyagarajan. Trpv1 activation counters diet-induced obesity through sirtuin-1 activation and prdm-16 deacetylation in brown adipose tissue. International Journal of Obesity, 41:739-749, Jan 2017. URL: https://doi.org/10.1038/ijo.2017.16, doi:10.1038/ijo.2017.16. This article has 222 citations and is from a highest quality peer-reviewed journal.

8. (baskaran2024trpv1activationantagonizes pages 14-15): Padmamalini Baskaran, Noah Gustafson, and Nicolas Chavez. Trpv1 activation antagonizes high-fat diet-induced obesity at thermoneutrality and enhances ucp-1 transcription via prdm-16. Pharmaceuticals, 17:1098, Aug 2024. URL: https://doi.org/10.3390/ph17081098, doi:10.3390/ph17081098. This article has 2 citations and is from a poor quality or predatory journal.

9. (simoes2025bidirectionalshiftsin pages 1-2): Marcela R. Simoes, Ana L. Gallo-Ferraz, Bruna Bombassaro, Fernando Valdivieso-Rivera, Guilherme A. S. Nogueira, Milena Monfort-Pires, Marcos Vinicius da Cruz, Ariane M. Zanesco, Nayra Fernanda-Oliveira, Leonardo Reis Silveira, Roger F. Castilho, Carlos H. Sponton, and Licio A. Velloso. Bidirectional shifts in pm20d1 expression impact thermogenesis and metabolism. Molecular Medicine, Aug 2025. URL: https://doi.org/10.1186/s10020-025-01345-9, doi:10.1186/s10020-025-01345-9. This article has 1 citations and is from a peer-reviewed journal.

10. (sponton2018multifacetedrolesof pages 2-3): Carlos Henrique Sponton and Shingo Kajimura. Multifaceted roles of beige fat in energy homeostasis beyond ucp1. Endocrinology, 159 7:2545-2553, Jul 2018. URL: https://doi.org/10.1210/en.2018-00371, doi:10.1210/en.2018-00371. This article has 36 citations and is from a domain leading peer-reviewed journal.

## Citations

1. simoes2025bidirectionalshiftsin pages 1-2
2. sponton2018multifacetedrolesof pages 2-3
3. https://doi.org/10.1186/s10020-025-01345-9
4. https://doi.org/10.1038/ijo.2017.16
5. https://doi.org/10.3390/ph17081098
6. https://doi.org/10.1210/en.2018-00371
7. https://doi.org/10.1038/ijo.2017.16,
8. https://doi.org/10.3390/ph17081098,
9. https://doi.org/10.1186/s10020-025-01345-9,
10. https://doi.org/10.1210/en.2018-00371,