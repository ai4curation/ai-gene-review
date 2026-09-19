# ARHGAP36: the arginine finger UniProt annotates, and the residue that is there

Every number below is produced by `analyze_arhgap36.py` in this directory.
Re-run it to regenerate this file; do not hand-edit.

```
uv run --no-project --with "biopython>=1.85" python analyze_arhgap36.py
uv run --no-project --with "biopython>=1.85" python analyze_arhgap36.py --self-test
```

## 1. What the UniProt entry says about itself

| | |
|---|---|
| entry | `RHG36_HUMAN` (Q6ZRI8), 547 aa |
| Rho-GAP DOMAIN | 226..426 |
| annotated arginine-finger Site | **258** |
| evidence on that Site | `ECO:0000255` |
| residue actually at that position | **T** |
| FUNCTION comment asserting GAP activity | "GTPase activator for the Rho-type GTPases by converting them to an inactive GDP-bound state" |
| evidence on that comment | `ECO:0000250` |

The entry therefore annotates a catalytic arginine at 258 and carries T there, while asserting GTPase-activator activity on `ECO:0000250`. Both statements are rule- or similarity-derived; neither is experimental.

## 2. Is that Site in register?

A ProRule Site is placed by profile alignment and can be misplaced, so the position is re-derived from controls that carry their own annotated arginine finger. Each control's finger is projected onto ARHGAP36 Rho-GAP domain to Rho-GAP domain.

| control | entry | its own site | residue | projects onto ARHGAP36 | residue there | same as ARHGAP36's own Site |
|---|---|---|---|---|---|---|
| Q07960 | `RHG01_HUMAN` | 282 | R | **258** | **T** | **yes** |
| O54834 | `RHG06_MOUSE` | 435 | R | **258** | **T** | **yes** |
| O43182 | `RHG06_HUMAN` | 433 | R | **258** | **T** | **yes** |

Distinct positions the controls project onto: [258]. Unanimous: **yes**. Agrees with UniProt's own Site: **yes**.

Method control — every control projected onto every other control must recover a known arginine finger:

| from | to | projected | target's own site | recovered | residue |
|---|---|---|---|---|---|
| `RHG01_HUMAN` | `RHG06_MOUSE` | 435 | 435 | **yes** | R |
| `RHG01_HUMAN` | `RHG06_HUMAN` | 433 | 433 | **yes** | R |
| `RHG06_MOUSE` | `RHG01_HUMAN` | 282 | 282 | **yes** | R |
| `RHG06_MOUSE` | `RHG06_HUMAN` | 433 | 433 | **yes** | R |
| `RHG06_HUMAN` | `RHG01_HUMAN` | 282 | 282 | **yes** | R |
| `RHG06_HUMAN` | `RHG06_MOUSE` | 435 | 435 | **yes** | R |

## 3. Could the arginine simply have moved?

The only result that would rescue the annotation is an arginine displaced by a residue or two. A window of ±10 residues around position 258 was scanned.

| | |
|---|---|
| window | 248..268 |
| sequence | `KHGLSAVGIFTLEYSVQRVRQ` |
| arginines in window | [265, 267] |
| nearest arginine | 265 |
| offset from the annotated site | 7 |

## 4. Does the sequence record agree with the published residue?

PMID:33999959 names the equivalent position **T227**, in the numbering of whichever isoform that paper worked in. Rather than assume which, the site is recomputed under the canonical sequence and under every UniProt splice variant lying wholly upstream of it, and the published number is looked for among the results.

| variant | span | description | net offset | position of the site | residue | isoform length |
|---|---|---|---|---|---|---|
| `(canonical)` | — | isoform 1, displayed sequence | +0 | **258** | **T** | 547 aa |
| `VSP_021357` | 1..136 | in isoform 3 | -136 | **122** | **T** | 411 aa |
| `VSP_039235` | 1..48 | in isoform 5 | -48 | **210** | **T** | 499 aa |
| `VSP_021358` | 1..32 | in isoform 2 | -31 | **227** ← | **T** | 516 aa |
| `VSP_039236` | 1..31 | in isoform 4 | -12 | **246** | **T** | 535 aa |

Exactly one variant reproduces `T227`: `VSP_021358`. So the published residue and the UniProt Site are the same residue, reached by two independent routes — a profile-based annotation rule and a mutagenesis paper's own construct numbering — and the threonine call does not depend on either one alone.

## 5. Is the loss ARHGAP36's, or the family's?

