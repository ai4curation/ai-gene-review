# HAL (Histidine ammonia-lyase / histidase) — review notes

UniProt: P42357 (HUTH_HUMAN); gene HAL (syn. HIS); HGNC:4806; GeneID 3034;
chromosome 12q. 657 aa. EC 4.3.1.3. Evidence at protein level (PE 1).

## Core biology

- **Molecular function.** Histidine ammonia-lyase (histidase): catalyzes the
  non-oxidative deamination of L-histidine to trans-urocanate + ammonia.
  [file:human/HAL/HAL-uniprot.txt "RecName: Full=Histidine ammonia-lyase;"]
  [file:human/HAL/HAL-uniprot.txt "Reaction=L-histidine = trans-urocanate + NH4(+); Xref=Rhea:RHEA:21232,"]
  Core MF term = **GO:0004397 histidine ammonia-lyase activity** (label verified
  current in local go.db; MF branch confirmed via entailed ancestors).

- **Catalytic mechanism.** Uses an autocatalytically formed MIO
  (4-methylideneimidazol-5-one) prosthetic group, made by cyclization/dehydration
  of an internal Ala-Ser-Gly tripeptide (crosslink FT 253..255; MOD_RES 254
  2,3-didehydroalanine).
  [file:human/HAL/HAL-uniprot.txt "Contains an active site 4-methylidene-imidazol-5-one (MIO), which"]

- **Pathway / BP.** First step (step 1/3) of L-histidine degradation to
  L-glutamate.
  [file:human/HAL/HAL-uniprot.txt "glutamate; N-formimidoyl-L-glutamate from L-histidine: step 1/3."]
  Core BP term = **GO:0006548 L-histidine catabolic process** (current; BP branch
  confirmed). Note: UniProt DR lines also carry GO:0019556 / GO:0019557
  ("...to glutamate and formamide/formate"), but both are now **obsolete** in
  go.db and are NOT in the GOA-seeded existing_annotations, so not used.

- **Location.** Soluble cytosolic enzyme (homotetramer). Reactome localizes to
  cytosol. Core CC = **GO:0005829 cytosol** (CC branch confirmed); the InterPro
  IEA "cytoplasm" (GO:0005737) is the less-specific parent.
  [Reactome:R-HSA-70899 "Cytosolic histidine ammonia lyase (HAL) catalyzes the reaction of histidine to form urocanate and NH4+"]

- **Expression.** Group-enriched in liver and skin.
  [file:human/HAL/HAL-uniprot.txt "Group enriched (liver, skin)"] Epidermal
  urocanate (the product) is a major UV chromophore of the stratum corneum
  (background biology, not separately quoted).

- **Family.** PAL/histidase (aromatic amino acid ammonia-lyase) family; shares
  the MIO mechanism with phenylalanine ammonia-lyase.
  [file:human/HAL/HAL-uniprot.txt "Belongs to the PAL/histidase family."]

- **Disease.** Histidinemia (HISTID; MIM 235800), autosomal recessive, caused by
  HAL loss of function; elevated histidine, decreased urocanate.
  [file:human/HAL/HAL-uniprot.txt "Histidinemia (HISTID) [MIM:235800]: Autosomal recessive"]
  [PMID:15806399 "and decreased urocanic acid in blood and skin and results from histidase"]
  Four disease missense mutations (R322P, P259L, R206T, R208L) in the human HAL
  gene were the first coding-region mutations reported.
  [PMID:15806399 "report describes the first mutations occurring in the coding region of the"]

## Annotation review summary

Actions (13 existing annotations):
- ACCEPT (7): GO:0004397 IBA, GO:0004397 IEA, GO:0004397 EXP (core MF);
  GO:0006548 IBA, GO:0006548 IEA, GO:0006548 TAS (core BP); GO:0005829 cytosol TAS
  (core CC).
- MARK_AS_OVER_ANNOTATED (3): GO:0003824 catalytic activity IEA (root),
  GO:0016841 ammonia-lyase activity IEA (parent of specific MF), GO:0031670
  cellular response to nutrient IEA (ortholog-transferred, vague/non-core).
- REMOVE (2): GO:0005515 protein binding IPI x2 (RPS19BP1/Q86WX3
  high-throughput) — see below.
- MODIFY (1): GO:0005737 cytoplasm IEA -> GO:0005829 cytosol (more specific;
  matches Reactome CC).

