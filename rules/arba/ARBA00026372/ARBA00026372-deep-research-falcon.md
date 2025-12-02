---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-01T23:21:06.086099'
end_time: '2025-12-01T23:29:12.506714'
duration_seconds: 486.42
template_file: templates/rule_research.md
template_variables:
  rule_id: ARBA00026372
  rule_type: arba
  go_terms: GO:0051998 (protein carboxyl O-methyltransferase activity)
  conditions_summary: '**Condition Set 1:** InterPro id: Isoprenylcysteine carboxyl
    methyltransferase (InterPro:IPR007269) AND InterPro id: Protein-S-isoprenylcysteine
    O-methyltransferase (InterPro:IPR025770) AND PANTHER id: PTHR12714


    **Condition Set 2:** FunFam id: Protein-L-isoaspartate O-methyltransferase (CATH.FunFam:3.40.50.150:FF:000027)
    AND taxon: Eukaryota (NCBITaxon:2759)


    **Condition Set 3:** FunFam id: Protein-S-isoprenylcysteine O-methyltransferase
    (CATH.FunFam:1.20.120.1630:FF:000007)


    **Condition Set 4:** FunFam id: Protein-S-isoprenylcysteine O-methyltransferase
    (CATH.FunFam:1.20.120.1630:FF:000018) AND taxon: Fungi (NCBITaxon:4751)


    **Condition Set 5:** FunFam id: Protein-L-isoaspartate O-methyltransferase (CATH.FunFam:3.40.50.150:FF:000235)
    AND taxon: Metazoa (NCBITaxon:33208)


    *These condition sets are OR-ed together (any match triggers the annotation)*'
  protein_count: 0 total (0 reviewed, 0 unreviewed)
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 31
---

## Question

# UniProt Rule Research

## Rule Context

- **Rule ID:** ARBA00026372
- **Rule Type:** arba
- **GO Term(s) Predicted:** GO:0051998 (protein carboxyl O-methyltransferase activity)
- **Proteins Annotated:** 0 total (0 reviewed, 0 unreviewed)

### Condition Summary

**Condition Set 1:** InterPro id: Isoprenylcysteine carboxyl methyltransferase (InterPro:IPR007269) AND InterPro id: Protein-S-isoprenylcysteine O-methyltransferase (InterPro:IPR025770) AND PANTHER id: PTHR12714

**Condition Set 2:** FunFam id: Protein-L-isoaspartate O-methyltransferase (CATH.FunFam:3.40.50.150:FF:000027) AND taxon: Eukaryota (NCBITaxon:2759)

**Condition Set 3:** FunFam id: Protein-S-isoprenylcysteine O-methyltransferase (CATH.FunFam:1.20.120.1630:FF:000007)

**Condition Set 4:** FunFam id: Protein-S-isoprenylcysteine O-methyltransferase (CATH.FunFam:1.20.120.1630:FF:000018) AND taxon: Fungi (NCBITaxon:4751)

**Condition Set 5:** FunFam id: Protein-L-isoaspartate O-methyltransferase (CATH.FunFam:3.40.50.150:FF:000235) AND taxon: Metazoa (NCBITaxon:33208)

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

For the predicted GO term(s) **GO:0051998 (protein carboxyl O-methyltransferase activity)**:
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

- **Rule ID:** ARBA00026372
- **Rule Type:** arba
- **GO Term(s) Predicted:** GO:0051998 (protein carboxyl O-methyltransferase activity)
- **Proteins Annotated:** 0 total (0 reviewed, 0 unreviewed)

### Condition Summary

**Condition Set 1:** InterPro id: Isoprenylcysteine carboxyl methyltransferase (InterPro:IPR007269) AND InterPro id: Protein-S-isoprenylcysteine O-methyltransferase (InterPro:IPR025770) AND PANTHER id: PTHR12714

**Condition Set 2:** FunFam id: Protein-L-isoaspartate O-methyltransferase (CATH.FunFam:3.40.50.150:FF:000027) AND taxon: Eukaryota (NCBITaxon:2759)

**Condition Set 3:** FunFam id: Protein-S-isoprenylcysteine O-methyltransferase (CATH.FunFam:1.20.120.1630:FF:000007)

**Condition Set 4:** FunFam id: Protein-S-isoprenylcysteine O-methyltransferase (CATH.FunFam:1.20.120.1630:FF:000018) AND taxon: Fungi (NCBITaxon:4751)

**Condition Set 5:** FunFam id: Protein-L-isoaspartate O-methyltransferase (CATH.FunFam:3.40.50.150:FF:000235) AND taxon: Metazoa (NCBITaxon:33208)

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

