# GABRB1 (human, UniProtKB:P18505) review notes

## 2026-11-17 session

### Data fetch

- `just fetch-gene human GABRB1` first wrote a header-only `GABRB1-goa.tsv`. The QuickGO
  `annotation/search` endpoint returned HTTP 500 whenever `includeFields=taxonName` was
  requested (its internal taxonomy service refused connections). The fetch was re-run through
  a scratch wrapper that dropped only that include field and filled the taxon name for taxon
  9606. The resulting file has 67 rows, which the stub seeded as 66 annotations (one row
  collapses on deduplication). No other change was made to the fetch.

### Deep research

- `just deep-research-falcon human GABRB1 --fallback perplexity-lite` failed. Falcon stopped
  with "Template file not found: templates/gene_research_go_focused.md" (the worktree is a
  sparse checkout without `templates/`), and the perplexity-lite fallback reported "Provider
  'perplexity' not available. Available: openscientist, claude_code". No provider file was
  written. The literature research below was done by hand from cached publications.

### Literature checked

Papers cited by GOA (all cached by `just fetch-gene-pmids`): PMID:16412217, PMID:26950270,
PMID:9039914, PMID:35355020, PMID:33234346, PMID:2465923, PMID:29950725, PMID:39843743,
PMID:2538761. Additional papers cached for this review: PMID:24281383, PMID:16469775,
PMID:11498050, PMID:15174078, PMID:23934111, PMID:27273810, PMID:10449790.

### Molecular function: a GABA-A receptor beta subunit