Note per curation policy (revised 2026-10-09): the two GO:0005515 "protein
binding" IPI rows are now REMOVE, not MARK_AS_OVER_ANNOTATED. The
generic-protein-binding policy excludes MARK_AS_OVER_ANNOTATED for GO:0005515 by
name — the defect is absence of functional information, not a claim exceeding the
evidence — and `just validate` warns on it. Removal does not assert the
interaction is false. The single interactor in both screens is RPS19BP1 (Q86WX3),
matching the UniProt INTERACTION line (NbExp=2). No established biological role
for a HAL-RPS19BP1 interaction, hence no MODIFY replacement term.

## Reference notes

- PMID:15806399 — histidinemia mutation study; abstract-only cache
  (full_text_available: false). PubMed-verified. Supports core MF + disease link
  (genetic evidence, not a direct in vitro kinetic assay).
- PMID:33961781 (BioPlex 3.0) and PMID:40205054 (multimodal U2OS cell map) —
  proteome-scale interactome screens; source of the two "protein binding" IPI
  annotations to RPS19BP1. The literal "HAL" occurrences in PMID:40205054 full
  text are the "HALT protease inhibitor" reagent, not the gene.
- Reactome R-HSA-70899 (reaction) and R-HSA-70921 (pathway) — cached; titles left
  exactly as fetched.

## 2026-10-09 — weekly compliance pass

Evidence-aware compliance (`just compliance-all`) had HAL at 45.88 weighted. The
gaps were almost entirely missing justification/provenance scaffolding rather
than wrong biology, so this pass added it without changing any accepted call
except the two generic protein-binding rows:

- **`review.reason` added to all 13 annotations.** Each reason now states *why*
  the action was chosen, not just what the annotation says. For the IEA rows the
  reason names the specific InterPro signature that fired (IPR008948 →
  GO:0003824; IPR022313 → GO:0016841; IPR005921 → GO:0005737), which is what makes
  them subsumed-but-true rather than wrong.
- **GO:0005515 ×2 migrated `MARK_AS_OVER_ANNOTATED` → `REMOVE`.** `just validate`
  warned on both: the generic-protein-binding policy excludes
  MARK_AS_OVER_ANNOTATED for GO:0005515 by name (the defect is absence of
  functional information, not a claim exceeding evidence). MODIFY was not
  available — neither screen assigns a function to the HAL–RPS19BP1 association,
  so there is no evidence-backed replacement MF. Reasons state explicitly that
  removal does not assert the interaction is false.
- **`inference_support` for the four propagated rows.** GO:0031670 now carries a
  `propagation_review` (`root_cause: TERM_SCOPING_PROBLEM`,
  `failure_modes: [ROLE_CONFLATION]`) naming the real source,
  **UniProtKB:P21213** (rat Hal, `ensembl:ENSRNOP00000006971`, from the GOA
  WITH/FROM column). The orthology is correct; the term is not — dietary
  modulation of hepatic histidase abundance makes HAL the *output* of a nutrient
  response, not a participant in one.
- **`findings` added to all 8 bare references**, with verbatim `supporting_text`
  for the two interactome papers and both Reactome entries.
  [PMID:33961781 "Through affinity-purification mass spectrometry, we have created two proteome-scale, cell-line-specific interaction networks."]
  [PMID:40205054 "Here we construct a global map of human subcellular architecture through joint measurement of biophysical interactions and immunofluorescence images for over 5,100 proteins in U2OS osteosarcoma cells."]
  GO_REF findings are statement-only: GO_REF documents are not cached, so any
  quote would be unverifiable by the quote validator. Left deliberately empty
  rather than filled with an unprovenanced string.
- **`alternative_products` descriptions.** Isoform 2 (VSP_044704) replaces
  residues 589–657 with 'FGK'; isoform 3 (VSP_046003) lacks 1–208, the whole
  region N-terminal to the MIO-forming Ala-Ser-Gly tripeptide (CROSSLNK 253..255).
  Both are cDNA-derived (PubMed:14702039) with no measured activity, so neither
  carries an annotation.
- **4 `suggested_questions` and 3 `suggested_experiments` added** (previously
  absent). All are genuine wet-lab gaps: are T637/S648 (by-similarity phospho
  sites) real in human tissue; are the hepatic and epidermal enzyme pools
  regulated separately; are isoforms 2/3 inert or dominant-negative; and is the
  RPS19BP1 interaction reproducible by low-throughput methods.

Result: 45.88 → **94.78** weighted, `just validate` clean (the two policy
warnings are gone). Two gap classes remain and are intentional: the four GO_REF
`findings[].supporting_text` slots (nothing citable to quote) and
`existing_annotations[12].review.literature_support` — the cytosol row is a
Reactome TAS, and no primary paper in this review measures HAL's subcellular
fractionation, so there is no PMID quote to attach. Padding either would mean
inventing provenance.
