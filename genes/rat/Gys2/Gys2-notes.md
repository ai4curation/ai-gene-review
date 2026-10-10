# Gys2 review notes

## Evidence summary
- [UniProtKB:P17625] UniProt describes Gys2 as extending glycogen primers by transferring glucose from UDP-glucose to the non-reducing end of alpha-1,4-glucan.
- [PMID:1731614] UniProt cites this publication for the glycogen synthase EC reaction and phosphorylation-dependent regulation.

## Curation decisions
- Core function: liver glycogen synthase (alpha-1,4-glucan glucosyltransferase (UDP-glucose donor) activity, GO:0004373).
- Specific catalytic activities and direct metabolic processes were accepted.
- Broad parent, localization, binding, and stimulus-response annotations were modified, kept non-core, or marked over-annotated according to support.

## Re-review 2026-10-10

- GOA refresh added two ISO rows (GO_REF:0000121) donor-split from human GYS2 (UniProtKB:P54840): GO:0004373 alpha-1,4-glucan glucosyltransferase (UDP-glucose donor) activity and GO:0005978 glycogen biosynthetic process. Both ACCEPT, consistent with the existing mouse-donor (MGI:2385254) ISO rows and the rat IDA rows [UniProtKB:P17625 "In this context, glycogen synthase transfers the glycosyl residue from UDP-Glc to the non-reducing end of alpha-1,4-glucan."]. No rows retired.
- GO:0005536 D-glucose binding (IDA, PMID:6096366): KEEP_AS_NON_CORE -> UNDECIDED. The cached record is abstract-only and the abstract reports only a cellular effect of glucose on cAMP-kinase sensitivity of glycogen synthase in hepatocytes [PMID:6096366 "Glucose (10 to 40 mM) increased the sensitivity of glycogen synthase to (Rp)-cAMPS inhibition of cAMP-dependent protein kinase"], not direct glucose binding; the established allosteric ligand is glucose-6-phosphate [UniProtKB:P17625 "Allosteric activation by glucose-6-phosphate"].
- GO:0009749 response to glucose (IDA, PMID:9003423) left as MARK_AS_OVER_ANNOTATED: the evidence is glucose-induced relocalization of the enzyme to the cell cortex, a consequence of the stimulus rather than a demonstrated role of Gys2 in a cellular response program.
- Description rewritten as standalone biology (removed review commentary). UniProt quotes still resolve (the refreshed flat file retains DR GO lines for this entry).
- Open question: does any full-text evidence show direct D-glucose binding by liver glycogen synthase (as distinct from glucose-6-phosphate)?
