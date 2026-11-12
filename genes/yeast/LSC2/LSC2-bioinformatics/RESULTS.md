# Evolution of the succinyl-CoA synthetase subunit families (LSC1 / LSC2)

Analysis: `scs_family_evolution.py`, run with `uv run --script scs_family_evolution.py --bootstraps 200`.
Outputs: `results.yaml` (all numbers below), `beta_panel_nj.nwk` (neighbor-joining tree, internal labels are clade bootstrap percentages) and `beta_panel_ml.nwk` (maximum-likelihood tree, internal labels are the lowest ultrafast bootstrap over three runs).
Inputs are fetched at run time: the PANTHER release 19 trees of PTHR11815 (beta subunit) and PTHR11117 (alpha subunit), and UniProt sequences and annotations.
This analysis serves both yeast subunits: LSC2 (P53312, beta) directly, and LSC1 (P53598, alpha) through the question of which beta subunits a genome encodes.

## Terms

- Succinyl-CoA synthetase (SCS) is an alpha-beta enzyme. The beta subunit binds the nucleotide, so it decides whether the enzyme makes ATP or GTP.
- Animals have two beta genes: SUCLA2 (ATP-specific enzyme) and SUCLG2 (GTP-specific enzyme).
- A daughter and G daughter are the two clades below the PANTHER duplication node PTN000212530. The A daughter contains human SUCLA2 and the G daughter contains human SUCLG2. These labels are PANTHER's placement of a sequence. They say nothing about its nucleotide specificity.
- Position 20 of the mature beta subunit is Pro in E. coli SucC and Gln in pig GTP-specific SCS, where the Gln side chain contacts the guanine base (PMID:16481318). Pro20 and Gln20 name the residue that a sequence has at the aligned position.
- A sequence is "with SUCLA2" or "with SUCLG2" when, in a tree rooted on E. coli SucC, it is closer to that human protein than the two human proteins are to each other. It is "outside both" when the two human proteins are closer to each other than either is to it.
- NJ clade bootstrap is the number of 200 resampled neighbor-joining trees that contain exactly the named clade. Ultrafast bootstrap (UFBoot) is the IQ-TREE support of a clade. UFBoot values below 95 are not strong support; values below about 80 are weak.

## Methods in brief

- Panel: 64 beta subunits. These are the PANTHER leaves of 32 organisms plus 16 added UniProt entries, all of which were fetched. The added entries are pig SUCLG2, Blastocystis B3FHP0, Thermus thermophilus P25126, nine genes from early-diverging fungi and Saitoella, and Gln20 genes from Tetrahymena, Thecamonas, Capsaspora and Naegleria. Paramecium tetraurelia was added to the panel organisms.
- Alignment: FAMSA, 423 columns kept (columns with under 50% gaps).
- Trees: neighbor joining on BLOSUM62 dissimilarities with 200 column bootstraps (seed 1, exactly reproducible), and maximum likelihood with IQ-TREE (LG+G4, 1000 ultrafast bootstraps, three runs with seeds 1, 2 and 3).
- Position 20 is read from a pairwise local alignment to the closest of three references (E. coli SucC, human SUCLA2, human SUCLG2). In the panel this gives the same residue as the alignment column for every protein that has an ATP-grasp domain.

## Results

### 1. LSC2 groups with animal SUCLA2, not with SUCLG2

PANTHER places a duplication node (PTN000212530) at the root of the eukaryotic beta subunits.
One daughter (PTN008330414, 63 leaves) contains human SUCLA2; the other (PTN002483419, 113 leaves) contains human SUCLG2.
Yeast LSC2 and S. pombe SPCC1620.08 both fall in the SUCLA2 (A-type) daughter clade, not in the SUCLG2 (G-type) clade.
Both sequence trees agree with PANTHER on this point.
In the maximum-likelihood tree, yeast LSC2 and human SUCLA2 fall in a clade of 16 sequences that contains 11 fungal and 5 animal beta subunits, all with Pro at position 20, and no other sequence. This clade has ultrafast bootstrap 100 in each of three runs and is recovered in 120 of 200 neighbor-joining bootstrap trees.
LSC2 is closer to human SUCLA2 than to human SUCLG2 in 197 of 200 neighbor-joining bootstrap trees and in all three maximum-likelihood runs.
Yeast LSC2 is therefore best read as the ortholog of animal SUCLA2 and a paralog of animal SUCLG2.
Pairwise identity does not show this: LSC2 is 46.3% identical to SUCLA2 and 45.1% identical to SUCLG2, so the relationship has to be read from the tree.

