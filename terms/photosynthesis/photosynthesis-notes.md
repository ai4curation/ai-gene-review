# Photosynthesis — concept notes

> Concept-level research notes for the AI gene review project. These are manually
> authored notes (the automated `term-deep-research` providers were not available in
> this environment — the run produced an empty placeholder report and was discarded).
> Provenance is recorded inline as `[PMID:xxxx "supporting text"]`. Identifiers are
> verified against the local GO term cache (`cache/go/terms.csv`), GOlr, UniProt, and
> PubMed; gene accessions that are not yet verified are explicitly marked.

## 1. Definition and scope

Photosynthesis is the light-driven conversion of inorganic carbon (CO2) into reduced
organic carbon, powered by light energy captured by chlorophyll and accessory pigments.
In oxygenic photosynthesis (cyanobacteria, algae, plants) the electrons used to reduce
CO2 are ultimately stripped from water, releasing O2 as a by-product. The process is
conventionally divided into two coupled stages:

1. **Light reactions** (thylakoid membrane): light energy drives electron transport from
   water to NADP+, generating NADPH and a transmembrane proton-motive force that powers
   ATP synthesis. Carried out by Photosystem II (PSII), the cytochrome b6f complex,
   Photosystem I (PSI), the mobile carriers plastoquinone / plastocyanin / ferredoxin,
   and the chloroplast/thylakoid ATP synthase.
2. **Carbon fixation** (stroma / cytoplasm): the Calvin–Benson–Bassham (CBB) reductive
   pentose-phosphate cycle uses the ATP and NADPH from the light reactions to fix CO2
   onto ribulose-1,5-bisphosphate via Rubisco, ultimately producing triose phosphates.

Anoxygenic photosynthesis (purple and green bacteria, heliobacteria) uses a single
reaction center and electron donors other than water (e.g. H2S, organics) and does not
evolve O2. The notes below focus on **oxygenic** photosynthesis, which dominates the
literature and the GO annotation base.

**Synonyms / related terms:** light reactions / dark reactions (the latter is dated —
the CBB cycle is light-*regulated*, not light-independent); photophosphorylation
(light-driven ATP synthesis); carbon assimilation; oxygenic vs anoxygenic photosynthesis.

## 2. How photosynthesis is represented in GO

GO splits photosynthesis across all three aspects. IDs below are verified against the
local term cache or GOlr.

**Biological process**
- `GO:0015979` photosynthesis (root of the BP branch)
- `GO:0019684` photosynthesis, light reaction
- `GO:0009765` photosynthesis, light harvesting
- `GO:0009767` photosynthetic electron transport chain
- `GO:0015977` carbon fixation
- `GO:0019253` reductive pentose-phosphate cycle (the CBB cycle)
- `GO:0009643` photosynthetic acclimation
- `GO:0048564` photosystem I assembly · `GO:0010206` photosystem II repair

**Molecular function**
- `GO:0016984` ribulose-bisphosphate carboxylase activity (Rubisco)
- `GO:0016168` chlorophyll binding

**Cellular component**
- `GO:0009522` photosystem I · `GO:0009523` photosystem II
- `GO:0009654` photosystem II oxygen evolving complex
- `GO:0034357` photosynthetic membrane
- `GO:0009535` chloroplast thylakoid membrane · `GO:0009534` chloroplast thylakoid ·
  `GO:0009543` chloroplast thylakoid lumen · `GO:0009579` thylakoid

**Curation watch-points (to revisit during gene review):**
- "Carbon fixation" (`GO:0015977`) is broad and spans several autotrophic pathways;
  CBB-cycle enzymes are better captured by `GO:0019253` (reductive pentose-phosphate cycle).
- Many electronic (IEA/IBA) annotations propagate generic terms like `GO:0009765`
  (light harvesting) or `GO:0016168` (chlorophyll binding) onto core reaction-center
  subunits whose primary role is charge separation/electron transport rather than antenna
  function. These are candidates for `MARK_AS_OVER_ANNOTATED` / `MODIFY` to a more specific term.
- Non-catalytic structural subunits frequently inherit catalytic MF terms from family-level
  rules — flag these the way the cellulosome project flagged scaffoldins.

## 3. Core components and genes

Gene/protein roles below are organism-agnostic at the family level; recommended model
organisms are listed per module in §4. Accessions are given only where verified in this
repository; otherwise they should be resolved with `just fetch-gene` when a review starts.

