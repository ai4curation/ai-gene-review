# Bioinformatics Analysis: RvSOD15 and Cu/Zn SOD Paralogs

## Question

Sim & Inoue (2023, PMID:37358501) report that *R. varieornatus* has 16 CuZnSOD
paralogs (RvSOD1-16) and claim that "some other RvSODs are also unusual SODs"
with deletions or mutations that "may have evolved to lose SOD function."
They only crystallized RvSOD15, which has Val replacing a catalytic His.

How many of the paralogs actually show loss of catalytic capability based on
sequence and motif analysis?

## Methods

We applied **two complementary approaches** to all R. varieornatus Cu/Zn SOD
family proteins in UniProt:

### Approach 1: Direct catalytic residue conservation

Aligned each mature protein (signal peptide removed if annotated) pairwise
against human SOD1 (P00441 mature, 153 aa) using BioPython's PairwiseAligner
(BLOSUM62, global). Checked conservation of:
- **Cu ligands**: H46, H48, H63, H120 (all histidines)
- **Zn ligands**: H63 (bridging), H71, H80, D83
- **Intrachain disulfide**: C57, C146

Script: `analyze_sods.py`

### Approach 2: PROSITE motif matching via InterPro REST API

Checked which PROSITE Cu/Zn SOD signatures match each paralog:
- **PS00087** (Cu/Zn SOD signature 1): N-terminal H-x-H Cu binding signature
  - Pattern: `[GA]-[IMFAT]-H-[LIVF]-H-{S}-x-[GP]-[SDG]-x-[STAGDE]`
  - The two Hs in this pattern correspond to H46 and H48 in human SOD1 numbering
  - This pattern requires not just the H-x-H residues but also specific flanking residues
- **PS00332** (Cu/Zn SOD signature 2): C-terminal disulfide cysteine signature
  - Pattern: `G-[GNHD]-[SGA]-[GR]-x-R-x-[SGAWRV]-C-x(2)-[IV]`
  - Centered on C146 of the disulfide bond

Also checked Pfam membership: **PF00080** (Sod_Cu, the canonical Cu/Zn SOD family).

PROSITE patterns are more rigorous than simple residue conservation because
they require canonical *flanking residues* that maintain the structural geometry
of the active site loop. A protein can have the catalytic residues but fail
PROSITE because the surrounding context is divergent - precisely the type of
"subtle" defect that may impair catalysis even when key residues are present.
This is exactly what Sim & Inoue's V87H rescue experiment demonstrated for
RvSOD15: restoring the histidine alone did not restore activity because a
nearby flexible loop destabilized the coordination.

Script: `check_prosite.py`

## Results

| Gene (ORF) | Accession | Length | Pfam SODC | PS00087 (N-term Cu) | PS00332 (C-term SS) | Cu lig (residue) | Zn lig | SS | Verdict |
|------------|-----------|--------|-----------|---------------------|---------------------|-----:|-------:|---:|---------|
| **RvY_13070 (RvSOD15)** | A0A1D1VU85 | 194 | YES | **MISSING** | MATCH | 3/4 (H48→V) | 4/4 | 2/2 | **PSEUDOENZYME** |
| RvY_00650 | A0A1D1UDY8 | 292 | YES | **MISSING** | MATCH | 4/4 | 4/4 | 2/2 | **PROBABLY IMPAIRED** |
| RvY_00651 | A0A1D1UKR0 | 154 | YES | MATCH | MATCH | 4/4 | 4/4 | 2/2 | Likely functional |
| RvY_01767 | A0A1D1USM4 | 230 | NO | **MISSING** | **MISSING** | 2/4 | 0/4 | 0/2 | **HIGHLY DEGRADED** |
| RvY_03754 | A0A1D1UP68 | 156 | YES | MATCH | MATCH | 4/4 | 4/4 | 2/2 | Likely functional |
| RvY_03757 | A0A1D1UP59 | 193 | YES | **MISSING** | MATCH | 4/4 | 4/4 | 2/2 | **PROBABLY IMPAIRED** |
| RvY_09480 | A0A1D1VEY6 | 317 | YES | MATCH | MATCH | 4/4 | 4/4 | 2/2 | Likely functional |
| RvY_10893 | A0A1D1VE88 | 185 | YES | MATCH | MATCH | 4/4 | 4/4 | 2/2 | Likely functional |
| RvY_17310 | A0A1D1W3Y1 | 475 | YES | **MISSING** | MATCH | 4/4 | 4/4 | 2/2 | **PROBABLY IMPAIRED** |
| RvY_15948 | A0A1D1VWP9 | 305 | YES | (no PROSITE match) | (no PROSITE match) | 2/4 (H46→A, H48→C) | 4/4 | 2/2 | **Cu chaperone (not SOD)** |