- Human beta1 was cloned with alpha1 and forms GABA-gated chloride channels in mammalian
  cells [PMID:2465923 "The human subunits display very high levels of sequence identity with
  the corresponding bovine receptor subunits."]
- alpha1beta1gamma2 receptors bind benzodiazepines with high affinity [PMID:2538761
  "coexpression of the gamma 2 subunit with alpha 1 and beta 1 subunits produces"].
- beta1 coassembles with the epsilon subunit [PMID:9039914 "describe a new class of human
  GABA(A) receptor subunit (epsilon) that can"] and with theta [PMID:10449790 "Within the rat
  striatum, this subunit coassembles with alpha2, beta1, and gamma1"].
- alpha3beta1-epsilon and alpha3beta1-theta receptors in Xenopus oocytes were characterised
  for GABA sensitivity and modulator effects [PMID:16412217 "We found 100-fold differences in
  GABA sensitivity between the receptors"].
- UniProt FUNCTION (curated, ECO:0000269 from PMID:10449790, PMID:16412217, PMID:26950270):
  beta subunit of the heteropentameric GABA-gated chloride channel; GABA binding sites at the
  alpha/beta interfaces (by similarity); histamine binding at the beta-beta interface (by
  similarity to P28472).
- Native human brain receptors contain beta1: cryo-EM of alpha1-containing receptors from
  epilepsy surgery tissue [PMID:39843743 "Our study revealed a minimum of 12 distinct
  α1-containing GABAA receptor assemblies, comprising α1, α2, α3, β1, β2, β3, and γ2
  subunits"], including a beta2-alpha1-beta1-alpha2-gamma2 assembly "with γ2 and β1 subunits
  swapping positions", and a beta1-beta1 interface coordinated like the beta3 histamine site.
- PMID:29950725 (alpha1beta2gamma2 structure) and PMID:35355020 (alpha4beta3delta) are
  structures of related receptors, not of beta1-containing receptors; they support GABA-A
  receptor architecture in general. ComplexPortal uses them for its complex-level NAS rows.

### Localization and physiology

- Janve et al. expressed alpha1, beta1 (wild type or F246S) and gamma2L in HEK293T cells and
  measured surface expression by flow cytometry and currents by patch clamp [PMID:26950270
  "GABAA receptor α1 and γ2L subunits were coexpressed with wild-type and/or mutant β3 or β1
  subunits in HEK 293T cells."]. The paper contains no occurrence of "presynaptic"; it does not
  address the presynaptic compartment. So it supports plasma membrane, GABA-gated chloride
  channel activity, GABA-A receptor complex, and GABA signalling, but not GO:0099507
  (ligand-gated channel activity involved in regulation of presynaptic membrane potential).
- Rat thalamic reticular nucleus: fast IPSCs need beta1 [PMID:16469775 "These data show that
  brief, beta(1)-dependent, loreclezole-insensitive IPSCs are present in a subpopulation of RTN
  neurons"]. This is postsynaptic, synaptic GABA-A receptor function in native neurons (rat).
- Mouse Gabrb1 L285R and P228H gain-of-function mutants: spontaneous channel opening,
  increased accumbal tonic current and higher ethanol consumption [PMID:24281383 "The mutation
  causes spontaneous GABA ion channel opening and increases GABA sensitivity of recombinant
  GABAARs, coupled to increased tonic currents in the nucleus accumbens"]. The authors
  speculate that presynaptic beta1 receptors could explain reduced mIPSC frequency ("it is
  conceivable that pre-synaptically located spontaneously-open β1-GABAARs ... would similarly
  influence GABA release"); this is a hypothesis, not a demonstration of presynaptic beta1.

### Disease

- DEE45 (MIM:617153): de novo GABRB1 F246S in an infantile spasms patient from Epi4K
  [PMID:26950270 "Additionally one IS patient had a mutation in the GABAA receptor β1 subunit
  gene (GABRB1(F246S))."]; F246S altered deactivation and produced spontaneous openings in
  HEK cells. A second de novo patient was reported by Lien et al. [PMID:27273810, abstract
  not available in cache; title "A second patient with a De Novo GABRB1 mutation and epileptic
  encephalopathy."]. PMID:23934111 (Epi4K) is the discovery cohort; its cached text mentions
  GABRB1 only in a network figure.

### SynGO provenance problems (checked against QuickGO 2026-11-17)

- Mouse Gabrb1 (UniProtKB:P50571) SynGO rows from PMID:11498050 (GO:0099528, GO:0098685,
  GO:0098982; EXP/IDA/IMP). The paper is a GABA(B1) (Gabbr1) knockout [PMID:11498050 "This
  demonstrates that GABA(B(1)) is an essential component of pre- and postsynaptic GABA(B)
  receptors"]. Human GABRB1 receives GO:0099528 and GO:0098685 by Ensembl projection
  (GO_REF:0000107) and GO:0098982 by UniProt combined IEA (GO_REF:0000120, which also cites
  rat P15431). GO:0007186 on human GABRB1 is a GOC inference from GO:0099528.
- Rat Gabrb1 (UniProtKB:P15431) SynGO rows from PMID:15174078 (GO:0048787 presynaptic active
  zone membrane, GO:0099634 postsynaptic specialization membrane, GO:0098982 GABA-ergic
  synapse). The paper is GABA(B1)/GABA(B2) immunogold in globus pallidus [PMID:15174078 "we use
  pre-embedding immunogold labeling to study the subcellular localization of GABA(B) receptor
  subunits, GABA(B1) and GABA(B2)"]. Human GABRB1 receives GO:0048787 and GO:0099634 by Ensembl
  projection.
- Rat Gabrb1 also has SynGO GO:0098982 and GO:1904315 from PMID:16469775, which is a genuine
  GABA-A beta1 paper, so GABA-ergic synapse and the postsynaptic channel term do not rest on
  the swap alone.
- Mouse Gabbr1 is UniProtKB:Q9WV18 and rat Gabbr1 is UniProtKB:Q9Z0U4 (UniProt REST,
  2026-11-17).

### Open points

- Whether beta1 is present in presynaptic GABA-A receptors anywhere is not established.
- Cell-type distribution of beta1 in human brain is poorly resolved; native structures show
  it is a minority subunit in alpha1-containing receptors from cortex.
