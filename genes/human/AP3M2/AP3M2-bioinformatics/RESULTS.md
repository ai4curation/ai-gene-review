# AP3M2 (mu3B) bioinformatics results

All numbers below are computed at run time by `analyze.py` from live UniProt, PDBe/RCSB and Human Protein Atlas records. Nothing is hardcoded; re-running regenerates this file.

## 1. Human adaptor medium (mu) subunits

| symbol | accession | length | UniProt MHD domain |
|---|---|---|---|
| AP3M2 | P53677 | 418 | 176-417 |
| AP3M1 | Q9Y2T2 | 418 | 176-417 |
| AP1M1 | Q9BXS5 | 423 | 168-421 |
| AP1M2 | Q9Y6Q5 | 423 | 168-421 |
| AP2M1 | Q96CW1 | 435 | 170-434 |
| AP4M1 | O00189 | 453 | 184-452 |
| AP2M1_RAT (structure anchor) | P84092 | 435 | 170-434 |

### Pairwise global identity (%, BLOSUM62 global alignment)

| | AP3M2 | AP3M1 | AP1M1 | AP1M2 | AP2M1 | AP4M1 |
|---|---|---|---|---|---|---|
| AP3M2 | 100.0 | 84.2 | 29.7 | 31.6 | 29.1 | 24.5 |
| AP3M1 | 84.2 | 100.0 | 30.9 | 32.9 | 29.2 | 26.2 |
| AP1M1 | 29.7 | 30.9 | 100.0 | 79.7 | 40.6 | 30.8 |
| AP1M2 | 31.6 | 32.9 | 79.7 | 100.0 | 39.4 | 32.5 |
| AP2M1 | 29.1 | 29.2 | 40.6 | 39.4 | 100.0 | 31.0 |
| AP4M1 | 24.5 | 26.2 | 31.3 | 31.8 | 31.0 | 100.0 |

The matrix is computed per ordered pair, and where several alignments are equally optimal the two directions can pick different ones, so it is very slightly asymmetric: the largest difference between a cell and its transpose is 0.6 percentage points. Both values in such a pair are correct for their own direction; the AP3M2 row, which is the one the review cites, is unaffected either way.

AP3M2's closest human paralogue is **AP3M1** (84.2% identity). Identity to the AP-1 and AP-2 medium subunits is AP1M1 29.7%, AP1M2 31.6%, AP2M1 29.1%.

## 2. The AP-3 tyrosine-cargo site, observed and transferred

### 2a. mu3A residues that contact LAMP1 cargo in PDB 9C5B

9C5B is the human AP-3 holocomplex on a lipid nanodisc with the LAMP1 cytoplasmic tail engaged (chain Y, modelled sequence `SHAGYQTI`, which carries the GYQTI YxxPhi motif). The mu subunit in the structure is Q9Y2T2 (AP3M1/mu3A). Every mu3A residue with a heavy atom within 4.0 A of the cargo peptide is taken as the site: 9 residues qualify. Because AP3M1 and AP3M2 are 84.2% identical, transferring these positions to AP3M2 is a near-trivial alignment rather than a cross-family inference.

| AP3M1 pos | mu3A | AP3M2 pos | mu3B | identical? |
|---|---|---|---|---|
| 180 | Y | 180 | Y | yes |
| 181 | F | 181 | F | yes |
| 389 | V | 389 | V | yes |
| 392 | L | 392 | L | yes |
| 402 | F | 402 | F | yes |
| 403 | K | 403 | K | yes |
| 404 | G | 404 | G | yes |
| 405 | V | 405 | I | no |
| 406 | K | 406 | K | yes |

**AP3M2 is identical to AP3M1 at 8 of the 9 cargo-contacting positions**, with no deletions. The tyrosine-cargo site that the AP-3 cryo-EM structure resolves is therefore intact in the neuronal mu3B paralogue; there is no residue-level evidence that AP3M2 has lost cargo recognition.

