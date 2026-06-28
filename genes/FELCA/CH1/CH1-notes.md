# Fel d 1 chain 1 (CH1, UniProt P30438) — curation notes

Curation triggered by the review article PMC5891966 / PMID:29643919
(Bonnet et al. 2018, *Allergy Asthma Clin Immunol*, "An update on molecular cat
allergens: Fel d 1 and what else? Chapter 1: Fel d 1, the major cat allergen").

## Identity
- UniProt P30438, `FEL1A_FELCA`, gene name `CH1` (chain 1 / α-chain).
- 92 aa precursor; signal 1–22, mature chain 23–92 (~70 aa, ~8 kDa).
- The complete Fel d 1 allergen is a ~35–38 kDa heterotetramer: two heterodimers,
  each a chain 1 (CH1, this gene, P30438) + chain 2 (CH2, P30440) pair, the two
  chains covalently linked by three interchain disulfide bonds; encoded by two
  separate genes [PMID:29643919 "Each dimer consists of two polypeptide chains, chain 1 and chain 2, covalently linked by three disulfide bridges and encoded by two different genes"].

## Family / fold
- Member of the **secretoglobin** (uteroglobin) family; all-α fold of eight
  helices [PMID:29643919 "Fel d 1 belongs to the family of secretoglobins or secretory globins"].
- Crystal structure shows striking similarity to uteroglobin (a steroid-inducible,
  cytokine-like, anti-inflammatory/immunomodulatory molecule)
  [PMID:12851385 "The structure of the Fel d 1 presents a striking similarity to that of uteroglobin, a steroid-inducible cytokine-like molecule with anti-inflammatory and immunomodulatory properties"].

## Molecular function (what is actually known vs inferred)
- **Calcium ion binding — experimentally supported.** The tetramer crystal
  structure reveals two distinct Ca2+-binding sites; UniProt records three Ca2+
  binding residues (68, 71, 74)
  [PMID:17543334 "the crystal structure of tetrameric Fel d 1 reveals two different calcium-binding sites"].
- **Steroid/ligand binding — NOT demonstrated, only a structural possibility.**
  The structures show an internal asymmetric cavity that *could* accommodate an
  amphipathic endogenous ligand; no steroid (or other ligand) has been shown to
  bind [PMID:12851385 "An internal, asymmetric cavity is formed in the Fel d 1 that could bind an endogenous ligand"].
  The IBA/IEA "steroid binding" GO annotation is a family-level (uteroglobin)
  inference, not evidence for this protein → treated as over-annotation.
- **Phospholipase A2 modulation — speculation.** By analogy to uteroglobin, Fel d 1
  is *speculated* to modulate PLA2 by sequestering Ca2+
  [PMID:17543334 "let us speculate that Fel d 1 could provoke an allergic response through the modulation of phospholipase A2, by sequestering Ca ions in a similar manner as previously suggested for uteroglobin"].
  UniProt summarizes this as "Chelates calciums ions and may inhibit the activity of
  calcium-dependent phospholipase A2." Too tentative for a confident MF assignment.
- **Biological function genuinely unknown.** Proposed (unproven) roles: skin
  protection (uteroglobin analogy) or transport of lipids/steroids/hormones/
  pheromones [PMID:29643919 "The biological function of Fel d 1 is still unknown"].

## Localization / expression
- Secreted protein [UniProt SUBCELLULAR LOCATION: Secreted].
- Produced mainly in **sebaceous glands** (not saliva, as once thought); also in
  saliva, anal glands, skin and fur
  [PMID:29643919 "It is now recognized that the sebaceous glands, and not saliva, are the main production site"].
- → "extracellular region" (GO:0005576) annotations are appropriate.

## Allergen biology (context, not core evolved function)
- Major cat allergen; >80–95% of cat-allergic patients have anti-Fel d 1 IgE;
  accounts for 60–90% of cat allergenic activity; binds IgE; drives Th2 responses;
  recognized by the mannose receptor on antigen-presenting cells
  [PMID:29643919 "In vivo, the allergenicity of Fel d 1 is determined by its recognition by the mannose receptor on mucosal antigen-presenting cells, such as dendritic cells or macrophages"].
- IgE binding (GO:0019863) is a real molecular activity but reflects allergenicity
  toward humans, not the protein's endogenous evolved function in cat.

## Curation decisions (existing GOA annotations)
1. GO:0005496 steroid binding (IBA, GO_REF:0000033) → MARK_AS_OVER_ANNOTATED
   (family inference; no direct evidence Fel d 1 binds steroids).
2. GO:0005576 extracellular region (IBA, GO_REF:0000033) → ACCEPT (secreted).
3. GO:0005496 steroid binding (IEA, GO_REF:0000118) → MARK_AS_OVER_ANNOTATED.
4. GO:0005576 extracellular region (IEA, GO_REF:0000120) → ACCEPT (secreted).

core_functions: documented MF = calcium ion binding (GO:0005509) in the
extracellular region; in vivo biological role recorded as a knowledge gap.

## Key references
- PMID:29643919 — review (curation target), full text in PMC.
- PMID:12851385 — monomeric crystal structure; secretoglobin/uteroglobin fold; cavity.
- PMID:17543334 — tetramer crystal structure; two Ca2+-binding sites; PLA2 speculation.
- PMID:1946388 — Fel d 1 protein sequence + cDNA cloning.
- PMID:1572548 — genomic structure of the two Fel d 1 genes.
- PMID:1712068 — biochemical structure of the major cat allergen.
- PMID:6747135 — Cat allergen 1 biochemical/antigenic/allergenic properties.

---

## Update: Falcon deep research integration (CH1-deep-research-falcon.md)

Ran FutureHouse Falcon deep research (34 citations). Key additions beyond the
original PMC5891966-based review, with primary sources fetched and verified:

### New molecular activity — LPS binding + TLR4/TLR2 enhancement (experimental)
Herre et al. 2013 (PMID:23878318, full text in PMC) is the best-characterized
molecular activity of Fel d 1:
- "Fel d 1 substantially enhances signaling through the innate receptors TLR4 and TLR2"
  [PMID:23878318 "enhances signaling through the innate receptors TLR4 and TLR2"].
- Fel d 1 binds the TLR4 agonist LPS, acting via a lipid-transfer mechanism (CD14/MD2-
  dependent) rather than by mimicking MD2
  [PMID:23878318 "bind to the TLR4 agonist LPS"].
→ Supports NEW annotations: lipopolysaccharide binding (GO:0001530) and positive
  regulation of toll-like receptor 4 signaling pathway (GO:0034145). This is shown
  largely in the context of human allergic sensitization/innate amplification, not
  confirmed cat physiology, but it is a bona fide molecular activity of the protein.

### Ligand binding revises the "steroid binding" assessment
Popescu et al. 2021 (PMID:34026578) reports that Fel d 1 binds fatty acids and
steroids with good affinity:
- [PMID:34026578 "binding with good affinity to some fatty acids and steroids, the best ligands being lauric acid"]
  (lauric acid; androsterone — a volatile steroid pheromone).
→ The IBA/IEA "steroid binding" (GO:0005496) is therefore NOT merely a baseless
  family inference; there is reported ligand-binding evidence. Revised from
  MARK_AS_OVER_ANNOTATED to KEEP_AS_NON_CORE: a real activity, plausibly part of a
  broader small-hydrophobic-ligand binding / transport (pheromone) role, but not the
  single core function. Fatty acid binding (lauric acid) is also reported.

### Native function still unknown; expression is androgen-regulated
- Native biological function in the cat remains formally unestablished
  (Grönlund 2010 PMID:19844127; Popescu 2021); proposed roles: lipid/steroid (pheromone)
  transport, chemical communication, epithelial/skin defense, immunoregulation.
- Production is testosterone-regulated (intact males >> neutered); secreted by
  sebaceous, salivary, lacrimal glands and anal sacs.
- Secretoglobin superfamily binds retinoids, phospholipids, steroids and calcium
  (Karn & Laukaitis 2025); no SCGB has a firmly established function.

### Newly added/verified references
- PMID:23878318 — Herre 2013, Fel d 1 enhances TLR activation by lipid ligands (PMC full text).
- PMID:19844127 — Grönlund 2010, major cat allergen Fel d 1 in diagnosis and therapy (review).
- PMID:34026578 — Popescu 2021, molecular diagnosis in cat allergy (review; ligand data).
- file:FELCA/CH1/CH1-deep-research-falcon.md — Falcon deep research report.
