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

## Deep research (falcon, added after initial review)
- `msl-3-deep-research-falcon.md` agrees MSL3 is a non-catalytic reader/adaptor bound to the MSL1 C terminus via its MRG domain that stimulates MOF on nucleosomes. It flags that the H3K36me3-spreading model is contested ["A direct methyl-mark-to-spreading model is now contested."] (2021 and 2024 H3K36R histone-replacement studies), and that the fly chromo-barrel binds H4K20me1/me2 peptides more strongly than H3K36me3 peptides (weak, mM affinities). The H3K36me3 reader term is kept (direct in vitro nucleosome binding) but the core-function description now carries this caveat. It also restates that H4K16ac antagonizes chromodomain binding, consistent with leaving the H4K16ac reader rows UNDECIDED.

## PR 4481 review fixes
- Softened the GO:0016456/GO:0072487 relationship claim; MSL complex used for in_complex.
- H4K20me1 and H4K20me1/me2 reader rows changed ACCEPT -> KEEP_AS_NON_CORE (weak mM in vitro affinities, physiological role not established), so they need not appear in core_functions.
- GO:1990841 REMOVE reason now names the plant donors (Arabidopsis MRG1/MRG2, reported to act with CONSTANS at the FT promoter).
- reference_review added: PMID:12683975 (Wolbachia review) relevance NONE, correctness MISCITED.
