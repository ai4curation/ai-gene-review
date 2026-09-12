# PRM5 (YIL117C) — curation notes

Journal for the AI GO-annotation review of *Saccharomyces cerevisiae* PRM5 (UniProt P40476,
SGD:S000001379, systematic name YIL117C). PRM5 is an **understudied ("dark") gene**: a
pheromone- and cell-wall-integrity-regulated single-pass membrane protein of **unknown
molecular function and unknown biological role**. The deliverable is an honest
`knowledge_gaps` section plus conservative, domain/orthology-grounded `description` and
`core_functions` — never invented function.

## Identity / provenance

- Standard name PRM5 ("Pheromone-Regulated Membrane protein 5"); systematic YIL117C; verified ORF.
- 318 aa, ~34.7 kDa (UniProt P40476).
- Paralog **YNL058C** (arose from the whole-genome duplication) [SGD locus page, "Paralog: YNL058C (arose from whole genome duplication)"].
- UniProt: `PE 1: Evidence at protein level` (protein identified in MS studies), but this is
  identification-level evidence only; no direct functional assay exists.

## Domain / topology reasoning (from PRM5-uniprot.txt, read inline)

- `FT TRANSMEM 75..98 /note="Helical" /evidence=ECO:0000255` — one predicted TM helix ⇒
  consistent with the UniProt subcellular-location statement `Membrane; Single-pass membrane protein {ECO:0000305}`.
- Large C-terminal (238–318) **disordered / low-complexity** region (MobiDB-lite), with basic-and-acidic
  and polar low-complexity stretches. No catalytic motif, no recognizable enzymatic domain.
- N-terminus (1–60) is Ser/Thr-rich (`...TTSTSS TTTASSSSTI TSVASSSSSL...`), consistent with a
  potential O-glycosylation-prone / membrane-anchored surface region, but this is inference only.
