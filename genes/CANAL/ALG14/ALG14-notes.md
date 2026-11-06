# ALG14 notes

## 2026-11-06

- Default Falcon deep research failed because `agentapi` was unavailable, so no provider-authored `ALG14-deep-research-falcon.md` was created.
- PubMed searches for `"Candida albicans" ALG14`, `"Candida albicans" "UDP-N-acetylglucosamine transferase subunit"`, and fungal ALG14/LLO combinations did not find a *Candida albicans* ALG14 functional characterization.
- `PTHR12154` is a coherent single-subfamily ALG14 review. The cached PAINT assertions place `GO:0043495` and `GO:0043541` at the eukaryote-wide `PTN000254968` node with `taxon:2759` scope, and place `GO:0006488` at `PTN001741631`.
- The molecular-function and complex assertions are consistent with the *S. cerevisiae* Alg13/Alg14 evidence: Gao et al. 2005 showed that Alg14 "functions as a membrane anchor that recruits Alg13 to the cytosolic face of the ER" [PMID:16100110]; Bickel et al. 2005 found that "Alg13p associates with Alg14p to a complex forming the active transferase" that makes GlcNAc2-PP-Dol [PMID:16100113]; and Noffz et al. 2009 showed that "the Alg7p, Alg13p, and Alg14p glycosyltransferases form a functional multienzyme complex" [PMID:19129246].
- The EnsemblFungi `GO:0098548` cytoplasmic side of Golgi membrane row traces to the *S. cerevisiae* ALG14 annotation that the yeast review already modifies to `GO:0098554` cytoplasmic side of endoplasmic reticulum membrane. Alg14 acts at the cytoplasmic face of the ER, not at the Golgi.
- The EnsemblFungi lipid-droplet row traces to the condition-specific *S. cerevisiae* oleate-growth localization row and is marked over-annotated for the same reason: it can be a valid LD-associated ER localization without defining the constitutive site of Alg14 activity.
