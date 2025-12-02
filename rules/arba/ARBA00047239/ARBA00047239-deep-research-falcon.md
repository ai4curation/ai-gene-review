---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2025-12-01T18:13:43.214530'
end_time: '2025-12-01T18:22:22.254526'
duration_seconds: 519.04
template_file: templates/rule_research.md
template_variables:
  rule_id: ARBA00047239
  rule_type: arba
  go_terms: GO:0032206 (positive regulation of telomere maintenance)
  conditions_summary: '**Condition Set 1:** InterPro id: Chaperonin TCP-1, conserved
    site (InterPro:IPR002194) AND InterPro id: Thermosome subunit alpha (InterPro:IPR054827)
    AND taxon: Primates (NCBITaxon:9443)


    **Condition Set 2:** FunFam id: Telomeric repeat-binding factor 2 (CATH.FunFam:1.10.10.60:FF:000129)
    AND FunFam id: Telomeric repeat-binding factor 2 (CATH.FunFam:1.25.40.210:FF:000002)
    AND taxon: Mammalia (NCBITaxon:40674)


    **Condition Set 3:** FunFam id: Serine-protein kinase ATM (CATH.FunFam:1.10.1070.11:FF:000011)
    AND FunFam id: Serine-protein kinase ATM (CATH.FunFam:3.30.1010.10:FF:000015)
    AND taxon: Eukaryota (NCBITaxon:2759)


    **Condition Set 4:** FunFam id: Poly [ADP-ribose] polymerase (CATH.FunFam:1.10.150.50:FF:000012)
    AND FunFam id: Poly [ADP-ribose] polymerase (CATH.FunFam:1.25.40.20:FF:000009)
    AND taxon: Primates (NCBITaxon:9443)


    **Condition Set 5:** FunFam id: T-complex protein 1 subunit eta (CATH.FunFam:1.10.560.10:FF:000017)
    AND FunFam id: T-complex protein 1 subunit eta (CATH.FunFam:1.10.560.10:FF:000045)
    AND taxon: Haplorrhini (NCBITaxon:376913)


    **Condition Set 6:** FunFam id: Regulator of telomere elongation helicase 1 (CATH.FunFam:1.20.1160.20:FF:000006)
    AND FunFam id: Regulator of telomere elongation helicase 1 (CATH.FunFam:1.20.1160.20:FF:000009)
    AND FunFam id: Regulator of telomere elongation helicase 1 (CATH.FunFam:3.40.50.300:FF:000431)


    **Condition Set 7:** FunFam id: Mitogen-activated protein kinase (CATH.FunFam:1.10.510.10:FF:000624)
    AND taxon: Homo (NCBITaxon:9605)


    **Condition Set 8:** FunFam id: RuvB-like helicase (CATH.FunFam:1.10.8.60:FF:000010)
    AND taxon: Mus (NCBITaxon:862507)


    **Condition Set 9:** FunFam id: SLX4 structure-specific endonuclease subunit (CATH.FunFam:3.30.710.10:FF:000116)
    AND taxon: Metazoa (NCBITaxon:33208)


    *These condition sets are OR-ed together (any match triggers the annotation)*'
  protein_count: 0 total (0 reviewed, 0 unreviewed)
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 22
---

## Question

# UniProt Rule Research

## Rule Context

- **Rule ID:** ARBA00047239
- **Rule Type:** arba
- **GO Term(s) Predicted:** GO:0032206 (positive regulation of telomere maintenance)
- **Proteins Annotated:** 0 total (0 reviewed, 0 unreviewed)

### Condition Summary

**Condition Set 1:** InterPro id: Chaperonin TCP-1, conserved site (InterPro:IPR002194) AND InterPro id: Thermosome subunit alpha (InterPro:IPR054827) AND taxon: Primates (NCBITaxon:9443)

**Condition Set 2:** FunFam id: Telomeric repeat-binding factor 2 (CATH.FunFam:1.10.10.60:FF:000129) AND FunFam id: Telomeric repeat-binding factor 2 (CATH.FunFam:1.25.40.210:FF:000002) AND taxon: Mammalia (NCBITaxon:40674)