### 2b. An independent AP-3 cargo complex: PDB 4IKN

4IKN is the Rattus norvegicus (Rat) mu3A C-terminal domain bound to the TGN38 cytoplasmic tail (chain B, modelled sequence `DYQRL`, carrying the DYQRL YxxPhi motif) - a different species and a different cargo from 9C5B, so it tests whether the site found there is structure-specific. 10 rat mu3A residues lie within 4.0 A of the peptide. Rat and human mu3A are 98.8% identical and rat mu3A and human mu3B are 84.2% identical.

| AP3M1_RAT pos | rat mu3A | human AP3M1 pos | mu3A | human AP3M2 pos | mu3B |
|---|---|---|---|---|---|
| 180 | Y | 180 | Y | 180 | Y |
| 181 | F | 181 | F | 181 | F |
| 182 | D | 182 | D | 182 | D |
| 389 | V | 389 | V | 389 | V |
| 392 | L | 392 | L | 392 | L |
| 402 | F | 402 | F | 402 | F |
| 403 | K | 403 | K | 403 | K |
| 404 | G | 404 | G | 404 | G |
| 405 | V | 405 | V | 405 | I |
| 406 | K | 406 | K | 406 | K |

Projected onto human AP3M1, the 10 contacts of 4IKN land on 10 positions, of which 9 are among the 9 that 9C5B shows contacting LAMP1 (shared: 180, 181, 389, 392, 402, 403, 404, 405, 406). Human AP3M2 carries the same residue as rat mu3A at 9 of the 10 positions. Two AP-3 structures, two different YxxPhi cargoes and two species therefore pick out the same site, and mu3B matches mu3A across it.

### 2c. Outgroup: the classical mu2 YxxPhi pocket (PDB 1BXX)

1BXX is the mu2 (AP50) C-terminal domain of Rattus norvegicus (Rat) bound to the TGN38 internalisation peptide (chain P, modelled sequence `DYQRLN`). 13 mu2 residues lie within 4.0 A of the peptide. Positions are in P84092 (AP2M1_RAT) numbering and are carried onto each human paralogue by pairwise alignment.

| P84092 pos | mu2 | AP3M2 | AP3M1 | AP1M1 | AP1M2 | AP2M1 | AP4M1 |
|---|---|---|---|---|---|---|---|
| 174 | F | Y180 | Y180 | F172 | F172 | F174 | F188 |
| 175 | L | F181 | F181 | L173 | I173 | L175 | L189 |
| 176 | D | D182 | D182 | D174 | D174 | D176 | D190 |
| 203 | K | C209 | C209 | R201 | K201 | K203 | K217 |
| 401 | V | V389 | V389 | V392 | V392 | V401 | V421 |
| 402 | R | N390 | N390 | R393 | R393 | R402 | R422 |
| 403 | Y | R391 | R391 | Y394 | Y394 | Y403 | F423 |
| 404 | L | L392 | L392 | L395 | M395 | L404 | L424 |
| 419 | I | F402 | F402 | L406 | L406 | I419 | - |
| 420 | K | K403 | K403 | P407 | P407 | K420 | K438 |
| 421 | W | G404 | G404 | W408 | W408 | W421 | W439 |
| 422 | V | I405 | V405 | V409 | V409 | V422 | V440 |
| 423 | R | K406 | K406 | R410 | R410 | R423 | R441 |

| paralogue | pocket positions identical to mu2 | of | % |
|---|---|---|---|
| AP3M2 | 4 | 13 | 31 |
| AP3M1 | 5 | 13 | 38 |
| AP1M1 | 10 | 13 | 77 |
| AP1M2 | 9 | 13 | 69 |
| AP2M1 | 13 | 13 | 100 |
| AP4M1 | 11 | 13 | 85 |

Positions where **every** human paralogue matches mu2: mu2 D176, mu2 V401 (2 of 13). Every other contact position has at least one paralogue that diverges.