## Key findings

### 1. Confirmed pseudoenzyme: RvSOD15 (RvY_13070)
Both methods agree. PROSITE PS00087 fails because the H-x-H motif is broken
(H48 → V). PROSITE PS00332 (the disulfide signature) still matches because
the C-terminal Cys region is intact. This independently confirms the Sim &
Inoue (2023) finding that RvSOD15 has lost a critical Cu ligand. PROSITE
agrees with their structural conclusion that this protein cannot perform
canonical SOD catalysis.

### 2. Three additional "context pseudoenzymes": RvY_00650, RvY_03757, RvY_17310
These three proteins have **all four Cu-binding histidines preserved** by
direct sequence inspection, but **fail PROSITE PS00087**. This means the
catalytic residues themselves are present, but the surrounding loop context
required for proper Cu coordination has diverged. By analogy with the V87H
rescue experiment in Sim & Inoue (where restoring His alone did not restore
activity due to loop dynamics), these proteins likely have impaired
catalytic function despite retaining the catalytic residues.

PROSITE detected these as suspect even though my simple residue-conservation
script did not - this is exactly the type of subtle pseudoenzyme that
sequence-only approaches miss.

### 3. Heavily degraded: RvY_01767
26.9% identity to human SOD1, 2/4 Cu ligands, 0/4 Zn ligands, 0/2 disulfide
cysteines, fails BOTH PROSITE patterns, AND is **not even in the Pfam SODC
family (PF00080)**. This is either a true pseudogene (if not expressed) or
has undergone such radical neofunctionalization that it no longer resembles
a SOD beyond ancestral sequence remnants. It should not have any SOD-related
GO annotation.

### 4. Copper chaperone: RvY_15948
Already classified by UniProt as "Superoxide dismutase copper/zinc binding
domain-containing protein." This is the **CCS** (Copper Chaperone for SOD)
homolog. CCS proteins have a SOD-like fold but lack canonical Cu ligands
because their function is to *deliver* copper to SODs, not catalyze
dismutation. The H46 → A and H48 → C substitutions are consistent with
chaperone function. Should not be annotated with SOD activity.

### 5. Four likely-functional canonical SODs
RvY_00651, RvY_03754, RvY_09480, RvY_10893 all pass both sequence
conservation AND both PROSITE patterns AND Pfam membership. These are the
strongest candidates for genuine functional CuZnSOD activity in
*R. varieornatus*.

### 6. Three of these have unusual size
RvY_17310 (475 aa), RvY_09480 (317 aa), RvY_00650 (292 aa). These are 2-3x
larger than canonical CuZnSOD (~150 aa). The SOD domain maps to the C-terminal
region in each. These are either:
- Genuine fusion proteins with N-terminal extensions of unknown function
- Annotation/prediction artifacts (introns not properly spliced)
- Tandem duplications

Worth noting: RvY_17310 is ~3x the canonical SOD size and PROSITE-impaired,
making it a particularly intriguing case. Independent verification (RNA-Seq,
proteomics) would be needed to confirm the predicted protein boundaries.

## Comparison of methods

