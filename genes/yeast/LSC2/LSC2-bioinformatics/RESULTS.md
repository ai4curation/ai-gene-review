# Evolution of the succinyl-CoA synthetase subunit families (LSC1 / LSC2)

Analysis: `scs_family_evolution.py` (run with `uv run --script scs_family_evolution.py --bootstraps 200`).
Machine-readable output: `results.yaml`; panel trees: `beta_panel_nj.nwk` (neighbor joining) and `beta_panel_ml.nwk` (maximum likelihood).
Inputs are fetched at run time: the PANTHER trees of PTHR11815 (beta subunit) and PTHR11117 (alpha subunit) from the PANTHER API (release 19), and 42 beta-subunit sequences from UniProt.
This analysis serves both yeast subunits: LSC2 (P53312, beta) directly, and LSC1 (P53598, alpha) through the census of which beta-subunit partners each genome encodes.

## Questions

1. Is yeast LSC2 an ADP-type beta subunit by descent, or only by assay?
2. Where on the tree did GDP specificity arise, and which lineages have a GDP-type beta subunit for their alpha subunit to pair with?

## Results

### 1. The eukaryotic beta subunit duplicated once, before the opisthokont-amoebozoan split

PANTHER places a duplication node (PTN000212530) at the root of the eukaryotic beta subunits.
One daughter (PTN008330414, 63 leaves) contains human SUCLA2; the other (PTN002483419, 113 leaves) contains human SUCLG2.
Yeast LSC2 and S. pombe SPCC1620.08 both fall in the SUCLA2 (A-type) daughter clade, not in the SUCLG2 (G-type) clade.

The independent neighbor-joining analysis (42 sequences, 420 alignment columns, 200 bootstrap replicates) agrees with the PANTHER topology:

| Quartet tested | Support |
|---|---|
| LSC2 + human SUCLA2 versus human SUCLG2 + E. coli SucC | 200/200 |
| S. pombe beta + human SUCLA2 versus human SUCLG2 + E. coli SucC | 200/200 |
| pig GTP-specific beta + human SUCLG2 versus human SUCLA2 + LSC2 | 200/200 |
| Arabidopsis beta + human SUCLG2 versus human SUCLA2 + LSC2 | 199/200 |
| Dictyostelium A-clade beta + human SUCLA2 versus Dictyostelium G-clade beta + human SUCLG2 | 185/200 |
| Ustilago maydis G-clade protein + human SUCLG2 versus human SUCLA2 + LSC2 | 199/200 |

A maximum-likelihood tree of the same alignment (IQ-TREE, LG+G4, 1000 ultrafast bootstraps) was built because distance trees can be misled by long branches. It recovers the two clades that matter and disagrees with PANTHER elsewhere:

| Smallest clade containing | Members | Ultrafast bootstrap |
|---|---|---|
| LSC2 and human SUCLA2 | 12 tips: all 7 fungal A-type subunits and the 5 animal SUCLA2 orthologs, and nothing else | 90 |
| human SUCLG2 and the Dictyostelium G-clade beta | 8 tips: animal, Monosiga and Dictyostelium SUCLG2-type subunits, all with Gln at position 20 | 96 |
| human SUCLA2 and the Dictyostelium A-clade beta | 17 tips: the 12 above plus Monosiga, Dictyostelium, Plasmodium and two stramenopile subunits | 70 |
| Arabidopsis beta and human SUCLG2 | 30 tips: every eukaryotic subunit except Trichomonas and the second Ustilago protein | 50 |

The fungal subunits and animal SUCLA2 form one clade in the PANTHER tree, the neighbor-joining tree and the maximum-likelihood tree.
Yeast LSC2 is therefore the ortholog of animal SUCLA2, and is a paralog of animal SUCLG2.
Because Dictyostelium and the choanoflagellate Monosiga each have one gene in each clade, the duplication predates the divergence of animals, fungi and amoebozoa.
Pairwise identity does not show this: LSC2 is 46.1% identical to SUCLA2 and 45.0% identical to SUCLG2, so orthology has to be read from the tree, not from similarity.
What the three trees do not agree on is the deep placement of the plant, stramenopile and excavate subunits: PANTHER and the neighbor-joining tree put them on the SUCLG2 side of the duplication, the maximum-likelihood tree puts plants and stramenopiles on the SUCLA2 side with weak support (54 and 70). That placement is unresolved and nothing below depends on it.

### 2. Fungi kept the A-type beta subunit and lost the G-type one

Beta-subunit paralog census per organism in the PANTHER tree (number of organisms):

| Group | A and G | A only | G only |
|---|---|---|---|
| Metazoa and choanoflagellates | 34 | 0 | 2 |
| Dictyostelium | 2 | 0 | 0 |
| Fungi | 1 | 14 | 0 |
| Viridiplantae | 0 | 0 | 40 |
| Excavates | 0 | 0 | 3 |
| Stramenopiles | 0 | 0 | 2 |
| Alveolata | 1 | 1 | 0 |

