# TFP (TaTFP) — Thlaspi arvense thiocyanate-forming protein — review notes

UniProt: G1FNI6 · EC 4.8.1.8 · Taxon 13288 (*Thlaspi arvense*, field pennycress)
PDB: 5A10 (1.42 Å), 5A11 (2.47 Å)

## Identity / function
- TaTFP is a **specifier protein** of the glucosinolate–myrosinase ("mustard oil bomb")
  defense system. It does **not** hydrolyze intact glucosinolate; it captures the
  unstable aglucone produced by myrosinase and **redirects its rearrangement** away from
  the default isothiocyanate toward **organic thiocyanates, epithionitriles, and simple
  nitriles**. [PMID:21783213 "A thiocyanate-forming protein generates multiple products
  upon allylglucosinolate hydrolysis"]
- UniProt RecName: "N-(sulfonatooxy)prop-2-enimidothioate **sulfolyase**" (EC 4.8.1.8) —
  i.e. it is curated as a **lyase/catalyst**, not merely a regulator. Eisenschmidt-Bönn
  et al. 2019 reclassify specifier proteins as **Fe(2+)-dependent lyases** based on
  structure, cofactor dependence, and mutagenesis. [PMID:30900313 "Structural
  diversification during glucosinolate breakdown: mechanisms of thiocyanate,
  epithionitrile and simple nitrile formation"]

## Biochemistry
- Catalyzes allylthiocyanate + 3,4-epithiobutanenitrile formation from allylglucosinolate
  in the presence of myrosinase; also converts aliphatic glucosinolates to simple nitriles.
  [UniProt G1FNI6 CATALYTIC ACTIVITY; PMID:21783213; PMID:23999604; PMID:26260516; PMID:30900313]
- **Cofactor: Fe(2+)**; stimulated by Fe(2+), repressed by EDTA; pH optimum 5.5–6.
  [PMID:21783213; PMID:26260516; PMID:30900313]
- Iron-binding triad in the central β-propeller pore: **E266, D270, H274**; Y45 stabilizes
  the thiolate (Y45F abolishes activity). [PMID:30900313]

## Structure / quaternary state
- **Kelch repeat protein**, six-bladed **β-propeller** fold; **homodimer** (crystal
  structure). Lacks the mannose-binding lectin domain found in some family members.
  [PMID:26260516 "The crystal structure of the thiocyanate-forming protein from Thlaspi
  arvense, a kelch protein involved in glucosinolate breakdown"]

## Expression / localization
- Constitutively expressed in roots, stems, leaves, flowers, siliques, seedlings.
  [PMID:21783213]
- Direct subcellular localization of TaTFP not experimentally established; specifier
  proteins act in the cytosol where myrosinase-generated aglucones become available.
  Falcon deep research notes cytosolic organization but flags this as a gap.
  [file:THLAR/TFP/TFP-deep-research-falcon.md]

## Annotation review decisions (summary)
- GO:0005634 nucleus (IEA/TreeGrafter) → **REMOVE**: implausible compartment for a
  cytosolic glucosinolate-breakdown enzyme; over-propagated phylogenetic inference.
- GO:0005829 cytosol (IEA/TreeGrafter) → **ACCEPT**: plausible site of action.
- GO:0030234 enzyme regulator activity (IEA/TreeGrafter) → **MODIFY → GO:0016846
  carbon-sulfur lyase activity**: protein is a catalyst (EC 4.8.1.8 sulfolyase), not a
  regulator; the "specifier/regulator" framing is the outdated view.
- GO:0019760 glucosinolate metabolic process (IDA) → **MODIFY → GO:0019762 glucosinolate
  catabolic process**: TFP acts specifically in breakdown.
- GO:0019760 glucosinolate metabolic process (IEA/ARBA) → **ACCEPT** (general but correct).
- GO:0080028 nitrile biosynthetic process (IEA/TreeGrafter) → **ACCEPT**: forms
  nitriles/epithionitriles.
- GO:0042802 identical protein binding / GO:0042803 protein homodimerization activity
  (IDA) → **KEEP_AS_NON_CORE**: real (homodimer) but structural, not the catalytic core.

## DOE/BER relevance
Pennycress is a winter-annual oilseed cover crop / SAF feedstock. Glucosinolate breakdown
chemistry (TFP and related specifier proteins) governs seed-meal palatability and defense
volatiles — a target for engineering low-antinutrient feed co-products.


## Module-member evidence audit — 2026-10-25

Reviewed every original row (8) and core function using review/annotation-reviewer instructions, current cached primary publications and the existing research. Preserved all source annotation fields and all pre-existing proposed rows. Reused the existing genuine Falcon provider report and its artifacts. These plant targets do not require bacterial FEBA retrieval.

Direct pennycress proteinG1FNI6 has recombinant product evidence21783213, structure26260516, and mechanistic30900313 support. Replaced a title-only core quote with the actual allylthiocyanate/epithionitrile result. Other tested substrates yield simple nitriles; product output depends on aglucone structure and specifier type. A lack of strict addedFe2+ dependence in early assays is not absence of bound iron. Propagated nuclear localization remains unresolved; ESP interaction-specific nuclear recruitment is not a demonstrated TaTFP location.

Broad and substrate-specific terms were assessed consistently across evidence codes. No NEW rows were added. Previously proposed rows were evaluated for direct participation rather than filled from pathway adjacency. Experimental cohort calls whose protein-level data were not verified were left UNDECIDED; full-text availability alone was not treated as proof of a target-specific assay. Original sources and provider reports were not hand-edited.
