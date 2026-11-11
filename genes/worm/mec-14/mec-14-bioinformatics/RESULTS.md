# mec-14 (Q20127) bioinformatics results

Analyses run 2026-10-21. Scripts and raw outputs are in this folder.

## 1. PANTHER tree placement (`panther_tree_placement.py` -> `panther_tree_placement.out`)

PANTHER 19 treeinfo for PTHR42686, filtered to C. elegans, D. melanogaster, S. cerevisiae, A. thaliana and human.

- mec-14 is leaf PTN000199442 in PTHR42686:SF1 (GH17980P-RELATED).
- PTN000199440 SPECIATION Ecdysozoa contains mec-14 and the three fly paralogs CG12224, CG3397 and CG18547 (the fly genes descend from a Drosophila duplication node), so mec-14 is a co-ortholog of all three fly genes.
- PTN000199433 SPECIATION Opisthokonts adds yeast ARA2 (Q04212).
- PTN000199432 SPECIATION Eukaryota adds Arabidopsis LGALDH (O81884).
- No human leaf is returned for PTHR42686 under the taxon filter: the family has no human (vertebrate) member. mec-14 is therefore not an ortholog of human KCNAB1 (Kv beta subunits, a different AKR family) in PANTHER.
- C. elegans has a single PTHR42686 member (mec-14).
- For comparison, the UniProt PANTHER cross-reference of human KCNAB1 (Q14722) is PTHR43150 (PTHR43150:SF7), a different AKR family (checked 2026-10-21 via the UniProt REST API).

## 2. PAINT node annotations for PTHR42686

PAINT GAF (gene_association.paint_uniprot), resolved with `ai-gene-review fetch-panther-paint PTHR42686` (written to a scratch directory, not committed). Node-level IBD assertions:

| node | GO term | seeds | taxon of node |
|---|---|---|---|
| PTN000920371 | GO:0045290 D-arabinose 1-dehydrogenase [NAD(P)+] activity (F) | SGD:S000004644 (ARA2) | taxon:451864 (Dikarya) |
| PTN000920371 | GO:0070485 dehydro-D-arabinono-1,4-lactone biosynthetic process (P) | SGD:S000004644 | taxon:451864 |
| PTN000920391 | GO:0010349 L-galactose dehydrogenase activity (F) | AGI:AT4G33670 (LGALDH) | taxon:3193 (Embryophyta) |
| PTN000920391 | GO:0019853 L-ascorbic acid biosynthetic process (P) | AGI:AT4G33670 | taxon:3193 |
| PTN002448388 | GO:0016491 oxidoreductase activity (F) | AT4G33670, S000004644 | family root |

Interpretation: PAINT curators placed the substrate-specific activities (D-arabinose dehydrogenase; L-galactose dehydrogenase) on the fungal and land-plant nodes only, and placed only generic oxidoreductase activity at the node that also covers the animal clade. mec-14 inherits only GO:0016491 by IBA. The omission of the substrate-specific terms from the Opisthokont and Eukaryota nodes is treated here as a deliberate decision.

## 3. Catalytic tetrad conservation (`tetrad_check.py` -> `tetrad_check.out`)

Pairwise global alignment (BLOSUM62, gap open -10, extend -0.5) to Arabidopsis LGALDH (O81884), whose AKR tetrad positions are Asp54, Tyr59 (UniProt proton donor), Lys87 and His124.

| O81884 | mec-14 (Q20127) | ARA2 (Q04212) | CG18547 (Q9VGF3) | CG12224 (Q9VGF2) |
|---|---|---|---|---|
| D54 | D132 | D53 | D71 | D73 |
| Y59 | Y137 | Y58 | Y76 | Y78 |
| K87 | K163 | K86 | K102 | K102 |
| H124 | H206 | H124 | H143 | H143 |

- mec-14 retains all four AKR catalytic tetrad residues (D132, Y137, K163, H206), so it is not predicted to be a pseudoenzyme.
- Identity of mec-14: 40.3% to LGALDH (310 aligned), 34.6% to ARA2, 43.5% to CG18547, 40.4% to CG12224.
- mec-14 (453 aa) has an N-terminal extension of about 75 residues absent from LGALDH (319 aa), including the MobiDB-lite disordered region 28-55, and a C-terminal extension of about 40 residues. Their function is unknown.

## Limitations

- Retention of the catalytic tetrad indicates likely catalytic competence but says nothing about substrate. In PTHR42686:SF1 the characterised members act on different substrates (L-galactose in plants, D-arabinose in yeast, D-threo-aldoses and pyridoxal in bacteria), so the substrate of mec-14 cannot be inferred from family membership.
- No enzyme assay of MEC-14 has been published.
