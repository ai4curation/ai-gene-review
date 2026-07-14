# SLC25A10 (DIC, mitochondrial dicarboxylate carrier) — review notes

## Identity and family
- UniProt Q9UBX3, `DIC_HUMAN`, "Mitochondrial dicarboxylate carrier", short DIC, AltName "Solute carrier family 25 member 10". HGNC:10980. 287 aa. [file:human/SLC25A10/SLC25A10-uniprot.txt "RecName: Full=Mitochondrial dicarboxylate carrier"]
- Member of the mitochondrial carrier (SLC25 / TC 2.A.29) family. Three tandem Solcar repeats, six predicted transmembrane helices, canonical SLC25 fold. [file:human/SLC25A10/SLC25A10-uniprot.txt "Belongs to the mitochondrial carrier (TC 2.A.29) family."] TCDB 2.A.29.2.7.
- Two isoforms by alternative splicing (Q9UBX3-1 displayed; Q9UBX3-2 = VSP_003267, insertion at residue 209). [file:human/SLC25A10/SLC25A10-uniprot.txt "Named isoforms=2"]

## Molecular function and mechanism
- Antiporter: catalyzes electroneutral exchange of dicarboxylates (malonate, malate, succinate), inorganic sulfur anions and phosphate across the inner mitochondrial membrane. [file:human/SLC25A10/SLC25A10-uniprot.txt "Catalyzes the electroneutral exchange or flux of"]
- UniProt lists explicit catalytic-activity (RHEA) reactions confirming the antiport chemistry, e.g. malate(in) + phosphate(out) = malate(out) + phosphate(in) (RHEA:71607); malate/succinate exchange (RHEA:29327); sulfate/phosphate, thiosulfate/sulfate, malonate/malate, etc. These are transport reactions, not enzymatic (bond-forming/breaking) catalysis — DIC is a transporter, not an enzyme.
- Substrate exchange follows a ping-pong (consecutive, single-binding-site) mechanism: one substrate binds and is translocated, dissociates, then the counter-substrate binds. [file:human/SLC25A10/SLC25A10-uniprot.txt "occurs consecutively with one substrate being transported"] [PMID:38937634]
- Functions as a monomer. [file:human/SLC25A10/SLC25A10-uniprot.txt "SUBUNIT: Monomer."] [PMID:38937634 "Human mitochondrial carriers of the SLC25 family function as monomers exchanging substrates with a ping-pong kinetic mechanism."]
- Does NOT transport glutathione (by similarity; and rat Slc25a10 does not transport GSH). [file:human/SLC25A10/SLC25A10-uniprot.txt "Does not transport glutathione (By similarity)."] [PMID:29211846 "rat Slc25a10 does not transport GSH, in agreement with similar findings with yeast DIC1"]
- Best single MF term capturing the characterized biology: **GO:0015364 dicarboxylate:phosphate antiporter activity** (def: "dicarboxylate(out) + phosphate(in) = dicarboxylate(in) + phosphate(out)"), a child of both GO:0005310 (dicarboxylic acid transmembrane transporter activity) and GO:0015297 (antiporter activity). GO:0015140 (malate) is the specific substrate MF; GO:0015141 (succinate) also applies.

## Substrate specificity (experimental)
- Human SLC25A10 substrates and antiport pairs are supported experimentally: malate:phosphate exchange (PMID:29211846, transport assay on reconstituted patient mitochondrial extracts) and a broad set of dicarboxylate/sulfur-anion/phosphate exchanges characterized by Pyrihova et al. and Cimadamore-Werthein et al. [PMID:38780415] [PMID:38937634]
- Sulfate, thiosulfate, malonate exchanges established in PMID:38780415 (FUNCTION, SUBSTRATE SPECIFICITY, TRANSPORTER ACTIVITY). [file:human/SLC25A10/SLC25A10-uniprot.txt "FUNCTION, SUBSTRATE SPECIFICITY, AND TRANSPORTER ACTIVITY."]
- Oxaloacetate transport is an IBA (phylogenetic) inference; it is not among the human-characterized catalytic-activity reactions in UniProt. Kept as non-core.

