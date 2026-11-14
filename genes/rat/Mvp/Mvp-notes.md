# Mvp (rat, Q62667) review notes

## Deep research

Deep-research providers (falcon, perplexity) have no API keys in this environment and
were not attempted. No `-deep-research-*.md` file exists. The literature search was
done by hand through PubMed E-utilities (esearch + esummary), and hits were cached with
`uv run ai-gene-review fetch-pmid`. The human MVP review (`genes/human/MVP/`) was
reused for framing and for the signalling literature, which is almost entirely human
and mouse.

Queries (PubMed):

- `vault[ti] AND rat[ti]` - found PMID:19150846, PMID:7681830, PMID:15571508, PMID:7525587
- `Kedersha[au] AND Rome[au] AND vault` - found PMID:2943744 (discovery), PMID:1988458,
  PMID:8270627, PMID:1694556, PMID:10477748
- `major vault protein[ti] AND rat` - found PMID:7828886 (rat cDNA), PMID:11349122,
  PMID:10087261, PMID:11727830, PMID:16505994, PMID:16441665
- `vault[ti] AND polyribosome*` and `Mrazek[au] AND vault` - found PMID:25354757
- `Tanaka H[au] AND vault[ti]` - found PMID:18453688, PMID:23695250, PMID:19150846
- `vault[ti] AND cryo-electron`, `vault RNA[ti] AND rat`, `vault[ti] AND (glucocorticoid
  receptor OR PC12)` - context only

Newly cached: PMID:7828886, 2943744, 25354757, 18044992, 18453688, 7681830, 10087261,
11727830, 16505994, 15571508, 1988458.

## Rat-specific evidence

- Discovery: vaults purified from rat liver; p104 (Mvp) dominates [PMID:2943744 "One of
  these (Mr 104,000) greatly predominates, accounting for greater than 70% of the total
  Coomassie Brilliant Blue-staining protein"]. Rat vault RNA is 141 nt, Pol III
  [PMID:7681830 "Vaults are large cytoplasmic ribonucleoprotein particles with a
  sedimentation value of about 150 S"].
- Structure of native rat liver vault, 3.5 A [PMID:19150846 "the cage structure consists
  of a dimer of half-vaults, with each half-vault comprising 39 identical major vault
  protein (MVP) chains"]; 39-fold symmetry [PMID:18453688 "indicated that the particle has
  39-fold dihedral symmetry"]. Earlier models (eightfold, 96 copies; PMID:1988458,
  PMID:18044992, PMID:8270627) are superseded on stoichiometry.
- Rat Mvp alone self-assembles [PMID:11349122 "the expression of the rat MVP alone can
  direct the formation of particles that have biochemical characteristics similar to
  endogenous rat vaults"]; assembly on polyribosomes [PMID:25354757].
- Nuclear pore/envelope association, rat tissue immunogold [PMID:8270627 "Immunogold EM
  confirmed that vaults associate with the nuclear envelope in tissue sections and with
  NPCs of isolated nuclei"].
- Microtubules and neurite tips in rat PC12 cells [PMID:10087261 "In neuritic extensions
  of differentiated PC12 cells, there is an almost complete overlap of the distribution of
  microtubules and vaults"; PMID:16505994].
- Phosphorylated by co-purifying kinases in PC12 cells [PMID:11727830].
- Co-purifies with GR from rat liver cytosol [PMID:16619302] - source of the two IPI
  protein binding rows.
- Induced in reactive microglia after status epilepticus [PMID:15571508].

## Curation decisions (consistent with human MVP)

- Protein binding IPI x2 (GR co-purification): REMOVE (protein-binding policy).
- Identical protein binding (ISO): ACCEPT, backed by rat structure and self-assembly.
- Cytoplasm (IBA, IEA, ISO) and cytosol (ISO): ACCEPT.
- Nucleus (IBA, ISO), nuclear pore (IEA), cytoskeleton, perinuclear region (IEA, ISO):
  KEEP_AS_NON_CORE.
- Signalling rows (signal transduction IBA; intracellular signal transduction, ERBB
  signalling, negative regulation of EGFR signalling, kinase and phosphatase binding ISO):
  KEEP_AS_NON_CORE; no rat-specific signalling data.
- Cell population proliferation (ISO from mouse IMP PMID:15133037): MARK_AS_OVER_ANNOTATED.
- Protein activation cascade (ISO from the same mouse IMP): REMOVE; source defect on
  the mouse row (UniProt-assigned), as in the human review.
- NEW: GO:0005198 structural molecule activity (IDA, PMID:19150846) as core MF;
  GO:1990904 ribonucleoprotein complex (IDA, PMID:2943744).
- Proposed term "vault complex" (same as human).

## Other genes

- `genes/mouse/Mvp/` is still an unreviewed stub (all PENDING); its GO:0072376 IMP row
  carries the same defect recorded here.