**Condition Set 3:** FunFam id: Serine-protein kinase ATM (CATH.FunFam:1.10.1070.11:FF:000011) AND FunFam id: Serine-protein kinase ATM (CATH.FunFam:3.30.1010.10:FF:000015) AND taxon: Eukaryota (NCBITaxon:2759)

**Condition Set 4:** FunFam id: Poly [ADP-ribose] polymerase (CATH.FunFam:1.10.150.50:FF:000012) AND FunFam id: Poly [ADP-ribose] polymerase (CATH.FunFam:1.25.40.20:FF:000009) AND taxon: Primates (NCBITaxon:9443)

**Condition Set 5:** FunFam id: T-complex protein 1 subunit eta (CATH.FunFam:1.10.560.10:FF:000017) AND FunFam id: T-complex protein 1 subunit eta (CATH.FunFam:1.10.560.10:FF:000045) AND taxon: Haplorrhini (NCBITaxon:376913)

**Condition Set 6:** FunFam id: Regulator of telomere elongation helicase 1 (CATH.FunFam:1.20.1160.20:FF:000006) AND FunFam id: Regulator of telomere elongation helicase 1 (CATH.FunFam:1.20.1160.20:FF:000009) AND FunFam id: Regulator of telomere elongation helicase 1 (CATH.FunFam:3.40.50.300:FF:000431)

**Condition Set 7:** FunFam id: Mitogen-activated protein kinase (CATH.FunFam:1.10.510.10:FF:000624) AND taxon: Homo (NCBITaxon:9605)

**Condition Set 8:** FunFam id: RuvB-like helicase (CATH.FunFam:1.10.8.60:FF:000010) AND taxon: Mus (NCBITaxon:862507)

**Condition Set 9:** FunFam id: SLX4 structure-specific endonuclease subunit (CATH.FunFam:3.30.710.10:FF:000116) AND taxon: Metazoa (NCBITaxon:33208)

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

For the predicted GO term(s) **GO:0032206 (positive regulation of telomere maintenance)**:
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

- **Rule ID:** ARBA00047239
- **Rule Type:** arba
- **GO Term(s) Predicted:** GO:0032206 (positive regulation of telomere maintenance)
- **Proteins Annotated:** 0 total (0 reviewed, 0 unreviewed)

### Condition Summary

**Condition Set 1:** InterPro id: Chaperonin TCP-1, conserved site (InterPro:IPR002194) AND InterPro id: Thermosome subunit alpha (InterPro:IPR054827) AND taxon: Primates (NCBITaxon:9443)

**Condition Set 2:** FunFam id: Telomeric repeat-binding factor 2 (CATH.FunFam:1.10.10.60:FF:000129) AND FunFam id: Telomeric repeat-binding factor 2 (CATH.FunFam:1.25.40.210:FF:000002) AND taxon: Mammalia (NCBITaxon:40674)

**Condition Set 3:** FunFam id: Serine-protein kinase ATM (CATH.FunFam:1.10.1070.11:FF:000011) AND FunFam id: Serine-protein kinase ATM (CATH.FunFam:3.30.1010.10:FF:000015) AND taxon: Eukaryota (NCBITaxon:2759)

**Condition Set 4:** FunFam id: Poly [ADP-ribose] polymerase (CATH.FunFam:1.10.150.50:FF:000012) AND FunFam id: Poly [ADP-ribose] polymerase (CATH.FunFam:1.25.40.20:FF:000009) AND taxon: Primates (NCBITaxon:9443)

**Condition Set 5:** FunFam id: T-complex protein 1 subunit eta (CATH.FunFam:1.10.560.10:FF:000017) AND FunFam id: T-complex protein 1 subunit eta (CATH.FunFam:1.10.560.10:FF:000045) AND taxon: Haplorrhini (NCBITaxon:376913)

**Condition Set 6:** FunFam id: Regulator of telomere elongation helicase 1 (CATH.FunFam:1.20.1160.20:FF:000006) AND FunFam id: Regulator of telomere elongation helicase 1 (CATH.FunFam:1.20.1160.20:FF:000009) AND FunFam id: Regulator of telomere elongation helicase 1 (CATH.FunFam:3.40.50.300:FF:000431)

