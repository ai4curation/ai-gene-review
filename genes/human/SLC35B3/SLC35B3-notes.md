# SLC35B3 (PAPST2 / Adenosine 3'-phospho 5'-phosphosulfate transporter 2) — review notes

## Identity and family

- UniProt Q9H1N7, human, 401 aa, gene `SLC35B3` (HGNC:21601); synonyms `C6orf196`, `PAPST2`, ORFName `CGI-19` [file:human/SLC35B3/SLC35B3-uniprot.txt "Name=SLC35B3", "Synonyms=C6orf196 ... PAPST2"].
- RecName in UniProt: "Adenosine 3'-phospho 5'-phosphosulfate transporter 2"; AltName "3'-phosphoadenosine 5'-phosphosulfate transporter" and "PAPS transporter 2" [file:human/SLC35B3/SLC35B3-uniprot.txt "RecName: Full=Adenosine 3'-phospho 5'-phosphosulfate transporter 2"].
- Belongs to the nucleotide-sugar transporter family, SLC35B subfamily [file:human/SLC35B3/SLC35B3-uniprot.txt "Belongs to the nucleotide-sugar transporter family. SLC35B", "subfamily."]. Domain: Pfam PF08449 (UAA); InterPro IPR013657 (SCL35B1-4/HUT1); TCDB 2.A.7.11.5 (drug/metabolite transporter superfamily). PANTHER subfamily PTHR10778:SF8 = "ADENOSINE 3'-PHOSPHO 5'-PHOSPHOSULFATE TRANSPORTER 2".
- Ten predicted helical transmembrane segments (multi-pass membrane protein) [file:human/SLC35B3/SLC35B3-uniprot.txt "Multi-pass membrane protein"]; three N-glycosylation sites (N12, N71, N254); `Glycoprotein` keyword.
- Paralog of SLC35B2 (PAPST1). Reactome groups them: "SLC35B2,3 exchange cytosolic PAPS with Golgi PAP" [file:reactome/R-HSA-741449.md].

## Function (molecular + biological process)

- UniProt FUNCTION: "Probably functions as a 3'-phosphoadenylyl sulfate:adenosine 3',5'-bisphosphate antiporter at the Golgi membranes. Mediates the transport from the cytosol into the lumen of the Golgi of 3'-phosphoadenylyl sulfate/adenosine 3'-phospho 5'-phosphosulfate (PAPS), a universal sulfuryl donor for sulfation events that take place in that compartment." (ECO:0000269|PubMed:16492677) [file:human/SLC35B3/SLC35B3-uniprot.txt].
- CATALYTIC ACTIVITY (Rhea RHEA:76063): 3'-phosphoadenylyl sulfate(in) + adenosine 3',5'-bisphosphate(out) = 3'-phosphoadenylyl sulfate(out) + adenosine 3',5'-bisphosphate(in) — i.e. a PAPS/PAP antiporter (ECO:0000305|PubMed:16492677) [file:human/SLC35B3/SLC35B3-uniprot.txt "Reaction=3'-phosphoadenylyl sulfate(in)"]. This antiport chemistry underlies the `Antiport` keyword and the UniProt-KW IEA annotation to GO:0015297 (antiporter activity) in the DR block (not in GOA TSV, so not reviewed here).
- Kinetics: KM = 2.2 uM for 3'-phosphoadenylyl sulfate (PAPS) (ECO:0000269|PubMed:16492677) [file:human/SLC35B3/SLC35B3-uniprot.txt "KM=2.2 uM for 3'-phosphoadenylyl sulfate"].

## Primary experimental characterization: Kamiyama et al. 2006 (PMID:16492677)

- Cached publication is **abstract-only** (`full_text_available: false`); abstract is detailed. The paper cloned and characterized PAPST2 (= SLC35B3) as a novel human PAPS transporter closely related to PAPST1 (SLC35B2).
- "PAPST2 protein was shown to have PAPS transport activity with an apparent Km value of 2.2 microM" [PMID:16492677 "PAPST2 protein was shown to have PAPS transport activity with an apparent Km value of 2.2 microM"].
- "The PAPST2 protein is localized on the Golgi apparatus in a manner similar to the PAPST1 protein." [PMID:16492677 "The PAPST2 protein is localized on the Golgi apparatus in a manner similar to the PAPST1 protein"].
- Biological role: "these findings indicate that PAPST2 is a PAPS transporter gene involved in the synthesis of sulfated glycoconjugates in the colon." RNAi of PAPST2 in HCT116 colon cancer cells reduced sialyl 6-sulfo N-acetyllactosamine epitope reactivity and total sulfate incorporation into cellular proteins [PMID:16492677 "PAPST2 is a PAPS transporter gene \ninvolved in the synthesis of sulfated glycoconjugates in the colon"].
- Tissue specificity: predominantly/preferentially expressed in colon [file:human/SLC35B3/SLC35B3-uniprot.txt "Preferentially and highly expressed in colon"], consistent with abstract "predominantly expressed in human colon tissues".

