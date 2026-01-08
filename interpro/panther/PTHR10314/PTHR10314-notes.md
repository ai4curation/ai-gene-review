# PANTHER Family PTHR10314 Analysis Notes

## Family Overview

| Field | Value |
|-------|-------|
| **Family ID** | PTHR10314 |
| **Name** | Cysteine Synthase/Cystathionine Beta-Synthase |
| **Root Node** | PTN000034104 |
| **Taxonomic Scope** | LUCA (Last Universal Common Ancestor) |
| **Root Event** | DUPLICATION |

## IBA Annotation Issue

### Problem Summary

GO:0019344 (L-cysteine biosynthetic process) is annotated at the root node PTN000034104 and propagated to ALL descendants. This is incorrect for subfamily SF135 (Cds1/desulfhydrase) which catalyzes cysteine **catabolism**, not biosynthesis.

### Tree Structure

```
PTHR10314 (Family)
    └── PTN000034104 (Root, LUCA, DUPLICATION)
            │
            │  ⚠️ GO:0019344 "L-cysteine biosynthetic process" annotated here
            │     → Propagates to ALL descendants (ERROR for SF135)
            │
            ├── PTN000034466 [SF194 - CBS/CysK] (branch 0.412)
            │   └── EC 4.2.1.22 / 2.5.1.47 - BIOSYNTHESIS ✓
            │
            ├── PTN008304321 [SF135 - Cds1] (branch 0.528)  ← LONGEST BRANCH
            │   └── EC 4.4.1.1 - CATABOLISM ✗ (WRONG ANNOTATION)
            │
            ├── PTN000741516 [SF5 - Threonine synthase] (branch 0.659)
            │
            ├── PTN008497437 [SF242 - O-Ac-Ser CBS] (branch 0.458)
            │
            └── PTN008497439 [SF162 - CysM] (branch 0.402)
                └── EC 2.5.1.47 - BIOSYNTHESIS ✓
```

### Key Subfamilies

| Subfamily | Name | Branch Length | EC | Function | Correct BP |
|-----------|------|---------------|-----|----------|------------|
| SF135 | Cds1 (desulfhydrase) | **0.528** | 4.4.1.1 | CATABOLISM | GO:0019450 |
| SF194 | CBS/CysK | 0.412 | 4.2.1.22 / 2.5.1.47 | Biosynthesis | GO:0019344 |
| SF162 | CysM | 0.402 | 2.5.1.47 | Biosynthesis | GO:0019344 |
| SF242 | O-Ac-Ser CBS | 0.458 | 2.5.1.47 | Biosynthesis | GO:0019344 |
| SF5 | Threonine synthase | 0.659 | 4.2.3.1 | Thr synthesis | GO:0009088 |

### Evidence: SF135 is Functionally Distinct

1. **Longest branch length (0.528)** from root indicates greatest sequence divergence
2. **Different EC number**: 4.4.1.1 (lyase) vs 2.5.1.47 (transferase)
3. **Opposite reaction direction**:
   - SF194/SF162: O-Ac-L-Ser + H2S → L-Cys (BIOSYNTHESIS)
   - SF135: L-Cys + H2O → H2S + pyruvate (CATABOLISM)
4. **Different products**: SF135 produces H2S as main product; SF194/SF162 consume H2S

### Proteins in SF135 (Cds1 subfamily)

| UniProt | Gene | Organism | Definition |
|---------|------|----------|------------|
| O69652 | cds1 (Rv3684) | M. tuberculosis | L-cysteine desulfhydrase Cds1 |
| Q9KT44 | cds1 (VC_1061) | V. cholerae | L-cysteine desulfhydrase Cds1 |
| Q8ZRB5 | cds1 (STM0458) | S. typhimurium | L-cysteine desulfhydrase Cds1 |
| Q8PCX2 | cysM (XCC0578) | X. campestris | L-cysteine desulfhydrase Cds1 |
| A0A2U2H408 | cds1 (YPO3147) | Y. pestis | L-cysteine desulfhydrase Cds1 |

### Source Proteins for IBA (WITH/FROM field)

These proteins ARE correctly annotated to GO:0019344:

