# Saro_2595 (Q2G542) — beta-aryl ether pathway review

## 2026-11-02 — source-specific curation

The normally fetched UniProt record identifies Q2G542 as Saro_2595 in Novosphingobium aromaticivorans F199/DSM12444 (NCBITaxon:279238). The seeded GOA review contains zero annotations. It is retained as an empty existing_annotations list; this is not an ND assertion and no NEW rows are manufactured. The raw UniProt and GOA files are unchanged.

Saro_2595 encodes NaGSTNu, a homodimeric Nu-class glutathione transferase-family enzyme that removes glutathione from both stereoisomers of beta-glutathionyl-gamma-hydroxypropiovanillone in Novosphingobium aromaticivorans F199. Using a second glutathione molecule, it produces gamma-hydroxypropiovanillone and glutathione disulfide. This intracellular deglutathionylation step completes the conversion of glutathionylated intermediates generated during beta-aryl ether cleavage; native deletion experiments establish its requirement for complete GGE metabolism. It accepts both epimers but has a higher measured catalytic efficiency for the beta(S) substrate.

- The native knockout targets Saro_2595, which encodes NaGSTNu. [PMID:29449375 "we generated an N. aromaticivorans strain (12444Δ2595) lacking Saro_2595, the gene that encodes NaGSTNu."]
- NaGSTNu removes glutathione from both GS-HPV stereoisomers. [PMID:29449375 "We found that recombinant NaGSTNu cleaved both stereoisomers of GS-HPV in vitro"]
- The beta(S) epimer has approximately fourfold higher measured catalytic efficiency. [PMID:29449375 "resulting in a ∼4-fold higher kcat/Km with the β(S)-isomer"]
- Deglutathionylation yields HPV and GSSG using a second glutathione. [PMID:29449375 "the glutathione moiety is removed from GS-HPV and combined with another GSH, producing hydroxypropiovanillone (HPV) and glutathione disulfide (GSSG)."]
- Native genetics establishes that NaGSTNu is required for complete GGE metabolism. [PMID:29449375 "These results show that NaGSTNu is necessary for complete GGE metabolism by N. aromaticivorans."]
- The characterized enzyme is a homodimer with GST-domain architecture. [PMID:29449375 "NaGSTNu is a homodimer; each subunit contains a characteristic N-terminal GST1 (thioredoxin-like) domain"]
- The GSH-activation mechanism is proposed from structural placement and mutational evidence, not directly observed thiolate chemistry. [PMID:29449375 "We propose that the thiol of a GSH molecule in the GSH1 active-site position of NaGSTNu is activated by hydrogen-bonding with the side-chain hydroxyl of Thr51 (3.0 Å) and the side-chain amide of Asn53 (3.2 Å)"]
- The fetched protein has the recorded family/domain classification PTHR44051:SF22 (DISULFIDE-BOND OXIDOREDUCTASE YGHU); this membership alone does not establish its substrate stereospecificity. [file:NOVAD/Saro_2595/Saro_2595-uniprot.txt "DR PANTHER; PTHR44051:SF22; DISULFIDE-BOND OXIDOREDUCTASE YGHU; 1."]

### Ontology and evidence limits

Live QuickGO definitions were checked on 2026-11-02. [GO:0004364](https://www.ebi.ac.uk/QuickGO/term/GO:0004364) says: "Catalysis of the reaction: RX + glutathione = an S-substituted glutathione + a halide anion + H+." Beta-aryl ether cleavage instead releases a phenol. [GO:0016846](https://www.ebi.ac.uk/QuickGO/term/GO:0016846) says: "Catalysis of the elimination of hydrogen sulfide or substituted H2S." That definition does not establish the reductive GS-HPV deglutathionylation reaction. [GO:0016765](https://www.ebi.ac.uk/QuickGO/term/GO:0016765) describes transfer of an alkyl or aryl group between compounds and is a chemically appropriate broad parent for etherase substitution. The proposed terms state the exact reactions; neither a generic GST label nor an ill-fitting GO reaction is substituted for the evidence.

[GO:0046274](https://www.ebi.ac.uk/QuickGO/term/GO:0046274) describes breakdown of lignin polymers. The alpha-keto model-dimer assays establish specific dimer chemistry, not unrestricted polymer depolymerization, so no new lignin-catabolism annotation is asserted. No cytosolic sub-compartment annotation is added from the broader intracellular-pathway context.

PANTHER labels, when present, were compared verbatim with interpro/panther/panther.obo. Saro_2091, Saro_2865, BaeA and BaeB share PTHR44051:SF8 despite different stereochemistry and partner requirements; its name is membership metadata, not a functional assay. NaGSTNu maps to PTHR44051:SF22. Saro_2405 has no PANTHER cross-reference in its fetched record and no family identifier is guessed.

### Research provenance and verification

A normal `just deep-research-falcon NOVAD Saro_2595` attempt failed with HTTP 403 authentication (missing, invalid or unauthorized key). No provider report was fabricated. Primary-literature reading supplies the evidence above; saved command logs record the failure. The primary studies were checked in cached PubMed/PMC full text, and all quoted findings were matched against those cached sources. Focused validation, rendering, raw-record preservation and a helper-generated history record are checked for this session.

## 2026-11-03 — shared proposed-term definition

PR5930 follow-up reconciles the shared proposed activity with the canonical definition, GO parent and chemistry-specific justification in `analysis/module_audits/bacterial_beta_aryl_ether_dimer_cleavage/canonical-proposed-terms.yaml`. Gene-specific evidence and stereoselectivity are retained. The broad parent is not substituted for the precise proposed activity; BaeAB subunits continue to contribute to the assembled complex rather than receiving standalone full activity.
