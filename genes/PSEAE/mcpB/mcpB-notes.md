# mcpB (PA0176, Q9I6V6) notes

## Review session 2026-11-05 (PseudoCAP IBA-seed protocol, tier 2)

Fetched with `just fetch-gene PSEAE Q9I6V6 --alias mcpB`; accession matches the
worklist. Reviewed Swiss-Prot entry (MCPB_PSEAE). No deep-research provider was
used. Literature came from the UniProt references; PMID:21255112, PMID:12142407 and
PMID:28167524 were cached with `ai-gene-review fetch-pmid`. NCBI E-utilities and
Europe PMC search were unavailable (errors/503) during this session, so no wider
search was possible. The seed paper PMID:14987771 is abstract-only.

### Identity

- Soluble chemoreceptor; aliases Aer2, Aer-2, TlpG. No transmembrane segment
  [PMID:14987771 "A hydropathy plot of TlpG indicated that hydrophobic membrane-spanning regions are missing in TlpG."];
  soluble when expressed [PMID:21255112 "coli, Aer-2 is stable, soluble, and amenable to structural and functional analyses"].
- Three N-terminal HAMP domains, a heme PAS domain, two C-terminal HAMP domains,
  and an MCP kinase control module ending in GWEEF (UniProt CC DOMAIN; PDB 3LNR).
- Heme and gas sensing [PMID:21255112 "we determined that the Aer-2 PAS domain binds penta-co-ordinated b-type haem"];
  [PMID:28167524 "O2 appeared to be the native Aer2 ligand"]; in E. coli
  [PMID:21255112 "here we show that Aer-2 can interact with the chemotaxis system of Escherichia coli to mediate repellent responses to oxygen, carbon monoxide and nitric oxide"].
- Che2 cluster gene; mutant chemotaxis defect
  [PMID:12142407 "An mcpB mutant was defective in chemotaxis when assayed in dilute rich soft-agar swarm medium or in minimal-medium swarm plates containing any 1 of 60 chemoattractants."].
- Aerotaxis [PMID:14987771 "Mutant strains which contained deletions in the methyl-accepting chemotaxis protein-like genes tlpC and tlpG showed decreased aerotaxis."].

### Annotation decisions

- ACCEPT: chemotaxis (IBA, IEA), cytoplasm (IEA), positive aerotaxis (IMP, CACAO).
- TOO_GENERAL: aerotaxis (IMP, PseudoCAP seed), entailed by positive aerotaxis.
- MODIFY: transmembrane signaling receptor activity (IBA, IEA) -> GO:0038023
  signaling receptor activity (McpB is soluble); signal transduction (IEA) ->
  GO:0035556 intracellular signal transduction.
- REMOVE: plasma membrane (IBA; propagation from transmembrane MCPs to a soluble
  leaf), membrane (IEA; InterPro2GO mapping wrong for this soluble receptor).
- KEEP_AS_NON_CORE: identical protein binding (IPI x2, dimeric structure).
- NEW: heme binding (IDA, PMID:21255112), oxygen sensor activity (IDA, PMID:28167524).
- Counts: ACCEPT 4, TOO_GENERAL 1, MODIFY 3, REMOVE 2, KEEP_AS_NON_CORE 2, NEW 2.

## PseudoCAP IBA-seed assessment

PTN002079588 is a different MCP node from the PTN001280296 chemotaxis node assessed
in genes/PSEAE/pctB/pctB-notes.md (and used by aer); the assessment is therefore
made here. It has 76 leaf IBAs in 12 taxa. Besides the chemotaxis IBD it carries
plasma membrane and transmembrane signaling receptor activity IBDs seeded only by
the E. coli receptors.

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN002079588 | GO:0006935 chemotaxis | 6 | 76 (12 taxa) | GO:0009454 aerotaxis, IMP, PMID:14987771 (PseudoCAP); GO:0052131 positive aerotaxis, IMP, same PMID (CACAO) | SOUND | The abstract states that the tlpG (mcpB) deletion decreases aerotaxis and the aer mcpB double mutant has none; aerotaxis is_a chemotaxis, and a receptor mutant phenotype in the behaviour the receptor drives is the gene's own process. | E. coli Tsr (P02942), Tar (P07017), Trg (P05704), Tap (P07018), Aer (P50466); Tar has IDA/IMP chemotaxis, Trg IMP chemotaxis (QuickGO, 2026-11-05) | Yes; five E. coli chemoreceptors with experimental chemotaxis evidence |

No `source_defects` were recorded. The PseudoCAP row is sound, and the node term
suits an MCP clade. Separate from the seed question: the plasma membrane and
transmembrane signaling receptor activity IBDs at the same node do not apply to
McpB, a soluble leaf that has lost the membrane architecture. Those rows are
handled with REMOVE/MODIFY and `propagation_review`, and raised as a suggested
question (a PAINT loss annotation on this leaf), not as a GO_CENTRAL defect,
because the node-level IBDs are right for the clade.