## Localization
- Mitochondrion inner membrane; multi-pass membrane protein. [file:human/SLC25A10/SLC25A10-uniprot.txt "SUBCELLULAR LOCATION: Mitochondrion inner membrane; Multi-pass membrane"]
- Confirmed mitochondrial by HPA IDA (GO:0005739) and by the high-confidence mitochondrial proteome (Morgenstern et al. 2021). [PMID:34800366]
- A `nucleus` HDA annotation (GO:0005634) derives from a sperm-nucleus proteome (de Mateo et al. 2011); this is almost certainly a co-purification/contaminant artifact for an inner-membrane transporter and contradicts the established IMM localization. [PMID:21630459] Marked as over-annotated (HDA, high-throughput, not physiological).

## Biological processes / physiology
- Supplies substrates for gluconeogenesis, fatty-acid metabolism, urea synthesis and sulfur metabolism, especially in liver. [file:human/SLC25A10/SLC25A10-uniprot.txt "Plays an important role in gluconeogenesis, fatty acid metabolism, urea"]
- Highly expressed in liver and kidney (consistent with gluconeogenic/ureogenic role); lower elsewhere. [file:human/SLC25A10/SLC25A10-uniprot.txt "Present in high amounts in liver and kidney"] Rat transcripts also in heart and brain. [PMID:9733776 "detected in rat liver and kidney, but unexpectedly, they were also detected in rat heart and brain tissues"]
- Core BP framing: dicarboxylate (malate/succinate) transmembrane transport coupled to phosphate; downstream physiology (gluconeogenesis, fatty-acid/sulfur metabolism) is a consequence of substrate supply.

## Disease
- Biallelic loss-of-function causes Mitochondrial DNA depletion syndrome 19 (MTDPS19, MIM:618972): severe epileptic encephalopathy, hypotonia → spastic quadriparesis, complex I deficiency and mtDNA depletion in skeletal muscle. [file:human/SLC25A10/SLC25A10-uniprot.txt "Mitochondrial DNA depletion syndrome 19 (MTDPS19)"] [PMID:29211846 "the first recessive mutations of SLC25A10 associated to an inherited severe mitochondrial neurodegenerative disorder"]
- Patient fibroblasts lacked SLC25A10 protein and transport activity; yeast DIC1 knockout phenocopies (respiration defect, decreased mtDNA). [PMID:29211846 "the transport assay on reconstituted mitochondrial extracts revealed no SLC25A10 activity"]

## Interactions (GO:0005515 IPI)
- All curated `protein binding` IPI annotations are from high-throughput interactome / Y2H mapping (Rolland 2014 PMID:25416956; Venkatesan 2009 PMID:19060904; Yu 2011 PMID:21516116 / related; Luck/Fragoza allelic map PMID:31515488), against partners including keratins/KRTAPs (KRT40, KRTAP4-2, KRTAP5-9, KRTAP10-8), MDFI, NOTCH2NLA, RBAK. [file:human/SLC25A10/SLC25A10-uniprot.txt "INTERACTION:"]
- These partners are cytosolic/nuclear and non-mitochondrial; interactions with an inner-membrane multi-pass transporter are almost certainly Y2H/high-throughput artifacts (sticky keratins are classic false positives). Uninformative for function → MARK_AS_OVER_ANNOTATED (policy: never REMOVE a bare protein-binding IPI). Not used in core_functions.

## Annotation review summary (actions)
- Core MF: dicarboxylate:phosphate antiporter (GO:0015364; via MODIFY of the general dicarboxylic-acid transporter EXP annotation) + malate/succinate specific transporter MFs (ACCEPT).
- Core CC: mitochondrial inner membrane (GO:0005743, ACCEPT).
- Core BP: malate/succinate transmembrane transport + phosphate ion transmembrane transport (ACCEPT); dicarboxylic acid transport (ACCEPT general).
- Non-core / accepted context: gluconeogenesis (KEEP_AS_NON_CORE — downstream physiology, TAS).
- Over-annotations: nucleus HDA; protein binding IPIs (sticky HT partners); sulfide oxidation TAS (Reactome pathway participation, not DIC's own function).
- Sulfate/thiosulfate/oxaloacetate transporter+transport IBA terms: real but ancillary substrate specificities → KEEP_AS_NON_CORE.
- IEA structural/pipeline terms (dicarboxylic acid transporter ARBA; IMM subcell; generic transmembrane transport InterPro; oxaloacetate(2-) inter-ontology): ACCEPT or KEEP_AS_NON_CORE as generic-but-correct; the generic GO:0055085 transmembrane transport (both IEA and Reactome TAS) is correct but uninformative → KEEP_AS_NON_CORE.
</content>
</invoke>
