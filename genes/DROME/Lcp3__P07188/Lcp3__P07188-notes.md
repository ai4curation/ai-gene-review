# Lcp3 (P07188) review notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

No ProtNLM2 files or prediction-evidence folders were consulted.

**Scope and folder.** P07188 is the reviewed canonical Swiss-Prot entry for FlyBase FBgn0002534 (Lcp3, CG2043) and carries the FlyBase experimental GO rows. The unreviewed A0A0B4KEF3 record (reviewed separately in `genes/DROME/Lcp3/`) encodes the identical 112-aa polypeptide (`genes/DROME/Lcp3/Lcp3-bioinformatics/RESULTS.md`). Because both accessions share the symbol, this folder uses the `<HOST>__<ACC>` convention (`dl__P15330` precedent), fetched with `just fetch-gene DROME P07188 --alias Lcp3__P07188`. Transfer from P07188 to A0A0B4KEF3 is sequence identity, not homology.

**Deep research.** `just deep-research-falcon DROME Lcp3__P07188 --fallback perplexity-lite` failed on 2026-10-21: Edison API returned 403 at authentication, and the perplexity-lite fallback also failed. Not retried (credential problem, not a timeout). The existing Falcon report for the identical polypeptide (`genes/DROME/Lcp3/Lcp3-deep-research-falcon.md`) was used for context only.

**Evidence actually read (all abstract-only caches).**
- PMID:101231 (Fristrom 1978): urea-soluble proteins of untanned larval cuticle, five major components, at least three encoded by separate structural genes. Does not name LCP-III; attribution rests on the curator's full-text reading plus later sequence matching.
- PMID:6168386 (Snyder 1981): 44D cluster, abundant late-third-instar epidermal expression; three of four abundant genes shown to code for larval cuticle proteins.
- PMID:6817923 (Snyder 1982): protein sequences of four major third-instar cuticle proteins match four 44D genes; each gene encodes a signal peptide. UniProt cites this for Lcp3 partial protein sequence.
- PMID:6441593 (Silvert 1984): larval vs pupal cuticle proteins; major larval proteins < 20 kDa, non-glycosylated.
- PMID:17628275 (Karouzou 2007): genome-wide R&R CPR annotation (source of ISM rows).

**Experimentally established in D. melanogaster for this gene product:** presence as a major protein of third-instar larval cuticle (isolation + protein sequencing), hence GO:0008010 structural constituent of chitin-based larval cuticle and GO:0062129 chitin-based extracellular matrix; epidermal expression in third-instar larvae (cluster-level). **Inferred only:** chitin binding (R&R domain; family-level, demonstrated for other CPRs such as Anopheles proteins per the Falcon report, not for Lcp3); procuticle layer; any loss-of-function phenotype (Beagle TATA-box insertion abolishes protein, no phenotype reported).

**Evolutionary placement.** PANTHER PTHR10380:SF237 with Lcp1, Lcp2, Lcp4, pupal Pcp (D. melanogaster, D. pseudoobscura), D. miranda Lcp orthologs and lobster AMP2-5. The larval qualifier is gene-specific and must not be transferred to the subfamily (agrees with `interpro/panther/PTHR10380/PTHR10380-review.yaml`). No IBA/PAINT rows exist for P07188.

**Decisions.** GO:0005214 IEA -> MODIFY to GO:0008010 (OLS: GO:0008010 is_a GO:0005214). GO:0008010 IDA x2 + ISM: ACCEPT. GO:0062129 IDA x2, IEA, ISM: ACCEPT. GO:0008363 IC (from GO:0008010): KEEP_AS_NON_CORE, as a deposited structural component contributing structure to the cuticle being synthesised; no phenotype claim. GO:0040003 ISM: KEEP_AS_NON_CORE; OLS shows GO:0008363 is not currently a descendant of GO:0040003 (it sits under molting cycle, chitin-based cuticle via GO:0042337, which OLS flags as obsoleted), so this is not entailed and not TOO_GENERAL. No NEW terms: chitin binding raised as a suggested question.

**Unresolved.** Falcon report (citing Fristrom 1986) says Lcp3 transcripts accumulate early in the third instar, whereas Snyder 1981 describes the cluster as abundant in late third instar. Not resolved; description says "third-instar".

Validation: `just validate DROME Lcp3__P07188` passes with no warnings.