Note on colon-restriction: UniProt SIMILARITY/tissue field says "Preferentially and highly expressed in colon", but the HPA line in the same record reports "Low tissue specificity" and Bgee reports broad expression ("Expressed in pancreatic ductal cell and 193 other cell types or tissues"). The 2006 characterization emphasized colon; broader databases show wider expression. Colon is the demonstrated functional context, not necessarily the only one.

## Subcellular location

- Golgi apparatus membrane, multi-pass membrane protein (ECO:0000269|PubMed:16492677) [file:human/SLC35B3/SLC35B3-uniprot.txt "SUBCELLULAR LOCATION: Golgi apparatus membrane"].
- GOA also carries an ER membrane annotation (GO:0005789) purely by IBA (phylogenetic, GO_REF:0000033). This is NOT supported by the experimental/primary data for SLC35B3, which locate it to the Golgi. Some SLC35B-family members (e.g., SLC35B1/UGTrel1) have ER localization, so the IBA likely reflects the broader family tree rather than SLC35B3 itself. Treated as over-annotation for this gene (kept, not core).

## Core function summary

- **Core MF:** GO:0046964 — 3'-phosphoadenosine 5'-phosphosulfate transmembrane transporter activity (IDA in GOA, PMID:16492677; also IBA and Reactome TAS). Mechanistically a PAPS/PAP antiporter.
- **Core BP:** PAPS transmembrane transport / 3'-phosphoadenosine 5'-phosphosulfate transport. GOA has GO:0046963 (IBA), GO:1902559 (IEA, the transmembrane child), and GO:1902558 (TAS Reactome, "5'-adenylyl sulfate transmembrane transport"). GO:1902559 is the more precise term (child of both GO:0046963 and GO:0055085).
- **Core CC:** GO:0000139 — Golgi membrane (IDA, PMID:16492677).

## Annotation-by-annotation reasoning (see YAML for actions)

1. GO:0005789 ER membrane (IBA) — over-annotation for SLC35B3; primary data = Golgi. KEEP_AS_NON_CORE (family-level IBA, cannot fully exclude minor ER pool; not REMOVE per policy caution around family trees).
2. GO:0055085 transmembrane transport (IBA) — correct but generic parent of the specific PAPS transport; KEEP_AS_NON_CORE (redundant with specific MF/BP).
3. GO:0000139 Golgi membrane (IBA) — correct location; redundant with IDA. ACCEPT (own correct core CC).
4. GO:0046964 PAPS transmembrane transporter activity (IBA) — correct core MF; ACCEPT.
5. GO:0046963 PAPS transport (IBA) — correct core BP; ACCEPT.
6. GO:0000139 Golgi membrane (IEA, SubCell mapping) — correct; ACCEPT.
7. GO:0055085 transmembrane transport (IEA, InterPro) — generic; KEEP_AS_NON_CORE.
8. GO:1902559 PAPS transmembrane transport (IEA, inter-ontology) — precise core BP; ACCEPT.
9. GO:1902558 5'-adenylyl sulfate (APS) transmembrane transport (TAS Reactome) — APS (adenosine 5'-phosphosulfate) is not the same molecule as PAPS (3'-phospho-AMP-sulfate); the Rhea reaction and characterized substrate is PAPS/PAP, not APS. This term is arguably imprecise/incorrect substrate. It is TAS (author statement via Reactome), not experimental, so MARK_AS_OVER_ANNOTATED with proposed replacement GO:1902559 rather than REMOVE.
10. GO:0000139 Golgi membrane (IDA, PMID:16492677) — experimental core CC; ACCEPT.
11. GO:0046964 PAPS transmembrane transporter activity (IDA, PMID:16492677) — experimental core MF; ACCEPT.
12. GO:0046964 PAPS transmembrane transporter activity (TAS Reactome) — correct core MF; ACCEPT.
13. GO:0000139 Golgi membrane (TAS Reactome) — correct core CC; ACCEPT.

## Open questions

- Is the physiological substrate strictly PAPS (as characterized), or does SLC35B3 also handle other nucleotide sugars/APS? Human data are limited to the single 2006 characterization.
- Functional redundancy/division of labor with SLC35B2 (PAPST1) across tissues (PAPST1 placenta/pancreas-high; PAPST2 colon-high).
- Physiological significance of the IBA ER-membrane localization: real minor ER pool for SLC35B3, or family-tree artifact?
