# HMG1 notes

UniProt A0A1D8PD39; Candida Genome Database HMG1 / orf19.1031 /
CAALFM_C103780CA; 3-hydroxy-3-methylglutaryl-coenzyme A reductase 1
with a sterol-sensing membrane region and a class I HMGR catalytic domain
[file:CANAL/HMG1/HMG1-uniprot.txt "HMG1 catalyzes the reduction of hydroxymethylglutaryl-CoA (HMG-CoA) to mevalonate"].

## 2026-10-24

- `just fetch-gene CANAL HMG1` created 15 GOA annotation rows and cached the
  three PMIDs referenced by CGD/GOA. Falcon deep research and the
  `perplexity-lite` fallback both failed because no provider API keys were
  available, so this review uses UniProt, GOA, cached publications, PTHR10572,
  existing yeast and fission-yeast reviews, and manual web/PubMed searches.
- PTHR10572 is the class I HMG-CoA reductase family in this project. The same
  SF24 subfamily contains *C. albicans* HMG1, *S. cerevisiae* HMG1/HMG2,
  *S. pombe* hmg1, *A. fumigatus* hmg1/hmg2, and *A. nidulans* AN1593
  [file:interpro/panther/PTHR10572/PTHR10572-entries.csv
  "A0A1D8PD39,3-hydroxy-3-methylglutaryl-coenzyme A reductase 1,protein,237561"].
- The family review already calls `PANTHER:PTN000060346` sound for
  `GO:0004420`, `GO:0008299`, and `GO:0016126`, calls the eukaryotic
  `PANTHER:PTN000060347` ER-membrane placement sound, calls the fungal
  `PANTHER:PTN000832055` ergosterol-biosynthesis placement sound, and calls the
  deep `PTN000060347` peroxisomal-membrane placement in need of pruning
  [file:interpro/panther/PTHR10572/PTHR10572-review.yaml
  "The fungal branch needs an IRD; the term should not sit at a node above the fungi"].
- Song et al. 2003 is abstract-only here. It identifies lovastatin as an HMG1
  inhibitor and reports that early sterol-pathway transcripts, including HMG1,
  did not change under lovastatin plus fluconazole
  [PMID:14653518 "This study examines gene expression of the sterol pathway in response to lovastatin, an inhibitor of HMG-CoA reductase (Hmg1p)"].
  That supports the identity of Hmg1 as the HMG-CoA reductase target but is not
  a direct enzymology paper.
- Xu et al. 2007 used a *C. albicans* heterozygous deletion collection in the
  CaFT assay and profiled ergosterol-biosynthesis inhibitors, including
  lovastatin
  [PMID:17604452 "The profiles of additional inhibitors of ergosterol biosynthesis, including terbinafine, lovastatin, and dyclonine, are described in Text S1"].
  The full text confirms the assay and drug class, but the extracted supporting
  material does not include the lovastatin/HMG1 table row itself.
- Cabezon et al. 2009 is abstract-only here. The abstract describes a
  *C. albicans* plasma-membrane proteome with "214 membrane proteins", but does
  not name Hmg1 or distinguish core plasma-membrane residents from contaminants
  and membrane-associated carryover
  [PMID:19824013 "a total of 214 membrane proteins were identified"].
  This is weak support for a plasma-membrane location for a polytopic ER enzyme.
- Andrade-Pavon et al. 2023 is the newest paper found in the web/PubMed sweep
  that mentions *C. albicans* HMG-CoA reductase directly. It tested
  alpha-asarone-derived HMGR inhibitors against *C. albicans* growth and
  ergosterol synthesis and modeled CaHMGR, but directly assayed recombinant
  CgHMGR rather than CaHMG1
  [PMID:38069194 "Since the recombinant HMGR from C. albicans is currently being investigated"].
