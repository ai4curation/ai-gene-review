# apg-10 Atg18 / PTHR11227 notes

Reviewed on 2026-11-21 as part of the fungal PAINT family pass for
PTHR11227, the WIPI/PROPPIN Atg18/Atg21/Hsv2 family.

I did not find a newer direct Atg18 paper for this species. The review therefore accepts conserved lipid-binding, adaptor and fungal vacuole-membrane calls from PTHR11227/UniProt while marking selective-autophagy and Cvt transfers as over-specific.

Key family decision:

- PTN000132136 is the WIPI/PROPPIN root. Its PI3P binding,
  PI(3,5)P2 binding and protein-macromolecule adaptor activity rows fit
  Atg18 orthologs.
- The same root node is too broad for pexophagy, mitophagy, nucleophagy
  and glycophagy because those processes are seeded from individual
  paralogs and should not automatically descend to every fungal Atg18.
- GO:0034045 is obsolete and is better represented as GO:0000407
  phagophore assembly site when the biological claim is just PAS
  recruitment.
- The fungal PTN000881190 node for GO:0000329 fungal-type vacuole
  membrane is sound for the reviewed ascomycete Atg18 proteins.

I also searched PubMed and the web on 2026-11-21 for `N. crassa
Atg18`, `apg-10 autophagy`, and `PTHR11227 Atg18 PROPPIN`.
The search found the cached 2023-2024 C. albicans DNA-damage autophagy
papers and the 2026 S. cerevisiae Atg18-AIM paper, but no direct newer
Atg18-specific paper for C. glabrata, N. crassa, or A. fumigatus.
