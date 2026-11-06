# VEGFA Notes - ISOFORMS Project

## Key Isoform Biology

VEGFA has **17 named isoforms** from alternative splicing, representing extreme diversity in isoform function.

### Major Isoforms by Length

| Isoform | UniProt ID | Length | Heparin Binding | Matrix Bound | Key Feature |
|---------|------------|--------|-----------------|--------------|-------------|
| VEGF206 | P15692-1 | 206 AA | Strong | Yes | Longest, matrix-bound |
| VEGF189 | P15692-2 | 189 AA | Strong | Yes | Matrix-bound |
| VEGF165 | P15692-4 | 165 AA | Moderate | Intermediate | Canonical "VEGF" |
| VEGF121 | P15692-9 | 121 AA | None | No | Freely diffusible |
| **VEGF165B** | P15692-8 | 165 AA | ? | ? | **ANTI-ANGIOGENIC** |

### Critical Isoform Difference: VEGF165 vs VEGF165B

UniProt explicitly states for VEGF165B:
> "Binds to the KDR receptor but does not activate downstream signaling pathways, does not activate angiogenesis and inhibits tumor growth" [PMID:15520188]

This means:
- **VEGF165**: Pro-angiogenic, promotes tumor growth
- **VEGF165B**: Anti-angiogenic, inhibits tumor growth

Same length (165 AA), same receptor binding, but **opposite biological effects**!

### Heparin Binding and Matrix Association

The longer isoforms (VEGF189, VEGF206) contain heparin-binding domains and remain matrix-bound, creating:
- **Steep gradients** - important for vessel sprouting
- **Localized signaling** - concentrated at source

The shorter isoform (VEGF121) lacks heparin binding:
- **Freely diffusible** - spreads through tissue
- **Broad signaling** - less directional

## GOA Annotation Status

- **267 total annotations**
- **NO isoform-specific annotations** (no P15692-X identifiers)
- Likely conflates pro-angiogenic (most isoforms) with anti-angiogenic (VEGF165B) functions

## Expected Annotation Issues

1. **Angiogenesis annotations** - should specify which isoforms
2. **"Positive regulation of angiogenesis"** - NOT true for VEGF165B
3. **VEGFR binding** - all isoforms bind, but different downstream effects

## Key References

- PMID:15520188 - VEGF165B anti-angiogenic properties
- Original VEGF papers describing isoform differences

## 2026-11-06 ORGANELLES ER batch 4 (endoplasmic reticulum rows)

- Row: GO:0005783 IEA (GO_REF:0000044, SL-0095). Kept KEEP_AS_NON_CORE; summary and reason rewritten, quotes added.
- Source: UniProt "[Isoform L-VEGF189]: Endoplasmic reticulum {ECO:0000269|PubMed:11731620}" (with Golgi). The other isoform lines (VEGF121, VEGF165, VEGF189) say Secreted. The displayed sequence (P15692-13) is L-VEGF189, so the row is not on the wrong isoform, and no source_defects entry was made.
- PMID:11731620 (Huez et al. 2001) was fetched and is abstract-only. In transfected COS-7 cells: [PMID:11731620 "The AUG-initiated form and the COOH cleavage product of the L-VEGF are both secreted. In contrast, the large isoform and its NH2 fragment present an intracellular localization."] The abstract does not name the ER.
- Decision: KEEP_AS_NON_CORE on curator deference (curated line from an unread full text). MARK_AS_OVER_ANNOTATED is the close alternative: overexpression data, and the classical isoforms only transit the ER. No lumen row: VEGFA is a secreted protein with no retention signal.
