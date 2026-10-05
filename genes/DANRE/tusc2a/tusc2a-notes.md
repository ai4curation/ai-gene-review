# tusc2a notes

## Setup and provenance

- Fetched with `just fetch-gene` on Q08BH0 (TrEMBL, zgc:153746, 111 aa); 4 GOA rows (ND root MF,
  3 IBA from mouse Tusc2). ZFIN ZDB-GENE-061013-612, Ensembl ENSDARG00000099817, chromosome 6.
- **Deep research unavailable**: Edison returned 402 Payment Required and the OpenAI key is
  invalid, so no `-deep-research-*.md` was generated. Literature searched by hand via Europe PMC
  (queries: `"tusc2a"`, `"tusc2b"`, `zebrafish AND (tusc2 OR fus1)`,
  `(TUSC2 OR FUS1) AND mitochondri* AND calcium`, title searches for Fus1 and inflammation).
- `"tusc2a"` finds only a largemouth-bass heat-stress transcriptome; `"tusc2b"` finds nothing. No
  zebrafish study of either copy exists.
- Part of DANRE_DUPLICATION batch 4 (random sample, seed 20260928); paralog tusc2b. Ensembl
  Compara (REST, 2026-09-28) places the duplication at Osteoglossocephalai; gar ENSLOCG00000014230
  is a one-to-many orthologue of both copies; medaka one-to-one orthologues are
  ENSORLG00000027802 (tusc2a) and ENSORLG00000027402 (tusc2b).

## Mammalian TUSC2 / FUS1 (ancestral function)

- Mitochondrial localization depends on myristoylation
  [PMID:35181743 "Also, myristoylation-deficient FUS1/TUSC2 loses its characteristic mitochondria/ER localization and its abilities to induce apoptosis and suppress tumor cell proliferation in vitro."]
- Regulator of mitochondrial calcium uptake (mouse cells)
  [PMID:24328503 "Fus1 loss resulted in reduced rate of mitochondrial calcium uptake in calcium-loaded epithelial cells, splenocytes, and activated CD4(+) T cells."]
  [PMID:24328503 "Our results establish Fus1 as one of the few identified regulators of mitochondrial calcium handling."]
- The calcium-binding domain was predicted, not measured
  [PMID:24328503 "Based on putative calcium-binding and myristoyl-binding domains that we identified in Fus1, we explored our hypothesis that Fus1 regulates mitochondrial calcium handling and calcium-coupled processes."]
- Knockout mice: chronic inflammation, mitochondrial parameters changed
  [PMID:22513871 "Untreated Fus1(-/-) mice had an ~eight-fold higher proportion of peritoneal granulocytes than Fus1(+/+) mice, pointing at ongoing chronic inflammation."]
- Motif conservation across metazoans (with AI modeling of an OSCP interface, a hypothesis)
  [PMID:42314984 "Because TUSC2 is a small and otherwise weakly conserved protein, searches were guided by conservation of the acidic calcium-binding motif region, including the canonical DEDGDLAHEFYEE sequence and related D-x-D-x-D-containing variants, which represent the most evolutionarily conserved region of the protein family."]

## Own analysis

See [RESULTS.md](tusc2a-bioinformatics/RESULTS.md). The copies are 80.2% identical; both keep
Gly2 (myristoylation) and the exact DEDGDLAHEFYEE motif; relative rate not different (5 vs 9
unique changes). Expression: tusc2a is the larger maternal transcript and then drops to 1-2 TPM at
gastrulation; tusc2b is the main zygotic copy (26-51 TPM). In adult Bgee calls tusc2b is higher in
21 of 25 shared tissues; tusc2a's top calls are testis and ovarian follicle.

## Curation decisions

- ND root MF: ACCEPT (MF genuinely unknown; calcium binding only predicted).
- mitochondrion (IBA): ACCEPT.
- regulation of mitochondrial membrane potential (IBA): ACCEPT.
- inflammatory response (IBA): MARK_AS_OVER_ANNOTATED (knockout consequence of mitochondrial
  dysfunction; the protein does not do the work of the inflammatory response).
