# Source-record defects for UNIPROT

15 open defect(s), generated from `source_defects` blocks in this repository's reviews. Do not edit by hand.

## 1. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9I537
- **Subject:** UniProtKB:Q9I537
- **Change:** EC:2.3.2.3 → EC:2.3.2.11 (alanylphosphatidylglycerol synthase)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/PA0920/PA0920-ai-review.yaml`

The ARBA-derived RecName "Phosphatidylglycerol lysyltransferase", EC 2.3.2.3 and the lysyl-tRNA CATALYTIC ACTIVITY on Q9I537 are wrong. PA0920 is the experimentally characterised alanyl-phosphatidylglycerol synthase (Klein et al. 2009; Hebecker et al. 2011, 2015), and the EC 2.3.2.3 mapping produces the incorrect GO:0050071 IEA. Name it alanyl-phosphatidylglycerol synthase (EC 2.3.2.11) and restrict the ARBA rule so it does not fire on A-PGS sequences.

> Consequently, the protein encoded by PA0920 was named A-PG synthase.
> — PMID:19087229

## 2. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniRule:UR000100634
- **Subject:** UniProtKB:P08308
- **Change:** delete the record asserting GO:0006526
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/arcB/arcB-ai-review.yaml`

UniRule UR000100634 transfers GO:0006526 L-arginine biosynthetic process to P. aeruginosa ArcB (P08308), whose own UniProt entry states that this catabolic OTCase does not carry out the biosynthetic reaction and places it in L-arginine degradation via the ADI pathway. The rule should exclude catabolic (ArcB-type) OTCs.

> This catabolic OTCase does not carry out the biosynthetic reaction because of a poor affinity and a marked cooperativity for carbamoyl phosphate
> — file:PSEAE/arcB/arcB-uniprot.txt

## 3. WRONG_REFERENCE (SUSPECTED, NOT_REPORTED)

- **Record:** UniProtKB:P18275 enables GO:0043858 arginine:ornithine antiporter activity (EXP, PMID:2158926)
- **Field:** DB:Reference
- **Change:** check PMID:2158926 (alternatives in the explanation)
- **Recorded in:** `genes/PSEAE/arcD/arcD-ai-review.yaml`

enables GO:0043858 (EXP) on P18275 ArcD cites Luthi et al. 1990, whose abstract only proposes the antiport from the arcD mutant phenotype. The activity was measured in PMID:1311296 (reconstituted proteoliposomes) and PMID:8449902, which UniProt's FUNCTION comment cites. Please check whether this row should cite PMID:1311296 (IDA) instead. The annotation is correct.

> it is proposed that arcD specifies an arginine: ornithine antiporter or a part thereof
> — PMID:2158926

## 4. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** ARBA:ARBA00086662
- **Subject:** UniProtKB:P22567
- **Field:** GO_ID
- **Change:** GO:0004358 → GO:0004042 (L-glutamate N-acetyltransferase activity, acting on acetyl-CoA as donor)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/argA/argA-ai-review.yaml`

ARBA00086662 assigns the ArgJ ornithine acetyltransferase term to an ArgA-type NAGS whose own record gives the acetyl-CoA reaction. The rule probably learned from the mis-termed GO:0004358 annotations on ArgA proteins. The rule's full scope was not checked, hence PROBABLE.

> Reaction=L-glutamate + acetyl-CoA = N-acetyl-L-glutamate + CoA + H(+)
> — file:PSEAE/argA/argA-uniprot.txt

## 5. WRONG_TERM (SUSPECTED, NOT_REPORTED)

- **Record:** UniProtKB:Q9I5F3 enables GO:0003960 quinone reductase (NADPH) activity (EXP, PMID:24915188)
- **Field:** GO_ID
- **Change:** check GO:0003960 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/azoR1/azoR1-ai-review.yaml`

UniProt EXP row for Q9I5F3 (paAzoR1) from PMID:24915188 and its CATALYTIC ACTIVITY line use RHEA:14269, which yields 1,4-benzosemiquinone (one-electron reduction). The paper measured NADPH oxidation only and frames the azoreductases as two-electron NAD(P)H quinone oxidoreductases, and FMN-dependent azoreductases act by hydride transfer. GO:0003955 (quinol product) is the better fit. Please check whether the semiquinone reaction was chosen deliberately. The paralogs paAzoR2 and paAzoR3 carry RHEA:65952, also a semiquinone-forming reaction.

