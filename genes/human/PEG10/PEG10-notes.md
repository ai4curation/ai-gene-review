# PEG10 (human, Q86TG7) — review notes

Family-batched SIRH/RTL review. PEG10 = SIRH1, founding family member.

## Key verified facts (primary sources)
- Domesticated Ty3/gypsy LTR retrotransposon; paternally imprinted, 7q21 [PMID:22866050 "PEG10 (SIRH1) and PEG11/RTL1 (SIRH2) play essential but different roles in placental development"].
- Essential for placentation; Peg10-null mice die ~E10.5 [PMID:16341224 "Peg10\nknockout mice showed early embryonic lethality owing to defects in the placenta"].
- Gag capsid self-assembles into VLPs; packages own mRNA; intercellular transfer (SEND) [PMID:34413232 "preferentially binds and facilitates vesicular secretion of its own messenger RNA"].
- X-ray CA fold confirms Gag ancestry [PMID:34357660 "highly similar to the C-terminal capsid (CA) domains of cognate Gag proteins"].
- -1 frameshift GAG / GAG-POL; ORF2 aspartic protease active, autoprocesses; DSG motif, D370A abolishes cleavage [PMID:17942406 "this enzyme is active and participates in post-translational processing of PEG10 ORF1-2"; PMID:32244497 "corresponds to the consensus -Asp-Ser/Thr-Gly- active-site motif of retroviral aspartic proteases"].
- Protease motif essential in vivo for placental fetal capillaries [PMID:34559199].
- Binds/inhibits TGF-beta receptors ALK1/ALK5 [PMID:15611116 "PEG10-RF1 inhibits ALK1 as well as ALK5 signaling"].
- Antagonizes pro-apoptotic SIAH1 [PMID:12810624].
- Disease: HCC/B-CLL oncofetal reactivation; ALS via UBQLN2 [PMID:36951542]; Angelman via UBE3A [PMID:34467244]; preeclampsia via VLP transfer + TGFbeta inhibition [PMID:38715110].

## Decisions
- 15 bare GO:0005515 rows: ACVRL1 (P37023) MODIFY -> GO:0005160 (TGF-beta receptor binding); all others REMOVE per protein-binding policy (interactions not denied; SIAH1/anti-apoptotic captured in description).
- nucleic acid binding IEA -> TOO_GENERAL (RNA/mRNA binding asserted).
- NEW MF: GO:0039660 structural constituent of virion; GO:0004190 aspartic-type endopeptidase activity (isoform Q86TG7-1).
- OpenScientist report integrated (leads verified against primary sources; cited as file:).
