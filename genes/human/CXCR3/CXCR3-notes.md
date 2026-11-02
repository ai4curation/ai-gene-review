# CXCR3 notes


## 2026-09-08 paired human–horse review



CXCR3 is a seven-transmembrane chemokine receptor that recognizes CXCL9, CXCL10 and CXCL11 and coordinates lymphocyte recruitment through G-protein signaling. Human alternative isoforms differ in ligand recognition and downstream growth responses; CXCR3-B also recognizes CXCL4 and mediates angiostatic responses.

## Isoforms and ligand specificity

CXCR3-A and CXCR3-B share the seven-transmembrane receptor core but differ at the N terminus and in signaling behavior. In the directly inspected Lasagni study, CXCR3-A supports cell survival/proliferation, whereas CXCR3-B supports endothelial growth inhibition and apoptosis; CXCL4 preferentially binds the B isoform. The paper explicitly includes a negative competition panel containing CCL3, CCL4 and CCL5/RANTES. That experiment is decisive against treating the named ligand list in the horse model output as established. It does not prove that every conceivable CC ligand fails to interact with every CXCR3 isoform. The C-C receptor/binding IBA annotations require tracing the curated ancestral claim and its actual experimental grounding, not counting donor proteins.

## Decisive inspected evidence

From [PMID:12782716](https://pubmed.ncbi.nlm.nih.gov/12782716/):

> Human microvascular endothelial cell line-1 (HMEC-1), transfected with either the known CXCR3 (renamed CXCR3-A) or CXCR3-B, bound CXCL9, CXCL10, and CXCL11, whereas CXCL4 showed high affinity only for CXCR3-B.

## Evidence inventory

- [PMID:12782716: An alternatively spliced variant of CXCR3 mediates the inhibition of endothelial cell growth induced by IP-10, Mig, and I-TAC, and acts as functional receptor for platelet factor 4.](https://pubmed.ncbi.nlm.nih.gov/12782716/). [DOI:10.1084/jem.20021897](https://doi.org/10.1084/jem.20021897). Full text is available in the repository cache.

## Transfer to the selected horse protein

The exact target is [A0A9L0T1D1](https://www.uniprot.org/uniprotkb/A0A9L0T1D1/entry), not an arbitrary horse record with a matching name. The reproducible [paired-sequence analysis](../../HORSE/CXCR3/CXCR3-bioinformatics/RESULTS.md) records identity, coverage and internal gaps. It supports homology but is not a reciprocal orthology test. Molecular properties are transferred only with the relevant domain, targeting and paralog constraints. The prediction-time sequence is not independently verified.

## Open evidence questions

The following annotation scopes need source-specific follow-up: C-C chemokine binding, C-C chemokine receptor activity, cell adhesion, cytoplasm, protein binding, regulation of cell adhesion, signaling receptor activity. Experimental annotations are not removed merely because a cached abstract omits the gene or a specific assay. High-throughput protein-binding rows require their actual partner or complex context before replacement with an informative molecular function.


Research provenance: external Falcon/Edison was attempted with Perplexity fallback. Some requests returned HTTP 429 and fallback returned insufficient-quota HTTP 401; successful external reports are preserved separately. Primary-source manual synthesis is explicitly labeled manual where no external report was available.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

Scope: every existing annotation in `CXCR3-ai-review.yaml` was re-examined against the cached
literature, the reviewed UniProt record (P49682) and the PANTHER/PAINT evidence. No ProtNLM2
output was opened or used. Deep research with falcon was attempted
(`just deep-research-falcon human CXCR3 --fallback perplexity-lite`); both the falcon run and the
perplexity-lite fallback timed out at 600 s, so no new `-deep-research-*.md` file was produced and
the review rests on primary literature read directly. Six publications cited by UniProt but absent
from the cache were fetched (PMID:16847335 and PMID:19151743 with full text; PMID:18174362,
PMID:23121557, PMID:10201891, PMID:24469069 abstract-only).

### Identity

P49682 is the canonical, reviewed UniProt entry for human CXCR3: 368 aa, seven transmembrane
segments (TOPO/TRANSMEM 54–321), extracellular N terminus 1–53 carrying sulfated Tyr-27 and Tyr-29
and N-glycosylation at Asn-22/Asn-32, and the conserved class A disulfide Cys124–Cys203. It is not a
fragment or an alternative gene model. Isoform 1 (CXCR3-A) is the displayed sequence; isoform 2
(CXCR3-B, VSP_015684) adds an extended N terminus, isoform 3 (CXCR3-alt, VSP_015685) is an
exon-skipping truncation. Several GOA rows are isoform-2-specific and are marked as such.

### The C-C chemokine rows are wrong for the human protein

Four rows assert CC-chemokine recognition: an IBA pair (`GO:0016493` C-C chemokine receptor
activity, `GO:0019957` C-C chemokine binding) from PAINT node PANTHER:PTN001628461, plus an IDA row
for `GO:0016493` citing Lasagni et al. and recorded in GO-CAM `5fce9b7300001616`
(SPModule-PGRP1-S100A4), where the CXCR3 node sits next to a CCR5 node with the same term.

The node placement itself is not in dispute: human CXCR3 is in PANTHER subfamily PTHR10489:SF671,
inside the clade under PTN001628461 whose other descendants include CCR1/CCR5/CCR6 and the MGI *Ccr*
genes, and the IBA follows mechanically. What does not hold is the ligand class, which diverged
within that clade, and three independent experiments say so for this gene product:

- [PMID:9064356 "but does not recognize the CXC-chemokines IL-8, GRO alpha, NAP-2, GCP-2. ENA78, PF4,
  the CC-chemokines MCP-1, MCP-2, MCP-3, MCP-4, MIP-1 alpha, MIP-1 beta. RANTES, 1309, eotaxin, nor
  lymphotactin"] — the original cloning paper.
- [PMID:12782716 "CXCR3-B did not react with any of the other 17 chemokines tested, including CCL21"]
  — full text read; the competition panel included CCL1, CCL2, CCL3, CCL4, CCL5, CCL11, CCL17,
  CCL19, CCL21, CCL22 and CCL25.
- [PMID:10201891 "human CC chemokine 6Ckine is not a ligand for the human or mouse CXC chemokine
  receptor CXCR3"] — CCL21 is the one CC chemokine seriously proposed as a CXCR3 agonist, and it
  works on mouse but not human CXCR3. UniProt curates this as a CAUTION.

Both IBA rows are therefore REMOVE with a `propagation_review` of root cause PROPAGATION_BAD /
FUNCTIONAL_DIVERGENCE; the IDA row is MODIFY to `GO:0016494` C-X-C chemokine receptor activity,
which also means the GO-CAM activity node should be retyped. The ligand-class difference is a
distributed N-terminal and extracellular-loop property (the sulfotyrosines Y27/Y29 among others),
not a point substitution, so it is recorded as `residue_claims_not_applicable` rather than as a
residue claim.

### Other substantive changes from the previous version

- Every `UNDECIDED` row was resolved. The seven bare `GO:0005515` rows are now policy-compliant:
  the CXCR4 row becomes `GO:0001664` G protein-coupled receptor binding (CXCR3–CXCR4 heteromers by
  co-IP, TR-FRET and BRET, [PMID:23170857]); the three HuRI rows and the three GPCR–RAMP screen rows
  are REMOVE as uninformative, which does not assert the interactions are false.
- `GO:0005737` cytoplasm (TAS, PMID:10903743) is MARK_AS_OVER_ANNOTATED: the cited work shows CXCR3
  staining on infiltrating T cells, and the protein is a seven-pass plasma membrane receptor.
- `GO:0045944` positive regulation of transcription by RNA Pol II (IDA, isoform 2) is
  MARK_AS_OVER_ANNOTATED: the observation is a p21 mRNA rise several steps downstream of receptor
  activation [PMID:12782716 "CXCL4 significantly up-regulated p21 mRNA transcription in CXCR3-B
  transfectants"]; the receptor performs none of the work of transcription.
- `GO:0007155` cell adhesion is MODIFY to `GO:0030155` regulation of cell adhesion: CXCR3 ligands
  up-regulate integrins and induce adhesion *through* CXCR3 signaling [PMID:10942362 "gamma IP-10 and
  Mig also induced GM-CSF-stimulated CD34(+) progenitor adhesion and aggregation by means of CXCR3"],
  which is inside-out regulation, not participation in adhesion.
- `GO:0002685` regulation of leukocyte migration is MODIFY to `GO:0010818` T cell chemotaxis for the
  same reason in the other direction: the chemoattractant receptor is a participant in chemotaxis,
  not a regulator of someone else's migration.
- The generic terms `GO:0004930`, `GO:0004950`, `GO:0006935`, `GO:0007166`, `GO:0007186`,
  `GO:0016020`, `GO:0019956`, `GO:0038023` and `GO:0060326` are MODIFY to the specific descendants
  the gene already carries (`GO:0016494`, `GO:0010818`, `GO:0048245`, `GO:0070098`, `GO:0005886`,
  `GO:0019958`), per the "correct but general terms are MODIFY" rule.
- The calcium rows are split: `GO:0007204` positive regulation of cytosolic calcium is ACCEPTed
  (directly shown, and lost when R216 is mutated [PMID:16847335 "residue R216 in the second
  extracellular loop is required for CXCR3-mediated chemotaxis and calcium mobilization"]), while
  `GO:0019722` calcium-mediated signaling is kept as non-core, because CXCL13 drives CXCR3-dependent
  chemotaxis without a calcium flux [PMID:11554781 "BCA-1 does not induce a calcium flux"].
- The isoform-2 angiostatic rows (`GO:0001937`, `GO:0016525`, `GO:0007189`, `GO:1900119`) stay
  KEEP_AS_NON_CORE. `core_functions` therefore carries one entry, the canonical CXCL9/10/11 receptor
  driving Gi-dependent calcium mobilization and T cell chemotaxis; CXCR3-B biology is described in
  the gene description and raised in `suggested_questions`.
- `GO:0009986` cell surface (IDA, PMID:20608915) is ACCEPTed while flagging that the cached record is
  abstract-only and its abstract is about CCR3 as a basophil marker. Per CLAUDE.md this is deferred to
  the curator who read the full text, not removed; the claim itself is well supported elsewhere.

### Family and module context

The PANTHER family review `interpro/panther/PTHR10489/PTHR10489-review.yaml` places human CXCR3 in
PTHR10489:SF671 as the family's reference protein and calls the family HETEROGENEOUS, with
`GO:0016494` scope UNRESOLVED at family level. That agrees with this review: no disagreement about
subfamily placement. The review's own text ("CXCR3 recognizes C-X-C chemokines, but other branches
recognize C-C or XC ligands") is the family-level statement of exactly the argument used here
against the inherited C-C rows.

`modules/chemokine_signaling.yaml` covers the chemokine-receptor-to-Gi-to-migration module and
mentions CXCR3 in its deep-research companion, but CXCR3 is not one of its represented parts; no
module was created or edited. GO-CAM `gocams/5fce9b7300001616` contains CXCR3 as noted above.

### Next relative to review

Mouse Cxcr3 (UniProtKB:O88410, MGI), same PANTHER subfamily PTHR10489:SF671 (confirmed in
`interpro/panther/PTHR10489/PTHR10489-entries.csv`) and the 1:1 ortholog. It has no review in the
repo. It is the right next target because the human/mouse ligand difference (CCL21 acts on mouse but
not human CXCR3) is the pivot of the C-C chemokine question raised here, and because the mouse gene
carries the knockout immunology that human work cannot supply.
