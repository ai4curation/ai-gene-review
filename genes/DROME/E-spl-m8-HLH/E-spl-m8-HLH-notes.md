# E(spl)m8-HLH (UniProt P13098) notes

Directory is `E-spl-m8-HLH` because parentheses are unsafe in paths; the
FlyBase symbol `E(spl)m8-HLH` (FBgn0000591) is recorded as `gene_symbol`.
Fetched with `just fetch-gene DROME P13098 --alias E-spl-m8-HLH`.
PANTHER PTHR10985 (BASIC HELIX-LOOP-HELIX TRANSCRIPTION FACTOR, HES-RELATED).

## Deep research
Falcon launched 2026-09-30; wrapper timed out at 600 s and perplexity fallback
unavailable. See end of file for final status.

## Key findings
- Direct Notch target in E(spl)-C
  [PMID:10373509 "The most immediate transcriptional target genes of Notch activation in Drosophila melanogaster encode seven bHLH proteins (Mδ, Mβ, Mγ, M3, M5 M7, and M8)"]
- Binds N-box as homo/heterodimer and attenuates proneural activation (the protein called ENHANCER OF SPLIT = m8)
  [PMID:8078474 "both proteins were found to attenuate the transcriptional activation mediated by the proneural bHLH proteins LETHAL OF SCUTE and DAUGHTERLESS"]
- Optimal class C site TGGCACGTG(C/T)(C/T)A [PMID:10373509]
- Groucho interacts with all E(spl) bHLH [PMID:9371806]; Gro always needed [PMID:12466194]
- CK2 phosphorylates m8 at Ser159; direct complex [PMID:11208814]
- CK2/E(spl) genetic interactions in R8 and bristle lateral inhibition [PMID:16930955]

## Review decisions
- Core MF GO:0001227 DNA-binding transcription repressor activity, RNA pol II-specific; GO:0001222 transcription corepressor binding (via MODIFY of Groucho protein-binding rows).
- IBA anterior/posterior pattern specification (PTN000105428) MARK_AS_OVER_ANNOTATED: vertebrate segmentation-clock role, fly segmentation Notch-independent.
- mesoderm development (PMID:1913825) kept non-core; early E(spl) alleles may not be m8-specific.
- negative regulation of gene expression MODIFIED to GO:0000122.

## PAINT nodes (GOA WITH/FROM)
- PTN004213585: GO:0000122, GO:0000981, GO:0005634, GO:0000978
- PTN000105428: GO:0009952, GO:0050767

## Deep research final status
Falcon output arrived after the wrapper timeout (`E-spl-m8-HLH-deep-research-falcon.md`); reviewed and cited (WRPW-Groucho, CK2 Ser159 requirement for Atonal repression, Bandyopadhyay 2016 per deep research).
