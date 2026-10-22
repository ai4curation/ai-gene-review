# BAT1 (YHR208W, P38891) notes

Batch: YeastPathways module `branched_chain_amino_acid_biosynthesis` (no paid deep research run).

## Identity and activity
- Mitochondrial branched-chain amino acid aminotransferase, EC 2.6.1.42 [UniProt:P38891 "RecName: Full=Branched-chain-amino-acid aminotransferase, mitochondrial"].
- Matrix targeting: [PMID:8798704 "encodes a protein of 393 amino acid residues with an NH2-terminal extension that directs Bat1p to the mitochondrial matrix"].
- Activity: [PMID:8798704 "Mitochondria and cytosol isolated from bat1 and bat2 deletion mutants, respectively, contained largely reduced activities for the conversion of branched-chain 2-ketoacids to their corresponding amino acids"]; [PMID:8702755 "ECA39 and ECA40 code for mitochondrial and cytosolic branched-chain amino acid aminotransferases, respectively"].
- Double mutant auxotrophy: [PMID:8798704 "deletion of both genes resulted in an auxotrophy for branched-chain amino acids (Ile, Leu, and Val)"].

## Paralog subfunctionalization (WGD pair with BAT2)
- [PMID:21267457 "Above presented results indicate that in a wild type strain Bat1 displays a biosynthetic character while Bat2 has a prominent catabolic role."]
- [PMID:21267457 "These results indicate that Bat2 has a prominent role in VIL catabolism, while Bat1 catabolic role is only evidenced in a bat2Δ genetic background"]
- K. lactis single ortholog KlBat1 is bifunctional and presequence-bearing (ancestral state) [PMID:21267457].

## Secondary roles
- KMTB -> methionine transamination in methionine salvage (UniProt citing PMID:18625006, not cached) [UniProt:P38891 "from 2-keto-4-methylthiobutyrate (KMTB) in the methionine salvage"]. Non-core.
- TORC1/cell-cycle links (UniProt, PMIDs 26659116, 37497662; not cached) likely metabolic/indirect; not annotated.

## Curation observations
- 9 RCA `is_active_in cytosol` rows from YeastPathways: wrong for Bat1 (matrix) -> REMOVE.
- All 9 RCA MF rows use GO:0052656 (isoleucine transaminase) even where the YeastPathways reaction is the Leu (BRANCHED-CHAINAMINOTRANSFERLEU-RXN), Val, or methionine-salvage R15-RXN reaction: a conversion artefact. MF still true for the protein, so ACCEPT, flagged in suggested_questions.
- protein binding IPIs are all with the paralog Bat2 (HT AP-MS) -> REMOVE (uninformative).