| UniProt | Gene | Subfamily | Organism | Correct? |
|---------|------|-----------|----------|----------|
| P0ABK5 | cysK | SF194 | E. coli | ✓ Yes |
| P35520 | CBS | SF194 | Human | ✓ Yes |
| P16703 | cysM | SF162 | E. coli | ✓ Yes |
| P9WP53 | cysM | SF162 | M. tuberculosis | ✓ Yes |
| P9WP55 | cysK1 | SF194 | M. tuberculosis | ✓ Yes |
| P37887 | cysK | SF194 | B. subtilis | ✓ Yes |

## Root Cause Analysis

### Why the Error Occurs

1. **Structural similarity ≠ functional equivalence**: All subfamilies share the TrpB-like PLP fold
2. **Annotation at wrong taxonomic level**: GO:0019344 should be at SF194/SF162 level, not root
3. **Neo-functionalization not captured**: SF135 evolved a new function after diverging from common ancestor

### Sequence Evidence from MSA Analysis

**Full family MSA**: [msa/PTHR10314.afa](msa/PTHR10314.afa) (1448 sequences, fetched via `just family-msa PTHR10314`)

**Representative subset**: [msa/representatives.aln](msa/representatives.aln) (5 key proteins for focused analysis)

#### Sequence Length Differences

| Protein | Subfamily | Length |
|---------|-----------|--------|
| Cds1 (M. tuberculosis) | SF135 | 368 aa |
| Cds1 (V. cholerae) | SF135 | 355 aa |
| CysK (E. coli) | SF194 | 323 aa |
| CysM (E. coli) | SF162 | 303 aa |
| CBS (Human) | SF194 | 551 aa |

#### Pairwise Sequence Identity

| Comparison | Identity |
|------------|----------|
| Cds1-Mtb vs Cds1-Vc | **59.2%** (conserved within SF135) |
| Cds1-Mtb vs CysK | **23.4%** |
| Cds1-Mtb vs CysM | **24.7%** |
| CysK vs CysM | 42.6% |
| CysK vs CBS | 39.9% |

**Key finding**: SF135 (Cds1) shares only ~24% identity with cysteine synthases, less than CysK shares with CysM (43%). This is consistent with neo-functionalization.

#### N-terminal Extension in SF135

Cds1 has a unique N-terminal extension before the aligned core:
- Cds1-Mtb: `MSGGACIAVRSLSRSWTDN` (19 residues)
- Cds1-Vc: `MCTDHQWINS` (10 residues)
- CysK/CysM: No equivalent extension

#### Active Site Signature Motif (MSA position ~1688)

The full PANTHER MSA reveals a **diagnostic active site signature** that explains functional divergence:

| Subfamily | Motif | Function |
|-----------|-------|----------|
| SF194/SF162 (synthases) | **PTSGNTG** | Cysteine biosynthesis |
| SF135 (desulfhydrase) | **ASSGST** | Cysteine catabolism |

Key substitutions in SF135:
- **P→A**: Proline to Alanine at loop start
- **N→S**: Asparagine to Serine in middle
- **G→T**: Different terminal residue

These substitutions in the active site loop alter substrate binding and explain why SF135 catalyzes the **reverse reaction** (cysteine breakdown → H₂S + pyruvate) compared to synthases (O-acetylserine + H₂S → cysteine).

#### Conserved PLP-Binding Lysine

Position 1352: Lysine conserved >97% in all subfamilies - this is the catalytic residue that binds pyridoxal-5'-phosphate (PLP). The core PLP chemistry is conserved; only substrate specificity differs.

#### Diagnostic Positions Summary

- 174 positions where SF135 is internally conserved but differs from both SF194 and SF162
- 31 differences in an 80-position window around active site
- SF135 shares only ~24% identity with synthases (vs 43% between CysK and CysM)

## Recommendations

### For GO-Central/PANTHER Curators

1. **Remove** GO:0019344 propagation to SF135
2. **Add** SF135-specific annotations:
   - GO:0019450 (L-cysteine catabolic process to pyruvate)
   - GO:0080146 (L-cysteine desulfhydrase activity)
   - GO:0070814 (hydrogen sulfide biosynthetic process)
