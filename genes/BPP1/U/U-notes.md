# U (Q71TD6) Curation Notes — Escherichia phage P1

## Functional Summary
- **Gene symbol**: `U` (third gene of the `R-S-U` tail-fiber operon in the C(+) orientation of the invertible C-segment).
- **Protein**: Tail fiber assembly protein U (`gpU`; 176 aa, ~19.4 kDa; InterPro `IPR003458` / Pfam `PF02413` `Caudo_TAP`).
- **Biological role**:
  - `gpU` is the tail fiber assembly protein (chaperone) co-expressed with the `Sc-Sv` isoform of the tail fiber structural protein `gpS` (`P22588`) when the Cin-invertible C-segment is in the C(+) orientation, which confers infectivity on *Escherichia coli* K-12 and C strains [PMID:6327269, PMID:2526777, PMID:15489417].
  - `gpU` shares 95% sequence identity with bacteriophage Mu gpU and is homologous to bacteriophage T4 gp38 and phage lambda Tfa (`IPR003458`), which act in the host cell cytoplasm (`GO:0030430` `host cell cytoplasm`) as dedicated intramolecular/intermolecular chaperones required for folding and trimerization of the distal C-terminal receptor-binding region of the long tail fiber (`GO:0098004` `virus tail fiber assembly`) [PMID:2526777, PMID:15489417].
  - Because `gpU` shares C-terminal sequence similarity with lambda Tfa and differs from its alternative isoform `gpU'` (`Q71TD7`) primarily in its C-terminal region, Łobocka et al. 2004 [PMID:15489417] noted that `gpU` may also remain associated with the tail fiber tip to participate in host adsorption (`GO:0019062` `virion attachment to host cell`), although `gpU` was not detected in LC-MS/MS proteomics of CsCl-purified P1 virions [PMID:35458408].

## Review of Existing GOA Annotations
- `GO:0019062` (`virion attachment to host cell`, IEA, `GO_REF:0000043`): **KEEP_AS_NON_CORE**. `gpU` is required to fold the `Sv` receptor-binding tip of `gpS` and has been proposed by homology to lambda Tfa / Mu gpU to remain at the fiber tip to assist LPS receptor binding [PMID:15489417], whereas its primary conserved molecular role is tail fiber assembly (`GO:0098004`).
- `GO:0030430` (`host cell cytoplasm`, IEA, `GO_REF:0000043` and `GO_REF:0000044`): **ACCEPT**. `gpU` functions in the host bacterial cytoplasm during late lytic development to chaperone the folding and assembly of nascent `gpS` tail fibers [PMID:15489417].
- `GO:0046718` (`symbiont entry into host cell`, IEA, `GO_REF:0000043`): **TOO_GENERAL**. Entailed by `GO:0019062` (`virion attachment to host cell`, which is `part_of` `GO:0046718`).
- `GO:0098003` (`viral tail assembly`, IEA, `GO_REF:0000043`): **TOO_GENERAL**. Entailed by the more specific child term `GO:0098004` (`virus tail fiber assembly`) present on this gene.
- `GO:0098004` (`virus tail fiber assembly`, IEA, `GO_REF:0000002` InterPro:IPR003458): **ACCEPT**. Core function of `gpU` as a T4 gp38 / Mu gpU family tail fiber assembly protein required for `gpS` (`Sc-Sv`) fiber maturation [PMID:2526777, PMID:15489417].
- `GO:0098678` (`viral tropism switching`, IEA, `GO_REF:0000043`): **KEEP_AS_NON_CORE**. Alternating expression of `Sv-U` versus `S'v-U'` via Cin-mediated inversion of the C-segment switches P1 host range (`viral tropism switching`); `U` is one of the two alternatively expressed tail-fiber assembly effectors of this switch [PMID:6327269, PMID:15489417].