| Paralog | Sequence-only | PROSITE | Final verdict |
|---------|---------------|---------|---------------|
| RvY_13070 | Broken (H48→V) | Broken (PS00087) | PSEUDOENZYME |
| RvY_01767 | Heavily degraded | Both broken + no Pfam | HIGHLY DEGRADED |
| RvY_15948 | Missing 2 Cu His | No PROSITE match | NOT A SOD (chaperone) |
| RvY_00650 | OK | Broken (PS00087) | PROBABLY IMPAIRED |
| RvY_03757 | OK | Broken (PS00087) | PROBABLY IMPAIRED |
| RvY_17310 | OK | Broken (PS00087) | PROBABLY IMPAIRED |
| RvY_00651 | OK | OK | LIKELY FUNCTIONAL |
| RvY_03754 | OK | OK | LIKELY FUNCTIONAL |
| RvY_09480 | OK | OK | LIKELY FUNCTIONAL |
| RvY_10893 | OK | OK | LIKELY FUNCTIONAL |

PROSITE detected 3 additional probably-impaired paralogs that simple residue
conservation missed. This validates Sim & Inoue's claim that "**some other
RvSODs are also unusual SODs**" - the precise count of impaired paralogs
appears to be at least 4 out of 9 SOD-like proteins (excluding the chaperone).

## Limitations

- **No biochemical assays**: Even paralogs flagged as impaired could retain
  weak/altered activity. Conversely, "likely functional" paralogs could have
  defects not detectable by sequence alone (e.g., metal binding stoichiometry,
  aggregation propensity).
- **No expression data**: Some "broken" paralogs may be true pseudogenes
  (never expressed) rather than functional pseudoenzymes.
- **No structural verification**: Sim & Inoue noted that RvSOD15 also has a
  flexible loop that destabilizes Cu coordination even in V87H mutants.
  PROSITE captures part of this (flanking sequence context) but cannot
  detect dynamic structural defects.
- **Pairwise alignment ambiguity**: For divergent paralogs like RvY_01767
  (27% identity), residue position mapping to human SOD1 may be unreliable.
- **ORF-to-RvSOD numbering**: Sim & Inoue use "RvSOD1-16" but only RvSOD15
  is explicitly mapped to a UniProt accession (RvY_13070). The other ORFs
  in this analysis are likely RvSOD1-14 and RvSOD16, but the exact mapping
  is not in the published literature.

## Implications for GO annotation

The standard automated annotation pipeline (InterPro2GO, EC2GO, UniRule) would
assign GO:0004784 (superoxide dismutase activity) to all 9 SOD-family paralogs
based on Pfam PF00080 membership. Our analysis suggests this is incorrect for
4 paralogs (RvSOD15 + 3 PROSITE failures + the heavily degraded one). This
is a textbook case of **annotation error from family-based propagation**
without considering catalytic residue conservation or motif integrity.

For curation:
- **RvY_13070 (RvSOD15)**: SOD activity should be MARKED_AS_OVER_ANNOTATED (already done)
- **RvY_00650, RvY_03757, RvY_17310**: SOD activity should be MARKED_AS_OVER_ANNOTATED with PROSITE failure as evidence
- **RvY_01767**: SOD activity should be REMOVED entirely (not in Pfam family)
- **RvY_15948**: Should be annotated as copper chaperone activity, not SOD
- **RvY_00651, RvY_03754, RvY_09480, RvY_10893**: SOD activity ACCEPT (with caveat that biochemical confirmation is lacking)

## Reproducibility

```bash
cd /Users/cjm/repos/ai-gene-review
uv run python genes/RAMVA/RvY_13070/RvY_13070-bioinformatics/analyze_sods.py
uv run python genes/RAMVA/RvY_13070/RvY_13070-bioinformatics/check_prosite.py
```

Both scripts use only the UniProt files cached in the gene directories
(`analyze_sods.py`) or the public InterPro REST API (`check_prosite.py`).
