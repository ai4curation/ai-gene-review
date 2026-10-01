---
title: "Toll and Toll-like Receptor Family"
maturity: IN_PROGRESS
tags: [BIOLOGY_DOMAIN]
species: [human, mouse, CHICK, DANRE, DROME, worm]
---

# Toll and Toll-like Receptor Family

Part of [Innate Immune System Pathways Across Animals](../INNATE_IMMUNITY.md).

**Bottom line:** batch 1 is reviewed. All ten human TLRs, mouse Tlr11–13,
chicken TLR15 and TLR21, zebrafish tlr5b, tlr21 and tlr22, Drosophila Toll
(Tl), 18w and Toll-7, and *C. elegans* TOL-1 now have complete reviews, as do
the accessory proteins and adaptors listed below — 37 gene products and 2,734
existing annotations in all. The Toll/TLR split held up: no fly Toll receptor
carries a vertebrate TLR-pathway term, but the fly Toll-pathway term had leaked
the other way, onto human IRAK4 and MYD88 by phylogenetic inference. Findings
by question are at the end of this page.

The family is the clearest test in the project of whether one name hides
different functions. Vertebrate TLRs are pattern recognition receptors, each
binding a class of microbial molecule. Drosophila Toll is a cytokine receptor
for cleaved Spätzle. *C. elegans* TOL-1 is the single nematode Toll and its role
in immunity is limited. GO reflects this with separate process terms —
GO:0002224 toll-like receptor signaling pathway and GO:0008063 Toll signaling
pathway.

## Receptors

"TrEMBL" entries are unreviewed; the accession shown is the reference-proteome
match on primary gene name. For chicken TLR15 and TLR21, which have several
reference-proteome records, the entry GOA annotates most was chosen and pinned in
`candidates.tsv`; the reviewer confirmed both against Ensembl, NCBI and ZFIN.

| Species | Gene | Accession | Entry | UniProt name | GO pathway term for this receptor | Reviewed |
|---------|------|-----------|-------|--------------|-----------------------------------|----------|
| human | TLR1 | Q15399 | Swiss-Prot | Toll-like receptor 1 | GO:0034130 | yes |
| human | TLR2 | O60603 | Swiss-Prot | Toll-like receptor 2 | GO:0034134 | yes |
| human | TLR3 | O15455 | Swiss-Prot | Toll-like receptor 3 | GO:0034138 | yes |
| human | TLR4 | O00206 | Swiss-Prot | Toll-like receptor 4 | GO:0034142 | yes |
| human | TLR5 | O60602 | Swiss-Prot | Toll-like receptor 5 | GO:0034146 | yes |
| human | TLR6 | Q9Y2C9 | Swiss-Prot | Toll-like receptor 6 | GO:0034150 | yes |
| human | TLR7 | Q9NYK1 | Swiss-Prot | Toll-like receptor 7 | GO:0034154 | yes |
| human | TLR8 | Q9NR97 | Swiss-Prot | Toll-like receptor 8 | GO:0034158 | yes |
| human | TLR9 | Q9NR96 | Swiss-Prot | Toll-like receptor 9 | GO:0034162 | yes |
| human | TLR10 | Q9BXR5 | Swiss-Prot | Toll-like receptor 10 | GO:0034166 | yes |
| mouse | `Tlr4` | Q9QUK6 | Swiss-Prot | Toll-like receptor 4 | GO:0034142 | no |
| mouse | Tlr11 | Q6R5P0 | Swiss-Prot | Toll-like receptor 11 | GO:0034170 | yes |
| mouse | Tlr12 | Q6QNU9 | Swiss-Prot | Toll-like receptor 12 | GO:0034174 | yes |
| mouse | Tlr13 | Q6R5N8 | Swiss-Prot | Toll-like receptor 13 | GO:0034178 | yes |
| CHICK | `TLR3` | A0A8V0YT51 | TrEMBL | Toll-like receptor 3 | GO:0034138 | no |
| CHICK | `TLR4` | C4PCF3 | TrEMBL | Toll-like receptor 4 | GO:0034142 | no |
| CHICK | `TLR7` | A0A1L4FML6 | TrEMBL | Toll like receptor 7 | GO:0034154 | no |
| CHICK | TLR15 | A0A8V0Z0H8 | TrEMBL | Toll-like receptor 15 | GO:0035681 | yes |
| CHICK | TLR21 | A0A8V0ZKW5 | TrEMBL | Toll like receptor 21 | GO:0035682 | yes |
| DANRE | `tlr3` | A0A8M1N4E3 | TrEMBL | Toll-like receptor 3 | GO:0034138 | no |
| DANRE | `tlr4ba` | A0A8M3B7X7 | TrEMBL | Toll-like receptor 4 | GO:0034142 (see question 2) | no |
| DANRE | `tlr5a` | F8W4F1 | TrEMBL | Toll-like receptor 5 | GO:0034146 | no |
| DANRE | tlr5b | A0ACM8R384 | TrEMBL | Toll-like receptor 5b precursor | GO:0034146 | yes |
| DANRE | `tlr18` | A3KH14 | TrEMBL | Toll-like receptor 18 isoform X4 | none | no |
| DANRE | `tlr19.1` | A0A8M1RKQ4 | TrEMBL | Toll-like receptor 12 (sic) | none | no |
| DANRE | `tlr20.2` | F1QRG0 | TrEMBL | Toll-like receptor 20, tandem duplicate 2 | none | no |
| DANRE | tlr21 | F1QMN8 | TrEMBL | Toll-like receptor 21 precursor | GO:0035682 | yes |
| DANRE | tlr22 | A0A2R8RTN4 | TrEMBL | Toll-like receptor 22 precursor | none | yes |
| DROME | Tl | P08953 | Swiss-Prot | Protein toll | GO:0008063 (Toll signaling pathway) | yes |
| DROME | 18w | A1ZBR2 | TrEMBL | 18 wheeler | — | yes |
| DROME | Toll-7 | Q7KIN0 | Swiss-Prot | Toll-like receptor 7 | — | yes |
| worm | tol-1 | Q9N5Z3 | TrEMBL | TIR domain-containing protein | — | yes |

