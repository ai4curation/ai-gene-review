# CPT1C Review Notes

## 2026-02-05: Initial Review

### Context
CPT1C was identified during analysis of human Recon3D metabolic model as having an EC number discrepancy (CLASS_CHANGE type). This prompted a full GO annotation review.

### Recon3D Model Error

**Finding**: CPT1C (gene ID 126129) is annotated in Recon3D with carnitine O-palmitoyltransferase activity (EC 2.3.1.21), but experimental evidence demonstrates it actually functions as a palmitoyl thioesterase (EC 3.1.2.22).

| Source | EC Number | Enzyme Class | Function |
|--------|-----------|--------------|----------|
| Recon3D | 2.3.1.21 | Transferase | Carnitine O-palmitoyltransferase |
| UniProt (correct) | 3.1.2.22 | Hydrolase | Palmitoyl thioesterase |

**Impact**: This is a CLASS_CHANGE error - the enzyme class is completely different:
- Recon3D assumes CPT1C transfers acyl groups to carnitine for mitochondrial fatty acid import
- CPT1C actually hydrolyzes thioester bonds to depalmitoylate proteins in the ER

This would affect:
1. Any metabolic model simulations involving fatty acid beta-oxidation
2. Predictions for CPT1C knockout phenotypes (would incorrectly predict fatty acid metabolism defects)
3. Drug target modeling (thioesterase vs transferase active sites are structurally different)

**Root cause**: CPT1C was named based on sequence homology to CPT1A and CPT1B, which are bona fide carnitine palmitoyltransferases. However, CPT1C has evolved a distinct function and is now classified as a pseudoenzyme with respect to the canonical CPT1 activity.

### GO Annotation Errors Found

Four IEA/IBA annotations incorrectly attribute ancestral CPT1 functions to CPT1C:

| GO Term | Annotation | Problem |
|---------|------------|---------|
| GO:0016740 | transferase activity | WRONG - CPT1C is a hydrolase |
| GO:0016746 | acyltransferase activity | WRONG - CPT1C lacks this activity |
| GO:0006631 | fatty acid metabolic process (IBA) | WRONG - CPT1C not involved |
| GO:0009437 | carnitine metabolic process (IBA) | WRONG - CPT1C not involved |

**Notably**, the correct NOT annotations already exist:
- NOT GO:0004095 (carnitine O-palmitoyltransferase activity)
- NOT GO:0005739 (mitochondrion)
- NOT GO:0006631 (fatty acid metabolic process)
- NOT GO:0009437 (carnitine metabolic process)

The conflict between positive IBA/IEA and negative ISS annotations reflects the tension between sequence-based inference and experimental evidence.

### Key Literature

1. **PMID:12376098** (Price 2002) - Original cloning, noted low/absent CPT1 activity
2. **PMID:16651524** (Wolfgang 2006) - Energy homeostasis role, malonyl-CoA binding
3. **PMID:25751282** (Rinaldi 2015) - SPG73 disease association, ER localization, ATL1 interaction
4. **PMID:30135643** (Gratacós-Batlle 2018) - KEY: Demonstrated palmitoyl thioesterase activity with catalytic triad Ser-252/His-470/Asp-474

### Disease Association

Mutations in CPT1C cause **Spastic Paraplegia 73 (SPG73)** [MIM:616282]:
- Autosomal dominant
- Pure spastic paraplegia phenotype
- R37C mutation affects N-terminal regulatory domain
- Mechanism involves altered lipid droplet formation and ATL1 interaction

### Alzheimer's Disease Relevance

CPT1C is relevant to AD through:
1. **AMPAR regulation** - CPT1C controls AMPAR trafficking; glutamatergic dysfunction is a feature of AD
2. **Brain-specific expression** - Only CPT1 isoform expressed predominantly in neurons
3. **Energy sensing** - Malonyl-CoA binding couples nutrient status to synaptic function
4. **Lipid metabolism** - Though not classical fatty acid metabolism, CPT1C affects lipid handling

The Recon3D error would incorrectly model CPT1C in fatty acid oxidation pathways rather than its actual role in synaptic receptor regulation.

### Summary of Functional Neofunctionalization

CPT1C represents a striking example of enzyme neofunctionalization:

```
                     CPT1A/CPT1B (mitochondrial)
                     - Carnitine O-palmitoyltransferase (EC 2.3.1.21)
                     - Fatty acid import into mitochondria
Ancestral CPT1 ----{
                     CPT1C (ER)
                     - Palmitoyl thioesterase (EC 3.1.2.22)
                     - Protein depalmitoylation for AMPAR trafficking
```

Despite retaining the carnitine palmitoyltransferase family fold and name, CPT1C has evolved:
- Different cellular localization (ER vs mitochondria)
- Different enzymatic mechanism (hydrolysis vs transfer)
- Different substrate (palmitoylated proteins vs acyl-CoA + carnitine)
- Different biological role (synaptic regulation vs energy metabolism)
