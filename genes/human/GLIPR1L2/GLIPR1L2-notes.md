# GLIPR1L2 review notes

## 2026-07-18 — data retrieval and research boundary

- `just fetch-gene human GLIPR1L2` retrieved reviewed UniProt Q4G1C9 and three current GOA groups: extracellular region (IBA), molecular adaptor activity (IBA), and membrane (IEA).
- `just fetch-gene-pmids human GLIPR1L2` found no PMID-backed rows in the seeded GOA.
- The configured Falcon/Edison deep-research request failed with HTTP 402, and the `perplexity-lite` fallback failed with HTTP 401 because provider quota was exhausted. No provider-named report was created; the evidence synthesis is recorded in `GLIPR1L2-deep-research-manual.md`.

## Direct human evidence

- GLIPR1L2 is an isoform-rich member of the GLIPR1/CAP family. The original discovery paper reports five differentially spliced isoforms, whereas the current reviewed UniProt record names six isoforms. [PMID:16714093 Identification and characterization of RTVP1/GLIPR1-like genes, a novel p53 target gene cluster, "GLIPR1L1 has two and GLIPR1L2 has five differentially spliced isoforms."]
- The 2006 paper identifies GLIPR1L2 as a p53-responsive gene and reports expression in multiple tissues including prostate and bladder; current UniProt metadata describes highest expression in testis. [PMID:16714093, "Like hRTVP-1, GLIPR1L1 and GLIPR1L2 are p53 target genes."] [PMID:16714093, "GLIPR1L2 is expressed in different types of tissues, including prostate and bladder."]
- UniProt Q4G1C9 describes a reviewed 344-aa protein with an SCP/CAP domain at residues 58–192, a predicted transmembrane helix at residues 254–274, and a long acidic/disordered C-terminal region. The record calls it a single-pass membrane protein but gives no experimentally resolved membrane, topology, or active extracellular form.
- The three recorded isoform-2 interactions with PECAM1, UBE2K, and VIM are high-throughput binary-interaction observations. They neither converge on a native physiological complex nor establish molecular adaptor activity.

## Reproductive evidence and its limits

- A 2025/2026 mouse study reports that Glipr1l2/GLIPR1L2 is highly expressed in mouse and human testis and epididymis. [PMID:40572022 Mouse genome engineering uncovers 18 genes dispensable for male reproduction, "Glipr1l1, Glipr1l2, Izumo4, Slc22a16, Spmip2, Tex51, Tmco2, Triml1, and Triml2 are highly expressed in mouse and human testis and epididymis"]
- The same study deleted a 10,138-bp interval spanning mouse Glipr1l1, Glipr1l2, and Glipr1l3. Triple-knockout males had normal fecundity, testis and epididymis histology, sperm morphology, and sperm motility. [PMID:40572022, "Glipr1l1‐3 KO males exhibited no anomalies in their testis weight, testis and epididymis histology, or sperm morphology and motility"]
- Because all three neighboring genes were deleted together, this experiment establishes that the cluster is collectively dispensable for natural male reproduction under the assays used; it does not isolate a positive or negative role for Glipr1l2 itself.
- Mouse GLIPR1L1, a paralog, has direct acrosomal/IZUMO1-complex evidence. The 2010 and 2019 studies experimentally assay GLIPR1L1 rather than GLIPR1L2. Their sperm-complex/adaptor mechanism must not be transferred to human GLIPR1L2 solely from shared CAP-family ancestry. [PMID:31672133 GLIPR1L1 is an IZUMO-binding protein required for optimal fertilization in the mouse, "At least two of these complexes contain IZUMO1 in partnership with GLI pathogenesis-related 1 like 1 (GLIPR1L1)."]

## Annotation-review conclusions

- Accept `membrane` (IEA). A predicted helix spanning residues 254–274 strongly supports a membrane-associated isoform, although the exact organelle and topology remain unknown.
- Remove `molecular adaptor activity` (IBA). The only PAINT experimental seed is mouse Glipr1l1, whose adaptor-like activity is tied to an IZUMO1-containing sperm complex. No GLIPR1L2 experiment establishes such a complex or bridging role.
- Leave `extracellular region` (IBA) undecided. CAP-family architecture and a single-pass topology make an extracellular/luminal N-terminal domain plausible, but the human discovery paper is abstract-only, UniProt does not define orientation, and no direct extracellular localization or activity has been demonstrated for a specific GLIPR1L2 isoform.
- Do not annotate p53 signaling, tumor suppression, sexual reproduction, acrosome reaction, sperm–egg adhesion, or fertilization as GLIPR1L2 protein functions. p53 regulation concerns transcription of the gene, the triple-knockout study supplies negative/nonessentiality evidence, and the positive fertilization mechanism belongs to GLIPR1L1.
- No specific molecular activity or biological process is currently established strongly enough for a positive core GO assertion.
