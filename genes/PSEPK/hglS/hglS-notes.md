# hglS Gene Review Notes

## Gene Function Clarification

The hglS gene encodes **2-oxoadipate dioxygenase/decarboxylase** (EC 1.13.11.93), also known as **hydroxyglutarate synthase**. This enzyme catalyzes:

```
2-oxoadipate + O2 → (R)-2-hydroxyglutarate + CO2
```

## Critical Distinction Between Two Different Enzymes

The deep research file contains a significant error where it conflates hglS with a completely different enzyme. After thorough investigation, these are definitively different proteins:

### 1. hglS (Hydroxyglutarate Synthase) - THIS GENE
- **EC Number**: 1.13.11.93
- **Reaction**: 2-oxoadipate (C6) + O2 → D-2-hydroxyglutarate (C5) + CO2
- **Reaction Type**: Dioxygenase with decarboxylation (removes one carbon as CO2)
- **Direction**: IRREVERSIBLE (due to CO2 release)
- **Cofactors**: Fe(II) and O2
- **Protein Family**: DUF1338
- **Function**: Terminal step in lysine catabolism pathway
- **Discovery**: 2019-2020 (Thompson et al., PMID:31064836, PMID:32523014)

### 2. α-Hydroxyglutarate Oxidoreductase (1969 enzyme) - DIFFERENT ENZYME
- **Reaction**: D-2-hydroxyglutarate (C5) + acceptor ⇌ 2-oxoglutarate (C5) + reduced acceptor  
- **Reaction Type**: Oxidoreductase (no change in carbon number)
- **Direction**: Potentially reversible
- **Cofactors**: Electron acceptors (ferricyanide, dichlorophenol indophenol, cytochrome c)
- **Location**: Membrane-bound in electron transport particle
- **Function**: Oxidation of D-2-hydroxyglutarate in different metabolic context
- **Discovery**: 1969 (Reitz & Rodwell, PMID:5354943)

## Why These Cannot Be The Same Enzyme

1. **Different substrates and products**:
   - hglS: 2-oxoadipate (6 carbons) → 2-hydroxyglutarate (5 carbons)
   - 1969 enzyme: 2-hydroxyglutarate (5 carbons) → 2-oxoglutarate (5 carbons)

2. **Different reaction chemistry**:
   - hglS: Decarboxylation + hydroxylation (loses CO2)
   - 1969 enzyme: Simple oxidation/reduction (no CO2 involved)

3. **Different thermodynamics**:
   - hglS: Irreversible due to CO2 release
   - 1969 enzyme: Potentially reversible oxidation/reduction

4. **Different metabolic roles**:
   - hglS: Final step converting 2-oxoadipate in lysine catabolism
   - 1969 enzyme: Metabolizes D-2-hydroxyglutarate to 2-oxoglutarate

## Lysine Catabolism Pathway Context

```
L-Lysine → ... → 2-oxoadipate → [hglS/HglS] → D-2-hydroxyglutarate
                      (C6)                           (C5) + CO2
```

The D-2-hydroxyglutarate produced by hglS could theoretically serve as substrate for the 1969 oxidoreductase (if both are present), but they are separate enzymes with distinct functions in the metabolic network.

## Key Evidence

### PDB Structures
- **6W1G**: Crystal structure at 1.14 Å showing hydroxyglutarate synthase
- **6W1H**: Crystal structure at 1.42 Å with substrate (2-oxoadipate) bound

### Key Papers
- **PMID:31064836**: First characterization of DUF1338 family function, showing hglS role in lysine catabolism
- **PMID:32523014**: Structural and mechanistic studies revealing successive decarboxylation and hydroxylation mechanism

## Biological Role
- Final step in lysine catabolism pathway
- Converts 2-oxoadipate (from lysine degradation) to D-2-hydroxyglutarate
- Essential for growth on both L-lysine and D-lysine
- Expression induced by lysine and related compounds

## GO Annotation Recommendations
1. Current "oxidoreductase activity" (GO:0016491) is too broad
2. "Dioxygenase activity" (GO:0051213) is accurate and should be retained
3. A new specific term "2-oxoadipate dioxygenase/decarboxylase activity" should be created for this enzyme class