Placement of each group of panel sequences. NJ counts are bootstrap trees with SUCLA2 / with SUCLG2 / outside both, out of 200. The three ML runs gave the same tree, so one ML result is shown.

| Sequences (position 20) | PANTHER | NJ tree | NJ bootstrap | ML tree |
|---|---|---|---|---|
| S. cerevisiae LSC2 (Pro) | A daughter | with SUCLA2 | 197 / 0 / 3 | with SUCLA2 |
| S. pombe O94415 (Pro) | A daughter | with SUCLA2 | 200 / 0 / 0 | with SUCLA2 |
| Dictyostelium Q55AI5 (Pro) | A daughter | with SUCLA2 | 127 / 59 / 14 | with SUCLA2 |
| Dictyostelium Q869S7 (Gln) | G daughter, under PTN000929335 | with SUCLG2 | 10 / 182 / 8 | with SUCLG2 |
| Lobosporangium, Linnemannia, Basidiobolus, Saitoella first gene (Pro) | not in tree | with SUCLA2 | 200 / 0 / 0 each | with SUCLA2 |
| Lobosporangium, Linnemannia, Basidiobolus, Saitoella second gene and Rozella (Gln) | not in tree | with SUCLG2 | 0 / 200 / 0 each | with SUCLG2 |
| Capsaspora, Thecamonas (Gln) | not in tree | with SUCLG2 | 0 / 200 / 0 and 1 / 199 / 0 | with SUCLG2 |
| Arabidopsis, rice, Chlamydomonas (Pro) | G daughter | with SUCLA2 | 110 / 57 / 33 | with SUCLA2 |
| Phytophthora, Thalassiosira (Pro) | G daughter | with SUCLA2 | 131 / 52 / 17 and 132 / 51 / 17 | with SUCLA2 |
| Trypanosoma brucei, Leishmania major (Glu) | G daughter | with SUCLA2 | 112 / 22 / 66 | with SUCLA2 |
| Trichomonas vaginalis, 3 genes (Gly) | G daughter | with SUCLG2 | 25 / 122 / 53 | outside both |
| Paramecium, 3 genes (Pro) | A daughter | with SUCLA2 | 141 / 7 / 52 | with SUCLA2 |
| Paramecium, 4 genes, and Tetrahymena (Gln) | G daughter, outside PTN000929335 (Tetrahymena not in tree) | outside both | 3 / 78 / 119 | with SUCLG2 |
| Blastocystis B3FHP0 (Gln) | not in tree | with SUCLA2 | 73 / 68 / 59 | outside both |
| Naegleria D2VP45 (Gln) | not in tree | with SUCLA2 | 89 / 50 / 61 | with SUCLA2 |
| Ustilago A0A0D1E3R8 (no residue) | G daughter, under PTN000929335 | outside both | 12 / 22 / 166 | outside both |

Named clades. Each row is the smallest clade that holds the named sequences in the maximum-likelihood tree.

