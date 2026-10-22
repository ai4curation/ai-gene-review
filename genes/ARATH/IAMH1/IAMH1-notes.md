# IAMH1 (AT4G37550) curation notes

## Identity

- Locus AT4G37550. There are seven unreviewed UniProt entries for this locus (B9DFI3, Q9SZE9, F4JS37, F4JS39,
  A0A178UXH8, A0A1P8B5Z2, A0A1P8B5Z4), corresponding to alternative gene models. I used A0A178UXH8 (456 aa,
  reference proteome UP000006548) because it is the entry that carries TAIR's GO annotations; the other
  entries carry only the InterPro2GO IEA row (QuickGO, 2026-10-21).
- Symbol IAMH1 (INDOLE-3-ACETAMIDE HYDROLASE 1) was assigned by Gao et al. 2020
  [PMID:32327358 "We renamed #483 mutant iamh1–1 (IAM hydrolase 1) and At4g37550 gene IAMH1."].
- Tandem paralog of IAMH2 (AT4G37560), 90% identical [PMID:32327358 "IAMH2 and IAMH1 share 90% amino acid sequence identity."].
  See `genes/ARATH/IAMH2/IAMH2-notes.md` for the shared family and domain analysis.

## Deep research

Automated deep research (`just deep-research-falcon ARATH IAMH1 --fallback perplexity-lite`) failed in this
session because no provider API keys were available. The literature was searched manually through PubMed;
PMID:32327358 is the only primary functional paper on IAMH1. PMID:42844995 (2026) is about IAMH2 but
discusses IAMH1 as background.

## Function evidence (Gao et al. 2020, PMID:32327358; full text read)

- Isolated from an EMS forward screen for IAM-insensitive mutants that keep normal auxin sensitivity. The
  allele iamh1-1 carries a premature stop codon; a T-DNA allele (iamh1-2) is also IAM-resistant.
- Complementation with the genomic fragment and with IAMH1pro:IAMH1-GFP:
  [PMID:32327358 "the IAMH1 genomic fragment fully restored the IAM sensitivity of the iamh1–1 mutant."]
  [PMID:32327358 "Such an observation further supports the hypothesis that IAMH1 is involved in converting IAM to IAA in Arabidopsis."]
- Expression: [PMID:32327358 "At seedling stage, the GUS expression was broadly distributed in cotyledons, true leaves, and root tips"]
  At the reproductive stage, GUS was seen in young flowers, gynoecia and inflorescences.
- Localization: [PMID:32327358 "Expression of IAMH1-GFP fusion driven by IAMH1 promoter showed that IAMH1 was clearly not expressed in the nucleus"]
  The cached text describes the signal only as non-nuclear and does not name another compartment.
- Double mutants iamh1-1 iamh2-2 and iamh1-1 iamh2-3 suppress iaaM-driven auxin overproduction and the
  IAM-induced rise in IAA and IAA conjugates, but have no developmental defect under normal growth conditions.
  Steady-state IAA is similar to wild type.
- I found no in vitro enzyme assay with purified IAMH1.
- Orthologs: [PMID:32327358 "IAMH1-like genes have been identified in all of the plant genomes including Chlamydomonas reinhardtii and Physcomitrella patens."]

## GO annotation decisions (summary)

- GO:0016811 (IEA): MODIFY to GO:0043864 indoleacetamide hydrolase activity (a descendant; OLS checked).
- GO:0005829 cytosol (HDA, Aryal et al. 2014): ACCEPT. It fits the non-nuclear GFP signal of a soluble
  enzyme without targeting signals.
- GO:0000325 plant-type vacuole (HDA, Carter et al. 2004 vegetative vacuole proteome) and
  GO:0005886 plasma membrane (HDA, membrane protein-correlation profiling, PMID:28887381): UNDECIDED,
  at the user's request (2026-10-22). These high-throughput detections are not judged in this review
  because the per-protein data were not examined. Context for a later reviewer:
  - The vacuole paper itself notes contaminants in the preparation (it excluded 15% of hits as potential
    chloroplast or mitochondrial contaminants).
  - The membrane study found many soluble proteins partitioned between cytosolic and membrane-associated pools.
  - The cytosol HDA row stays ACCEPT because it agrees with the IAMH1-GFP data and supports the core function.
- GO:0009507 chloroplast (ISM, AtSubP prediction): MARK_AS_OVER_ANNOTATED.
  - It is a single sequence-based prediction with no experimental support.
  - The first 80 residues of IAMH1 and IAMH2 are nearly identical (compared from the two UniProt files),
    yet IAMH2 has no chloroplast annotation.
  - None of the three proteomic datasets places IAMH1 in plastids.
- NEW GO:0009684 indoleacetic acid biosynthetic process (IMP, PMID:32327358).
  - Participation: IAMH1 is proposed to catalyse IAM to IAA, so it performs a step of the process.
  - Evidence: genetic and metabolite data. Comparator AMI1 carries GO:0009684 by IDA (QuickGO, taxon 3702).
  - Caveat: the evidence concerns IAM supplied exogenously or produced from the iaaM transgene. Endogenous
    IAA is unchanged in the double mutant.
