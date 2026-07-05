# Bioinformatics analysis of S. cerevisiae NIT1 (P40447 / YIL164C)

Reproducible pipeline: `just all` (see `justfile`). All scripts read their inputs
from `data/` at run time; no results are hardcoded in code.

## Question

NIT1 (P40447, YIL164C) is a 199-aa putative nitrilase-superfamily protein (carbon-
nitrogen hydrolase superfamily; Pfam PF00795 CN_hydrolase; PANTHER PTHR46044:SF1).
Three questions were addressed:

1. Is the nitrilase-superfamily **Glu-Lys-Cys (E-K-C) catalytic triad** intact?
2. Is NIT1 a **truncated / split ORF** (UniProt CAUTION: "Could be the product of a
   pseudogene. NIT1/YIL164C seems to be the N-terminal part of a putative nitrilase-
   like protein formed of NIT1/YIL164C and YIL165C")?
3. **Orthology** to human NIT1 / NIT2.

## Data

| Accession | Protein | Length | Role in analysis |
|-----------|---------|--------|------------------|
| P40447 | NIT1 / YIL164C (S. cerevisiae) | 199 | query |
| P40446 | YIL165C (S. cerevisiae) | 119 | adjacent ORF (putative C-terminal partner) |
| Q86X76 | human NIT1 (deaminated-glutathione amidase) | 327 | ortholog candidate |
| Q9NQR4 | human NIT2 (omega-amidase) | 276 | ortholog candidate |
| P32961 | Arabidopsis NIT1 (true nitrilase, IAN→IAA) | 346 | bona fide nitrilase outgroup |

Sequences fetched from UniProt REST (`data/*.fasta`).

## Methods

- `scripts/catalytic_triad.py` — reports the residue at each given 1-based position
  in a FASTA (positions supplied on the command line; not hardcoded).
- MAFFT `--auto` alignment of the five sequences (`results/combined.aln.fasta`).
- `scripts/analyze_alignment.py` — maps the reference's PROSITE-predicted triad
  positions to alignment columns and reports what every other sequence has in
  those columns, plus each sequence's non-gap span (truncation proxy).
- `scripts/test_split.py` — builds the artificial NIT1+YIL165C concatenation and
  aligns it with the real family members to test the split-ORF hypothesis.
- `scripts/pairwise_identity.py` — % identity of NIT1 to each homolog over
  co-aligned (gap-free) columns.

## Results

### 1. Catalytic triad is present in NIT1

PROSITE-predicted active sites map to **E44, K135, C169** in NIT1
(`results/nit1_triad.tsv`):

| position | residue | expected | context (±5) |
|----------|---------|----------|--------------|
| 44 | Glu (E) | E (proton acceptor) | LVVIP**E**ATLGG |
| 135 | Lys (K) | K (proton donor) | VGKHR**K**LMPTA |
| 169 | Cys (C) | C (nucleophile) | IGGAI**C**WENMM |

All three canonical nitrilase-superfamily triad residues are present at the
predicted positions. In the multiple alignment these three residues fall in the
same columns (87, 188, 232) occupied by the E-K-C triad of human NIT1, human NIT2
and Arabidopsis NIT1 (`results/alignment_analysis.txt`) — i.e. the triad is
**conserved and correctly positioned**. The nucleophilic Cys sits in the
family-diagnostic `GGAICWEN` motif.

Positive control (`results/nit2_triad_control.tsv`): running the same script on
human NIT2 at its own UniProt active-site positions (E43, K112, C153) correctly
returns E/K/C, confirming the script reads residues from whatever
sequence/positions it is given rather than returning a fixed answer.

### 2. NIT1 is the N-terminal ~2/3 of a nitrilase fold; YIL165C is the C-terminal ~1/3

Non-gap alignment spans (`results/split_test.txt`, `results/alignment_analysis.txt`):

| sequence | first col | last col | residues |
|----------|-----------|----------|----------|
| NIT1 / YIL164C | 1 | 270 | 199 |
| YIL165C | 271 | 406 | 119 |
| NIT1 + YIL165C (concat) | 1 | 406 | 318 |
| human NIT1 (Q86X76) | 1 | 406 | 327 |
| human NIT2 (Q9NQR4) | 1 | 386 | 276 |
| Arabidopsis NIT1 (P32961) | 1 | 406 | 346 |

In the split-test alignment, **NIT1 (cols 1–270) and YIL165C (cols 271–406) tile
the domain almost exactly end-to-end with no overlap**, and the 318-aa
concatenation spans the full 1–406 columns — the same span as the full-length
family members (human NIT1 327 aa; Arabidopsis 346 aa). The complete E-K-C triad
lies entirely within the NIT1 fragment (cols 87/188/232, all < 270); YIL165C
contributes only the C-terminal region downstream of the triad and carries none of
the triad residues (`-/-/-` at the triad columns).

**Interpretation.** This is strong sequence-level support for the UniProt CAUTION:
YIL164C + YIL165C together reconstitute one complete nitrilase-superfamily domain
of normal length, split across two adjacent annotated ORFs. NIT1 alone, although it
retains all three catalytic residues, is **missing the C-terminal ~1/3 of the
fold**. In characterised nitrilase-superfamily enzymes the C-terminal region
contributes to the α-β-β-α sandwich fold and to the oligomerisation interfaces
required for activity, so a fragment ending at the equivalent of column ~270 is very
unlikely to fold into an active enzyme on its own. Whether YIL164C+YIL165C are
translated as one protein (e.g. via a sequencing error, frameshift, or read-through
that the reference genome splits) or are a genuinely disrupted pseudogene cannot be
resolved from sequence alone.

### 3. Orthology / identity

Percent identity of NIT1 over co-aligned columns (`results/pairwise_identity.tsv`):

| homolog | % identity | co-aligned positions |
|---------|-----------|----------------------|
| Arabidopsis NIT1 (true nitrilase) | 47.2 | 195 |
| human NIT1 | 30.6 | 170 |
| human NIT2 | 25.6 | 172 |
| YIL165C | 50.0 | 2 (non-overlapping — not meaningful) |

NIT1 shows the expected carbon-nitrogen-hydrolase-superfamily level of similarity to
all three reference enzymes (~25–47% over the aligned catalytic core). It is not
markedly closer to human NIT1 than to human NIT2, and both yeast ORFs sit in the
uncharacterised PANTHER subfamily **PTHR46044:SF1 "CN hydrolase domain-containing
protein"** — i.e. **not** in the substrate-defined subfamilies of the same family
(SF14 arylacetonitrilase, SF4 cyanide hydratase, SF11 nitrilase-1-related). A clean
1:1 orthology assignment to a specific human paralog is therefore not supported;
NIT1 is a divergent fungal member of the superfamily whose substrate-specific
subfamily is undefined.

## Bottom line

- The **E-K-C catalytic triad residues are individually intact** in NIT1 (E44, K135,
  C169), conserved and correctly positioned relative to characterised family members
  — so NIT1 is **not** a triad-loss pseudoenzyme.
- However, NIT1 encodes only the **N-terminal ~2/3 of a nitrilase-superfamily
  domain**; the C-terminal third is separately annotated as YIL165C, and the two
  concatenate to a full-length domain. NIT1 as annotated is therefore a **truncated
  fragment** unlikely to be an active enzyme on its own, consistent with the UniProt
  pseudogene CAUTION and its PE=5 ("Uncertain") status.
- **No specific catalytic substrate can be assigned.** The intact triad argues the
  ancestral fold was catalytic, but membership in the uncharacterised PTHR46044:SF1
  subfamily (not a substrate-defined branch) and the truncation mean the physiological
  activity — if any — is **unknown**. A generic "nitrilase activity" assignment is not
  supported by these data.

## Checklist

- [x] Scripts use no hardcoded inputs/outputs (all positions/paths passed as args;
      concatenation computed at run time).
- [x] Triad script tested on a second, unrelated input (human NIT2 positive control
      returns the correct E/K/C).
- [x] Analyses completed as expected (MAFFT + all scripts ran; outputs in `results/`).
- [x] Direct script outputs are in `results/`.
- [x] Summary includes provenance and justification; uncertainty explicitly stated
      where sequence alone cannot resolve the question (translation vs pseudogene).
