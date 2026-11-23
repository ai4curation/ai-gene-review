# Saro_2873 (Q2G4B4) — beta-aryl ether pathway review

## 2026-11-02 — source-specific curation

The normally fetched UniProt record identifies Q2G4B4 as Saro_2873 in Novosphingobium aromaticivorans F199/DSM12444 (NCBITaxon:279238). The seeded GOA review contains zero annotations. It is retained as an empty existing_annotations list; this is not an ND assertion and no NEW rows are manufactured. The raw UniProt and GOA files are unchanged.

Saro_2873 encodes BaeA, one of the two glutathione S-transferase-like subunits of the BaeAB beta-aryl etherase in Novosphingobium aromaticivorans F199. Together with BaeB (Saro_2872), it forms a heterodimer that cleaves beta(R)-MPHPV into guaiacol and a glutathionylated hydroxypropiovanillone product, using glutathione. This reaction provides an alternative to NaLigE during intracellular aromatic-dimer metabolism; substantial activity requires both BaeAB subunits. BaeA residues Asn14 and Ser15 contribute to catalysis and substrate binding in the assembled enzyme.

- The exact F199 loci encode the two BaeAB subunits. [PMID:30541921 "we identify this β-etherase as a previously uncharacterized heterodimeric GST (named here BaeAB) encoded by Saro_2873 (baeA) and Saro_2872 (baeB)."]
- The heterodimer cleaves beta(R)-MPHPV but does not measurably act on beta(S)-MPHPV in the reported assay. [PMID:30541921 "the recombinant enzyme had no effect on β(S)-MPHPV and converted β(R)-MPHPV into GS-HPV and guaiacol"]
- Individual subunits exhibit only trace conversion; mixing both produces robust cleavage of half the racemic substrate. [PMID:30541921 "When the Saro_2873 or Saro_2872 polypeptides were individually incubated with racemic (β(R) and β(S)) MPHPV and GSH, only a trace amount of GS-HPV was observed (representing <1% conversion of the MPHPV present in the reaction)"]
- The purified complex has an apparent mass consistent with a heterodimer of the approximately 29-kDa subunits. [PMID:30541921 "We also analyzed the purified recombinant protein complex by gel permeation chromatography (GPC) and found that it eluted as a single peak with an apparent molecular weight of ∼59 kDa"]
- Loss of either subunit prevents beta(R)-MPHPV metabolism when NaLigE is also absent. [PMID:30541921 "loss of either Saro_2873 or Saro_2872 rendered 12444ΔligE unable to metabolize β(R)-MPHPV"]
- The BaeA Asn14 mutation strongly reduces turnover and apparent substrate affinity in the assembled complex. [PMID:30541921 "When we replaced Asn14 in BaeA with an alanine, we found that the resulting variant (A:N14A) had a kcat value ∼20-fold lower and a Km value ∼12.5-fold higher than WT BaeAB"]
- The fetched protein has the recorded family/domain classification PTHR44051:SF8 (GLUTATHIONE S-TRANSFERASE GSTA); this membership alone does not establish its substrate stereospecificity. [file:NOVAD/Saro_2873/Saro_2873-uniprot.txt "DR PANTHER; PTHR44051:SF8; GLUTATHIONE S-TRANSFERASE GSTA; 1."]

### Ontology and evidence limits

Live QuickGO definitions were checked on 2026-11-02. [GO:0004364](https://www.ebi.ac.uk/QuickGO/term/GO:0004364) says: "Catalysis of the reaction: RX + glutathione = an S-substituted glutathione + a halide anion + H+." Beta-aryl ether cleavage instead releases a phenol. [GO:0016846](https://www.ebi.ac.uk/QuickGO/term/GO:0016846) says: "Catalysis of the elimination of hydrogen sulfide or substituted H2S." That definition does not establish the reductive GS-HPV deglutathionylation reaction. [GO:0016765](https://www.ebi.ac.uk/QuickGO/term/GO:0016765) describes transfer of an alkyl or aryl group between compounds and is a chemically appropriate broad parent for etherase substitution. The proposed terms state the exact reactions; neither a generic GST label nor an ill-fitting GO reaction is substituted for the evidence.

[GO:0046274](https://www.ebi.ac.uk/QuickGO/term/GO:0046274) describes breakdown of lignin polymers. The alpha-keto model-dimer assays establish specific dimer chemistry, not unrestricted polymer depolymerization, so no new lignin-catabolism annotation is asserted. No cytosolic sub-compartment annotation is added from the broader intracellular-pathway context.

PANTHER labels, when present, were compared verbatim with interpro/panther/panther.obo. Saro_2091, Saro_2865, BaeA and BaeB share PTHR44051:SF8 despite different stereochemistry and partner requirements; its name is membership metadata, not a functional assay. NaGSTNu maps to PTHR44051:SF22. Saro_2405 has no PANTHER cross-reference in its fetched record and no family identifier is guessed.

BaeAB is one BaeA plus one BaeB. The isolated-subunit trace activity is retained rather than rewritten as an absolute zero, but it does not justify assigning substantial independent beta-etherase activity to either chain. The core uses contributes_to_molecular_function on GO:0016765; the precise proposed activity belongs to the complex. BaeB Ser14Ala neutrality is not evidence that BaeB is merely structural. Product GS-HPV was measured, but its epimer was not directly assigned in these BaeAB assays; stereoinversion is not presented as a separate direct BaeAB observation.

### Research provenance and verification

A normal `just deep-research-falcon NOVAD Saro_2873` attempt failed with HTTP 403 authentication (missing, invalid or unauthorized key). No provider report was fabricated. Primary-literature reading supplies the evidence above; saved command logs record the failure. The primary studies were checked in cached PubMed/PMC full text, and all quoted findings were matched against those cached sources. Focused validation, rendering, raw-record preservation and a helper-generated history record are checked for this session.

## 2026-11-03 — shared proposed-term definition

PR5930 follow-up reconciles the shared proposed activity with the canonical definition, GO parent and chemistry-specific justification in `analysis/module_audits/bacterial_beta_aryl_ether_dimer_cleavage/canonical-proposed-terms.yaml`. Gene-specific evidence and stereoselectivity are retained. The broad parent is not substituted for the precise proposed activity; BaeAB subunits continue to contribute to the assembled complex rather than receiving standalone full activity.