> Two electron reduction reactions of quinones are carried out by a group of enzymes known as NAD(P)H quinone oxidoreductases.
> — PMID:24915188

## 6. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** UniRule:UR000101231
- **Subject:** UniProtKB:Q9I5F3
- **Field:** GO_ID
- **Change:** delete the record asserting GO:0016652
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/azoR1/azoR1-ai-review.yaml`

UniRule UR000101231 (azoreductase type 1, HAMAP MF_01216) maps GO:0016652 oxidoreductase activity, acting on NAD(P)H, NAD(P) as acceptor. That term is for enzymes in which NAD(P)H reduces NAD(P)+ (EC 1.6.1). Azoreductases transfer electrons from NAD(P)H to quinones and azo compounds; the appropriate terms are GO:0016655 and its child GO:0003955. Checked against the GO definition. The same mapping reaches azoR2 (Q9I2E2) and azoR3 (Q9HZ17) and every MF_01216 member.

## 7. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:O33407 involved_in GO:0008610 lipid biosynthetic process (IMP, PMID:17631636)
- **Field:** GO_ID
- **Change:** check GO:0008610 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/estA/estA-ai-review.yaml`

The IMP lipid biosynthetic process row on EstA (O33407) from PMID:17631636 is based on reduced rhamnolipid in an estA deletion mutant. The UniProt entry itself says the role of EstA is unclear, and EstA is a surface-exposed outer-membrane esterase, not a rhamnolipid synthase. Unless the full text shows EstA acting on a biosynthetic intermediate, please consider removing the row. It is the sole seed of the PAINT IBD at PTN005219546 (960 leaf IBAs).

## 8. WRONG_STATEMENT (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9I648   UniProt entry Q9I648 (Q9I648_PSEAE) (, file:PSEAE/fiuA/fiuA-uniprot.txt)
- **Field:** DE RecName
- **Change:** Metal-pseudopaline receptor CntO → Ferrichrome receptor FiuA
- **Recorded in:** `genes/PSEAE/fiuA/fiuA-ai-review.yaml`

The ARBA-derived recommended name (ARBA00072467) names Q9I648 after CntO, the pseudopaline-metal receptor encoded elsewhere in the PAO1 genome. Q9I648 is fiuA (PA0470), the ferrichrome receptor, as the 55Fe uptake data show. The same ARBA name and the matching ARBA FUNCTION text (pseudopaline transport) are on FoxA (Q9I116). Please replace the name and FUNCTION text on this entry.

> ferrichrome is transported across the outer membrane primarily (80%) by the FiuA receptor and to a lesser extent (20%) by a secondary transporter
> — PMID:20047910

