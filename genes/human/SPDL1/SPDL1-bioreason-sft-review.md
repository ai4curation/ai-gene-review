# BioReason SFT Review: SPDL1 (Spindly)

**UniProt:** Q96EA4 | **Gene:** SPDL1 (CCDC99) | **Organism:** Homo sapiens

## Overall Assessment

BioReason's SFT model analysis of SPDL1 captures the broad functional profile correctly but contains several specific factual errors about binding partners and molecular mechanisms that are not supported by the published literature.

**Accuracy grade: B-** (core function identified correctly; significant errors in molecular details)

## Correct Claims

1. **Domain architecture**: Correctly identifies IPR028593 (Protein Spindly, chordates, residues 1-605) and IPR051149 (Spindly/BICDR Dynein Motor Adapter, residues 3-468). The coiled-coil N-terminal/mid-region as the motor-adapter module is accurately described.

2. **Core function as dynein adaptor**: The central description of Spindly as a dynein-recruiting kinetochore adaptor is correct. PMID:17576797 (Griffis et al. 2007) and PMID:19468067 (Chan et al. 2009) established this function.

3. **GO term associations**: The functional summary correctly associates Spindly with GO:0019899 (enzyme binding), GO:0007080 (mitotic metaphase chromosome alignment), GO:0000132 (establishment of mitotic spindle orientation), GO:0034501 (protein localization to kinetochore), GO:0016477 (cell migration), GO:0000940 (outer kinetochore), GO:0000922 (spindle pole), GO:0005829 (cytosol), and GO:0005634 (nucleus). All are validated by experimental evidence.

4. **Cell migration role**: Correctly notes the cell migration function, supported by PMID:30258100 (Conte et al. 2018).

5. **Subcellular localization cycle**: Accurately describes Spindly cycling between cytosol/nucleus (interphase), outer kinetochore (prometaphase), and spindle pole (metaphase).

## Errors and Unsupported Claims

### Error 1: Binding partners - BUB1B/BUB3 and NDC80 complex
**Claim:** "the adaptor binds outer-kinetochore receptors such as BUB1B/BUB3 and the NDC80 complex to anchor dynein"
**Verdict:** INCORRECT. Spindly is recruited to kinetochores via the RZZ complex (Rod/ZW10/Zwilch), NOT via BUB1B/BUB3 or NDC80. While NDC80/Hec1 is required upstream for RZZ recruitment to kinetochores (PMID:19468067), Spindly does not directly bind NDC80. The Spindly-RZZ interaction is well-documented: "RZZ members (ZW10 and Rod), but not dynein, could be coimmunoprecipitated with hSpindly" (PMID:19468067).

### Error 2: SKA1/2/3 and CENP-F interactions
**Claim:** "The same scaffold can engage additional kinetochore modules (SKA1/2/3, CENP-F) to stabilize end-on attachments"
**Verdict:** UNSUPPORTED. There is no published evidence that Spindly directly engages the SKA complex or CENP-F. These are independent outer kinetochore components with distinct recruitment mechanisms.

### Error 3: HOX-D13 as a partner
**Claim:** lists "developmental regulators like HOX-D13" as an observed partner
**Verdict:** HALLUCINATED. There is no evidence in any published study linking Spindly to HOXD13. This appears to be a model confabulation.

### Error 4: MKLN1 (muskelin) confused with BICDR
**Claim:** "association with MKLN1 (BICDR) tunes dynein loading in interphase"
**Verdict:** INCORRECT identification. MKLN1 is muskelin, a kelch-repeat/LisH-domain protein involved in the CTLH complex. The related dynein adaptor is BICDL1/BICDR1 (BICD family-like cargo adapter 1), encoded by BICDL1 (not MKLN1). These are entirely different proteins.

### Error 5: GO:0098806 "Spindly-BICDR complex"
**Claim:** presence in "GO:0098806 Spindly-BICDR complex"
**Verdict:** This GO term does not appear to exist in the Gene Ontology. The Spindly/BICDR family relationship is at the InterPro domain level (IPR051149), not as a named GO complex.

### Error 6: PLK1 and CDC20 as direct Spindly regulatory partners
**Claim:** "Phosphorylation by PLK1 and checkpoint factors modulates its affinity and timing"
**Verdict:** PARTIALLY CORRECT but misleading. PLK1 phosphorylates dynein intermediate chains (PMID:21507953), which affects kinetochore dynein recruitment. However, PLK1 phosphorylation of Spindly itself is not the primary regulatory mechanism. Aurora B, not PLK1, is the established kinase controlling Spindly kinetochore localization (PMID:19468067). The Spindly-CDC20 interaction is not established in the literature.

## Missing Key Information

1. **Farnesylation requirement**: BioReason fails to mention that C-terminal farnesylation of Spindly is essential for kinetochore targeting and RZZ interaction (PMID:25825516, PMID:25808490). This is a major mechanistic detail.

2. **Corona expansion function**: The recently discovered dynein-independent function of Spindly in driving kinetochore corona/fibrous corona expansion through RZZ-Spindly oligomerization (PMID:29915359, Sacristan et al. 2018) is not mentioned.

3. **Conserved Spindly motif**: The conserved motif essential for dynein recruitment, identified in PMID:20439434 (Gassmann et al. 2010), is not discussed.

4. **USP45 interaction and monoubiquitination**: While cell migration is mentioned, the specific mechanism involving USP45-mediated deubiquitination of monoubiquitinated Spindly (PMID:30258100) is not described.

5. **Species-specific differences**: The critical finding that human Spindly, unlike Drosophila Spindly, is NOT required for checkpoint protein (MAD2, ZW10) removal from kinetochores (PMID:19468067) is absent.

## GO Term Prediction Assessment

BioReason's GO predictions section was empty (no specific MF, BP, or CC predictions made beyond the thinking trace), which is a missed opportunity given the well-characterized functions of this protein.

## Reference Verification Summary

All PMIDs cited in the GOA annotations for SPDL1 were verified as real publications:
- PMID:17576797 - Griffis et al. 2007, J Cell Biol (discovery paper)
- PMID:19468067 - Chan et al. 2009, J Cell Biol (human characterization)
- PMID:23382074 - Armour et al. 2013, Mol Cell Biol (SIRT1 interactome)
- PMID:25035494 - McKenney et al. 2014, Science (dynein activation)
- PMID:25416956 - Rolland et al. 2014, Cell (interactome)
- PMID:25910212 - Sahni et al. 2015, Cell (interactome perturbations)
- PMID:26871637 - Yang et al. 2016, Cell (alternative splicing)
- PMID:30258100 - Conte et al. 2018, Sci Rep (USP45-Spindly)
- PMID:33961781 - Huttlin et al. 2021, Cell (BioPlex 3.0)

All Reactome pathway references are valid entries in the Reactome database.

## Conclusion

BioReason's analysis demonstrates competence at identifying broad protein function from domain architecture (InterPro) but exhibits weaknesses in specific protein-protein interaction details and regulatory mechanisms. The model appears to hallucinate specific binding partners (BUB1B, NDC80 as direct Spindly receptors; SKA complex; CENP-F; HOX-D13) and confuses related but distinct proteins (MKLN1 vs BICDL1). For curation purposes, the analysis is useful as a starting framework but requires substantial verification and correction of molecular details.
