# ndhH notes

- Fetched with `just fetch-gene POPTR ndhH`.
- Curated as a chloroplast NDH subunit using the UniProt reviewed entry and GOA snapshot. Key decisions: keep thylakoid/photosynthetic-chain annotations, refine generic NAD(P)H oxidoreductase activity to quinone-acceptor oxidoreductase activity, and add direct NDH complex/proton-coupled electron-transport context from UniProt.

- Addressed PR #469 review on 2026-05-10: GO:0019684 was narrowed to NEW GO:0009778 cyclic photosynthetic phosphorylation, using the official QuickGO label for cyclic photophosphorylation rather than GO:0009773, which QuickGO defines as photosynthetic electron transport in photosystem I.
