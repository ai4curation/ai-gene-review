# Bacillus subtilis strain 168 acoB: source-grounded review

## Identity and native context

The accession is the strain168 reference protein (tax224308), with aco symbol and BSU locus verified before normal seeding. PMID10368162 studied168 (DSMZ402), with SMY as a growth comparator. AF006075 is the experimental clone set; AcoC has minor C-terminal differences from the reference sequence, explicitly reported by the authors.

AcoB is the beta subunit of the thiamine-diphosphate-dependent acetoin-cleaving E1 enzyme in Bacillus subtilis strain 168. Together with the complementary E1 subunit it contributes to acetoin cleavage, releasing acetaldehyde and supplying an acetyl equivalent to the lipoyl-bearing E2 acetyltransferase. Disruption of acoA abolishes detectable E1 activity and acetoin-supported growth of stationary cells. The acoABCL locus and conserved component architecture support the lipoyl-linked pathway; purified Bacillus subunit reconstitution has not been established by these experiments.

## Assays and limits

[PMID:10368162] "In
accordance with this, AoDH E1 was present in extracts of stationary
wild-type cells (0.016 U/mg of protein), while cell extracts of SA35
contained no detectable activity (<0.003 U/mg of protein) and gave no
stained band in the protein pattern during activity staining."

[PMID:1898934] "The combination of purified Ao:DCPIP OR, DHLTA, and
DHLDH in the presence of thiamine pyrophosphate and the substrate acetoin or
methylacetoin resulted in a coenzyme A-dependent reduction of NAD."

DCPIP is an artificial electron acceptor. Its oxidative-hydrolytic cleavage assay does not by itself establish physiological lipoyl acetylation or autonomous activity of either isolated E1 subunit. PMID1898934 explicitly reports native Pelobacter E1/E2/E3 reconstitution with CoA-dependent NAD reduction. The 1994 gene paper maps purified components to acoABCL; heterologous expression is a distinct observation. H16 lacks an identified E3 in acoXABC; a Pelobacter AcoL must not be silently imported as its native partner. Bacillus physiological evidence is strongest at the native aco system and E1 activity; E2/E3 assignments retain their sequence-inference status.

## All-row decisions and ontology

- GO:0045150 (IEA): ACCEPT. AcoB performs part of the acetoin catabolic enzyme system: the beta-subunit contribution to the E1 enzyme. Native Bacillus genetics establish the system-level role; the individual E2/E3 chemistry is supported by sequence and comparative biochemistry, not a separate subunit knockout.
- GO:0016624 (IC): NEW. The beta subunit is an identified structural component of active heteromeric E1, rather than a substrate consumed by the reaction. No existing molecular-function row covers this contribution. The proposed broad redox term avoids claiming that isolated AcoB catalyzes acetoin cleavage. Native-system evidence and comparative Pelobacter reconstitution support the physiological lipoyl-acceptor interpretation; the target-species DCPIP/genetic assay alone does not measure that acceptor.

GO:0004739 specifically uses pyruvate and releases CO2. GO:0019152 is acetoin/diacetyl NAD-dependent interconversion, not the acetoin-cleaving E1 reaction. GO:0016624 is therefore the compatible broad E1 chemistry. E2 GO:0004742 is reversible and used toward acetyl-CoA formation here. E3 GO:0004148 explicitly uses a protein-bound lipoyl substrate and NAD+. No new process annotation is proposed merely for pathway completeness.

PAINT source assertions were read in the committed PTHR11516 and PTHR22912 paint slices. PTN008519424 activity/process and PTN000162370 complex assertions are retained as original provenance; no branch-specific loss was inferred without a target placement. PTN000530299 supports general E3 chemistry and FAD binding; it does not resolve target partner sharing. The presence of a small donor set is not the objection.

## Acquisition and provenance

All original non-review annotation fields and both raw files are preserved against the captured baseline. Normal Falcon plus perplexity-lite attempts failed authentication/quota; no generated provider report is invented. Normal gene-publication retrieval completed successfully. An actual FEBA attempt failed because no reachable mapped source was available; no fitness result is inferred. PMID10368162 is full text; 2061286, 8110297 and 1898934 remain abstract-only after normal force and provider-chain attempts. EuropePMC scanned-PDF access also returned 403. The initial candidate PMID2200674 proved to be an unrelated Bacillus stearothermophilus pyruvate E1 paper and is not cited as Pelobacter evidence.

## Independent lipoyl-mechanism review

Full PMID20508247 explains the TPP-bound hydroxyethyl intermediate and E2 lipoyl acylation. It reports: "Reconstituted AoDH containing the E1, E2, and E3 subunits from the bacterium Pelobacter carbinolicus is specific for acetoin and does not use pyruvate or α-ketoglutarate as substrate ( 162 )." This is secondary evidence of whole-complex substrate specificity, not a newly inspected negative assay in the abstract-only primary. It does not exclude E2/E3 sharing with other native partners or establish H16/Bacillus isolated-subunit kinetics.