Fourteen of fifteen fungal genomes in the tree, including S. cerevisiae, S. pombe, Candida albicans, Neurospora crassa, Cryptococcus neoformans and the chytrid Batrachochytrium dendrobatidis, encode only an A-type beta subunit.
The one exception is Ustilago maydis, which has a second, divergent protein (A0A0D1E3R8, named only as a CoA-binding domain-containing protein) that PANTHER places in the G clade. Its position is unstable: the neighbor-joining tree groups it with SUCLG2, the maximum-likelihood tree puts it outside all other eukaryotic subunits on a long branch, and it has Ala, not Gln, at position 20. It is not evidence that a fungus retains a GDP-type beta subunit.
Every fungal genome has one or two alpha-subunit genes; S. cerevisiae has exactly one alpha (LSC1) and one beta (LSC2).
The two "G only" metazoan entries are Pristionchus pacificus and a Xanthomonas campestris sequence that PANTHER places inside the animal G clade as a horizontal transfer; both are more likely gaps or artefacts of the tree than real biology.

### 3. GDP specificity is a derived state inside the G clade, marked by Gln at position 20

Position 20 of the mature beta subunit is Pro in E. coli SucC and Gln in pig GTP-specific SCS, where the Gln side chain contacts the guanine base (PMID:16481318, PMID:22751660).
Residue aligned to E. coli SucC Pro20 in the 42-sequence panel:

| Clade | Residue at position 20 |
|---|---|
| A clade, 15 sequences (animals, fungi, Dictyostelium, Plasmodium) | Pro in 14, Gly in Monosiga |
| G clade, animals, Monosiga and Dictyostelium (7 sequences, plus pig) | Gln in all |
| G clade, plants, green alga and stramenopiles (5 sequences) | Pro in all |
| G clade, trypanosomatids (2) and Trichomonas (3) | Glu, Gly |
| G clade, Ustilago maydis second protein | Ala |
| Bacteria and archaea (8 sequences) | Pro in 5, Ser in 2, Thr in 1 |

Yeast LSC2 has Pro at this position, the ancestral state shared with E. coli SucC and human SUCLA2.
Gln at position 20 is confined to the animal, choanoflagellate and Dictyostelium members of the G clade, which is exactly the clade (PTN000929335) where PAINT records the gain of GDP-forming activity and the loss of ADP-forming activity.
Plant, stramenopile and excavate beta subunits are on the SUCLG2 side of the duplication in the PANTHER tree but keep the ancestral residue, so position relative to the duplication does not by itself predict GDP specificity.

### 4. PANTHER node ids used in the family reviews

These ids are read from the PANTHER release 19 trees by the script (`panther_tree_nodes` in `results.yaml`), not typed in.

| Family | Node | PANTHER label | Leaves | Role in the reviews |
|---|---|---|---|---|
| PTHR11117 (alpha) | PTN000122012 | LUCA, speciation | 187 | root node; PAINT places the ADP- and GDP-forming terms here |
| PTHR11117 (alpha) | PTN004231559 | horizontal transfer | 166 | joins the eukaryotic clade to Proteobacteria |
| PTHR11117 (alpha) | PTN000122014 | Eukaryota, speciation | 150 | eukaryotic clade; PAINT places mitochondrion here |
| PTHR11117 (alpha) | PTN000874203 | Fungi, speciation | 21 | fungal clade containing LSC1; proposed place for a loss of GDP-forming activity |
| PTHR11117 (alpha) | PTN008961326 | duplication | 3 | Trichomonas vaginalis alpha subunits |
| PTHR11815 (beta) | PTN000212531 | LUCA, speciation | 208 | root node |
| PTHR11815 (beta) | PTN000212530 | duplication | 176 | eukaryotic beta duplication |
| PTHR11815 (beta) | PTN008330414 | Eukaryota, speciation | 63 | A-type daughter clade, contains LSC2 and SUCLA2 |
| PTHR11815 (beta) | PTN000929379 | Fungi, speciation | 16 | fungal beta subunits |
| PTHR11815 (beta) | PTN008982090 | duplication | 3 | Trichomonas vaginalis beta subunits |
| PTHR11815 (beta) | PTN001721370 | leaf | 1 | Xanthomonas campestris SucC, placed below a horizontal-transfer node (PTN008982084) inside the animal G clade |

The fungal alpha-subunit clade is node PTN000874203 (21 leaves), on the path from the root to LSC1.

## Interpretation

- LSC2 is ADP-specific by descent: it belongs to the A-type lineage that also gave rise to animal SUCLA2, and it carries the ancestral Pro at the position where GDP-specific enzymes have Gln.
- Fungi lost the G-type beta paralog, so a fungal alpha subunit such as LSC1 has no GDP-specific partner. This is why GDP-forming activity, placed by PAINT at the root of the alpha-subunit family, does not hold for LSC1.
- The gene duplication that produced the A and G lineages is older than animals, older than the proposal in PMID:9765291 that the two genes arose early in the evolution of multicellular eukaryotes.

## Limitations

- Position 20 is a marker, not a complete determinant. E. coli SCS has Pro20 and uses both nucleotides, and Thermus aquaticus SCS has Pro20 and prefers GTP (PMID:22751660). The residue cannot predict specificity for the bacterial, archaeal, excavate or Ustilago sequences.
- The trees are built on a 42-sequence panel and one alignment; they test specific groupings and are not a full phylogenetic reconstruction. The deep branching order of eukaryotic beta subunits outside the two supported clades is unresolved, so whether plants descend from the A-side or the G-side copy is not known.
- The census counts genes in PANTHER's reference proteomes. Absence of a G-type gene from a fungal genome in this set is an observation about these 15 genomes, not about all fungi.
- No enzyme assays were done. Nucleotide specificity of yeast SCS rests on PMID:9874242.
