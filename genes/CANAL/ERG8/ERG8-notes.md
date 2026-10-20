# CANAL ERG8 notes

## 2026-10-17 fungal PAINT/IBA review

ERG8 is Candida albicans phosphomevalonate kinase, the GHMP-family enzyme that
phosphorylates 5-phosphomevalonate to 5-diphosphomevalonate in the mevalonate
pathway [PMID:11243736 "Phosphomevalonate kinase (PMK; EC 2.7.4.2) catalyzes
the phosphorylation of 5-phosphomevalonate into 5-diphosphomevalonate"].

The PTHR31814 family review is the right frame for the IBA rows. PTN001274235
places phosphomevalonate kinase activity and IPP biosynthesis on the
fungal/plant GHMP branch; PTN001274236 places ergosterol biosynthesis on the
fungal branch; both apply to Candida ERG8. PTN000781523 is different: it is a
Eukaryota-level peroxisome node seeded only by Arabidopsis AT1G31910, and the
PTHR31814 family review already marks it NEEDS_PRUNING for fungal ERG8 proteins.

The CGD ND cellular_component row is a root no-data placeholder, not evidence
for a real location. I removed it while accepting the UniProt/SubCell
cytoplasm row as the best current compartment call for this soluble fungal
mevalonate-pathway kinase.

PMID:11737641 and PMID:14653518 are both abstract-only in the cache. Murad et
al. is cited by UniProt for NRG1 regulation of ERG8, but the cached abstract
does not show ERG8-specific data. Song et al. is useful for C. albicans sterol
pathway context, and UniProt cites it for ERG8 pathway context, but the abstract
does not name ERG8.

Newer-paper searches for direct C. albicans ERG8 literature did not find a
newer functional paper. The main cross-species hit was a 2024 Aspergillus
oryzae AoErg8 functional study, which is corroborating context for fungal
phosphomevalonate kinases rather than direct evidence for C. albicans ERG8.
