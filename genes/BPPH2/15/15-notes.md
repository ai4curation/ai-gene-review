# Curation Notes: Bacillus phage phi29 Gene 15 (Endolysin / Lysozyme gp15, P11187)

## Summary of Gene Function
- **Product**: Endolysin / muramidase gp15 (UniProt `P11187`, 258 aa, ~28.0 kDa, EC 3.2.1.17).
- **Modular Architecture**: Modular Gram-positive phage endolysin consisting of:
  1. **N-terminal catalytic GH24 phage-type lysozyme (muramidase) domain** (residues 1–156): Hydrolyzes the beta-1,4-glycosidic bond between N-acetylmuramic acid (MurNAc) and N-acetylglucosamine (GlcNAc) in the *Bacillus subtilis* peptidoglycan backbone (`GO:0003796` `lysozyme activity`, `GO:0009253` `peptidoglycan catabolic process`; [PMID:3469652](file:///Users/cjm/orca/workspaces/ai-gene-review/aigr-agy-phages/publications/PMID_3469652.md)).
  2. **C-terminal cell-wall-binding domain containing two LysM repeats** (residues 165–208 and 213–256): Mediates high-affinity binding to the *B. subtilis* peptidoglycan cell wall ([15-uniprot.txt](file:///Users/cjm/.gemini/antigravity-cli/brain/4b846598-3920-4c66-ba84-db24d924c2d1/scratch/prd1_phi29/genes/BPPH2/15/15-uniprot.txt)).
- **Role in Host Cell Lysis**: Synthesized in the host cytoplasm (`GO:0030430`) during late infection. Once the `gp14` holin forms lesions in the cytoplasmic membrane, `gp15` crosses into the cell wall space and degrades the peptidoglycan sacculus, causing rapid host cell cytolysis (`GO:0044659` `viral release from host cell by cytolysis`) to release progeny virions ([PMID:820555](file:///Users/cjm/orca/workspaces/ai-gene-review/aigr-agy-phages/publications/PMID_820555.md), [PMID:3469652](file:///Users/cjm/orca/workspaces/ai-gene-review/aigr-agy-phages/publications/PMID_3469652.md)).

## Review of Existing GO Annotations
1. `GO:0003796` (`lysozyme activity`, IEA `GO_REF:0000120` and IMP `PMID:3469652`): **ACCEPT** — Directly demonstrated on purified gp15 protein in [PMID:3469652](file:///Users/cjm/orca/workspaces/ai-gene-review/aigr-agy-phages/publications/PMID_3469652.md).
2. `GO:0003824` (`catalytic activity`, IEA `GO_REF:0000043`): **TOO_GENERAL** — Entailed by `GO:0003796` (`lysozyme activity`).
3. `GO:0009253` (`peptidoglycan catabolic process`, IEA `GO_REF:0000120`): **ACCEPT** — Core biochemical process of the gp15 muramidase on host peptidoglycan.
4. `GO:0016787` (`hydrolase activity`, IEA `GO_REF:0000043`): **TOO_GENERAL** — Entailed by `GO:0003796` (`lysozyme activity`).
5. `GO:0016798` (`hydrolase activity, acting on glycosyl bonds`, IEA `GO_REF:0000043`): **TOO_GENERAL** — Entailed by `GO:0003796` (`lysozyme activity`).
6. `GO:0016998` (`cell wall macromolecule catabolic process`, IEA `GO_REF:0000002`): **TOO_GENERAL** — Entailed by `GO:0009253` (`peptidoglycan catabolic process`).
7. `GO:0030430` (`host cell cytoplasm`, IEA `GO_REF:0000044`): **ACCEPT** — gp15 lacks a secretory signal peptide and accumulates in the host cytoplasm until released through gp14 holin pores.
8. `GO:0031640` (`killing of cells of another organism`, IEA `GO_REF:0000043`): **TOO_GENERAL** — Entailed by `GO:0044659` (`viral release from host cell by cytolysis`) on this record.
9. `GO:0042742` (`defense response to bacterium`, IEA `GO_REF:0000043`): **REMOVE** — False keyword mapping from `KW-0081` (`Bacteriolytic enzyme`); phage phi29 is a virus lysing its bacterial host to release progeny virions, not an organism mounting an antibacterial immune defense response.
10. `GO:0044659` (`viral release from host cell by cytolysis`, IEA `GO_REF:0000104` and IMP `PMID:820555`): **ACCEPT** — Directly supported by gene 15 mutant phenotypes (delayed lysis rescued by artificial lysis; [PMID:820555](file:///Users/cjm/orca/workspaces/ai-gene-review/aigr-agy-phages/publications/PMID_820555.md)).
