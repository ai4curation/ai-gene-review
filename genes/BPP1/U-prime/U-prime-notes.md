# U-prime / U' (Q71TD7) Curation Notes — Escherichia phage P1

## Functional Summary
- **Gene symbol**: `U-prime` in directory/YAML (`U'` in UniProt `Q71TD7`; note: `gene_symbol: U-prime` is preserved in `U-prime-ai-review.yaml` to match the directory `genes/BPP1/U-prime/`).
- **Protein**: Alternative tail fiber assembly protein U' (`gpU'`; 172 aa, ~19.1 kDa; InterPro `IPR003458` / Pfam `PF02413` `Caudo_TAP`).
- **Biological role**:
  - `gpU'` is the alternative tail fiber assembly chaperone encoded in the oppositely oriented `S'v-U'` cassette within the 4.2-kb Cin-invertible C-segment of phage P1 [PMID:6327269, PMID:2526777, PMID:1534556, PMID:15489417].
  - When Cin-mediated site-specific inversion flips the C-segment into the C(-) orientation, `S'v` is joined in-frame to the constant N-terminal `Sc` region of `S`, and `U'` is co-transcribed immediately downstream from the late promoter `LP_S` as the third gene of the `R-S'-U'` operon [PMID:2526777, PMID:15489417].
  - Like its C(+) counterpart `gpU` (`Q71TD6`), `gpU'` is homologous to phage Mu gpU', T4 gp38, and lambda Tfa, acting in the host cell cytoplasm (`GO:0030430` `host cell cytoplasm`) to chaperone the folding and assembly of the alternative `Sc-S'v` tail fiber (`GO:0098004` `virus tail fiber assembly`), which confers adsorption specificity for alternative enterobacterial hosts [PMID:6327269, PMID:15489417].

## Review of Existing GOA Annotations
- `GO:0019062` (`virion attachment to host cell`, IEA, `GO_REF:0000043`): **KEEP_AS_NON_CORE**. `gpU'` folds the `S'v` receptor-binding domain of `gpS'` and may also remain associated with the fiber tip by analogy to lambda Tfa [PMID:15489417], whereas its primary conserved molecular role is tail fiber assembly (`GO:0098004`).
- `GO:0030430` (`host cell cytoplasm`, IEA, `GO_REF:0000043` and `GO_REF:0000044`): **ACCEPT**. `gpU'` acts in the host bacterial cytoplasm during lytic morphogenesis to fold and assemble nascent `Sc-S'v` tail fibers [PMID:15489417].
- `GO:0046718` (`symbiont entry into host cell`, IEA, `GO_REF:0000043`): **TOO_GENERAL**. Entailed by `GO:0019062` (`virion attachment to host cell`, which is `part_of` `GO:0046718`).
- `GO:0098003` (`viral tail assembly`, IEA, `GO_REF:0000043`): **TOO_GENERAL**. Entailed by the more specific child term `GO:0098004` (`virus tail fiber assembly`) present on this gene.
- `GO:0098004` (`virus tail fiber assembly`, IEA, `GO_REF:0000002` InterPro:IPR003458): **ACCEPT**. Core function of `gpU'` as a T4 gp38 / Mu gpU' family tail fiber assembly chaperone required for `gpS'` (`Sc-S'v`) fiber maturation [PMID:2526777, PMID:15489417].
- `GO:0098678` (`viral tropism switching`, IEA, `GO_REF:0000043`): **KEEP_AS_NON_CORE**. Alternating expression of `Sv-U` versus `S'v-U'` via Cin-mediated inversion of the C-segment switches P1 host tropism; `U'` is the C(-)-specific tail-fiber assembly effector of this genetic switch [PMID:6327269, PMID:15489417].
