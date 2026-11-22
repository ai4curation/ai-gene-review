# Manual deep research: worm unc-50 (Q10045)

## Scope and provenance

The configured Falcon deep-research provider was unavailable on 2026-11-21, and the
Perplexity-lite fallback also failed. This manual synthesis uses the local UniProt
record, the seeded GOA table, the WormBase MOD description, the PANTHER
PTHR12841 PAINT trace and the two cached primary references. It is deliberately
named `-deep-research-manual.md`, not after a provider.

PMID:17853888 initially cached as abstract-only because PMC HTML/PDF fell back to
a Google reCAPTCHA page and Europe PMC full-text routes were unavailable. The
EMBO PDF endpoint for doi:10.1038/sj.emboj.7601858 was reachable manually and was
used to check the exact UNC-50/GEA1 and neuromuscular-junction evidence without
editing the cached publication file.

## Core identity

UNC-50 is the C. elegans member of the eukaryotic UNC-50/Gmh1 family and has five
predicted transmembrane segments in the reviewed UniProtKB Q10045 record. P47102,
the WITH/FROM accession on the protein-binding row, resolves to Saccharomyces
cerevisiae GEA1. P48182, the WITH/FROM accession on the regulation-of-muscle-
contraction row, resolves to the C. elegans ACR-2 receptor subunit.

PTHR12841-paint.tsv contains: PTHR12841 PTN000303504 GO:0000139 C IBD. The PAINT
row uses the C. elegans WBGene00006785 seed and the S. cerevisiae GMH1 seed at a
eukaryotic UNC-50-family node; `just paint-losses worm unc-50` reported no IRD or
IKR loss on the Q10045 lineage.

## Golgi localization and L-AChR trafficking

Eimer et al. showed that C. elegans unc-50 mutants lose functional
levamisole-sensitive acetylcholine receptors at body-wall neuromuscular junctions
without losing GABA-gated currents in the same muscle. The authors summarized the
mechanistic result as: "UNC-50 is required in body-wall muscles for the trafficking
of the assembled Lev-AChR to the NMJ." For surface receptor localization, they
detected cell-surface LEV-1-4xHA at wild-type but not unc-50 mutant NMJs after
live injection of labeled antibody, and anti-UNC-29 immunofluorescence detected
the endogenous L-AChR at wild-type NMJs but not at unc-50 mutant synaptic sites or
intracellular compartments.

The same study expressed functional fluorescent UNC-50 fusions in body-wall
muscle and found that mRFP-UNC-50 and Mannosidase II-GFP staining showed 91 +/-
3% colocalization. mRFP-UNC-50 did not overlap an ER-resident GFP-cytochrome b5
fusion. These data support a Golgi, not ER, steady-state localization.

In unc-50 mutants, cup-5 impairment of lysosome biogenesis partially restored
detectable UNC-29 protein, but the double mutants were still levamisole-resistant.
Eimer et al. concluded that in the absence of UNC-50 Lev-AChRs enter the lysosomal
compartment and are efficiently degraded by the lysosomes. UNC-50 therefore acts
after assembly of the receptor, routing assembled receptors through the Golgi
toward the cell surface rather than to a degradative compartment.

## Gea1p interaction

The WormBase IPI row names UniProtKB:P47102, the S. cerevisiae ARF guanine-
nucleotide exchange factor GEA1. Eimer et al. tested whether metazoan UNC-50
family members shared the yeast Gmh1p interaction with Gea1p: "UNC-50, like the
yeast Gmh1 and the human hGmh1, specifically interacted with the C-terminus of
the yeast Arf GEF Gea1p." The authors also reported that the Gea1L862S mutation
strongly reduced this interaction. The interaction is real but cross-species and
was assayed with yeast Gea1p aa749-1408, so it supports conservation of an
UNC-50/Gea-like Arf-GEF binding surface rather than a specific C. elegans protein
partner annotation.

## ACR-2R ancillary factor

Jospin et al. studied the neuronal ACR-2 receptor. Their extragenic suppressor
screen of acr-2(n2420gf) recovered unc-50 and unc-74 loss-of-function alleles
alongside unc-38 and unc-63 alleles. They inferred that "loss-of-function
mutations in unc-50 and unc-74 suppress acr-2(n2420gf) suggests that these two
ancillary proteins also function in ACR-2R assembly and trafficking." This is a
second receptor system for UNC-50, but the paper uses the convulsion phenotype as
an indirect readout of ACR-2R function in cholinergic motor neurons.

## Curation implications

1. Accept Golgi membrane for the direct WormBase IDA row, the UniProt
   subcellular-location IEA row and the PTHR12841 IBA row.
2. Accept receptor localization to synapse as the core biological-process row:
   UNC-50 acts in muscle on the post-assembly route that directs L-AChR to the
   neuromuscular-junction surface.
3. Keep the ACR-2R genetic interaction with P48182 as non-core physiological
   context; ACR-2 is a neuronal receptor subunit, and the convulsion screen is
   an indirect readout of the receptor-trafficking role.
4. Remove the bare GO:0005515 row under the protein-binding policy. The
   cross-species yeast Gea1p interaction is valid experimental evidence, but the
   generic GO term adds no specific molecular function for UNC-50.