| Clade | Members | UFBoot, 3 runs | NJ clade bootstrap |
|---|---|---|---|
| LSC2 and human SUCLA2 | 16: 11 fungal and 5 animal subunits, all Pro20 | 100 to 100 | 120/200 |
| human SUCLG2 and the five fungal Gln20 genes | 14: animal SUCLG2 orthologs, Monosiga, Capsaspora, Thecamonas and the five fungal genes, all Gln20 | 91 to 96 | 152/200 |
| the five fungal Gln20 genes | 5 | 81 to 83 | 28/200 |
| human SUCLG2 and the Paramecium Gln20 genes | 19: the 14 above, four Paramecium genes and Tetrahymena, all Gln20 | 25 to 29 | 15/200 |
| human SUCLA2 and the Dictyostelium Pro20 gene | 24: the 16 above, Monosiga A9UTU9 (Gly20), Dictyostelium Q55AI5, Phytophthora H3GTW5, Thalassiosira B8BS06, three Paramecium Pro20 genes and Plasmodium Q8ILE9; no Gln20 sequence | 98 to 98 | 33/200 |
| Arabidopsis beta and human SUCLA2 | 30: the 24 above, three plant genes, two trypanosomatid genes and Naegleria; human SUCLG2 is outside | 83 to 92 | 26/200 |

What the sequence trees show for the groups where PANTHER and the sequence trees differ:

- Plants. PANTHER places the plant beta subunits in the G daughter, but the neighbor-joining and maximum-likelihood trees both place them with SUCLA2, with weak to moderate support (110 of 200 neighbor-joining bootstrap trees, ultrafast bootstrap 83 to 92).
- Stramenopiles. PANTHER places the Phytophthora and Thalassiosira beta subunits in the G daughter, but the neighbor-joining and maximum-likelihood trees both place them with SUCLA2 (131 and 132 of 200 neighbor-joining bootstrap trees). In the maximum-likelihood tree they are inside the 24-sequence clade that holds SUCLA2, LSC2, the Dictyostelium Pro20 gene, the Paramecium Pro20 genes and Plasmodium (ultrafast bootstrap 98 in each run); that exact clade is in only 33 of 200 neighbor-joining bootstrap trees. The Blastocystis subunit is not placed consistently by either tree.
- Trypanosomatids. PANTHER places the Trypanosoma brucei and Leishmania major beta subunits in the G daughter, but both sequence trees place them with SUCLA2, weakly (112 of 200 neighbor-joining bootstrap trees).
- Trichomonas. The three Trichomonas vaginalis beta subunits are with SUCLG2 in the neighbor-joining tree (122 of 200 bootstrap trees) and outside both human paralogs in the maximum-likelihood tree, so their placement is unresolved.
- Ustilago. The second Ustilago maydis protein A0A0D1E3R8 is placed under PTN000929335 by PANTHER, but the neighbor-joining tree (166 of 200 bootstrap trees) and all three maximum-likelihood runs place it outside both human paralogs, next to the archaeal and bacterial sequences. In the maximum-likelihood tree it is outside all other eukaryotic beta subunits (that 54-sequence clade has ultrafast bootstrap 35 to 61 and is in 59 of 200 neighbor-joining bootstrap trees); in the neighbor-joining tree the ciliate Gln20 genes are also outside that clade. The neighbor-joining and maximum-likelihood trees agree with each other that it is outside both human paralogs, and disagree with PANTHER.

Removing A0A0D1E3R8 and rebuilding the maximum-likelihood tree (one run, seed 1) changes no entry of the placement table. In that tree the Dictyostelium Gln20 gene joins the SUCLG2 clade before the ciliate genes do (15 sequences, ultrafast bootstrap 83), and the clade with the ciliate genes has 20 sequences (ultrafast bootstrap 46).

### 2. The G-type beta gene was lost within fungi, not by all fungi

In this section a G-type (SUCLG2-type) gene is a beta gene that groups with human SUCLG2 in the sequence trees, and an A-type gene is one that groups with human SUCLA2.

