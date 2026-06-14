# TRIM13 (RFP2 / Leu5) review notes

UniProt: O60858 (TRIM13_HUMAN). EC=2.3.2.27 (RING-type E3). TRIM/RBCC family.
ER membrane-anchored, single-pass membrane protein. Chromosome 13 (B-CLL minimal deletion region).

## Domain architecture
- RING-type zinc finger -> E3 ligase activity; required for autopolyubiquitination [UniProt DOMAIN]
- B-box + coiled-coil (coiled-coil required for induction of autophagy during ER stress) [UniProt DOMAIN]
- C-terminal transmembrane domain -> indispensable for ER localization [UniProt DOMAIN]
(No PRYSPRY; differs from TRIM5.)

## Core functions (UniProt FUNCTION + experimental)
1. ER membrane-anchored E3 ubiquitin ligase in ERAD: retrotranslocation/turnover of membrane and secretory proteins from the ER; acts on misfolded and regulated correctly-folded proteins. Interacts (via C-terminal domain) with VCP/p97. [PMID:17314412 "novel transmembrane E3 ubiquitin ligase involved in ERAD"; UniProt]
   - Supports GO:0036503 ERAD pathway (IDA, IBA), GO:0004842 ubiquitin-protein transferase (IDA), GO:0061659 ubiquitin-like protein ligase activity (IDA), GO:0043161 proteasome-mediated Ub-dependent catabolism (IDA), GO:0051865 protein autoubiquitination (IDA), GO:0005789 ER membrane (IDA/EXP).
2. Regulates ER-stress-induced autophagy / reticulophagy; coiled-coil required; colocalizes with p62/SQSTM1 and ZFYVE1 (DFCP1) at perinuclear ER; may act as tumor suppressor. [PMID:22178386 "TRIM13 regulates ER stress induced autophagy and clonogenic ability"]
   - Supports GO:0016239 positive regulation of macroautophagy (IDA, IBA), GO:0097038 perinuclear ER (IDA).
3. Apoptosis/DNA-damage: enhances ionizing-radiation-induced p53 stability and apoptosis by ubiquitinating MDM2 and AKT1 -> their proteasomal degradation, decreasing AKT1 kinase activity. [PMID:21333377 "Ret finger protein 2 enhances ionizing radiation-induced apoptosis via degradation of AKT and MDM2"]
4. NF-kB signaling - bidirectional:
   - Positive: stimulates NF-kB in TLR2 pathway; ubiquitinates TRAF6 via K29 chains -> NF-kB activation (PMID:28087809); participates in TCR-mediated NF-kB activation (PMID:25088585). HMP screen (PMID:12761501) and IDA (PMID:23077300) report TRIM13 activates NF-kB.
   - Negative: in presence of TNF, modulates IKK complex by regulating IKBKG/NEMO ubiquitination -> represses NF-kB (PMID:25152375 "TRIM13 regulates ubiquitination and turnover of NEMO to suppress TNF induced NF-kB activation").
   - The existing positive-regulation-of-NF-kB annotations (GO:0043123) are supported (TLR2/TRAF6). Keep, with note that TRIM13 is context-dependent.
5. Antiviral: in a broad TRIM screen (PMID:18248090), TRIM13 affected late stages of the retroviral life cycle (viral release). Also "negative regulation of viral transcription" (UniProt DR GO). The antiviral role is real but secondary/context.
   - GO:0140374 antiviral innate immune response (IDA PMID:18248090), GO:0044790 suppression of viral release by host (IDA PMID:18248090).

## Localization
- ER membrane (single-pass TM), perinuclear ER; concentrates with SQSTM1 and ZFYVE1. [UniProt; PMID:17314412; PMID:22178386]
- GO:0005737 cytoplasm (IBA/IEA) - generic; the specific localization is ER membrane.
- GO:0044322 ER quality control compartment (IEA GOC, inter-ontology from ERAD) - reasonable for an ERAD ligase.

## Notes on specific annotations
- GO:0003713 transcription coactivator activity (IDA PMID:23077300, ARUK-UCL): same caveat as TRIM5 - reflects NF-kB activation in a TRIM screen, not direct transcriptional coactivation. MARK_AS_OVER_ANNOTATED. NOTE: the YAML stub does NOT include this annotation in existing_annotations (it's in UniProt DR but not GOA stub), so only review what's present.
- GO:1904380 ER mannose trimming (TAS Reactome R-HSA-901032): TRIM13 placed in ERAD/ERQC Reactome pathway; mannose trimming itself is done by mannosidases, not TRIM13. This is a pathway-context over-annotation. MARK_AS_OVER_ANNOTATED.
- GO:0061630 ubiquitin protein ligase activity (multiple: IBA, IEA EC, TAS Reactome): core. ACCEPT representative; others ACCEPT/KEEP redundant.
- GO:0045893 positive regulation of DNA-templated transcription (IEA GO_REF:0000108): inter-ontology inference from transcription coactivator activity; over-annotation (TRIM13 not a direct transcriptional activator). MARK_AS_OVER_ANNOTATED.
- protein binding (GO:0005515) IPI: AKT1 (P31749), MDM2 (Q00987), VCP (P55072 - actually P55072 is VCP), Bcl2/Q13501? (PMID:22178386 with UniProtKB:Q13501 = SQSTM1? no, Q13501 = SQSTM1/p62). Bare protein binding -> KEEP_AS_NON_CORE.
  - PMID:21333377 IPI with P31749 (AKT1) and Q00987 (MDM2): substrate interactions.
  - PMID:17314412 IPI with P55072 (VCP/p97): ERAD partner.
  - PMID:22178386 IPI with Q13501 (SQSTM1/p62): autophagy partner.

## GO IDs verified relevant
- GO:0036503 ERAD pathway (core BP)
- GO:0061630 / GO:0004842 / GO:0061659 ubiquitin ligase/transferase (core MF)
- GO:0016239 positive regulation of macroautophagy
- GO:0043161 proteasome-mediated ubiquitin-dependent protein catabolic process
- GO:0051865 protein autoubiquitination
- GO:0005789 endoplasmic reticulum membrane (core CC)
- GO:0097038 perinuclear endoplasmic reticulum
- GO:0043123 positive regulation of canonical NF-kappaB signal transduction (supported, context-dependent)
