# CALCOCO1 (human) research notes

UniProt: Q9P1Z2 (CACO1_HUMAN). Gene: CALCOCO1 (HGNC:29306). 691 aa. Chromosome 12.
Aliases: Calphoglin; Coiled-coil coactivator protein (CoCoA); Sarcoma antigen NY-SAR-3; KIAA1536.

## Summary of two distinct narratives for CALCOCO1

CALCOCO1 has two largely separate bodies of literature:

1. **Selective-autophagy receptor (current "core" view).** CALCOCO1 is a soluble
   selective-autophagy receptor that functions in reticulophagy (ER-phagy) and Golgiphagy.
   It bridges ER/Golgi cargo to the ATG8 family (LC3/GABARAP) via LIR (LC3-interacting region)
   and UDS (UIM-docking site)-type motifs, and engages ER-phagy machinery (e.g. VAPA/VAPB on
   the ER membrane). This is the function emphasised in recent (post-2019) literature and is
   reflected in the UniProt IntAct interaction set, which lists direct interactions with
   GABARAPL1 (Q9H0R8) and GABARAPL2 (P60520) — the ATG8/LC3-GABARAP family.

2. **Transcriptional coactivator (historical "CoCoA" view).** Older work (2003-2014) characterised
   CALCOCO1 as "coiled-coil coactivator" (CoCoA), a secondary/bridging coactivator for nuclear
   receptors, the aryl hydrocarbon receptor, and the Wnt/beta-catenin (CTNNB1) and LEF1/TCF
   pathways, acting in the nucleus via p160 coactivators (GRIP1/NCOA2), p300/CBP, CARM1, and
   in association with CCAR1/MED1. A separate "calphoglin" report links it to inorganic
   pyrophosphatase (PPA1)/phosphoglucomutase (PGM) activation.

The GOA/UniProt annotation set assigned to this gene (the existing_annotations being reviewed)
is dominated entirely by the **transcription coactivator / CoCoA / beta-catenin** narrative plus
generic high-throughput protein-binding entries. The modern autophagy-receptor function is NOT
represented in the curated GO annotations and is therefore captured in description, core_functions,
and proposed_new_terms.

## Evidence from the UniProt record (file:human/CALCOCO1/CALCOCO1-uniprot.txt)

- Domain architecture: N-terminal SKICH domain (Pfam PF17751), CALCOCO1 domain (PF07888),
  three coiled-coil regions (145-205, 232-339, 417-514), a disordered region (514-606), and a
  C-terminal UBZ1-type zinc finger (653-679; Zn coordinated by C656, C659, H675, H679).
  [file:human/CALCOCO1/CALCOCO1-uniprot.txt "ZN_FING 653..679 /note=\"UBZ1-type\""]
- FUNCTION (coactivator): "Functions as a coactivator for aryl hydrocarbon and nuclear
  receptors (NR). Recruited to promoters through its contact with the N-terminal basic
  helix-loop-helix-Per-Arnt-Sim (PAS) domain of transcription factors or coactivators, such as
  NCOA2." [file:human/CALCOCO1/CALCOCO1-uniprot.txt "Functions as a coactivator for aryl hydrocarbon and nuclear"]
- FUNCTION (Wnt): "Involved in the transcriptional activation of target genes in the Wnt/CTNNB1
  pathway. Functions as a secondary coactivator in LEF1-mediated transcriptional activation via
  its interaction with CTNNB1."
  [file:human/CALCOCO1/CALCOCO1-uniprot.txt "Involved in the\nCC       transcriptional activation of target genes in the Wnt/CTNNB1"]
- FUNCTION (calphoglin): "Seems to enhance inorganic pyrophosphatase thus activating
  phosphogluomutase (PMG). Probably functions as a component of the calphoglin complex"
  [file:human/CALCOCO1/CALCOCO1-uniprot.txt "Seems to enhance inorganic pyrophosphatase thus activating"]
- SUBCELLULAR LOCATION: "Cytoplasm. Nucleus. Note=Shuttles between nucleus and cytoplasm."
  [file:human/CALCOCO1/CALCOCO1-uniprot.txt "Shuttles between nucleus"]
- IntAct partners include the ATG8 family: GABARAPL1 (Q9H0R8) and GABARAPL2 (P60520),
  consistent with an autophagy-receptor / ATG8-binding function.
  [file:human/CALCOCO1/CALCOCO1-uniprot.txt "Q9H0R8: GABARAPL1"]
