# SepN (all4109) — Nostoc sp. PCC 7120 — research notes

- **UniProt:** A0ACD7RWW5 (`A0ACD7RWW5_NOSS1`), TrEMBL/unreviewed, 235 aa, 26.7 kDa.
- **Gene / locus:** `sepN` = `all4109`. Named "SepN" for its **sep**tal localization.
  [PMID:36470860 "sepN encodes an unknown protein of 235 aa."]
- **Organism:** *Nostoc* sp. (strain PCC 7120 / SAG 25.82 / UTEX 2576), a filamentous,
  heterocyst-forming (diazotrophic) cyanobacterium. NCBITaxon:103690.
- **Distribution:** a signature protein of filamentous cyanobacteria (Nostocales /
  Oscillatoriales / Stigonematales); **always co-occurs with FraD**.
  [PMID:36470860 "SepN always co-occurs with FraD."]

## Function summary

SepN is a bitopic cytoplasmic (inner)-membrane protein that forms the **plug** module of
the **septal junction (SJ)** — the intercellular channel connecting adjacent cells in a
cyanobacterial filament. SepN is the FraD-interacting component that gates (opens/closes)
molecular diffusion through the SJ.

### Topology (Cell Reports 2026, Phobius + AlphaFold 3)
- **N-terminal transmembrane helix** (aa ~8–28) anchoring SepN in the cytoplasmic membrane.
- **Large cytoplasmic domain** (aa 29–235) whose C-terminus is exposed to the cytoplasm.
- AlphaFold 3 predicts SepN self-assembles most confidently as a **pentamer**, matching the
  5-fold symmetry of the SJ observed in situ; five SepN copies form the central plug and
  interact with five peripheral FraD anchors.
  [PMID:42424141 "Structural modeling positions SepN as the plug-forming component and FraD as a membrane-spanning anchor with a periplasmic domain."]

### Role in the septal junction
- SepN forms the SJ **plug**; cryo-ET of the `sepN−` mutant shows loss of the plug density,
  and C-terminal bulky-protein (MBP/GFP) fusions to SepN add density on the **cytoplasmic**
  side of the plug — consistent with SepN forming the plug with its C-terminus in the
  cytoplasm.
- SepN was discovered as the most abundant hit co-immunoprecipitating with FraD and is
  **indispensable for plug formation**.
  [PMID:36470860 "SepN is a septal junction component required for gated cell-cell communication in the filamentous cyanobacterium Nostoc."]

### Loss-of-function phenotypes
- `sepN−` (neomycin cassette in `sepN`): abnormal cap morphology, **absent plug**, impaired
  intercellular communication, and inability to **close/gate** SJs; failure to close SJs
  leads to propagating cell death along a filament upon stress.
- Unlike `∆fraD`, the `sepN−` mutant **still grows diazotrophically** and forms WT-like
  heterocyst septa — indicating the plug plays only a minor role in establishing functional
  heterocysts, and distinguishing SepN's role from FraD's role in septum remodeling
  (Cell Reports 2026).
- **N-terminal TM helix is dispensable for function**: a `sepN∆TM` truncation (cytoplasmic
  domain only, aa 34–235) restores WT-like FRAP gating and normal SJ ultrastructure,
  showing the TM helix is not essential under the tested conditions (Cell Reports 2026).

## Protein family

Unlike FraD, **SepN has no dedicated Pfam / InterPro / NCBIfam signature** — querying
InterPro for A0ACD7RWW5 returns zero matches, and its UniProt entry is a bare TrEMBL record
with no domain annotation. SepN nonetheless defines a conserved, taxonomically restricted
family:

- **Conserved homologs occur across filamentous cyanobacteria** — the families
  Oscillatoriophycideae, Nostocaceae, and Stigonematales.
  [PMID:36470860 "Conserved homologs of SepN can be found in filamentous cyanobacteria of the families Oscillatoriaphycideae, Nostocaceae, and Stigonematales."]
- Previously described as a **signature protein for the order Nostocales**.
- **Co-occurs with FraD**: by STRING analysis, SepN is (with one exception) always found
  together with FraD, mirroring FraD's own restriction to filamentous cyanobacteria.
  [PMID:36470860 "SepN always co-occurs with FraD."]

The lack of a formal domain model is expected for a small, lineage-specific structural
protein; the family is best defined operationally by the FraD co-occurrence and the
Nostocales-signature distribution. This restriction to multicellular cyanobacteria is
consistent with SepN's dedicated septal-junction (plug) role.

## GO annotation status
- GOA/QuickGO returns **no GO annotations** for A0ACD7RWW5 (empty `SepN-goa.tsv`). This
  review is de-novo; proposed core functions are recorded in `SepN-ai-review.yaml`.
- No dedicated GO cellular-component term exists for the bacterial **septal junction**
  (GO:0005918 "septate junction" is the arthropod epithelial junction). Candidate new term.
- UniProt entry A0ACD7RWW5 is a bare TrEMBL record (no domain/feature annotation); topology
  and function above come from the primary literature.

## Key references
- PMID:36470860 — Kieninger et al. 2022, *Nat Commun* — identification and characterization of SepN as the FraD-interacting SJ plug component (source discovery paper).
- PMID:42424141 — Kieninger et al. 2026, *Cell Rep* — SepN pentamer forms the plug; SepN–FraD architecture; sepN∆TM dispensable.
- PMID:20487302 — Merino-Puerto et al. 2010, *Mol Microbiol* — Fra proteins / SJ context (FraD partner).
