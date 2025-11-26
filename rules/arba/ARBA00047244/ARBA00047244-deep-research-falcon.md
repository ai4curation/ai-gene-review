---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-11-25T19:22:57.812751'
end_time: '2025-11-25T19:28:38.865647'
duration_seconds: 341.05
template_file: templates/rule_research.md
template_variables:
  rule_id: ARBA00047244
  rule_type: arba
  go_terms: GO:0043605 (amide catabolic process)
  conditions_summary: '**Condition Set 1:** InterPro id: Urease, beta subunit-like
    (InterPro:IPR002019) AND InterPro id: Urease, gamma/gamma-beta subunit (InterPro:IPR002026)
    AND InterPro id: Urease active site (InterPro:IPR017950)


    **Condition Set 2:** FunFam id: N-fatty-acyl-amino acid synthase/hydrolase PM20D1
    (CATH.FunFam:1.10.150.900:FF:000003) AND FunFam id: N-fatty-acyl-amino acid synthase/hydrolase
    PM20D1 (CATH.FunFam:3.40.630.10:FF:000027) AND taxon: Eukaryota (NCBITaxon:2759)


    **Condition Set 3:** FunFam id: Putative ureidoglycolate hydrolase (CATH.FunFam:3.30.70.360:FF:000012)
    AND FunFam id: Allantoate amidohydrolase (CATH.FunFam:3.40.630.10:FF:000044) AND
    taxon: Viridiplantae (NCBITaxon:33090)


    **Condition Set 4:** FunFam id: (S)-ureidoglycine aminohydrolase (CATH.FunFam:2.60.120.10:FF:000137)
    AND taxon: Streptophyta (NCBITaxon:35493)


    *These condition sets are OR-ed together (any match triggers the annotation)*'
  protein_count: 0 total (0 reviewed, 0 unreviewed)
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 17
---

## Question

# UniProt Rule Research

## Rule Context

- **Rule ID:** ARBA00047244
- **Rule Type:** arba
- **GO Term(s) Predicted:** GO:0043605 (amide catabolic process)
- **Proteins Annotated:** 0 total (0 reviewed, 0 unreviewed)

### Condition Summary

**Condition Set 1:** InterPro id: Urease, beta subunit-like (InterPro:IPR002019) AND InterPro id: Urease, gamma/gamma-beta subunit (InterPro:IPR002026) AND InterPro id: Urease active site (InterPro:IPR017950)

**Condition Set 2:** FunFam id: N-fatty-acyl-amino acid synthase/hydrolase PM20D1 (CATH.FunFam:1.10.150.900:FF:000003) AND FunFam id: N-fatty-acyl-amino acid synthase/hydrolase PM20D1 (CATH.FunFam:3.40.630.10:FF:000027) AND taxon: Eukaryota (NCBITaxon:2759)

**Condition Set 3:** FunFam id: Putative ureidoglycolate hydrolase (CATH.FunFam:3.30.70.360:FF:000012) AND FunFam id: Allantoate amidohydrolase (CATH.FunFam:3.40.630.10:FF:000044) AND taxon: Viridiplantae (NCBITaxon:33090)

**Condition Set 4:** FunFam id: (S)-ureidoglycine aminohydrolase (CATH.FunFam:2.60.120.10:FF:000137) AND taxon: Streptophyta (NCBITaxon:35493)

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

For the predicted GO term(s) **GO:0043605 (amide catabolic process)**:
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

- **Rule ID:** ARBA00047244
- **Rule Type:** arba
- **GO Term(s) Predicted:** GO:0043605 (amide catabolic process)
- **Proteins Annotated:** 0 total (0 reviewed, 0 unreviewed)

### Condition Summary

**Condition Set 1:** InterPro id: Urease, beta subunit-like (InterPro:IPR002019) AND InterPro id: Urease, gamma/gamma-beta subunit (InterPro:IPR002026) AND InterPro id: Urease active site (InterPro:IPR017950)

