# Gpdh3 re-review bioinformatics (2026-10-21)

Scripts: `compare_isoforms_rereview.py` (output `output_rereview.txt`) and
`survey_orthologs_rereview.py` (output `survey_output_rereview.txt`). Both fetch
sequences live from the UniProt REST API; the isoform/active-site comparison uses MAFFT
(L-INS-i) on the first 400 residues.

## 1. Isoform identity of E1JIT1

E1JIT1 is Gpdh3-PB (1291 aa). Gpdh3-PA (Q8IN06, 1304 aa) is the PANTHER tree leaf for the
gene and Gpdh3-PC (Q9VD20, 1303 aa) is the third product. None of the three is Swiss-Prot reviewed.
Relative to PA and PC, PB replaces the 14-residue segment EFPLFTAIHLICQS (PA residues 318-331)
by a single D at residue 318, immediately after the Pfam C-terminal GPDH domain (194..312);
PC additionally lacks one S. The N-terminal ~317 residues and the long C-terminal extension are
identical among the three products.

Q8IN06: replace E1JIT1[317:318]='D' -> Q8IN06[317:331]='EFPLFTAIHLICQS'

## 2. Catalytic and NAD-binding positions (vs human GPD1 P21695 and fly Gpdh1 P13706)

| GPD1 position (UniProt role) | human GPD1 | fly Gpdh1 | Gpdh3 (E1JIT1) |
|---|---|---|---|
| 12 (NAD; middle Gly of GxGxxG) | G12 | G13 | E13 |
| 120 (substrate) | K120 | K121 | K120 |
| 204 (ACT_SITE, proton acceptor) | K204 | K206 | T205 |
| 269 (substrate + NAD) | R269 | R270 | K269 |
| 270 (substrate) | N270 | N271 | N270 |
| 296 (NAD) | K296 | K297 | K296 |

Catalytic-loop window: human `TVEICGALKNVVAVGAGF`, fly Gpdh1 `AVEVCGALKNIVACGAGF`,
Gpdh3 `GVELCGTLTDVVALGAGF` (the catalytic lysine of the ALKN motif is a threonine and the
following asparagine an aspartate). NAD loop: human `GSGNWG`, Gpdh1 `GSGNWG`, Gpdh3 `GAEGWG`.

Identical aligned residues E1JIT1 vs P13706 over the first 400 aa: 160 (~45% of the ~355-residue
GPDH core).

## 3. Lineage distribution of the substitutions (long Drosophilid PTHR11728 members)

The NAD-loop glutamate (GxExxG in place of GxGxxG) is present in every long Gpdh3 ortholog
recovered (melanogaster, simulans, mauritiana, yakuba, erecta, suzukii, rhopaloa, ananassae,
kikkawai, pseudoobscura, persimilis, madeirensis, willistoni, virilis, mojavensis, arizonae,
hydei, grimshawi, albomicans, busckii, lebanonensis), so it is an ancestral feature of the
Gpdh3 lineage.

The catalytic lysine is retained (`CGTLKD`) in D. pseudoobscura, D. persimilis, D. madeirensis,
D. willistoni and D. lebanonensis, but replaced in the melanogaster group: T in D. melanogaster,
D. simulans, D. mauritiana, D. yakuba, D. erecta and D. rhopaloa; S in D. suzukii; N in
D. kikkawai. In D. melanogaster the threonine is present in all cDNA- and genome-derived entries
(Q6NP03, C3KKB8, H1UUR6, Q8IN06, Q9VD20, E1JIT1), so it is not a single gene-model artefact.

## Interpretation

Gpdh3 is a long, fast-evolving, testis-biased member of PTHR11728:SF8 whose GPDH core has an
ancestrally altered NAD-binding glycine loop and, in the D. melanogaster lineage specifically, has
lost the lysine that UniProt annotates as the GPD1 proton acceptor. Canonical NAD-dependent
glycerol-3-phosphate dehydrogenase activity therefore cannot be assumed for D. melanogaster
Gpdh3 from family membership; it is untested, and these substitutions make it doubtful. No assay
of any Gpdh3 product has been reported.

Limitations: motif windows are located by flanking-motif string search (not a full alignment);
orthology of the long Drosophilid members is inferred from PANTHER PTHR11728 membership,
length (>=900 aa) and the shared N-terminal motif, not a phylogeny. The role of D260 and the
14-residue PA/PB difference was not assessed functionally.
