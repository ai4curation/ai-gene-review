# Fel d 1 chain 2 (CH2, UniProt P30440) — curation notes

Curated alongside chain 1 (CH1, P30438) from the review article
PMC5891966 / PMID:29643919 (Bonnet et al. 2018, *Allergy Asthma Clin Immunol*,
"An update on molecular cat allergens: Fel d 1 and what else? Chapter 1: Fel d 1,
the major cat allergen"). See `genes/FELCA/CH1/CH1-notes.md` for the shared
Fel d 1 background.

## Identity
- UniProt P30440, `FEL1B_FELCA`, gene name `CH2` (chain 2 / β-chain).
- 109 aa precursor; signal 1–17, mature chain 18–109 (~10–11 kDa).
- **Glycoprotein**: N-linked glycosylation at Asn50 [UniProt CARBOHYD 50;
  KW Glycoprotein]. This distinguishes chain 2 from chain 1 (which is not glycosylated).
- Chain 2 pairs with chain 1 (CH1, P30438) via three interchain disulfide bonds to
  form a heterodimer; two heterodimers assemble into the ~35–38 kDa Fel d 1
  heterotetramer
  [PMID:29643919 "Each dimer consists of two polypeptide chains, chain 1 and chain 2, covalently linked by three disulfide bridges and encoded by two different genes"].
- Three alternatively spliced isoforms: long (CH2L, salivary-gland preferential),
  short (CH2S, skin-preferential), and a truncated form [UniProt ALTERNATIVE PRODUCTS
  + TISSUE SPECIFICITY].

## Family / fold
- Member of the **secretoglobin** (uteroglobin) family; contributes to the
  all-α uteroglobin-like fold of the assembled allergen
  [PMID:29643919 "Fel d 1 belongs to the family of secretoglobins or secretory globins"].
- Note: chain 2 sits in a different PANTHER family (PTHR31708) than chain 1
  (PTHR21226), so it did NOT receive the family-propagated "steroid binding"
  IBA/IEA annotation that chain 1 did.

## Molecular function (known vs inferred)
- **Calcium ion binding — experimentally supported.** Chain 2 contributes three
  calcium-coordinating residues (36, 72, 77); the tetramer crystal structure
  resolves two distinct Ca2+-binding sites
  [PMID:17543334 "the crystal structure of tetrameric Fel d 1 reveals two different calcium-binding sites"].
  UniProt FUNCTION (shared with chain 1): "Chelates calciums ions and may inhibit
  the activity of calcium-dependent phospholipase A2."
- **Phospholipase A2 modulation — speculation** (uteroglobin analogy), as for chain 1
  [PMID:17543334 "let us speculate that Fel d 1 could provoke an allergic response through the modulation of phospholipase A2, by sequestering Ca ions in a similar manner as previously suggested for uteroglobin"].
- **Biological function genuinely unknown** for the Fel d 1 complex
  [PMID:29643919 "The biological function of Fel d 1 is still unknown"].

## Localization / expression
- Secreted [UniProt SUBCELLULAR LOCATION: Secreted].
- Saliva and sebaceous glands; long form preferentially in salivary gland, short
  form preferentially in skin; sebaceous glands are the main Fel d 1 production site
  [PMID:29643919 "It is now recognized that the sebaceous glands, and not saliva, are the main production site"].
- → "extracellular region" (GO:0005576) is appropriate.

## Curation decisions (existing GOA annotations)
1. GO:0005576 extracellular region (IEA, GO_REF:0000120) → ACCEPT (secreted).

NEW: GO:0005509 calcium ion binding (chain-2 Ca-coordinating residues; tetramer
structure) added and recorded as core molecular function in the extracellular region;
in vivo biological role + cavity ligand recorded as knowledge gaps (shared with CH1).

## Key references
- PMID:29643919 — review (curation target), full text in PMC.
- PMID:12851385 — monomeric crystal structure; secretoglobin/uteroglobin fold; cavity.
- PMID:17543334 — tetramer crystal structure; two Ca2+-binding sites; PLA2 speculation.
- PMID:1946388 — Fel d 1 protein sequence + cDNA cloning (chain 2 sequence).
- PMID:1572548 — genomic structure, alternative splicing and variants of chain 2.
- PMID:1712068 — biochemical structure of the major cat allergen.
- PMID:6747135 — Cat allergen 1 biochemical/antigenic/allergenic properties.

---

## Update: Falcon deep research integration (CH2-deep-research-falcon.md)

Ran FutureHouse Falcon deep research for chain 2 (27 citations). Findings mirror
the CH1 deep research, since the documented activities are properties of the
assembled Fel d 1 tetramer to which chain 2 contributes (the deep research notes
"no independent chain-specific mechanism reported" for chain 2). Verified against
the same primary sources used for CH1:

- LPS binding + TLR4/TLR2 enhancement (Herre 2013, PMID:23878318): Fel d 1 binds
  LPS and enhances TLR4/TLR2 signaling via CD14/MD2-dependent lipid transfer;
  enhancement is independent of glycosylation status (relevant since chain 2 is the
  glycosylated chain) [PMID:23878318 "bind to the TLR4 agonist LPS"].
  → Added NEW: lipopolysaccharide binding (GO:0001530) and positive regulation of
  toll-like receptor 4 signaling pathway (GO:0034145), framed as chain 2's
  contribution to the heterotetramer (UniProt places the same FUNCTION on both
  P30438 and P30440).
- Ligand binding: Fel d 1 binds fatty acids and steroids (lauric acid, androsterone)
  [PMID:34026578 "binding with good affinity to some fatty acids and steroids, the best ligands being lauric acid"];
  both chains form the hydrophobic cavity. Captured in description/knowledge gaps
  rather than as a chain-2-specific MF.
- Chain-2 specifics reaffirmed: glycosylated (N-linked tri-antennary), ~10 kDa,
  tissue-specific length isoforms (skin short / salivary long), contributes
  calcium-coordinating residues.

### Newly added references
- PMID:23878318 — Herre 2013 (LPS/TLR4 enhancement; glycosylation-independent).
- PMID:34026578 — Popescu 2021 (fatty-acid/steroid ligand binding).
- file:FELCA/CH2/CH2-deep-research-falcon.md — Falcon deep research report.
