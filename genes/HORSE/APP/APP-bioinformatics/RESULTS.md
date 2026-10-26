# APP (horse, A0A3Q2IKB0): sequence and gene-model analysis

All scripts use PEP 723 inline metadata and are run with `uv run --script` from the repository root.

## 1. Alignment to human APP770 (P05067)

Reproduce: `uv run --script genes/HORSE/APP/APP-bioinformatics/align.py genes/HORSE/APP/APP-uniprot.txt P05067 genes/HORSE/APP/APP-bioinformatics 28-189 291-341 374-565 672-713 700-723 724-770`

Method: Biopython PairwiseAligner, global, BLOSUM62, gap open -10, gap extend -0.5. Raw output: `alignment_output.txt`.

Key output lines:

```
query A0A3Q2IKB0 length 768; human P05067 length 770
aligned pairs 746; identical 711; identity over aligned pairs 95.31%
human residues 345-363 (MSQSLLKTTQEPLARDPVK) absent from query
human region 291-341: 51 of 51 residues aligned, 51 identical
human region 374-565: 192 of 192 residues aligned, 192 identical
human region 672-713: 42 of 42 residues aligned, 42 identical
human region 724-770: 42 of 47 residues aligned, 20 identical
```

Interpretation:

- E1 domain (human 28-189): 157/162 identical. None of the substitutions (R40K, D53E, D64G, P109A, F111I) falls on the copper-binding residues His147, His151 or Tyr168.
- Kunitz/BPTI protease-inhibitor domain (human 291-341): 51/51 identical, so this model is a KPI-containing isoform.
- The 19-residue OX-2 exon (human 345-363) is absent, so the ectodomain is APP751-like (KPI+, OX-2-).
- E2 domain (human 374-565): 192/192 identical. Amyloid-beta 1-42 (human 672-713): 42/42 identical (human-type peptide). Transmembrane segment and juxtamembrane region (human 700-738) identical.
- Cytoplasmic tail: identity collapses after human Glu738 (horse ...SIHHGVVE). Human 739-770 (VDAAVTPEERHLSKMQQNGYENPTYKFFEQMQN) is replaced by an unrelated 48-residue horse sequence (LCRRSHYTKHPGKQTRLFEMVILLPAHPPEISLFQAVTAVALKPKRRPTK). The model therefore lacks the Thr743 (APP695 Thr668) phosphorylation site, the YENPTY motif and the C-terminal AICD sequence that binds PTB/PID adaptors.

## 2. All horse APP gene models

Reproduce: `uv run --script genes/HORSE/APP/APP-bioinformatics/compare_horse_models.py ENSECAG00000021011`. Raw output: `compare_horse_models_output.txt`.

Six unreviewed horse UniProt entries derive from Ensembl transcripts of the one APP gene (ENSECAG00000021011). Four of them (A0A3Q2HIF9, F6XKR3, A0A5F5PX07, A0A5F5PMR9) end in the conserved APP C-terminus (`VDAAVTPEERHLSKMQQNGYENPTYKFFEQMQN`) and contain the YENPTY motif. A0A3Q2IKB0 and A0A5F5PLP1 have unrelated C-terminal tails and lack YENPTY. Ensembl flags ENSECAT00000045461 (A0A3Q2IKB0) as the canonical transcript, which is why this model is the gene-centric UniProt entry.

Interpretation: the APP cytoplasmic tail, including YENPTY, is conserved from fish to mammals and is present in four other horse transcripts of the same gene and in the donkey model (A0A9L0JJJ9). The A0A3Q2IKB0 tail is most likely a gene-model artefact (an aberrant terminal exon, for example read-through into intronic sequence) rather than a functional horse-specific isoform. No transcript or protein evidence for this tail was examined here; the conclusion rests on conservation alone.

## 3. Ortholog experimental GO annotations

Reproduce: `uv run --script genes/HORSE/APP/APP-bioinformatics/fetch_experimental_goa.py genes/HORSE/APP/APP-bioinformatics/ortholog_experimental_goa.tsv P05067,P12023,P08592 > genes/HORSE/APP/APP-bioinformatics/ortholog_experimental_goa.txt`

QuickGO experimental-evidence annotations (ECO:0000269 and descendants) for human APP (P05067), mouse App (P12023) and rat App (P08592). These are the experimental sources behind the horse Ensembl Compara (GO_REF:0000107) transfers. Raw TSV: `ortholog_experimental_goa.tsv`; one line per distinct annotation: `ortholog_experimental_goa.txt`.

## 4. Phylogenetic placement

UniProt places A0A3Q2IKB0 in PANTHER PTHR23103:SF7 (AMYLOID-BETA PRECURSOR PROTEIN), the vertebrate APP ortholog subfamily that also holds human APP, mouse and rat App. The horse IBA rows derive from PAINT nodes PTN002749606 (APP ortholog node; cellular-component terms, signaling receptor binding and signaling receptor activator activity) and PTN000559854 (APP family; axonogenesis and central nervous system development). This agrees with the repository family review `interpro/panther/PTHR23103/PTHR23103-review.yaml`.
