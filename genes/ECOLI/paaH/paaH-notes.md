# paaH (P76083) notes, E. coli K-12

## Deep research

`just deep-research ECOLI paaH --provider falcon` was attempted on 2026-10-23 and failed
("Exception: Failed to authenticate"; all providers failed). No deep-research file exists;
the review is built from cached literature and the UniProt record.

## Function

- E. coli PaaH (the paper used the E. coli protein) is an NAD+-dependent 3-hydroxyadipyl-CoA dehydrogenase
  [PMID:20660314 "Recombinant enzymes from Escherichia coli (PaaZ, PaaH) or Pseudomonas sp. strain Y2 (PaaABC(D)E, PaaG, PaaJ, PaaF) were tagged"]
  [PMID:20660314 "we added purified mbp-tagged PaaH to enzymatically produced 3-hydroxyadipyl-CoA. We observed the formation of NADH, succinyl-CoA, and acetyl-CoA in the presence of CoA, NAD + , and PaaJ"]
  [PMID:20660314 "3-hydroxyadipyl-CoA dehydrogenase forming 3-oxoadipyl-CoA"]
  Stereospecificity was only inferred ("probably (S)-3-specific").
- E. coli paaH deletion mutant cannot grow on phenylacetate and accumulates 3-hydroxyadipate
  [PMID:12846838 "Incubation of the paaF and paaH mutants with phenylacetate yielded delta3-dehydroadipate and 3-hydroxyadipate, respectively."]
- PaaH does not form a FadBA-like complex with PaaF/PaaJ
  [PMID:22961985 "No complex between PaaF, PaaH, and PaaJ, equivalent to the fatty acid β-oxidation complex, was detected."]
- E. coli PaaH crystal structure: PDB 3MOG [PMID:22961985 "E. coli PaaH (Protein Data Bank code 3MOG)"]

## Curation decisions

- GO:0008691 3-hydroxybutyryl-CoA dehydrogenase activity is defined as the NADP+-dependent
  (S)-3-hydroxybutanoyl-CoA reaction (checked in local GO db). No experiment shows that PaaH
  uses 3-hydroxybutyryl-CoA or NADP+; the assayed reaction was NAD+ with 3-hydroxyadipyl-CoA,
  so GO:0003857 is correct. All three GO:0008691 rows are MODIFY -> GO:0003857. The IDA row
  (assigned by UniProt) is flagged as a probable WRONG_TERM source defect. The PANTHER subfamily name
  (PTHR48075:SF5 "3-HYDROXYBUTYRYL-COA DEHYDROGENASE") and the structural-genomics PDB title
  likely drove the butyryl label.
- Fatty acid beta-oxidation / fatty acid metabolic process: over-annotations; the substrate is
  an aromatic-ring-derived C6 dicarboxylic CoA ester.
