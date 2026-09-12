# NDUFA10 (O95299) — Gene Review Notes

## Identity and overview

- **Gene:** NDUFA10 (HGNC:7684); UniProt **O95299** (NDUAA_HUMAN).
- **Product:** "NADH dehydrogenase [ubiquinone] 1 alpha subcomplex subunit 10, mitochondrial"; aka **Complex I-42kD / CI-42kD**, "NADH-ubiquinone oxidoreductase 42 kDa subunit" [file:human/NDUFA10/NDUFA10-uniprot.txt "AltName: Full=Complex I-42kD"].
- Precursor with an N-terminal mitochondrial transit peptide (residues 1–35); mature chain 36–355 [file:human/NDUFA10/NDUFA10-uniprot.txt "TRANSIT 1..35"].

## Core biology: accessory (supernumerary) subunit of Complex I membrane arm

- UniProt FUNCTION: "**Accessory subunit** of the mitochondrial membrane respiratory chain NADH dehydrogenase (Complex I), **that is believed not to be involved in catalysis**. Complex I functions in the transfer of electrons from NADH to the respiratory chain. The immediate electron acceptor for the enzyme is believed to be ubiquinone." (ECO:0000269|PubMed:27626371) [file:human/NDUFA10/NDUFA10-uniprot.txt "believed not to be involved in catalysis"].
- SUBUNIT: "Complex I is composed of 45 different subunits. This a component of the **hydrophobic protein fraction**." (ECO:0000269|PubMed:12611891, PubMed:27626371) [file:human/NDUFA10/NDUFA10-uniprot.txt "component of the hydrophobic protein"]. The HP fraction is the membrane arm.
- Human complex I = 14 conserved core subunits (catalytic) + 31 accessory/supernumerary subunits; the core subunits are essential for enzymatic function and the accessory subunits have less clear individual roles [PMID:27626371 "Bacterial and human complex I share 14 core subunits that are essential for enzymatic function; however, the role and necessity of the remaining 31 human accessory subunits is unclear."].
- Stroud et al. knocked out each accessory subunit; 25 are strictly required to assemble a functional complex, and loss of a subunit destabilizes other subunits in the same structural module [PMID:27626371 "we show that 25 subunits are strictly required for assembly of a functional complex ... loss of each subunit affects the stability of other subunits residing in the same structural module"]. This establishes accessory subunits (including NDUFA10) as **structural/assembly** components rather than catalytic.

## dNK (deoxyribonucleoside kinase) fold — pseudoenzyme, no assigned catalytic activity

- Structural/domain annotations place NDUFA10 in a **deoxyribonucleoside kinase (dNK) / P-loop NTPase** fold: InterPro IPR050566 (Deoxyribonucleoside_kinase), IPR031314 (DNK_dom), Pfam PF01712 (dNK), CDD cd02030 (NDUO42), PANTHER PTHR10513 (DEOXYNUCLEOSIDE KINASE), Gene3D 3.40.50.300 (P-loop NTPase) [file:human/NDUFA10/NDUFA10-uniprot.txt "InterPro; IPR050566; Deoxyribonucleoside_kinase"].
- **However, UniProt assigns NO catalytic activity** (no CATALYTIC ACTIVITY / EC line) and explicitly states the subunit is "believed not to be involved in catalysis." The dNK fold here is a structural scaffold; NDUFA10 is a **pseudokinase / pseudoenzyme** in the complex I context. The FAD cofactor note ("Binds 1 FAD per subunit") is a family/structural feature, not evidence of a nucleoside-kinase catalytic function.
- Consequence for GO: a nucleoside/nucleotide **kinase molecular function should NOT be assigned from the fold** — that would be a classic fold-based pseudoenzyme over-annotation. The honest MF for a structural subunit is **GO:0005198 structural molecule activity**, contributing to the complex-level catalysis (GO:0008137) via `contributes_to`, not `enables`.

## Localization

- Mature protein resides in the **mitochondrial inner membrane** as part of the complex I membrane arm; ComplexPortal annotates it to GO:0005743 (mitochondrial inner membrane) IDA [PMID:28844695].
- UniProt SUBCELLULAR LOCATION line reads "Mitochondrion matrix" (ECO:0000305|PubMed:12611891) — this is a topological inference for a matrix-facing accessory subunit and is the source of the GO:0005759 IEA (UniProtKB-SubCell) annotation. The membrane-arm inner-membrane localization (GO:0005743) is better supported by structural/ComplexPortal evidence.
- NDUFA10 is a high-confidence mitochondrial proteome member; MitoCoP defines ">1,100 proteins" [PMID:34800366 "defined a mitochondrial high-confidence proteome of >1,100 proteins (MitoCoP)"] (source of the GO:0005739 mitochondrion HTP annotation).

## Complex I structure / assembly context

