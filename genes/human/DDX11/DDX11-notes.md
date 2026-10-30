# DDX11 curation notes

## 2026-10-17 — initial evidence review

Identity: human HGNC:2736, UniProt Q96FC9. The 87 imported annotation dictionaries and five alternative-product records are preserved. The review contains no NEW assertion. Normal fetched records, publication caches, PAINT data and provider outputs have not been edited. Both genuine automated research attempts failed authentication/quota checks; this is a manual evidence review, not a provider report.

The [evidence guide](DDX11-evidence-guide.md) distinguishes cached abstracts, separately accessed originals, structured database records and unresolved sources. Original-only assay details in reasons are paraphrases, not quotations claimed to occur in abstract caches. The sole supporting-text quotation is the 11-word helicase-direction passage from the cached [2008 biochemical paper](https://pubmed.ncbi.nlm.nih.gov/18499658/).

Supported generic interaction records follow the user's explicit [CLINGEN_MENDELIAN instruction at the fixed source commit](https://github.com/ai4curation/ai-gene-review/blob/e32937e9a43d197137f795d76417027d318843f0/projects/CLINGEN_MENDELIAN.md#curation-instructions): refine a demonstrated partner class where justified; otherwise retain supported associations as non-core. Inaccessible or unresolved source-specific assertions remain undecided. This is a scoped project instruction, not a claim that every repository skill states the same policy.

The core is one directional DNA-helicase activity in the nucleus. Reviewed cohesion and fork-processing assertions remain in their source rows; these processes are not automatically attached to every catalytic experiment. Individual binding assays, complex co-purification and phenotype studies are evaluated at their actual resolution. The three undecided rows concern the original viral E2 assay, the second FUZ dataset and the exosome protein record; none is a claim that the interaction or localization is false.

Product reconstruction establishes sequences of 970, 906, 880, 856 and 288 residues. Historical construct numbering and gene-level antibody assays do not assign activity to all five products. The 2075 antibody epitope from the 2006 Methods matches products 2, 3 and 4, but not displayed product 1 or product 5. This is a literal sequence comparison, not a complete prediction of antibody specificity. HPA metadata also remains gene-level.

The source NOT flag for mitotic cohesin is retained with its metaphase/centromeric context; it is not converted into a positive assertion or an absolute denial of earlier complex association. The historical nucleolar antibody discrepancy is documented alongside independent later localization evidence. No old source cache is rewritten to reconcile those observations.

This initial scientific packet is subject to independent ROOT review and ordinary validation, status inspection and rendering before publication. ROOT owns canonical writes, append-only history scaffolding and remote publication. Legacy workspace content was untouched; no new whole-workspace audit is claimed.

### Independent review refinement

The CONCR-associated RNA-dependent ATPase assertion is retained as non-core. The current term's exact synonyms include RNA-dependent ATPase; the source measures RNA-stimulated ATP turnover. Unresolved coupling does not, by itself, contradict that curator-backed scope. No RNA-helicase activity or separate RNA core is asserted. Explicit reference links were added to nine already-supported rows without adding quotations or changing their judgments.


## 2026-10-17 — source-specific activity and core clarification

This follow-up supersedes earlier retention of the rDNA/CONCR ATP-dependent activity rows: their assays establish ATP turnover without identifying the coupled reaction required by the current GO definitions. The review now uses GO:0016887 for those measurements and retains RNA/DNA stimulation in the reasons. It also preserves the historical positive hybrid-unwinding result through GO:0033677 replacements, without adding a native R-loop process.

Supported directional DNA-helicase refinements retain the original PAINT, domain and TAS provenance. The inspected PAINT node is valid (NO_FAILURE_CORE); target biochemistry supplies precision. MODIFY follows the explicit [project curation instructions](https://github.com/ai4curation/ai-gene-review/blob/a87ae568676c4012ea4abe5393967aeff1b52ae7/projects/CLINGEN_MENDELIAN.md#curation-instructions) and the user's instruction for a sound but overly general term. Repeated source support does not create new coverage.

The single motor core now connects to the already accepted fork-processing and cohesion-establishment processes, with unresolved in-cell substrate and catalytic-versus-association contributions retained as questions. Source-specific locators and limits appear in the [follow-up evidence guide](DDX11-evidence-guide.md#2026-10-17-follow-up-source-locators). All five products, 87 source objects, NOT assertion, eight binding non-core decisions and three inaccessible-source UNDECIDED decisions are unchanged. No NEW annotation or publication quotation was added. Normal-cache access flags remain literal despite separately recovered originals.