**Condition Set 7:** FunFam id: Mitogen-activated protein kinase (CATH.FunFam:1.10.510.10:FF:000624) AND taxon: Homo (NCBITaxon:9605)

**Condition Set 8:** FunFam id: RuvB-like helicase (CATH.FunFam:1.10.8.60:FF:000010) AND taxon: Mus (NCBITaxon:862507)

**Condition Set 9:** FunFam id: SLX4 structure-specific endonuclease subunit (CATH.FunFam:3.30.710.10:FF:000116) AND taxon: Metazoa (NCBITaxon:33208)

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

For the predicted GO term(s) **GO:0032206 (positive regulation of telomere maintenance)**:
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
We evaluate UniProt Rule ARBA00047239, which predicts GO:0032206 (positive regulation of telomere maintenance) from diverse domain/family signatures. Recent evidence (2023–2024) supports direct telomeric roles for SLX4 (processing telomeric joint molecules; regulation in ALT), PARP1/2 (DNA ADP-ribosylation at telomeres; PARP2-driven BIR/MiDAS), and an indirect but mechanistically specific role for the CCT/TRiC chaperonin via telomerase assembly (through TCAB1) and RIOK2-regulated expression of TRiC/dyskerin subunits. Conversely, broad families (ATM, MAPKs, RUVBL1/2) are multifunctional and risk false positives if annotated solely from family signatures. Several taxonomic filters and domain combinations appear inconsistent (e.g., mixing eukaryotic CCT with archaeal thermosome under Primates). We recommend tightening logic: retain SLX4, TRF2, RTEL1, tankyrases/PARP1-2 with telomere-context constraints; drop or heavily restrict ATM/MAPK and generic RUVBL/CCT subunit triggers; correct taxonomy.

