# Cupriavidus necator H16 (historically Alcaligenes eutrophus H16) acoA: source-grounded review

## Identity and native context

Current CUPNH records use H16 strain tax381666. Each links the original M66060 clone and later AM260480 genome; all three are sequence version3, so locus identity is secure without claiming every current residue was assayed in 1991.

AcoA is the alpha subunit of the thiamine-diphosphate-dependent acetoin-cleaving E1 enzyme in Cupriavidus necator H16 (historically Alcaligenes eutrophus H16). Together with the complementary E1 subunit it contributes to acetoin cleavage, releasing acetaldehyde and supplying an acetyl equivalent to the lipoyl-bearing E2 acetyltransferase. Native acetoin-grown cells yield a probable alpha2-beta2 E1 tetramer. DCPIP-dependent production of acetate in vitro is distinct from physiological transfer of acetyl to the lipoyl system.

## Assays and limits

[PMID:2061286] "Ao:DCPIP OR consisted of alpha and
beta subunits (Mrs, 35,500 and 36,000, respectively), and a tetrameric alpha 2
beta 2 structure was most likely for the native protein."

[PMID:1898934] "The combination of purified Ao:DCPIP OR, DHLTA, and
DHLDH in the presence of thiamine pyrophosphate and the substrate acetoin or
methylacetoin resulted in a coenzyme A-dependent reduction of NAD."

DCPIP is an artificial electron acceptor. Its oxidative-hydrolytic cleavage assay does not by itself establish physiological lipoyl acetylation or autonomous activity of either isolated E1 subunit. PMID1898934 explicitly reports native Pelobacter E1/E2/E3 reconstitution with CoA-dependent NAD reduction. The 1994 gene paper maps purified components to acoABCL; heterologous expression is a distinct observation. H16 lacks an identified E3 in acoXABC; a Pelobacter AcoL must not be silently imported as its native partner. Bacillus physiological evidence is strongest at the native aco system and E1 activity; E2/E3 assignments retain their sequence-inference status.

## All-row decisions and ontology

- GO:0004739 (IEA): MARK_AS_OVER_ANNOTATED. GO:0004739 specifically oxidatively decarboxylates pyruvate with release of CO2; acetoin cleavage releases acetaldehyde instead. The native protein is mapped to the acetoin system by purified-protein N termini and its aco locus. The shared dehydrogenase family supports related chemistry but overextends substrate or complex specificity here. This assessment does not assert that an unmeasured pyruvate side activity or secondary complex association is impossible. The original TreeGrafter node is preserved; it is not treated as a new pairwise experimental assay.
- GO:0006086 (IEA): MARK_AS_OVER_ANNOTATED. GO:0006086 specifically converts pyruvate to acetyl-CoA, not acetoin to acetyl-CoA. The native protein is mapped to the acetoin system by purified-protein N termini and its aco locus. The shared dehydrogenase family supports related chemistry but overextends substrate or complex specificity here. This assessment does not assert that an unmeasured pyruvate side activity or secondary complex association is impossible. The original TreeGrafter node is preserved; it is not treated as a new pairwise experimental assay.
- GO:0016624 (IEA): ACCEPT. The native AcoA/AcoB assembly and lipoyl-linked acetoin system support this broad redox activity. Cupriavidus necator H16 (historically Alcaligenes eutrophus H16) AcoA contributes as a subunit; the original relationship field is preserved and is not used to reject the claim. The DCPIP assay alone does not demonstrate physiological disulfide reduction; that interpretation uses the E1/E2/E3 system, directly reconstituted in Pelobacter and inferred for homologous native systems.
- GO:0045150 (IEA): ACCEPT. AcoA performs part of the acetoin catabolic enzyme system: E1 acetoin cleavage together with AcoB. Native protein identification and comparative biochemical evidence support this participation, rather than a downstream phenotype alone.

GO:0004739 specifically uses pyruvate and releases CO2. GO:0019152 is acetoin/diacetyl NAD-dependent interconversion, not the acetoin-cleaving E1 reaction. GO:0016624 is therefore the compatible broad E1 chemistry. E2 GO:0004742 is reversible and used toward acetyl-CoA formation here. E3 GO:0004148 explicitly uses a protein-bound lipoyl substrate and NAD+. No new process annotation is proposed merely for pathway completeness.

PAINT source assertions were read in the committed PTHR11516 and PTHR22912 paint slices. PTN008519424 activity/process and PTN000162370 complex assertions are retained as original provenance; no branch-specific loss was inferred without a target placement. PTN000530299 supports general E3 chemistry and FAD binding; it does not resolve target partner sharing. The presence of a small donor set is not the objection.

## Acquisition and provenance

All original non-review annotation fields and both raw files are preserved against the captured baseline. Normal Falcon plus perplexity-lite attempts failed authentication/quota; no generated provider report is invented. Normal gene-publication retrieval completed successfully. An actual FEBA attempt failed because no reachable mapped source was available; no fitness result is inferred. PMID10368162 is full text; 2061286, 8110297 and 1898934 remain abstract-only after normal force and provider-chain attempts. EuropePMC scanned-PDF access also returned 403. The initial candidate PMID2200674 proved to be an unrelated Bacillus stearothermophilus pyruvate E1 paper and is not cited as Pelobacter evidence.

## Independent lipoyl-mechanism review

Full PMID20508247 explains the TPP-bound hydroxyethyl intermediate and E2 lipoyl acylation. It reports: "Reconstituted AoDH containing the E1, E2, and E3 subunits from the bacterium Pelobacter carbinolicus is specific for acetoin and does not use pyruvate or α-ketoglutarate as substrate ( 162 )." This is secondary evidence of whole-complex substrate specificity, not a newly inspected negative assay in the abstract-only primary. It does not exclude E2/E3 sharing with other native partners or establish H16/Bacillus isolated-subunit kinetics.
