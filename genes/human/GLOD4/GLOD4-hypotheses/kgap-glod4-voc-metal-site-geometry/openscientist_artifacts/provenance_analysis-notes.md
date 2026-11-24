# Provenance notes: kgap-glod4-voc-metal-site-geometry

All computation was run inside the `execute_code` Python executor. The executed code and its
raw stdout are preserved in the session analysis log; the numeric results are reproduced here
so that each claim in `final_report.md` can be traced to the call that produced it.

## Environment constraints encountered, stated plainly

1. **Phenix could not be used.** `run_phenix_tool` and `compare_structures` read host-side files
   inside the job directory. Host-side network access is blocked (a `curl` to the AlphaFold
   endpoint returned a 403 HTML page of 134 bytes), so no PDB or mmCIF file could be written into
   the job directory for Phenix to read. Network access works only from inside the `execute_code`
   executor, whose filesystem is separate from the job directory and does not persist between
   calls. Consequence: `phenix.superpose_pdbs` and `phenix.molprobity` were not run. All
   superposition, SASA and alignment code was therefore hand written in numpy.
2. **biopython is not importable** in this executor despite being listed in the tool description.
   `import urllib.request` is also blocked by the import allowlist; `requests` works.
3. **The executor filesystem does not persist between calls.** Every script re-downloads its
   structures from RCSB and AlphaFold DB.
4. **AlphaFold DB model versions v3 and v4 return 404** for Q9HC38. The working URL is
   `https://alphafold.ebi.ac.uk/files/AF-Q9HC38-F1-model_v6.pdb`.
5. **PDB 1JC5 (methylmalonyl-CoA epimerase) contains no metal ion.** The MCEE arm of the
   superposition requested in the seed hypothesis could not be performed against a metal-bound
   reference, and no metal-bound human MCEE structure was found.
6. **No full text was retrieved for PMID 41628334.** Only the PubMed abstract was available
   through the provided tooling. The abstract does not mention the metal site, His8, Glu70 or
   Cys254.

## Structures used

| PDB / model | Content | Role |
|---|---|---|
| 9CSJ | Human GLOD4 residues 2-298 (isoform 2 numbering), 3 chains, 5 Zn, multiple Cl | primary metal-bound GLOD4 structure |
| 3ZI1 | Human GLOD4, metal free | apo control, tests whether the site is preformed |
| 1QIN | Human glyoxalase I (GLO1), Zn | catalytic VOC reference |
| 1LQK | FosA fosfomycin resistance protein, Mn | catalytic VOC reference |
| 1JC5 | Methylmalonyl-CoA epimerase | requested reference, contains no metal, not usable |
| AF-Q9HC38-F1-model_v6 | AlphaFold GLOD4, 313 aa (isoform 1 numbering) | predicted model |

## Methods implemented from scratch in numpy

- Fixed-column PDB parser, altloc A or blank only.
- Kabsch superposition by SVD with a determinant sign correction.
- TM-align style iterative superposition: gapless-threading seeds, score matrix
  `1 / (1 + (d/d0)^2)` with `d0 = 1.24*(L-15)^(1/3) - 1.8`, vectorised linear-gap
  Needleman-Wunsch using the running-max identity `F[i] = cummax(G - gap*j) + gap*j`,
  iterated to convergence.
- Shrake-Rupley solvent accessible surface area, 960-point Fibonacci sphere, probe 1.4 A,
  standard van der Waals radii, metal occluded by protein atoms only (waters and ions excluded
  so that the measurement reports pocket enclosure rather than solvent modelling).
- BLOSUM62 affine-gap global alignment (open -11, extend -1) for ortholog position scoring.

## Raw results

### PDB 9CSJ, all five zinc sites, recomputed in the final call