For the predicted GO term(s) **GO:0051998 (protein carboxyl O-methyltransferase activity)**:
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
ARBA00026372 aims to assign GO:0051998 (protein carboxyl O‑methyltransferase activity) when proteins match ICMT- or PIMT-related domain/family signatures. ICMT (isoprenylcysteine carboxyl methyltransferase) and PIMT/PCMT1 (protein‑L‑isoaspartate O‑methyltransferase) are both protein carboxyl O‑methyltransferases, but they are mechanistically and biologically distinct: ICMT is an ER-resident integral membrane enzyme that methylates C‑terminal prenylcysteine residues of CAAX proteins, whereas PIMT is a soluble repair enzyme that methylates abnormal L‑isoaspartyl residues formed by protein damage. OR-ing ICMT and PIMT signatures under a single rule risks conflating these activities. The GO term is chemically correct but overly broad for both families; substrate-specific GO terms are preferable (e.g., protein‑S‑isoprenylcysteine O‑methyltransferase vs protein‑L‑isoaspartate O‑methyltransferase). Based on the evidence, ICMT-related signatures (InterPro IPR007269, IPR025770; PANTHER PTHR12714; ICMT CATH FunFams) are appropriate predictors of prenylcysteine carboxyl O‑methylation, while PIMT-related CATH FunFams appropriately predict isoaspartyl repair methylation; combining them in a single OR rule should be avoided (maheshwari2024isoprenylcysteinecarboxylmethyltransferase pages 14-19, maheshwari2024isoprenylcysteinecarboxylmethyltransferase pages 37-41, maheshwari2024isoprenylcysteinecarboxylmethyltransferase pages 26-30, maheshwari2024isoprenylcysteinecarboxylmethyltransferase pages 30-34, soliman2021lisoaspartylmethyltransferasedeficiency pages 14-15, soliman2021lisoaspartylmethyltransferasedeficiency pages 17-18).

2. Domain Analysis
- InterPro: IPR007269 (Isoprenylcysteine carboxyl methyltransferase) and IPR025770 (Protein‑S‑isoprenylcysteine O‑methyltransferase): These describe ICMT, the sole eukaryotic enzyme that methylates the α‑carboxylate of terminal prenylated cysteines of CAAX proteins using SAM; ICMT is integral to the ER and required for correct localization/function of many prenylated small GTPases (e.g., RAS). These signatures are diagnostic for prenylcysteine carboxyl O‑methylation (maheshwari2024isoprenylcysteinecarboxylmethyltransferase pages 14-19, maheshwari2024isoprenylcysteinecarboxylmethyltransferase pages 37-41, maheshwari2024isoprenylcysteinecarboxylmethyltransferase pages 30-34).
- PANTHER: PTHR12714: Groups ICMT family members and supports the above function; membership indicates ER membrane methyltransferase acting on prenylcysteine substrates (maheshwari2024isoprenylcysteinecarboxylmethyltransferase pages 14-19, yang2017isoprenylcarboxylmethyltransferase pages 1-2).
- CATH FunFams 1.20.120.1630:FF:000007 and :FF:000018 (fungi): ICMT structural families (including Ste14p in fungi) that catalyze prenylcysteine carboxyl O‑methylation; these are appropriate and taxonomically coherent for ICMT (wright2009topologyofmammalian pages 6-7, maheshwari2024isoprenylcysteinecarboxylmethyltransferase pages 30-34).
- CATH FunFams 3.40.50.150:FF:000027 and :FF:000235 (metazoa): Protein‑L‑isoaspartate O‑methyltransferase (PCMT/PIMT) families; these encode soluble SAM‑dependent repair methyltransferases that methylate L‑isoaspartyl residues formed by deamidation/isomerization in proteins. They are diagnostic for isoaspartyl repair methylation, not prenylcysteine methylation (soliman2021lisoaspartylmethyltransferasedeficiency pages 14-15, soliman2021lisoaspartylmethyltransferasedeficiency pages 1-2, soliman2021lisoaspartylmethyltransferasedeficiency pages 17-18).
- Multifunctionality/subfamilies: ICMT has a largely single catalytic activity; differences across species (e.g., N‑terminal regulatory extensions) do not indicate alternative chemistries (wright2009topologyofmammalian pages 6-7). PIMT has paralogs/related proteins (e.g., PCMTD1/PCMTD2) and non‑catalytic interactions in signaling contexts, but canonical catalysis remains isoaspartyl repair (pang2025structuralbasisfor pages 5-7, simko2020pimtbindingto pages 8-11).

