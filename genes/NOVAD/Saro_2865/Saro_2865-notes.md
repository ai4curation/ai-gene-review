# Saro_2865 (Q2G4C2) — beta-aryl ether pathway review

## 2026-11-02 — source-specific curation

The normally fetched UniProt record identifies Q2G4C2 as Saro_2865 in Novosphingobium aromaticivorans F199/DSM12444 (NCBITaxon:279238). The seeded GOA review contains zero annotations. It is retained as an empty existing_annotations list; this is not an ND assertion and no NEW rows are manufactured. The raw UniProt and GOA files are unchanged.

Saro_2865 encodes NaLigF2, a glutathione-dependent beta-aryl etherase of Novosphingobium aromaticivorans F199. It cleaves beta(S)-configured alpha-keto beta-O-4 aromatic dimers by replacing the aryloxy group with a glutathionyl group. Purified enzyme assays establish activity on model dimers containing guaiacyl and syringyl units. This chemistry contributes to the intracellular processing of small lignin-derived aromatics after oxidation of their benzylic alcohol groups.

- The assayed NaLigF2 enzyme is linked explicitly to Saro_2865 from DSM12444. [PMID:25232892 "Genes encoding potential Lig enzymes NaLigE (Saro_2405), NaLigF1 (Saro_2091), NaLigF2 (Saro_2865), and RpHypGST (RPA4340) were cloned from genomic DNA from N. aromaticivorans strain DSM12444 or Rhodopseudomonas palustris (R. palustris) strain CGA009, respectively."]
- NaLigF2 was tested individually with glutathione and four guaiacyl/syringyl model dimer classes. [PMID:25232892 "individual proteins NaLigE, NsLigE, SsLigE, SsLigP, NaLigF1, NaLigF2, or SsLigF1 (0.25 mg mL–1) were individually incubated with GSH and one of the racemic β-ethers GβG, GβS, SβG, or SβS (1.0 mM) as cosubstrates."]
- NaLigF2 belongs to the experimentally tested beta(S)-selective etherase group. [PMID:25232892 "each LigE/LigP β-etherase homologue has the conserved function of degrading β(R)-enantiomers whereas each LigF1/LigF2 β-etherase homologue exhibits stereospecificity for the β(S)-enantiomers."]
- NaLigF2 corresponds to the Saro_2865 locus in the comparative beta-etherase analysis. [PMID:30541921 "NaLigF2 (Saro_2865; WP_052241956.1)"]
- The fetched protein has the recorded family/domain classification PTHR44051:SF8 (GLUTATHIONE S-TRANSFERASE GSTA); this membership alone does not establish its substrate stereospecificity. [file:NOVAD/Saro_2865/Saro_2865-uniprot.txt "DR PANTHER; PTHR44051:SF8; GLUTATHIONE S-TRANSFERASE GSTA; 1."]

### Ontology and evidence limits

Live QuickGO definitions were checked on 2026-11-02. [GO:0004364](https://www.ebi.ac.uk/QuickGO/term/GO:0004364) says: "Catalysis of the reaction: RX + glutathione = an S-substituted glutathione + a halide anion + H+." Beta-aryl ether cleavage instead releases a phenol. [GO:0016846](https://www.ebi.ac.uk/QuickGO/term/GO:0016846) says: "Catalysis of the elimination of hydrogen sulfide or substituted H2S." That definition does not establish the reductive GS-HPV deglutathionylation reaction. [GO:0016765](https://www.ebi.ac.uk/QuickGO/term/GO:0016765) describes transfer of an alkyl or aryl group between compounds and is a chemically appropriate broad parent for etherase substitution. The proposed terms state the exact reactions; neither a generic GST label nor an ill-fitting GO reaction is substituted for the evidence.

[GO:0046274](https://www.ebi.ac.uk/QuickGO/term/GO:0046274) describes breakdown of lignin polymers. The alpha-keto model-dimer assays establish specific dimer chemistry, not unrestricted polymer depolymerization, so no new lignin-catabolism annotation is asserted. No cytosolic sub-compartment annotation is added from the broader intracellular-pathway context.

PANTHER labels, when present, were compared verbatim with interpro/panther/panther.obo. Saro_2091, Saro_2865, BaeA and BaeB share PTHR44051:SF8 despite different stereochemistry and partner requirements; its name is membership metadata, not a functional assay. NaGSTNu maps to PTHR44051:SF22. Saro_2405 has no PANTHER cross-reference in its fetched record and no family identifier is guessed.

The 2014 experiments establish activity of each purified NaLigF enzyme. They do not establish which one is indispensable in unmodified F199, so the native division of work remains a question. Picart et al. PMID:25186983 was inspected in abstract form; it supports enzyme-discovery and model-polymer context but cannot assign a particular native physiological or polymer assay to this exact locus without full-text details. Its abstract is therefore not used to support an additional core claim.

### Research provenance and verification

A normal `just deep-research-falcon NOVAD Saro_2865` attempt failed with HTTP 403 authentication (missing, invalid or unauthorized key). No provider report was fabricated. Primary-literature reading supplies the evidence above; saved command logs record the failure. The primary studies were checked in cached PubMed/PMC full text, and all quoted findings were matched against those cached sources. Focused validation, rendering, raw-record preservation and a helper-generated history record are checked for this session.

Product configuration qualification: PMID:25232892 directly compares the Na substrate preferences, but its explicit analysis of glutathionyl-product configuration names SsLigE, SsLigP and SsLigF (SYK-6). Reciprocal Na product configuration is the shared-mechanism interpretation, not a separate Na product-configuration measurement in that study.

## 2026-11-03 — shared proposed-term definition

PR5930 follow-up reconciles the shared proposed activity with the canonical definition, GO parent and chemistry-specific justification in `analysis/module_audits/bacterial_beta_aryl_ether_dimer_cleavage/canonical-proposed-terms.yaml`. Gene-specific evidence and stereoselectivity are retained. The broad parent is not substituted for the precise proposed activity; BaeAB subunits continue to contribute to the assembled complex rather than receiving standalone full activity.
