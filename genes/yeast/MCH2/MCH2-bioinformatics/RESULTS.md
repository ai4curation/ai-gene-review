# MCH2 (YKL221W / P36032) bioinformatics analysis

Comparative and structural bioinformatics supporting the GO-annotation review of
*Saccharomyces cerevisiae* MCH2, a "dark" monocarboxylate-transporter (MCT/MFS)
homolog with no demonstrated transport substrate.

## Objectives

1. Confirm the MFS / monocarboxylate-porter (SLC16-like, TC 2.A.1.13) fold and the
   transmembrane-helix count.
2. Test whether conserved MCT/SLC16 functional residues and the MFS "motif A" are
   retained in MCH2, and whether a substrate can be inferred from motifs.
3. Place MCH2 within its family: pairwise identity to yeast paralogs (MCH1–MCH5,
   JEN1) and to the human SLC16/MCT family, and its closest relatives.

## Methods (reproducible)

- Sequences fetched programmatically from UniProt (`scripts/fetch_sequences.py`;
  accession lists in `data/accessions.tsv`, `data/accessions_test.tsv`). The fetched
  MCH2 sequence was byte-for-byte identical to the local `MCH2-uniprot.txt` sequence
  (473 aa) — verified.
- MSA with MAFFT (`--auto`).
- Pairwise % identity over columns where both sequences have a residue
  (`scripts/pairwise_identity.py`).
- Neighbor-joining tree, identity distance (Biopython; `scripts/build_tree.py`).
- UniProt TM/topology features parsed from the flat file
  (`scripts/parse_uniprot_topology.py`).
- Kyte–Doolittle hydropathy profile used ONLY to corroborate the hydrophobicity of
  each annotated TM helix (`scripts/hydropathy_corroboration.py`), not to count
  helices de novo (see caveat).
- Conserved-residue / motif scan anchored on human MCT1 (`scripts/motif_check.py`).
- Run everything with `just all` (needs `uv` and `mafft` on PATH).

## Results

### 1. Fold and transmembrane topology — CONFIRMED (12 TMS, MFS)

- UniProt annotates **12 transmembrane helices** with **cytoplasmic N- and C-termini**
  (`results/uniprot_topology.tsv`) — the canonical 12-TMS MFS architecture, including a
  large central cytoplasmic loop between TM6 and TM7 (TOPO_DOM 221–243). The N/C-in,
  even-TM topology was experimentally constrained for MCH2 in the yeast global topology
  map (PMID:16847258).
- All **12/12** annotated helices carry a positive Kyte–Doolittle hydropathy peak
  (`results/tm_hydropathy_corroboration.tsv`), independently corroborating that each
  annotated segment is genuinely hydrophobic.
- Domain assignments already in UniProt/InterPro (MFS PF07690 / IPR011701; CDD
  MFS_MCT_SLC16 cd17352; PANTHER PTHR11360 Proton-linked MCT) are consistent with this.
- **Conclusion:** MCH2 is a bona fide polytopic MFS membrane protein of the
  monocarboxylate-porter (SLC16/MCT-like) family. This is the firm, defensible part.

### 2. Functional-residue conservation — MCH2 DIVERGES from transporting MCTs; substrate NOT inferable

- The conserved TM1 lysine of human MCT1 (**Lys38**, verified at position 38 of P53985;
  implicated in the H⁺/lactate translocation pathway) is retained across the transporting
  monocarboxylate subfamily (MCT1/2/3/4/7 = SLC16A1/7/8/3/6 all have **K** at the aligned
  column). **MCH2 has Serine at this column** (`results/motif_conservation.tsv`). All four
  yeast MCH paralogs also lack the lysine (T/A/N/N), as do the aromatic-amino-acid / thyroid-
  hormone MCTs (MCT8, MCT10 have N).
- The canonical MFS "motif A" (G-x₃-[DE]-[RK]-x-G-[RK][RK], TM2–TM3 loop) is **not** found in
  MCH2 by either a strict or a relaxed regex, whereas a recognizable motif-A-like sequence IS
  present in paralogs MCH3 (`GLAGDKFGR`) and MCH5 (`GYLSDKFGR`). MCH2's motif A is degenerate.
- Objectively, MCH2 matches the family consensus at only **35 of 54** highly-conserved
  (≥70%) alignment columns (`results/conserved_columns.tsv`) — it retains a core MFS
  scaffold but is a divergent member.
- **Conclusion:** MCH2 does not conserve the residues that define the transporting
  monocarboxylate MCTs, so a substrate **cannot** be inferred from close motif similarity to
  any characterized MCT. This is consistent with the experimental finding that yeast Mch
  proteins do not transport monocarboxylic acids (PMID:11536335).
- CAVEAT: an initial attempt also anchored three further MCT1 residues (numbered 302/306/360
  from memory); those positions did **not** carry the expected D/R/F in the actual P53985
  sequence, so they were flagged MISMATCH and **excluded** from all interpretation. Only the
  independently verified Lys38 is reported. No residue claim rests on an unverified anchor.

### 3. Family placement — closest to paralog MCH3; distant from all characterized MCTs

Pairwise identity to MCH2 (`results/mch2_closest.tsv`), top hits:

