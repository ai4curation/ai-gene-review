# E manual review notes

## 2026-05-21 deeper SPKW-BPT4 review

Reviewed the AIGR review skill, `E-ai-review.yaml`, `E-goa.tsv`, `E-uniprot.txt`, `E-deep-research-falcon.md`, and cached publications `PMID_1201752.md`, `PMID_4582731.md`, `PMID_4865643.md`, `PMID_8266098.md`, and `PMID_22389108.md`.

Core molecular function is lysozyme/muramidase activity. The strongest accessible cached experimental support is [PMID:1201752 Studies on the specificity of action of bacteriophage T4 lysozyme., "T4 acts as an endo-acetylmuramidase capable of cleaving glycosidic bonds"]. The cached `PMID_4865643.md` only contains the title/abstract stub, so it remains marked as full-text unavailable in the YAML.

The process context is viral release by cytolysis, not defense against bacteria. UniProt states that the endolysin participates with holin and spanin proteins in programmed host cell lysis releasing mature viral particles, and the deep research file places E in the holin-endolysin-spanin lysis pathway. This supports keeping `GO:0044659 viral release from host cell by cytolysis` as core and changing the broad `GO:0031640 killing of cells of another organism` row to `MODIFY`, not just a vague over-annotation.

The `PMID:4582731` row remains a reference-level removal. The cached paper is titled [PMID:4582731 Bacteriophage T7 lysozyme is an N-acetylmuramyl-L-alanine amidase., "Bacteriophage T7 lysozyme is an N-acetylmuramyl-L-alanine amidase"], so it should not support a T4 gene `E` annotation even though T4 lysozyme activity is otherwise correct.