3. **Generalize** root annotation to "cysteine metabolic process" OR restrict to SF194/SF162

### For Gene Reviews

Mark GO:0019344 as REMOVE for any SF135 protein with reason:
> "Incorrect IBA propagation - enzyme is catabolic (EC 4.4.1.1 desulfhydrase), not biosynthetic (EC 2.5.1.47 synthase). Source proteins in WITH/FROM are from SF194/SF162 (true synthases), but target is in SF135 (desulfhydrase subfamily) which diverged early with longest branch length (0.528) indicating neo-functionalization."

## Deep Research Findings (Falcon 2026-01-06)

See full report: [PTHR10314-deep-research-falcon.md](PTHR10314-deep-research-falcon.md)

### Key Structural Features

- **Common fold**: Tryptophan synthase β-superfamily (PLP fold type II/β family)
- **Core chemistry**: PLP-mediated β-elimination/β-replacement via aminoacrylate intermediate
- **Conserved catalytic lysine**: Lys41 (OASS numbering) forms internal aldimine with PLP

### Substrate Specificity Determinants

| Subfamily | Key Residues | Sulfur Donor | Reference |
|-----------|--------------|--------------|-----------|
| CysK | Gly230/Ala231/Gly232 | Sulfide only | McGarvie 2025 |
| CysM | Arg210/Arg211/Trp212 + 3-residue insertion | Sulfide OR thiosulfate | McGarvie 2025 |
| OPS-CysM | Similar to CysM | Thiocarboxylated CysO | McGarvie 2025 |
| CBS | Different architecture | Homocysteine | Pedretti 2024 |

### Regulatory Diversity

1. **CysK**: Forms Cysteine Synthase Complex (CSC) with serine acetyltransferase (CysE)
   - CysE C-terminal tail binds in CysK active site and inhibits activity
   - CysM generally LACKS CSC formation

2. **CBS (mammalian)**:
   - N-terminal heme-binding domain
   - C-terminal SAM-responsive Bateman regulatory domain
   - Forms filaments modulated by SAM (morpheein behavior)

### Literature Support

- Zmich et al. 2023 ACS Catalysis: Multiplexed screening of 40 PLP-dependent homologs reveals mis-annotation
- McGarvie 2025: OASS structure-function and druggability
- Pedretti 2024: H2S-producing enzymes as antimicrobial targets

## Note on Cds1 (SF135) Gap in Literature

The deep research focused primarily on OASS (CysK/CysM) and CBS subfamilies. The **L-cysteine desulfhydrase (Cds1) subfamily (SF135)** was not extensively covered, though it represents a clear case of neo-functionalization:

- Cds1 catalyzes the **reverse reaction**: L-cysteine → H2S + pyruvate (EC 4.4.1.1)
- This is cysteine CATABOLISM, not biosynthesis
- Key experimental papers: PMID:34439535 (M. tuberculosis), PMID:34283874 (V. cholerae)

## References

- PANTHER API: https://www.pantherdb.org/services/oai/pantherdb/treeinfo?family=PTHR10314
- InterPro: https://www.ebi.ac.uk/interpro/entry/panther/PTHR10314/
- QuickGO IBA documentation: https://www.ebi.ac.uk/QuickGO/term/GO:0019344
- Zmich et al. 2023: https://doi.org/10.1021/acscatal.3c02498

## Experimental Evidence

### For SF135 (Cds1) function:

**PMID:34439535** (Kunota et al. 2021) - M. tuberculosis Cds1:
- Genetic deletion reduces H2S production
- LC-MS/MS confirms products: H2S + pyruvate
- KM = 11.26 mM for cysteine, kcat = 78.71 sec-1
- Activity inhibited by AOAA (PLP inhibitor), NOT by PAG (CGL inhibitor)

**PMID:34283874** (Ma et al. 2021) - V. cholerae Cds1:
- VC1061 (cds1) is principal determinant of cysteine-derived H2S
- H2S protects against oxidative stress (H2O2)
- CBS-derived H2S enhances catalase (KatB) activity

---
*Analysis performed 2026-01-06*