| chain | site | protein ligands | first shell (A) | metal SASA (A^2) | % exposed | Zn B | nearest Cys SG (A) |
|---|---|---|---|---|---|---|---|
| A | His8/Glu70 VOC | 2 | GLU70 OE1 1.98, CL305 2.08, HIS8 NE2 2.13, CL310 2.19 | 13.86 | 14.2 | 35.72 | Cys254 5.09 |
| B | His8/Glu70 VOC | 3 | HIS8 NE2 2.12, CL305 2.13, GLU70 OE2 2.21, CL306 2.25, GLU70 OE1 2.42 | 13.55 | 13.9 | 35.58 | Cys254 5.14 |
| C | His8/Glu70 VOC | 2 | GLU70 OE1 1.86, HIS8 NE2 2.09, CL303 2.24 | 17.73 | 18.1 | 57.84 | Cys254 5.13 |
| A | single-His surface | 1 | HIS66 NE2 1.94, CL309 2.14, CL308 2.29 | 36.17 | 37.0 | 30.27 | Cys182 13.19 |
| A | single-His surface | 1 | HIS291 NE2 1.94, CL306 2.13, CL307 2.30 | 42.80 | 43.8 | 29.28 | Cys45 14.80 |

Mean protein B-factor in 9CSJ: 51.9.

Correction to an earlier statement made during the investigation: the zinc B-factor range is not
35.6-35.7 across all three VOC sites. Chains A and B are 35.7 and 35.6, below the protein mean,
but chain C is 57.8, above it. Chain C is also the chain whose zinc has only one modelled
chloride and the largest SASA. The B-factor argument therefore supports full occupancy in chains
A and B and partial occupancy in chain C.

### Catalytic VOC reference metals, same SASA method

| metal | SASA (A^2) | % exposed |
|---|---|---|
| GLO1 1QIN Zn chain A | 3.46 | 3.5 |
| GLO1 1QIN Zn chain B | 3.16 | 3.2 |
| FosA 1LQK Mn chain A | 12.69 | 11.1 |
| FosA 1LQK Mn chain B | 12.81 | 11.2 |

GLOD4 (13.6-17.7 A^2) brackets FosA and is far less exposed than the two single-His surface
zincs in its own crystal (36.2 and 42.8 A^2). GLO1 is the most deeply buried of the three.

### Cross-superposition of GLOD4 onto metal-bound VOC enzymes

After TM-align style superposition of 9CSJ chain A:

| reference | metal offset after superposition | residue mapped onto GLOD4 Cys254 | CA-CA (A) | residue mapped onto GLOD4 Arg201 |
|---|---|---|---|---|
| human GLO1 1QIN | GLOD4 Zn 1.64 A from GLO1 catalytic Zn | GLO1 Glu172 | 0.55 | GLO1 His126 |
| FosA 1LQK | GLOD4 Zn 1.65 A from FosA catalytic Mn | FosA Glu110 | 0.99 | FosA His64 |

GLO1 Glu172 is both a zinc ligand and the catalytic base of glyoxalase I.

### Second-shell environment of the GLOD4 zinc, chain A

Cys254 SG to the chloride occupying an open coordination position: 3.96 A.
Cys254 SG neighbours: Ile244 3.45, Phe255 N 3.53, Val242 3.74, Ala203 4.73 A (apolar pocket).
Cationic residues lining the open face of the metal: Lys55 NZ 4.86, Arg201 NH2 5.24,
Arg33 NH1 6.67 A.

### Apo control

3ZI1, metal free, same salt system: His8 NE2 to Glu70 OE1 = 3.10 A.
9CSJ metal bound: 2.78-3.27 A across the three chains. The site is preformed.

### Crystallization and purification chemistry

9CSJ REMARK 280 and the deposition record: GLOD4 residues 2-298 with a cleavable N-terminal
8-His tag, expressed in E. coli, purified by IMAC then size exclusion, stored in
50 mM HEPES pH 7.5 / 500 mM NaCl / 5% glycerol, crystallized in 34% PEG 3350 / 200 mM MgCl2 /
50 mM HEPES pH 7.3. 3ZI1: 0.2 M MgCl2 / 0.1 M HEPES pH 7.5 / 25% PEG 3350.
No zinc salt appears in either record. The chlorides are accounted for by MgCl2 and NaCl.

### AlphaFold model

AF-Q9HC38-F1-model_v6, 313 aa, isoform 1 numbering. Mean pLDDT 89.4.
Site residues: His8 98.4, Glu70 (model residue 85) 96.3, Arg201 (216) 97.5,
Cys254 (269) 98.3, Lys55 (70) 90.1.
Isoform-1-specific segment 32-62: mean pLDDT 49.8.
Superposition on 9CSJ chain A: 282 CA pairs, RMSD 1.92 A, 92% of pairs within 2 A.
His8 NE2 to Glu70 OE1: 5.17 A in the model, 3.27 A in 9CSJ chain A, 3.10 A in apo 3ZI1.
Zinc position transferred by superposition: 1.99 A from AF His8 NE2, 3.74 A from AF Glu70 OE1.

