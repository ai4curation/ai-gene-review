# Syntrophotalea carbinolica (historically Pelobacter carbinolicus), strain Gra Bd 1 acoL: source-grounded review

## Identity and native context

Current SYNCB records use Syntrophotalea carbinolica species tax19; the historical name is Pelobacter carbinolicus. Both U01100 and L24124 cross-references map these accessions to strain Gra Bd 1. These original-paper records are intentionally retained rather than substituted with separate SYNC1 genome accessions.

AcoL is the FAD-dependent dihydrolipoyl dehydrogenase associated with the acetoin catabolic system in Syntrophotalea carbinolica (historically Pelobacter carbinolicus), strain Gra Bd 1. It reoxidizes the reduced protein-bound lipoyl cofactor while reducing NAD+, allowing repeated cycles of acetoin cleavage and acetyl-CoA production. Native AcoL was purified as a homodimer with NAD(H) specificity and contributes to reconstitution with the native E1 and E2 components.

## Assays and limits

[PMID:8110297] "Use of oligonucleotide probes, which were deduced from the N-terminal sequences
of the purified enzyme components, identified the structural genes for the alpha
and beta subunits of E1 (acetoin:2,6-dichlorophenolindophenol oxidoreductase),
E2 (dihydrolipoamide acetyltransferase), and E3 (dihydrolipoamide dehydrogenase)
of the Pelobacter carbinolicus acetoin dehydrogenase enzyme system, which were
designated acoA, acoB, acoC, and acoL, respectively."

[PMID:1898934] "The combination of purified Ao:DCPIP OR, DHLTA, and
DHLDH in the presence of thiamine pyrophosphate and the substrate acetoin or
methylacetoin resulted in a coenzyme A-dependent reduction of NAD."

DCPIP is an artificial electron acceptor. Its oxidative-hydrolytic cleavage assay does not by itself establish physiological lipoyl acetylation or autonomous activity of either isolated E1 subunit. PMID1898934 explicitly reports native Pelobacter E1/E2/E3 reconstitution with CoA-dependent NAD reduction. The 1994 gene paper maps purified components to acoABCL; heterologous expression is a distinct observation. H16 lacks an identified E3 in acoXABC; a Pelobacter AcoL must not be silently imported as its native partner. Bacillus physiological evidence is strongest at the native aco system and E1 activity; E2/E3 assignments retain their sequence-inference status.

## All-row decisions and ontology

- GO:0004148 (IEA): ACCEPT. The NAD+-dependent reoxidation of reduced lipoyl residues is the E3 recycling step. Native purified DHLDH is NAD(H)-specific and reconstitutes acetoin-dependent NAD reduction with native E1 and E2; the 1994 N-terminal mapping identifies this AcoL.
- GO:0006103 (IEA): UNDECIDED. The reviewed native evidence assigns AcoL to acetoin turnover. A conserved E3 enzyme can in principle be shared among dehydrogenase systems, so acetoin association does not establish loss of 2-oxoglutarate-system function. The TreeGrafter PTN000530396 transfer does not resolve which native multienzyme partners this AcoL actually services. Retain uncertainty rather than infer absence from the accessible source or donor count.
- GO:0016491 (IEA): MODIFY. The broad redox classification is correct, but GO:0004148 specifies oxidation of protein-bound dihydrolipoyl groups with NAD+ and is already represented in this review. Native purified Pelobacter DHLDH reacts only with NAD(H), so NADP is not asserted.
- GO:0016668 (IEA): MODIFY. The broad redox classification is correct, but GO:0004148 specifies oxidation of protein-bound dihydrolipoyl groups with NAD+ and is already represented in this review. Native purified Pelobacter DHLDH reacts only with NAD(H), so NADP is not asserted.
- GO:0050660 (IEA): ACCEPT. The purified Pelobacter enzyme has the FAD-binding N-terminal sequence, and independently curated PIRSR/RuleBase binding features support the FAD cofactor assignment.

GO:0004739 specifically uses pyruvate and releases CO2. GO:0019152 is acetoin/diacetyl NAD-dependent interconversion, not the acetoin-cleaving E1 reaction. GO:0016624 is therefore the compatible broad E1 chemistry. E2 GO:0004742 is reversible and used toward acetyl-CoA formation here. E3 GO:0004148 explicitly uses a protein-bound lipoyl substrate and NAD+. No new process annotation is proposed merely for pathway completeness.

PAINT source assertions were read in the committed PTHR11516 and PTHR22912 paint slices. PTN008519424 activity/process and PTN000162370 complex assertions are retained as original provenance; no branch-specific loss was inferred without a target placement. PTN000530299 supports general E3 chemistry and FAD binding; it does not resolve target partner sharing. The presence of a small donor set is not the objection.

## Acquisition and provenance

All original non-review annotation fields and both raw files are preserved against the captured baseline. Normal Falcon plus perplexity-lite attempts failed authentication/quota; no generated provider report is invented. Normal gene-publication retrieval completed successfully. An actual FEBA attempt failed because no reachable mapped source was available; no fitness result is inferred. PMID10368162 is full text; 2061286, 8110297 and 1898934 remain abstract-only after normal force and provider-chain attempts. EuropePMC scanned-PDF access also returned 403. The initial candidate PMID2200674 proved to be an unrelated Bacillus stearothermophilus pyruvate E1 paper and is not cited as Pelobacter evidence.

## Independent lipoyl-mechanism review

Full PMID20508247 explains the TPP-bound hydroxyethyl intermediate and E2 lipoyl acylation. It reports: "Reconstituted AoDH containing the E1, E2, and E3 subunits from the bacterium Pelobacter carbinolicus is specific for acetoin and does not use pyruvate or α-ketoglutarate as substrate ( 162 )." This is secondary evidence of whole-complex substrate specificity, not a newly inspected negative assay in the abstract-only primary. It does not exclude E2/E3 sharing with other native partners or establish H16/Bacillus isolated-subunit kinetics.