| Signature/Family | Enzyme family | Canonical function | Diagnostic for GO:0051998? | Known alternative functions/subfamilies | Taxonomic span (per literature) | Notes/risks for annotation |
|---|---|---|---:|---|---|---|
| InterPro:IPR007269 | Isoprenylcysteine carboxyl methyltransferase (ICMT) | Methylesterification of C-terminal prenylcysteine (CaaX) on prenylated proteins using SAM → SAH (post‑prenylation Cys carboxyl O‑methylation) (maheshwari2024isoprenylcysteinecarboxylmethyltransferase pages 14-19, wright2009topologyofmammalian pages 6-7) | Yes — corresponds to prenylcysteine carboxyl O‑methylation (fits protein carboxyl O‑methyltransferase activity) (maheshwari2024isoprenylcysteinecarboxylmethyltransferase pages 37-41) | Largely single canonical activity; animal N‑terminal extensions suggest regulatory variants but not new chemistry (wright2009topologyofmammalian pages 6-7) | Broadly conserved across eukaryotes (yeast Ste14 → metazoan ICMT); ER membrane localization (maheshwari2024isoprenylcysteinecarboxylmethyltransferase pages 26-30, maheshwari2024isoprenylcysteinecarboxylmethyltransferase pages 30-34) | Strong diagnostic for prenylcysteine methylation; low false‑positive risk if used alone, but risk if OR‑combined with unrelated methyltransferases. |
| InterPro:IPR025770 | Protein‑S‑isoprenylcysteine O‑methyltransferase (ICMT descriptor) | Same as above (ER‑localized methylation of prenylcysteine on CaaX proteins) (maheshwari2024isoprenylcysteinecarboxylmethyltransferase pages 14-19) | Yes (directly matches prenylcysteine methyltransferase activity) (yang2017isoprenylcarboxylmethyltransferase pages 1-2) | No well‑established alternative catalytic activities reported; species variants exist | Eukaryotic distribution; functional homologs in yeast and animals (maheshwari2024isoprenylcysteinecarboxylmethyltransferase pages 30-34) | As with IPR007269: reliable for ICMT annotation; include membrane/ER context to avoid misannotation. |
| PANTHER:PTHR12714 | ICMT family (PANTHER grouping) | Post‑prenylation methylation of prenylcysteine residues (CaaX processing) (maheshwari2024isoprenylcysteinecarboxylmethyltransferase pages 14-19, yang2017isoprenylcarboxylmethyltransferase pages 1-2) | Yes — PANTHER family maps to ICMT catalytic activity | Family clustering may include divergent paralogs with regulatory extensions but canonical chemistry conserved | Eukaryotes (well represented in metazoa, yeast orthologs used in studies) (maheshwari2024isoprenylcysteinecarboxylmethyltransferase pages 37-41) | Family match strongly supports GO:0051998 for prenylcysteine substrates; verify transmembrane topology. |
| CATH.FunFam:1.20.120.1630:FF:000007 | Protein‑S‑isoprenylcysteine O‑methyltransferase (ICMT FunFam) | ICMT‑type methylation of prenylated cysteine residues (structural FunFam for ICMT fold) (maheshwari2024isoprenylcysteinecarboxylmethyltransferase pages 26-30) | Yes — FunFam membership is diagnostic for ICMT activity in many species (maheshwari2024isoprenylcysteinecarboxylmethyltransferase pages 30-34) | Subfamily/organism‑specific variations possible (e.g., insect vs mammal sequence differences) | Eukaryotes (includes fungal/animal representatives) (maheshwari2024isoprenylcysteinecarboxylmethyltransferase pages 26-30) | Good structural support; FunFam hits should be combined with membrane/ER annotation to reduce misannotation. |
| CATH.FunFam:1.20.120.1630:FF:000018 (taxon: Fungi) | ICMT / Ste14‑like methyltransferase (fungal) | Ste14‑type prenylcysteine methylation in fungi (ER membrane) (wright2009topologyofmammalian pages 6-7) | Yes (fungal Ste14 is canonical ICMT homolog) (wright2009topologyofmammalian pages 6-7) | Primarily Ste14/ICMT activity; functional conservation in fungi reported | Fungi (Ste14 founding member characterized in Saccharomyces) (wright2009topologyofmammalian pages 6-7) | Taxon restriction appropriate; retain to avoid transferring nonfungal annotations. |
| CATH.FunFam:3.40.50.150:FF:000027 | Protein‑L‑isoaspartate (D‑aspartate) O‑methyltransferase (PCMT/PIMT) | SAM‑dependent repair methyltransferase that methylates abnormal L‑isoaspartyl (isoAsp) carboxyl groups in damaged proteins (protein‑repair) (soliman2021lisoaspartylmethyltransferasedeficiency pages 14-15, soliman2021lisoaspartylmethyltransferasedeficiency pages 17-18) | Partial — GO:0051998 (protein carboxyl O‑methyltransferase) is chemically compatible, but substrate specificity (isoAsp/repair) is distinct from prenylcysteine methylation (soliman2021lisoaspartylmethyltransferasedeficiency pages 1-2) | PCMT paralogs/related proteins (PCMTD1/PCMTD2) and non‑repair roles (interactions with signaling proteins, CAIX binding) reported (simko2020pimtbindingto pages 21-22, simko2020pimtbindingto pages 8-11, pang2025structuralbasisfor pages 5-7) | Broadly conserved (bacteria, archaea, plants, animals); essential roles in vertebrate nervous system; some taxa (certain fungi/yeast) may lack canonical PCMT (soliman2021lisoaspartylmethyltransferasedeficiency pages 1-2, soliman2021lisoaspartylmethyltransferasedeficiency pages 17-18) | Although GO:0051998 can apply, applying the same GO to ICMT vs PCMT without qualifiers causes cross‑annotation errors; substrate‑specific GO terms or EC/GPI qualifiers recommended. |
| CATH.FunFam:3.40.50.150:FF:000235 (taxon: Metazoa) | PCMT (metazoan PCMT1 family) | IsoAsp repair methyltransferase acting on damaged Asp/Asn residues in metazoan proteins; important in brain physiology and proteostasis (soliman2021lisoaspartylmethyltransferasedeficiency pages 14-15, soliman2021lisoaspartylmethyltransferasedeficiency pages 17-18) | Yes — appropriate for metazoan PCMTs, but denotes isoAsp substrate (GO generic term applies but is ambiguous) (soliman2021lisoaspartylmethyltransferasedeficiency pages 17-18) | Metazoan‑specific isoforms/isozymes and regulatory interactions (e.g., CAIX binding, p53 regulation) described (simko2020pimtbindingto pages 21-22, simko2020pimtbindingto pages 8-11) | Metazoa (vertebrates shown essential; zebrafish/mouse models with severe phenotypes) (soliman2021lisoaspartylmethyltransferasedeficiency pages 14-15) | Taxon restriction is useful; annotate with substrate‑specific evidence to avoid conflation with ICMT family. |


