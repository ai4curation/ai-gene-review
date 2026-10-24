# APOF (Q13790) sequence analysis — results

Reproduce with `uv run python analyze_apof.py` from this directory. Every number
below is computed at run time from sequences fetched live from the UniProt REST
API; nothing is hardcoded except accessions, the UniProt feature boundaries being
tested, the Eisenberg hydrophobicity scale, and the published values each
computation is compared against. The raw console output is in `results.txt`.

## 1. The mature protein is the 162-residue C-terminal third of a 326-residue precursor

UniProt Q13790 declares a 326-residue precursor with SIGNAL 1-35, PROPEP 36-164
and CHAIN 165-326. The script asserts the CHAIN boundaries against the live record
and confirms the arithmetic:

| quantity | computed | literature |
|---|---|---|
| precursor length | 326 | 326 (PMID:19008531) |
| signal peptide 1-35 | 35 aa | "a small signal peptide" (PMID:19008531) |
| propeptide 36-164 | 129 aa | — |
| mature CHAIN 165-326 | **162 aa** | "composed of 162 amino acids" (PMID:8093033); "the 162 amino acid C-terminus" (PMID:19008531) |

signal + propeptide + chain = 326 = the full precursor. The mature circulating
protein is therefore only the C-terminal 50% of the translated product, and the
1994 cloning paper's inference that "apolipoprotein F is a proteolytic product of
a larger protein" is exactly reproduced by the current annotation. PCSK7/PC7 has
been shown to process proApoF (PMID:25349778).

The boundary is not merely predicted. Lagor et al. mutated the P1 residue of the
predicted cleavage site and abolished maturation: "we mutated arginine 164 at the
predicted proprotein cleavage site to alanine (R165 in mApo F). This substitution
completely inhibited processing to the mature form" (PMID:19008531). Arg-164 is
the last residue of UniProt's PROPEP 36-164, so the experiment places the cut
exactly where the feature table does. The same paper reports that "The Apo F
proprotein could not be detected in human plasma", i.e. circulating ApoF is
fully processed.

A discrepancy worth recording: the 2020 expert review states the precursor is a
"308 amino acid protein containing a signal peptide and a 286 amino acid
proprotein" (PMID:32520778), whereas the 2009 paper from the other principal
group states a "326 amino acid precursor ... cleaved to release the 162 amino
acid C-terminus" (PMID:19008531). UniProt's 326/162 agrees with the latter, and
carries its own CAUTION that "It is uncertain whether Met-1 or Met-12 is the
initiator". Both numbers agree on 162 for the mature chain, which is the
quantity that matters biologically.

## 2. About 12-16 kDa of the mature protein's apparent mass is not polypeptide

| quantity | value |
|---|---|
| computed mass of CHAIN 165-326, unmodified | **17.42 kDa** |
| "expected 17.4kDa" (PMID:32520778) | 17.4 kDa |
| apparent mass on SDS-PAGE | 29 kDa (PMID:2715721), ~33 kDa (PMID:9880564) |
| difference | 11.6-15.6 kDa, i.e. 66-89% above the polypeptide mass |

The computed unmodified mass reproduces the review's stated expectation to
0.02 kDa. The gap between it and the observed 29-33 kDa is the direct
quantitative basis for the statement that ApoF is "heavily glycosylated with
both O- and N-linked sugar groups" and migrates at "a molecular mass about 40%
greater than predicted" (PMID:19008531). Note that the computed excess (66-89%)
is larger than the "about 40%" that paper quotes; the two are not inconsistent,
because gel mobility of a heavily sialylated glycoprotein is not a mass
measurement, but the mass discrepancy is not a subtle one under any reading.

## 3. The precursor is a charge dipole: basic propeptide, acidic mature chain

| segment | length | computed pI | net charge at pH 7.4 | D+E | K+R |
|---|---|---|---|---|---|
| signal 1-35 | 35 | 5.47 | -1.73 | 3 | 2 |
| propeptide 36-164 | 129 | **9.51** | **+3.70** | 8 | 12 |
| mature chain 165-326 | 162 | **4.40** | **-10.78** | 21 | 11 |

This reproduces, from sequence alone, the claim that "At physiologic pH, the
N-terminal peptide is strongly positively charged, whereas the C-terminal portion
(ApoF) is negatively charged" (PMID:32520778), and it explains why ApoF was named
"a new acidic apolipoprotein" on isolation (PMID:204339). The computed
polypeptide pI of 4.40 sits just below the isoelectric points measured for the
mature glycoprotein, 4.6 (PMID:2715721) and 4.5 (PMID:19008531); these are not
the same quantity, since the measured values are for the sialylated protein, and
no adjustment has been applied to either.

The charge polarity is functionally relevant rather than incidental: what binds
LDL and inhibits CETP is the acidic mature chain, and LDL surface charge is a
documented modulator of that activity — "the negative charge of LDL surface
lipids, but not protein, is an important regulator of CETP and LTIP activity"
(PMID:12951364).

## 4. Exactly one N-glycosylation sequon survives propeptide removal

N-X-S/T sequons (X != Pro) in the precursor, in precursor numbering:

| segment | sequons |
|---|---|
| propeptide 36-164 | N118 (NAT), N139 (NVS) |
| mature chain 165-326 | **N267 (NIS)** — the only one |