PANTHER tree, beta genes per organism (number of organisms; A and G are PANTHER's daughter clades):

| Group (UniProt lineage) | A and G | A only | G only |
|---|---|---|---|
| Metazoa and choanoflagellates | 34 | 0 | 1 |
| Amoebozoa (Dictyostelium) | 2 | 0 | 0 |
| Fungi | 1 | 14 | 0 |
| Viridiplantae | 0 | 0 | 40 |
| Discoba and Metamonada | 0 | 0 | 3 |
| Stramenopiles | 0 | 0 | 2 |
| Alveolata | 1 | 1 | 0 |

The "G only" label for plants, stramenopiles and trypanosomatids is PANTHER's placement, which the sequence trees do not support (section 1).
The alveolate with both is Paramecium tetraurelia (3 A-daughter and 4 G-daughter genes). The "G only" animal is Pristionchus pacificus. One bacterial leaf, Xanthomonas campestris SucC (Q8P676), sits inside the animal G clade below a horizontal-transfer node and is not counted as an animal.
The one fungus with a G-daughter leaf is Ustilago maydis, and that leaf is A0A0D1E3R8, which is not a G-type beta subunit (section 3).
The 15 fungal genomes in the PANTHER tree (14 Dikarya and the chytrid Batrachochytrium dendrobatidis) have an A-type beta gene and no G-type beta gene.

PANTHER's 15 genomes are not all fungi. A census of every fungal UniProt entry of the family (taxonomy 4751, 2997 entries, of which 1878 are beta subunits with an ATP-grasp domain) gives Pro20 in 1699, Gln20 in 45, no readable residue in 119 entries whose alignment does not reach the position, and another residue in 15.

| Fungal phylum | Beta entries | Gln20 entries | Organisms with a Gln20 gene | of these, also a Pro20 gene |
|---|---|---|---|---|
| Mortierellomycota | 44 | 16 | 15 of 16 | 14 |
| Basidiobolomycota | 7 | 2 | 2 of 2 | 2 |
| Rozellomycota | 2 | 1 | 1 of 2 (Rozella allomycis) | 0 |
| Ascomycota | 1373 | 26 | 26 of 1006 | 26 |
| Basidiomycota | 319 | 0 | 0 of 299 | 0 |
| Mucoromycota | 38 | 0 | 0 of 32 | 0 |
| Kickxellomycota | 36 | 0 | 0 of 32 | 0 |
| Glomeromycota | 24 | 0 | 0 of 21 | 0 |
| Chytridiomycota | 20 | 0 | 0 of 16 | 0 |

Six further phyla with 15 entries in total (Blastocladiomycota, Entomophthoromycota, Neocallimastigomycota, Microsporidia, Zoopagomycota, Monoblepharomycota) have no Gln20 entry.

The Gln20 entries of Mortierellomycota, Basidiobolomycota and Rozella are in PANTHER subfamily SF10. Of the 26 Ascomycota entries, one is the second gene of Saitoella complicata (SF10). The other 25 are in subfamily SF1, the subfamily of LSC2; they come from Fusarium, Gibberella and Microdochium and were not placed in a tree.
Five of these Gln20 genes are in the panel (Lobosporangium A0A1Y2H5W1, Linnemannia A0A197JV50, Basidiobolus A0A1Y1YRN0, Rozella A0A075B0S1, Saitoella A0A0E9NQG5). All five group with human SUCLG2 in 200 of 200 neighbor-joining bootstrap trees and in all three maximum-likelihood runs, inside a clade of 14 Gln20 sequences with animal SUCLG2 (ultrafast bootstrap 91 to 96).
The first (Pro20) gene of the same four species groups with LSC2 and human SUCLA2.

Early-diverging fungi (Mortierellomycota, Basidiobolus, Rozella) keep a SUCLG2-type beta gene with Gln at position 20, so the G-type beta gene was lost within fungi and not in the common ancestor of all fungi.
No enzyme from these fungi has been assayed, so the nucleotide specificity of the fungal SUCLG2-type subunits is unknown.
Among Dikarya the only Gln20 entries are the Saitoella gene and the 25 Ascomycota entries of subfamily SF1; the 319 Basidiomycota entries have none. The sampled Mucoromycota, Kickxellomycota, Glomeromycota and Chytridiomycota entries have no Gln20 gene either.
S. cerevisiae S288c has one beta-subunit entry in UniProt, LSC2 (P53312), and S. pombe has one, O94415; both are A-type genes with Pro20, and neither genome has a second beta gene.
The PANTHER alpha tree has one or two alpha genes per fungal genome; S. cerevisiae has exactly one alpha (LSC1) and one beta (LSC2).
How many times the G-type gene was lost within fungi is not established here. The Saitoella gene groups with the Mortierellomycota genes only weakly (ultrafast bootstrap 57), so vertical retention in Taphrinomycotina, transfer and contamination are not distinguished here.

### 3. Gln20 is found in the characterised GTP-specific enzymes but is not confined to them

Residue at position 20 across all 208 leaves of the PANTHER PTHR11815 tree (10 deleted UniProt entries were read from their last UniSave version):

| PANTHER node | Leaves | Residue at position 20 |
|---|---|---|
| under PTN000929335 (PAINT gain of GDP-forming and loss of ADP-forming activity) | 42 | Gln 38, Pro 1 (Xanthomonas Q8P676), Arg 1 (unreviewed Anolis entry), none 2 (Ustilago A0A0D1E3R8, a Trichoplax fragment) |
| rest of the G daughter (PTN007541286, Bikonts) | 71 | Pro 60, Gln 4 (all Paramecium tetraurelia), Gly 3 (Trichomonas), Glu 2 (trypanosomatids), none 2 |
| A daughter (PTN008330414) | 63 | Pro 59, Ser 2, Gly 1 (Monosiga), none 1 |
| Bacteria, outside the duplication | 26 | Pro 14, Leu 3, Ser 3, Gln 2 (Deinococcus radiodurans Q9RUY3, Neisseria meningitidis Q9JZP4), Thr 2, Glu 1, Lys 1 |
| Archaea, outside the duplication | 6 | Pro 5, Leu 1 |

Yeast LSC2 has Pro at position 20, as do human SUCLA2, E. coli SucC and most members of the family.
Gln at position 20 is not confined to the clade under PTN000929335: in the PANTHER tree itself it is also found in four Paramecium tetraurelia leaves (PTN002624621, in the Bikonts sister clade) and in two bacterial SucC leaves.
Among eukaryotic UniProt entries outside animals, fungi and green plants (412 entries, 362 beta subunits), 66 have Gln20: 33 from alveolates (mostly ciliates), 11 from stramenopiles, 2 from Rhizaria, 10 from Amoebozoa, 5 from Discoba (Naegleria and relatives, Andalucia), 2 from choanoflagellates and one each from Capsaspora, Fonticula and Thecamonas.
PTN000929335 is the node that holds the experimentally characterised GTP-specific enzymes (pig and human SUCLG2); it is not the limit of Gln20.
The eukaryotic Gln20 sequences in the panel do not form one clade. The animal, choanoflagellate, Capsaspora, Thecamonas and fungal Gln20 genes form a clade (14 sequences, ultrafast bootstrap 91 to 96). The ciliate Gln20 genes join that clade in the maximum-likelihood tree only with weak support (ultrafast bootstrap 25 to 29) and are outside both human paralogs in the neighbor-joining tree. The Naegleria and Blastocystis Gln20 genes do not join it.

Gln at position 20 is not sufficient for GTP specificity, and is not required for GTP use or preference. Thermus aquaticus SCS has Pro20, uses both nucleotides and prefers GTP (PMID:22751660); Blastocystis SCS has Gln20 (B3FHP0) and is ATP-specific (PMID:18452512). The enzymes shown to be GTP-specific (pig and human SUCLG2) have Gln20.
In E. coli SCS the Pro20-to-Gln mutant has an apparent Km for GTP more than 5 times lower than wild type, with the parameters for the other substrates unchanged (PMID:10353839), so the residue contributes to GTP affinity but does not set specificity alone.
The residue therefore does not by itself decide nucleotide use for an unassayed subunit. GDP-forming activity of the unassayed Gln20 subunits of Monosiga, Dictyostelium, ciliates and early-diverging fungi is an inference from their grouping with SUCLG2, not a measurement.

Plant and the sampled Phytophthora and Thalassiosira beta subunits have Pro at position 20, the trypanosomatid subunits have Glu, and the Trichomonas subunits have Gly.
Excavates cannot be described as ADP-forming as a group. Trichomonas vaginalis hydrogenosomes have both ADP-dependent and GDP-dependent succinate thiokinase activity (PMID:1898409), and for Trypanosoma brucei the evidence is ATP production in isolated mitochondria (PMID:12095995).
Whether Gln20 arose on the stem of the G-type lineage or within it is not resolved. PANTHER's tree implies it arose within the G daughter, because it puts Pro20 plant and stramenopile subunits there. The sequence trees put those Pro20 subunits with SUCLA2 instead, which would make Gln20 a feature of nearly the whole G-type lineage. Gln20 also occurs in sequences that do not group with SUCLG2 (Naegleria, Blastocystis, two bacterial SucC), so more than one origin is possible.

The second Ustilago maydis protein, A0A0D1E3R8 (UMAG_01904, named "ATP-citrate synthase/succinyl-CoA ligase C-terminal domain-containing protein"), lacks the N-terminal ATP-grasp domain (Pfam PF00549 only, 400 residues), so it has no residue homologous to position 20.
A0A0D1E3R8 is not evidence that a fungus of the Dikarya retains a G-type beta subunit: it has no nucleotide-binding domain and both sequence trees place it with prokaryotic sequences, outside both human paralogs.
The PANTHER alpha tree has a second Ustilago leaf, A0A0D1CWH6 (UMAG_01903, "CoA-binding domain-containing protein"), whose locus tag is consecutive with UMAG_01904, so the two may be a divergent alpha-like and beta-like pair.

### 4. PANTHER node ids used in the family reviews

The duplication node PTN000212530 and the PAINT node PTN000929335 are given to the script as inputs and checked against the tree; all other ids, labels and leaf counts are read from the PANTHER release 19 trees (`panther_tree_nodes` in `results.yaml`). The PAINT annotations named in the last column come from the PAINT annotation files of the two families, not from this script.

| Family | Node | PANTHER label | Leaves | Role in the reviews |
|---|---|---|---|---|
| PTHR11117 (alpha) | PTN008961318 | unlabelled | 189 | root of the tree |
| PTHR11117 (alpha) | PTN000122012 | LUCA, speciation | 187 | LUCA node, one step below the root; PAINT places the ADP- and GDP-forming terms here |
| PTHR11117 (alpha) | PTN004231559 | horizontal transfer | 166 | horizontal-transfer node above the eukaryotic clade |
| PTHR11117 (alpha) | PTN000122014 | Eukaryota, speciation | 150 | eukaryotic clade; PAINT places mitochondrion here |
| PTHR11117 (alpha) | PTN000874203 | Fungi, speciation | 21 | fungal clade containing LSC1; every fungal genome under it lacks a SUCLG2-type beta gene |
| PTHR11117 (alpha) | PTN008961326 | duplication | 3 | Trichomonas vaginalis alpha subunits |
| PTHR11815 (beta) | PTN000212531 | LUCA, speciation | 208 | root node |
| PTHR11815 (beta) | PTN000212530 | duplication | 176 | eukaryotic beta duplication |
| PTHR11815 (beta) | PTN008330414 | Eukaryota, speciation | 63 | A daughter, contains LSC2 and SUCLA2 |
| PTHR11815 (beta) | PTN002483419 | Eukaryota, speciation | 113 | G daughter, contains SUCLG2 |
| PTHR11815 (beta) | PTN000929335 | Unikonts, speciation | 42 | PAINT gain of GDP-forming and loss of ADP-forming activity |
| PTHR11815 (beta) | PTN007541286 | Bikonts, speciation | 71 | sister of PTN000929335 inside the G daughter |
| PTHR11815 (beta) | PTN002624621 | duplication | 4 | Paramecium tetraurelia Gln20 genes, inside PTN007541286 |
| PTHR11815 (beta) | PTN000929379 | Fungi, speciation | 16 | fungal beta subunits of the A daughter |
| PTHR11815 (beta) | PTN008982090 | duplication | 3 | Trichomonas vaginalis beta subunits |
| PTHR11815 (beta) | PTN001721370 | leaf | 1 | Xanthomonas campestris SucC, placed below a horizontal-transfer node (PTN008982084) inside the animal G clade |

The fungal alpha-subunit clade is node PTN000874203 (21 leaves), on the path from the root to LSC1.
PTN000122012 is the LUCA node of the alpha tree, not its root; the root is PTN008961318 (189 leaves).

## Interpretation

- LSC2 belongs to the A-type lineage by descent: it groups with animal SUCLA2 in the PANTHER tree, the neighbor-joining tree and the maximum-likelihood tree. The yeast enzyme is ATP-specific by assay: it uses ATP but not GTP (PMID:9874242).
- S. cerevisiae and S. pombe each encode one beta subunit, of the A type, so their alpha subunits have no SUCLG2-type partner. This is why GDP-forming activity, placed by PAINT at the LUCA node of the alpha-subunit family, is not expected for LSC1.
- The loss of the G-type beta gene happened within fungi. Mortierellomycota, Basidiobolus and Rozella keep a Gln20 SUCLG2-type gene, and Dikarya other than Saitoella do not. A statement that fungi as a kingdom lack a G-type beta subunit is wrong.
- The duplication that produced the A-type and G-type genes predates the divergence of animals, fungi and Dictyostelium, because Dictyostelium, Monosiga, Mortierellomycota and Basidiobolus each have one gene of each type in the trees (Capsaspora and Thecamonas have a Gln20 gene that groups with SUCLG2 and a second, Pro20 entry that was not placed in a tree; Rozella has only the Gln20 gene in UniProt). This is older than the proposal in PMID:9765291 that the two genes arose early in the evolution of multicellular eukaryotes. Whether the duplication is as old as the eukaryotes is not resolved. The maximum-likelihood tree has an A-type clade that includes stramenopile and alveolate Pro20 genes (24 sequences, ultrafast bootstrap 98), so the duplication may predate the split of Amorphea and the SAR group. The neighbor-joining tree does not recover that clade (33 of 200 bootstrap trees), the ciliate Gln20 genes group with SUCLG2 only weakly, and the trees are rooted on a single bacterial sequence.
- This analysis does not show which nucleotide specificity is ancestral. E. coli SCS has Pro20 and uses both nucleotides, with a preference for ADP (PMID:22751660), so what the A-type lineage shares with the bacterial enzyme is ADP use, not ADP specificity.

## Limitations

- These are single-gene trees of 64 sequences from one alignment and one fixed model (LG+G4, no model selection). They test specific groupings and are not a full reconstruction of eukaryotic beta-subunit history.
- The orthology of LSC2 and SUCLA2 is well supported (ultrafast bootstrap 100, 197 of 200 neighbor-joining triplets), but the exact 16-sequence clade is found in only 120 of 200 neighbor-joining bootstrap trees. The placement of the Phytophthora, Thalassiosira and Paramecium Pro20 genes with SUCLA2 is supported by the maximum-likelihood tree (ultrafast bootstrap 98) but only weakly by the neighbor-joining tree (131 to 141 of 200 triplets; 33 of 200 bootstrap trees for the same clade). The deep placements of plant, trypanosomatid, Trichomonas, Blastocystis and Naegleria subunits and of the ciliate Gln20 genes do not have strong support in either tree and should be treated as unresolved.
- Neighbor joining uses uncorrected distances, and 15 internal branches of the neighbor-joining tree are shorter than 0.01. The three Trichomonas genes are on long branches.
- IQ-TREE as called through piqtree 0.8.3 does not give identical results for a fixed seed. The three runs found the same tree, but ultrafast bootstrap values differ between runs, by under 10 points for the well-supported clades and by up to 26 points for poorly supported deep clades (35 to 61 for the 54-sequence eukaryote clade), so they are given as ranges and will not be reproduced exactly on rerun. The neighbor-joining numbers are exactly reproducible.
- The UniProt census reads one residue per entry. It counts UniProt taxon ids, so strains of one species count separately, and it includes unreviewed gene models. Absence of a gene from UniProt is not proof of absence from a genome.
- Position 20 is one residue. It does not by itself predict nucleotide specificity (section 3).
- No enzyme assays were done. Nucleotide specificity of yeast SCS rests on PMID:9874242.