The ligand, Drosophila Spätzle (spz, P48607, Swiss-Prot), is listed with the
receptors because it is what activates Tl. The pathway-term column records
which GO term *exists* for that receptor, checked against OLS on 2026-09-30.
It does not record what the gene is annotated to — that is what the reviews will
establish. GO has no pathway term for TLR14, TLR16, TLR17, TLR18, TLR19,
TLR20 or TLR22.

Zebrafish tlr19.1 (A0A8M1RKQ4) carries the submitter name "Toll-like receptor
12"; other entries for the gene carry the matching name, so choose the entry
before fetching it.

**Mouse Tlr11 and Tlr12 names are swapped between the literature and the
databases.** The paper that calls its protein "`TLR12`" (PMID:23246311) gives
RefSeq NP_991388.1, which UniProt maps to Q6R5P0 — the entry MGI and UniProt
name Tlr11. Both UniProt entries carry a caution that the literature swaps the
two names. Because the numbered GO terms GO:0034170 and GO:0034174 are named
after the literature receptors, neither review assigns them; both use
GO:0002224 and raise the naming as a question for GO and MGI.

## Accessory proteins and adaptors in this batch

Human CD14 (P08571), LY96/MD-2 (Q9Y6Y9), LBP (P18428), UNC93B1 (Q9H1C4),
MYD88 (Q99836), TIRAP (P58753), TICAM1 (Q8IUC6), TICAM2 (Q86XR7) and IRAK4 (Q9NWZ3);
Drosophila Myd88, Tube, Pelle, Cactus, Dorsal and Dif; Nematostella MyD88
(A7RHZ4). CD14, LY96 and LBP are ligand-delivery and co-receptor proteins; the
test for them is the same as for the receptors — which of them performs the
recognition step (see CLAUDE.md, *Do not add what curators deliberately
declined to add*).

## Findings by question

The review for each gene holds the evidence; this summarises the cross-gene
answers.

1. **Toll is not a PRR — confirmed.** Tl and 18w carry no pattern recognition
   receptor activity and no GO:0002224-branch term. Tl's immune and
   dorsoventral roles both rest on one function, cytokine receptor for Spätzle
   in GO:0008063. 18w's immune rows are marked over-annotated: its larval
   immune defect comes from delayed fat-body development. Toll-7 is the one
   exception: it carries GO:0038187 by curator inference from virion
   co-precipitation. Those rows are kept as non-core, not accepted, because no
   viral ligand is defined and a later paper contradicts the specificity
   control.
2. **The fly term leaks onto human proteins.** GO:0008063 is defined by ligand
   binding to "the receptor Toll", yet human IRAK4 and MYD88 carry it by IBA
   (PAINT nodes PTN000701353 and PTN000386853, fly donors) and MYD88 also by a
   rat-derived IEA. Both reviews change these to GO:0002755 MyD88-dependent
   toll-like receptor signaling pathway and question the node placement.
3. **Ligand-specific terms on orthologues and partners.** Challenged where the
   ligand is not shared: triacyl lipopeptide binding on chicken TLR15 (transferred from
   human TLR2; TLR15 is not a TLR2 orthologue and lipopeptides do not activate
   it), LPS-mediated signaling on fly Pelle and Tube (removed), the TLR8 pathway
   term on TLR7 (removed), and LPS receptor activity on TLR1, TLR2 and TLR6,
   which recognise lipopeptides: modified to pattern recognition receptor
   activity on TLR1, TLR2 and TLR6 (TLR2's review-article row is removed). The
   rows come from GO-CAMs 5fb9cc0600000727 and 5fce9b7300000030, now reviewed
   in their `GoCamReview` files. Numbered pathway terms were kept where receptor
   identity is clear (TLR15, TLR21 in chicken and zebrafish, zebrafish tlr5b).
4. **Missing pathway terms.** For zebrafish tlr22, GO:0002224 is sufficient for
   now: no ligand or adaptor has been shown in zebrafish (the dsRNA work was in
   fugu), and fish TLR21/22/23 naming is unstable. No new term is requested.
5. **No TLR-specific molecular function.** Reviews use GO:0038187 pattern
   recognition receptor activity plus a ligand-binding term (dsRNA, unmethylated
   CpG, lipopeptide, guanosine, LPS). Only TLR4 keeps GO:0001875 LPS immune
   receptor activity as core; MD-2 (LY96) records it as contributes_to, and
   CD14 is changed to molecular carrier activity because it delivers LPS but
   cannot signal across the membrane. Chicken TLR15, which is
   protease-activated, keeps generic signaling receptor activity.
6. **TLR10 is inhibitory.** Confirmed from cached primary papers. Its inherited
   positive-signaling rows are kept as non-core, and it gains NEW negative
   regulation of toll-like receptor signaling pathway (GO:0034122).
7. **Nematostella.** The single cnidarian protein reviewed is MyD88 (A7RHZ4, a
   fragment). No Nematostella TLR accession has yet been asserted.
