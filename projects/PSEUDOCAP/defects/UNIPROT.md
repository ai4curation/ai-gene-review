# Source-record defects for UNIPROT

30 open defect(s), generated from `source_defects` blocks in this repository's reviews. Do not edit by hand.

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
- **Likely cause:** UNKNOWN
- **Recorded in:** `genes/PSEAE/arcD/arcD-ai-review.yaml`

enables GO:0043858 (EXP) on P18275 ArcD cites Luthi et al. 1990, whose abstract only proposes the antiport from the arcD mutant phenotype (full text not read). The activity was measured in PMID:1311296 (reconstituted proteoliposomes) and PMID:8449902. In the UniProt entry itself the FUNCTION and CATALYTIC ACTIVITY comments carry ECO:0000269 evidence from PubMed:1311296 and PubMed:8449902, and PubMed:2158926 is cited only for the name and the disruption phenotype, yet the two UniProt EXP rows for this term cite PMID:2158926 and PMID:8449902. Please check whether the row citing PMID:2158926 should cite PMID:1311296 instead. The annotation is correct.

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

## 5. WRONG_STATEMENT (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:P80358
- **Subject:** UniProtKB:P80358
- **Field:** CC:SIMILARITY
- **Change:** revise "Belongs to the succinylarginine dihydrolase family." in CC:SIMILARITY (see explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/aruG/aruG-ai-review.yaml`

P80358 carries Pfam PF04958 (AstA) and InterPro IPR007041 (Arg_succinylTrfase_AstA/AruG), and is a subunit of arginine N-succinyltransferase. E. coli AstA (P0AE37) is classified in the arginine N-succinyltransferase family; this chain should be too. The dihydrolase-family statement probably echoes the PANTHER PTHR30420 family name. The identical error on the alpha chain is reported from the astA review (UniProtKB:P80357), and both chains of the one heterotetramer should be corrected together.

> Pfam; PF04958; AstA; 1.
> — file:PSEAE/aruG/aruG-uniprot.txt

## 6. WRONG_QUALIFIER (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:P80358 enables GO:0008791 L-arginine N-succinyltransferase activity (IEA, GO_REF:0000120)
- **Field:** Qualifier
- **Change:** enables → contributes_to
- **Likely cause:** SCOPE_OVER_REACH
- **Recorded in:** `genes/PSEAE/aruG/aruG-ai-review.yaml`

P80358 is one chain of the two-chain heterotetrameric arginine/ornithine N-succinyltransferase (PMID:7523119); the GO:0008791 row should use contributes_to unless each chain is shown to be active alone.

## 7. WRONG_STATEMENT (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:P80357
- **Subject:** UniProtKB:P80357
- **Field:** CC:SIMILARITY
- **Change:** revise "Belongs to the succinylarginine dihydrolase family." in CC:SIMILARITY (see explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/astA/astA-ai-review.yaml`

P80357 carries Pfam PF04958 (AstA) and InterPro IPR007041 (Arg_succinylTrfase_AstA/AruG), and is a subunit of arginine N-succinyltransferase. E. coli AstA (P0AE37) is classified in the arginine N-succinyltransferase family; this chain should be too. The dihydrolase-family statement probably echoes the PANTHER PTHR30420 family name. The identical error on the beta chain is reported from the aruG review (UniProtKB:P80358), and both chains of the one heterotetramer should be corrected together.

> Pfam; PF04958; AstA; 1.
> — file:PSEAE/astA/astA-uniprot.txt

## 8. WRONG_QUALIFIER (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:P80357 enables GO:0008791 L-arginine N-succinyltransferase activity (IEA, GO_REF:0000120)
- **Field:** Qualifier
- **Change:** enables → contributes_to
- **Likely cause:** SCOPE_OVER_REACH
- **Recorded in:** `genes/PSEAE/astA/astA-ai-review.yaml`

P80357 is one chain of the two-chain heterotetrameric arginine/ornithine N-succinyltransferase (PMID:7523119); the GO:0008791 row should use contributes_to unless each chain is shown to be active alone.

## 9. WRONG_TERM (SUSPECTED, NOT_REPORTED)

- **Record:** UniProtKB:Q9I5F3 enables GO:0003960 quinone reductase (NADPH) activity (EXP, PMID:24915188)
- **Field:** GO_ID
- **Change:** check GO:0003960 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/azoR1/azoR1-ai-review.yaml`

UniProt EXP row for Q9I5F3 (paAzoR1) from PMID:24915188 and its CATALYTIC ACTIVITY line use RHEA:14269, which yields 1,4-benzosemiquinone (one-electron reduction). The paper measured NADPH oxidation only and frames the azoreductases as two-electron NAD(P)H quinone oxidoreductases, and FMN-dependent azoreductases act by hydride transfer. GO:0003955 (quinol product) is the better fit. Please check whether the semiquinone reaction was chosen deliberately. The paralogs paAzoR2 and paAzoR3 carry RHEA:65952, also a semiquinone-forming reaction.

> Two electron reduction reactions of quinones are carried out by a group of enzymes known as NAD(P)H quinone oxidoreductases.
> — PMID:24915188

## 10. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** UniRule:UR000101231
- **Subject:** UniProtKB:Q9I5F3
- **Field:** GO_ID
- **Change:** delete the record asserting GO:0016652
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/azoR1/azoR1-ai-review.yaml`

UniRule UR000101231 (azoreductase type 1, HAMAP MF_01216) maps GO:0016652 oxidoreductase activity, acting on NAD(P)H, NAD(P) as acceptor. That term is for enzymes in which NAD(P)H reduces NAD(P)+ (EC 1.6.1). Azoreductases transfer electrons from NAD(P)H to quinones and azo compounds; the appropriate terms are GO:0016655 and its child GO:0003955. Checked against the GO definition. The same mapping reaches azoR2 (Q9I2E2) and azoR3 (Q9HZ17) and every MF_01216 member.

## 11. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:O33407 involved_in GO:0008610 lipid biosynthetic process (IMP, PMID:17631636)
- **Field:** GO_ID
- **Change:** check GO:0008610 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/estA/estA-ai-review.yaml`

The IMP lipid biosynthetic process row on EstA (O33407) from PMID:17631636 is based on reduced rhamnolipid in an estA deletion mutant. The UniProt entry itself says the role of EstA is unclear, and EstA is a surface-exposed outer-membrane esterase, not a rhamnolipid synthase. The full text has since been read and does not show EstA acting on a biosynthetic intermediate; the authors state there is no obvious function in the pathway requiring an esterase, report no intracellular rhamnolipid accumulation, and find rhlB and rhlC downregulated in the mutant, placing EstA upstream of the biosynthetic enzymes. Please consider removing the row. It is the sole seed of the PAINT IBD at PTN005219546 (960 leaf IBAs).

## 12. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** Q9HX03
- **Subject:** UniProtKB:Q9HX03
- **Field:** GO annotation / CC:SUBCELLULAR LOCATION
- **Change:** check GO:0031469 (alternatives in the explanation)
- **Recorded in:** `genes/PSEAE/eutB/eutB-ai-review.yaml`

Review organism-specific scope of MF_00861 / its UniRule propagation. PAO1 has the enzyme pair but no recognized shell signatures in its complete reference proteome; an enterobacterial Eut compartment location should not be inferred from enzyme-family membership alone.

> PAO1 has zero matches for each of PF00936,PF03319,IPR000249 and IPR004992; the Ecoli control recovers four BMC-domain proteins and one EutN/CcmL vertex protein.
> — file:PSEAE/eutB/eutB-source-analysis/shell-inventory.yaml

## 13. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** Q9HX03
- **Subject:** UniProtKB:Q9HX03
- **Field:** GO annotation / CC:SUBCELLULAR LOCATION
- **Change:** check GO:0031471 (alternatives in the explanation)
- **Recorded in:** `genes/PSEAE/eutB/eutB-ai-review.yaml`

Review organism-specific scope of MF_00861 / its UniRule propagation. PAO1 has the enzyme pair but no recognized shell signatures in its complete reference proteome; an enterobacterial Eut compartment location should not be inferred from enzyme-family membership alone.

> PAO1 has zero matches for each of PF00936,PF03319,IPR000249 and IPR004992; the Ecoli control recovers four BMC-domain proteins and one EutN/CcmL vertex protein.
> — file:PSEAE/eutB/eutB-source-analysis/shell-inventory.yaml

## 14. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** Q9HX02
- **Subject:** UniProtKB:Q9HX02
- **Field:** GO annotation / CC:SUBCELLULAR LOCATION
- **Change:** check GO:0031469 (alternatives in the explanation)
- **Recorded in:** `genes/PSEAE/eutC/eutC-ai-review.yaml`

Review organism-specific scope of MF_00601 / its UniRule propagation. PAO1 has the enzyme pair but no recognized shell signatures in its complete reference proteome; an enterobacterial Eut compartment location should not be inferred from enzyme-family membership alone.

> PAO1 has zero matches for each of PF00936,PF03319,IPR000249 and IPR004992; the Ecoli control recovers four BMC-domain proteins and one EutN/CcmL vertex protein.
> — file:PSEAE/eutB/eutB-source-analysis/shell-inventory.yaml

## 15. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** Q9HX02
- **Subject:** UniProtKB:Q9HX02
- **Field:** GO annotation / CC:SUBCELLULAR LOCATION
- **Change:** check GO:0031471 (alternatives in the explanation)
- **Recorded in:** `genes/PSEAE/eutC/eutC-ai-review.yaml`

Review organism-specific scope of MF_00601 / its UniRule propagation. PAO1 has the enzyme pair but no recognized shell signatures in its complete reference proteome; an enterobacterial Eut compartment location should not be inferred from enzyme-family membership alone.

> PAO1 has zero matches for each of PF00936,PF03319,IPR000249 and IPR004992; the Ecoli control recovers four BMC-domain proteins and one EutN/CcmL vertex protein.
> — file:PSEAE/eutB/eutB-source-analysis/shell-inventory.yaml

## 16. WRONG_STATEMENT (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9I648   UniProt entry Q9I648 (Q9I648_PSEAE) (, file:PSEAE/fiuA/fiuA-uniprot.txt)
- **Field:** DE RecName
- **Change:** Metal-pseudopaline receptor CntO → Ferrichrome receptor FiuA
- **Recorded in:** `genes/PSEAE/fiuA/fiuA-ai-review.yaml`

The ARBA-derived recommended name (ARBA00072467) names Q9I648 after CntO, the pseudopaline-metal receptor encoded elsewhere in the PAO1 genome. Q9I648 is fiuA (PA0470), the ferrichrome receptor, as the 55Fe uptake data show. The same ARBA name and the matching ARBA FUNCTION text (pseudopaline transport) are on FoxA (Q9I116). Please replace the name and FUNCTION text on this entry.

> ferrichrome is transported across the outer membrane primarily (80%) by the FiuA receptor and to a lesser extent (20%) by a secondary transporter
> — PMID:20047910

## 17. OTHER (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9K3C5 located_in GO:0009421 bacterial-type flagellum filament cap (IDA, PMID:9488388)
- **Field:** SUBUNIT
- **Change:** Homopentamer → Homohexamer
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/fliD/fliD-ai-review.yaml`

The UniProt entry Q9K3C5 records "SUBUNIT: Homopentamer {ECO:0000250}", an inference by similarity. The oligomeric state of PAO1 FliD has since been determined experimentally and it is a hexamer: the FliD78-405 core crystallises as a six-pointed star hexamer (PDB 5FHY), the hexamer is confirmed in solution and by negative-stain EM class averaging, and the same study shows that capping-protein stoichiometry differs between species (Salmonella FliD is a pentamer). Please update the SUBUNIT line to a homohexamer with ECO:0000269|PubMed:27664419 and add PMID:27664419 to the entry.

> Thus, we confirmed that the hexameric assembly of FliD78–405 occurs not only in the crystalline environment but also in solution using negative stain EM class averaging (Tang et al.
> — PMID:27664419

## 18. WRONG_STATEMENT (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9I116   UniProt entry Q9I116 (Q9I116_PSEAE) (, file:PSEAE/foxA/foxA-uniprot.txt)
- **Field:** DE RecName
- **Change:** Metal-pseudopaline receptor CntO → Ferrioxamine receptor FoxA
- **Recorded in:** `genes/PSEAE/foxA/foxA-ai-review.yaml`

The ARBA-derived recommended name (ARBA00072467) and the ARBA FUNCTION text name Q9I116 as the pseudopaline-metal receptor CntO. Q9I116 is foxA (PA2466), the ferrioxamine receptor, as mutant uptake assays show. The same wrong name is on FiuA (Q9I648). Please replace the name and FUNCTION text.

> FoxA of the ferric forms of nocardamine, bisucaberin, DFOB and DFOG
> — PMID:39138320

## 19. OTHER (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9I296
- **Subject:** UniProtKB:Q9I296
- **Field:** DE
- **Change:** Isovaleryl-CoA dehydrogenase, mitochondrial → Isovaleryl-CoA dehydrogenase
- **Recorded in:** `genes/PSEAE/liuA/liuA-ai-review.yaml`

The unreviewed entry Q9I296 (LiuA, PA2015) of the bacterium Pseudomonas aeruginosa PAO1 has the RecName "Isovaleryl-CoA dehydrogenase, mitochondrial" from ARBA:ARBA00018258. Bacteria have no mitochondria; the qualifier comes from the eukaryotic IVD template. The name should be "Isovaleryl-CoA dehydrogenase" (the activity is shown for the purified protein in PMID:18625020).

> Isovaleryl-CoA dehydrogenase, mitochondrial
> — file:PSEAE/liuA/liuA-uniprot.txt

## 20. MISSING_STATEMENT (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9HVF1 enables GO:0008924 L-malate dehydrogenase (quinone) activity (IDA, PMID:12480887)
- **Field:** reference list and protein existence
- **Change:** add cite PMID:12480887 and reflect its in-species experimental evidence to RecName "Probable malate:quinone oxidoreductase 2"; PE 3: Inferred from homology; all CC statements ECO:0000255|HAMAP-Rule:MF_00212; references limited to an EMBL submission and PMID:10984043 (reference list and protein existence)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/mqo2/mqo2-ai-review.yaml`

The entry cites two references: an EMBL submission dated July 2002 (AY129296) and the PAO1 genome paper. PMID:12480887 is absent, although it reports a deletion phenotype, a complementation and a measured dye-dependent MQO activity, and maps its gene to PA4640 in its own closing sentence. The submission date is suggestive: AY129296 was deposited in July 2002 and the paper appeared that December, so the record carries the sequence from that study without the characterisation it was deposited for. The consequences are on the record: the name is qualified "Probable", protein existence is 3 (Inferred from homology), and every functional statement - catalytic activity, cofactor, pathway, family - is HAMAP-rule evidence, with nothing experimental behind any of it. Filed at PROBABLE rather than CONFIRMED for one reason that is UniProt's to weigh, not mine: the work was done in strain ATCC 17933 while this entry is PAO1, so whether the evidence counts as protein-level for this accession is their editorial judgement. What is not in doubt is that the paper exists, concerns this locus by its own statement, and is uncited.

## 21. WRONG_STATEMENT (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9HUL8
- **Subject:** UniProtKB:Q9HUL8
- **Field:** CC:FUNCTION
- **Change:** revise "It is required for dam-dependent methyl-directed DNA mismatch repair." in CC:FUNCTION (see explanation)
- **Likely cause:** OVER_PROPAGATION
- **Recorded in:** `genes/PSEAE/mutL/mutL-ai-review.yaml`

The HAMAP MF_00149 function text describes the E. coli Dam/MutH-directed pathway. P. aeruginosa lacks Dam and MutH homologues, and its MutL is itself a metal-dependent strand-incision endonuclease. The text should describe MutH-independent incision by the MutL endonuclease domain.

> Although Pseudomonas aeruginosa does not have the corresponding E. coli MutH and Dam homologues, and consequently the MMRS seems to work differently
> — PMID:15709980

> In this work we show that Pseudomonas aeruginosa MutL protein possess an in vitro metal ion-dependent endonuclease activity.
> — PMID:21889424

## 22. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9HZZ4 involved_in GO:0006351 DNA-templated transcription (IEA, GO_REF:0000104)
- **Field:** GO_ID
- **Change:** GO:0006351 → GO:0006355 (regulation of DNA-templated transcription)
- **Likely cause:** UNKNOWN
- **Recorded in:** `genes/PSEAE/ohrR/ohrR-ai-review.yaml`

involved_in GO:0006351 DNA-templated transcription (IEA, GO_REF:0000104) on PA2849 (OhrR) comes from a sequence-feature transfer based on the MarR-type HTH domain. A transcriptional repressor is not a participant in transcription itself; the regulation branch (GO:0006355 or, for OhrR, GO:0045892) is intended. Please check the UniRule/ARBA mapping that emits the process term for this HTH family.

> PANTHER; PTHR33164:SF5; ORGANIC HYDROPEROXIDE RESISTANCE TRANSCRIPTIONAL REGULATOR; 1.
> — file:PSEAE/ohrR/ohrR-uniprot.txt

## 23. WRONG_STATEMENT (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q51553
- **Subject:** UniProtKB:Q51553
- **Field:** DE EC
- **Change:** revise "EC:2.4.1.-" in DE EC (see explanation)
- **Recorded in:** `genes/PSEAE/phaG/phaG-ai-review.yaml`

The frozen EC2.4.1.- designation classifies glycosyl transfer, whereas supported PhaG chemistry transfers a hydroxyacyl group between CoA and ACP. Correct the EC classification to the appropriate acyltransferase class after resource review; no specific fourth-level EC is asserted here. The raw record is preserved.

> Catalyzes the transfer of the acyl moiety from in vitro synthesized 3-hydroxydecanoyl-CoA to acyl carrier protein.
> — file:PSEAE/phaG/phaG-uniprot.txt

## 24. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:G3XDA8 located_in GO:0005576 extracellular region (EXP, PMID:18282104)
- **Field:** GO_ID
- **Change:** GO:0005576 → GO:0009986 (cell surface)
- **Recorded in:** `genes/PSEAE/pstS/pstS-ai-review.yaml`

The GO:0005576 extracellular region row on PA5369 (UniProtKB:G3XDA8), evidence EXP from PMID:18282104, appears to use the wrong member of a mutually exclusive pair. GO's comment on GO:0005576 states it is "intended to annotate gene products that are not attached to the cell surface. For gene products at the cell surface, consider a[nother term]", and the comment on GO:0009986 cell surface states it is for products "attached (integrated or loosely bound) to the plasma membrane or cell wall". GO:0005576 is not an ancestor of GO:0009986, so one does not subsume the other. The cited paper describes attached protein throughout: "outer surface PstS", "Formation of the PstS rich appendages", and a reduction in surface PstS in a DeltaHxcR secretion mutant. Marked PROBABLE rather than CONFIRMED because a type II secretion system can release protein as well as display it, so a genuinely released fraction may exist even though the evidence presented is for surface-associated protein. Requested change: repoint this row to GO:0009986, or retain GO:0005576 only if a released, unattached pool has been demonstrated.

> significantly less outer surface PstS was observed in the MPAO1 mutant DeltaHxcR thus establishing a role for the alternative type II secretion system Hxc in outer surface PstS expression
> — PMID:18282104

## 25. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9I157 involved_in GO:0071766 Actinobacterium-type cell wall biogenesis (IEA, GO_REF:0000117)
- **Field:** GO term
- **Change:** delete the record asserting GO:0071766
- **Likely cause:** OVER_PROPAGATION
- **Recorded in:** `genes/PSEAE/pvdL/pvdL-ai-review.yaml`

GO:0071766 Actinobacterium-type cell wall biogenesis is annotated to PvdL (PA2424, Q9I157) of Pseudomonas aeruginosa by ARBA:ARBA00050076. P. aeruginosa is a Pseudomonadota, not an Actinomycetota, and does not build an Actinobacterium-type cell wall, so the process does not occur in this organism and the annotation cannot be correct whatever the protein does. Stated at CONFIRMED because it rests on the taxon of the annotated entry rather than on any reading of the protein's function. The likely cause is the fatty acyl-AMP ligase domain IPR040097, shared with mycobacterial FAAL enzymes that do participate in cell-envelope lipid assembly; the association rule should carry a taxonomic restriction, since the same transfer will affect other FAAL-domain proteins outside the Actinomycetota.

> DR InterPro; IPR040097; FAAL/FAAC.
> — file:PSEAE/pvdL/pvdL-uniprot.txt

## 26. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:G3XCY5 enables GO:0031071 cysteine desulfurase activity (IEA, GO_REF:0000003)
- **Field:** Protein name
- **Change:** check cysteine desulfurase (EC 2.8.1.7) (alternatives in the explanation)
- **Likely cause:** OVER_PROPAGATION
- **Recorded in:** `genes/PSEAE/pvdN/pvdN-ai-review.yaml`

G3XCY5 (pvdN, PA2394) is named "cysteine desulfurase" with EC 2.8.1.7 on the strength of ARBA association rules alone - ARBA00012239 for the name and EC, ARBA00050776 for the catalytic activity, ARBA00010447 for the Csd subfamily assignment - with no curated or experimental statement behind any of them. The protein is in fact a periplasmic pyoverdine side-chain tailoring enzyme: it is periplasmic by direct evidence, required for pyoverdine biosynthesis by one IDA and three IMP rows, and the pathway review (PMID:30386787) states that PvdN generates the succinamide residue of the siderophore, with the paralogue PtaA making the alternative alpha-ketoglutarate form. What it shares with the cysteine desulfurases is the class-V PLP-dependent aminotransferase fold, which is common to enzymes acting on quite different substrates. The misassignment propagates: the EC number feeds an EC2GO row for GO:0031071 on this entry, and the same fold also draws an IBA from a PAINT node seeded entirely by genuine cysteine desulfurases (E. coli SufS and CsdA, B. subtilis SufS, P. falciparum SufS), so correcting the name and EC would clear the derived annotation at source. UniProt's own protein-specific NCBIfam model for this entry, NF051467 peri_mod_PvdN, is named for periplasmic modification and not for sulfur mobilisation, so the record is internally inconsistent on this point. There is one piece of counter-evidence, and it has to be named. The record cites two crystal structures of the purified protein, both with PLP bound. PDB 5I90 is published (PMID:27139833) and supports the correction rather than the current name: it is titled for a periplasmic aminotransferase, finds high structural homology to type I aspartate aminotransferases - not to the class-V Csd subfamily the SIMILARITY line asserts - and calls the step PvdN catalyses uncharacterized. PDB 5HH9 is the problem: its deposition title claims structural and biochemical characterization of a novel L-cystine desulfurase involved in the biosynthesis of the major siderophore pyoverdine, which is a direct claim of desulfurase activity on this protein in this pathway. Three things limit what it can settle. It is a PDB deposition and nothing more - the record shows it as submitted to the PDB in January 2016 with no literature citation, so the asserted biochemical characterisation was never published or refereed. It names L-cystine, the disulfide, whereas this row's term and EC number are for the L-cysteine reaction, so even at face value it is not evidence for GO:0031071 or EC 2.8.1.7. And it is contradicted on function by the published structure of the same protein at higher resolution, and by the in-frame deletion phenotype, which abolishes only the succinamide and succinic acid pyoverdine forms. That unresolved claim is exactly why this is raised at PROBABLE with CHECK rather than CONFIRMED with a correction: there is an unpublished assertion of the opposite activity that a UniProt curator is better placed than I am to weigh, and the positive identification of PvdN's real reaction comes from a review rather than from primary enzymology I read. If the 5HH9 work is published and holds, the protein is bifunctional and the name may stand; if it is not, the ARBA chain is the whole basis for it.

> PvdN generates the succinamide residue
> — PMID:30386787

> The PvdN model shows high structural homology to type I aspartate aminotransferases
> — PMID:27139833

> DR NCBIfam; NF051467; peri_mod_PvdN; 1.
> — file:PSEAE/pvdN/pvdN-uniprot.txt

> RL Submitted (JAN-2016) to the PDB data bank.
> — file:PSEAE/pvdN/pvdN-uniprot.txt

## 27. WRONG_STATEMENT (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9I6J2
- **Subject:** UniProtKB:Q9I6J2
- **Field:** CC:INDUCTION
- **Change:** revise "By putrescine and agmatine." in CC:INDUCTION (see explanation)
- **Recorded in:** `genes/PSEAE/spuC/spuC-ai-review.yaml`

The INDUCTION line of UniProtKB:Q9I6J2 reads "By putrescine and agmatine. Also regulated by the global CbrA/CbrB two-component system." with evidence ECO:0000269|PubMed:12081945. That paper reaches the opposite conclusion about agmatine, and says so in its abstract: "Since the observed induction effect of agmatine was abolished in an aguA mutant where conversion of agmatine into putrescine was blocked, putrescine or spermidine, but not agmatine, serves as the inducer molecule of the spuA-spuI divergent promoters." The agmatine effect is indirect, mediated by its conversion to putrescine, and the paper identifies spermidine as the second genuine inducer. The line appears to have been written from the experiments rather than from the authors' interpretation of them. Requested change: check the line against the cited paper; it should read "By putrescine and spermidine", optionally noting that agmatine induces indirectly through conversion to putrescine.

> Since the observed induction effect of agmatine was abolished in an aguA mutant where conversion of agmatine into putrescine was blocked, putrescine or spermidine, but not agmatine, serves as the inducer molecule of the spuA-spuI divergent promoters.
> — PMID:12081945

## 28. OTHER (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:G3XD94 located_in GO:0016020 membrane (IEA, GO_REF:0000044)
- **Change:** delete the record asserting GO:0016020
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/wbpA/wbpA-ai-review.yaml`

G3XD94 (WbpA) carries a predicted TRANSMEM 13..32 (ECO:0000255) and a Membrane / single-pass subcellular location, which generate GO:0016020. The segment SRQALIGIVGLGYVGLPLML contains the GxGxxG NAD-binding motif at the N-terminus of the UDP-glucose/GDP-mannose dehydrogenase Rossmann fold, and WbpA was purified as a soluble His-tagged oligomer (PMID:15226302). Please review the TRANSMEM feature and location.

## 29. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:G3XD61 enables GO:0008761 UDP-N-acetylglucosamine 2-epimerase activity (IDA, PMID:17346239)
- **Change:** check GO:0008761 (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/wbpI/wbpI-ai-review.yaml`

GO:0008761 is defined as UDP-N-acetyl-D-glucosamine = UDP-N-acetyl-D-mannosamine. PMID:17346239 shows that WbpI catalyses UDP-GlcNAc3NAcA = UDP-ManNAc3NAcA (EC 5.1.3.23, RHEA:24764) and does not use UDP-GlcNAc. GO has no term for EC 5.1.3.23; use GO:0016857 until one is created (a new term is proposed in this review), and do not use GO:0008761.

> Neither enzyme utilized UDP-alpha-D-GlcNAc, UDP-alpha-D-GlcNAcA (UDP-2-acetamido-2,3-dideoxy-alpha-D-glucuronic acid) or UDP-alpha-D-GlcNAc3NAc (UDP-2,3-diacetamido-2,3-dideoxy-alpha-D-glucose) as substrates.
> — PMID:17346239

## 30. WRONG_QUALIFIER (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9HT73
- **Subject:** UniProtKB:Q9HT73
- **Field:** Qualifier
- **Change:** check enables (alternatives in the explanation)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/znuC/znuC-ai-review.yaml`

The EC 7.2.2.20 / RHEA:29795 transport reaction is carried out by the ZnuABC complex. ZnuC is the nucleotide-binding subunit and has no transmembrane segment, so it cannot translocate Zn(2+) on its own; the UniProt record itself states that the complex comprises two ZnuC, two ZnuB and one ZnuA. contributes_to GO:0015633 would be the accurate qualifier for the subunit, as is done for other ABC importer ATPases.

> The complex is composed of two ATP-binding proteins (ZnuC),
> — file:PSEAE/znuC/znuC-uniprot.txt