- Keywords: Activator, Wnt signaling pathway, Zinc, Zinc-finger, Transcription, Nucleus, Cytoplasm.

Note: the UniProt FUNCTION text for the coactivator role is heavily "By similarity"
(ECO:0000250 from mouse ortholog Q8CGU1); only the GATA1/CCAR1 erythroid result is human
experimental (ECO:0000269|PubMed:24245781).

## Evidence from cached publications

### PMID:16344550 (Yang, Kim, Li, Stallcup 2006, J Biol Chem) — CoCoA / beta-catenin
- "another component of the p160 nuclear receptor coactivator complex, the coiled-coil
  coactivator (CoCoA), directly binds to and cooperates synergistically with beta-catenin as a
  coactivator for AR and TCF/LEF."
  [PMID:16344550 "directly binds to and cooperates \nsynergistically with \nbeta-catenin as a coactivator for AR and TCF/LEF"]
- "CoCoA associated specifically with the promoters of transiently transfected and endogenous
  target genes of TCF/LEF, and reduction of the endogenous CoCoA level decreased the ability of
  TCF/LEF and beta-catenin to activate transcription"
  [PMID:16344550 "CoCoA associated specifically with the promoters"]
- Supports: beta-catenin binding (GO:0008013), transcription coregulator/coactivator activity,
  sequence-specific DNA binding (promoter association via ChIP), positive regulation of
  transcription. These are real but are the historical/secondary nuclear function.

### PMID:24245781 (Mizuta et al. 2014, Genes Cells) — CCAR1/CoCoA + GATA1/MED1
- "Recombinant GATA1, CCAR1, CoCoA and MED1(1-602) formed a complex in vitro, and GATA1, CCAR1,
  CoCoA and MED1 were recruited to the gamma-globin promoter in K562 cells during erythroid
  differentiation."
  [PMID:24245781 "Recombinant GATA1, CCAR1, CoCoA and MED1(1-602) formed a"]
- "CoCoA AD2 may interact with GATA1, CoCoA AD1 interacts with CCAR1 ... and that the GATA1 CF
  domain serves as a docking surface for multiple coactivators, including CoCoA, CCAR1, and MED1."
  [PMID:24245781 "the GATA1 CF domain serves as a docking surface for multiple coactivators, including CoCoA, CCAR1, and MED1"]
- "GATA1, MED1, CCAR1, and CoCoA were all recruited onto the gamma-globin promoter at the
  GATA1-binding sites after 2 and 3 days during erythroid differentiation"
  [PMID:24245781 "GATA1, MED1, CCAR1, and CoCoA were all recruited onto the"]
- This is the strongest *human experimental* support for the coactivator role; supports
  transcription coactivator activity (IMP) and promoter/cis-regulatory DNA binding (IDA via ChIP).

### High-throughput interactome papers (all generic "protein binding", GO:0005515)
- PMID:16189514 (Rual et al., proteome-scale Y2H map) — WITH NDC80 (O14777).
- PMID:25416956 (Rolland et al., human interactome) — many partners (GABARAPL2 P60520, etc.).
- PMID:32296183 (Luck et al., HuRI binary interactome) — includes GABARAPL1 (Q9H0R8),
  GABARAPL2 (P60520).
- PMID:33961781 (Huttlin et al., BioPlex) — NDC80, BFSP2.
- PMID:40205054 (Schaffer et al. 2025, multimodal cell maps) — NDC80, BFSP2.
These are uninformative as "protein binding" per curation guidelines. They do, however,
collectively corroborate the ATG8/GABARAP interactions underlying the autophagy-receptor role.

## Falcon deep research findings (2026-06-07)

The Falcon report (Edison) adds primary-literature support for several claims that the
existing review previously sourced only from UniProt/notes, plus some new disease/biomarker
links. Distinguishing CONFIRMS / NEW / PROVISIONAL:

