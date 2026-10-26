# NADK2 (donkey, Equus asinus) — A0A8C4M4D0 notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Scope: full review of the donkey NADK2 gene model A0A8C4M4D0 (538 aa, Ensembl
ENSEASP00005021431.1, gene ENSEASG00005014681.2). This folder is
`NADK2__A0A8C4M4D0` because `genes/EQUAS/NADK2/` is keyed to the isoform-2-like
model A0A9L0K2P4 of the same gene. ProtNLM2 predictions were not opened or used.

### Data fetch and deep research
- `just fetch-gene EQUAS A0A8C4M4D0 --alias NADK2__A0A8C4M4D0`: 4 GOA rows, all IEA
  (GO_REF:0000120 combined pipeline x3, GO_REF:0000117 ARBA x1).
- Deep research FAILED: falcon "Failed to authenticate" (Edison client), fallback
  perplexity-lite returned HTTP 401 insufficient_quota. No deep-research file was
  created. The review relies on the cached primary literature on the human ortholog
  (PMID:23212377, full text; PMID:24847004, abstract only) and local sequence/PANTHER data.

### Evolutionary grounding
- UniProt: PANTHER PTHR13158:SF5 "NAD KINASE 2, MITOCHONDRIAL"; Pfam PF01513; InterPro
  IPR002504 NADK, IPR017437/IPR017438 ATP-NAD kinase domains. PE 3 (homology); every
  CC line is ARBA, so the record itself provides no evidence beyond family membership.
- `interpro/panther/PTHR13158/PTHR13158-entries.csv`: SF5 contains human Q4G0N4, mouse
  Q8C5H8, rat Q1HCL7, Xenopus Q08CZ6 — the same subfamily as the donkey gene.
- PAINT (`PTHR13158-paint.tsv`): IBD GO:0003951 NAD+ kinase activity and GO:0019674 NAD+
  metabolic process at PTN004406956 (seeds human NADK2, mouse Nadk2); GO:0005739
  mitochondrion at PTN000994636 (taxon Eukaryota). Human NADK2 also carries an IDA
  GO:0042803 protein homodimerization activity (PMID:23212377) that PAINT did NOT
  propagate; treated as a deliberate omission, so no NEW homodimerization row here.
- Donkey is not a PAINT reference proteome; GOA rows cite TreeGrafter node
  PTN001407776 (not in the cached PAINT table).

### Sequence (reused existing analysis, not rerun)
`genes/EQUAS/NADK2/NADK2-bioinformatics/RESULTS-rereview.md` (written for the
benchmark model's re-review) already compares all three donkey NADK2 models, including
this accession, against human Q4G0N4 with a reproducible PEP 723 script:
- A0A8C4M4D0: 538 aa, 100% coverage of human canonical, 96.83% identity, gap-free.
- Retains human 288-319 segment (missing from the benchmark A0A9L0K2P4), including the
  positions equivalent to human Ser306/Lys317/Trp319 (donkey S402/K413/W415), which
  Ohashi et al. map to the NAD+-binding Asp/Thr/Tyr of M. tuberculosis Ppnk.
- GGDG motif conserved (human 159-162 = donkey 255-258).
- 96-residue N-terminal extension upstream of donkey Met97 (= human Met1) is shared by
  all equid models (Ensembl start-site choice). The human transit-peptide-equivalent
  region (human 1-62) is internal (donkey 97-158). True translational start uncertain.

### Literature (human ortholog; nothing experimental exists for donkey)
- [PMID:23212377 "we detected the formation of NADP+ from NAD+ and of ADP from ATP (Fig. 2c), showing that C5orf33 protein has NADK activity using ATP and poly(P) as phosphoryl donors"]
- Kinetics: Km(NAD+) 0.022 mM; NADH kinase only 10% of NADK activity; inhibited by NADH,
  NADPH and NADP+ [PMID:23212377 "the NADK activity of C5orf33 protein was inhibited by NADH, NADPH and in particular NADP+"].
- Localisation: [PMID:23212377 "confirming that C5orf33 protein is a mitochondrial NADK, and that its N-terminal 62 residues contain a functional mitochondrial-targeting sequence"]. Submitochondrial (matrix) placement is inferred (soluble protein, NADP-dependent matrix clients), not directly assayed.
- Requirement for mitochondrial NADP(H): [PMID:24847004 "NADK2 encodes the mitochondrial NAD kinase, which is crucial for NADP biosynthesis evidenced by decreased mitochondrial NADP(H) levels in patient fibroblasts"]. DECR and lysine degradation deficiency are downstream consequences (NADPH supply to other enzymes); not annotated as NADK2 process participation.

### Decisions
- GO:0003951 NAD+ kinase activity: ACCEPT (core; same subfamily as characterised human).
- GO:0005739 mitochondrion: ACCEPT (level experimentally established in human).
- GO:0005759 mitochondrial matrix: ACCEPT (inferred specific compartment).
- GO:0019674 NAD+ metabolic process: MODIFY -> GO:0006741 NADP+ biosynthetic process
  (is_a descendant verified via OLS hierarchicalAncestors; NADK2 performs the step).
- No NEW rows: homodimerization omitted by PAINT; ROS/DECR/lysine phenotypes are downstream.

### What is experimental in this species
Nothing. All donkey statements are homology inferences from human (and mouse via
PAINT seeds) NADK2 in the same PANTHER subfamily.