| role | accession | entry | annotated site | residue |
|---|---|---|---|---|
| PAINT/IBD seed (MGI:1196332) | O54834 | `RHG06_MOUSE` | 435 | **R** |
| human paralog, same PANTHER family | O43182 | `RHG06_HUMAN` | 433 | **R** |
| binds a RHO GTPase without catalysing (reference) | Q01968 | `OCRL_HUMAN` | 757 | **Q** |
| retains R but is experimentally GAP-dead | Q3KRB8 | `RHGBB_HUMAN` | 87 | **R** |
| **query** | Q6ZRI8 | `RHG36_HUMAN` | 258 | **T** |

Across all reviewed human proteins carrying the PROSITE RhoGAP profile PS50238:

| | count |
|---|---|
| entries | 66 |
| with an annotated arginine finger | 66 |
| that position holds R | 60 |
| that position does not hold R | 6 |

Entries whose annotated arginine-finger position does not hold an arginine:

| entry | residue |
|---|---|
| `ARAP2_HUMAN` | Q |
| `DEP1B_HUMAN` | I |
| `FA13B_HUMAN` | Q |
| `I5P2_HUMAN` | Q |
| `OCRL_HUMAN` | Q |
| `RHG36_HUMAN` | T |

The query is among them: **yes**. The decoupling control (`RHGBB_HUMAN`) is **not** — it keeps its arginine and is nonetheless experimentally GAP-dead, so a retained arginine is not evidence of activity. The inference this report supports runs only in the other direction.

## 6. Catalysis versus binding

UniProt records an experimental RAC1 interaction via ARHGAP36's Rho-GAP domain. Losing the catalytic arginine does not by itself remove the binding surface, so the two are counted separately. The GAP:GTPase interface is taken from PDB 1TX4 (p50RhoGAP:RhoA:GDP:AlF4), as every GAP residue with an atom within 4.5 A of the GTPase or of the nucleotide/metal/fluoride.

Chain roles are proved, not assumed: chain A is 99.5% identical to Q07960 and chain B is 99.4% identical to P61586. The calculation recovers the control's own annotated arginine finger (282) among its contacts, as it must.

| | count |
|---|---|
| control GAP:GTPase contacts | 25 |
| inside the control's Rho-GAP domain | 25 |
| projected onto ARHGAP36 | 25 |
| unmapped (aligned to a gap) | 0 |
| identical residue in ARHGAP36 | 8 |

Projection in register (control's finger lands on ARHGAP36's own Site 258): **yes**.

| control pos | control res | ARHGAP36 pos | ARHGAP36 res | identical |
|---|---|---|---|---|
| 278 | E | 254 | V | no |
| 279 | G | 255 | G | **yes** |
| 282 | R | 258 | T | no |
| 283 | R | 259 | L | no |
| 284 | S | 260 | E | no |
| 285 | A | 261 | Y | no |
| 286 | N | 262 | S | no |
| 287 | T | 263 | V | no |
| 288 | Q | 264 | Q | **yes** |
| 309 | N | 285 | Q | no |
| 319 | K | 295 | K | **yes** |
| 323 | R | 299 | R | **yes** |
| 386 | K | 373 | R | no |
| 387 | M | 374 | M | **yes** |
| 391 | N | 378 | N | **yes** |
| 394 | V | 381 | L | no |
| 395 | V | 382 | V | **yes** |
| 398 | P | 385 | S | no |
| 399 | N | 386 | A | no |
| 406 | A | 397 | E | no |
| 407 | A | 398 | S | no |
| 409 | T | 400 | K | no |
| 410 | L | 401 | T | no |
| 413 | I | 409 | V | no |
| 417 | N | 413 | N | **yes** |

8 of 25 projected interface positions (32%) are identical in ARHGAP36. A percentage alone has no scale, so the same interface was projected onto `RHG06_MOUSE` (O54834), the PAINT/IBD seed, experimentally GAP-active — the member of this family whose experiments are the basis of the IBD under review. It scores 9/25 (36%).

So the GTPase-contacting surface is conserved in ARHGAP36 to a degree comparable to the family member that does catalyse, while the one residue that performs the catalysis is not conserved. That is the configuration in which a domain can still engage a GTPase without accelerating its hydrolysis — the shape `OCRL_HUMAN` is documented to have. This is a statement about what the structure permits, not a measurement of binding: the binding claim rests on the curated experiment, not on this table.
