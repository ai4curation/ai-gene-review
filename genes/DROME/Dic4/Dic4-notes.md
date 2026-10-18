# Dic4 evidence notes

## Identity and evidence

Current FlyBase lists Q9VVS1 as the 302-residue PA/PC product; the separate PB product is 173 residues. The prediction-time sequence is absent from the release, so the current exact accession is the evaluated product. [Dic4-flybase.txt](Dic4-flybase.txt) and [frozen UniProt JSON](Dic4-uniprot-source.json) preserve these records.

[PMID:21130726](https://pubmed.ncbi.nlm.nih.gov/21130726/), “No transport activity was observed for DmDic4p.” The abstract also directly reports mitochondrial localization for all expressed Dic proteins. Full assay details are unavailable in the cached abstract. Retain both NOT dicarboxylate annotations. The sulfate, thiosulfate and phosphate IBAs require reconciliation with the target-specific biochemical result; this is a conflict with experimental evidence, not an objection to the number of PAINT donors.

ThPP was not identified in the accessible abstract as a tested substrate. Therefore the negative carrier assay cannot by itself refute the ProtNLM ThPP claim. No specific molecular function is established sufficiently to populate core_functions. The original prediction is a function paragraph only, reviewed separately in the linked function-description review.

## Provider research assessment

The completed Falcon synthesis was inspected and its key carrier review was fetched as PMID:32842667. The full review describes failed homo- and hetero-exchange assays and possible changes at substrate-contact points CP1/CP2. Its summary table lists subfamily substrates that the prose does not establish for Dic4. These observations strengthen the specific substrate caveat. The primary PMID:21130726 abstract directly reports mitochondrial localization, which is more specific evidence than the provider report’s statement that direct localization was not found. No inspected source identifies a ThPP assay.

## 2026-09-20 full-gene IBA re-review

Restored broad membrane and transport assertions. Retained the two experimental NOT dicarboxylate rows and unresolved substrate-specific IBAs after critical incorporation of the existing OpenScientist report.

The existing OpenScientist report is reused critically, with exact limitation excerpts in the reviews. Its absence-of-positive-experiment argument is not adopted as loss evidence. General transport is retained as an ancestral carrier inference, without assigning a measured Dic4 substrate. Primary NOT annotations remain negated and accepted.

- PMID:21130726: Primary abstract directly reports mitochondrial localization and no detected DmDic4p transport. Exact substrate-panel conditions and insertion/folding competence remain unresolved.
- PMID:32842667: Full review discusses failed homo/hetero-exchange and substrate-contact substitutions without proving complete transport incapacity.
- file:DROME/Dic4/Dic4-hypotheses/fly41-thiamine-pyrophosphate-transport/openscientist.md: Read substantive report and explicit limitations. It acknowledges untested ThPP and unresolved assay conditions, contradicting its categorical refuted/carry-over framing. A characterized Tpc1 does not itself exclude shared capacity; identity-based UPGMA is not the PAINT ancestral placement.

PAINT: {'family': 'PTHR45618', 'nodes': ['PTN000756618', 'PTN002515516'], 'finding': 'Current specific anion-transport and general carrier assertions were inspected separately; negative tests of one panel do not remove every possible transport function.'}

All 12 rows were assessed, including experimental, electronic, negated and old proposed entries. Source annotation fields and row counts remain unchanged. Remaining questions are recorded in `projects/IBA_REVIEW/rereview-2026-09-20/receptor-and-lipid-claims.yaml`; coordinated reports will be assessed critically when available.
