# SERINC3 curation notes

Date: 2026-07-18

## Retrieval record

- Fetched the reviewed UniProt record, all 17 GOA rows grouped into 15 review
  entries, and all five cited PubMed records.
- Inspected the full human SERINC3 cryo-EM and purified-proteoliposome study
  (PMID:37474505), both 2015 antiviral studies, the older Serinc-family lipid
  study, and the 2025 mechanism preprint PMID:41292925.
- Falcon failed with HTTP 402 and Perplexity-lite failed with HTTP 401. Manual
  synthesis is in `SERINC3-deep-research-manual.md`.

## Core conclusion

Core function: SERINC3 is a plasma-membrane phospholipid scramblase whose
incorporation into retroviral envelopes disrupts lipid asymmetry and restricts
viral infectivity.

The purified human protein flips PS, PE, and PC
[PMID:37474505, "purified hSERINCs reconstituted into proteoliposomes induce
flipping of phosphatidylserine (PS), phosphatidylethanolamine and
phosphatidylcholine."]. This is the most direct molecular evidence and makes
phospholipid scramblase activity the preferred term over the older generic
molecular-carrier annotation.

## Annotation decisions

- ACCEPT both Golgi-membrane records, all three plasma-membrane records,
  phospholipid scramblase activity, plasma-membrane phospholipid scrambling, and
  all three antiviral innate immune response records.
- MODIFY the two broad membrane annotations to plasma membrane, the directly
  demonstrated physiologically relevant location.
- MODIFY molecular carrier activity to phospholipid scramblase activity.
- KEEP_AS_NON_CORE perinuclear cytoplasm because this is principally the
  infection-dependent Nef-redirected pool.
- MARK_AS_OVER_ANNOTATED generic protein binding from a large
  neurodegeneration-focused interactome screen.
- Add no NEW GO term: the current annotations already capture the direct
  scramblase activity, membrane process, location, and antiviral outcome.

## Isoforms and open questions

UniProt records Q13530-1 and Q13530-2; isoform 2 lacks residues 1-55. No source
reviewed here tests their relative surface localization, scramblase activity, or
antiviral potency.

1. Test isoform-resolved membrane topology, lipid flipping, and virion
   incorporation.
2. Identify the physiological non-viral consequences of constitutive SERINC3
   lipid scrambling in human cells.
3. Validate the predicted credit-card lipid pathway with separation-of-function
   mutants that retain surface expression.
