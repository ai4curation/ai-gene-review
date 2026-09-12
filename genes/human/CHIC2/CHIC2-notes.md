# CHIC2 (Cysteine-rich hydrophobic domain-containing protein 2) — Review Notes

UniProt: Q9UKJ5 (CHIC2_HUMAN); Gene: CHIC2; Synonym: BTL ("BrX-like translocated in leukemia"); 165 aa; HGNC:1935; locus 4q12.

## Core biology

- CHIC2 is a small (165 aa, ~19 kDa) protein and the founding/defining member of the CHIC family, characterized by a single **cysteine-rich hydrophobic (CHIC) motif** (residues 88–106) [file:human/CHIC2/CHIC2-uniprot.txt MOTIF 88..106].
- It is **palmitoylated** within the CHIC motif, and palmitoylation is **required for membrane association** [PMID:11257495 "Palmitoylation in the CHIC motif is required for membrane association"]. Mutagenesis of the cysteine cluster (88-CGCLCCCC-95 → SGSLSSSS) causes **loss of palmitoylation and abolishes membrane association** [file:human/CHIC2/CHIC2-uniprot.txt MUTAGEN 88..95].
- Subcellular location (experimental, IDA): **cell membrane / plasma membrane** and **cytoplasmic vesicle**; also present at a **Golgi-like vesicular compartment and at scattered vesicles** [PMID:11257495; file:human/CHIC2/CHIC2-uniprot.txt SUBCELLULAR LOCATION].
- The N-terminus (1–26) is predicted coiled-coil (acidic, EEEDEE-rich) [file:human/CHIC2/CHIC2-uniprot.txt COILED 1..26].
- Pfam: Erf4 (PF10256); InterPro: CHIC1/2 (IPR039735), Golgin_A_7/ERF4 (IPR019383); PANTHER PTHR13005. The Erf4/Golgin-A7 relationship suggests possible roles in vesicle/Golgi-associated trafficking and protein palmitoylation/processing, but a defined molecular function for CHIC2 is not established.

## Molecular function — poorly defined

- The molecular function of CHIC2 is **not experimentally established**. It has been implicated broadly in **cytokine secretion and vesicle trafficking** (literature/secondary sources), consistent with its palmitoylated membrane/vesicle localization, but no direct biochemical activity has been demonstrated.
- All GO molecular-function annotations in GOA are **bare `protein binding` (GO:0005515, IPI)** derived from **high-throughput interactome / Y2H mapping projects** (CCSB/Human Reference Interactome and network-prediction studies):
  - PMID:16189514 — Rual et al., "Towards a proteome-scale map of the human protein-protein interaction network" (HT Y2H).
  - PMID:19060904 — Venkatesan et al., "An empirical framework for binary interactome mapping" (HT Y2H benchmarking).
  - PMID:25416956 — Rolland et al., "A proteome-scale map of the human interactome network" (HI-II-14).
  - PMID:30886144 — Kovács et al., "Network-based prediction of protein interactions" (computational prediction).
  - PMID:32296183 — Luck et al., "A reference map of the human binary protein interactome" (HuRI).
- The UniProt IntAct interaction list (65 partners) is dominated by sticky/promiscuous Y2H preys (numerous KRTAPs, LCEs, keratins, homeodomain TFs such as OTX1, HOXA1, MEOX2, POU4F2) with NbExp=3, which are classic non-specific binders. None of these define a specific molecular function and none are independently corroborated as functional partners. Treated as **over-annotations** of bare protein binding.

## Disease / clinical relevance

- CHIC2 lies at 4q12. A **cryptic interstitial deletion at 4q12 fuses FIP1L1 to PDGFRA**, producing the constitutively active FIP1L1-PDGFRA tyrosine kinase that drives **hypereosinophilic syndrome / chronic eosinophilic leukemia**. **Deletion of CHIC2 is used clinically as a FISH marker (CHIC2 deletion)** for this fusion; CHIC2 loss is a positional marker and is **not established as causal** in the disease phenotype.
- A separate chromosomal translocation **t(4;12)(q12;p13) fuses CHIC2 (BTL) to ETV6** in a form of acute myeloid leukemia [PMID:10477709 (UniProt RN[1]); file:human/CHIC2/CHIC2-uniprot.txt DISEASE]. The functional consequence for CHIC2 itself is unclear.

## GO annotation assessment summary

- **Cellular component (localization):** Well supported as a membrane/vesicle-associated protein.
  - `plasma membrane` (GO:0005886) — IDA (HPA, GO_REF:0000052) and IBA: ACCEPT/supported; consistent with PMID:11257495 cell membrane localization.
  - `cytoplasmic vesicle` (GO:0031410) — IEA from UniProt SubCell (SL-0088): supported by PMID:11257495 "Cytoplasmic vesicle"; KEEP.
  - `Golgi-associated vesicle` (GO:0005798) — IBA + IEA(Ensembl ortholog): consistent with "Golgi-like vesicular compartment" note; reasonable but inferred, keep as non-core / accept localization.
  - `Golgi apparatus` (GO:0005794) — IEA(Ensembl ortholog, GO_REF:0000107): broader/less precise than the documented Golgi-like *vesicular* compartment; KEEP_AS_NON_CORE.
- **Molecular function:** All `protein binding` (GO:0005515) IPI from high-throughput interactome screens — uninformative bare protein binding → MARK_AS_OVER_ANNOTATED (per curation guidance to avoid bare protein binding).

## Tentative core function

Palmitoylated, membrane/vesicle-associated small protein localized to the plasma membrane and cytoplasmic/Golgi-associated vesicles; implicated in intracellular vesicle trafficking/secretion. Molecular mechanism undefined.
