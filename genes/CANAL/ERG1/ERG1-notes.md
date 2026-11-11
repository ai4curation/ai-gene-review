# ERG1 notes

## Workflow

- The falcon/perplexity-lite deep-research recipe was attempted before this manual pass and failed because
  this environment has no `agentapi` command and no provider API key. No
  `ERG1-deep-research-falcon.md` or `ERG1-deep-research-perplexity-lite.md` file was created; these notes
  summarize the cached literature and family rows instead.
- I searched PubMed/Web for newer Candida albicans ERG1 or squalene epoxidase papers. Recent hits were
  compound-perturbation, docking, or adjuvant studies that did not change the direct ERG1 functional
  model, so no new PMID cache files were needed.

## Manual evidence notes

- UniProt Q92206 records Candida ERG1 as the PTHR10835 squalene monooxygenase and gives the curated
  Rhea reaction for squalene epoxidation: "Reaction=squalene + reduced [NADPH--hemoprotein reductase]
  + O2 = (S)-" [file:genes/CANAL/ERG1/ERG1-uniprot.txt].
- Ryder and Dupont assayed the Candida particulate enzyme before ERG1 was cloned: "A washed
  'microsomal' fraction converted radiolabelled squalene to 2,3-oxidosqualene and lanosterol" and its
  minimum activity requirements were oxygen, NADH or NADPH, and FAD [PMID:6378256].
- Ryder and Dupont then showed that allylamines inhibit the Candida enzyme; naftifine and SF 86-327 were
  "potent inhibitors of the Candida epoxidases" [PMID:3877503]. This supports druggability of the enzyme
  but the molecular assignment to ERG1 comes from the later cloning paper.
- Favre and Ryder cloned Candida squalene epoxidase and expressed it in budding yeast; homogenates
  "overexpressing the C. albicans protein SE activity was 10-fold higher than the" endogenous activity
  [PMID:9161422].
- Pasrija et al. conditionally depleted ERG1 and found "a total lack of ergosterol and instead
  accumulation of squalene" [PMID:15845783]. They also reported drug-sensitivity and hyphal defects, but
  those are downstream consequences of losing ergosterol-rich membrane structure rather than direct ERG1
  processes.
- The later raft-lipid report uses the same logic: ERG1 or IPT1 perturbation "leads to improper surface
  localization of" Cdr1p [PMID:16246085]. This is useful phenotype evidence for sterol/sphingolipid-rich
  domains, not a reason to make Cdr1 localization a core ERG1 annotation.
- Roemer et al. placed one ERG1 allele under `MET3p` and showed the conditional strain was specifically
  hypersensitive to terbinafine: "reduced expression of Ca ERG1 resulted in cells that were hypersensitive
  only to the target-specific inhibitor terbinafine" [PMID:16607011].
- The CaFT paper reports genome-wide heterozygote responses to many compounds, with "additional inhibitors
  of ergosterol biosynthesis, including terbinafine, lovastatin, and dyclonine" in the supplements
  [PMID:17604452]. The xenobiotic-response GO rows inferred from these profiles are target/fitness
  perturbations, not evidence that ERG1 executes xenobiotic response.
- The plasma-membrane proteome paper identified 214 proteins by LC-MS/MS [PMID:19824013], but the local
  cache contains only the abstract and does not expose the ERG1-specific entry. I left the plasma-membrane
  row undecided pending the full protein table.

## PANTHER rows

- `PTHR10835	PTN000089417	GO:0004506	F	IBD	false` supports fungal/animal squalene
  monooxygenase activity.
- `PTHR10835	PTN000089417	GO:0005783	C	IBD	false` supports ER localization for the same
  broad squalene monooxygenase node.
- `PTHR10835	PTN000851137	GO:0006696	P	IBD	false` supports the fungal ergosterol biosynthetic
  process assertion.