### Isoform numbering

Q9HC38-1 (UniProt canonical) is 313 aa and carries `ESCSVARLECSGAISAHCSDYTRITEDSFSK` at 32-62.
Q9HC38-2 is 298 aa and carries `LRHEEFEEGCKAACNG` at 32-47.
Offset map: position i in isoform 2 equals position i in isoform 1 for i <= 31, and i+15 for
i >= 48. Canonical equivalents of the hypothesis residues: His8 stays His8, Glu70 becomes
Glu85, Cys254 becomes Cys269. Under isoform 1 numbering, positions 70 and 254 are Lys and Thr.

MANE Select: ENST00000301329.11 / NM_016080.4 / NP_057164.3 / CCDS32520.1 encodes Q9HC38-2.
UniProt canonical Q9HC38-1 corresponds to ENST00000301328.9 / NP_001353176.1 / CCDS92216.1.

Ortholog residues 28-52, all matching the isoform-2 segment:

```
F6VS00 macaque      GMKVLRHEEFEEGCKAACNGPYDGK
Q5I0D1 rat          GMQVLRHEEFEEGCKAACNGPYDGK
G1N587 turkey       GMSVLRHEEFDEGCKASCNGPYDGK
A7RM33 Nematostella GMKVLRHEEFEKGCDAACNGPYDGK
E9H280 Daphnia      GMKILRHEEFEEGCKAACNGPYDGK
C3Z4C4 amphioxus    GMKVLRHEEFEEGCKASCNGPYDGR
human isoform 1     GMKVESCSVARLECSGAISAHCSDY   (matches none)
```

Withdrawn statement: an AlphaFold pLDDT value reported during the investigation for "Arg33"
was wrong. Arg33 of isoform 2 lies inside the isoform-2-specific segment and has no equivalent
residue in isoform 1, so the offset map pointed at His48 of isoform 1. That line is retracted.
No pLDDT value for Arg33 can be read from AF-Q9HC38-F1, because the model is built on isoform 1.

### Conservation

Scored by BLOSUM62 affine-gap global alignment to Q9HC38-2 and reading the aligned column.

| position | 196 vertebrate GLOD4 orthologs | 106 non-vertebrate metazoan homologs (UniRef50_Q9HC38, 56-72% identity) |
|---|---|---|
| His8 | 95.1% | 100% |
| Glu70 | 98.0% | 100% |
| Lys55 | 97.9% | 100% |
| Arg201 | 99.0% | 100% |
| Arg33 | 98.4% | 99.0% |
| Cys254 | 98.0% | 99.0% |

Non-vertebrate set composition: 92 Arthropoda, 4 Platyhelminthes, 3 Cephalochordata,
2 Cnidaria, 2 Mollusca, 1 Porifera, 1 Nematoda.

Pseudo-symmetric positions in the second VOC module of human GLOD4: Lys140, Glu185, Gly88,
Tyr126. No metal is modelled at that site in any chain of 9CSJ or in 3ZI1.

### GO baseline, QuickGO annotation API, geneProductId=UniProtKB:Q9HC38

Four annotations, nothing else:

| GO ID | aspect | term | evidence | reference |
|---|---|---|---|---|
| GO:0045296 | MF | cadherin binding | HDA | PMID:25468996 |
| GO:0005739 | CC | mitochondrion | IEA | GO_REF:0000044 |
| GO:0005739 | CC | mitochondrion | HTP | PMID:34800366 |
| GO:0070062 | CC | extracellular exosome | HDA | PMID:23533145 |

### GO ontology search for nitration terms

