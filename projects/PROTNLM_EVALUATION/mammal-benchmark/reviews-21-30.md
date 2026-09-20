# Paired horse–human reviews: cases 21–30

All ten pairs have an initial annotation review and human research. Source-specific uncertainty is retained in the YAML; no PENDING rows remain. ProtNLM narrative and GO statements are assessed separately.

| Gene | Human rows | Horse rows | ProtNLM GO | Narrative | Human research |
|---|---:|---:|---|---|---|
| CDK7 | 146 | 23 | CNN 1, COR 1 | — | Falcon |
| MAP2K2 | 174 | 15 | COR 1 | — | Falcon |
| ZDHHC23 | 13 | 9 | CNN 1 | — | Falcon |
| CH25H | 25 | 14 | LSP 2, CNN 1 | — | Falcon |
| BCAT2 | 42 | 5 |  | supported | Falcon |
| SIRT5 | 68 | 1 | UNC 1 | UNC | Falcon |
| USP8 | 83 | 9 | CNN 1 | supported | Falcon |
| OMA1 | 54 | 16 | CNN 1 | — | Falcon |
| EFR3A | 13 | 1 | UNC 1 | — | Falcon |
| CACNB3 | 46 | 10 | COR 1 | — | Falcon |

## Findings needing attention

- **SIRT5 F6S899:** the chosen sequence loses the normal C-terminal conservation pattern, substitutes Trp at two human zinc-ligand cysteines, and changes or loses several NAD-contact segments. Metal binding and the multi-activity narrative remain UNC for this exact protein model. This is not yet a demonstrated horse pseudoenzyme.
- **EFR3A A0A9L0S4L8:** the N-terminal cysteine cluster is missing, although the downstream sequence is 98.24% identical. Primary human mutagenesis supports the significance of losing this membrane anchor; membrane recruitment remains UNC.
- **BCAT2:** catalysis is supported, but the extra 60-residue N-terminal segment means the exact-model mitochondrial targeting remains unresolved.
- **CDK7:** the seven-subunit TFIIH core excludes the CAK module; protein kinase activity should not become ATP-driven DNA modification. The human experimental DNA-activity assignment remains UNDECIDED until its whole-complex assay is resolved.
- **CH25H:** C4 methylsterol oxidation/zymosterol synthesis should not be transferred from other sterol enzymes to a cholesterol C25 hydroxylase. Lipid biosynthesis itself remains a defensible description of oxysterol formation.
- **CACNB3:** the beta subunit is a channel regulator rather than a pore-forming subunit.
- **USP8:** deubiquitination can participate in cargo degradation; the ubiquitin-dependent catabolic-process prediction is not refuted merely by the deubiquitinase label.

## Evidence and validation

The comparison scripts, alignments, residue maps and sequence hashes are in each horse gene’s bioinformatics directory. Primary source caches were fetched with the repository pipeline; rate-limited requests were retried with a delay. Human annotations use primary findings and experimentally supported UniProt passages; research reports serve as literature syntheses and source leads. Target annotation overlap is distinct from unknown training-set membership.

Individual gene validation and prediction-evidence validation were run. Remaining advisories concern evidence-specific UNDECIDED rows, omission of unsupported horse core functions, structured propagation metadata, and research-report citation suggestions. The review is an initial evidence pass, not expert sign-off.
