# FGFR2 (Fibroblast Growth Factor Receptor 2) Notes - ISOFORMS Project

## Key Isoform Biology

FGFR2 encodes a receptor tyrosine kinase with **tissue-specific isoform switching** that determines ligand specificity.

### Critical Isoforms: IIIb vs IIIc

| Isoform | UniProt ID | Exon Usage | Ligand Specificity | Tissue Expression |
|---------|------------|------------|-------------------|-------------------|
| **FGFR2IIIb** | P21802-1 | Exon IIIb | FGF1, FGF3, FGF7 (KGF), FGF10 | **EPITHELIAL** |
| **FGFR2IIIc** | P21802-3 | Exon IIIc | FGF1, FGF2, FGF4, FGF6, FGF9 | **MESENCHYMAL** |

### The IIIb vs IIIc Switch

The Ig-like domain III is alternatively spliced:
- **Exon IIIb** encodes epithelial-specific splice variant
- **Exon IIIc** encodes mesenchymal-specific splice variant

This creates **mutually exclusive ligand binding**:
- FGF7 (KGF) binds ONLY to IIIb (epithelial)
- FGF2 binds preferentially to IIIc (mesenchymal)

### Biological Significance: Epithelial-Mesenchymal Communication

The IIIb/IIIc isoform switching enables **paracrine signaling**:
- Mesenchyme produces FGF7/10 → signals to epithelium (IIIb)
- Epithelium produces FGF2/4 → signals to mesenchyme (IIIc)

This is critical for:
- Limb development
- Lung branching morphogenesis
- Prostate development
- Wound healing

### Soluble/Secreted Isoforms

- **Isoform 8** (P21802-8): Secreted
- **Isoform 13** (P21802-13): Secreted

These may act as decoy receptors, similar to soluble FAS.

### Cancer Relevance

**Isoform switching in cancer:**
- Epithelial-to-mesenchymal transition (EMT) includes IIIb→IIIc switch
- Some cancers inappropriately express IIIc in epithelial contexts
- Mis-splicing correlates with metastatic potential

## GOA Annotation Status

- **250 annotations fetched, 229 seeded**
- **NO isoform-specific annotations** - all annotated to P21802 gene level

## Expected Annotation Issues

1. **"FGF receptor signaling pathway"** - applies to both isoforms but with different ligands
2. **"fibroblast growth factor binding"** - TRUE for both, but DIFFERENT FGFs
3. Epithelial morphogenesis terms may be IIIb-specific
4. Mesenchymal development terms may be IIIc-specific
5. Any FGF7 (KGF) signaling annotations should be IIIb-specific
6. Any FGF2 signaling annotations should be preferentially IIIc

## Key References

- UniProt P21802 function annotation distinguishes IIIb and IIIc ligand binding
- PMID:1309608 - FGFR2 cloning and splice variants
- PMID:7987400 - FGF receptor ligand specificities


## 2026-10-27 — source audit and correction

The earlier journal entry above is preserved as written. Its accession table and
ligand exclusivity statement are superseded by the following source-bound
correction. UniProt P21802 identifies **P21802-1 as IIIc/BEK** and **P21802-3 as
IIIb/KGFR**. The products named 8 and 13 are **P21802-14 and P21802-19**, not
P21802-8/P21802-13. Six truncated sequence-note strings were completed from
the literal continuation lines of the same immutable UniProt record. No product
was regenerated, renamed, reordered or assigned a new function.

Alternative exon choice is distinct from mutually exclusive ligand recognition.
PMID:8663044 Table I uses human FGFR2b and mouse FGFR2c in BaF3 cells; its Methods,
Figure 3 and Table II show overlapping recognition, including FGF1. The original
Results warn that mitogenic rankings depend on the cell and heparan-sulfate
context. PMID:7987400 is a Crouzon syndrome paper, not the ligand-specificity
experiment previously assigned to it here. Soluble-product secretion does not
establish a decoy mechanism, and epithelial/mesenchymal expression preferences
should not become universal rules for every tissue or splice product.

The receptor's biological role is extracellular ligand recognition coupled to
tyrosine phosphorylation and intracellular signaling. The original
PMID:10618369 Methods and structural Results identify a human FGF1–FGFR2IIIc
extracellular complex. Recovered PMID:11390973 Results and Figure 1/2 captions
identify FGF2 contacts in Apert mutant structures, although complete construct
Methods remain unrecovered. Those are evidence-backed FGF-binding refinements.
In contrast, PMID:22726438 identifies GRB2 as the adaptor and FGFR2 as the
receptor: binding an adaptor does not confer its adaptor activity. Its operative
full text remains unavailable, so the source-specific interaction is undecided.

PMID:16844695 was read in bounded original Methods/Results and figure captions.
Human FGFR2IIIc and engineered glycosylation/C278F constructs in MC3T3-E1 and
COS7 cells distinguish surface receptor from retained intracellular pools.
Dimerization and phosphorylation/PLCG1 readouts support the receptor mechanism,
but retention and signaling differ with cell context. These engineered proteins
are not the 17 natural splice products. No figure-pixel or whole-paper reading
claim is made. The original PMID:17959718 Methods instead use mouse gland
explants and mouse FGFR2b–human Fc as a binding probe; that does not establish
endogenous human FGFR2 cell-surface localization in that experiment.

Protein association is not rejected merely because it is non-core or comes from
a large screen. Exact original BioPlex rows (PMID:33961781) and the separate
AP-MS/co-IP versus BioID records in PMID:35384245 support bounded association.
Drug-focused PMID:23597563 and PMID:26267536 also have exact positive protein-pair
NMR records in IntAct, so the previous drug-only objections were unsound; their
original panels remain unread. PMID:25241761 provides proximity-ligation records,
which do not by themselves measure direct affinity. For PMID:35922511, the
author workbooks actually contain the FCER2–FGFR2 target pair. Uncertainty now
concerns specificity: the original screening Methods explicitly discuss FGFRs
as recurrent nonspecific candidates. Network membership and the aggregate
validation rate do not establish pair-specific physiological binding.

All 75 mouse ISS and 11 rat Ensembl contexts have actual same-term donor joins.
Their tissue-specific phenotypes or expression responses remain distinct from
human experimental evidence. A narrow developmental context is not an error
simply because it is non-core. PAINT has eight literal positive IBD joins and
a complete 159-row family assertion census, including 23 negatives. The failed
tree request and capped MSA response leave target ancestry and sequence matching
unverified; no family-negative node is assigned to FGFR2 without that path.
All 58 Reactome references have genuine P21802-family participant joins, including
mutant/fusion models. A PI3K-containing complex or RAS-GEF set does not turn FGFR2
into PI3K or a GEF. Current source-specific details and access limits are indexed
in [the source guide](FGFR2-source-guide.md) and
[the evidence file](FGFR2-source-evidence.yaml).

The core remains receptor-centered. The checked strict is_a/part_of ancestry
returned no ancestor pair among the seven previously listed BP terms. The
embryonic cranial skeleton term was omitted from the revised core because its
specific human source/participation scope remains unresolved, not because it
was shown to be redundant. Broader bone-development and branching/lung contexts
retain curated ortholog support.
Unresolved human localization and soluble-product physiology remain questions,
not new annotations. All 229 source objects, 94 inherited references/findings,
65 inherited quotation associations and immutable source caches are preserved.
No publication quotations were added.
