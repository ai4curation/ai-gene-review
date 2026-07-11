# SET6 (YPL165C / UniProt Q12529) — SET-domain integrity analysis

## Question

Is *S. cerevisiae* SET6 a **catalytically competent** SET-domain protein-lysine
methyltransferase, or a **degenerate / pseudo-methyltransferase** like Set3 and Set4?
And does it belong to the SMYD subfamily (like its paralog Set5), consistent with the
RCA zinc-ion-binding annotation?

This tests the claim in PMID:37252976 ("The protein methylation network in yeast") that
Set6 is *"likely to be an active methyltransferase"* whereas Set3/Set4 *"appear to lack
methyltransferase activity due to amino acid substitutions at key AdoMet-binding
residues"* — directly on the SET6 sequence.

## Methods (reproducible; see `justfile`)

- **Panel** (`scripts/fetch_sequences.py`): SET6 (Q12529, read from the local UniProt
  flat file), yeast SET1/SET2 (active KMTs), Set5 (SMYD paralog, characterized H4K5/8/12
  KMT), Set3/Set4 (reported inactive), and human SMYD1/2/3 + SETD6.
- **Domain detection** (`hmmsearch` vs Pfam **PF00856 SET** HMM from InterPro):
  `results/set_domain_hmmsearch.txt` / `.domtbl`.
- **Motif read-out** (`scripts/motif_from_mafft.py`): MAFFT L-INS-i MSA of the panel,
  then read every protein's residues at the SET6 catalytic/SAM-binding motif columns.
  Output `results/motif_readout_mafft.txt`.
- **Identity** (`scripts/pairwise_identity.py`, `scripts/set_domain_identity.py`):
  full-length and SET-domain-restricted % identity of SET6 vs the panel.

## Key results

### 1. SET domain is present and near-complete
`hmmsearch` vs PF00856 gives SET6 a significant SET-domain hit
(domain E-value **6.3e-14**) spanning residues **23–337**, matching HMM match states
1–104 (essentially the whole domain model). The wide span (with a long internal insert)
is the **split-SET architecture** typical of the SMYD subfamily; human SMYD1/2/3 and
SETD6 in the same run show the identical single wide split-SET hit. Consistent with
UniProt's SET domain call (residues 12–338) and "class V-like SAM-binding
methyltransferase superfamily".

### 2. The catalytic / SAM-binding motifs are INTACT in SET6 (unlike Set3/Set4)

Residues each protein contributes at the SET6 catalytic-pocket columns
(`results/motif_readout_mafft.txt`), with catalytically critical positions marked `*`:

```
NHSC pocket (SAM/AdoMet + catalytic; SET6 residues 302-309)
                          ***
  SET6_YEAST      F N H S C N P N   <- N303/H304/S305/C306 intact  (ACTIVE-like)
  SET5_YEAST      I N H D C E P N   <- N/H intact (active SMYD)
  SET1_YEAST      I N H C C D P N   <- N/H intact (active H3K4 KMT)
  SET2_YEAST      C N H S C S P N   <- N/H/S intact (active H3K36 KMT)
  SMYD2_HUMAN     M N H S C C P N   <- intact
  SMYD3_HUMAN     L N H S C D P N   <- intact
  SET3_YEAST      L R R S C Q P N   <- N-H -> R-R  (LOST; degenerate)
  SET4_YEAST      I R R S C E P N   <- N-H -> R-R  (LOST; degenerate)

Catalytic-Y motif (SET6 residues 324-337, terminal Y337)
  SET6_YEAST      N R D I K K D E Q I C I D Y   <- Y337 present
  (SET1/SET2/SMYD2/SMYD3 all retain the terminal aromatic Y)
```

**This is the decisive result.** The invariant Asn-His of the "NHSC" AdoMet/catalytic
motif is **conserved in SET6** (Asn303-His304-Ser305-Cys306), exactly as in the active
enzymes Set1, Set2, Set5, SMYD2 and SMYD3. In sharp contrast, the two proteins reported
to be catalytically dead — **Set3 and Set4 — have the Asn-His replaced by Arg-Arg**
(`RRSC`). SET6 also retains the C-terminal catalytic tyrosine (Tyr337). So on primary
sequence, **SET6 groups with the active methyltransferases, not with the pseudoenzymes**,
which independently reproduces the PMID:37252976 assertion.

