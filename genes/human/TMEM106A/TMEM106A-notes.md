# TMEM106A (Transmembrane protein 106A) research notes

UniProt: Q96A25 (T106A_HUMAN), 262 aa. HGNC symbol TMEM106A.
Topology: type II single-pass transmembrane protein; TM helix at residues 95-115 (so a
short N-terminal cytoplasmic region and a large C-terminal lumenal/extracellular domain).
Family: TMEM106 family (PANTHER PTHR28556; family named after the better-studied paralog
TMEM106B). Paralogs: TMEM106B (lysosomal membrane protein implicated in FTD/hypomyelinating
leukodystrophy) and TMEM106C.

## Summary of function

TMEM106A is a plasma-membrane type II transmembrane protein best characterized as a
positive regulator of macrophage activation and as a candidate tumor suppressor that is
epigenetically silenced (promoter hypermethylation) in several carcinomas.

1. **Macrophage activation / M1 polarization.** TMEM106A activates macrophages and
   polarizes them toward an M1-like phenotype via MAPK and NF-κB signaling. It up-regulates
   CD80, CD86, CD69 and MHC class II on macrophages and induces pro-inflammatory mediators
   (TNF, IL1B, IL6, CCL2, nitric oxide). This is the conserved family function, established
   in the mouse ortholog (UniProtKB:Q8VC04) and transferred to human by similarity
   [UniProt FUNCTION, ECO:0000250|UniProtKB:Q8VC04]. This underlies the
   macrophage activation (GO:0042116) and innate-immunity annotations.

2. **Tumor-suppressor / anti-proliferative activity.** TMEM106A is frequently silenced by
   promoter methylation in gastric, renal and lung cancers; re-expression inhibits
   proliferation, migration and invasion and induces apoptosis.
   - Renal cancer: "TMEM106a is a Novel Tumor Suppressor in Human Renal Cancer";
     TMEM106a overexpression suppresses growth and migration; described as "a conserved
     type II transmembrane protein which is a key factor to regulate macrophage
     activation" whose inactivation in gastric cancer is associated with poor prognosis
     [PMID:29131025, abstract only].
   - Lung (NSCLC): "TMEM106A inhibits cell proliferation, migration, and induces apoptosis
     of lung cancer cells"; overexpression represses EMT (↑E-cadherin, ↓N-cadherin,
     ↓vimentin) and suppresses PI3K/Akt/NF-κB signaling [PMID:30456879, abstract only].

## Subcellular location

- Cell membrane; single-pass membrane protein [UniProt SUBCELLULAR LOCATION,
  ECO:0000250|UniProtKB:Q8VC04 + ECO:0000255]. Plasma-membrane annotations (GO:0005886,
  ISS/IEA) are consistent.
- **Lysosomal membrane (GO:0005765, IBA) is very likely a paralog-derived
  over-propagation.** The TMEM106 family PAINT node carries "lysosomal membrane" because
  the paralog TMEM106B is a well-characterized lysosomal membrane protein. TMEM106A itself
  is curated to the cell/plasma membrane by UniProt, and its documented function
  (macrophage-surface activation) operates at the cell surface, i.e. target-specific
  evidence of divergent localization. Treat the lysosomal-membrane IBA cautiously
  (non-core / over-annotated), not as a core location.

## Tissue expression

Expressed in renal cells and epithelial cells at protein level [UniProt TISSUE
SPECIFICITY; PMID:29131025, PMID:30456879].

## GOA annotation orientation

- GO:0042116 macrophage activation (IBA/IEA/ISS, involved_in) — CORE process.
- GO:0035556 intracellular signal transduction (IEA/ISS) — the MAPK/NF-κB signaling it
  drives; correct but general; supporting/non-core.
- GO:0005886 plasma membrane (IEA/ISS) — ACCEPT, matches UniProt curated location.
- GO:0005765 lysosomal membrane (IBA) — likely paralog over-propagation (see above).
- GO:0005515 protein binding (IPI ×2) — from high-throughput interactome screens
  (PMID:32296183 HuRI; PMID:33961781 BioPlex). Uninformative per project guidelines;
  non-core.

## References

- PMID:29131025 — Wu et al., Kidney Blood Press Res 2017: TMEM106a tumor suppressor in
  renal cancer; notes its role as key regulator of macrophage activation. (abstract only)
- PMID:30456879 — Liu & Zhu, J Cell Biochem 2019: TMEM106A tumor suppressor in NSCLC;
  represses EMT and PI3K/Akt/NF-κB. (abstract only)
- PMID:32296183 — Luck et al., Nature 2020 (HuRI reference interactome). Interactome IPI.
- PMID:33961781 — Huttlin et al., Cell 2021 (BioPlex). Interactome IPI.
- Mouse ortholog UniProtKB:Q8VC04 — source of the "by similarity" macrophage-activation
  and localization curation.
