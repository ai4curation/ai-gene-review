# BDH1 (YAL060W, UniProt P39714) notes

## Activity
- NAD-dependent (R,R)-butanediol dehydrogenase [PMID:10938079 "The YAL060W gene product can therefore be classified as an NAD-dependent (2R,3R)-2,3-butanediol dehydrogenase (BDH)."]; no acetoin -> diacetyl oxidation [PMID:10938079 "It was unable, however, to further oxidize these acetoins to diacetyl."]
- Zn MDR family; 2 Zn by similarity [UniProt:P39714]
- Diacetyl -> (R)-acetoin reduction reported in a UAB thesis from the same group (web search; not cached) - basis for keeping RCA GO:0019152 as non-core.

## Processes
- Butanediol formation in fermentation [PMID:19966022 "Deletion of BDH1 resulted in an accumulation of acetoin and a diminution of 2,3-butanediol in two S. cerevisiae strains under two different growth conditions."]
- Butanediol utilization [PMID:10938079 "S. cerevisiae could grow on 2,3-butanediol as the sole carbon and energy source."]
- Paralog BDH2 inactive on butanediol (PMID:19966022 abstract).

## Curation observations
- RCA acetoin biosynthetic process marked over-annotated: in vivo Bdh1p consumes acetoin.


## 2026-10-25 alcoholic-fermentation audit

Native NAD(H)-specific Bdh1 converts R-acetoin to R,R-butanediol and S-acetoin to meso-butanediol. PMID19966022 full text separates this R-selectivity from NADPH-dependent Ara1 S-selectivity and native residual pathways. PMID26729717 full text inspected externally at https://pmc.ncbi.nlm.nih.gov/articles/PMC4784035/: Table 2 directly measures purified Bdh1 diacetyl reduction (Km 60 mM; kcat 1735 s-1), less efficient than acetoin reduction (Km 3 mM; kcat 1625 s-1). Kinetics used 0.2 mM NADH, 25C, pH7. This corrects the earlier implication that failure to oxidize acetoin refutes diacetyl reduction. GO:0019152 explicitly specifies the reverse reaction. PMID19329666 full text inspected externally at https://pmc.ncbi.nlm.nih.gov/articles/PMC2681661/: V5 bdh1 deletion doubled diacetyl, and native NADH Bdh1 was contrasted with engineered NADPH-specific 221EIA223-to-SRS protein. Do not transfer mutant coenzyme specificity to wild type. Both new local caches remain abstract-only after supported fetch XML/HTML failures; the 2016 retry also failed to cache full text. Detailed external findings are paraphrased, not falsely quoted from the abstract cache.

Workflow: fetched current gene data using `just fetch-gene`; existing original row fields were preserved (verified against the pre-edit JSON snapshot). All 24 rows were reassessed by term and source, including non-fermentation activities/localizations. Annotation-reviewer and core-function synthesis instructions were applied. `just deep-research-falcon yeast BDH1 --fallback perplexity-lite` ran concurrently with `just fetch-gene-pmids`: Falcon/Edison failed HTTP403 authentication; Perplexity failed HTTP401 insufficient_quota. No generated provider report was fabricated. Publication caching completed successfully. FEBA fitness is a prokaryote-only review requirement and does not apply to yeast.

Family membership from the fetched record (official names independently checked in `interpro/panther/panther.obo`):

```text
DR   PANTHER; PTHR43161:SF23; (R,R)-BUTANEDIOL DEHYDROGENASE-RELATED; 1.
DR   PANTHER; PTHR43161; SORBITOL DEHYDROGENASE; 1.
```

GO-CAM index lookup by the UniProt accession returned no entries in the current index; existing RCA/YeastPathways assertions were assessed from their explicit terms and underlying chemistry. No new process rows were manufactured.

Audit decisions by original term (duplicate evidence rows remain intact):

- GO:0000721 (R,R)-butanediol dehydrogenase activity: ACCEPT.
- GO:0005737 cytoplasm: MODIFY.
- GO:0005829 cytosol: ACCEPT.
- GO:0008270 zinc ion binding: ACCEPT.
- GO:0016491 oxidoreductase activity: TOO_GENERAL.
- GO:0019152 acetoin dehydrogenase (NAD+) activity: KEEP_AS_NON_CORE.
- GO:0034078 butanediol catabolic process: ACCEPT.
- GO:0034079 butanediol biosynthetic process: ACCEPT.
- GO:0045151 acetoin biosynthetic process: KEEP_AS_NON_CORE.
- GO:1902652 secondary alcohol metabolic process: TOO_GENERAL.