### 3. SET6 is a SMYD-subfamily protein; Set5 is its closest yeast relative
SET-domain-restricted identity (`results/set_domain_identity.txt`) ranks
**Set5 first (24.7 % id over 255 aligned positions)** — the highest identity *and*
coverage of the panel — with the human SMYD/SETD6 group next. (Full-length global
identity is uniformly low, 22–30 %, and is *not* informative here because panel members
carry very different N/C extensions, e.g. Set1 is 1080 aa; the SET-domain-restricted
comparison is the appropriate metric.) This matches the literature that Set5 and Set6 are
the two yeast orthologs of the metazoan SMYD family.

### 4. Cysteine-rich; consistent with SMYD-type zinc binding (supports RCA annotation)
SET6 has **17 Cys (4.6 %**, well above the ~1.3 % proteome average), in three clusters:
N-terminal/early-SET (C26, C58, C61 — a `CxxC`), an internal insert cluster
(C189/C194/C195/C200/C213), and a C-terminal post-SET `C-x-C...C` (C360, C362, C365:
`FFDCACERCK`). This clustered pattern is the expected SMYD-family zinc-knot / post-SET
metal-binding architecture and is consistent with the computational zinc-ion-binding
prediction (RCA, PMID:30358795). Note the NHSC Cys306 is one of these cysteines. SET6
(373 aa) is shorter than Set5 (526 aa) and does not carry a separately annotated canonical
MYND domain, so a full MYND ZF could not be confirmed here.

## Interpretation and caveats

- **What is supported:** SET6 has an intact SET domain and retains the canonical
  catalytic/SAM-binding residues that Set3/Set4 have lost. It is therefore a **plausible,
  catalytically competent SET-domain (SMYD-subfamily) protein-lysine methyltransferase**.
  This licenses a `putative`/`likely` MF of protein-lysine methyltransferase activity.
- **What is NOT supported:** sequence integrity says nothing about the **substrate** or
  the **biological role**. No in-vitro or in-vivo methyltransferase activity, and no
  substrate, has been demonstrated for SET6 in the literature. A generic "histone
  methyltransferase activity" is unsupported — the SMYD family (and SETD6) act largely on
  **non-histone** substrates, and Set6's substrate is explicitly listed as unknown.
- Motif conservation is necessary but not sufficient for activity; the only way to settle
  competence is an enzymatic assay.

## Reproducibility checklist

- [x] Scripts take inputs from files / live UniProt fetch; **no hardcoded inputs**.
- [x] **No conclusions hardcoded** — code only extracts residues/identities; all
      interpretation is in this RESULTS.md.
- [x] Pipeline tested on **other inputs**: the same panel includes 9 non-SET6 proteins
      (positive controls Set1/Set2/Set5/SMYD1-3, negative-pattern Set3/Set4); the
      SET-HMM was additionally run on a non-SET protein (yeast ADH1) and correctly
      returned **0 significant hits**.
- [x] Analyses completed as expected; direct outputs in `results/`.
- [x] Provenance/justification given; uncertainty about substrate/activity stated
      honestly.

## Files
- `scripts/` — analysis code
- `data/reference_sequences.fasta`, `data/SET6.fasta`, `data/PF00856_SET.hmm`
- `results/set_domain_hmmsearch.txt` / `.domtbl` — SET-domain detection
- `results/motif_readout_mafft.txt` — catalytic/SAM-binding motif read-out
- `results/panel_mafft.aln.fasta` — MSA
- `results/pairwise_identity.txt`, `results/set_domain_identity.txt`
- `justfile` — reproducible workflow (`just all`)

## Tools & databases
MAFFT v7 (L-INS-i); HMMER 3.3 (hmmsearch/hmmalign); Pfam PF00856 (SET domain, via
InterPro); Biopython 1.87 (PairwiseAligner, BLOSUM62); UniProt REST. Panel accessions:
Q12529 (SET6), P38890 (Set5), P36124 (Set3), P42948 (Set4), P38827 (Set1), P46995 (Set2),
Q8NB12/Q9NRG4/Q9H7B4 (SMYD1/2/3), Q8TBK2 (SETD6).