AP3M2 aligns to 13/13 of the mu2 pocket positions, with no deletions, but matches mu2's residue at only 4 of them - fewer than AP1M1 (10), AP1M2 (9) or AP4M1 (11). The AP-3 medium subunits have diverged substantially from the AP-2 signal pocket even though, per section 2a, they bind tyrosine cargo through the structurally equivalent region.

### 2d. Do the alignment and structure routes agree?

Projecting the 13 mu2 pocket positions onto AP3M1 by alignment lands on 13 AP3M1 positions, of which 9 are among the 9 positions the 9C5B structure actually shows contacting LAMP1 cargo (overlap: 180, 181, 389, 392, 402, 403, 404, 405, 406). The alignment-only route and the structure-observed route therefore identify the same site, which is the check that the cross-family alignment in 2c is not drifting.

## 3. The mu-linker amphipathic helix

Begley et al. 2024 (PMID:39705307) report a membrane-inserting amphipathic helix in the mu3 linker of human AP-3. Below, the highest-hydrophobic-moment 18-residue window starting in the 45 residues that precede each protein's own UniProt MHD domain, using the Eisenberg consensus scale at 100 degrees per residue.

| symbol | window (start-end) | sequence | <H> | <uH> |
|---|---|---|---|---|
| AP3M2 | 139-156 | `ILRTVVNTITGSTNVGDQ` | +0.10 | 0.487 |
| AP3M1 | 138-155 | `TILRSVVNSITGSSNVGD` | +0.12 | 0.450 |
| AP1M1 | 133-150 | `EYITQEGHKLETGAPRPP` | -0.16 | 0.433 |
| AP1M2 | 140-157 | `NKLETGKSRVPPTVTNAV` | -0.14 | 0.373 |
| AP2M1 | 139-156 | `KSQHQTKEEQSQITSQVT` | -0.41 | 0.227 |
| AP4M1 | 139-156 | `VVSKPFSLFDLSSVGLFG` | +0.44 | 0.161 |

AP3M2 <uH> = 0.487 versus AP3M1 0.450; the AP-1/AP-2 subunits score AP1M1 0.433, AP1M2 0.373, AP2M1 0.227 and AP4M1 0.161. The two mu3 proteins hold the top two hydrophobic moments. Mean hydrophobicity is positive for AP3M2 (+0.10), AP3M1 (+0.12), AP4M1 (+0.44) - so a positive <H> alone does not separate mu3 from the rest, and it is the moment that does.

## 4. AP3M2 isoform 2 (P53677-2)

- VAR_SEQ 268-273: NLVAIP -> KCCLGM (in isoform 2)
- VAR_SEQ 274-418: Missing (in isoform 2)

The MHD of AP3M2 spans 176-417 of 418 residues, so the isoform-2 variant removes the C-terminal portion of the very domain that carries the sorting-signal site analysed in section 2. Of the 9 cargo-contacting positions, isoform 2 deletes 7 (389, 392, 402, 403, 404, 405, 406) and retains 2 (180, 181), which lie N-terminal to the truncation.

## 5. Is human AP3M2 neuron-restricted?

Human Protein Atlas fields for ENSG00000070718:

- **RNA tissue specificity**: Low tissue specificity
- **RNA tissue distribution**: Detected in all
- **RNA single cell type specificity**: Cell type enhanced
- **RNA single cell type specific nCPM**: {'Differentiating spermatogonia': '82.0', 'Late spermatids': '110.1', 'Melanocytes': '103.5', 'T-cells': '88.5'}
- **RNA single cell type group specific nCPM**: {'Pigment cells': '103.5', 'Spermatogenic cell types': '110.1'}
- **RNA single nuclei brain specificity**: Low cell type specificity
- **RNA brain regional specificity**: Low region specificity
- **Tissue expression cluster**: Cluster 46: Brain & retina - Neuronal signaling

