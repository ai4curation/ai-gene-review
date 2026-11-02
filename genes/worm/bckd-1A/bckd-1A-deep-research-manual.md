# bckd-1A (Y39E4A.3; UniProt O45924) - manual literature review

Deep-research API providers were not available for this review; this file was written
by hand from cached publications (`publications/PMID_*.md`), PubMed searches and the
UniProt record. It is not the output of an automated deep-research provider.

## Identity

- C. elegans Y39E4A.3, named bckd-1A; reviewed UniProt entry O45924 (ODBA_CAEEL),
  "2-oxoisovalerate dehydrogenase subunit alpha, mitochondrial", 431 aa, with a predicted
  N-terminal mitochondrial transit peptide.
- Ortholog of human BCKDHA (P12694) and bovine BCKDHA (P11178): E1 alpha chain of the
  branched-chain alpha-ketoacid dehydrogenase (BCKDH) complex. Pfam PF00676 (E1_dh),
  thiamine-diphosphate-binding fold, PANTHER PTHR43380:SF1.
- UniProt: "Belongs to the BCKDHA family."; thiamine diphosphate and K(+) binding sites
  are annotated by similarity to human P12694.

## Literature

1. Kniazeva et al. 2004, PLoS Biol (PMID:15340492; full text cached).
   - Identified Y39E4A.3 as the C. elegans E1 alpha subunit by sequence similarity:
     [PMID:15340492 "We identified a predicted C. elegans protein, Y39E4A.3, with significant sequence homology to the E1 alpha subunit of BCKAD"]
   - RNAi knockdown reduced the monomethyl branched-chain fatty acids C15ISO and C17ISO:
     [PMID:15340492 "RNAi of Y39E4A.3 led to a significant decrease in C15ISO and C17ISO production"]
   - Pathway context: BCKAD provides the branched acyl-CoA primers that are then elongated:
     [PMID:15340492 "Key enzymes engaged in synthesizing the mmBCFA acyl-CoA primers are branched-chain aminotransferase (BCAT) and the branched-chain α-keto-acid dehydrogenase (BCKAD) complex"]
   - No enzyme assay of the worm protein was performed; the evidence is RNAi + GC
     fatty-acid profiling, plus homology.

2. Jia et al. 2016, J Biol Chem (PMID:26683372; full text cached).
   - Studies the E2 subunit dbt-1 (ZK669.4) mutant; confirms that E1beta (F27D4.5) and
     E1alpha (Y39E4A.3) RNAi also reduce mmBCFAs.
   - [PMID:26683372 "Here we show that disrupting BCKDH in Caenorhabditis elegans causes mmBCFA deficiency, in addition to BCAA accumulation."]
   - [PMID:26683372 "Worms with deficiency in BCKDH function manifest larval arrest and embryonic lethal phenotypes, and mmBCFA supplementation suppressed both without correcting BCAA levels."]
   - Complex composition: [PMID:26683372 "BCKDH is composed of three subunits, E1, E2 and E3, of which E1 and E2 are unique to this complex."]

3. Zdraljevic et al. 2019, eLife (PMID:30958264; cached). Natural variation in dbt-1
   (E2) explains arsenic responses via iso-branched-chain fatty acids. Concerns the E2
   subunit; relevant only as context for the worm BCKDH complex.

## Synthesis

bckd-1A encodes the E1 alpha subunit of the mitochondrial BCKDH complex. With the E1
beta chain it forms the thiamine-diphosphate-dependent E1 component that decarboxylates
branched-chain 2-oxo acids (from leucine, isoleucine, valine) and transfers the acyl
group to the lipoyl domain of DBT-1 (E2). In C. elegans the resulting branched-chain
acyl-CoAs serve both BCAA catabolism and as primers for monomethyl branched-chain fatty
acid (C15ISO, C17ISO) synthesis; loss of mmBCFAs is the main cause of the developmental
arrest of BCKDH-deficient worms.
