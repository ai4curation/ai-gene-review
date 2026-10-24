# APOO / MIC26 (Q9BUR5) — N-terminal targeting sequence and paralogue architecture

Reproduce with:

```bash
cd genes/human/APOO/APOO-bioinformatics
uv run python targeting_sequence_analysis.py
```

All sequences and feature spans are fetched live from the UniProt REST API at run time;
nothing about the outcome is hardcoded. The script asserts that each parsed sequence length
matches the length declared on that entry's `ID` line, and it reports (rather than silently
drops) any panel member whose N-terminal feature is not the type the panel design assumes.

## Question

UniProt annotates Q9BUR5 residues **1..25 as SIGNAL** with evidence `ECO:0000255`, i.e. a
sequence-analysis prediction with no experimental support, and the same record still lists
`Secreted`, `Golgi apparatus membrane` and `Endoplasmic reticulum membrane` among its
subcellular locations. Those locations, and the historical identity of this protein as the
plasma apolipoprotein "ApoO", all trace back to a 55 kDa immunoreactive band that a later
knockout-controlled study showed to be non-specific (PMID:37279200). The paralogue
Q6UXV4 (APOOL / MIC27) — same PANTHER family PTHR14564, same complex, same membrane — is
annotated by UniProt not with a SIGNAL peptide but with a **TRANSIT peptide (1..27)**.

So: does the MIC26 N-terminus carry the sequence signature of a secretory signal peptide, or
of a mitochondrial matrix-targeting presequence?

## Design

Two control panels of human proteins, scored on their own UniProt-annotated N-terminal
segment:

- **mitochondrial TRANSIT panel** (10 proteins): HSPD1, SOD2, ATP5F1C, UQCRC1, SDHB, PMPCB,
  SDHA, ATP5F1D, IMMT/MIC60, HSPA9.
- **secretory SIGNAL panel** (10 proteins): APOA1, APOE, APOA4, APOH, APOB, AGT, ALB,
  SERPINA1, APOA2, APOD. Deliberately weighted towards plasma apolipoproteins, because the
  claim under test is specifically that MIC26 is a secreted apolipoprotein.

Discriminating metrics, all computed from the segment sequence: net charge (K+R−D−E), number
of acidic residues, Arg per 10 residues, maximum Eisenberg hydrophobic moment over an
11-residue window (amphipathicity, the hallmark of a matrix-targeting presequence), and the
maximum Kyte–Doolittle hydropathy over a 7-residue window (the h-region, the hallmark of a
secretory signal peptide).

## Result

| metric | mito TRANSIT mean±SD [min,max] | secretory SIGNAL mean±SD [min,max] | APOO/MIC26 | APOOL/MIC27 | closer to |
|---|---|---|---|---|---|
| net charge (K+R−D−E) | 4.80±1.55 [2.00,7.00] | 0.60±0.84 [−1.00,2.00] | 3.00 | 3.00 | mitochondrial (\|z\|=1.2 vs 2.8) |
| acidic residues (D+E) | 0.60±1.07 [0.00,3.00] | 0.30±0.48 [0.00,1.00] | 0.00 | 0.00 | mitochondrial (\|z\|=0.6 vs 0.6) |
| Arg per 10 residues | 1.58±0.41 [0.80,2.27] | 0.17±0.28 [0.00,0.74] | 0.40 | 0.37 | secretory (\|z\|=2.9 vs 0.8) |
| max Eisenberg hydrophobic moment (11-res) | 0.61±0.16 [0.37,0.81] | 0.25±0.06 [0.16,0.34] | 0.60 | 0.31 | mitochondrial (\|z\|=0.1 vs 5.8) |
| max Kyte–Doolittle h-region (7-res) | 1.80±0.52 [1.16,2.79] | 3.04±0.31 [2.63,3.59] | 1.70 | 1.69 | mitochondrial (\|z\|=0.2 vs 4.4) |

MIC26 segment scored: `MFKVIQRSVGPASLSLLTFKVYAAP` (residues 1–25).
MIC27 segment scored: `MAAIRMGKLTTMPAGLIYASVSVHAAK` (residues 1–27).

On 4 of the 5 metrics the MIC26 1–25 segment sits closer to the mitochondrial-presequence
panel than to the secretory-signal-peptide panel.

The two most informative numbers are the last two rows:

- **The h-region is missing.** A secretory signal peptide is defined by a long uncharged
  hydrophobic core. Every one of the ten signal peptides in the panel reaches a 7-residue
  Kyte–Doolittle mean of at least +2.63; MIC26 reaches only **+1.70**, below the entire
  secretory panel and inside the mitochondrial range.
