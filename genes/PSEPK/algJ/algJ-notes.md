# algJ curation notes

- PMID:25165982 directly crystallized the soluble domain of KT2440 AlgJ/Q88ND3
  (PpAlgJ75-370; PDB 4O8V), providing target-specific structural evidence.
- P. aeruginosa algJ deletion produces non-acetylated alginate and is rescued by
  complementation [PMID:12003941, "each mutant produced alginate lacking
  O-acetyl groups"].
- AlgJ has acetylesterase activity in vitro, but it binds polymannuronate weakly
  or not detectably and its physiological relay substrate remains unknown
  [PMID:25165982, "AlgJ exhibits either weak or no detectable polymer binding"].
- Because the in-vivo reaction is unresolved, the review adds the exact
  acetylation process without assigning a speculative hydrolase or transferase
  molecular function.


## 2026-10-25 cross-species evidence audit

Normal `just fetch-gene PSEPK algJ` was run without forcing source replacement. The helper backfilled supporting entities (and algF qualifiers); remote differences in existing source records were reported and preserved. Every pre-existing review row and all its machine-source fields were retained. References to GOA and the derived module were removed from the evidence bibliography because they are annotation/curation outputs, not independent biological support. No matching activity was found for these four accessions in the local GO-CAM index.

Publication caching used the normal pipeline concurrently with provider attempts. PMID:25165982 and PMID:37797696 were read in full. PMID:36494359 was newly fetched with full text. PMID:12003941 and PMID:23779107 currently have abstract-only caches; explicit abstract findings are used, without inventing unreported methods. PMID:31900562 is an abstract plus repository landing-page extract despite legacy full-text metadata; its explicit mutant/stability/pull-down summary is usable, but the cache does not supply full experimental methods.

Bacterial fitness retrieval was attempted with `just fetch-fitness PSEPK algJ`. It failed because no local FEBA database or reachable remote source was available; no fitness artifact was written. This is missing data, not evidence of normal fitness or dispensability.

The exact physiological acetyl donor and detailed AlgI→AlgJ→AlgX transfer chemistry remain unresolved. PMID:40171682 is a 2025 review that explicitly says “This full model has yet to be demonstrated experimentally”. Its C-terminal AlgI acyl-shuttle proposal is informed by work on other MBOAT/SGNH systems. Direct Dlt intermediate chemistry cannot be silently reassigned to AlgI. PMID:40821665 is likewise a review, not a new target-specific AlgI assay.

Neither GOA evidence codes nor absence of a foreground gene in a title were used as grounds for rejection. In particular, the P. aeruginosa-titled papers contain direct P. putida construct experiments. Protein interaction evidence supports assembly participation, but no bare protein-binding annotation is added. Hydrolysis of an artificial ester proves catalytic capacity under the assay conditions, not the full physiological transfer reaction.

`just deep-research-falcon PSEPK algJ --fallback perplexity-lite` was attempted. Falcon failed with HTTP403 Forbidden; fallback Perplexity failed with HTTP401 insufficient_quota. No successful provider report was generated, and these manual notes are not labeled as provider output. The existing genuine shared OpenScientist project report was reused as literature triage, not direct experimental evidence.

### AlgJ conclusions

PMID:25165982 directly examines KT2440 Q88ND3 (PpAlgJ75–370; PDB4O8V). Methods name KT2440; Figure3's “PpAlgJ: P. aeruginosa … Q88ND3” is an internal species-label typo, not evidence that the target was unassayed. Both PaAlgJ79–379 and PpAlgJ75–370 hydrolyzed 3-carboxyumbelliferyl acetate. The Pp D190/H192/S288 substitutions reduced activity by approximately80%; the corresponding Pa catalytic residues are D193/H195/S297. This confirms surrogate-substrate hydrolysis, without identifying the physiological acetyl-transfer donor or acceptor.

PMID:37797696 directly measures binding of PpAlgJ75–370 to PpAlgF (Kd86±12µM). AlgJ–AlgX binding alone was too weak for reliable fitting. Direct mannuronate-binding assays in PMID:25165982 used PaAlgJ79–379, not the Pp construct; their negative/weak result is not a direct Pp measurement.

Curated family/domain assignments are AlgJ IPR034657, SGNH-like IPR031811 and PF16822 ALGX; the shared SGNH domain alone does not distinguish AlgJ from terminal AlgX. No PANTHER cross-reference is in the fetched record. Physiological transfer chemistry remains a BIOLOGY gap; no unsupported transferase MF is invented. The biosynthesis row is corrected laterally to acetylation, explicitly without claiming an ontology descendant relationship.

## Independent final QA, 2026-10-25

Reassessed the pre-existing NEW process proposal rather than assuming it was justified. Live exact GO:0051979 QuickGO annotation queries found P. aeruginosa AlgI Q51392 (1), AlgJ Q51393 (2), AlgF Q06062 (2), and A. vinelandii AlgF P70799 (1), all experimental. Pa and Az AlgF are exact same-role organizational-component comparators; AlgI/J are acetyl-processing machinery comparators for the catalytic components. These counts are annotation-convention checks only, not supporting evidence. The term means addition of O-acetyl ester groups to alginate; the proteins perform catalytic or structural machinery work, rather than serving as its polymer substrate. GO:0051979 and GO:0042121 are not ancestor/descendant duplicates. A fresh search of gocams/index.tsv found none of Q88ND0/Q88ND2/Q88ND3/Q88ND4, so there is no cached target model whose different role is being overridden.

Removed the redundant NEW GO:0051979 row because the existing biosynthesis row already proposes that same term via MODIFY. Copied its target-specific rationale and evidence into the replacement decision. This supersedes the prior note retaining every pre-existing proposal: all GOA source rows remain, while the duplicate reviewer-authored proposal does not. No biological coverage is lost.

The live OLS parent lookup for GO:0051979 returned GO:0005976 polysaccharide metabolic process. This classifies modification of a polysaccharide; it does not restrict the participants to a polymer substrate or imply synthesis of the backbone.
