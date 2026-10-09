# msl-3 (P50536) review notes

## Identity
- MRG-family; chromo-barrel + MRG domain. Cloned and shown on male X. [PMID:7768187 "We have found that MSL-3 is also associated with the male X chromosome."]

## Histone reading
- H3K36me3: [PMID:17936709 "recombinant MSL3 protein preferentially binds nucleosomes marked by H3K36me3 in vitro"]; chromodomain needed for spreading [PMID:19029895 "MSL3 chromodomain mutants retain binding to chromatin entry sites but show a clear disruption in the full pattern of MSL targeting in vivo"]
- H4K20me1/2: [PMID:20943666 "both the human and Drosophila MSL3 chromo-barrel domains bind preferentially to peptides representing the mono or dimethyl isoform of lysine 20 on the histone H4 N-terminal tail"]
- H4K16ac antagonizes binding: [PMID:20657587 "H4K16 acetylation antagonizes MSL3 binding"] -> GO:0140046 H4K16ac reader rows left UNDECIDED.

## Germline role (MSL-independent)
- [PMID:34878097 "Msl3, acting independently of the rest of the male-specific lethal complex, promotes transcription of genes, including a germline-enriched ribosomal protein S19 paralog RpS19b."]

## Curation decisions
- Generic histone reader -> H3K36me3 reader (MODIFY).
- Plant-seeded promoter-specific chromatin binding IBA REMOVE.
- Chromocenter (roX mutant mislocalization) MARK_AS_OVER_ANNOTATED.
- RNA binding (roX2 co-purification) -> lncRNA binding; lncRNA binding itself KEEP_AS_NON_CORE (MSL3 shows little roX preference [PMID:34943924 "MSL3 and MOF are reported to bind RNA but, unlike MLE and MSL2, show no great preference for roX transcripts"]).
- TAS citing a Wolbachia review (PMID:12683975) kept (term correct) but reference is a poor fit.
- Shared MSL conventions as in mof/mle/msl-1/msl-2.
