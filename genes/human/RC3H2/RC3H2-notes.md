# RC3H2 notes

## 2026-11-22 family review

- Fetched with `just fetch-gene human RC3H2`; the GOA file has 37 annotation rows plus the header, so the review is not based on a header-only failed fetch.
- Automated provider-backed deep research was unavailable in this checkout, so this review used the fetched UniProt, GOA, PAINT, and cached publication records directly.
- PTHR13139 places human RC3H2 in `PTHR13139:SF2`. The PAINT slice has a single Metazoa gain node, `PTN002295097`, for Roquin stress-granule localization, RNA binding, stem-loop/double-stranded RNA binding, RING E3 ligase/polyubiquitination, deadenylation-dependent mRNA decay, and ubiquitin-dependent protein catabolic process. `just paint-losses human RC3H2` reported no IRD or IKR losses on the RC3H2 lineage.
- PMID:26249698 and PMID:26489670 both support human Roquin-2 ROQ-domain CDE stem-loop recognition. PMID:26489670 also supports the separate double-stranded RNA surface and the ability of RNA binding to modulate RC3H2 auto-ubiquitination in vitro.
- PMID:28165457 showed that the Roquin-2 C-terminal region, like the Roquin-1 C-terminal region, can recruit the CCR4-NOT complex and promote target mRNA decay. I added CCR4-NOT complex binding as a missing direct molecular activity for RC3H2 to make it consistent with RC3H1.
- PMID:24448648 directly supports RC3H2 as an E3 ubiquitin ligase for ROS-induced ubiquitination and degradation of ASK1/MAP3K5; PMID:26489670 supports E2-dependent polyubiquitin-chain assembly by purified RC3H2. Together they support both RING E3 activity and the non-core protein-degradation PAINT term.
- The old MNAB paper, PMID:10938276, proposed DNA-binding and membrane/cell-surface roles before the Roquin family model was established and explicitly noted that the cell-surface interpretation still awaited confirmation. DNA binding, membrane, and cell surface were therefore marked over-annotated in favor of the current cytoplasmic ROQ-domain RNA-binding and E3 ligase model.
- Immune cell differentiation, TCR signaling, and miRNA-homeostasis rows were kept as real but non-core phenotypic or secondary RNA-regulatory effects of Roquin-family transcript control.
- No Roquin-family GO-CAM was found. Production GO-CAM `69729a3800003422` uses RC3H2 as the substrate of a CUL3/KLHL6/RBX1 degradation reaction, not as the active Roquin-family RNA/E3 effector.
