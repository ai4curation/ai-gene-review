# gad1a / gad1b protein, expression and synteny comparison

Scripts (run from the repo root):

- `pair_analysis.py` (`uv run python genes/DANRE/gad1a/gad1a-bioinformatics/pair_analysis.py > genes/DANRE/gad1a/gad1a-bioinformatics/output.txt`);
  raw output in `output.txt` (run 2026-09-28).
- `probe_identity.py` (`... probe_identity.py > .../probe_identity_output.txt`); raw output in
  `probe_identity_output.txt`.

Zebrafish sequences come from the cached UniProt records (gad1a A0A8M1RDR2, 591 aa; gad1b Q7ZUS3,
587 aa). Human GAD1 (Q99259) and GAD2 (Q05329) come from UniProt; the gar and medaka proteins are
the Ensembl canonical proteins of the orthologs that Ensembl Compara assigns. Alignments: Biopython
global, BLOSUM62, gap open -10, extend -0.5; identity = identical columns / alignment length.

## Orthology and duplication node (Ensembl Compara)

- gad1a (ENSDARG00000093411, chr9) and gad1b (ENSDARG00000027419, chr6) are within-species
  paralogues with the duplication node at Clupeocephala.
- Both copies share one spotted gar ortholog (ENSLOCG00000007840, one-to-many) and one human
  ortholog, GAD1 (one-to-many).
- Medaka: Ensembl gives a one-to-one medaka ortholog (ENSORLG00000017268) for gad1a only; no medaka
  ortholog is listed for gad1b. PANTHER reports two medaka co-orthologs for the pair, so whether
  medaka kept both copies is not settled by these two sources.

## Protein

| Comparison | Identity |
|---|---|
| gad1a vs gad1b | 86.3% (592 columns) |
| gad1a / gad1b vs human GAD1 | 80.0% / 82.7% |
| gad1a / gad1b vs human GAD2 | 63.4% / 64.1% |
| gad1a / gad1b vs gar GAD1 | 85.5% / 87.8% |

Per region of human GAD1 (identical residues / region length):

| Region | gad1a | gad1b | gar |
|---|---|---|---|
| N-terminal region (1-95) | 58.9% | 65.3% | 80.0% |
| Catalytic body (96-594) | 84.4% | 86.4% | 89.8% |

Both copies keep the PLP-binding lysine (human K405, in the same RANSVTWNPHKMMGV motif), the
annotated GABA-binding residues (Q190-L191-S192 and R567) and the C-terminal RLGQDL. The only
annotated human point feature that differs is the phosphoserine S78 in the variable N-terminal
region, which is a threonine in gad1a (in every Ensembl gad1a translation) and a serine in gad1b,
gar and medaka.
Both copies keep the PLP lysine and the GABA-binding residues of human GAD1.

**Relative rate (gar outgroup):** of 584 gar positions aligned in both copies, 37 changed only in
gad1a and 23 only in gad1b (chi2 = 3.27, not significant at 0.05). The N-terminal region is the
least conserved part of GAD1 in all comparisons, and gad1a is further from human there (58.9% vs
65.3% identity); the script does not partition the relative-rate test by region.

## Identity of the classic zebrafish "GAD67" cDNA

The first zebrafish GAD67 cDNA (Martin et al. 1998, GenBank AF017266, partial CDS, 232 aa) was
compared with both paralogs (`probe_identity_output.txt`). Its translation is 99.6% identical to
gad1b (230/231 local-alignment columns) and 90.9% identical to gad1a (210/231).
The classic GAD67 cDNA AF017266 is gad1b by sequence.
Older papers that say "GAD67", "gad67" or "gad1" (including the GOA IEP row from PMID:9634146, and
Mueller & Guo 2009, whose probe is taken from AF017266) are therefore about gad1b. Two later papers
(Lueffe et al. 2021, 2022) describe their "gad1a (previously gad67a)" probe as coming from the
Martin et al. plasmid; if that plasmid is the AF017266 clone, their "gad1a" in situ signal would be
gad1b. This could not be checked because the probe sequence is not given.

## Expression

**Whole-embryo time course (E-ERAD-475, median TPM).** gad1b rises from pharyngula (3 TPM at
prim-5) to 84 TPM at day 5. gad1a stays at 0.4-4 TPM from segmentation to day 5, with a single
5 TPM value at the 2-cell stage.
gad1b is about 20-fold more abundant than gad1a in whole larvae (84 vs 4 TPM at day 5).

**Bgee calls** (only "expressed" calls are returned; absence of a call is not evidence of absence).
gad1a has 8 calls, all RNA-seq: brain 68.6, liver 63.0, early embryo 60.0, blastula 35.5, gastrula
31.2, larva 31.0, head 27.2, bone element 24.0. gad1b has 88 calls, mostly from in situ
hybridization in brain nuclei, retina, spinal cord interneurons, Kolmer-Agduhr neurons and Purkinje
cells, plus RNA-seq in larva (91.3), bone, gonad/testis and head kidney. The two copies share calls
only for larva and bone element; the difference in number of calls mostly reflects the many
published in situ studies that used gad1b.

**Gar (pre-duplication state).** Gar GAD1 (ENSLOCG00000007840) has 8 calls: brain 96.2, eye 96.0,
larva 78.6, bone 58.9, ovary 57.5, muscle 37.5, embryo 31.3, testis 25.3.

**ZFIN curated wild-type expression.** gad1b: 247 records from 69 publications, 109 anatomy terms
across forebrain, midbrain, hindbrain, spinal cord and retina. gad1a: 17 records from 4 publications
(an RT-qPCR brain panel, two Lueffe et al. in situ papers and one whole-organism record), with
terms in ventral telencephalon, preoptic area, thalamus, caudal tuberculum and medulla oblongata,
all of which are also gad1b terms.

## Synteny

gad1a is on chr9 (3.62 Mb) and gad1b on chr6 (3.83 Mb). For each copy the script took all
protein-coding genes within 1.5 Mb and asked Ensembl for their zebrafish paralogues with a
teleost-level duplication node (Clupeocephala, Osteoglossocephalai or Teleostei).

- **Conserved neighbours:** tlk1a and dync1i2a lie near gad1a on chr9 (3.55 and 3.17 Mb), and their
  teleost-level paralogues tlk1b and dync1i2b lie near gad1b on chr6 (3.88 and 3.93 Mb). The same
  two pairs are found from both directions.
- **Chromosome level:** 8 teleost-level paralogue pairs from the gad1a neighbourhood have their
  partner on chr6, and 5 from the gad1b neighbourhood have their partner on chr9.

Two flanking gene pairs duplicated at the teleost level sit next to both copies, which supports
gad1a and gad1b lying in ohnologous chromosome segments.

## Interpretation

- Protein: both copies keep every catalytic feature checked; no evidence of divergence in enzyme
  function. The N-terminal region, which in mammals differs between GAD1 and GAD2 and controls
  membrane association, is the least conserved part in both copies.
- Expression: gad1b is the dominant, pan-GABAergic copy in embryos and larvae. gad1a is expressed
  at a much lower level, with RNA-seq calls in brain and a possible maternal/early-embryo signal and
  a liver call that gad1b lacks. Published statements that the two copies have similar expression
  patterns rest on in situ probes whose paralog identity is uncertain (see above).