2. Domain Analysis
- SLX4 (Condition set 9; SLX4 structure-specific endonuclease subunit): SLX4 scaffolds SLX1/MUS81/XPF, is recruited via TRF2, and processes branched telomeric DNA. Disruption of SLX4–TRF2 or nuclease activity causes telomere fragility. Mechanistically, SLX4 associates with telomeres across the cycle, peaking in late S and under genotoxic stress, and resolves joint molecules to support replication; regulation with BLM suppresses recombination-associated byproducts (t-circles, T-SCE) (NAR 2015) (sarkar2015slx4contributesto pages 1-2). In ALT, SLX4 recruitment is modulated by PCNA ubiquitination and ATR; excess SLX4 at telomeres is deleterious and restrained by ATR (EMBO J 2024), confirming a direct role at ALT telomeres (chen2024atrlimitsrad18mediated pages 1-2) (mori2024alternativelengtheningof pages 1-1).
- PARP family (Condition set 4; Poly[ADP-ribose] polymerase): Distinct members have telomere roles. PARP1 catalyzes DNA ADP-ribosylation at telomeres during lagging-strand synthesis; TARG1 removes it. Persistent DNA-ADPr (e.g., TARG1 deficiency) shortens telomeres; direct telomeric DNA-ADPr occurs at unligated Okazaki fragments and 3′ overhangs (Nat Struct Mol Biol 2024) (wondisford2024deregulateddnaadpribosylation pages 1-2). PARP2 promotes replication stress-induced telomere fragility via BIR and prevents telomere loss by orchestrating POLD3-dependent MiDAS; it promotes resection and strand invasion in stressed telomeres (Nat Commun 2024) (muoio2024parp2promotesbreak pages 1-2). Tankyrases (not shown directly in 2023–2024 items here) classically regulate TRF1 and telomere length; rule logic should prefer tankyrase-specific signatures or PARP1/2 with telomere evidence (sola2024telomeresinterstitialtelomeric pages 96-99).
- CCT/TRiC chaperonin (Condition sets 1 and 5): TRiC is essential for folding telomerase cofactor TCAB1; depletion of a TRiC subunit destabilizes TCAB1 and impairs telomerase (historical). New 2024 work identifies RIOK2 as a transcriptional activator for TRiC and dyskerin complexes; loss of RIOK2 reduces TRiC/dyskerin expression, impairs telomerase activity, and shortens telomeres; RIOK2 overexpression rescues telomere shortening in patient-derived fibroblasts. This provides human cellular evidence that TRiC/dyskerin expression positively regulates telomere maintenance via telomerase biogenesis (Nat Commun 2024) (ghosh2024riok2transcriptionallyregulates pages 1-2). Note: Set 1 illogically combines eukaryotic CCT with archaeal thermosome; thermosome α is archaeal, not Primate (see Recommendations).
- TRF2 (Condition set 2; CATH FunFams labeled as “Telomeric repeat-binding factor 2”): TRF2 is a core shelterin component, directly protecting telomeres and suppressing ATM activation; broad 2024 review emphasizes shelterin-mediated protection and replication, and TRF2’s central role (Frontiers 2024) (harman2024telomeremaintenanceand pages 4-5). Additional synthesis reviews cover TRF1/TRF2 roles, telomerase control and replication stress coupling (sola2024telomeresinterstitialtelomeric pages 96-99).
- RTEL1 helicase (Condition set 6): RTEL1 directly unwinds telomeric DNA (G4s/t-loops) to allow replication/telomerase; field consensus and reviews integrate RTEL1 as essential to telomere maintenance (cited in 2025 review excerpt) (harman2024telomeremaintenanceand pages 4-5). While not a 2024 primary article in our evidence set, this remains a well-established, telomere-specific helicase function (harman2024telomeremaintenanceand pages 4-5).
- ATR/ATM/MAPKs (Condition sets 3 and 7): ATR directly influences ALT telomere stability via Rad18–PCNA monoubiquitination, limiting SLX4 recruitment; this preserves ALT telomere stability (EMBO J 2024) (chen2024atrlimitsrad18mediated pages 1-2). In contrast, “ATM” and “MAPK” are large multifunctional families. Although ATM/ATR are engaged by telomere dysfunction, ATM-family membership alone is not diagnostic for positive regulation of telomere maintenance. Similarly, MAPK (ERK/p38/JNK) signaling intersects with telomere biology indirectly; family-level signatures will yield many non-telomeric proteins (harman2024telomeremaintenanceand pages 4-5).
- RUVBL1/2 (Condition set 8): AAA+ ATPases with roles in R2TP, H/ACA snoRNP assembly, and chromatin remodeling. Their involvement in telomerase biogenesis is through H/ACA RNP assembly and associations with telomerase components; however, 2024 MM transcriptional signatures (CB-6644) are cancer-general and not telomere-specific. Family-level detection is not diagnostic for positive regulation of telomere maintenance unless telomerase complex context is present (yi2024molecularsignaturesof pages 1-2). General telomere overviews and older mechanistic studies place RUVBLs with telomerase assembly, but annotation should be context-constrained (sola2024telomeresinterstitialtelomeric pages 96-99).

3. GO Term Evaluation (GO:0032206)
- Appropriate and specific for: SLX4 (directly supports telomere replication/processing, including ALT), PARP1/2 (promote telomere replication under stress and maintain integrity), TRF2 (shelterin), and RTEL1 (telomeric helicase). These have direct telomere mechanisms (sarkar2015slx4contributesto pages 1-2, chen2024atrlimitsrad18mediated pages 1-2, wondisford2024deregulateddnaadpribosylation pages 1-2, muoio2024parp2promotesbreak pages 1-2, harman2024telomeremaintenanceand pages 4-5, sola2024telomeresinterstitialtelomeric pages 96-99).
- Appropriate but indirect for: CCT/TRiC, when tied to telomerase biogenesis (TCAB1/dyskerin) or RIOK2-dependent expression programs. Annotation should specify “via telomerase assembly” to avoid overreach (ghosh2024riok2transcriptionallyregulates pages 1-2).
- Too broad for: ATM family, generic MAPKs, and generic RUVBL1/2 family signatures without telomerase/telomere complex context. These should not trigger GO:0032206 without additional constraints (chen2024atrlimitsrad18mediated pages 1-2, harman2024telomeremaintenanceand pages 4-5, yi2024molecularsignaturesof pages 1-2).
- Alternative/better GO qualifiers: consider child terms like “regulation of ALT pathway” where available (for SLX4/ATR-PCNA axis), or “regulation of telomerase activity” for TRiC/TCAB1 contexts.

