# ndhB1 notes

- Fetched with `just fetch-gene POPTR ndhB1`.
- Curated in parallel with ndhB2. Key decisions: modify respiratory-chain/ubiquinone annotations to chloroplast NDH/photosynthetic-chain equivalents, keep thylakoid localization, and treat ATP synthesis coupled electron transport as non-core relative to the direct NDH redox/proton-translocation role.

- Addressed PR #469 review on 2026-05-10: respiratory/light-reaction process review now points to NEW GO:0009778 cyclic photosynthetic phosphorylation. QuickGO defines GO:0009773 as photosynthetic electron transport in photosystem I, so GO:0009778 was used for the cyclic photophosphorylation process.

- Addressed PR #469 re-review on 2026-05-10: NEW annotation original_reference_id now points to the reviewed UniProt entry as the mechanistic source rather than a generic GO_REF.
