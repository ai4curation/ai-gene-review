# dmg / Q9AGP8 research notes

## 2026-11-06 primary review

Normal fetch created one GO0047866 IEA row; its full payload and both raw-source hashes were frozen before editing in `.cache/module-audit-logs/dimethylglycine-20261106/artgo-dmg/seed-baseline.json`. A genuine default Falcon attempt failed HTTP 403 authentication. No provider report was written; these are manual notes.

Identity is exact: the frozen 830-residue Q9AGP8 protein matches ENA AF329477.3/AAK16482.1 and RCSB 1PJ5 entity 1 at all 830positions. The genomic source is NRRL B-2979. RCSB 3GSI is the D552A mutant covering residues 4–830, expressed through pEH1 in E. coli JM109. Its first three missing residues and the mutation are construct differences, not a corrected native gene model. See identity-provenance.yaml and verify_identity.py.

PMID:11422368 full publisher text distinguishes Arthrobacter globiformis NRRL B-2979 dmg from Arthrobacter sp. 1-IN SoxBDAG. Native/recombinant oxidation consumes oxygen and produces sarcosine/peroxide; purified DMGO excludes sarcosine, choline, glycine betaine, creatine and creatinine as tested substrates. The 26 kb expanded AF329477.3 record contains the distinct dmg2 paralog ABB73054.1/Q2Z1K4 but no identified same-strain SoxBDAG quartet. No additional gene was seeded.

PMID:11926836 (abstract read) supplies stopped-flow evidence for dimethylglycine reduction of the flavin and oxygen-dependent flavin reoxidation. PMID:12912903 (full text read) supplies structural separation of the N-terminal oxidation and C-terminal folate-reacting sites and THF-dependent product measurements. PMID:19369258 (full PMC HTML read independently) uses an engineered E. coli W3GM formaldehyde reporter; D552 variants and C-terminal truncation impair coupling. Its diffusion calculations and lactone-inhibitor preference do not identify the linear/cyclic intermediate conclusively. No claim of native Arthrobacter flux is derived from the reporter.

The existing GO0047866 term is ACCEPT with its conditional formaldehyde output stated explicitly. A proposed MF represents THF-coupled net RHEA45756 rather than fitting this activity to glycine-cleavage aminomethyltransferase or sarcosine oxidase. No additional GO rows or generic binding annotations are proposed. No broad betaine-catabolic BP is manufactured from a reconstructed pathway; exact downstream strain partners remain unassigned.

Official frozen family membership is PTHR43757:SF11, whose official label is SARCOSINE DEHYDROGENASE. That label does not override the negative substrate assay. The distinct dmg2 candidate belongs to SF2. No ancestral PTN was guessed or asserted.

Full acquired article HTML/text and genomic/PDB response files remain in ignored cache. Committed source analysis contains only short exact excerpts and sequence/provenance findings.
