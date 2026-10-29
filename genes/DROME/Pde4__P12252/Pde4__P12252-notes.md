# dnc (dunce), P12252, Drosophila melanogaster: review notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

New folder `Pde4__P12252` for the canonical Swiss-Prot entry P12252 (isoform II) of the dnc
locus (FBgn0000479, CG32498). `genes/DROME/Pde4` is keyed to Q9W4S9 (isoforms N/G) of the
same locus. Fetched with `just fetch-gene DROME P12252 --alias Pde4__P12252`; 36 GOA rows.
No ProtNLM2 files or prediction-evidence folders were opened.

### Deep research

`just deep-research-falcon DROME Pde4__P12252 --fallback perplexity-lite` failed: falcon
returned "Failed to authenticate" and the perplexity-lite fallback returned HTTP 401
(insufficient quota). No deep-research file was written. I worked from cached publications
and from classic dnc papers fetched for this review (PMID:6256649, PMID:6265472,
PMID:3025834, PMID:1848082, PMID:818641).

### Evidence established in Drosophila (not inferred)

- cAMP PDE activity: a dnc cDNA expressed in yeast gave cAMP PDEase activity "identical in
  properties to the Drosophila enzyme affected by the dnc mutation" [PMID:1660926].
- Amorphic alleles (dunceM14, M11, ML) "completely lack the cAMP-specific phosphodiesterase"
  and "exhibit extremely high levels of cAMP" [PMID:6265472].
- dunce+ is the structural gene for a PDE, by sequence homology [PMID:3025834].
- The protein is concentrated in mushroom-body neuropil; the RNA is enriched in Kenyon-cell
  perikarya [PMID:1848082].
- Behavioural and physiological phenotypes: olfactory learning [PMID:818641, PMID:16135747],
  aversive larval conditioning [PMID:19158309], ARM abolished in dnc1, with dnc acting in
  Kenyon cells and antennal-lobe local neurons [PMID:23197709], increased synaptic excitation
  onto embryonic motoneurons [PMID:14507965], enhanced NMJ arborization [PMID:14960616].

### Evolutionary grounding

- UniProt: "Belongs to the cyclic nucleotide phosphodiesterase family. PDE4 subfamily."
  PANTHER PTHR11347. The task brief places the locus in PTHR11347:SF219 via Q9W4T4;
  `interpro/panther/panther.obo` gives SF219 the name "CAMP-SPECIFIC 3',5'-CYCLIC
  PHOSPHODIESTERASE, ISOFORM I".
- PAINT (`interpro/panther/PTHR11347/PTHR11347-paint.tsv`): node PTN001682918 carries IBDs for
  GO:0004115 (FB:FBgn0000479, i.e. dnc, is a seed), GO:0047555 cGMP PDE and GO:0141162
  negative regulation of cAMP/PKA signal transduction. This is a deep node that includes
  PDE families with cGMP preference. P12252 itself has no IBA rows in GOA.
- The cGMP IBD on the same node does not fit dnc, whose dnc-dependent enzyme is
  cAMP-specific [PMID:6265472]. I did not propose cGMP PDE activity. I raised it as a
  suggested question about pruning the node.
- P12252 and Q9W4S9 share an identical 614-residue C-terminal block, including every
  catalytic and metal-binding residue (existing analysis
  `genes/DROME/Pde4/Pde4-bioinformatics/RESULTS.md`, cited, not modified).

### Decisions

- MF: GO:0004115 is ACCEPTED (EXP, IEA, ISS). GO:0004114 and GO:0008081 go to MODIFY → GO:0004115.
- GO:0006198 cAMP catabolic process is ACCEPTED, because the enzyme performs the step.
- GO:0007165 signal transduction goes to MODIFY → GO:0141162. This matches the PAINT IBD at
  PTN001682918 and is used in core_functions.
- GO:0007268 chemical synaptic transmission (IEA and 2 IMP rows) goes to MODIFY → GO:0050804
  modulation of chemical synaptic transmission. dnc modulates transmission through cAMP and
  performs no step of it.
- learning goes to MODIFY → olfactory learning, and memory goes to MODIFY → short-term memory.
  These are the specific terms the assays support. Other behavioural terms (associative and
  olfactory learning, STM, ARM, conditioned taste aversion, thermosensory, courtship, mating,
  circadian, nonassociative learning) are KEEP_AS_NON_CORE. They are organismal readouts of
  cAMP hydrolysis, and I deferred to the FlyBase curators for TAS reviews whose abstracts I
  could not check.
- GO:0048675 axon extension is MARK_AS_OVER_ANNOTATED. It is an indirect, sign-reversed
  NMJ-arborization phenotype.
- GO:0045202 synapse (inter-ontology IEA) is KEEP_AS_NON_CORE. It is plausible from the
  neuropil enrichment, but synapse-specific localization has not been shown.
- No NEW annotations. Female fertility and other phenotypes were deliberately not added as
  process participation.
