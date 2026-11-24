# Bacillus subtilis strain 168 acoL: source-grounded review

## Identity and native context

The accession is the strain168 reference protein (tax224308), with aco symbol and BSU locus verified before normal seeding. PMID10368162 studied168 (DSMZ402), with SMY as a growth comparator. AF006075 is the experimental clone set; AcoC has minor C-terminal differences from the reference sequence, explicitly reported by the authors.

AcoL is the FAD-dependent dihydrolipoyl dehydrogenase associated with the acetoin catabolic system in Bacillus subtilis strain 168. It reoxidizes the reduced protein-bound lipoyl cofactor while reducing NAD+, allowing repeated cycles of acetoin cleavage and acetyl-CoA production. Its E3 assignment is supported by the acoABCL locus, the native acetoin-use phenotype and conserved FAD-, NAD(H)- and redox-disulfide features; these observations do not establish a separately purified Bacillus E3 assay.

## Assays and limits

[PMID:10368162] "AcoL exhibited the putative flavin adenine dinucleotide-binding domain
( 5 ) at the N-terminal region, an active disulfide bridge
site at position Cys 38 and Cys 43 , a putative
NAD(H)-binding region in the central part, and the putative interface
region at the C terminus and therefore matched the characteristic
properties of dihydrolipoamide dehydrogenases ( 16 , 22 )."

[PMID:1898934] "DHLDH had a
native Mr of 110,000, consisted of two identical subunits of Mr 54,000, and
reacted only with NAD(H) as a coenzyme. The N-terminal amino acid sequence
included the flavin adenine dinucleotide-binding site and exhibited a high
degree of homology to other DHLDHs."

DCPIP is an artificial electron acceptor. Its oxidative-hydrolytic cleavage assay does not by itself establish physiological lipoyl acetylation or autonomous activity of either isolated E1 subunit. PMID1898934 explicitly reports native Pelobacter E1/E2/E3 reconstitution with CoA-dependent NAD reduction. The 1994 gene paper maps purified components to acoABCL; heterologous expression is a distinct observation. H16 lacks an identified E3 in acoXABC; a Pelobacter AcoL must not be silently imported as its native partner. Bacillus physiological evidence is strongest at the native aco system and E1 activity; E2/E3 assignments retain their sequence-inference status.

## All-row decisions and ontology

- GO:0004148 (IBA): ACCEPT. The NAD+-dependent reoxidation of reduced lipoyl residues is the E3 recycling step. The 1999 native locus study identifies the FAD/NAD(H)-binding and active-disulfide features of AcoL; curated sequence features and the PAINT PTN000530299 activity assertion corroborate a conserved E3 role. This is functional inference, not a purified Bacillus E3 measurement.
- GO:0004148 (IEA): ACCEPT. The NAD+-dependent reoxidation of reduced lipoyl residues is the E3 recycling step. The 1999 native locus study identifies the FAD/NAD(H)-binding and active-disulfide features of AcoL; curated sequence features and the PAINT PTN000530299 activity assertion corroborate a conserved E3 role. This is functional inference, not a purified Bacillus E3 measurement.
- GO:0005737 (IEA): ACCEPT. The curated UniProt cellular-location statement and soluble intracellular metabolic role support cytoplasmic localization. Retain the root cellular compartment without inventing a more specific localization assay or replacing it with an unsupported subcompartment.
- GO:0006103 (IBA): UNDECIDED. The reviewed native evidence assigns AcoL to acetoin turnover. A conserved E3 enzyme can in principle be shared among dehydrogenase systems, so acetoin association does not establish loss of 2-oxoglutarate-system function. The PAINT PTN000530299 IBD source includes genuine 2-oxoglutarate-system descendants, but target-specific partner sharing is not resolved by the locus paper. Retain uncertainty rather than infer absence from the accessible source or donor count.
- GO:0016491 (IEA): MODIFY. The broad redox classification is correct, but GO:0004148 specifies oxidation of protein-bound dihydrolipoyl groups with NAD+ and is already represented in this review. The Bacillus inference rests on the acoL architecture and native-system context; the Pelobacter assay is comparative evidence, not a Bacillus cofactor assay.
- GO:0016668 (IEA): MODIFY. The broad redox classification is correct, but GO:0004148 specifies oxidation of protein-bound dihydrolipoyl groups with NAD+ and is already represented in this review. The Bacillus inference rests on the acoL architecture and native-system context; the Pelobacter assay is comparative evidence, not a Bacillus cofactor assay.
- GO:0045150 (IEA): ACCEPT. AcoL performs part of the acetoin catabolic enzyme system: E3 lipoyl-cofactor reoxidation. Native Bacillus genetics establish the system-level role; the individual E2/E3 chemistry is supported by sequence and comparative biochemistry, not a separate subunit knockout.
- GO:0050660 (IBA): ACCEPT. The Bacillus primary sequence analysis identifies the N-terminal FAD-binding region, complemented by curated FAD-binding features and the PTN000530299 cofactor IBD. This is conserved cofactor inference, not a direct Bacillus stoichiometric measurement.
- GO:0050660 (IEA): ACCEPT. The Bacillus primary sequence analysis identifies the N-terminal FAD-binding region, complemented by curated FAD-binding features and the PTN000530299 cofactor IBD. This is conserved cofactor inference, not a direct Bacillus stoichiometric measurement.

