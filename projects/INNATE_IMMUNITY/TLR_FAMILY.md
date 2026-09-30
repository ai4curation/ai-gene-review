---
title: "Toll and Toll-like Receptor Family"
maturity: SCOPING
tags: [BIOLOGY_DOMAIN]
species: [human, mouse, CHICK, DANRE, DROME, worm]
---

# Toll and Toll-like Receptor Family

Part of [Innate Immune System Pathways Across Animals](../INNATE_IMMUNITY.md).

**Bottom line:** the first review batch. 32 Toll/TLR receptors from five
species are listed below with UniProt accessions resolved by
[`resolve_candidates.py`](scripts/resolve_candidates.py); none has been
reviewed yet. The family is the clearest test in the project of whether one
name hides different functions. Vertebrate TLRs are pattern recognition
receptors, each binding a class of microbial molecule. Drosophila Toll is a
cytokine receptor for cleaved Spätzle. *C. elegans* TOL-1 is the single
nematode Toll and its role in immunity is limited. GO reflects this with
separate process terms — GO:0002224 toll-like receptor signaling pathway and
GO:0008063 Toll signaling pathway — but annotations propagated by domain or
phylogeny can cross that line.

## Receptors

"TrEMBL" entries are unreviewed; the accession shown is the highest
annotation-score match on primary gene name and must be confirmed before
`just fetch-gene`.

| Species | Gene | Accession | Entry | UniProt name | GO pathway term for this receptor |
|---------|------|-----------|-------|--------------|-----------------------------------|
| human | TLR1 | Q15399 | Swiss-Prot | Toll-like receptor 1 | GO:0034130 |
| human | TLR2 | O60603 | Swiss-Prot | Toll-like receptor 2 | GO:0034134 |
| human | TLR3 | O15455 | Swiss-Prot | Toll-like receptor 3 | GO:0034138 |
| human | TLR4 | O00206 | Swiss-Prot | Toll-like receptor 4 | GO:0034142 |
| human | TLR5 | O60602 | Swiss-Prot | Toll-like receptor 5 | GO:0034146 |
| human | TLR6 | Q9Y2C9 | Swiss-Prot | Toll-like receptor 6 | GO:0034150 |
| human | TLR7 | Q9NYK1 | Swiss-Prot | Toll-like receptor 7 | GO:0034154 |
| human | TLR8 | Q9NR97 | Swiss-Prot | Toll-like receptor 8 | GO:0034158 |
| human | TLR9 | Q9NR96 | Swiss-Prot | Toll-like receptor 9 | GO:0034162 |
| human | TLR10 | Q9BXR5 | Swiss-Prot | Toll-like receptor 10 | GO:0034166 |
| mouse | Tlr4 | Q9QUK6 | Swiss-Prot | Toll-like receptor 4 | GO:0034142 |
| mouse | Tlr11 | Q6R5P0 | Swiss-Prot | Toll-like receptor 11 | GO:0034170 |
| mouse | Tlr12 | Q6QNU9 | Swiss-Prot | Toll-like receptor 12 | GO:0034174 |
| mouse | Tlr13 | Q6R5N8 | Swiss-Prot | Toll-like receptor 13 | GO:0034178 |
| CHICK | TLR3 | A0A8V0YT51 | TrEMBL | Toll-like receptor 3 | GO:0034138 |
| CHICK | TLR4 | C4PCF3 | TrEMBL | Toll-like receptor 4 | GO:0034142 |
| CHICK | TLR7 | A0A1L4FML6 | TrEMBL | Toll like receptor 7 | GO:0034154 |
| CHICK | TLR15 | Q2XQ10 | TrEMBL | Toll-like receptor 2 (sic) | GO:0035681 |
| CHICK | TLR21 | A0A8V0ZYL3 | TrEMBL | Toll like receptor 21 | GO:0035682 |
| DANRE | tlr3 | Q32PW5 | TrEMBL | Toll-like receptor 3 | GO:0034138 |
| DANRE | tlr4ba | A0A8M3B7X7 | TrEMBL | Toll-like receptor 4 | GO:0034142 (see question 2) |
| DANRE | tlr5a | F8W4F1 | TrEMBL | Toll-like receptor 5 | GO:0034146 |
| DANRE | tlr5b | F8W3J5 | TrEMBL | Toll-like receptor 5b | GO:0034146 |
| DANRE | tlr18 | A3KH14 | TrEMBL | Toll-like receptor 18 isoform X4 | none |
| DANRE | tlr19.1 | A0A8M1RKQ4 | TrEMBL | Toll-like receptor 12 (sic) | none |
| DANRE | tlr20.2 | F1QRG0 | TrEMBL | Toll-like receptor 20, tandem duplicate 2 | none |
| DANRE | tlr21 | F1QMN8 | TrEMBL | Toll-like receptor 21 precursor | GO:0035682 |
| DANRE | tlr22 | A0A2R8RTN4 | TrEMBL | Toll-like receptor 22 precursor | none |
| DROME | Tl | P08953 | Swiss-Prot | Protein toll | GO:0008063 (Toll signaling pathway) |
| DROME | 18w | A1ZBR2 | TrEMBL | 18 wheeler | — |
| DROME | Toll-7 | Q7KIN0 | Swiss-Prot | Toll-like receptor 7 | — |
| worm | tol-1 | Q9N5Z3 | TrEMBL | TIR domain-containing protein | — |