**Condition Set 2:** FunFam id: N-fatty-acyl-amino acid synthase/hydrolase PM20D1 (CATH.FunFam:1.10.150.900:FF:000003) AND FunFam id: N-fatty-acyl-amino acid synthase/hydrolase PM20D1 (CATH.FunFam:3.40.630.10:FF:000027) AND taxon: Eukaryota (NCBITaxon:2759)

**Condition Set 3:** FunFam id: Putative ureidoglycolate hydrolase (CATH.FunFam:3.30.70.360:FF:000012) AND FunFam id: Allantoate amidohydrolase (CATH.FunFam:3.40.630.10:FF:000044) AND taxon: Viridiplantae (NCBITaxon:33090)

**Condition Set 4:** FunFam id: (S)-ureidoglycine aminohydrolase (CATH.FunFam:2.60.120.10:FF:000137) AND taxon: Streptophyta (NCBITaxon:35493)

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

For the predicted GO term(s) **GO:0043605 (amide catabolic process)**:
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
ARBA00047244 predicts GO:0043605 (amide catabolic process) when proteins match selected urease signatures or CATH FunFams for plant ureide amido/aminohydrolases and PM20D1-like proteins. The rule is largely valid for urease and for plant ureide-pathway hydrolases, which catalyze hydrolysis of amide bonds during purine/ureide breakdown. Multiple structural and biochemical studies show that canonical ureases possess a conserved dinickel active site bridged by a carbamylated lysine and are dedicated urea hydrolases, a quintessential amide catabolic reaction. Plant ureide enzymes (allantoate amidohydrolase, (S)-ureidoglycine aminohydrolase, and ureidoglycolate amidohydrolase) are experimentally established amide-cleaving enzymes in Viridiplantae. However, support for the PM20D1 FunFam/Eukaryota condition is not present in the available evidence context here, so that branch should be reviewed for potential overbreadth. Where possible, more specific biological process GO terms (e.g., allantoin or ureide catabolism; urea catabolism) may be preferable to a generic amide catabolic term to improve specificity. (proshlyakov2021ironcontainingureases. pages 1-2, mazzei2020thestructurebasedreaction pages 9-11, werner2013theureidedegradingreactions pages 1-2, witte2011ureametabolismin pages 4-5)

