# CHIC2 (Cysteine-rich hydrophobic domain-containing protein 2) — Review Notes

UniProt: Q9UKJ5 (CHIC2_HUMAN); Gene: CHIC2; Synonym: BTL ("BrX-like translocated in leukemia"); 165 aa; HGNC:1935; locus 4q12.

## Core biology

- CHIC2 is a small (165 aa, ~19 kDa) protein and the founding/defining member of the CHIC family, characterized by a single **cysteine-rich hydrophobic (CHIC) motif** (residues 88–106) [file:human/CHIC2/CHIC2-uniprot.txt MOTIF 88..106].
- It is **palmitoylated** within the CHIC motif, and palmitoylation is **required for membrane association** [PMID:11257495 "Palmitoylation in the CHIC motif is required for membrane association"]. Mutagenesis of the cysteine cluster (88-CGCLCCCC-95 → SGSLSSSS) causes **loss of palmitoylation and abolishes membrane association** [file:human/CHIC2/CHIC2-uniprot.txt MUTAGEN 88..95].
- Subcellular location (experimental, IDA): **cell membrane / plasma membrane** and **cytoplasmic vesicle**; also present at a **Golgi-like vesicular compartment and at scattered vesicles** [PMID:11257495; file:human/CHIC2/CHIC2-uniprot.txt SUBCELLULAR LOCATION].
- The N-terminus (1–26) is predicted coiled-coil (acidic, EEEDEE-rich) [file:human/CHIC2/CHIC2-uniprot.txt COILED 1..26].
- Pfam: Erf4 (PF10256); InterPro: CHIC1/2 (IPR039735), Golgin_A_7/ERF4 (IPR019383); PANTHER PTHR13005. The Erf4/Golgin-A7 relationship suggests possible roles in vesicle/Golgi-associated trafficking and protein palmitoylation/processing; direct biochemical work now supports a non-catalytic STUB1-adapter role for CHIC2 in a membrane-associated ubiquitin ligase complex.

## Molecular function — STUB1 adapter plus high-throughput binding

- CHIC2 has no demonstrated enzymatic activity, but LaFleur et al. 2025 establish it as a **non-catalytic adapter for STUB1/CHIP** in a membrane-associated ubiquitin ligase complex that regulates cytokine receptor expression in mouse and human CD8+ T cells [PMID:40796662 "Mechanistically, STUB1 interacts with the adapter protein CHIC2 to regulate cytokine receptor expression in mouse and human CD8+ T cells"].
- CHIC2 binds STUB1 through its C-terminal **IFRPD** motif; wild-type CHIC2 co-immunoprecipitates STUB1 whereas the CHIC2 ΔIFRPD mutant does not, and loss of either STUB1 or CHIC2 increases IFNγR1 and IL-27Rα receptor abundance in T cells [PMID:40796662 "CHIC2 could co-precipitate STUB1 but CHIC2 ΔIFRPD could not"; "STUB1 KO and CHIC2 KO CD8+ T cells had significantly increased expression of IFNγR1 and IL-27Rα"].
- The adapter model remains sharper than "protein binding": a CHIC2 palmitoylation-site mutant fails to rescue cytokine receptor regulation, and CHIC2 does not detectably co-precipitate IFNγR1 or IL-27Rα, suggesting that membrane-localized CHIC2 brings STUB1 into proximity with receptors rather than serving as a catalytic E3 or a simple receptor-binding subunit [PMID:40796662 "suggesting that CHIC2 may function by bringing STUB1 into proximity with IL-27Rα and IFNγR1 rather than directly binding to these cytokine receptors"].
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
- **STUB1 ubiquitin ligase complex:** The PMID:40796662 full text supports a new `part_of` `ubiquitin ligase complex` (GO:0000151) annotation for CHIC2 as the non-catalytic adapter in a STUB1-CHIC2 complex. The generic complex-membership term is conservative; the paper supports CHIC2 binding to the E3 ligase STUB1 and regulating cytokine receptor abundance, not CHIC2 having its own E3 catalytic activity.

## Tentative core function

Palmitoylated, membrane/vesicle-associated small protein localized to the plasma membrane and cytoplasmic/Golgi-associated vesicles. In CD8+ T cells, it functions as a membrane adapter in a STUB1 ubiquitin ligase complex that post-translationally limits cytokine receptor abundance.

## 2026-09-27 PROTEOSTASIS follow-up

- Fetched and read the full PMC text for PMID:40796662, the 2025 STUB1-CHIC2 CD8+ T-cell paper flagged by the PROTEOSTASIS phase-1 audit.
- The evidence supports adding **NEW `GO:0030674 protein-macromolecule adaptor activity`** and
  **`part_of GO:0000151 ubiquitin ligase complex`** annotations for CHIC2. The complex annotation
  should use IPI evidence because it is based on STUB1-CHIC2 co-IP, and the assertion should stay at
  adaptor/complex-membership level because CHIC2 is the adapter while STUB1 carries the U-box E3
  catalytic activity.
- Updated the review description, references, core functions, and suggested questions/experiments to remove the stale "molecular function unknown" framing and capture the IFRPD-dependent STUB1-adapter role.