### A. Photosystem II — light-driven water oxidation
PSII is a water:plastoquinone oxidoreductase. The D1/D2 (PsbA/PsbD) heterodimer binds the
chlorophyll special pair P680 and the Mn4CaO5 oxygen-evolving cluster; CP47/CP43
(PsbB/PsbC) are the core chlorophyll antennae; the extrinsic PsbO/PsbP/PsbQ proteins
stabilize the oxygen-evolving complex. [PMID:21499260 "Crystal structure of oxygen-evolving
photosystem II at a resolution of 1.9 Å" — defines the D1/D2 reaction center, CP43/CP47
antenna, and the Mn4CaO5 water-oxidation cluster].

| Gene | Role | Notes |
|------|------|-------|
| psbA (D1) | PSII reaction-center, binds P680 / Mn4CaO5 | high turnover; PSII repair cycle |
| psbD (D2) | PSII reaction-center | partners D1 |
| psbB (CP47), psbC (CP43) | core chlorophyll antenna | feed excitation to P680 |
| psbO | oxygen-evolving complex extrinsic protein (OEC33) | stabilizes Mn4CaO5; `GO:0009654` |

### B. Photosystem I — plastocyanin:ferredoxin oxidoreductase
PSI completes the electron path, reducing ferredoxin (and thence NADP+). The PsaA/PsaB
heterodimer carries P700 and the early acceptors; PsaC binds the terminal FA/FB
iron-sulfur clusters. [PMID:11418848 "Three-dimensional structure of cyanobacterial
photosystem I at 2.5 A resolution" — 12 subunits and 127 cofactors incl. 96 chlorophylls
and 3 Fe4S4 clusters; basis for PSI light capture and electron transfer].

| Gene | Role | Notes |
|------|------|-------|
| psaA, psaB | PSI reaction-center, bind P700 | core heterodimer |
| **psaC** | PSI terminal Fe-S clusters (FA/FB) | **already seeded: CHLRE Q00914** |

### C. Electron-transport carriers and coupling
| Gene | Role |
|------|------|
| petA (cyt f), petB (cyt b6), petC (Rieske Fe-S) | cytochrome b6f complex; plastoquinol oxidation, Q-cycle, proton translocation |
| petE | plastocyanin — mobile Cu carrier, b6f → PSI |
| petF | ferredoxin — mobile Fe-S carrier downstream of PSI |
| petH (FNR) | ferredoxin–NADP+ reductase — makes NADPH |
| atpA, atpB | chloroplast ATP synthase (CF1) — uses proton-motive force to make ATP |

### D. Light harvesting and photoprotection
| Gene | Role |
|------|------|
| LHCB1 / LHCA family | chlorophyll a/b-binding antenna proteins (`GO:0016168`, `GO:0009765`) |
| PsbS | non-photochemical quenching (qE) photoprotection in plants |

