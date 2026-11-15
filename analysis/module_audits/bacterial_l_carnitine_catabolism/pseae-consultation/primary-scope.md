# PAO1 carnitine enzymes and Cbc transporter: source scope

Reviewed 2026-11-07. Original UniProt, GOA, PAINT and publication caches are preserved. Official PAO1 identity captures are in pao1-transporter-records.json with exact URL/hash in transporter-query.json.

## CbcWV and CaiX (PMID19919675)

The full cached primary paper identifies PA5377/Q9HTI7 as CbcW and PA5376/Q9HTI8 as CbcV by the PA5378–PA5376 locus, component architecture and PAO1 cloning source. The official records independently match these locus/accession pairs. PA5378/Q9HTI6 is CbcX. The PAO1 core is assayed by heterologous expression and complementation; native insertion mutants are PA14. The paper's Table 5 CaiX reconstitution uses a P. syringae B728a substrate-binding protein with the PAO1 core in E. coli MKH13, so it is not a purified or fully native PAO1 CaiX–CbcWV assay. PA14 CaiX mutant and complementation evidence supports the P. aeruginosa recognition role. Uptake affinity is not a purified-protein ligand-binding dissociation constant.

The publication states: "The plasmids pCbcB728a, pCbcDC3000 and pCbcPAO1 were constructed by introducing the cbc loci from B728a, DC3000 and PAO1, respectively". It also distinguishes the core from substrate-binding proteins: "a transmembrane protein (CbcW) and an ATPase (CbcV)". These exact excerpts are in the protected full cache.

Choline, glycine betaine and carnitine are transported with appropriate binding proteins; CaiX does not give choline or glycine-betaine specificity. CbcWV supplies translocation/ATP coupling, not substrate chemical breakdown. Uptake-dependent growth is distinguished from direct catabolic chemistry. No target protein is assigned autonomous full ABC transport solely from its subunit membership.

## PMID21478341, publisher full text

Accessed the full ASM primary article at https://journals.asm.org/doi/10.1128/jb.00160-11 on 2026-11-07. The protected cache remains abstract-only. Table 1 and methods identify PA14 deletion backgrounds and a PAO1 cbcXWV complementation plasmid. Cbc-dependent substrate uptake supports growth under the tested conditions; the assay does not make Cbc proteins chemical degradative enzymes. Osmolarity changes transporter contributions, and retained osmoprotection in transporter mutants is not a universal negative for every stress-related role.

Exact Table 1 provenance excerpt: "pME6041 with cbcXWV from P. aeruginosa PAO1".

## PMID23763788, publisher full text

Accessed the full Wiley primary article at https://onlinelibrary.wiley.com/doi/full/10.1111/tpj.12262 on 2026-11-07. The protected cache remains abstract-only. Figure 5 and the accompanying text use B728a binding-protein mutants and pNCbcWV/pNCbcXWV inherited from the earlier study. The measured sulfur-containing cargo is choline-O-sulfate in a CosX-dependent transporter configuration. This supports transport of an organic sulfur compound, not inorganic sulfate. Broader substrate specificity therefore belongs to a compatible core/binding-protein combination, rather than an autonomous CbcV sulfate pump or an unrestricted specificity of CaiX.

Exact source excerpt: "CosX, which is a choline-O-sulfate (COS) SBP (Psyr_0028)".

## PMID24240508, primary supplementary evidence

The publisher landing page is accessible but the main article remains access restricted. Authentic Supplementary Text and Figures (MOESM244 PDF) and Data Sets 2/4 (MOESM246/248 XLSX) were downloaded from the article's own links; URLs/statuses/hashes are in the acquisition receipt. Dataset 2 maps Q9HTH7 to BKACE_529, P. aeruginosa PAO1, group G5. Supplementary Table 6 assays BKACE_503, BKACE_291 and BKACE_82; they are not Q9HTH7. The G5 substrate-promiscuity measurements must not be relabeled as assays of CdhC. Dataset 4 has no BKACE529 screen row. Curated UniProt ECO:0000269 statements remain the evidence for the exact CdhA/B/C target reactions; the accessible supplement neither overturns them nor independently exposes all of the curator's underlying target assay details.

## Access and ontology limits

PMID19406895 was subsequently read in full through the independently acquired PMC web output, preserved under the neighboring PSEPK consultation ignored cache (19406895-web-result.txt and 19406895-web-results-discussion.txt). Initial requests encountered access challenges; the successful source is https://pmc.ncbi.nlm.nih.gov/articles/PMC2857723/ (2026-11-07). Table 1 and Results include PAO1 transposon mutants in PA5388/PA5387/PA5386/PA5385, all defective for growth on carnitine. The targeted deletion/complementation series and carnitine-dependent NADH lysate assays primarily use PA14. The paper distinguishes PA5388 uptake from enzyme chemistry; it does not resolve the later CdhC/CdhB reaction assignments. Exact Results excerpt: "Deletion of PA5388 was sufficient to abrogate growth on carnitine, supporting a role for this ProX homologue in carnitine uptake." The earlier DhcAB/AtoB pathway proposal is historical, not a second experimentally completed route. PMID4302217 has no cached abstract and is used through curated UniProt specificity statements, not falsely described as newly read primary text.

Fresh official QuickGO definitions are in go-terms.json. Carnitine catabolism describes chemical breakdown. Amine terms name amino/substituted-amino compounds, while the QAC substrates here carry quaternary ammonium; the prior ontology analysis remains preserved. The historical NEW acyl-CoA hydrolase and acyltransferase rows duplicate the corresponding existing MODIFY replacements and can be retired without withdrawing either target activity.
