# P4HA2 (Prolyl 4-hydroxylase subunit alpha-2) — review notes

UniProt: O15460 (P4HA2_HUMAN), 535 aa precursor (signal 1-21), HGNC:8547, gene on chr5.
EC 1.14.11.2. MANE-select isoform IIa (O15460-2); displayed isoform IIb (O15460-1).

## Core function

P4HA2 is one of three catalytic alpha-subunit isoforms (P4HA1/2/3) of collagen prolyl
4-hydroxylase. The active enzyme is an **alpha2-beta2 heterotetramer** in which the beta
subunit is P4HB (protein disulfide isomerase, PDI), which acts as a structural/retention
subunit. The enzyme resides in the **ER lumen** and catalyzes formation of trans-4-
hydroxy-L-proline at the Y position of -Xaa-Pro-Gly- repeats in procollagen; 4-Hyp is
essential for folding and thermal stability of the collagen triple helix.

[PMID:9211872 "Prolyl 4-hydroxylase (proline hydroxylase, EC 1.14.11.2) catalyzes the formation of 4-hydroxyproline in collagens. The vertebrate enzyme is an alpha2beta2 tetramer, the beta subunit of which is identical to protein disulfide-isomerase (PDI, EC 5.3.4.1)."]

[PMID:9211872 "the presence of the corresponding polypeptide and the (alpha(II))2beta2 tetramer was demonstrated in cultured human WI-38 and HT-1080 cells. The type II tetramer was found to represent about 30% of the total prolyl 4-hydroxylase in these cells"]

The alpha(I) and alpha(II) subunits do **not** form mixed alpha(I)alpha(II)beta2 tetramers
[PMID:9211872 "The results of coexpression in insect cells argued strongly against the formation of a mixed alpha(I)alpha(II)beta2 tetramer."]. Type II enzyme is kinetically very similar to type I, differing mainly in Ki for poly(L-proline)
[PMID:9211872 "The properties of the purified human type II enzyme were very similar to those of the type I enzyme, but the Ki of the former for poly(L-proline) was about 200-1000 times that of the latter."].

## Catalysis / cofactors (UniProt O15460)

- Catalytic reaction: L-prolyl-[collagen] + 2-oxoglutarate + O2 = trans-4-hydroxy-L-prolyl-[collagen] + succinate + CO2 (RHEA:18945; EC 1.14.11.2). It is a 2-oxoglutarate/Fe(II)-dependent dioxygenase.
- COFACTOR Fe(2+): "Binds 1 Fe(2+) ion per subunit." Fe-binding residues 430, 432, 501; 2-oxoglutarate binding residue 511; Fe2OG dioxygenase domain 412-520.
- COFACTOR L-ascorbate (vitamin C; required to re-reduce Fe after uncoupled cycles).
- KM = 22 uM for 2-oxoglutarate [PMID:9211872].
- Domains: N-terminal P4Ha_N (peptide-substrate binding), TPR repeats (~207-240; involved in tetramer assembly / substrate binding), C-terminal Fe2OG catalytic domain.

## Localization

UniProt: SUBCELLULAR LOCATION = Endoplasmic reticulum lumen. HPA IDA = endoplasmic reticulum
(GO:0005783). Reactome places it in ER lumen (collagen biosynthesis). All consistent.

## Subunit / interactions

- P4HB (P07237): bona fide beta subunit of the active tetramer — biologically meaningful interaction (the alpha2beta2 enzyme). [PMID:9211872]
- P4HA1 (P13674): the alpha(I) catalytic isoform; co-purification/IntAct capture. Note alpha(I) and alpha(II) do NOT co-assemble into mixed tetramers, so this is not a functional heterotetramer.
- KIF7 (Q2M1P5): kinesin; captured in high-throughput interactome screens, not an obvious ER-lumenal partner.
- The 4 IPI "protein binding" GOA annotations come from large-scale proteomics/interactome
  screens (PMID:30021884 histone XL-MS; PMID:33961781 BioPlex; PMID:35271311 OpenCell;
  PMID:40205054 multimodal cell maps) and are bare GO:0005515 — uninformative for MF.

## Disease