GO:0004739 specifically uses pyruvate and releases CO2. GO:0019152 is acetoin/diacetyl NAD-dependent interconversion, not the acetoin-cleaving E1 reaction. GO:0016624 is therefore the compatible broad E1 chemistry. E2 GO:0004742 is reversible and used toward acetyl-CoA formation here. E3 GO:0004148 explicitly uses a protein-bound lipoyl substrate and NAD+. No new process annotation is proposed merely for pathway completeness.

PAINT source assertions were read in the committed PTHR11516 and PTHR22912 paint slices. PTN008519424 activity/process and PTN000162370 complex assertions are retained as original provenance; no branch-specific loss was inferred without a target placement. PTN000530299 supports general E3 chemistry and FAD binding; it does not resolve target partner sharing. The presence of a small donor set is not the objection.

## Acquisition and provenance

All original non-review annotation fields and both raw files are preserved against the captured baseline. Normal Falcon plus perplexity-lite attempts failed authentication/quota; no generated provider report is invented. Normal gene-publication retrieval completed successfully. An actual FEBA attempt failed because no reachable mapped source was available; no fitness result is inferred. PMID10368162 is full text; 2061286, 8110297 and 1898934 remain abstract-only after normal force and provider-chain attempts. EuropePMC scanned-PDF access also returned 403. The initial candidate PMID2200674 proved to be an unrelated Bacillus stearothermophilus pyruvate E1 paper and is not cited as Pelobacter evidence.

## 2026-11-02 — acetoin/butanediol module completion pass

- Deep research: no provider deep-research file exists for this gene, and none could be generated
  in this session (no deep-research provider API keys were configured). No deep-research file was
  written by hand. The review rests on the cached primary publications, the UniProt record and the
  PANTHER/PAINT family files cited in the review.
- Resolved the former UNDECIDED IBA row for GO:0006103 2-oxoglutarate metabolic process as
  MARK_AS_OVER_ANNOTATED. PTN000530299 is seeded by housekeeping E3s of the 2-oxoglutarate
  dehydrogenase complex; AcoL is the acoABCL-cluster E3, and B. subtilis separately encodes PdhD
  [PMID:20508247 "Bacillus subtilis contains the PDH E1α, E1β, E2, and E3 subunits (encoded by pdhA , pdhB , pdhC , and pdhD , respectively)"].
  Treated the same way as the Syntrophotalea AcoL IEA row.