- **It is strongly amphipathic.** MIC26's maximum hydrophobic moment, 0.602, is essentially
  the mitochondrial panel mean (0.61) and 5.8 SD above the secretory panel mean. Signal
  peptides are not amphipathic; matrix-targeting presequences are, and that amphipathic helix
  is what the TOM/TIM receptors read.

It also has zero acidic residues in 25, as presequences characteristically do.

### The one metric that disagrees, and why it does not rescue the signal-peptide call

MIC26 has only one arginine in the segment (Arg/10 = 0.40), well below the mitochondrial
panel (1.58±0.41). Classic presequences are Arg-rich, so this is a genuine mismatch and is
reported as such. But **the paralogue behaves identically** (Arg/10 = 0.37) and UniProt
nonetheless annotates its N-terminus as a TRANSIT peptide, so within this family a low Arg
count is evidently compatible with mitochondrial targeting. MIC26's basic character is
carried by lysine instead (K3, K20 in the segment, K26/K27 immediately after it): net charge
is +3 with no acidic counter-charges. Neither MIC26 nor MIC27 has Arg at −2 or −3, the MPP
cleavage motif — consistent with these being inner-membrane proteins whose N-terminal segment
may not be processed by MPP at all.

## MIC26 vs MIC27 architecture

Global BLOSUM62 alignment of Q9BUR5 (198 aa) against Q6UXV4 (268 aa): **72/197 identities in
aligned columns (36.5%)**. MIC27's features projected onto MIC26 coordinates:

| MIC27 feature | MIC27 span | aligned MIC26 span | MIC26 residues | max KD (7-res) |
|---|---|---|---|---|
| TRANSIT | 1..27 | 1..26 | `MFKVIQRSVGPASLSLLTFKVYAAPK` | +1.70 |
| TRANSMEM 1 | 111..129 | 110..128 | `FFPRLGVIGFAGLIGLLLA` | +3.01 |
| TRANSMEM 2 | 138..155 | 136..153 | `LVYPPGFMGLAASLYYPQ` | +1.70 |

MIC26's own UniProt-annotated transmembrane span is 108..128 — i.e. it coincides with the
region aligned to MIC27's TM1, and MIC26 has no annotated counterpart to MIC27's TM2. A 2026
simulation study predicts two short transmembrane helices in both MIC26 and MIC27
(PMID:42647630). The hydropathy here is **not decisive either way**: the MIC26 region aligned
to MIC27 TM2 scores +1.70, clearly less hydrophobic than its own TM1 (+3.01) but not polar.
This analysis neither confirms nor refutes a second MIC26 membrane-embedded helix; it is
recorded as an open question, not a result.

## Conclusions

1. The MIC26 N-terminal segment that UniProt calls a SIGNAL peptide has the composition and
   amphipathicity of a **mitochondrial targeting presequence**, not of a secretory signal
   peptide, and in particular lacks the hydrophobic h-region that every member of the
   secretory control panel has. This is an independent, sequence-level line of support for
   the experimental conclusion (PMID:37279200) that MIC26 is exclusively mitochondrial, and
   it identifies a likely origin of the historical "secreted apolipoprotein" identity: a
   sequence-analysis prediction (`ECO:0000255`) that assigned the wrong class of targeting
   peptide.
2. The homologous N-terminus of the paralogue MIC27 is annotated by UniProt as TRANSIT, and
   scores the same way. The SIGNAL/TRANSIT asymmetry between the two family members is an
   annotation inconsistency, not a biological difference.
3. This is a sequence-feature argument, not an experiment. It cannot by itself exclude a
   minor secreted pool; the knockout, tagged-construct and mass-spectrometry evidence in
   PMID:37279200 is what does that. It is offered as corroboration and as an explanation of
   how the prediction went wrong.

## Caveats

- The two panels are small (10 each) and hand-chosen; the SD-based "closer to" call is a
  descriptive distance, not a classifier with a calibrated error rate.
- Segment boundaries come from UniProt, and for MIC26 that boundary is itself the prediction
  under test. Scores are, however, dominated by composition over 25 residues and are not
  sensitive to a few residues either side.
- No dedicated targeting-sequence predictor (TargetP, MitoFates, DeepLoc, SignalP) was run;
  none is callable without either a local install or a web form, and this repository's rules
  forbid writing a script that pretends to call a tool it cannot reach. The metrics above are
  the published features those predictors are built on, computed directly.