2. Domain Analysis
- InterPro: IPR002019 (urease beta subunit-like), IPR002026 (urease gamma/gamma–beta), IPR017950 (urease active site)
  • Function and specificity: Ureases are metalloenzymes that hydrolyze urea to ammonia and carbamate; the latter decomposes to bicarbonate and additional ammonia. Canonical ureases contain a conserved dinuclear nickel active site where a carbamylated lysine bridges the two Ni(II) ions, along with histidine and carboxylate ligands, and a catalytic water/hydroxide cluster. Structures and mechanistic analyses confirm the central nucleophilic “bridging hydroxide” mechanism and the role of active-site flap residues in catalysis. The conserved metallocenter and accessory subunits are hallmarks of urease assemblies across bacteria and plants, supporting diagnosticity for urea hydrolysis. (Coordination Chemistry Reviews, 2021-12-01, https://doi.org/10.1016/j.ccr.2021.214190; JBIC, 2020-08-01, https://doi.org/10.1007/s00775-020-01808-w) (proshlyakov2021ironcontainingureases. pages 1-2, mazzei2020thestructurebasedreaction pages 9-11)
  • Subfamily/function diversity: Recent work emphasizes conserved active-site architecture across ureases irrespective of oligomeric states (bacterial UreABC vs. plant single-chain hexamers). Accessory proteins (UreD/E/F/G) and metallocenter assembly are required but do not change catalytic specificity; these features reinforce that these InterPro signatures are tightly linked to ureolysis. (Plant Science, 2011-03-01, https://doi.org/10.1016/j.plantsci.2010.11.010) (witte2011ureametabolismin pages 6-7)

- Plant ureide-pathway hydrolases (matched via CATH FunFams in rule Condition Sets 3 and 4)
  • Allantoate amidohydrolase (AAH): Hydrolyzes allantoate to (S)-ureidoglycine; initiates ER-localized amide cleavage steps of allantoin degradation. (Plant Physiology, 2013-08-01, https://doi.org/10.1104/pp.113.224261) (werner2013theureidedegradingreactions pages 1-2)
  • (S)-Ureidoglycine aminohydrolase (UGlyAH): Converts (S)-ureidoglycine to (S)-ureidoglycolate with NH3 release; a bi-cupin enzyme using Mn2+ for stereoselective binding; forms homo-octamers. (Thesis/monograph, 2014, structural and functional analyses) (신인철2014structuralandfunctional pages 112-120, 신인철2014structuralandfunctional pages 125-128)
  • Ureidoglycolate amidohydrolase (UAH): Hydrolyzes (S)-ureidoglycolate to glyoxylate, CO2 and two NH3 via a bimetal center and tetrahedral intermediate; crystal structures reveal metal ligation and ligand-induced conformational change and explain specificity versus AAH. (Thesis/monograph, 2014; Plant Physiology, 2013-08-01, https://doi.org/10.1104/pp.113.224261) (신인철2014structuralandfunctional pages 112-120, werner2013theureidedegradingreactions pages 1-2)
  • Multifunctionality/neofunctionalization: The ureide-pathway amidases (AAH/UAH) are close homologs with distinct active-site determinants that enforce narrow substrate specificity (e.g., AtUAH Tyr-423 vs. Gly in AAH; QXR motif in AAH). Available evidence supports specialized, not broadly multifunctional, roles in purine/ureide catabolism. (Thesis/monograph, 2014) (신인철2014structuralandfunctional pages 112-120)

- PM20D1 FunFams (Condition Set 2)
  • Not supported in the provided evidence context. No direct, citable evidence was retrieved here linking the listed CATH FunFams to PM20D1 biochemistry or diagnosticity; this branch should be reassessed with current primary literature before use in automated annotation. (No supporting context ID)

3. GO Term Evaluation (GO:0043605, amide catabolic process)
- Appropriateness
  • Urease: Urease catalyzes hydrolysis of the amide bond in urea, a prototypical amide catabolic reaction. GO:0043605 is appropriate, though a more specific term such as “urea catabolic process” would increase precision if available in the GO hierarchy. The conserved urease signatures (beta/gamma subunits and active site) collectively point to this reaction. (Coordination Chemistry Reviews, 2021-12-01, https://doi.org/10.1016/j.ccr.2021.214190; JBIC, 2020-08-01, https://doi.org/10.1007/s00775-020-01808-w) (proshlyakov2021ironcontainingureases. pages 1-2, mazzei2020thestructurebasedreaction pages 9-11)
  • Plant ureide-pathway hydrolases: AAH, UGlyAH, and UAH each break specific ureido amide bonds during allantoin/allantoate-to-glyoxylate conversion, liberating ammonia and CO2. GO:0043605 is appropriate; however, more specific biological process terms (e.g., allantoin catabolic process or ureide catabolic process) would better capture pathway context. (Plant Physiology, 2013-08-01, https://doi.org/10.1104/pp.113.224261; Plant Science, 2011-03-01, https://doi.org/10.1016/j.plantsci.2010.11.010) (werner2013theureidedegradingreactions pages 1-2, witte2011ureametabolismin pages 4-5)
- Breadth/Specificity
  • GO:0043605 is broad. Where the rule has strong evidence for specific substrates (urea, allantoate, (S)-ureidoglycine, (S)-ureidoglycolate), more specific BP annotations would reduce ambiguity and improve downstream utility. (werner2013theureidedegradingreactions pages 1-2, witte2011ureametabolismin pages 4-5)

4. Evidence Review
- Urease subunits/active site and mechanism
  • Dinuclear Ni(II) center bridged by a carbamylated lysine is conserved; accessory proteins UreD/E/F/G assemble and metallate the site; catalytic “bridging hydroxide” mechanism supported by structural and inhibitor studies; active-site flap dynamics stabilize intermediates. These features are diagnostic of ureolytic enzymes. (Coordination Chemistry Reviews, 2021-12-01, https://doi.org/10.1016/j.ccr.2021.214190; JBIC, 2020-08-01, https://doi.org/10.1007/s00775-020-01808-w; Plant Science, 2011-03-01, https://doi.org/10.1016/j.plantsci.2010.11.010) (proshlyakov2021ironcontainingureases. pages 1-2, mazzei2020thestructurebasedreaction pages 9-11, witte2011ureametabolismin pages 6-7)

- Plant ureide-pathway hydrolases
  • In Arabidopsis, soybean and rice, allantoin degradation employs one aminohydrolase (UGlyAH) and three amidohydrolases (ALN upstream ring opening; AAH; UAH) to convert (S)-allantoin to glyoxylate, CO2 and NH3. Gene silencing and metabolite accumulation support in vivo roles; ER localization is reported for several steps; orthologs are broadly present across Viridiplantae, including mosses and algae, indicating conservation. (Plant Physiology, 2013-08-01, https://doi.org/10.1104/pp.113.224261) (werner2013theureidedegradingreactions pages 1-2)
  • Detailed structural enzymology of UGlyAH and UAH explains metal dependence, stereoselective substrate recognition, and reaction chemistry, including bimetal centers and residues that specify substrates (e.g., AtUAH Tyr-423). (Thesis/monograph, 2014) (신인철2014structuralandfunctional pages 112-120, 신인철2014structuralandfunctional pages 125-128)
  • Historical plant literature also documents debate over urea production versus direct ammonia release in ureide degradation; current genetic/biochemical data in Arabidopsis favor the amidohydrolase route without obligatory urea. (Plant Science, 2011-03-01, https://doi.org/10.1016/j.plantsci.2010.11.010) (witte2011ureametabolismin pages 4-5)

- PM20D1 FunFam branch
  • No directly citable evidence present in the current context for PM20D1 biochemistry, directionality, or taxonomic breadth. This is a gap for Condition Set 2 and should be addressed before relying on this branch of the rule.

5. Taxonomic Considerations
- Urease: Occurs in bacteria and plants with conserved active-site architecture; accessory maturation systems are widely distributed. Thus, applying amide catabolism for matched urease subunit/active-site signatures has broad taxonomic validity when the combination of subunits and active-site motif is present. (Plant Science, 2011-03-01, https://doi.org/10.1016/j.plantsci.2010.11.010; JBIC, 2020-08-01, https://doi.org/10.1007/s00775-020-01808-w; Coordination Chemistry Reviews, 2021-12-01, https://doi.org/10.1016/j.ccr.2021.214190) (witte2011ureametabolismin pages 6-7, mazzei2020thestructurebasedreaction pages 9-11, proshlyakov2021ironcontainingureases. pages 1-2)
- Plant ureide enzymes: AAH, UGlyAH, and UAH orthologs are broadly conserved in Viridiplantae (including soybean, rice, Arabidopsis; also reported in mosses/algae). Streptophyta-restricted conditions (e.g., for (S)-ureidoglycine aminohydrolase) are consistent with the distribution of the ureide catabolic phase. (Plant Physiology, 2013-08-01, https://doi.org/10.1104/pp.113.224261) (werner2013theureidedegradingreactions pages 1-2)
- PM20D1 in Eukaryota: Not supported in the provided context; verify presence and function across Eukaryota before applying taxon filters that could include distant eukaryotes lacking the pathway.

6. Rule Logic Assessment
- Biological sense of domain combinations
  • Condition Set 1 (urease beta, gamma, and active site) provides a strong, mechanistically coherent signature for urease; together these should be highly specific for ureolysis and thus for amide catabolism. (proshlyakov2021ironcontainingureases. pages 1-2, mazzei2020thestructurebasedreaction pages 9-11)
  • Condition Sets 3 and 4 (ureide-pathway hydrolase FunFams with Viridiplantae/Streptophyta filters) align with well-established plant ureide catabolism enzymes; likely specific for amide hydrolysis steps in the pathway. (werner2013theureidedegradingreactions pages 1-2, 신인철2014structuralandfunctional pages 112-120)
  • Condition Set 2 (PM20D1 FunFams in Eukaryota) lacks support in this evidence set and may admit false positives or include proteins with bidirectional or context-dependent activity; review needed.
- Redundancy
  • Within urease, requiring both subunit signatures and the active-site signature reduces false positives from paralogous metalloenzymes or partial matches.
- False positives/negatives
  • Urease: Low risk when the full combination is present. Partial hits to a single subunit without the active-site signature could be risky.
  • Plant ureide enzymes: FunFam assignment plus Viridiplantae filters should reduce spurious microbial amidohydrolases not involved in the ureide pathway; consider adding additional sequence motifs/active-site residues (e.g., AtUAH Tyr-423 equivalent) to further tighten specificity. (신인철2014structuralandfunctional pages 112-120)
  • PM20D1 branch: Without corroborating evidence, this condition could yield false positives across diverse eukaryotic M20 or related peptidase-like proteins with different functions.

7. Recommendations
- Keep: Condition Set 1 (urease) and Condition Sets 3–4 (plant ureide hydrolases) under GO:0043605; these are well supported by conserved structure and pathway biochemistry. (proshlyakov2021ironcontainingureases. pages 1-2, mazzei2020thestructurebasedreaction pages 9-11, werner2013theureidedegradingreactions pages 1-2)
- Improve specificity: Where possible, add specific process annotations in addition to GO:0043605, such as “urea catabolic process” for urease and “allantoin/ureide catabolic process” for plant enzymes, to reflect pathway roles. (werner2013theureidedegradingreactions pages 1-2, witte2011ureametabolismin pages 4-5)
- Reassess Condition Set 2 (PM20D1 FunFams in Eukaryota): Acquire and incorporate contemporary primary literature to validate directionality, substrate scope, and taxonomic distribution prior to applying this branch; alternatively, restrict to well-validated taxa/families once confirmed. (No supporting context ID)
- Add discriminating residues/motifs for plant amidases: Consider integrating active-site determinants (e.g., AtUAH Tyr-423 vs. AAH Gly; AAH QXR motif) to distinguish UAH from AAH-like homologs. (신인철2014structuralandfunctional pages 112-120)

References (URLs, dates)
- Proshlyakov DA et al. Iron-Containing Ureases. Coordination Chemistry Reviews. 2021-12-01. https://doi.org/10.1016/j.ccr.2021.214190 (proshlyakov2021ironcontainingureases. pages 1-2)
- Mazzei L et al. The structure-based reaction mechanism of urease, a nickel dependent enzyme. JBIC. 2020-08-01. https://doi.org/10.1007/s00775-020-01808-w (mazzei2020thestructurebasedreaction pages 9-11)
- Werner AK et al. The ureide-degrading reactions... Plant Physiology. 2013-08-01. https://doi.org/10.1104/pp.113.224261 (werner2013theureidedegradingreactions pages 1-2)
- Witte C-P. Urea metabolism in plants. Plant Science. 2011-03-01. https://doi.org/10.1016/j.plantsci.2010.11.010 (witte2011ureametabolismin pages 4-5)
- Shin I.-C. (thesis/monograph). Structural and functional studies of two enzymes from Arabidopsis thaliana in the ureide pathway: ureidoglycine aminohydrolase and ureidoglycolate… 2014. (신인철2014structuralandfunctional pages 112-120, 신인철2014structuralandfunctional pages 125-128)


References

1. (proshlyakov2021ironcontainingureases. pages 1-2): Denis A. Proshlyakov, Mark A. Farrugia, Yegor D. Proshlyakov, and Robert P. Hausinger. Iron-containing ureases. Coordination chemistry reviews, 448:214190, Dec 2021. URL: https://doi.org/10.1016/j.ccr.2021.214190, doi:10.1016/j.ccr.2021.214190. This article has 15 citations and is from a peer-reviewed journal.

2. (mazzei2020thestructurebasedreaction pages 9-11): Luca Mazzei, Francesco Musiani, and Stefano Ciurli. The structure-based reaction mechanism of urease, a nickel dependent enzyme: tale of a long debate. JBIC Journal of Biological Inorganic Chemistry, 25:829-845, Aug 2020. URL: https://doi.org/10.1007/s00775-020-01808-w, doi:10.1007/s00775-020-01808-w. This article has 202 citations.

3. (werner2013theureidedegradingreactions pages 1-2): Andrea K. Werner, N. Medina-Escobar, Monika Zulawski, I. Sparkes, Feng-Qiu Cao, and C. Witte. The ureide-degrading reactions of purine ring catabolism employ three amidohydrolases and one aminohydrolase in arabidopsis, soybean, and rice1[w]. Plant Physiology, 163:672-681, Aug 2013. URL: https://doi.org/10.1104/pp.113.224261, doi:10.1104/pp.113.224261. This article has 67 citations and is from a highest quality peer-reviewed journal.

4. (witte2011ureametabolismin pages 4-5): Claus-Peter Witte. Urea metabolism in plants. Plant science : an international journal of experimental plant biology, 180 3:431-8, Mar 2011. URL: https://doi.org/10.1016/j.plantsci.2010.11.010, doi:10.1016/j.plantsci.2010.11.010. This article has 522 citations.

5. (witte2011ureametabolismin pages 6-7): Claus-Peter Witte. Urea metabolism in plants. Plant science : an international journal of experimental plant biology, 180 3:431-8, Mar 2011. URL: https://doi.org/10.1016/j.plantsci.2010.11.010, doi:10.1016/j.plantsci.2010.11.010. This article has 522 citations.

6. (신인철2014structuralandfunctional pages 112-120): 신인철. Structural and functional studies of two enzymes from arabidopsis thaliana in the ureide pathway: ureidoglycine aminohydrolase and ureidoglycolate …. Unknown journal, 2014.

7. (신인철2014structuralandfunctional pages 125-128): 신인철. Structural and functional studies of two enzymes from arabidopsis thaliana in the ureide pathway: ureidoglycine aminohydrolase and ureidoglycolate …. Unknown journal, 2014.

## Citations

1. witte2011ureametabolismin pages 6-7
2. werner2013theureidedegradingreactions pages 1-2
3. witte2011ureametabolismin pages 4-5
4. mazzei2020thestructurebasedreaction pages 9-11
5. w
6. https://doi.org/10.1016/j.ccr.2021.214190;
7. https://doi.org/10.1007/s00775-020-01808-w
8. https://doi.org/10.1016/j.plantsci.2010.11.010
9. https://doi.org/10.1104/pp.113.224261
10. https://doi.org/10.1104/pp.113.224261;
11. https://doi.org/10.1007/s00775-020-01808-w;
12. https://doi.org/10.1016/j.plantsci.2010.11.010;
13. https://doi.org/10.1016/j.ccr.2021.214190
14. https://doi.org/10.1016/j.ccr.2021.214190,
15. https://doi.org/10.1007/s00775-020-01808-w,
16. https://doi.org/10.1104/pp.113.224261,
17. https://doi.org/10.1016/j.plantsci.2010.11.010,