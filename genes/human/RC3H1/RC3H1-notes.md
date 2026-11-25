# RC3H1 notes

## 2026-11-22 family review

- Fetched with `just fetch-gene human RC3H1`; the GOA file has 75 annotation rows plus the header, so the review is not based on a header-only failed fetch.
- Automated provider-backed deep research was unavailable in this checkout, so this review used the fetched UniProt, GOA, PAINT, and cached publication records directly.
- PTHR13139 places human RC3H1 in `PTHR13139:SF6`. The PAINT slice has a single Metazoa gain node, `PTN002295097`, for Roquin stress-granule localization, RNA binding, stem-loop/double-stranded RNA binding, RING E3 ligase/polyubiquitination, deadenylation-dependent mRNA decay, and ubiquitin-dependent protein catabolic process. `just paint-losses human RC3H1` reported no IRD or IKR losses on the RC3H1 lineage.
- The strongest core molecular evidence is direct structural and cell work on the human Roquin-1 ROQ domain. PMID:25026078 shows that the human ROQ domain recognizes CDE stem-loop RNA and a double-stranded RNA site, and that mutations in either site prevent rescue of HMGXB3 and IL6 mRNA decay in human cells.
- PMID:28165457 supports direct Roquin recruitment of CCR4-NOT as the effector arm for deadenylation-dependent target mRNA decay; PMID:31636267 confirms that a human disease truncation of Roquin-1 loses P-body localization, CCR4-NOT interaction, ICOS mRNA decay, and cytokine control.
- PMID:26489670 supports a genuine RING-domain ubiquitin protein ligase activity for both RC3H1 and RC3H2. Protein polyubiquitination was kept as a core process, while the broader PAINT `GO:0006511` protein-degradation process was retained as a real but non-core branch because direct protein-substrate degradation is better established for RC3H2 and C. elegans RLE-1 than for human RC3H1.
- Immune cell differentiation and germinal-center rows were kept as non-core consequences of Roquin-mediated mRNA decay. They are biologically real, but the curated molecular role is target-RNA recognition coupled to CCR4-NOT recruitment.
- The HPA cytosol row was kept because it agrees with cytoplasmic Roquin and RNA-granule pools. The HPA plasma-membrane row was marked over-annotated because RC3H1 is a soluble cytoplasmic RNA-binding/E3 ligase and there is no independent support for a functional plasma-membrane pool.
- No Roquin-family GO-CAM was found. Production GO-CAM `69729a3800003422` uses RC3H2 as the substrate of a CUL3/KLHL6/RBX1 degradation reaction, not as the active Roquin-family RNA/E3 effector.
