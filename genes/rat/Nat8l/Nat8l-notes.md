# Nat8l review notes

## Evidence summary
- [PMID:18621030] The cached abstract/title support characterization of rat NAT8L as N-acetylaspartate synthetase.
- [UniProtKB:D3ZVU9] UniProt records the reaction L-aspartate + acetyl-CoA = N-acetyl-L-aspartate + CoA + H(+) with PubMed:18621030 evidence.

## Curation decisions
- Core function: N-acetylaspartate synthetase (L-aspartate N-acetyltransferase activity, GO:0017188).
- Specific catalytic activities were accepted; broad parent terms were modified to the specific activity where possible.
- Localization, cofactor/binding, and phenotype-level annotations were retained only as non-core unless directly tied to the enzymatic role.

## Re-review 2026-10-10

GOA refresh (commit a3cf70b6d): 2 new rows, no retired rows.

- GO:0008080 N-acetyltransferase activity, IBA from PANTHER:PTN000358947 (NAT8 family; donors include human NAT8 Q9UHE5 and NAT8B Q9UHF3): MODIFY to GO:0017188 L-aspartate N-acetyltransferase activity. The IBA node placement is not challenged; the term is correct but less specific than the known activity, matching the existing MODIFY on the InterPro IEA row for the same term.
- GO:0017188 L-aspartate N-acetyltransferase activity, ISO from human NAT8L (UniProtKB:Q8N9F0): donor-split of the mouse-donor ISO row; ACCEPT.

Action changes: none. Re-audit notes:
- GO:0051586 positive regulation of dopamine uptake involved in synaptic transmission (ISO, mouse): MARK_AS_OVER_ANNOTATED kept, but the rationale was corrected. The earlier text attributed the effect to altered NAA levels and stated the deep research does not mention dopamine; the refreshed UniProt entry states the mechanism is indirect via TNF [UniProtKB:D3ZVU9 "Promotes dopamine uptake by regulating TNF expression (By similarity)."].
- GO:0005759 mitochondrial matrix (ISO): KEEP_AS_NON_CORE kept; re-anchored to [PMID:18621030 "about 70% of the total Asp-NAT activity in the crude supernatant was present in the mitochondrial fraction"]; UniProt describes a single-pass mitochondrial membrane protein, so matrix vs membrane remains unresolved.

Quote hygiene: 10 UniProtKB quotes cited DR GO cross-reference lines that are gone from the refreshed entry; 11 more cited DR GO lines that still exist but merely restate the annotation. All 21 were replaced with verbatim CC text (FUNCTION, CATALYTIC ACTIVITY, SUBCELLULAR LOCATION).

Description rewritten to remove curation commentary and give standalone biology.

Open question: PMID:18621030 (Ariyannur et al. 2008) predates the molecular identification of NAT8L as Asp-NAT and measured enzyme activity in rat brain fractions; the IDA rows rely on the later gene assignment. Left as is (curator decision).
