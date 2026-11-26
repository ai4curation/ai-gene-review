# PR6194 additive implementation handoff

This supersedes only the changed files listed in `handoff.json`; all previous handoffs, the read-only triage, raw sources and historical provenance remain intact. Before review documents and their exact texts are in `baseline.json`. `preservation.json` records ordered payload/lifecycle comparisons and exact old/new annotation reviews and term scopes. No commits, staging, push or full-corpus validation were performed.

## Review response

| Finding | Implemented answer |
|---|---|
| Family gain-placement versus loss | Corrected four relevant node reasons. TOO_DEEP concerns where the gain arose, not demonstrated later loss. Original negative rationales based only on other physiological roles, absent assays and putative labels were not restored. BioH/ABHD6 positives and all15 raw assertion payloads remain. Eleven unrelated node objects are exactly unchanged. |
| PTHR36837 coherence and broad scope | MOSTLY_COHERENT; GO0016747 and GO0042621 now SUBFAMILY_ONLY for verified SF5. Actual five-leaf reference branch, independent domain signatures and characterized anchors support common PHA-polymerizing transfer. No chain-length uniformity, native flux, SF4 hydrolase exception or invented ancestral node. |
| PSEPK PhaZ tributyrin | KEEP_AS_NON_CORE→MARK_AS_OVER_ANNOTATED. Positive weak overnight KT2442 activity remains true; physiological function is unresolved. C4 tributyrin is not excluded from the GO reaction definition. |
| PhaZ core granularity | PSEPK core explicitly records KT2442 LC-MS monomer/dimer products and copolymer/strain limitations. This refutes the claim that product sizes were unmeasured in both systems. ECTOL core uses its existing specific proposed activity without inventing a GPo1 oligomer distribution. |
| ECTOL membrane | Retained UNDECIDED with explicit peripheral-bilayer-association definition; no TM helix alone cannot establish absence. |
| PAO1 PhaG biotin comparator | Added normally fetched full PMID36689471. Native dedicated BioH deletion/rescue supports GO0009102 MAOA; exact PhaG methyl-ester activity GO0090499 remains UNDECIDED. Lack of native compensation is not a purified enzyme negative. |
| Nearby evidence presentation | Removed the negative forward-assay limitation from PSEPK PhaG positive core support while retaining it in prose/reference findings. Backfilled ECTOL/PSEAE UniProt sections. PSEPK PhaZ NTR now has immediate genus GO0016788. PAO1 raw EC2.4.1.- defect is recorded under the cited UniProt reference; raw record unchanged. |
| Historical PAO1 NEW evidence code | IC payload retained as explicitly instructed, with no unapproved rewrite or retirement. A separate evidence-code provenance decision remains available; this handoff does not claim the reference is an isolated PAO1 catalytic assay. |

## Limits and integration

The ECTOL PhaZ core now names the proposed molecular function rather than GO0016788, so root must reconcile any module/capacity consumer requiring that GO field. Its actual biology and GO0016788 parent remain intact. No module/checker edit was made here.

A PANTHER MSA was not available from the frozen tree acquisition or the attempted official service endpoint; no alignment/residue-based loss claim is made. The broad SF5 inference uses actual reference topology and independent PhaC signatures. Other families' uncertain mixed substrate branches remain explicit rather than receiving fabricated positive scopes or exceptions. The original AcoC exception archive remains available; the PTHR43798 live exception is unchanged.

Final gene checks pass with five non-blocking warnings: ECTOL process coverage, PAO1 process coverage, PSEPK PhaZ MF coverage, and two unused-provider-reference warnings. They do not justify new rows or treating generated research as primary evidence. Family schema, terms, references, grounding (70 pass/0 fail/0 unresolved) and gene cross-check (3 consistent/0 conflict) pass. All seven new helper histories validate. Initial failed schema placement and the corrected checks are retained in separate logs; no failed result is presented as passing.
