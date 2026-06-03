# AIPL1 notes

## 2026-06-03 Proteostasis PN review

- Deep research status: `just deep-research-falcon human AIPL1 --fallback perplexity-lite` was attempted. Falcon timed out after 600 seconds, then the Perplexity-lite fallback failed with a quota/401 error. No provider-generated deep-research file was created, so this review proceeds from cached GOA, UniProt, PN projection files, and cached primary literature.

- PN projection context: `projects/PROTEOSTASIS/reports/pn_projection/pn_projected_annotations.tsv` projects AIPL1 to `GO:0031072 heat shock protein binding` via the HSP70-HSP90 joint cochaperone class, and also shows `GO:0003755 peptidyl-prolyl cis-trans isomerase activity` as already in GOA through the FKBP-type PPIase branch. The review accepts the direction of the HSP90/co-chaperone projection but recommends the narrower, gene-supported `GO:0051879 Hsp90 protein binding` rather than the broad `GO:0031072`. The PPIase annotation is removed because AIPL1-specific evidence contradicts catalytic PPIase activity.

- AIPL1 is a photoreceptor/pineal protein with TPR motifs. The original gene paper describes "a new photoreceptor/pineal-expressed gene, AIPL1" and says its protein has "three tetratricopeptide (TPR) motifs" [PMID:10615133 "photoreceptor/pineal-expressed gene, AIPL1" / "three tetratricopeptide (TPR) motifs"].

- AIPL1 is present in human photoreceptors and interacts with NUB1, but this NUB1 binding is not the core PN proteostasis function. Akey et al. verified the interaction by co-immunoprecipitation and found AIPL1 in developing and adult photoreceptors [PMID:12374762 "The AIPL1-NUB1 interaction was verified by co-immunoprecipitation studies in Y79 retinoblastoma cells" / "AIPL1 is present in the developing photoreceptor layer of the human retina and within the photoreceptors of the adult retina"].

- Farnesyl/prenyl binding is a real AIPL1 function. Ramamurthy et al. showed that "AIPL1 interacts specifically with farnesylated proteins" and "AIPL1 enhances the processing of farnesylated proteins" [PMID:14555765]. Majumder et al. later mapped this to the FKBP-like domain, stating that "farnesylated-Cys binds exclusively to the FKBP domain of AIPL1" [PMID:23737531].

- The FKBP-like domain should not be curated as PPIase activity. Majumder et al. state that "the FKBP domain of AIPL1 does not bind FK506 or exhibit peptidylprolylisomerase activity" [PMID:23737531]. This directly argues against retaining the InterPro/PN PPIase transfer.

- The strongest PN-relevant function is AIPL1-HSP90 co-chaperone activity for PDE6 maturation. Yadav et al. report that AIPL1 "preferentially binds to HSP90 in the closed state with a stoichiometry of 1:2" and that "Disruption of the AIPL1 interaction with HSP90 impedes maturation of PDE6" [PMID:35065964]. Sacristan-Reviriego et al. also describe AIPL1 as a "photoreceptor-specific co-chaperone that interacts with the molecular chaperone HSP90" [PMID:28973376].

- High-throughput generic protein-binding rows should not drive core function. The TINF2 row comes from a telomere interactome screen over about 12,000 proteins [PMID:21044950 "we identified over 300 proteins that associated with the six core telomeric proteins"]. The HuRI rows come from a genome-scale binary interactome resource whose paper notes that "the cellular function of most individual PPIs remains to be elucidated" [PMID:32296183]. These are useful interaction-screen records but not evidence for a core AIPL1 PN role.