Autosomal-dominant nonsyndromic **high myopia (MYP25, MIM:617238)**; variants Q140R, I150V,
E291K (E291K decreases protein abundance) [UniProt DISEASE; PMID:25741866 (not in cited set)].
Connective-tissue/collagen role in scleral ECM is the likely mechanistic link.

## Annotation review summary

- procollagen-proline 4-dioxygenase activity (GO:0004656): ACCEPT, core MF (IDA PMID:9211872,
  plus IBA/IEA/TAS duplicates).
- procollagen-proline 4-dioxygenase complex (GO:0016222): ACCEPT, core CC (alpha2beta2 with P4HB).
- iron ion binding (GO:0005506), L-ascorbic acid binding (GO:0031418),
  oxidoreductase ... molecular oxygen (GO:0016705): ACCEPT — cofactor/MF, all directly
  supported by UniProt cofactor + catalytic-residue annotations.
- ER (GO:0005783), ER lumen (GO:0005788): ACCEPT.
- electron transfer activity (GO:0009055), TAS PMID:9211872: this is a misleading MF for a
  2-OG dioxygenase. The enzyme does not function as an electron carrier; "electron transfer"
  here is an over-interpretation of the redox chemistry. MARK_AS_OVER_ANNOTATED.
- protein binding (GO:0005515) x4 IPI: KEEP_AS_NON_CORE (bare term; P4HB interaction is real
  and meaningful but captured only as uninformative protein binding here).

## Falcon deep-research findings (incorporated 2026-06)

- The two non-canonical (non-collagen) substrate mechanisms are already captured in the review:
  P4HA2 binds mTOR and hydroxylates conserved Pro2341 to activate mTOR kinase (PMID:38654109, Jin
  2024, Oncogene; DOI 10.1038/s41388-024-03032-1), and P4HA2 hydroxylates SUFU at the ciliary tip in
  complex with KIF7 to amplify Hedgehog signaling (PMID:38909089, Li 2024, Leukemia;
  DOI 10.1038/s41375-024-02313-8). Falcon corroborates both; PMIDs re-verified against PubMed.
- NEW: SP1 transcriptionally activates P4HA2 in colorectal cancer — SP1 binds the P4HA2 promoter (ChIP
  + luciferase), and P4HA2 drives proliferation/EMT with AGO1 as a probable downstream target.
  [PMID:38857058 "the transcription factor SP1 binds to the promoter sequence of P4HA2, activating its expression in CRC"]
- NEW (review): Hironaka & Xiong 2025 (PMID:41096640) provides an up-to-date C-P4H review covering the
  alpha2-beta2/PDI tetramer, ER localization, Fe(II)/2-OG/O2/ascorbate chemistry, and both canonical
  collagen-deposition and non-canonical (stemness, hypoxia, glucose metabolism, angiogenesis, TIL
  modulation) cancer roles. [PMID:41096640 "not only in the canonical collagen deposition role, but also in non-canonical functions, such as cell stemness, hypoxic response, glucose metabolism, angiogenesis"]
- Falcon reiterates the isoform substrate-bias concept: P4HA1 vs P4HA2 differ in sequence preference
  across X-Pro-Gly triplets (isoenzyme-biased substrate selection rather than strict collagen-type
  specificity), consistent with the existing review's suggested_questions on isoenzyme substrate
  preference. (Review-level claim; not added as a primary reference.)
- Several additional 2024 P4HA2 cancer papers (HNSCC PI3K/AKT — DOI 10.1007/s12032-024-02358-w; OSCC
  PI3K/AKT — DOI 10.1038/s41598-024-64264-5; pan-P4H HNC biomarker — DOI 10.1038/s41598-024-62678-9;
  osteosarcoma biomarker — DOI 10.1016/j.heliyon.2024.e27191) are correlative TCGA/cell-line biomarker
  studies. They reinforce the (non-core) "overexpressed/poor-prognosis in solid tumors via PI3K/AKT or
  EMT" theme but add little mechanistic novelty beyond Dang/Jin/Li; not added as primary references.
- Salo & Myllyharju 2021 (already in review as PMID:32969070) is reiterated by Falcon for the field
  status that no collagen-hydroxylase inhibitor is yet in clinical use, in contrast to HIF-PHD inhibitors.