- **CONFIRMS + key NEW primary reference for the core function.** The foundational ER-phagy
  paper Stefely et al. 2020 (Autophagy) [PMID:31971854 "we show that CALCOCO1 physically
  interacts with MAP1LC3C ... Genetic deletion ... disrupted autophagy of the endoplasmic
  reticulum (reticulophagy)"] was MISSING from the existing `references:` even though the
  review's whole "core" autophagy-receptor narrative rests on it. It provides the direct
  experimental basis: a canonical LIR (W47A abolishes LC3-family binding), a non-canonical
  CLIR (L140A/V142A weakens MAP1LC3C binding) explaining MAP1LC3C preference, MTOR-regulated
  turnover (MLN0128 lowers, chloroquine/bafilomycin raise CALCOCO1), and ER-phagy reporter
  flux reduced ~50% (GST-LSCS-GFP-cb5) / ~25% (Keima-cb5) in knockouts. NOTE: this is a
  *mouse/MEF + human cell* study; the genetic ER-phagy data are largely in mouse cells.
  Now added to the review as a statement-only reference.
- **NEW primary reference for the historical coactivator (non-core) role.** Kim et al. 2008
  (Mol Cell) [PMID:18722177 "CCAR1, a key regulator of mediator complex recruitment to nuclear
  receptor transcription complexes"] is the original CCAR1/CoCoA paper underpinning the
  CCAR1-CoCoA-Mediator axis already described; previously only Mizuta 2014 (PMID:24245781) was
  cited. Added as statement-only reference.
- **NEW: direct experimental test of CALCOCO1 as a glucocorticoid-receptor coregulator.**
  Wu et al. 2014 (Nucl Recept Signal) [PMID:25422592 "siRNA mediated depletion ... CCAR1,
  CCAR2, CALCOCO1 and ZNF282 ... each coregulator acted in a selective and gene-specific
  manner"] shows CALCOCO1 is a *gene-selective* GR coregulator with both positive and negative
  effects - i.e. not a global coactivator. Reinforces the KEEP_AS_NON_CORE coactivator calls
  and the steroid-hormone-signaling annotations. Added as statement-only reference.
- **NEW / nuancing the Golgiphagy proposed term.** Kitta et al. 2024 (EMBO J) [PMID:38822137
  "YIPF3 and YIPF4 ... constitute a Golgiphagy receptor"] tested CALCOCO1 in a HeLa Golgiphagy
  reporter: CALCOCO1 knockdown alone did NOT decrease Golgiphagy, and triple YIPF3/YIPF4/CALCOCO1
  knockdown retained activity - arguing CALCOCO1 is not the dominant Golgi receptor in that
  context (redundancy / context-specific). This tempers the "Golgiphagy receptor activity"
  proposed term: keep proposed but flag redundancy. Commentary Ma & Zhang 2024 (Life Metab)
  [PMID:39871880] frames CALCOCO1 as a soluble ER-phagy receptor with a minor Golgi pool
  (possibly via ZDHHC17), distinct from the YIPF3/4 mechanism. Both added as statement-only refs.
- **PROVISIONAL / low-confidence disease links (NOT used to change annotations).**
  (i) A tumor-associated **R12H** variant reduced MAP1LC3C association (Stefely 2020) - a
  mechanistic, not disease-causal, observation. (ii) Meng et al. 2024 AD multi-omics
  (DOI:10.1186/s13195-024-01578-6) reportedly lists CALCOCO1 among downregulated plasma proteins
  in high-severity AD, but the abstract's top features are SKAP1/NEFL and CALCOCO1 is not named
  there - treat as weak, association-only. (iii) Wei et al. 2023 (DOI:10.1186/s41065-023-00289-6)
  is actually an **NPM3/LUAD** paper; CALCOCO1 appears only peripherally, so it is NOT a
  CALCOCO1-focused reference and is intentionally kept out of the YAML.
- **No change to existing annotation actions.** Falcon confirms the existing two-narrative
  framing (cytoplasmic ER-phagy/Golgiphagy receptor = core; nuclear CoCoA coactivator =
  non-core; generic protein binding = over-annotated). It adds primary citations and one
  redundancy caveat (Golgiphagy) but does not contradict any existing action.

## Conclusion on core vs non-core

- **Core (current understanding, not in GOA):** selective-autophagy receptor / cargo receptor
  bridging ER and Golgi membranes to ATG8 (LC3/GABARAP) family for reticulophagy and Golgiphagy;
  ATG8-family protein binding (LIR/UIM-type). Cytoplasmic.
- **Non-core (historical, well-cited):** transcriptional coactivator (CoCoA) for nuclear
  receptors / AhR / Wnt-beta-catenin/LEF1 / GATA1; nuclear localization and promoter association.
  Real but secondary/context-dependent and largely "by similarity" at the human level.
- **Over-annotated / uninformative:** generic "protein binding" (GO:0005515) from interactome
  screens; broad "signal transduction"; the calphoglin/PPA1-PGM activity (single old report).
