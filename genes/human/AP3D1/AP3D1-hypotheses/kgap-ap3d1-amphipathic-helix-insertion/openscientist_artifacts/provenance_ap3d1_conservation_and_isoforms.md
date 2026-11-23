# Vertebrate conservation of AP3D1 residues 1-14, and isoform coverage

All values computed in this job from live UniProt REST queries.

## Isoform coverage of O14617

UniProt O14617 annotates five isoforms. All five were retrieved as FASTA and all five
begin with the identical 24 residues MALKMVKGSIDRMFDKNLQDLVRG.

| Isoform | Length | Residues 1-24 |
|---|---|---|
| O14617-1 (displayed) | 1153 | MALKMVKGSIDRMFDKNLQDLVRG |
| O14617-2 | 1112 | MALKMVKGSIDRMFDKNLQDLVRG |
| O14617-3 | 984 | MALKMVKGSIDRMFDKNLQDLVRG |
| O14617-4 | 1021 | MALKMVKGSIDRMFDKNLQDLVRG |
| O14617-5 | 1215 | MALKMVKGSIDRMFDKNLQDLVRG |

The five annotated alternative-sequence features span residues 117-285 (isoform 3),
168-258 (isoform 2), 746-877 (isoform 4) and 866-866 (isoforms 2 and 5). None touches
residues 1-24. A residue-numbered annotation on 1-14 is therefore isoform safe.

## Vertebrate orthologue set

Query: `(gene:AP3D1) AND taxonomy_id:7742 AND length:[900 TO 1400] AND fragment:false`
returned 611 sequences. Filtered to entries with gene name exactly AP3D1, starting at
Met, length >= 900, then deduplicated to the longest entry per species: **180 species**.

Identity of residues 1-14 to human MALKMVKGSIDRMF: median 100.0 %, 123/180 species
(68.3 %) identical at all 14 positions.

### Per-position identity to human

| Position | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Residue | M | A | L | K | M | V | K | G | S | I | D | R | M | F |
| % identical | 100.0 | 92.2 | 93.3 | 92.2 | 68.3 | 92.8 | 92.8 | 92.2 | 92.8 | 92.8 | 93.9 | 92.2 | 92.2 | 92.2 |

### The variation that exists is physicochemically conservative

| Variant | Species | Count | muH (1-14) |
|---|---|---|---|
| MALKMVKGSIDRMF | human and 122 other species | 123 | 0.464 |
| MALKIVKGSIDRMF (M5I) | teleosts: Danio rerio, Takifugu rubripes, Oryzias latipes, Salmo trutta, Oreochromis niloticus and 40 others | 45 | 0.450 |
| MALRIVKGSIDRMF (K4R, M5I) | Xenopus tropicalis, Leptobrachium leishanense | 2 | 0.520 |
| unrelated N-termini | Bos taurus, Bos indicus, Bison bison, Nomascus leucogenys, Sapajus apella, Carlito syrichta, Pteropus vampyrus, Trichechus manatus, Echinops telfairi, Callorhinchus milii, Meleagris gallopavo, Taeniopygia guttata, Crenichthys baileyi, Austrofundulus limnaeus | 12 | 0.081-0.755 |

M5I is apolar to apolar and K4R is basic to basic, so the amphipathic face and net charge
are preserved. Counting these as equivalent gives 168/180 species (93.3 %) with a
physicochemically identical helix.

The 12 outliers are unreviewed TrEMBL gene models with alternative or truncated start
sites. Two of them begin at human residues 8 (Nomascus leucogenys, MGSIDRMFDKNLQD) and
15 (Crenichthys baileyi, MFDKNLQDLVRGIR), which identifies them as annotation artifacts
rather than genuine divergence.

## Reading

The species set spans teleosts, Latimeria chalumnae, Erpetoichthys calabaricus,
caecilians, frogs, squamates, crocodilians, turtles, birds and mammals, roughly 450 Myr
of divergence. A 14-residue segment that is unresolved in three of five AP-3 cryo-EM
reconstructions, assigned pLDDT 48.3 by AlphaFold, and making no heavy-atom contact with
the rest of the complex in PDB 9C59 is held at near-identity across that range. Disordered
non-contacting sequence normally drifts, so this is strong purifying selection.

What the conservation does not do is point at a mechanism. Apolar-face positions
(M1, L3, M5, V6, I10, M13, F14) and polar-side positions (K4, K7, S9, D11, R12) are
conserved to the same degree, so there is no differential-conservation signal favouring a
lipid-facing surface over a protein-binding surface. Combined with the absence of the
motif in S. cerevisiae Apl5 while the adjacent trunk helix is retained, the constraint
looks metazoan rather than universal (Drosophila MALKKVKGNFFERMF and C. elegans
MALRKVRSNIDRIF retain the MAL[KR].[VK]K pattern).

Figure: `plot_5.png`, per-position conservation bar chart plus the distribution of
hydrophobic moment of residues 1-14 across the 180 species.