## 9. OTHER (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9K3C5 located_in GO:0009421 bacterial-type flagellum filament cap (IDA, PMID:9488388)
- **Field:** SUBUNIT
- **Change:** Homopentamer → Homohexamer
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/fliD/fliD-ai-review.yaml`

The UniProt entry Q9K3C5 records "SUBUNIT: Homopentamer {ECO:0000250}", an inference by similarity. The oligomeric state of PAO1 FliD has since been determined experimentally and it is a hexamer: the FliD78-405 core crystallises as a six-pointed star hexamer (PDB 5FHY), the hexamer is confirmed in solution and by negative-stain EM class averaging, and the same study shows that capping-protein stoichiometry differs between species (Salmonella FliD is a pentamer). Please update the SUBUNIT line to a homohexamer with ECO:0000269|PubMed:27664419 and add PMID:27664419 to the entry.

> Thus, we confirmed that the hexameric assembly of FliD78–405 occurs not only in the crystalline environment but also in solution using negative stain EM class averaging (Tang et al.
> — PMID:27664419

## 10. WRONG_STATEMENT (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9I116   UniProt entry Q9I116 (Q9I116_PSEAE) (, file:PSEAE/foxA/foxA-uniprot.txt)
- **Field:** DE RecName
- **Change:** Metal-pseudopaline receptor CntO → Ferrioxamine receptor FoxA
- **Recorded in:** `genes/PSEAE/foxA/foxA-ai-review.yaml`

The ARBA-derived recommended name (ARBA00072467) and the ARBA FUNCTION text name Q9I116 as the pseudopaline-metal receptor CntO. Q9I116 is foxA (PA2466), the ferrioxamine receptor, as mutant uptake assays show. The same wrong name is on FiuA (Q9I648). Please replace the name and FUNCTION text.

> FoxA of the ferric forms of nocardamine, bisucaberin, DFOB and DFOG
> — PMID:39138320

## 11. OTHER (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9I296
- **Subject:** UniProtKB:Q9I296
- **Field:** DE
- **Change:** Isovaleryl-CoA dehydrogenase, mitochondrial → Isovaleryl-CoA dehydrogenase
- **Recorded in:** `genes/PSEAE/liuA/liuA-ai-review.yaml`

The unreviewed entry Q9I296 (LiuA, PA2015) of the bacterium Pseudomonas aeruginosa PAO1 has the RecName "Isovaleryl-CoA dehydrogenase, mitochondrial" from ARBA:ARBA00018258. Bacteria have no mitochondria; the qualifier comes from the eukaryotic IVD template. The name should be "Isovaleryl-CoA dehydrogenase" (the activity is shown for the purified protein in PMID:18625020).

> Isovaleryl-CoA dehydrogenase, mitochondrial
> — file:PSEAE/liuA/liuA-uniprot.txt

## 12. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9HZZ4 involved_in GO:0006351 DNA-templated transcription (IEA, GO_REF:0000104)
- **Field:** GO_ID
- **Change:** GO:0006351 → GO:0006355 (regulation of DNA-templated transcription)
- **Likely cause:** UNKNOWN
- **Recorded in:** `genes/PSEAE/ohrR/ohrR-ai-review.yaml`

involved_in GO:0006351 DNA-templated transcription (IEA, GO_REF:0000104) on PA2849 (OhrR) comes from a sequence-feature transfer based on the MarR-type HTH domain. A transcriptional repressor is not a participant in transcription itself; the regulation branch (GO:0006355 or, for OhrR, GO:0045892) is intended. Please check the UniRule/ARBA mapping that emits the process term for this HTH family.

> PANTHER; PTHR33164:SF5; ORGANIC HYDROPEROXIDE RESISTANCE TRANSCRIPTIONAL REGULATOR; 1.
> — file:PSEAE/ohrR/ohrR-uniprot.txt

## 13. OTHER (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:G3XD94 located_in GO:0016020 membrane (IEA, GO_REF:0000044)
- **Change:** delete the record asserting GO:0016020
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/wbpA/wbpA-ai-review.yaml`

G3XD94 (WbpA) carries a predicted TRANSMEM 13..32 (ECO:0000255) and a Membrane / single-pass subcellular location, which generate GO:0016020. The segment SRQALIGIVGLGYVGLPLML contains the GxGxxG NAD-binding motif at the N-terminus of the UDP-glucose/GDP-mannose dehydrogenase Rossmann fold, and WbpA was purified as a soluble His-tagged oligomer (PMID:15226302). Please review the TRANSMEM feature and location.

## 14. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:G3XD61 enables GO:0008761 UDP-N-acetylglucosamine 2-epimerase activity (IDA, PMID:17346239)
- **Change:** check GO:0008761 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/wbpI/wbpI-ai-review.yaml`

GO:0008761 is defined as UDP-N-acetyl-D-glucosamine = UDP-N-acetyl-D-mannosamine. PMID:17346239 shows that WbpI catalyses UDP-GlcNAc3NAcA = UDP-ManNAc3NAcA (EC 5.1.3.23, RHEA:24764) and does not use UDP-GlcNAc. GO has no term for EC 5.1.3.23; use GO:0016857 until one is created (a new term is proposed in this review), and do not use GO:0008761.

> Neither enzyme utilized UDP-alpha-D-GlcNAc, UDP-alpha-D-GlcNAcA (UDP-2-acetamido-2,3-dideoxy-alpha-D-glucuronic acid) or UDP-alpha-D-GlcNAc3NAc (UDP-2,3-diacetamido-2,3-dideoxy-alpha-D-glucose) as substrates.
> — PMID:17346239

## 15. WRONG_QUALIFIER (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9HT73
- **Subject:** UniProtKB:Q9HT73
- **Field:** Qualifier
- **Change:** check enables (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/znuC/znuC-ai-review.yaml`

The EC 7.2.2.20 / RHEA:29795 transport reaction is carried out by the ZnuABC complex. ZnuC is the nucleotide-binding subunit and has no transmembrane segment, so it cannot translocate Zn(2+) on its own; the UniProt record itself states that the complex comprises two ZnuC, two ZnuB and one ZnuA. contributes_to GO:0015633 would be the accurate qualifier for the subunit, as is done for other ABC importer ATPases.

> The complex is composed of two ATP-binding proteins (ZnuC),
> — file:PSEAE/znuC/znuC-uniprot.txt