The ligand, Drosophila Spätzle (spz, P48607, Swiss-Prot), is listed with the
receptors because it is what activates Tl. The pathway-term column records
which GO term *exists* for that receptor, checked against OLS on 2026-09-30.
It does not record what the gene is annotated to — that is what the reviews will
establish. GO has no pathway term for TLR14, TLR16, TLR17, TLR18, TLR19,
TLR20 or TLR22.

Two TrEMBL names disagree with the gene symbol: chicken TLR15 (Q2XQ10) is
named "Toll-like receptor 2", and zebrafish tlr19.1 (A0A8M1RKQ4) is named
"Toll-like receptor 12". Both are submitter names on unreviewed entries; other
entries for the same genes carry the matching name, so choose the entry before
fetching.

## Accessory proteins and adaptors in this batch

Human CD14 (P08571), LY96/MD-2 (Q9Y6Y9), LBP (P18428), UNC93B1 (Q9H1C4),
MYD88 (Q99836), TIRAP (P58753), TICAM1 (Q8IUC6), TICAM2 (Q86XR7) and IRAK4 (Q9NWZ3);
Drosophila Myd88, Tube, Pelle, Cactus, Dorsal and Dif; Nematostella MyD88
(A7RHZ4). CD14, LY96 and LBP are ligand-delivery and co-receptor proteins; the
test for them is the same as for the receptors — which of them performs the
recognition step (see CLAUDE.md, *Do not add what curators deliberately
declined to add*).

## Questions for this batch

Biological claims below marked "reported" are leads from background knowledge
and must be sourced (deep research, cached PMIDs) before they are used in a
review.

1. **Toll is not a PRR.** Check Tl, 18w and Toll-7 for GO:0038187 pattern
   recognition receptor activity or any GO:0002224-branch term. Toll-7 has
   been reported to act in antiviral defence in the fly; decide from the
   literature whether that supports a direct recognition MF or only a process
   term.
2. **Ligand-specific terms on orthologues.** Human TLR ligand terms (e.g. TLR4
   and LPS) should transfer only to orthologues that keep the ligand. Chicken
   TLR4 and the zebrafish tlr4 paralogues are the check: fish TLR4 has been
   reported not to respond to LPS in the way mammalian TLR4 does.
3. **Missing pathway terms.** Fish tlr18–20 and tlr22 have no numbered term.
   Decide per gene whether GO:0002224 is sufficient or a new term is justified.
4. **TLR10.** Human TLR10 is reported as an inhibitory TLR; check that
   propagated positive-signaling terms fit the experimental evidence.
5. **Nematostella.** 17 Nematostella UniProt entries carry a TIR domain but
   none is named a Toll-like receptor. Identify the TLR (if any) with a domain
   architecture check (LRR + transmembrane + TIR) before asserting an
   accession.