*Table: Concise mapping of the rule's domain/family signatures to enzyme families, canonical functions, substrate specificity and taxonomic span, with notes on whether each signature is diagnostic for GO:0051998 and risks of cross‑annotation. This helps assess the rule's validity and potential false positives.*

3. GO Term Evaluation
- Appropriateness of GO:0051998: Chemically correct for both ICMT and PIMT since both catalyze protein carboxyl O‑methylation. However, it is too broad for precise functional annotation because it merges distinct substrate classes and biological roles (prenylcysteine processing vs isoaspartyl repair) (maheshwari2024isoprenylcysteinecarboxylmethyltransferase pages 37-41, soliman2021lisoaspartylmethyltransferasedeficiency pages 1-2).
- Better alternatives:
  • For ICMT signatures: a substrate-specific term such as “protein‑S‑isoprenylcysteine O‑methyltransferase activity” (matches IPR025770 label) to reflect prenylcysteine substrates, ER localization, and post‑prenylation CAAX processing (maheshwari2024isoprenylcysteinecarboxylmethyltransferase pages 14-19, maheshwari2024isoprenylcysteinecarboxylmethyltransferase pages 30-34).
  • For PIMT signatures: “protein‑L‑isoaspartate O‑methyltransferase activity” to reflect repair of isoaspartyl residues (soliman2021lisoaspartylmethyltransferasedeficiency pages 1-2, soliman2021lisoaspartylmethyltransferasedeficiency pages 17-18).
- Narrowness/breadth: Using the generic GO:0051998 across ICMT and PIMT is too broad; using only an ICMT‑specific term would be too narrow for PIMT FunFams and vice versa (maheshwari2024isoprenylcysteinecarboxylmethyltransferase pages 14-19, soliman2021lisoaspartylmethyltransferasedeficiency pages 14-15).

4. Evidence Review
ICMT
- Biochemical function, substrates, localization, and uniqueness: ICMT resides in the ER membrane, catalyzing methyl esterification of C‑terminal prenylcysteine α‑carboxylates of CAAX proteins, using SAM and producing SAH. It is the sole cellular enzyme for this reaction, and methylation contributes to membrane localization and activity of RAS, RHO family, lamins, and other prenylated proteins (Maheshwari 2024 review; Nature 2018 structure) (maheshwari2024isoprenylcysteinecarboxylmethyltransferase pages 14-19, maheshwari2024isoprenylcysteinecarboxylmethyltransferase pages 37-41).
- Structure: An atomic structure of eukaryotic ICMT shows an 8‑TM intramembrane methyltransferase with a membrane-embedded substrate cavity and distinct entry routes for SAM and prenylcysteine substrates, explaining catalysis at the membrane interface (Diver et al., Nature 2018) (maheshwari2024isoprenylcysteinecarboxylmethyltransferase pages 37-41). Topology experiments in live cells confirm ER localization, 8 TMs, and cytosolic N/C termini (Wright et al., 2009) (wright2009topologyofmammalian pages 6-7).
- Conservation: Yeast Ste14p is the founding member; human ICMT and Ste14 share significant homology and function, indicating conservation across eukaryotes (maheshwari2024isoprenylcysteinecarboxylmethyltransferase pages 26-30, wright2009topologyofmammalian pages 6-7, maheshwari2024isoprenylcysteinecarboxylmethyltransferase pages 30-34).
- Cellular/organismal roles: Genetic and pharmacological studies show that loss or inhibition of ICMT mislocalizes KRAS and reduces oncogenic signaling; context dependence is reported in pancreatic models (yang2017isoprenylcarboxylmethyltransferase pages 1-2, wright2009topologyofmammalian pages 6-7, maheshwari2024isoprenylcysteinecarboxylmethyltransferase pages 37-41).
- Recent (2023–2024) developments/applications: A 2024 review summarizes ICMT structure/function and inhibitor design, identifying new bi‑substrate analog hits (YD series) and reiterating ICMT as a Ras‑adjacent target; oncology reviews in 2024 emphasize post‑prenylation processing targets, including ICMT, as complementary strategies to direct RAS inhibition (Maheshwari 2024; Piazza 2024) (maheshwari2024isoprenylcysteinecarboxylmethyltransferase pages 14-19, maheshwari2024isoprenylcysteinecarboxylmethyltransferase pages 37-41). Additional 2024 commentary highlights ICMT as part of the RAS membrane‑localization machinery under active exploration (Nakhchi 2024) (pang2025structuralbasisfor pages 7-10).
- Expert perspectives: Mutant p53 can upregulate ICMT, potentially enhancing prenylation-dependent oncogenic signaling; wild‑type p53 downregulates ICMT, linking ICMT to tumor biology and metabolism (Etichetti 2020) (etichetti2020beyondthemevalonate pages 3-4).