### E. Carbon fixation — Calvin–Benson–Bassham cycle
Rubisco fixes CO2 onto ribulose-1,5-bisphosphate; it is famously inefficient and competes
with an oxygenase side-reaction, making it a focal point for crop-improvement research.
[PMID:18294858 "Structure and function of Rubisco" — "the major enzyme assimilating CO2
into the biosphere ... an extremely inefficient catalyst ... carboxylase activity is
compromised by an opposing oxygenase activity involving atmospheric O2"].

| Gene | Role | Notes |
|------|------|-------|
| rbcL | Rubisco large (catalytic) subunit | `GO:0016984`; chloroplast-encoded in plants |
| rbcS | Rubisco small subunit | nuclear-encoded in plants |
| rca | Rubisco activase | ATP-dependent removal of inhibitory sugar phosphates |
| prk (PRK) | phosphoribulokinase | regenerates RuBP; redox-regulated |
| gapA / gapB | chloroplastic glyceraldehyde-3-P dehydrogenase | redox-regulated CBB enzyme |
| **CP12** | redox switch; forms PRK–GAPDH–CP12 ternary complex that shuts the CBB cycle in the dark | **already seeded: CHLRE A6Q0K5** |

CP12 is a small, intrinsically disordered chloroplast protein and a node of redox
signalling on the CBB cycle. [PMID:33761918 "CP12 ... is an actor of the redox signaling
pathway involved in the regulation of the Calvin Benson Bassham (CBB) cycle ... regulating
phosphoribulokinase (PRK) and glyceraldehyde-3-phosphate dehydrogenase (GAPDH) through the
formation of a ternary complex"].

### F. Carbon-concentrating mechanism (algae / cyanobacteria)
| Gene | Role | Notes |
|------|------|-------|
| **LCI5** | low-CO2 inducible thylakoid-associated protein; CCM-associated | **already seeded: CHLRE Q94ET8** (UniProt: induced "under low CO2 growth conditions") |
| (carbonic anhydrases, LCIA/B, CCM1/CIA5) | inorganic-carbon uptake and concentration around Rubisco | candidates for follow-up |

### G. Pigment biosynthesis (supporting)
| Gene | Role |
|------|------|
| CHLH / CHLD / CHLI | magnesium chelatase — committed step of chlorophyll biosynthesis |
| POR | protochlorophyllide oxidoreductase — light-dependent chlorophyll synthesis |

## 4. Species coverage and recommended models (mixed-organism strategy)

The evidence base is dominated by a few deeply characterized systems; per the user's
"mix across organisms" choice, pick the best-characterized ortholog per module:

- **Cyanobacteria — *Synechocystis* sp. PCC 6803 (UniProt SYNY3) / *Thermosynechococcus***:
  cleanest genetics for the core light reactions, no chloroplast compartmentation; source
  of the landmark PSI [PMID:11418848] and PSII [PMID:21499260] structures. Best for
  psbA/D, psaA/B, petA/B/C, atpA/B.
- **Green alga — *Chlamydomonas reinhardtii* (CHLRE, NCBITaxon:3055)**: already seeded
  here (psaC, CP12, LCI5); excellent for CBB regulation and the carbon-concentrating
  mechanism.
- **Land plant — *Arabidopsis thaliana* (ARATH)**: best for photoprotection (PsbS),
  the LHC antenna family, and nuclear-encoded Rubisco small subunit / activase.
- **Reference structural orthologs** (spinach/tobacco Rubisco; *Thermosynechococcus* PSII)
  may be used where a specific module is best characterized outside the three models above.

## 5. Candidate genes for follow-up review

Already in the repository (link these into the review pass): `CHLRE/psaC` (Q00914),
`CHLRE/CP12` (A6Q0K5), `CHLRE/LCI5` (Q94ET8).

New candidates by priority (see `projects/PHOTOSYNTHESIS.md` for the tracked checklist):
PSII core (psbA/D1, psbD/D2, psbO), PSI core (psaA, psaB), electron transport (petA/B/C,
petE plastocyanin, petF ferredoxin, petH/FNR), ATP synthase (atpA/atpB), carbon fixation
(rbcL, rbcS, rca, PRK, gapA/gapB), light harvesting / photoprotection (LHCB1, PsbS), and
pigment biosynthesis (CHLH, POR) as supporting context.

## 6. Key literature (PubMed-verified)

According to PubMed:
- Umena Y, Kawakami K, Shen J-R, Kamiya N. *Crystal structure of oxygen-evolving
  photosystem II at a resolution of 1.9 Å.* Nature 473:55–60 (2011). PMID:21499260.
- Jordan P, Fromme P, Witt HT, Klukas O, Saenger W, Krauss N. *Three-dimensional structure
  of cyanobacterial photosystem I at 2.5 Å resolution.* Nature 411:909–917 (2001).
  PMID:11418848. [DOI](https://doi.org/10.1038/35082000)
- Andersson I, Backlund A. *Structure and function of Rubisco.* Plant Physiol Biochem
  46:275–291 (2008). PMID:18294858. [DOI](https://doi.org/10.1016/j.plaphy.2008.01.001)
- Shao H, et al. *A new type of flexible CP12 protein in the marine diatom Thalassiosira
  pseudonana.* Cell Commun Signal 19:38 (2021). PMID:33761918.
  [DOI](https://doi.org/10.1186/s12964-021-00718-x)

## Provenance / status log

- 2026-06-12: Concept folder created under `terms/photosynthesis/`. Automated
  `term-deep-research` (falcon provider) failed — the `concept_research.md.j2` template
  uses literal `{concept}` rather than a substituted variable, so the provider received an
  unfilled placeholder and returned a "concept not provided" non-report; that file was
  discarded rather than kept as a misleading `-deep-research-falcon.md`. (Template bug fixed
  2026-06-14: `{concept}` → Jinja `{{ concept }}`.) These manual notes
  were written instead, with GO IDs verified against `cache/go/terms.csv` + GOlr and the
  four key references verified via PubMed. Gene reviews deferred per the chosen scope
  ("just the concept writeup"); candidate genes tracked in `projects/PHOTOSYNTHESIS.md`.