UniProt annotates two carbohydrate features: N118 "N-linked (GlcNAc...)
asparagine" (evidence ECO:0000255, i.e. sequence-analysis prediction) and T274
"O-linked (GalNAc...) threonine" (experimental, PMID:22171320).

This computed inventory is confirmed experimentally, site for site, by work that
was published before the present analysis and found afterwards: "Human Apo F
contains three predicted N-linked glycosylation sites not found in the mouse
protein... Two of these sites are in the proprotein (N118 and N139), and one lies
in the mature peptide (N267)" (PMID:19008531). The same paper tested each site by
mutagenesis: "The proprotein in the media was glycosylated at both N118 and N139
... The mature form of Apo F appears to be variably glycosylated at N267, as
mutation of this residue abolished the upper band of the doublet in the media".

Two things follow. First, the only N-glycosylation site UniProt annotates lies at
position 118, **inside the propeptide**, so whatever glycan it carries is shed
with the propeptide and is not present on mature circulating ApoF. Second, N267 —
the one mature-chain sequon, and the one site shown by mutagenesis to be
glycosylated on the secreted mature protein — is **not annotated in UniProt at
all**, and neither is N139. N267 also lies inside the tryptic peptide DANISQPETTK
(precursor positions 265-275) that Kumar et al. had to exclude from their
quantitation assay because "it was glycosylated" (PMID:28935895), and that same
11-residue peptide contains the experimentally mapped O-GalNAc site T274. So the
mature chain carries an N-site and an O-site within eleven residues of each
other, both on the peptide that behaves anomalously in targeted proteomics.

The curation gap is therefore concrete: UniProt's glycosylation feature table for
Q13790 annotates one predicted site that cannot be on the mature protein, and
omits the two sites with experimental support on it.

## 5. ApoF has markedly less amphipathic helix than the classical apolipoproteins

Eisenberg mean hydrophobic moment `<uH>` over 18-residue sliding windows. "Strong
windows" are those with `<uH>` >= 0.40; the fraction of such windows measures how
much of the chain is amphipathic, which is what the literature claim is about,
rather than the single best window.

| protein (mature chain) | length | max `<uH>` | mean `<uH>` | strong windows |
|---|---|---|---|---|
| **APOF** 165-326 | 162 | 0.471 | **0.254** | **11/145 (7.6%)** |
| APOA1 19-267 | 249 | 0.535 | 0.330 | 51/232 (22.0%) |
| APOA2 19-100 | 82 | 0.548 | 0.346 | 32/65 (49.2%) |
| APOE 19-317 | 299 | 0.656 | 0.304 | 60/282 (21.3%) |
| APOC3 21-99 | 79 | 0.514 | 0.319 | 22/62 (35.5%) |

ApoF has the lowest mean moment and a 3- to 6-fold lower proportion of strongly
amphipathic windows than every control. This is consistent with, and quantifies,
the statement that ApoF is "predicted to lack strong amphipathic alpha helices
which are essential for the lipid binding properties of other HDL-associated
apolipoproteins such as apo A-I, apo A-II, apo E and the apo Cs" (PMID:22363685).

The peak moments are only modestly separated (0.471 vs 0.514-0.656), so the peak
statistic alone would not have supported the claim; it is the extent that
separates ApoF from the controls. This is a helical-wheel proxy, not a structural
determination: no experimental structure of ApoF exists.

## 6. ApoF is unrelated in sequence to the classical apolipoproteins

Smith-Waterman local alignment, BLOSUM62, gap open -11, extend -1.

Positive controls — ApoF orthologues, full precursors:

| pair | length | score | identity |
|---|---|---|---|
| APOF_HUMAN vs APOF_MOUSE (Q91V80) | 315 | 917.0 | 60.5% over 311 columns |
| APOF_HUMAN vs APOF_RAT (Q5M889) | 308 | 866.0 | 65.8% over 266 columns |

Classical apolipoproteins, mature chain vs mature ApoF:

| pair | length | score | identity |
|---|---|---|---|
| APOF vs APOA1 (P02647) | 249 | 28.0 | 31.2% over 32 columns |
| APOF vs APOA2 (P02652) | 82 | 31.0 | 25.4% over 67 columns |
| APOF vs APOE (P02649) | 299 | 36.0 | 37.5% over 48 columns |
| APOF vs APOC3 (P02656) | 79 | 41.0 | 25.5% over 51 columns |

Under identical settings the orthologue alignments score 866-917 over the full
length, while every classical-apolipoprotein comparison scores 28-41 over short
32-67 column fragments — the signature of chance local matches, not homology.
This independently confirms that ApoF "bears no structural or sequence similarity
to the other classical apolipoproteins" (PMID:22363685), and it is consistent
with PANTHER placing ApoF in its own single-subfamily family PTHR15011
("APOLIPOPROTEIN F") with no relationship to the apolipoprotein A/C/E families,
and with Pfam assigning it a dedicated family (PF15148, Apolipo_F).

## What this does and does not establish

Established here: the mature/precursor boundary arithmetic, the size of the
glycan-attributable mass gap, the charge dipole across the precursor, the sequon
inventory and its distribution either side of the cleavage site, the
amphipathicity deficit relative to four controls, and the absence of detectable
homology to the classical apolipoproteins.

Not established here: anything about how ApoF binds LDL or inhibits CETP. There
is no experimental structure of ApoF, no mapped LDL-binding surface and no mapped
CETP-inhibitory determinant, so no residue-level claim is made and none should be
read into these results.
