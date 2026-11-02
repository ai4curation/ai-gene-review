# Donkey SNAP23 (A0A8C4M333): orthology, conservation and PAINT node placement

Analysis date: 2026-10-21.

## 1. Family and subfamily placement

The UniProt record for A0A8C4M333 assigns it to PANTHER PTHR19305 (SYNAPTOSOMAL ASSOCIATED
PROTEIN) and to subfamily PTHR19305:SF4 (SYNAPTOSOMAL-ASSOCIATED PROTEIN 23). Human SNAP23
(O00161) and mouse Snap23 (O09044) are in the same subfamily; human SNAP25 (P60880) is in a
different subfamily (PTHR19305:SF5) of the same family (see
`genes/EQUAS/SNAP23/SNAP23-bioinformatics/RESULTS-rereview.md`, section 2). A0A8C4M333 is the
product of Ensembl transcript ENSEAST00005020803 of donkey gene ENSEASG00005013173 and is
211 aa, the same length as human SNAP-23a (O00161-1). Domain signatures: two t-SNARE
coiled-coil homology domains (PROSITE PS50192, residues 14-76 and 146-208), Pfam PF00835
(SNAP-25), CDD cd15895 SNARE_SNAP23N and cd15884 SNARE_SNAP23C.

## 2. Sequence conservation (`align_to_orthologs.py`, output in `align_output.txt`)

```
uv run --script align_to_orthologs.py ../SNAP23__A0A8C4M333-uniprot.txt
```

Global alignment (BLOSUM62, gap open -10, extend -0.5) against sequences fetched live from UniProt:

| comparator | identical / shorter length |
|---|---|
| human SNAP23 O00161 (PTHR19305:SF4) | 189/211 (89.6%), gapless |
| mouse Snap23 O09044 (PTHR19305:SF4) | 193/210 (91.9%) |
| human SNAP25 P60880 (PTHR19305:SF5) | 132/206 (64.1%) |

The donkey protein is collinear with human SNAP23 with no indels. Residues conserved at
experimentally characterized human positions:

- Gln-48, the buried central glutamine of the SNAP-23 N-terminal coiled coil (PMID:12556468): conserved.
- The cysteine-rich cluster Cys-79, -80, -83, -85, -87, S-palmitoylated in human (UniProt
  O00161 LIPID features, PMID:21044946): all five conserved, consistent with the membrane
  lipid anchor. Human Cys-112 (also reported palmitoylated) is Ser in donkey.

Interpretation: by subfamily membership and conservation of both SNARE motifs and the
palmitoylation cluster, A0A8C4M333 is the donkey SNAP23 ortholog and is expected to act as a
plasma-membrane Qbc-SNARE. This is inference; no experimental study of donkey SNAP23 was found.

## 3. PAINT nodes behind the electronic annotations (QuickGO, queried 2026-10-21)

The IBA annotations of human O00161 and SNAP25 P60880 carry these PANTHER nodes in WITH/FROM:

| term | node (O00161) | node (P60880) |
|---|---|---|
| GO:0005484 helical-bundle zippering fusogenic activity (formerly SNAP receptor activity), GO:0006887 exocytosis, GO:0031201 SNARE complex | PTN000447753 | PTN000447753 |
| GO:0016082 synaptic vesicle priming, GO:0031629 synaptic vesicle fusion to presynaptic active zone membrane | PTN000447754 | PTN000447754 |
| GO:0005886 plasma membrane | PTN000447752 | PTN000447752 |
| GO:0019905 syntaxin binding (O00161) / GO:0017075 syntaxin-1 binding and GO:0070032 synaptobrevin 2-SNAP-25-syntaxin-1a-complexin I complex (P60880 only) | PTN000447753 | PTN002712515 |

The first non-PANTHER WITH/FROM entry returned by QuickGO is Drosophila Snap25 (FBgn0011288)
for most rows, mouse Snap25 (MGI:98331) for syntaxin binding, and Arabidopsis AT5G61210 for
plasma membrane (full donor lists were not retrieved). Because human SNAP23 and SNAP25 both
inherit from PTN000447754, the synaptic-vesicle terms sit at a node ancestral to the
SNAP23/SNAP25 split, while the
SNAP25-specific syntaxin-1 binding and neuronal SNARE-complex (VAMP2-SNAP25-STX1A-complexin I) terms were kept
at a SNAP25-lineage node (PTN002712515). The donkey TreeGrafter rows cite PANTHER:PTN001455290.
