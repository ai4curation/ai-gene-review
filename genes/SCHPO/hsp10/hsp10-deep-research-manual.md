# Manual deep research for S. pombe hsp10

Automated deep research was attempted with Falcon and the `perplexity-lite` fallback, but neither provider was available in this environment. The cached primary literature and the existing budding-yeast HSP10/HSP60 reviews were sufficient for a focused manual review of the fission-yeast Cpn10 ortholog.

## Functional summary

S. pombe hsp10 (O59804; SPCC550.06c) is the Cpn10/GroES-family mitochondrial co-chaperonin. UniProt identifies it as the 10 kDa mitochondrial heat shock protein, places it in the mitochondrial matrix, and summarizes the conserved similarity-based function as partnership with Cpn60 in mitochondrial protein biogenesis.

The experimentally characterized budding-yeast ortholog, HSP10/CPN10, is a mitochondrial Cpn10 cofactor for Hsp60. Rospert et al. identified yeast mitochondrial Cpn10 by functional complementation of Hsp60-mediated substrate refolding: Rubisco denatured onto yeast Cpn60 required yeast Cpn10 for subsequent refolding, and yeast Cpn60 plus yeast Cpn10 formed a stable MgATP-dependent complex [PMID:7902576].

Hohfeld and Hartl tested HSP10 in vivo and found that Hsp10 is an essential part of the mitochondrial protein-folding system, with temperature-sensitive hsp10 alleles impairing folding and assembly of proteins imported into the matrix. The same work also connected Hsp10 to sorting of selected substrates, including Rieske Fe/S protein, that transit through the matrix en route to the intermembrane space [PMID:7913473].

Dubaquie et al. purified the yeast mitochondrial Hsp60/Hsp10 system and measured tight, nucleotide-dependent Hsp10-Hsp60 binding: one Hsp10 bound Hsp60 in ADP with apparent Kd about 0.9 nM, a second with Kd about 24 nM. In ATP, the purified chaperonins mediated mitochondrial malate dehydrogenase refolding, and Hsp10 inhibited Hsp60 ATPase activity, coupling the co-chaperonin to Hsp60 ATP turnover rather than establishing ATP binding by Hsp10 itself [PMID:9256426].

The conserved mitochondrial matrix localization is supported directly in budding yeast by Cpn10 import without detectable cleavage [PMID:7903252] and in S. pombe by the PomBase HDA annotation from the ORFeome YFP localization dataset [PMID:16823372].

## Annotation implications

- `GO:0051087 protein-folding chaperone binding`, `GO:0044183 protein folding chaperone`, and `GO:0006457 protein folding` are the conserved core function.
- `GO:0005759 mitochondrial matrix` is the precise location for hsp10 action; the broader root term `GO:0005739 mitochondrion` should also be retained under the root-organelle policy.
- `GO:0030150 protein import into mitochondrial matrix` is pathway context rather than hsp10's direct transport role. Hsp10 folds and assembles imported substrates after translocation.
- `GO:0046872 metal ion binding` is weakly propagated from a Mycobacterium tuberculosis Cpn10 structure that identified dome-loop metal sites [PMID:11807250]. This is plausible but not established as a conserved mitochondrial Hsp10 activity.
- `GO:0005524 ATP binding` maps the Cpn10 signatures onto the Cpn60 side of the ATPase cycle and should be removed for hsp10.

## GO-CAM consistency

The model activity `gomodel:69729a3800007453/698e557b00000783` has the same basic biology as this gene review: S. pombe hsp10 enables `GO:0044183`, occurs in `GO:0005759`, and is connected to Hsp60/Mcp60 folding after mitochondrial import. Its enabled_by ISO evidence, however, cites `SGD:S000000004`, which is SSA1/YAL005C. The S. cerevisiae HSP10 ortholog is `SGD:S000005546`, which already appears in the same hsp10 activity's matrix-location IBA.
