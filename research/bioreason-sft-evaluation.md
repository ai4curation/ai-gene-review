# BioReason-Pro SFT Catalogue Evaluation

Systematic evaluation of BioReason-Pro SFT predictions from the HuggingFace
`wanglab/protein_catalogue` (223K proteins) against expert-curated AIGR gene reviews.

Source: `data/bioreason-hf/protein_catalogue.ddb`
Branch: `feat/bioreason-hf-catalogue`

## Methods

For each protein:
1. Extract SFT generation from HF catalogue → `{GENE}-deep-research-bioreason.md`
2. Fetch UniProt/GOA via `just fetch-gene`
3. Deep literature research → `{GENE}-notes.md`
4. Complete expert review → `{GENE}-ai-review.yaml`
5. Evaluate BioReason trace → `{GENE}-bioreason-sft-review.md` (correctness + completeness, 1-5 scale)
6. Validate: `just validate {SPECIES} {GENE}`

## Per-Protein Results

### Round 1: DANRE, DICDI, METJA, MYCTU, PSEAE (15 proteins)

| Gene | Clade | UniProt | Correctness | Completeness | Key failure mode |
|------|-------|---------|:-----------:|:------------:|------------------|
| fen1 | DANRE | Q6TNU4 | 4 | 4 | Minor overstatement of recombination roles |
| ufsp2 | DANRE | Q7T347 | 4 | 3 | Fabricated gravitaxis phenotype claims |
| dph2 | DANRE | A4QN59 | 3 | 4 | Wrong chemistry, unsupported nuclear localization |
| nip7 | DICDI | B0G104 | 3 | 3 | Fabricated UV/DNA-damage response |
| mlcD | DICDI | Q7Z2B8 | 2 | 3 | Family-level conflation (calmodulin → myosin I LC) |
| tlcd4b | DICDI | Q550S9 | 2 | 2 | Ceramidase confusion (actually acyltransferase) |
| MJ1511 | METJA | Q58906 | **1** | 2 | Fabricated HMF catabolism, fake UniProt summary |
| nadX | METJA | Q58325 | 3 | 4 | Wrong product (oxaloacetate → iminoaspartate) |
| thiL | METJA | Q60337 | 3 | 3 | Wrong GO term, speculative metabolon |
| Rv3660c | MYCTU | P9WKX7 | 2 | 2 | Fabricated UniProt summary, missed septum function |
| Rv0898c | MYCTU | P9WKP5 | **1** | 2 | Fabricated UniProt summary + CoA narrative |
| clpP2 | MYCTU | P9WPC3 | 4 | 3 | Generic ClpP, misses Mtb heterocomplex |
| ubiE | PSEAE | Q9HUC0 | 4 | 3 | Menaquinone-biased, speculative metabolon |
| secF | PSEAE | Q9HXI2 | 4 | 4 | Minor: SecD size, protein binding as MF |
| rpsD | PSEAE | O52759 | 4 | 4 | Minor: wrong 30S subdomain name |

**Round 1 means: Correctness 2.9/5, Completeness 3.1/5**

### Round 2: ANOGA, ARATH, DROME, ECOLI, SCHPO, human, mouse, rat, worm, yeast (30 proteins)

*(In progress)*

| Gene | Clade | UniProt | Correctness | Completeness | Key failure mode |
|------|-------|---------|:-----------:|:------------:|------------------|
| | | | | | |

## Per-Clade Summary

| Clade | n | Mean Correctness | Mean Completeness | Notes |
|-------|---|:----------------:|:-----------------:|-------|
| DANRE | 3 | 3.7 | 3.7 | Diagnostic domains score well |
| DICDI | 3 | 2.3 | 2.7 | Family conflation, organism biology absent |
| METJA | 3 | 2.3 | 3.0 | Worst clade: archaeal biology missed, fabrication |
| MYCTU | 3 | 2.3 | 2.3 | Fabricated UniProt summaries on uncharacterized proteins |
| PSEAE | 3 | 4.0 | 3.7 | Best clade: well-annotated prokaryotic proteins |

## Failure Mode Analysis

### 1. Fabricated UniProt Summaries (3/15 proteins)
BioReason SFT generates a "UniProt Summary" line that does not match the actual
UniProt record. All three cases are on poorly characterized proteins (MJ1511,
Rv0898c, Rv3660c). The model appears to confabulate plausible-sounding summaries
when the real UniProt entry says "Uncharacterized protein."

### 2. Cross-Kingdom Fold Bias (MJ1511)
HMF catabolism predicted for a hyperthermophilic archaeon. BioReason applies
eukaryotic/bacterial biology to an archaeal protein based on fold similarity.

### 3. Family-Level Conflation (mlcD, tlcd4b)
BioReason applies the biology of well-characterized family members to divergent
paralogs. mlcD gets calmodulin biology instead of myosin I light chain specifics.
tlcd4b gets ceramidase activity instead of acyltransferase (the correct function
per 2025 literature).

### 4. Organism-Specific Biology Absent (clpP2, nadX, thiL)
Even when the core enzyme type is correct, BioReason misses organism-specific
features: Mtb ClpP1-ClpP2 heterocomplex, archaeal NAD biosynthesis pathway
specifics, chimeric thiamine pathway.

### 5. Confabulation on Uncharacterized Proteins
The two worst scores (1/5) are both uncharacterized proteins. BioReason produces
elaborate but entirely unsupported narratives rather than acknowledging uncertainty.
InterPro2GO's conservative approach (assign nothing) is more accurate.

### 6. False Specificity vs InterPro2GO
BioReason outperforms InterPro2GO when domains are highly diagnostic (fen1, secF,
rpsD) but underperforms when it adds false specificity to generic domain predictions
(tlcd4b, mlcD). The net effect is mixed — more informative when right, more
misleading when wrong.

## Overall Conclusions

*(Will be updated after round 2)*
