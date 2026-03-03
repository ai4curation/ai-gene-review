# SNIPE: Membrane-Bound Nuclease Anti-Phage Defence

## Overview

SNIPE (Surface-associated Nuclease Inhibiting Phage Entry) is a bacterial anti-phage defence system that cleaves phage DNA during genome injection. It represents a novel self/non-self discrimination strategy in prokaryotic immunity, distinct from CRISPR-Cas (sequence recognition) and restriction-modification (DNA modification recognition). SNIPE exploits the spatial organization of phage genome injection — the fact that phage DNA must pass through the cell membrane — to specifically target foreign DNA.

**Key paper**: Saxton DS, DeWeirdt PC, Doering CR, Roney IJ & Laub MT (2026). A membrane-bound nuclease directly cleaves phage DNA during genome injection. *Nature*. https://doi.org/10.1038/s41586-026-10207-1

**Previous identification**: Vassallo CN, Doering CR, Littlehale ML, Teodoro GIC & Laub MT (2022). A functional selection reveals previously undetected anti-phage defence systems in the *E. coli* pangenome. *Nat. Microbiol.* 7:1568-1579. (Originally named PD-lambda-1.)

## Mechanism

1. SNIPE is a ~500 aa inner membrane protein with three domains:
   - **N-terminal transmembrane domain** (aa 5-24): anchors to inner membrane
   - **DUF4041 domain** (aa ~144-262): binds DNA; interacts with phage tape measure proteins (TMPs)
   - **GIY-YIG nuclease domain** (aa ~357-450): cleaves phage DNA (catalytic residue E414)
2. SNIPE pre-associates with **ManYZ** (mannose permease) in the inner membrane before infection
3. During phage genome injection, DUF4041 binds the phage tape measure protein, positioning the nuclease to cleave incoming DNA
4. This provides **direct defence** — the infected cell survives (unlike abortive infection systems)
5. SNIPE also provides ManYZ-independent defence against siphoviruses via weak TMP interactions

## InterPro / Pfam

- **IPR025280** — "SNIPE associated domain" (recently renamed from DUF4041 to reflect this paper)
- **PF13250** — Pfam entry for DUF4041
- 1,612 protein matches across 1,044 proteomes and 2,466 taxa
- ~500 curated SNIPE homologues across many bacterial phyla
- 33% of well-sequenced bacterial clades harbour at least one SNIPE homologue

## Key Proteins

### SNIPE (PD-lambda-1)
- **UniProt TrEMBL**: A0A8T9CRB7 (best match; no Swiss-Prot entry)
- **GenBank**: RCP76574.1 (from *E. coli* MOD1-ECOR26, locus APT27_20780)
- **RefSeq**: WP_001606968.1
- Not present in *E. coli* K-12 MG1655 — encoded in prophage elements of wild *E. coli* strains

### E. coli host proteins involved

| Protein | UniProt | Role in SNIPE mechanism |
|---------|---------|------------------------|
| ManY | P69801 | Inner membrane permease; SNIPE pre-associates with ManYZ complex |
| ManZ | P69805 | Inner membrane permease; part of genome injection apparatus for lambda |
| ManX | P69797 | Mannose PTS EIIAB component |
| LamB | P02943 | Outer membrane maltoporin; lambda receptor |
| OmpF | P02931 | Outer membrane porin; alternative receptor for generalist lambda |

### Phage lambda proteins

| Protein | UniProt | Role |
|---------|---------|------|
| gpH (TMP) | P03736 | Tape measure protein; SNIPE target during genome injection |
| gpJ | P03749 | Tail tip protein; host specificity |

## Evolutionary Diversity of SNIPE Homologues

SNIPE homologues show a modular architecture with highly diversified N-terminal regions:
- **59%** harbour one transmembrane domain
- **7%** harbour two transmembrane domains
- **34%** lack predicted TM domains — these use alternative membrane-targeting strategies:
  - DivIVA domains (negative membrane curvature binding)
  - Type III secretion system domains
  - Pleckstrin homology domains (phospholipid binding)
  - Phage tail protein fusions

The GIY-YIG nuclease domain is the most conserved region. The DUF4041 domain shows moderate conservation with a positively charged DNA-binding interface. The N-terminal region has the highest variability, suggesting it functions as an adapter for phage specificity.

## GO Annotation Considerations

### Potential GO terms for SNIPE
- **Molecular Function**: endonuclease activity (GIY-YIG family); DNA binding; protein binding (tape measure protein)
- **Biological Process**: defence response to bacteriophage; DNA catabolic process; negative regulation of viral genome replication
- **Cellular Component**: integral component of plasma membrane

### Annotation challenges
1. No existing GO term captures "cleavage of foreign DNA during membrane injection"
2. The DUF4041 domain has dual function (DNA binding + TMP binding) — needs careful annotation
3. Direct defence vs. abortive infection distinction matters for BP annotation
4. The ManYZ interaction is pre-infection positioning, not a canonical "protein complex"

### Potential new GO terms
- "phage genome injection site" (CC) — for membrane complexes at injection points
- "defence response to bacteriophage via direct DNA cleavage" (BP) — to distinguish from abortive infection
- "tape measure protein binding" (MF) — specific interaction that enables SNIPE targeting

## Related Projects

- ANTI_CRISPR — other phage defence systems
- Bacterial immunity annotation more broadly

## Genes for Review

| Species | Gene | UniProt | Status |
|---------|------|---------|--------|
| ECOLX (wild) | SNIPE/PD-lambda-1 | A0A8T9CRB7 | DRAFT |

## Key References

- Saxton et al. (2026) Nature — SNIPE characterization (PMID:41741653)
- Vassallo et al. (2022) Nat Microbiol 7:1568-1579 — Original identification as PD-lambda-1
- Maffei et al. (2021) PLoS Biol 19:e3001424 — BASEL phage collection
- Branon et al. (2018) Nat Biotechnol 36:880-887 — TurboID proximity labelling
- Hallgren et al. (2022) bioRxiv — DeepTMHMM transmembrane prediction

---

# STATUS

## Completed
- [x] Read and summarize Saxton et al. 2026
- [x] Full gene review of SNIPE (A0A8T9CRB7) — genes/ECOLX/SNIPE/SNIPE-ai-review.yaml
- [x] Assess whether new GO terms are needed — proposed 2 new terms in review
- [x] Draft GO issue for antiviral nucleic acid defence hierarchy — projects/SNIPE/go-issue-antiviral-nucleic-acid-defense.md

## Pending
- [ ] Check current GO annotations for SNIPE homologues
- [ ] Review SNIPE homologue diversity and domain architecture annotations in InterPro
- [ ] Cross-reference with DefenseFinder database entries
- [ ] Propose InterPro2GO mappings for PF13250/IPR025280 (currently none exist)
- [ ] Add literature references to IPR025280 (currently none linked)

Last updated: 2026-03-01

# NOTES

## 2026-03-01

**Project Creation**

Created from reading Saxton et al. (2026) Nature paper on SNIPE.

Key observations:
- IPR025280 (formerly DUF4041) has already been renamed to "SNIPE associated domain" in InterPro, with description updated to reference the cleavage mechanism. This suggests InterPro curators updated the entry around publication.
- SNIPE represents a genuinely novel immune mechanism — not sequence-based (like CRISPR) or modification-based (like R-M), but localization-based.
- Conceptual parallel to eukaryotic IFITM proteins that block viral entry at membranes.
- The modular N-terminal diversity across ~500 homologues is an interesting case for studying domain shuffling and functional diversification.
