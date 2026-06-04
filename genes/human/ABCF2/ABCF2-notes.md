# ABCF2 notes

## Deep research status

Falcon deep research was attempted for ABCF2 on 2026-06-03 with `just deep-research-falcon human ABCF2 --fallback perplexity-lite`. Falcon timed out after 600 seconds, and the configured fallback failed with a Perplexity 401 quota error. No provider deep-research file was produced. This review therefore uses the documented manual fallback: UniProt, GOA, cached publications, the local Reactome record, PN projection reports, and targeted primary-source checks.

## Function synthesis

ABCF2 is a soluble ABCF-family ATP-binding cassette protein, not a membrane transporter. UniProt records two ABC transporter domains and two ATP-binding sites, and cautions that ABCF2 "Lacks transmembrane domains and is probably not involved in transport" [file:human/ABCF2/ABCF2-uniprot.txt, "Lacks transmembrane domains and is probably not involved in transport"]. Bao et al. state the same distinction in primary literature: ABCF family proteins have nucleotide-binding domains but not transmembrane domains and "do not function as transporters of molecules across the membrane" [PMID:28112439 ABCF2, an Nrf2 target gene, contributes to cisplatin resistance in ovarian cancer cells., "Unlike other subgroups, ABCF members have NBDs but not TMDs, and thus do not function as transporters of molecules across the membrane"].

The strongest supported molecular-function model is therefore ATP binding/ATP hydrolysis activity for a cytosolic ABCF protein. There is not enough gene-level evidence to assign a specific biological process coupled to the ATPase cycle. ATP binding and ATP hydrolysis rows are retained; the cytosol row is retained because ABCF2 is described as "a cytosolic member of the ABC superfamily" [PMID:28112439 ABCF2, an Nrf2 target gene, contributes to cisplatin resistance in ovarian cancer cells., "Among these genes, ABCF2, a cytosolic member of the ABC superfamily of transporters"].

ABCF2 was originally cloned in a study of mRNAs responsive to cellular iron levels, but that paper is cloning/regulation evidence rather than direct GO function evidence [PMID:10944468 cDNA cloning by amplification of circularized first strand cDNAs reveals non-IRE-regulated iron-responsive mRNAs., "We tested this new method on eight mRNAs that we have previously shown to respond to cellular iron levels"]. ABCF2 is also overexpressed/amplified in ovarian clear cell adenocarcinoma and correlates with chemoresistance markers [PMID:16203778 Identification of overexpression and amplification of ABCF2 in clear cell ovarian adenocarcinomas by cDNA microarray analyses., "significantly higher ABCF2 DNA and mRNA copy number and protein levels in clear cell cases compared with those in serous cases"].

Bao et al. provide the key modern primary evidence: ABCF2 has a functional NRF2/NFE2L2 antioxidant-response element in its promoter, NRF2 binds the promoter region by ChIP, and manipulating ABCF2 changes cisplatin response in ovarian cancer cell lines [PMID:28112439 ABCF2, an Nrf2 target gene, contributes to cisplatin resistance in ovarian cancer cells., "To further confirm that NRF2 binds to the putative ARE of the ABCF2 promoter"; PMID:28112439 ABCF2, an Nrf2 target gene, contributes to cisplatin resistance in ovarian cancer cells., "ABCF2 overexpression rendered A2780 cells more resistant to cisplatin and ABCF2 knockdown rendered resistant A2780 cells more sensitive to cisplatin"]. This supports NFE2L2 target-gene and cancer-drug-response context, but not a precise GO molecular process for ABCF2.

## Existing GOA decisions

The two ATP binding rows and the ATP hydrolysis activity row are accepted as the conserved molecular-function core of a two-NBD ABCF ATPase. The cytosol row is accepted.

The Reactome plasma membrane row is removed. The Reactome event is "NFE2L2 dependent ABCF2 expression" and supports promoter regulation, not direct plasma-membrane localization [Reactome:R-HSA-9796042 NFE2L2 dependent ABCF2 expression, "ABCF2 is an NFE2L2 target gene that contains a functional ARE sequence in the promoter"]. The primary paper and UniProt both argue against a membrane-transporter model.

The high-throughput NK-cell membrane row is also removed. The NK proteome paper explicitly notes that many identified proteins were likely transiently associated with membranes [PMID:19946888 Defining the membrane proteome of NK cells., "The remaining species were largely involved in cellular processes and molecular functions that could be predicted to be transiently associated with membranes"]. For ABCF2, a soluble cytosolic ATPase with no transmembrane domains, the row is too weak to retain.

## Proteostasis PN projection

The PN projection report places ABCF2 under `Translation|Cytosolic translation|Ribosome-associated QC|other RQC processes` and projects `GO:0006515 protein quality control for misfolded or incompletely synthesized proteins` as `new_to_goa`. The mapping audit flags the parent RQC-group mapping as requiring manual gene-level review before changing a gene review because it is a high-level/contextual source and can lose specificity.

For ABCF2, I did not find direct evidence for stalled-ribosome recognition, ribosome rescue, collided-ribosome signaling, RQC-complex membership, or degradation of incomplete nascent chains. The PN projected `GO:0006515` term is therefore not proposed. It is recorded as an expert question and experimental follow-up.