A QuickGO ontology search for "nitration" returns no terms. The nearest existing terms are
GO:0017014 protein nitrosylation ("the covalent addition of a nitric oxide group to an amino
acid within a protein") and GO:0018119 peptidyl-cysteine S-nitrosylation. Neither describes
tyrosine nitration, which adds a nitro group to the aromatic ring. GO:0072541 peroxynitrite
reductase activity and GO:0062213 peroxynitrite isomerase activity exist but describe
consumption of peroxynitrite without transfer of the nitro group to a protein acceptor.
There is therefore no GO term that captures the activity reported in PMID:41628334.

## Iteration 3: human VOC paralog comparison

Method: each human VOC-fold AlphaFold v6 model was superposed onto PDB 9CSJ chain A with the
same TM-align style routine, the GLOD4 His8/Glu70 zinc position was transferred into the aligned
frame, and every N, O or S atom within 6 A was listed, keeping the closest donor per residue.
AlphaFold models are apo, so donor distances are displaced outward; the residue identity at the
position is the readout, not the distance.

| symbol | accession | length | mean pLDDT | TM vs 9CSJ:A | aligned CA | residues at the transferred GLOD4 zinc (A) |
|---|---|---|---|---|---|---|
| GLOD4 (control) | Q9HC38 | 313 | 89.4 | 0.957 | 298 | H8:NE2 2.06; E85:OE2 3.05; K70:NZ 4.58; C269:SG 5.44; R216:NH1 5.54 |
| GLOD5 | A6NK44 | 160 | 90.0 | 0.613 | 155 | C104:SG 4.12; E153:OE2 4.14; T133:O 4.93 |
| GLO1 | Q04760 | 184 | 95.4 | 0.356 | 184 | E173:OE2 2.62; H127:NE2 4.40; G129:N 5.46 |
| MCEE | Q96PE7 | 176 | 86.9 | 0.333 | 174 | H50:NE2 0.71; H122:NE2 2.92; E172:OE2 2.96; E97:OE2 3.96; C124:SG 4.29 |
| HPD | P32754 | 393 | 95.7 | 0.380 | 296 | H183:NE2 1.35; E349:OE2 2.92; Q334:NE2 4.02; H266:NE2 4.22; R353:NH2 5.08 |

GLOD4 control residues are in isoform-1 (AlphaFold) numbering: E85 = Glu70, K70 = Lys55,
C269 = Cys254, R216 = Arg201 in isoform-2 numbering. GLO1 E173/H127 are the AlphaFold-numbered
catalytic Glu172 and His126 (AlphaFold retains the initiator Met). HPD H183/E349/H266 are its
Fe(II) 2-His-1-carboxylate facial triad.

TM-scores of 0.33-0.38 for GLO1, MCEE and HPD reflect global alignment of a small single-module
or differently-built protein over the full length of a 298-residue two-module protein. The
reported RMSD values over those full alignments (18-40 A) are correspondingly meaningless. The
informative output is that His and Glu donors from four independent sequences converge on one
point in space.

### GLOD5 register check

GLOD5 vs 9CSJ:A: TM 0.613, 155 aligned CA, 100 pairs within 4 A, covering GLOD4 residues 60-258.
Of those 100 pairs, 84 map into the C-terminal module (151-298) and 16 into the N-terminal
module (1-150). GLOD5 therefore aligns preferentially onto GLOD4's degenerate, metal-free module.

Position-by-position:

```
GLOD4 H8    -> no well-superposed GLOD5 equivalent
GLOD4 K55   -> no well-superposed GLOD5 equivalent
GLOD4 E70   -> no well-superposed GLOD5 equivalent
GLOD4 R201  -> GLOD5 D102   (CA offset 1.26 A)
GLOD4 C254  -> GLOD5 E153   (CA offset 1.20 A)
```

The GLOD5 C104 and E153 that appeared near the transferred zinc are a consequence of this
C-module register and do not represent a GLOD4-type site.

GLOD5 sequence (A6NK44, 160 aa):

```
   1 MLRHLPSRLPVKMWGRTLEKQSWRDSSQTPPPCLIRRLDHIVMTVKSIKDTTMFYSKILG
  61 MEVMTFKEDRKALCFGDQKFNLHEVGKEFEPKAAHPVPGSLDICLITEVPLEEMIQHLKA
 121 CDVPIEEGPVPRTGAKGPIMSIYFRDPDRNLIEVSNYISS
```

His positions: 4, 40, 83, 95, 117. Cys positions: 33, 74, 104, 121.
His4 lies inside the predicted N-terminal mitochondrial targeting segment and is not the
structural equivalent of GLOD4 His8, which sits in MAARRALHFVFKVGNRFQT (9CSJ chain A, 1-19).

Conclusion: GLOD5 cannot build the GLOD4 His8/Glu70 site within one chain, because it has only
the module that in GLOD4 carries no metal. Whether it could build an equivalent site across a
homodimer interface, as GLO1 and FosA do, is not tested by this analysis.