| Rank | Protein | % identity to MCH2 |
|------|---------|--------------------|
| 1 | MCH3 (ESBP6, YNL125C) | 30.1 |
| 2 | SLC16A12 / MCT12 (human) | 22.7 |
| 3 | SLC16A10 / MCT10 / TAT1 (human) | 21.5 |
| 4 | SLC16A2 / MCT8 (human) | 20.5 |
| 5 | MCH4 | 20.2 |
| 6 | MCH5 (riboflavin transporter) | 19.6 |
| … | classical lactate MCT1/2/3/4 | 17.0 / 16.9 / 19.3 / 19.0 |
| 18 | JEN1 (yeast lactate transporter) | 15.1 |
| 19 | MCH1 | 12.1 |

- MCH2's single closest relative is its paralog **MCH3/ESBP6** (30%); all other identities
  are ≤23% (twilight zone).
- MCH2 is **not** specifically close to the well-characterized lactate/pyruvate transporters:
  human MCT1–MCT4 (SLC16A1/7/8/3) are at 17–19%, and yeast JEN1 (a real carboxylic-acid
  transporter) is only 15%. Where MCH2 has any preferential human similarity it is to the
  amino-acid / thyroid-hormone MCTs (MCT8/10/12), not the monocarboxylate ones — but at
  ~20–23% this is too low to assign substrate.
- The NJ tree (`results/panel_nj_ascii.txt`) places MCH2 with the yeast MCH paralogs and
  adjacent to the MCT8/MCT10 (amino-acid) clade, away from the MCT1–4 monocarboxylate clade.
  NB: at 15–30% identity NJ branch order is not statistically robust; treat the tree as
  corroborating the identity ranking, not as an independent phylogeny.

## Overall interpretation (for the GO review)

- **Confirmed:** MCH2 is a 12-TMS MFS protein of the SLC16/MCT (monocarboxylate-porter)
  family — supports the generic `transmembrane transporter activity` (GO:0022857),
  `transmembrane transport` (GO:0055085), and `membrane` (GO:0016020) annotations.
- **Not supported by sequence:** any specific substrate. MCH2 lacks the conserved TM1
  lysine and the MFS motif A of the transporting MCTs, and is distant (≤23%) from every
  functionally characterized transporter in the panel, including the classical
  monocarboxylate MCTs and yeast JEN1. Sequence analysis therefore **cannot** rescue a
  specific substrate, direction, or symport/uniport mechanism — consistent with the
  experimental negative result that yeast Mch proteins do not transport monocarboxylates
  (PMID:11536335) and with Mch5p (riboflavin) being the only paralog with a known substrate.
- **Net:** the molecular function is defensible only at the generic "transmembrane
  transporter" level; the substrate and biological process remain genuine knowledge gaps.

## Analysis checklist

- [x] Scripts contain NO hardcoded input sequences or hardcoded results (only UniProt
      accession IDs and literature-anchored residue positions are specified; all sequence
      data is fetched/aligned at run time).
- [x] Scripts tested on independent inputs: HXT1 UniProt file → 12 TM parsed correctly;
      MCH2-vs-HXT1 (13.4%) and MCH2-vs-CYC1 non-MFS control (12.5%) both correctly lower
      than MCH2's real relatives, confirming the identity metric discriminates.
- [x] Analyses completed as expected (`just all` runs clean end-to-end).
- [x] Direct script outputs are in `results/` (topology, hydropathy corroboration,
      identity matrix, ranked relatives, NJ tree, motif/conservation tables).
- [x] Summary includes provenance and justification, and is explicit about uncertainty.
- [~] De novo TM COUNTING by hydropathy is UNRELIABLE for closely packed MFS helices
      (the sliding-window method under-counts, calling 3–10 rather than 12 across the whole
      panel including known 12-TMS transporters). We therefore do NOT report a de novo TM
      count; the 12-TMS call rests on UniProt (ECO:0000255) + experimental topology
      (PMID:16847258), corroborated by 12/12 hydrophobic peaks. This limitation is by design,
      not a failure.

## Files

- `data/accessions.tsv`, `data/accessions_test.tsv` — accession lists (inputs; IDs only)
- `data/panel.fasta`, `data/test_panel.fasta` — fetched sequences
- `results/uniprot_topology.tsv` — 12 annotated TM helices + topology
- `results/tm_hydropathy_corroboration.tsv` — 12/12 helices hydrophobic
- `results/tm_predictions.tsv`, `results/tm_predictions_test.tsv` — de novo hydropathy TM (unreliable; see caveat)
- `results/panel_aln.fasta` — MAFFT alignment
- `results/identity_matrix.tsv`, `results/mch2_closest.tsv` — pairwise identity
- `results/panel_nj.nwk`, `results/panel_nj_ascii.txt` — NJ tree
- `results/motif_conservation.tsv`, `results/conserved_columns.tsv` — residue/motif conservation

## Tool versions / citations

- MAFFT (v7, `--auto`); Biopython 1.81; Kyte & Doolittle (1982) J Mol Biol 157:105.
- Functional MCT1 residue context: Wilson et al. (2009) J Biol Chem 284:20011.
- Sequence source: UniProt (2026 release).
