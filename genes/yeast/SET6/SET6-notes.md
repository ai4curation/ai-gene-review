# SET6 (YPL165C / UniProt Q12529) — research notes

Research journal for the GO-annotation review of *Saccharomyces cerevisiae* SET6.
Provenance recorded inline as `[PMID:xxxxx "verbatim quote"]` or `[file:... ]` for the
local bioinformatics analysis.

## One-line summary

SET6 is a **dark** budding-yeast SET-domain protein: a **putative, likely catalytically
competent protein-lysine methyltransferase of the SMYD subfamily** whose **substrate,
in-vivo activity, and biological role are all unknown**. It is the paralog of the
characterized SMYD enzyme Set5.

## What is KNOWN

### Domain architecture / family
- UniProt (Q12529) names it "Potential protein lysine methyltransferase SET6", EC 2.1.1.-,
  373 aa, with a SET domain (residues ~12–338) and assigns it to the "class V-like
  SAM-binding methyltransferase superfamily". PE level 3 ("Inferred from homology"). The
  only experimental FUNCTION note is chemogenomic (see below); there is no methyltransferase
  assay.
- InterPro/PANTHER place SET6 in PANTHER family PTHR12197 ("HISTONE-LYSINE
  N-METHYLTRANSFERASE SMYD"), subfamily SF294 ("POTENTIAL PROTEIN LYSINE METHYLTRANSFERASE
  SET6"); CDD cd20071 SET_SMYD (from the UniProt DR lines). So the family-level signal is
  clearly **SMYD-type SET domain**.
- SET6 and its paralog Set5 are the two yeast SMYD proteins:
  [PMID:31685550 "Saccharomyces cerevisiae contains two SMYD proteins, Set5 and" ... "which
  share structural elements with the mammalian SMYD enzymes."] and
  [PMID:31642774 "Set5, and another member of this sub-group, Set6, are homologous to the
  mammalian SMYD proteins [6], which have been reported to have both histone and non-histone
  targets."].

### Catalytic competence (bioinformatics, this review)
- Local reproducible analysis (`file:yeast/SET6/SET6-bioinformatics/RESULTS.md`) shows the
  SET domain is present and near-complete (hmmsearch vs Pfam PF00856, domain E=6.3e-14,
  residues 23–337, split-SET/SMYD architecture) and, critically, that the invariant
  catalytic/SAM-binding residues are **intact**: the "NHSC" pocket (Asn303-His304-Ser305-
  Cys306) and the C-terminal catalytic Tyr337 are conserved, exactly as in the active
  enzymes Set1/Set2/Set5/SMYD2/SMYD3. In contrast, the two yeast SET proteins that are
  reported to be catalytically dead — **Set3 and Set4** — have the Asn-His replaced by
  Arg-Arg. On primary sequence SET6 therefore groups with the **active** methyltransferases,
  not with the pseudoenzymes. This independently reproduces the literature assertion below.
- SET-domain-restricted identity ranks Set5 first (closest yeast relative), consistent with
  the SMYD ortholog-pair literature.
- SET6 is Cys-rich (17 Cys, 4.6%) in three clusters (an N-terminal CxxC, an internal-insert
  cluster, and a C-terminal post-SET C-x-C...C), the expected SMYD-family zinc-knot/post-SET
  metal-binding architecture — consistent with the RCA zinc-ion-binding annotation.
  A separate canonical MYND zinc finger could not be confirmed (SET6 is 373 aa, shorter than
  Set5 at 526 aa).

### Literature: likely-active but substrate unknown
- The most authoritative statement is from the near-complete yeast methylation-network
  paper: of the yeast SET/7βS/SPOUT methyltransferases, only five are predicted to target
  proteins [PMID:37252976 "Only five methyltransferases are predicted to target proteins:
  Set3, Set4, Set6, Mtf1, and YNL092W."], and of the three plausibly-active ones **Set6 is
  singled out as the most likely genuine protein methyltransferase**: [PMID:37252976 "Of
  these three putative methyltransferases, the most likely protein methyltransferase is
  Set6, as the SET domain invariably methylates proteins."]. The Set3/Set4 contrast is
  explicit: [PMID:37252976 "This is because Set3 and Set4 appear to lack methyltransferase
  activity due to amino acid substitutions at key AdoMet-binding residues"].
- Same paper: SET domain enzymes are protein (not RNA/DNA/metabolite) methyltransferases:
  [PMID:37252976 "SET domain enzymes invariably methylate proteins"].
- Whatever Set6 methylates is not yet identified: [PMID:37252976 "If they are in fact
  protein methyltransferases, they are most likely to target as-yet undiscovered methylation
  sites"]. In Table 2 of that paper Set6 is listed as a putative protein/SET methyltransferase
  with **no assigned substrate and no disqualifying "Notes"** (unlike Set3/Set4, which carry
  active-site-substitution notes).

### The one experimental phenotype
- SET6 (YPL165C) appears in a chemogenomic (heterozygous-deletion) screen: it is "Involved
  in resistance to compounds that target ergosterol biosynthesis, including fenpropimorph,
  dyclonine, and alverine citrate" (UniProt FUNCTION, ECO:0000269|PubMed:14718668). UniProt
  itself hedges that, because deletion has no growth effect absent the compounds, SET6 "is
  more likely to be involved in compound availability" rather than in ergosterol biosynthesis
  per se. The primary paper [PMID:14718668] is a genome-wide small-molecule/deletion screen
  ("alverine citrate"); it is a fitness-profiling readout, not a molecular-function assay, so
  it does not establish a methyltransferase activity, substrate, or a defined biological
  process for SET6.

## What is NOT known (the knowledge gaps)

1. **Substrate** — no protein (histone or non-histone) methylation site attributable to SET6
   has ever been identified. The generic "histone methyltransferase" call is an
   IBA/family-transfer inference; the SMYD family (and human SETD6) act **largely on
   non-histone targets**, so a histone-specific MF is not defensible for SET6.
2. **In-vivo (or in-vitro) activity** — SET6 has never been shown to transfer a methyl group
   to anything; competence is inferred only from sequence-conserved active-site residues.
   "Motif conservation is necessary but not sufficient for activity"
   (`file:yeast/SET6/SET6-bioinformatics/RESULTS.md`).
3. **Biological role** — deletion has no standalone growth phenotype; the only phenotype is
   drug-conditional fitness of uncertain mechanism. Subcellular localization is unmeasured:
   [PMID:31642774 "While the subcellular localization of Set6 is not yet known, Set5 is found
   in both the nucleus and cytoplasm [19], suggesting it is also likely to have non-histone
   substrates."]. The nucleus annotation is IBA family-transfer, not measured for SET6.

## Annotation-by-annotation reasoning (GOA, 7 annotations)

| # | Term | Evid | Ref | Decision | Rationale |
|---|------|------|-----|----------|-----------|
| 1 | GO:0016279 protein-lysine N-methyltransferase activity | IBA | GO_REF:0000033 | KEEP_AS_NON_CORE | Best-supported MF: intact SET/SMYD active site + literature calling Set6 the most-likely genuine protein KMT. Putative, not demonstrated, so non-core. |
| 2 | GO:0042054 histone methyltransferase activity | IBA | GO_REF:0000033 | MARK_AS_OVER_ANNOTATED | Over-specific substrate class. SMYD/SETD6 act largely on non-histone targets; no histone substrate shown for Set6. The lysine-KMT MF (#1) is the defensible level. |
| 3 | GO:0005634 nucleus | IBA | GO_REF:0000033 | KEEP_AS_NON_CORE | Plausible by SMYD family transfer, but Set6 localization is explicitly unmeasured; keep as non-core, low confidence. |
| 4 | GO:0006338 chromatin remodeling | IEA (from GO:0042054) | GO_REF:0000108 | REMOVE | Inter-ontology inference chained off the over-annotated histone-MTase term (#2); no evidence Set6 remodels chromatin. Falls with its parent term. |
| 5 | GO:0008270 zinc ion binding | RCA | PMID:30358795 | KEEP_AS_NON_CORE | Computational (zinc-proteome) prediction, corroborated by the Cys-rich SMYD zinc-knot/post-SET architecture in the bioinformatics analysis. Structural, non-core. |
| 6 | GO:0005575 cellular_component (root) | ND | GO_REF:0000015 | ACCEPT | Root/ND placeholder; accept as-is per GO convention. |
| 7 | GO:0008150 biological_process (root) | ND | GO_REF:0000015 | ACCEPT | Root/ND placeholder; accept as-is per GO convention. |

## Reference triage

- PMID:37252976 (Hamey & Wilkins, PNAS 2023, near-complete yeast methylation network) —
  HIGH; full text; directly adjudicates Set6 as the most-likely genuine yeast protein KMT
  with unknown substrate. VERIFIED.
- PMID:31642774 (Jethmalani & Green, review) — HIGH; SMYD homology, histone/non-histone
  substrate range, unmeasured localization. VERIFIED (full text).
- PMID:31685550 (Jaiswal et al., Set5 SMYD paper) — MEDIUM; establishes Set5/Set6 as the two
  yeast SMYDs (context/paralog). VERIFIED (abstract).
- PMID:30358795 (Wang et al., yeast zinc proteome) — MEDIUM; source of the RCA zinc-binding
  annotation. VERIFIED (abstract; this is the RCA support).
- PMID:14718668 (Giaever et al., chemogenomic profiling) — LOW; source of the only phenotype
  (drug-conditional fitness); does not define molecular function. VERIFIED (abstract).
- file:yeast/SET6/SET6-bioinformatics/RESULTS.md — HIGH; reproducible SET-domain integrity /
  SMYD-family / zinc-architecture analysis.
- GO_REF:0000015 / 0000033 / 0000108 — pipeline references (ND / IBA / inter-ontology IEA).

## Deep research

`just deep-research-falcon yeast SET6 --fallback perplexity-lite` was attempted but timed
out (no report produced); per project policy no fabricated deep-research file was written.
These notes are the manual research journal instead.
