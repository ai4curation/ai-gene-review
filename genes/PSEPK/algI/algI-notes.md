# algI curation notes

- Q88ND2 is the syntenic KT2440 AlgI ortholog and retains the exact AlgI family
  and seven-pass inner-membrane architecture.
- P. aeruginosa nonpolar algI deletion yields alginate lacking O-acetyl groups,
  and complementation restores acetylation [PMID:12003941, "each mutant produced
  alginate lacking O-acetyl groups"].
- GO:0051979 is not a descendant of GO:0042121 in the current GO release.
  Therefore the exact acetylation process is added separately rather than used
  as a formal replacement for the broader pathway-context annotation.
- The immediate acetyl donor and transient acceptor remain unresolved; retain
  only the broad acyltransferase molecular function.


## 2026-10-25 cross-species evidence audit

Normal `just fetch-gene PSEPK algI` was run without forcing source replacement. The helper backfilled supporting entities (and algF qualifiers); remote differences in existing source records were reported and preserved. Every pre-existing review row and all its machine-source fields were retained. References to GOA and the derived module were removed from the evidence bibliography because they are annotation/curation outputs, not independent biological support. No matching activity was found for these four accessions in the local GO-CAM index.

Publication caching used the normal pipeline concurrently with provider attempts. PMID:25165982 and PMID:37797696 were read in full. PMID:36494359 was newly fetched with full text. PMID:12003941 and PMID:23779107 currently have abstract-only caches; explicit abstract findings are used, without inventing unreported methods. PMID:31900562 is an abstract plus repository landing-page extract despite legacy full-text metadata; its explicit mutant/stability/pull-down summary is usable, but the cache does not supply full experimental methods.

Bacterial fitness retrieval was attempted with `just fetch-fitness PSEPK algI`. It failed because no local FEBA database or reachable remote source was available; no fitness artifact was written. This is missing data, not evidence of normal fitness or dispensability.

The exact physiological acetyl donor and detailed AlgI→AlgJ→AlgX transfer chemistry remain unresolved. PMID:40171682 is a 2025 review that explicitly says “This full model has yet to be demonstrated experimentally”. Its C-terminal AlgI acyl-shuttle proposal is informed by work on other MBOAT/SGNH systems. Direct Dlt intermediate chemistry cannot be silently reassigned to AlgI. PMID:40821665 is likewise a review, not a new target-specific AlgI assay.

Neither GOA evidence codes nor absence of a foreground gene in a title were used as grounds for rejection. In particular, the P. aeruginosa-titled papers contain direct P. putida construct experiments. Protein interaction evidence supports assembly participation, but no bare protein-binding annotation is added. Hydrolysis of an artificial ester proves catalytic capacity under the assay conditions, not the full physiological transfer reaction.

`just deep-research-falcon PSEPK algI --fallback perplexity-lite` was attempted. Falcon failed with HTTP403 Forbidden; fallback Perplexity failed with HTTP401 insufficient_quota. No successful provider report was generated, and these manual notes are not labeled as provider output. The existing genuine shared OpenScientist project report was reused as literature triage, not direct experimental evidence.

### AlgI conclusions

Q88ND2/PP_1280 is supported as an AlgI-family membrane acyltransferase by curated classification, operon context and P. aeruginosa deletion/complementation. PMID:37797696 names Q88ND2 among AlphaFold inputs, not as purified enzyme used in a direct transfer assay. Keep GO:0016746 acyltransferase activity at the broad inferred level; do not invent an immediate acceptor or claim a measured membrane-translocation mechanism.

UniProt explicitly lists `PANTHER; PTHR13285; ACYLTRANSFERASE` and `PANTHER; PTHR13285:SF23; TEICHOIC ACID D-ALANYLTRANSFERASE`; both official labels were checked in panther.obo. The surprising subfamily name is real membership, not evidence for D-alanine chemistry in AlgI. The narrower target classification is InterPro IPR028362 AlgI; MBOAT PF03062/IPR004299 is shared and not alginate-specific.

The broad biosynthesis row is changed to MODIFY→GO:0051979 as a lateral correction to its demonstrated modification role. This is not claimed to be a descendant refinement: the terms are not in that parent-child relationship. Primary genetics distinguish acetylation from synthesis of the unmodified backbone. The existing NEW acetylation row is retained; no duplicate row is manufactured.

## Independent final QA, 2026-10-25

Reassessed the pre-existing NEW process proposal rather than assuming it was justified. Live exact GO:0051979 QuickGO annotation queries found P. aeruginosa AlgI Q51392 (1), AlgJ Q51393 (2), AlgF Q06062 (2), and A. vinelandii AlgF P70799 (1), all experimental. Pa and Az AlgF are exact same-role organizational-component comparators; AlgI/J are acetyl-processing machinery comparators for the catalytic components. These counts are annotation-convention checks only, not supporting evidence. The term means addition of O-acetyl ester groups to alginate; the proteins perform catalytic or structural machinery work, rather than serving as its polymer substrate. GO:0051979 and GO:0042121 are not ancestor/descendant duplicates. A fresh search of gocams/index.tsv found none of Q88ND0/Q88ND2/Q88ND3/Q88ND4, so there is no cached target model whose different role is being overridden.

Removed the redundant NEW GO:0051979 row because the existing biosynthesis row already proposes that same term via MODIFY. Copied its target-specific rationale and evidence into the replacement decision. This supersedes the prior note retaining every pre-existing proposal: all GOA source rows remain, while the duplicate reviewer-authored proposal does not. No biological coverage is lost.

The live OLS parent lookup for GO:0051979 returned GO:0005976 polysaccharide metabolic process. This classifies modification of a polysaccharide; it does not restrict the participants to a polymer substrate or imply synthesis of the backbone.