- Identified as one of the ~42 human complex I polypeptides by immunopurification + MS [PMID:12611891 "we can resolve and identify the human homologues of 42 polypeptides detected so far"].
- Present in respiratory supercomplexes/megacomplex (I2III2IV2) resolved by cryo-EM, which "reveals the precise assignment of individual subunits of human CI" [PMID:28844695 "reveals the precise assignment of individual subunits of human CI"]; NDUFA10 subunit assignment in these structures underlies the ComplexPortal CI membership (GO:0045271, IPI/IDA).
- Reactome models NDUFA10 as a constituent of mature Complex I and of the catalytic reaction "Complex I oxidises NADH to NAD+, reduces CoQ to CoQH2" [reactome:R-HSA-163217]; the R-HSA-6799178/6799179/6799191/6799196/6799197/6799202 reactions describe the stepwise Complex I biogenesis pathway in which the mature complex forms.

## PTM

- PTM line: "Phosphorylation at Ser-250 by PINK1 is required for the binding and/or reduction of the complex I substrate ubiquinone." (ECO:0000250|UniProtKB:Q99LC3 — by similarity to mouse) [file:human/NDUFA10/NDUFA10-uniprot.txt "Phosphorylation at Ser-250 by PINK1"]. This links NDUFA10 phospho-regulation to complex I ubiquinone handling but is a by-similarity inference, not human-experimental.

## Disease

- Biallelic NDUFA10 variants cause **Mitochondrial complex I deficiency, nuclear type 22 (MC1DN22)**, autosomal recessive; phenotypes include Leigh syndrome [file:human/NDUFA10/NDUFA10-uniprot.txt "Mitochondrial complex I deficiency, nuclear type 22 (MC1DN22)"].
- First disease report: compound-heterozygous NDUFA10 mutations in a Leigh patient; patient fibroblasts showed "decreased amount and activity, and a disturbed assembly of complex I" — directly supporting an assembly/structural role for NDUFA10 (PubMed:21150889; not in GOA/publications cache, PubMed metadata verified). [DOI](https://doi.org/10.1038/ejhg.2010.204)
- Additional variant (Pro-294) reported in a comprehensive mitochondrial-disease genomic study (PubMed:26741492). [DOI](https://doi.org/10.1371/journal.pgen.1005679)
- (These two disease papers are UniProt references but are NOT in the GOA table, so they are not reviewed as existing_annotations.)

## Annotation-review summary (rationale)

- **Structural/complex-membership annotations** (GO:0045271 respiratory chain complex I, part_of; via IDA/IPI/IBA/NAS/IEA): well supported — NDUFA10 is a bona fide stable subunit → ACCEPT the experimentally-supported ones (IDA PMID:12611891, PMID:27626371; IPI PMID:28844695), KEEP others.
- **Localization**: GO:0005743 (mitochondrial inner membrane, IDA ComplexPortal) is the best-supported location → ACCEPT; GO:0005739 (mitochondrion HTP) ACCEPT as coarse/non-core; GO:0005759 (mitochondrial matrix, IEA-SubCell) KEEP_AS_NON_CORE (topological, less precise than inner membrane); Reactome GO:0005743 TAS entries ACCEPT/KEEP.
- **Process annotations** GO:0006120 (mito electron transport NADH→ubiquinone) and GO:0009060 / GO:0042776 / GO:1902600: these are **complex-level** processes. NDUFA10 contributes as a structural subunit → KEEP_AS_NON_CORE (accessory, not itself catalytic); GO:0006120 is the closest to core and can be ACCEPTed as a contributing role. GO:1902600 (proton transmembrane transport, IEA GO_REF:0000108 inferred from GO:0008137) is a mechanistic over-reach for an accessory subunit → MARK_AS_OVER_ANNOTATED.
- **MF GO:0008137 NADH dehydrogenase (ubiquinone) activity, enables, NAS PMID:9878551**: this is the whole-complex catalytic activity. NDUFA10 is explicitly non-catalytic; `enables` on an accessory subunit is an over-annotation (should be `contributes_to` at most) → MARK_AS_OVER_ANNOTATED. Do NOT convert to a kinase MF.
- **cytoplasm (GO:0005737, IBA)**: over-broad; the protein is mitochondrial (inner membrane) → MARK_AS_OVER_ANNOTATED (coarse localization; not removed since IBA).

## Core functions (final)

- MF: **GO:0005198 structural molecule activity** (honest MF for a non-catalytic structural subunit).
- MF contribution: **contributes_to GO:0008137 NADH dehydrogenase (ubiquinone) activity** (complex-level catalysis it helps constitute).
- CC: **part_of GO:0045271 respiratory chain complex I** (and located_in GO:0005743 mitochondrial inner membrane).
- BP: **GO:0006120 mitochondrial electron transport, NADH to ubiquinone** and **GO:0032981 mitochondrial respiratory chain complex I assembly** (assembly/structural role supported by KO and disease-fibroblast assembly defects).
</content>
</invoke>