- Pfam `PF28230 (SCY_4732)`; InterPro `IPR051009 (PRM5-like)`; PANTHER `PTHR36089` ("Pheromone-regulated
  membrane protein" / short "PRM"). **The InterPro/PANTHER free-text description for PTHR36089 is
  machine-generated (`is_llm: true`, `is_reviewed_llm: false`) and must NOT be used as evidence of
  function** — it merely restates the family name and the vacuolar-membrane localization of some members.
- Conclusion from domains: **localization (membrane) is defensible; molecular function is NOT
  inferable from sequence.** Single TM + long disordered cytosolic tail is compatible with many roles
  (scaffold, regulatory membrane anchor) but specifies none.

## PANTHER family PTHR36089 context (interpro/panther/PTHR36089/)

The family bundles several *S. cerevisiae* members that share the PRM/vacuolar-membrane fold but
have divergent/unknown functions:
- **PRM5** = P40476 (this gene)
- **YNL058C** = P53947 ("Vacuolar membrane protein YNL058C") — WGD paralog of PRM5
- **CSI2** = Q08054 ("Chitin synthase 3 complex protein CSI2", YOL007C)

Even the better-studied family members carry **ND** (no data) for molecular_function and
biological_process — i.e. the whole family is functionally dark at the MF level.

## Source of the IBA (phylogenetic) localization annotations — verified

PRM5's two IBA annotations propagate from experimentally-localized *S. cerevisiae* paralogs via
the PANTHER tree (QuickGO with/from fields, verified 2026-07-05):

- `GO:0000324 fungal-type vacuole` — IBA (GO_REF:0000033), with/from PANTHER:PTN002188658 | **SGD:S000005367**
- `GO:0005935 cellular bud neck`  — IBA (GO_REF:0000033), with/from PANTHER:PTN002188659 | **SGD:S000005367**

**SGD:S000005367 = CSI2 (YOL007C)** (resolved via SGD backend). QuickGO confirms CSI2 (Q08054) has
**experimental** annotations to both terms: `GO:0000324` (IDA + HDA) and `GO:0005935` (IDA); the
WGD paralog YNL058C (P53947) also has experimental `GO:0000324` (HDA). So the IBA localization
calls on PRM5 are grounded in real experimental localization of close relatives — reasonable
**localization** propagations for a conserved membrane-protein family, though they do not establish
PRM5's own localization directly and do NOT imply any molecular function.

## What is KNOWN about PRM5

1. **Membrane protein.** Single predicted TM helix (UniProt FT TRANSMEM 75..98) → UniProt annotates
   `Membrane; Single-pass membrane protein` (ECO:0000305). Supports `GO:0016020 membrane`
   (IEA, UniProtKB-SubCell SL-0162).
2. **Regulated by two stimuli (INDUCTION, experimental).** UniProt: "Expression is regulated by the
   cell integrity signaling pathway and by pheromone." (ECO:0000269|PubMed:10594829,
   ECO:0000269|PubMed:11062271).
   - CWI/Mpk1–Rlm1 induction: [PMID:10594829 "The cell integrity pathway of Saccharomyces cerevisiae
     monitors cell wall remodelling during growth and differentiation... We identified 25 genes whose
     regulation was altered by Mpk1 activity... All of the regulation detected was mediated by the
     Rlm1 transcription factor"]. (Abstract does not enumerate PRM5 by name — it is one of the Mpk1/Rlm1
     targets in the full dataset; regulation attribution follows UniProt's ECO:0000269 curation.)
   - Pheromone induction: the "PRM" designation comes from Heiman & Walter, who defined 20
     pheromone-regulated membrane-protein (PRM) genes induced >3-fold by α-factor and encoding ≥1
     hydrophobic domain [PMID:11062271 "This parameter narrowed our pool of 54 candidates to 20 genes,
     which we henceforth refer to as PRM genes (pheromone-regulated membrane proteins)."]. That paper
     characterized PRM1 in depth; PRM5 is one of the co-identified PRM set (listed in its Fig. 1 table),
     not individually characterized there.
3. **Post-translational modifications (large-scale MS, experimental identification).**
   - Phosphoserines S129, S279, S282, S288 [PMID:17330950, alpha-factor-arrested phosphoproteome].
   - Ubiquitination at K314 [PMID:22106047, sites of ubiquitin attachment].
   - These establish the protein is expressed and is a substrate of the phospho/ubiquitin machinery
     under mating arrest, but do not define its function.
4. **Deletion phenotype: viable, only subtle large-scale-survey phenotypes** (SGD): decreased
   competitive fitness, decreased oxidative-stress resistance, decreased sporulation efficiency,
   decreased starvation resistance, altered toxin resistance. All from high-throughput surveys; no
   dedicated mechanistic study.

## What is NOT known (the primary deliverable: knowledge gaps)

- **Molecular function: entirely unknown** (SGD/GO = ND; no enzyme motif; family-wide MF is ND).
  Not a `protein binding` situation — there is simply no informative MF term supportable.
- **Biological process: unknown** (GO = ND). It is *induced by* pheromone and CWI signaling, but
  induction ≠ participation; no mating or cell-wall phenotype has been demonstrated for a prm5Δ.
- **Own subcellular localization not directly determined.** Membrane is supported by topology; the
  vacuole/bud-neck IBA calls are paralog-propagations, not direct PRM5 data.
- **No physical partners establishing a pathway.** BioGRID lists interactions but none define function.

## Annotation-by-annotation plan

1. `GO:0000324 fungal-type vacuole` (IBA, is_active_in) — localization propagated from CSI2 (experimental).
   Plausible localization for the family but PRM5's own localization is unverified and this is a
   *component* not function. Keep but mark **non-core** (KEEP_AS_NON_CORE): defensible, not a core
   functional claim, and `is_active_in` overstates certainty for a dark protein.
2. `GO:0005935 cellular bud neck` (IBA, is_active_in) — same provenance (CSI2). CSI2 is a chitin
   synthase-3 complex bud-neck protein; propagation of *its* localization to PRM5 is weaker (function
   diverged; PRM5 is a WGD-era paralog with ND function). Keep as **non-core** (KEEP_AS_NON_CORE),
   noting reduced confidence; do not treat as core.
3. `GO:0016020 membrane` (IEA, located_in) — directly supported by TM prediction/UniProt SubCell.
   The single defensible, sequence-grounded annotation. **ACCEPT.**
4. `GO:0003674 molecular_function` (ND) — correct honest placeholder; MF genuinely unknown. **ACCEPT**
   (the ND root annotation accurately records "no data").
5. `GO:0008150 biological_process` (ND) — likewise the honest placeholder; BP unknown. **ACCEPT.**

`core_functions`: at most a minimal localization statement (integral membrane component); no MF can
be responsibly asserted. `knowledge_gaps` carries the substance.