4. Evidence Review (2023–2024 emphasis)
- PARP1/2 at telomeres: PARP1 catalyzes DNA-linked ADP-ribose at telomeres during lagging-strand synthesis; its persistence shortens telomeres, establishing a direct, replication-coupled mechanism at chromosome ends (Nature Structural & Molecular Biology, 7 May 2024; https://doi.org/10.1038/s41594-024-01279-6) (wondisford2024deregulateddnaadpribosylation pages 1-2). PARP2 promotes replication-stress-induced BIR and MiDAS at telomeres, preventing loss under oxidative damage or BLM depletion (Nature Communications, 26 April 2024; https://doi.org/10.1038/s41467-024-47222-7) (muoio2024parp2promotesbreak pages 1-2).
- ALT/SLX4/ATR–PCNA: In ALT cells, ATR phosphorylates RAD18 to restrain PCNA monoubiquitination, preventing excessive SLX4 accumulation at stalled forks and preserving telomere stability (The EMBO Journal, 11 March 2024; https://doi.org/10.1038/s44318-024-00066-9) (chen2024atrlimitsrad18mediated pages 1-2). Comprehensive ALT review confirms SLX4’s role in recombination-mediated telomere maintenance, ALT prevalence 5–10% overall and higher in certain cancers (Journal of Clinical Pathology, 27 Oct 2023 online first; 2024 issue; https://doi.org/10.1136/jcp-2023-209005) (mori2024alternativelengtheningof pages 1-1). Classic mechanistic study shows SLX4 recruited by TRF2 to process telomeric intermediates, preventing fragility (Nucleic Acids Research, 18 May 2015; https://doi.org/10.1093/nar/gkv522) (sarkar2015slx4contributesto pages 1-2).
- TRiC/TCAB1/dyskerin and telomerase: RIOK2 deficiency downregulates TRiC and dyskerin complex subunits, impairs telomerase, and shortens telomeres in human cells; ectopic RIOK2 rescues shortening (Nature Communications, 28 Aug 2024; https://doi.org/10.1038/s41467-024-51336-3) (ghosh2024riok2transcriptionallyregulates pages 1-2). General background on telomeres and shelterin functions also supports TRF2’s centrality (Frontiers in Cell and Developmental Biology, 9 Oct 2024; https://doi.org/10.3389/fcell.2024.1472906) (harman2024telomeremaintenanceand pages 4-5) and broader telomere literature synthesis (sola2024telomeresinterstitialtelomeric pages 96-99).
- RUVBL1/2: 2024 MM study defines transcriptional signatures of CB-6644 inhibition of RUVBL1/2; not telomere-specific but underscores broad roles of RUVBLs; annotation must be context-tethered to telomerase complexes (International Journal of Molecular Sciences, 20 Aug 2024; https://doi.org/10.3390/ijms25169022) (yi2024molecularsignaturesof pages 1-2).

5. Taxonomic Considerations
- SLX4, PARP1/2, TRF2, RTEL1, TRiC/TCAB1 functions are conserved in vertebrates and broadly in eukaryotes (TRiC in all eukaryotes). Applying Primates-only filters to CCT/TRiC is unjustified, and combining with archaeal thermosome (Set 1) is taxonomically incorrect: the archaeal thermosome α (IPR054827) is not present in Primates (ghosh2024riok2transcriptionallyregulates pages 1-2). ALT regulatory circuitry (ATR–RAD18–PCNA–SLX4) is studied in human cells; metazoan scope is reasonable (chen2024atrlimitsrad18mediated pages 1-2, mori2024alternativelengtheningof pages 1-1, sarkar2015slx4contributesto pages 1-2). RUVBL1/2 are eukaryote-wide; telomerase biogenesis roles are conserved but require co-complex context.

6. Rule Logic Assessment and Recommendations
- Remove or split Condition Set 1: Do not combine eukaryotic CCT conserved site (IPR002194) with archaeal thermosome α (IPR054827). If aiming to capture TRiC-linked positive regulation, require evidence of TCAB1/dyskerin/telomerase complex context or use a conjunction with telomerase-associated factors; expand taxon to Eukaryota or Vertebrata accordingly (ghosh2024riok2transcriptionallyregulates pages 1-2).
- Prioritize direct telomere actors:
  • Retain SLX4 (Set 9) with current taxon (Metazoa), possibly refine to Bilateria/Vertebrata if needed (sarkar2015slx4contributesto pages 1-2, chen2024atrlimitsrad18mediated pages 1-2, mori2024alternativelengtheningof pages 1-1).
  • Retain TRF2 (Set 2), but ensure domain specificity (TRFH plus Myb/SANT) rather than broad FunFam names to avoid non-TRF Myb proteins (harman2024telomeremaintenanceand pages 4-5, sola2024telomeresinterstitialtelomeric pages 96-99).
  • Retain RTEL1 (Set 6) with recognizable helicase domain combinations specific to RTEL1 subfamily (harman2024telomeremaintenanceand pages 4-5).
- PARP logic (Set 4): Distinguish PARP subclasses. For GO:0032206, require tankyrase-specific architecture (ANK repeats + PARP catalytic ± SAM) for TRF1 regulation, or PARP1/2 with telomere evidence (e.g., PARP1/2 catalytic domain plus nuclear localization and absence of tankyrase ANKs) and restrict to Metazoa/Vertebrata; alternatively, add a qualifier “under replication stress” to align with PARP2/PARP1 telomeric roles (wondisford2024deregulateddnaadpribosylation pages 1-2, muoio2024parp2promotesbreak pages 1-2).
- ATM/MAPK (Sets 3 and 7): Remove or gate with stringent context (e.g., ATR—not generic ATM—plus ALT markers; MAPK only with demonstrated telomere-binding partners). Currently too broad and likely to annotate many non-telomeric kinases (chen2024atrlimitsrad18mediated pages 1-2, harman2024telomeremaintenanceand pages 4-5).
- RUVBL (Set 8): Restrict to cases where RUVBL1/2 signatures co-occur with H/ACA snoRNP/telomerase complex markers (dyskerin/NOP10/NHP2/NAF1) or TCAB1; otherwise high false positive risk (yi2024molecularsignaturesof pages 1-2, ghosh2024riok2transcriptionallyregulates pages 1-2).
- CCT subunit η (Set 5): Subunit-level FunFams are ubiquitous; require co-evidence for telomerase assembly (TCAB1/dyskerin) or RIOK2-like transcriptional module to predict positive regulation (ghosh2024riok2transcriptionallyregulates pages 1-2).

7. Current Applications, Expert Views, and Data
- ALT biomarkers and therapy: ALT is 5–10% of cancers, enriched in sarcomas, IDH-mutant astrocytomas, pNETs, neuroblastoma; detection via ultrabright telomeric foci or C-circles; SLX4 participates in resolution steps and is regulated by DDR/PCNA ubiquitination (J Clin Pathol 2024) (mori2024alternativelengtheningof pages 1-1). ATR’s constraint of Ub-PCNA–SLX4 at ALT telomeres identifies a regulatory axis and potential therapeutic angle (EMBO J 2024) (chen2024atrlimitsrad18mediated pages 1-2).
- Quantitative/statistical highlights: ALT prevalence 5–10% overall (mori2024alternativelengtheningof pages 1-1); direct telomeric DNA-ADPr observed and abolished by PARP inhibition or PARP1 knockdown (wondisford2024deregulateddnaadpribosylation pages 1-2); PARP2-driven MiDAS depends on POLD3 (muoio2024parp2promotesbreak pages 1-2). RIOK2 overexpression reduced telomere shortening in patient fibroblasts (ghosh2024riok2transcriptionallyregulates pages 1-2).

8. Conclusion
ARBA00047239 has a strong basis when applied to direct telomere factors (SLX4, TRF2, RTEL1) and to PARP1/2 with telomeric replication-stress context, and to TRiC/TRiC-associated factors with explicit telomerase assembly links. It is likely over-permissive for broad families (ATM, MAPK, RUVBL, generic CCT subunits) without additional constraints. Taxonomic inconsistencies should be corrected. Implementing the recommendations above will improve precision and biological validity of GO:0032206 predictions.

Citations
- Harman A, Bryan TM. Telomere maintenance and the DNA damage response: a paradoxical alliance. Frontiers in Cell and Developmental Biology, 9 Oct 2024. https://doi.org/10.3389/fcell.2024.1472906 (harman2024telomeremaintenanceand pages 4-5).
- Wondisford AR et al. Deregulated DNA ADP-ribosylation impairs telomere replication. Nature Structural & Molecular Biology, 7 May 2024. https://doi.org/10.1038/s41594-024-01279-6 (wondisford2024deregulateddnaadpribosylation pages 1-2).
- Muoio D et al. PARP2 promotes Break Induced Replication-mediated telomere fragility in response to replication stress. Nature Communications, 26 Apr 2024. https://doi.org/10.1038/s41467-024-47222-7 (muoio2024parp2promotesbreak pages 1-2).
- Chen S et al. ATR limits Rad18-mediated PCNA monoubiquitination to preserve replication fork and telomerase-independent telomere stability. The EMBO Journal, 11 Mar 2024. https://doi.org/10.1038/s44318-024-00066-9 (chen2024atrlimitsrad18mediated pages 1-2).
- Mori JO, Keegan J, Flynn RL, Heaphy CM. Alternative lengthening of telomeres: mechanism and the pathogenesis of cancer. Journal of Clinical Pathology, 2024 (online first 27 Oct 2023). https://doi.org/10.1136/jcp-2023-209005 (mori2024alternativelengtheningof pages 1-1).
- Sarkar J et al. SLX4 contributes to telomere preservation and regulated processing of telomeric joint molecule intermediates. Nucleic Acids Research, 18 May 2015. https://doi.org/10.1093/nar/gkv522 (sarkar2015slx4contributesto pages 1-2).
- Ghosh S et al. RIOK2 transcriptionally regulates TRiC and dyskerin complexes to prevent telomere shortening. Nature Communications, 28 Aug 2024. https://doi.org/10.1038/s41467-024-51336-3 (ghosh2024riok2transcriptionallyregulates pages 1-2).
- Sola L. Telomeres, interstitial telomeric sequences and their transcription. 2024. (sola2024telomeresinterstitialtelomeric pages 96-99).

References

1. (sarkar2015slx4contributesto pages 1-2): Jaya Sarkar, Bingbing Wan, Jinhu Yin, Haritha Vallabhaneni, Kent Horvath, Tomasz Kulikowicz, Vilhelm A. Bohr, Yanbin Zhang, Ming Lei, and Yie Liu. Slx4 contributes to telomere preservation and regulated processing of telomeric joint molecule intermediates. Nucleic Acids Research, 43:5912-5923, May 2015. URL: https://doi.org/10.1093/nar/gkv522, doi:10.1093/nar/gkv522. This article has 81 citations and is from a highest quality peer-reviewed journal.

2. (chen2024atrlimitsrad18mediated pages 1-2): Siyuan Chen, Chen Pan, Jun Huang, and Tingting Liu. Atr limits rad18-mediated pcna monoubiquitination to preserve replication fork and telomerase-independent telomere stability. The EMBO Journal, 43:1301-1324, Mar 2024. URL: https://doi.org/10.1038/s44318-024-00066-9, doi:10.1038/s44318-024-00066-9. This article has 12 citations.

3. (mori2024alternativelengtheningof pages 1-1): Joakin O Mori, Joshua Keegan, Rachel L Flynn, and Christopher M Heaphy. Alternative lengthening of telomeres: mechanism and the pathogenesis of cancer. Journal of Clinical Pathology, 77:82-86, Oct 2024. URL: https://doi.org/10.1136/jcp-2023-209005, doi:10.1136/jcp-2023-209005. This article has 22 citations and is from a peer-reviewed journal.

4. (wondisford2024deregulateddnaadpribosylation pages 1-2): Anne R. Wondisford, Junyeop Lee, Robert Lu, Marion Schuller, Josephine Groslambert, Ragini Bhargava, Sandra Schamus-Haynes, Leyneir C. Cespedes, Patricia L. Opresko, Hilda A. Pickett, Jaewon Min, Ivan Ahel, and Roderick J. O’Sullivan. Deregulated dna adp-ribosylation impairs telomere replication. Nature Structural & Molecular Biology, 31:791-800, May 2024. URL: https://doi.org/10.1038/s41594-024-01279-6, doi:10.1038/s41594-024-01279-6. This article has 10 citations and is from a highest quality peer-reviewed journal.

5. (muoio2024parp2promotesbreak pages 1-2): Daniela Muoio, Natalie Laspata, Rachel L. Dannenberg, Caroline Curry, Simone Darkoa-Larbi, Mark Hedglin, Shikhar Uttam, and Elise Fouquerel. Parp2 promotes break induced replication-mediated telomere fragility in response to replication stress. Nature Communications, Apr 2024. URL: https://doi.org/10.1038/s41467-024-47222-7, doi:10.1038/s41467-024-47222-7. This article has 12 citations and is from a highest quality peer-reviewed journal.

6. (sola2024telomeresinterstitialtelomeric pages 96-99): L Sola. Telomeres, interstitial telomeric sequences and their transcription. Unknown journal, 2024.

7. (ghosh2024riok2transcriptionallyregulates pages 1-2): Shrestha Ghosh, Mileena T. Nguyen, Ha Eun Choi, Maximilian Stahl, Annemarie Luise Kühn, Sandra Van der Auwera, Hans J. Grabe, Henry Völzke, Georg Homuth, Samuel A. Myers, Cory M. Hogaboam, Imre Noth, Fernando J. Martinez, Gregory A. Petsko, and Laurie H. Glimcher. Riok2 transcriptionally regulates tric and dyskerin complexes to prevent telomere shortening. Nature Communications, Aug 2024. URL: https://doi.org/10.1038/s41467-024-51336-3, doi:10.1038/s41467-024-51336-3. This article has 6 citations and is from a highest quality peer-reviewed journal.

8. (harman2024telomeremaintenanceand pages 4-5): Ashley Harman and Tracy M. Bryan. Telomere maintenance and the dna damage response: a paradoxical alliance. Frontiers in Cell and Developmental Biology, Oct 2024. URL: https://doi.org/10.3389/fcell.2024.1472906, doi:10.3389/fcell.2024.1472906. This article has 8 citations and is from a poor quality or predatory journal.

9. (yi2024molecularsignaturesof pages 1-2): Weijun Yi, Sebastian A. Dziadowicz, Rachel S. Mangano, Lei Wang, Joseph McBee, Steven M. Frisch, Lori A. Hazlehurst, Donald A. Adjeroh, and Gangqing Hu. Molecular signatures of cb-6644 inhibition of the ruvbl1/2 complex in multiple myeloma. International Journal of Molecular Sciences, 25:9022, Aug 2024. URL: https://doi.org/10.3390/ijms25169022, doi:10.3390/ijms25169022. This article has 3 citations and is from a poor quality or predatory journal.

## Citations

1. mori2024alternativelengtheningof pages 1-1
2. wondisford2024deregulateddnaadpribosylation pages 1-2
3. sola2024telomeresinterstitialtelomeric pages 96-99
4. harman2024telomeremaintenanceand pages 4-5
5. yi2024molecularsignaturesof pages 1-2
6. ADP-ribose
7. https://doi.org/10.1038/s41594-024-01279-6
8. https://doi.org/10.1038/s41467-024-47222-7
9. https://doi.org/10.1038/s44318-024-00066-9
10. https://doi.org/10.1136/jcp-2023-209005
11. https://doi.org/10.1093/nar/gkv522
12. https://doi.org/10.1038/s41467-024-51336-3
13. https://doi.org/10.3389/fcell.2024.1472906
14. https://doi.org/10.3390/ijms25169022
15. https://doi.org/10.1093/nar/gkv522,
16. https://doi.org/10.1038/s44318-024-00066-9,
17. https://doi.org/10.1136/jcp-2023-209005,
18. https://doi.org/10.1038/s41594-024-01279-6,
19. https://doi.org/10.1038/s41467-024-47222-7,
20. https://doi.org/10.1038/s41467-024-51336-3,
21. https://doi.org/10.3389/fcell.2024.1472906,
22. https://doi.org/10.3390/ijms25169022,