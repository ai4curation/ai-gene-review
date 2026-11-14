# TRPC subunit residue-level comparison (computed provenance)

**Hypothesis tested:** Among TRPC1/3/4/5/6/7 co-expressed in GnRH neurons, TRPC4
"alone combines the cSrc-phosphorylated tyrosine and the PIP2-interaction
determinants" required by the published kisspeptin gating mechanism.

**Inputs:** UniProt canonical sequences — TRPC1 P48995 (793 aa), TRPC3 Q13507
(921 aa), TRPC4 Q9UBN4 (977 aa, = TRPC4α), TRPC5 Q9UL62 (973 aa), TRPC6 Q9Y210
(931 aa), TRPC7 Q9HCX4 (862 aa).

**Methods:** Sequences fetched from UniProt REST. cSrc/Src-family target
tyrosines defined as hTRPC4 Tyr-959 and Tyr-972 (Odell 2005, PMID:16144838).
Smith-Waterman (local) and Needleman-Wunsch (global) alignment of the TRPC4
C-terminus against each paralog, BLOSUM62, gap −5/−6. Residue aligned to
TRPC4 Y959 and Y972 was read from the alignment columns.

## Result 1 — cSrc target tyrosines (TRPC4 Y959, Y972)

TRPC4 distal C-tail (last 40 aa): `EDTVPIIPKEKHAKEEDSSIDYDLNLPDTVTHEDYVTTRL`
(Y959 is the Y in `...SSID**Y**DL...`; Y972 is the Y in `...HED**Y**VTTRL`)

| Subunit | Residue aligned to TRPC4 **Y959** | Residue aligned to TRPC4 **Y972** | C-terminal distal-tail (last 40 aa) |
|---------|:---:|:---:|---|
| TRPC4 (ref) | **Y** | **Y** | ...SSIDYDLNLPDTVTHEDYVTTRL |
| TRPC5 | L | **Q** | SSNSKLLDSSEDVFETWGEACDLLMHKWGDGQEEQVTTRL |
| TRPC1 | L | F | DQATVENLNELRQDLSKFRNEIRDLLGFRTSKYAMFYPRN |
| TRPC3 | I / (Y in local aln) | M | QDISSLRYELLEDKSQATEELAILIHKLSEKLNPSMLRCE |
| TRPC6 | L | Q | SSLRYELLEEKSQNTEDLAELIRELGEKLSMEPNQEETNR |
| TRPC7 | Q / (Y in local aln) | H | LLEEKSQATGELADLIQQLSEKFGKNLNKDHLRVNKGKDI |

**Interpretation:** Neither Y959 nor Y972 is conserved at the aligned position in
any paralog. The tyrosines are TRPC4-specific, BUT (a) they lie in the
hypervariable, poorly-aligning distal C-tail; (b) Odell 2005 showed they control
EGF/Src-dependent membrane insertion/trafficking, not the channel gating step;
(c) they are present in both TRPC4α and TRPC4β, so they cannot explain the
α-specific identification in GnRH neurons.

## Result 2 — PIP2-interaction / PIP2-depletion gating determinant

| Determinant | TRPC4α | TRPC4β | TRPC5 | TRPC3/6/7 | Discriminates TRPC4 from TRPC5? |
|---|---|---|---|---|---|
| Inhibited by intracellular PIP2 | Yes (PMID:18230622) | No | Yes (PMID:18665391) | No (DAG-gated) | **No** |
| Activated by PIP2 depletion (PI4K inhib.) | Yes | — | Yes (PMID:18665391) | No | **No** |
| C-terminal PDZ/NHERF motif (…VTTRL) | Yes | Yes | Yes (…VTTRL) | No | **No** |
| Phosphoinositide regulation (general) | Yes | Yes | Yes | Yes | No (pan-TRP, PMID:37871124) |

**Interpretation:** The PIP2-depletion gating mechanism distinguishes the
TRPC1/4/5 subfamily from the DAG-gated TRPC3/6/7 subfamily, but does NOT
distinguish TRPC4 from its co-expressed closest paralog TRPC5. The C-terminal
NHERF/PDZ (…VTTRL) motif is also shared by TRPC4 and TRPC5.

## Bottom line
The two determinants do not co-localize into a single TRPC4-exclusive gating
module: the cSrc tyrosines are a trafficking feature (α=β), while the PIP2
determinant is an α-vs-β / subfamily feature shared with TRPC5. The hypothesis's
"TRPC4 alone combines both" premise is not supported as a discriminator.
