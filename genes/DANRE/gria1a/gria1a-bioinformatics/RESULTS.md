# gria1a / gria1b protein, expression and synteny comparison

Script: `pair_analysis.py` (run from the repo root with
`uv run python genes/DANRE/gria1a/gria1a-bioinformatics/pair_analysis.py > genes/DANRE/gria1a/gria1a-bioinformatics/output.txt`).
Raw output: `output.txt` (run 2026-09-28). Zebrafish sequences come from the cached UniProt records
(gria1a Q71E65, 914 aa; gria1b E7F1V8, 917 aa). Human GRIA1 (P42261) and GRIA2 (P42262) come from
UniProt; the gar and medaka proteins are the Ensembl canonical proteins of the orthologs that
Ensembl Compara assigns. Alignments: Biopython global, BLOSUM62, gap open -10, extend -0.5;
identity = identical columns / alignment length. Human positions are UniProt precursor numbering
(signal peptide 1-18), so human S849 and S863 are the mature-protein S831 and S845.

## Orthology and duplication node (Ensembl Compara)

- gria1a (ENSDARG00000021352, chr14) and gria1b (ENSDARG00000032714, chr21) are within-species
  paralogues with the duplication node at Osteoglossocephalai.
- Both share one spotted gar ortholog (ENSLOCG00000009807) and one human ortholog, GRIA1.
- Medaka has a one-to-one ortholog of each copy (ENSORLG00000007719 for gria1a, ENSORLG00000022427
  for gria1b), so both copies were kept in the two lineages.

## Protein

| Comparison | Identity |
|---|---|
| gria1a vs gria1b | 82.5% (920 columns) |
| gria1a / gria1b vs human GRIA1 | 74.4% / 71.0% |
| gria1a / gria1b vs gar GRIA1 | 88.3% / 81.7% |
| medaka gria1a / medaka gria1b ortholog vs gar GRIA1 | 87.4% / 71.6% |

Per region of human GRIA1 (identical residues / region length):

| Region (UniProt features of P42261) | gria1a | gria1b | gar |
|---|---|---|---|
| Extracellular N-terminal part (19-536) | 70.8% | 68.7% | 72.6% |
| M1, pore loop, M3 (537-630) | identical except cytoplasmic loop 558-584 | same | same |
| Extracellular ligand-binding part (631-805) | 95.4% | 90.3% | 94.9% |
| M4 (806-826) | 95.2% | 95.2% | 95.2% |
| Cytoplasmic C-terminal tail (827-906) | 57.5% | 48.8% | 62.5% |

Both copies keep the six glutamate-binding residues, the pore loop and M2-M3 segment, and both palmitoylation cysteines of human GRIA1.
The pore loop and M2-M3 segment (human 585-612, FGIFNSLWFSLGAFMQQGCDISPRSLSG) are identical in human,
gar, both zebrafish copies and both medaka orthologs.

**C-terminal tail.** The human phosphoserines at S849 and S863 (mature S831 and S845) are kept in
gria1a, gar and medaka gria1a. In gria1b the S849 position is an isoleucine, and no serine aligns to
S863 (the region carries a short deletion relative to gria1a). The same differences are present in
every Ensembl gria1b translation. The medaka gria1b ortholog has a leucine at S849 but keeps a serine
at S863. The S849 change is shared by the gria1b lineage in zebrafish and medaka.
The PDZ-binding C-terminus is ATGL in human, ATGM in gar, ASGM in gria1a and medaka gria1a, TTGM in
gria1b and STGM in medaka gria1b; the L to M change predates the teleost duplication.

**Relative rate (gar outgroup):** of 903 gar positions aligned in both copies, 34 changed only in
gria1a and 86 only in gria1b (chi2 = 22.53, P < 0.05).
gria1b has changed significantly faster than gria1a since the duplication (86 vs 34 unique changes relative to gar).
The medaka gria1b ortholog is also strongly diverged from gar (71.6%) while medaka gria1a is not (87.4%),
so the faster evolution of the b copy began before the zebrafish-medaka split.

## Expression

**Whole-embryo time course (E-ERAD-475, median TPM).** Both copies are near zero until
segmentation, then rise; in 3-5-day larvae gria1a is at 12-14 TPM and gria1b at 5-6 TPM.
gria1a is about two to three times more abundant than gria1b in whole larvae.

**Bgee calls** (only "expressed" calls are returned; absence of a call is not evidence of absence).
Both copies: brain (81.0 / 79.6), retina (66.3 / 75.4), larva, embryo, testis (22.4 / 49.6).
gria1a only: bone element. gria1b only: mature ovarian follicle (65.2), spleen (64.7), pharyngeal
gill (31.4). Gar GRIA1: brain 87.7, eye 63.9, larva 62.0, ovary 34.8, bone 33.2, embryo 24.8.

**ZFIN curated in situ data** (all from Hoppmann et al. 2008, 24-72 hpf; plus whole-organism
RT-PCR records). gria1a has 26 anatomy terms and gria1b 20. 19 are shared: brain and whole organism
from the RT-PCR records, and 17 in situ terms (olfactory bulb, habenula, hypothalamus, preoptic area,
thalamus, ventral thalamus, tegmentum, optic tectum, medulla oblongata, retinal ganglion cell and
inner nuclear layers, motor and sensory neurons, spinal cord interneurons, and the early
dorso-rostral, ventro-rostral and ventro-caudal clusters).
Most in situ domains are shared; telencephalon, dorsal thalamus, rhombomeres, spinal cord and retinal ganglion cells are recorded for gria1a only and otic vesicle for gria1b only.

## Synteny

gria1a is on chr14 (34.1 Mb) and gria1b on chr21 (26.2 Mb). For each copy the script took all
protein-coding genes within 1.5 Mb and asked Ensembl for their zebrafish paralogues with a
teleost-level duplication node (Clupeocephala, Osteoglossocephalai or Teleostei).

- **No conserved neighbours within 1.5 Mb** in either direction (15 of 83 gria1a neighbours and 46 of
  102 gria1b neighbours have a teleost-level paralogue, but none of the partners lies near the other
  copy).
- **Chromosome level:** 6 teleost-level paralogue pairs from the gria1a neighbourhood have their
  partner on chr21 (lcp2, foxi3, afap1l1, adrb2, il12b, rnf145), and 11 from the gria1b neighbourhood
  have their partner on chr14 (including npas4, efemp2, fibp, fosl1, vegfb, stx5a, nxf1, bscl2).

The chr14 and chr21 regions share many teleost-level paralogue pairs, but they sit several Mb away
from the gria1 genes, so the local gene order has been rearranged. This is weaker synteny support
than a shared neighbour, and no background expectation was computed.

## Interpretation

- Protein: both copies keep the ligand-binding and channel-forming residues, so both should form
  AMPA receptors. gria1b has evolved faster, most visibly in its cytoplasmic tail, where it has lost
  a residue matching a mammalian CaMKII/PKC phosphorylation site (shared with medaka gria1b) and, in
  zebrafish only, the PKA site. Whether this changes regulation of the receptor is untested.
- Expression: largely overlapping neural expression, with gria1a higher in larvae and recorded in
  telencephalon and spinal cord, and gria1b with an otic vesicle domain and non-neural RNA-seq calls
  (ovary, spleen, gill).
