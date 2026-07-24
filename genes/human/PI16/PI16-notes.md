# PI16 review notes

## 2026-07-18 — review initiation and source audit

- Seeded the human PI16 review with `just fetch-gene human PI16` (UniProt Q6UXB8). QuickGO returned 13 rows collapsed by the project into eight term/evidence/reference groups.
- `just deep-research-falcon human PI16 --fallback perplexity-lite` could not run: Edison/Falcon returned HTTP 402 and Perplexity returned HTTP 401 insufficient quota. No provider-named report was retained. The review therefore uses a manual primary-literature synthesis in `PI16-deep-research-manual.md`.
- The reviewed UniProt record describes a 463-aa CAP-family glycoprotein with an N-terminal signal peptide, an SCP/CAP domain, a hydrophobic C terminus, two splice isoforms, and direct recovery from serum and urine. Human serum purification directly established an extracellular soluble pool `[PMID:15344909 "PSPBP (PSP94-binding protein) was purified from human serum"]`.
- Human coronary endothelial-cell experiments identified PI16 as an MMP2 inhibitor. Recombinant PI16 strongly inhibited recombinant MMP2, and PI16 overexpression reduced endothelial migration `[PMID:27996045 "recombinant PI16 produced in E. coli showed a strong inhibition of recombinant MMP2 activity"]` `[PMID:27996045 "adenoviral overexpression of PI16 significantly reduced the migration of HCAECs into a ‘scratch wound’ in vitro"]`.
- Human skin-homing CD8 T cells display PI16 at the plasma membrane through a GPI anchor, and inhibitor/pull-down assays support cathepsin K inhibition `[PMID:30365157 "PI16 was confined to the plasma membrane, was GPI-anchored"]` `[PMID:30365157 "Inhibitor screening and pull-down experiments confirmed that PI16 inhibits cathepsin K"]`.
- Mouse cardiac work provides orthogonal physiological context: Pi16 is displayed by cardiac fibroblasts through a GPI anchor, inhibits cathepsin K, and suppresses proteolytic chemerin activation `[PMID:27539859 "Purified recombinant PI16 efficiently inhibited cathepsin K, a chemerin-activating protease, in vitro"]`. Earlier mouse work found secreted Pi16 limits cardiomyocyte growth `[PMID:17909105 "PI16, a novel protein secreted from the heart, is strongly upregulated early in heart failure and inhibits growth of cardiomyocytes both in vitro and in vivo"]`.
- The neuropathic-pain phenotype is also mouse-specific and downstream of fibroblast/endothelial cross-talk. It is useful context, but it is not sufficient to assign a direct human molecular activity beyond the experimentally established protease inhibition `[PMID:32079726 "PI16 promotes neuropathic pain by mediating a cross-talk between fibroblasts and the endothelial barrier"]`.

## PAINT/IBA trace

- The local trace `interpro/panther/PTHR10334/PTHR10334-paint.tsv` assigns GO:0060090 molecular adaptor activity at the broad family node PTN000036124 from a single seed, MGI:MGI:1916536. That identifier is mouse `Glipr1l1`, whose experimentally annotated reproductive role is distinct from PI16.
- The same node spans a deeply divergent CAP superfamily that includes mammalian PI15/PI16/CRISP/GLIPR proteins, fungal PRY proteins, plant PR-1 proteins, and animal venom allergens. A root-node adaptor inference from `Glipr1l1` is therefore not biologically specific enough for PI16.
- Direct PI16 studies instead establish two inhibitor activities: metalloendopeptidase inhibitor activity toward MMP2 and cysteine-type endopeptidase inhibitor activity toward cathepsin K. The molecular-adaptor IBA is reviewed as `REMOVE`, with these two activities added as `NEW` annotations.

## Curation boundaries

- Serum/urine detection and GPI-anchored plasma-membrane localization are compatible: PI16 can occur as a cell-surface ectoprotein and as a soluble extracellular protein. The available data do not establish which isoforms, cleavage events, or cell types generate each pool.
- The direct substrate spectrum remains narrow. MMP2 and cathepsin K are supported; other MMPs or cathepsins should not be inferred from CAP-domain membership alone.
- The PSP94/MSMB interaction is directly reported, but generic `protein binding` is not an informative molecular-function term.
- The high-throughput binary-interactome and immune-surface-interactome rows provide partner context, not a defined core biochemical activity. Their generic protein-binding annotations are marked over-annotated rather than treated as evidence against the reported interactions.