PIMT/PCMT1
- Biochemical function, substrates, and localization: PIMT (PCMT1) is a soluble SAM‑dependent repair methyltransferase that recognizes and methylates L‑isoaspartyl residues formed in proteins by deamidation/isomerization (via succinimide intermediates), initiating conversion back to normal L‑aspartyl residues. Substrates include calmodulin and other calcium‑binding proteins; loss causes accumulation of isoaspartyl‑damaged proteins (Soliman 2021) (soliman2021lisoaspartylmethyltransferasedeficiency pages 1-2, soliman2021lisoaspartylmethyltransferasedeficiency pages 17-18). Tissue expression is high in brain and testis; alternative splicing variants and potential ER‑retained isoforms are reported in some species (soliman2021lisoaspartylmethyltransferasedeficiency pages 14-15).
- Conservation and physiology: PCMT is broadly conserved (bacteria to vertebrates). Vertebrate models show that deficiency leads to neurological defects and lethality; zebrafish knockdown reveals impaired brain calcium signaling, indicating physiological significance in Ca2+ homeostasis (Soliman 2021) (soliman2021lisoaspartylmethyltransferasedeficiency pages 14-15, soliman2021lisoaspartylmethyltransferasedeficiency pages 1-2). Emerging work suggests complementary roles of PCMT paralogs (PCMTD1/2) in managing isoAsp damage (pang2025structuralbasisfor pages 5-7, pang2025structuralbasisfor pages 7-10).
- Disease links and signaling: PIMT modulates apoptosis and stress responses (e.g., protects cardiomyocytes against hypoxia via MST1), interacts with p53/S100A4 to influence degradation pathways, and may interact with CAIX to mediate hypoxic signaling in tumors (Yan 2013; Simko 2020) (yan2013proteinlisoaspartate(daspartate)omethyltransferase pages 9-9, simko2020pimtbindingto pages 8-11).
- Recent (2023–2024) relevance: Although direct 2023–2024 primary reports in the current evidence set are limited, contemporary datasets and reviews emphasize PCMT’s roles in proteostasis, neurobiology, and aging; single‑cell datasets report pcmt enrichment under oxidative stress contexts in fish spleen, underscoring conserved stress‑repair functions in vivo (Aldersey 2024) (https://doi.org/10.1371/journal.pone.0309397, Sep 2024; ).

5. Taxonomic Considerations
- ICMT: Eukaryote-specific integrally membrane ER enzyme; conserved from fungi (Ste14p) to metazoa. The ICMT‑specific InterPro and CATH FunFams should not be extended to bacteria/archaea (maheshwari2024isoprenylcysteinecarboxylmethyltransferase pages 37-41, maheshwari2024isoprenylcysteinecarboxylmethyltransferase pages 26-30, wright2009topologyofmammalian pages 6-7, maheshwari2024isoprenylcysteinecarboxylmethyltransferase pages 30-34).
- PIMT: Broad distribution across bacteria, archaea, plants, and animals; vertebrate nervous system shows strong dependency. Some species/lineages may vary in gene complement or reliance on paralogs (pcmt vs pcmtd), but the repair function is broadly conserved (soliman2021lisoaspartylmethyltransferasedeficiency pages 1-2, soliman2021lisoaspartylmethyltransferasedeficiency pages 17-18, pang2025structuralbasisfor pages 5-7).

6. Rule Logic Assessment
- Biological sense of domain combinations: Grouping ICMT-related signatures together is coherent; grouping PIMT-related FunFams together is coherent. However, OR‑combining ICMT and PIMT signatures in one rule is problematic because it collapses two distinct enzyme families (substrates, localization, and biology differ) under one GO label, diminishing specificity (maheshwari2024isoprenylcysteinecarboxylmethyltransferase pages 37-41, soliman2021lisoaspartylmethyltransferasedeficiency pages 1-2).
- Redundancy: IPR007269 and IPR025770 both represent ICMT and may be partially redundant. PANTHER PTHR12714 similarly supports the same family; using all three may be unnecessary if one high-confidence signature is sufficient (maheshwari2024isoprenylcysteinecarboxylmethyltransferase pages 14-19, maheshwari2024isoprenylcysteinecarboxylmethyltransferase pages 30-34).
- False positives: The current OR logic can produce false positives by assigning the same GO term to PIMT matches (isoaspartyl repair) and to ICMT matches (prenylcysteine methylation). While GO:0051998 is technically true for both, downstream users may infer prenylation biology for PIMT hits or repair biology for ICMT hits, which is incorrect (soliman2021lisoaspartylmethyltransferasedeficiency pages 1-2, maheshwari2024isoprenylcysteinecarboxylmethyltransferase pages 37-41).

7. Recommendations
- Split the rule into two substrate‑specific rules:
  • ICMT Rule: Triggered by ICMT signatures (IPR007269/IPR025770/PTHR12714/CATH 1.20.120.1630 FunFams), assign a substrate‑specific GO term for protein‑S‑isoprenylcysteine O‑methyltransferase activity, with ER membrane localization annotations; taxonomic scope: Eukaryota (maheshwari2024isoprenylcysteinecarboxylmethyltransferase pages 37-41, wright2009topologyofmammalian pages 6-7, maheshwari2024isoprenylcysteinecarboxylmethyltransferase pages 30-34).
  • PIMT Rule: Triggered by PIMT FunFams (CATH 3.40.50.150 FunFams, including metazoan-restricted FF:000235 where appropriate), assign protein‑L‑isoaspartate O‑methyltransferase activity and include protein repair/aging-related process terms; broad taxonomic scope with lineages where present (soliman2021lisoaspartylmethyltransferasedeficiency pages 1-2, soliman2021lisoaspartylmethyltransferasedeficiency pages 17-18).
- Remove cross‑family OR logic to avoid conflation. If a single rule must be retained, at minimum attach substrate-specific GO qualifiers in evidence lines and add distinct secondary annotations for subcellular localization (ER membrane for ICMT; cytosol/nucleus for PIMT) (maheshwari2024isoprenylcysteinecarboxylmethyltransferase pages 37-41, soliman2021lisoaspartylmethyltransferasedeficiency pages 1-2).
- Prefer the most discriminative signatures: For ICMT, InterPro or CATH FunFam specific to ICMT plus PANTHER family can be sufficient; for PIMT, CATH 3.40.50.150 FunFams are strong, with metazoan FF:000235 aiding taxon specificity (maheshwari2024isoprenylcysteinecarboxylmethyltransferase pages 30-34, soliman2021lisoaspartylmethyltransferasedeficiency pages 17-18).
- Cite recent developments in rule documentation: Reference the 2018 Nature ICMT structure for mechanistic justification and 2024 reviews highlighting ongoing ICMT inhibitor discovery efforts; for PIMT, underline vertebrate neurophysiological evidence and 2021 zebrafish in vivo Ca2+ signaling phenotypes (maheshwari2024isoprenylcysteinecarboxylmethyltransferase pages 37-41, maheshwari2024isoprenylcysteinecarboxylmethyltransferase pages 14-19, soliman2021lisoaspartylmethyltransferasedeficiency pages 14-15, soliman2021lisoaspartylmethyltransferasedeficiency pages 1-2).

References (URLs and dates where available)
- Diver MM et al. Atomic structure of the eukaryotic intramembrane Ras methyltransferase ICMT. Nature. 2018-01. https://doi.org/10.1038/nature25439 (maheshwari2024isoprenylcysteinecarboxylmethyltransferase pages 37-41)
- Maheshwari A. Isoprenylcysteine Carboxyl Methyltransferase (ICMT): Structure, Function, And Inhibitor Design. 2024 (review) (maheshwari2024isoprenylcysteinecarboxylmethyltransferase pages 14-19, maheshwari2024isoprenylcysteinecarboxylmethyltransferase pages 78-81, maheshwari2024isoprenylcysteinecarboxylmethyltransferase pages 26-30, maheshwari2024isoprenylcysteinecarboxylmethyltransferase pages 30-34)
- Wright LP et al. Topology of Mammalian ICMT Determined in Live Cells. Mol Cell Biol. 2009-04. https://doi.org/10.1128/MCB.01719-08 (wright2009topologyofmammalian pages 6-7)
- Yang WS et al. ICMT inhibitors: patents and review. Amino Acids. 2017-06. https://doi.org/10.1007/s00726-017-2454-x (yang2017isoprenylcarboxylmethyltransferase pages 1-2)
- Etichetti CMB et al. Mutant p53 control of post‑prenylation processing including ICMT. Front Oncol. 2020-11. https://doi.org/10.3389/fonc.2020.595034 (etichetti2020beyondthemevalonate pages 3-4)
- Piazza GA et al. Assessment of KRASG12C inhibitors for CRC. Front Oncol. 2024-06. https://doi.org/10.3389/fonc.2024.1412435 ()
- Nakhchi BG et al. Targeting endothelial Rap1B; notes ICMT as RAS‑localization target. Int J Mol Sci. 2024-09. https://doi.org/10.3390/ijms25189853 (pang2025structuralbasisfor pages 7-10)
- Soliman R et al. L‑Isoaspartyl methyltransferase deficiency in zebrafish. Front Genet. 2021-01. https://doi.org/10.3389/fgene.2020.612343 (soliman2021lisoaspartylmethyltransferasedeficiency pages 14-15, soliman2021lisoaspartylmethyltransferasedeficiency pages 1-2, soliman2021lisoaspartylmethyltransferasedeficiency pages 17-18)
- Yan G et al. PCMT1 protects cardiomyocytes against hypoxia‑induced apoptosis. Int J Cardiol. 2013-10. https://doi.org/10.1016/j.ijcard.2013.04.045 (yan2013proteinlisoaspartate(daspartate)omethyltransferase pages 9-9)

Expert analysis and relevant statistics
- KRAS mutations occur in ~25% of all human cancers and in ~45% of CRC; post‑prenylation enzymes including ICMT remain active targets to complement direct KRAS inhibitors (Piazza 2024) (). The eukaryotic‑specific, sole prenylcysteine O‑methyltransferase role of ICMT underpins its diagnostic domain signatures and its importance in prenylome biology (Diver 2018; Maheshwari 2024) (maheshwari2024isoprenylcysteinecarboxylmethyltransferase pages 37-41, maheshwari2024isoprenylcysteinecarboxylmethyltransferase pages 14-19). In contrast, the broadly conserved PIMT system constitutes a proteome‑repair axis essential for neuronal physiology and calcium signaling in vivo (Soliman 2021) (soliman2021lisoaspartylmethyltransferasedeficiency pages 14-15, soliman2021lisoaspartylmethyltransferasedeficiency pages 1-2).

Overall, ARBA00026372 should be split into two rules aligned to substrate‑specific GO terms to preserve biological precision and reduce false positives, with taxonomy and localization constraints tailored to each enzyme family.

References

1. (maheshwari2024isoprenylcysteinecarboxylmethyltransferase pages 14-19): A Maheshwari. Isoprenylcysteine carboxyl methyltransferase (icmt): structure, function, and inhibitor design. Unknown journal, 2024.

2. (maheshwari2024isoprenylcysteinecarboxylmethyltransferase pages 37-41): A Maheshwari. Isoprenylcysteine carboxyl methyltransferase (icmt): structure, function, and inhibitor design. Unknown journal, 2024.

3. (maheshwari2024isoprenylcysteinecarboxylmethyltransferase pages 26-30): A Maheshwari. Isoprenylcysteine carboxyl methyltransferase (icmt): structure, function, and inhibitor design. Unknown journal, 2024.

4. (maheshwari2024isoprenylcysteinecarboxylmethyltransferase pages 30-34): A Maheshwari. Isoprenylcysteine carboxyl methyltransferase (icmt): structure, function, and inhibitor design. Unknown journal, 2024.

5. (soliman2021lisoaspartylmethyltransferasedeficiency pages 14-15): Remon Soliman, Maria Lorena Cordero-Maldonado, Teresa G. Martins, Mahsa Moein, Jean-François Conrotte, Rebeccah A. Warmack, Alexander Skupin, Alexander D. Crawford, Steven G. Clarke, and Carole L. Linster. L-isoaspartyl methyltransferase deficiency in zebrafish leads to impaired calcium signaling in the brain. Frontiers in Genetics, Jan 2021. URL: https://doi.org/10.3389/fgene.2020.612343, doi:10.3389/fgene.2020.612343. This article has 5 citations and is from a peer-reviewed journal.

6. (soliman2021lisoaspartylmethyltransferasedeficiency pages 17-18): Remon Soliman, Maria Lorena Cordero-Maldonado, Teresa G. Martins, Mahsa Moein, Jean-François Conrotte, Rebeccah A. Warmack, Alexander Skupin, Alexander D. Crawford, Steven G. Clarke, and Carole L. Linster. L-isoaspartyl methyltransferase deficiency in zebrafish leads to impaired calcium signaling in the brain. Frontiers in Genetics, Jan 2021. URL: https://doi.org/10.3389/fgene.2020.612343, doi:10.3389/fgene.2020.612343. This article has 5 citations and is from a peer-reviewed journal.

7. (yang2017isoprenylcarboxylmethyltransferase pages 1-2): Woo Seok Yang, Seung-Gu Yeo, Sungjae Yang, Kyung-Hee Kim, Byong Chul Yoo, and Jae Youl Cho. Isoprenyl carboxyl methyltransferase inhibitors: a brief review including recent patents. Amino Acids, 49:1469-1485, Jun 2017. URL: https://doi.org/10.1007/s00726-017-2454-x, doi:10.1007/s00726-017-2454-x. This article has 26 citations and is from a peer-reviewed journal.

8. (wright2009topologyofmammalian pages 6-7): Latasha P. Wright, Helen Court, Adam Mor, Ian M. Ahearn, Patrick J. Casey, and Mark R. Philips. Topology of mammalian isoprenylcysteine carboxyl methyltransferase determined in live cells with a fluorescent probe. Molecular and Cellular Biology, 29:1826-1833, Apr 2009. URL: https://doi.org/10.1128/mcb.01719-08, doi:10.1128/mcb.01719-08. This article has 30 citations and is from a domain leading peer-reviewed journal.

9. (soliman2021lisoaspartylmethyltransferasedeficiency pages 1-2): Remon Soliman, Maria Lorena Cordero-Maldonado, Teresa G. Martins, Mahsa Moein, Jean-François Conrotte, Rebeccah A. Warmack, Alexander Skupin, Alexander D. Crawford, Steven G. Clarke, and Carole L. Linster. L-isoaspartyl methyltransferase deficiency in zebrafish leads to impaired calcium signaling in the brain. Frontiers in Genetics, Jan 2021. URL: https://doi.org/10.3389/fgene.2020.612343, doi:10.3389/fgene.2020.612343. This article has 5 citations and is from a peer-reviewed journal.

10. (pang2025structuralbasisfor pages 5-7): Eric Z. Pang, Boyu Zhao, Cameron Flowers, Elizabeth Oroudjeva, Jasmine B. Winter, Vijaya Pandey, Michael R. Sawaya, James Wohlschlegel, Joseph A. Loo, Jose A. Rodriguez, and Steven G. Clarke. Structural basis for l-isoaspartyl-containing protein recognition by the pcmtd1 cullin-ring e3 ubiquitin ligase. bioRxiv, May 2025. URL: https://doi.org/10.1101/2025.05.21.654933, doi:10.1101/2025.05.21.654933. This article has 1 citations and is from a poor quality or predatory journal.

11. (simko2020pimtbindingto pages 8-11): Veronika Simko, Petra Belvoncikova, Lucia Csaderova, Martina Labudova, Katarina Grossmannova, Miriam Zatovicova, Ivana Kajanova, Ludovit Skultety, Monika Barathova, and Jaromir Pastorek. Pimt binding to c-terminal ala459 of caix is involved in inside-out signaling necessary for its catalytic activity. International Journal of Molecular Sciences, 21:8545, Nov 2020. URL: https://doi.org/10.3390/ijms21228545, doi:10.3390/ijms21228545. This article has 5 citations and is from a poor quality or predatory journal.

12. (simko2020pimtbindingto pages 21-22): Veronika Simko, Petra Belvoncikova, Lucia Csaderova, Martina Labudova, Katarina Grossmannova, Miriam Zatovicova, Ivana Kajanova, Ludovit Skultety, Monika Barathova, and Jaromir Pastorek. Pimt binding to c-terminal ala459 of caix is involved in inside-out signaling necessary for its catalytic activity. International Journal of Molecular Sciences, 21:8545, Nov 2020. URL: https://doi.org/10.3390/ijms21228545, doi:10.3390/ijms21228545. This article has 5 citations and is from a poor quality or predatory journal.

13. (pang2025structuralbasisfor pages 7-10): Eric Z. Pang, Boyu Zhao, Cameron Flowers, Elizabeth Oroudjeva, Jasmine B. Winter, Vijaya Pandey, Michael R. Sawaya, James Wohlschlegel, Joseph A. Loo, Jose A. Rodriguez, and Steven G. Clarke. Structural basis for l-isoaspartyl-containing protein recognition by the pcmtd1 cullin-ring e3 ubiquitin ligase. bioRxiv, May 2025. URL: https://doi.org/10.1101/2025.05.21.654933, doi:10.1101/2025.05.21.654933. This article has 1 citations and is from a poor quality or predatory journal.

14. (etichetti2020beyondthemevalonate pages 3-4): Carla M Borini Etichetti, Evelyn Arel Zalazar, Nabila Cocordano, and Javier Girardini. Beyond the mevalonate pathway: control of post-prenylation processing by mutant p53. Frontiers in Oncology, Nov 2020. URL: https://doi.org/10.3389/fonc.2020.595034, doi:10.3389/fonc.2020.595034. This article has 16 citations and is from a poor quality or predatory journal.

15. (yan2013proteinlisoaspartate(daspartate)omethyltransferase pages 9-9): Guijun Yan, Qing Qin, Bing Yi, Kurt Chuprun, Haixiang Sun, Shengdong Huang, and Jianxin Sun. Protein-l-isoaspartate (d-aspartate) o-methyltransferase protects cardiomyocytes against hypoxia induced apoptosis through inhibiting proapoptotic kinase mst1. International journal of cardiology, 168 4:3291-9, Oct 2013. URL: https://doi.org/10.1016/j.ijcard.2013.04.045, doi:10.1016/j.ijcard.2013.04.045. This article has 32 citations and is from a peer-reviewed journal.

16. (maheshwari2024isoprenylcysteinecarboxylmethyltransferase pages 78-81): A Maheshwari. Isoprenylcysteine carboxyl methyltransferase (icmt): structure, function, and inhibitor design. Unknown journal, 2024.

## Citations

1. wright2009topologyofmammalian pages 6-7
2. maheshwari2024isoprenylcysteinecarboxylmethyltransferase pages 37-41
3. maheshwari2024isoprenylcysteinecarboxylmethyltransferase pages 14-19
4. yang2017isoprenylcarboxylmethyltransferase pages 1-2
5. maheshwari2024isoprenylcysteinecarboxylmethyltransferase pages 30-34
6. maheshwari2024isoprenylcysteinecarboxylmethyltransferase pages 26-30
7. soliman2021lisoaspartylmethyltransferasedeficiency pages 1-2
8. soliman2021lisoaspartylmethyltransferasedeficiency pages 17-18
9. soliman2021lisoaspartylmethyltransferasedeficiency pages 14-15
10. pang2025structuralbasisfor pages 7-10
11. etichetti2020beyondthemevalonate pages 3-4
12. pang2025structuralbasisfor pages 5-7
13. simko2020pimtbindingto pages 8-11
14. simko2020pimtbindingto pages 21-22
15. maheshwari2024isoprenylcysteinecarboxylmethyltransferase pages 78-81
16. https://doi.org/10.1371/journal.pone.0309397,
17. https://doi.org/10.1038/nature25439
18. https://doi.org/10.1128/MCB.01719-08
19. https://doi.org/10.1007/s00726-017-2454-x
20. https://doi.org/10.3389/fonc.2020.595034
21. https://doi.org/10.3389/fonc.2024.1412435
22. https://doi.org/10.3390/ijms25189853
23. https://doi.org/10.3389/fgene.2020.612343
24. https://doi.org/10.1016/j.ijcard.2013.04.045
25. https://doi.org/10.3389/fgene.2020.612343,
26. https://doi.org/10.1007/s00726-017-2454-x,
27. https://doi.org/10.1128/mcb.01719-08,
28. https://doi.org/10.1101/2025.05.21.654933,
29. https://doi.org/10.3390/ijms21228545,
30. https://doi.org/10.3389/fonc.2020.595034,
31. https://doi.org/10.1016/j.ijcard.2013.04.045,