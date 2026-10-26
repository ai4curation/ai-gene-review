# Androgen receptor module: taxon, mechanism and source audit

## 2026-10-26 scope and literature synthesis

This is a manual augmentation of the existing module, with 15 audited gene exemplars. The earlier Falcon report remains an immutable discovery aid; no generated provider file or publication cache was edited. The existing Metazoa envelope and generic causal arrows did not resolve the receptor lineage, cellular steps or cofactor context. The revised abstract template covers full-length NR3C4-dependent **genomic** signaling in characterized jawed vertebrates (Gnathostomata, NCBITaxon:7776), supported by mammalian, ray-finned-fish and shark experiments. It does not infer AR from any steroid response in another metazoan.

Primary comparative phylogeny and cloned-receptor assays [PMID:19819965] establish the jawed-vertebrate lineage and teleost duplication. The structural review [PMID:39208923] organizes ligand sensing, response-element recognition, domain cooperation and receptor assembly; the coregulator review [PMID:32449767] provides context for overlapping but nonidentical cofactors. These reviews guide synthesis; the mechanistic claims below are assigned to primary experiments.

The model ends at transcriptional response. Steroid synthesis and transport, HSP70/HOP and import/export machinery, other chromatin factors, non-NR3C4 androgen sensors, LBD-deficient splice products and disease-specific variants are outside the named-member panel. They are not asserted absent. A recent primary study [PMID:39227594] distinguishes low-androgen monomer-dependent non-genomic activity from dimer/oligomer-associated transcription in prostate cancer cells. That result prevents a claim that *all* AR signaling requires the complete genomic sequence; it is not silently grafted onto normal fish physiology.

## Receptor identity and comparative limits

The unique receptor exemplars are human AR P10275, mouse Ar P19091, medaka ara D1MV72 and arb D1MV73, brownbanded bamboo shark AR D0VX34, and zebrafish ar A4GT83. The gene notes and normal source caches establish the medaka sequence mapping (ara AB252233/chromosome 10, arb AB252679/chromosome 14) and shark clone AB213019. No accession was guessed from a similar symbol.

- Human cloned receptor ligand binding is grounded in [PMID:3353726]. Human AR DBD structures and BLI assays establish cooperative, head-to-head binding to natural AREs [PMID:38604378]; isolated DBD structures do not determine the stoichiometry of every full-length nuclear complex.
- Mouse Sertoli-cell Aard ChIP/EMSA/reporter data directly connect DNA binding with transcription [PMID:27959439]. A second-zinc-finger disruption preserves nuclear AR but impairs genomic function [PMID:19574395], so localization is not equated with productive transcription.
- Shark assays establish androgen-responsive reporter function and ligand-dependent localization in heterologous cells [PMID:19819965]. The absence of the mammalian-like N/C motif does not make the receptor nonfunctional. Many teleost experiments in that paper concern mosquitofish, not medaka.
- Medaka reporter/localization data [PMID:26507457] and native knockout/localization data [PMID:36918573] are separated. Ara can be cytoplasmic in native anal fin despite constitutive nuclear behavior in particular transfected assays. Double knockouts retain functional sperm under the tested conditions; this limits a universal *necessity* claim but does not prove no modulatory role in spermatogenesis.
- Zebrafish receptor binding/transactivation supports testosterone and 11-ketotestosterone responses [PMID:18469035]. The independently inspected primary table establishes weak high-concentration cortisol activation, but this does not establish physiological glucocorticoid signaling or transfer to medaka.

## Cofactor logic and source attribution

HSP90AA1 P07900 supplies a verified cytosolic ATP-dependent chaperone exemplar. General HSP90-complex experiments do not prove HSP90AA1-exclusive AR dependence. The HSP90 family selector therefore requires a cytosolic NR3C4-client role and does not assign every organellar/family member to AR signaling.

FKBP4/FKBP52 and FKBP5/FKBP51 are separate optional implementation choices, not sequential obligatory exchange factors. The human exemplars are Q02790 and Q13451; mouse counterparts are P30416 and Q64378. Human prostate cancer assays show both can support AR dimerization and chromatin binding while nuclear entry remains intact [PMID:34057812]. FKBP51 can recruit p23 to ATP-bound HSP90 and increase androgen-binding competent AR [PMID:20048054]. Mouse knockout evidence distinguishes a requirement for Fkbp4 in selected androgen-dependent reproductive traits from the lack of those defects after Fkbp5 loss, while retaining AR binding/import [PMID:17142810]. GR import/exchange and GR structural studies are not direct proof of the same AR mechanism.

Human PTGES3/p23 Q15185 is an optional contextual branch with **direct AR evidence**, not solely a GR analogy. It increases ligand-binding capacity and promoter occupancy, including effects of an HSP90-binding-defective p23 mutant [PMID:22899854]. The 2025 study directly reports PTGES3–AR binding, stability and nuclear target-gene effects [PMID:41193657]. General ATP-bound HSP90 interaction [PMID:10543959] is distinguished from the partly HSP90-independent AR role. The recent paper's normal cache is abstract-only after PMC rate limiting; no uninspected detailed molecular mechanism was added. Prostaglandin synthesis and passive holdase activity remain in the gene review, outside this pathway role.

NCOA1 Q15788 and NCOA2 Q15596 are alternative or coexisting coactivators, not mandatory consecutive steps. SRC1 AR-AF1 recruitment and preserved potentiation after LXXLL disruption [PMID:10567563] prohibit an AF2-only recruitment assertion. Full-length versus isolated-domain context matters [PMID:10454556]. AR-LBD recognition of selected LXXLL/FXXLF motifs remains valid complementary evidence [PMID:15563469]; it does not resolve every original NCOA2 construct. Direct TIF2/AR AF2 experiments show promoter dependence [PMID:9717843], and TIF2 depletion reduces AR-induced genes in prostate cancer cells [PMID:17079484]. These newer module sources were sent to the NCOA2 reviewer for gene-level augmentation.

NCOR1 O75376 supplies contextual repression. Antagonist-bound AR recruits NCOR1/SIRT1 at target promoters [PMID:17505061], and FBI-1 can enhance NCOR1/SMRT recruitment at PSA sequences [PMID:20812024]. General NCOR1 scaffolding/HDAC3 activation [PMID:11931768] is not deacetylase catalysis by NCOR1. None of these observations makes NCOR1 a universal component of every liganded receptor complex.

The graph uses functional-contribution connections with explicit evidence and context. These are not sufficient Boolean switches or a fixed temporal schedule: cofactor association can precede DNA occupancy, and import and oligomerization are separable. The signed POSITIVELY_REGULATES and NEGATIVELY_REGULATES edges retain the demonstrated direction of cofactor effects in their stated contexts. These biological assertions do not establish an all-or-none quantitative gate or a universal effect outside those contexts. Co-chaperone and coregulator variants use ZERO_OR_MORE selection. Native requirement in a specific organism is not erased by optionality in a cross-species template.

## Verified family and PAINT handling

- All six receptor records carry the broad PTHR48092 assignment, whose official name is KNIRPS-RELATED PROTEIN-RELATED. It is not an exact NR3C4 descriptor. The module omits an AR family ID and retains free NR3C4 intent, exact members and primary comparative evidence. No substitute ID or mandatory InterPro signature was guessed.
- HSP90 uses verified PTHR11528 with its official label and an AR-client/cytosolic functional restriction.
- PANTHER19.0 classifications independently place human and mouse FKBP4 in PTHR10516:SF25 and FKBP5 in PTHR10516:SF26. Current UniProt puts all four in PTHR46512:SF9. The module follows the release subfamilies to preserve paralog identity and documents both sources. This is a deliberate source-supported choice, not mechanical ID repair.
- The old PAINT nodes PTN000163527/PTN000163629 for HSP90 and PTN002471265 for FKBPs are retained only for their general molecular claims. Human targets among experimental descendants are legitimate evidence; donor count and self-inclusion are not circularity. No new ancestral AR-regulation claim is inferred.
- NCOA1 PTHR10684:SF1, NCOA2 PTHR10684:SF2, NCOR1 PTHR13992:SF5 and p23 PTHR22932:SF3 are verified against target UniProt and official PANTHER names. Each role remains functionally and contextually constrained.

## Validation and provenance

The PANTHER release-plus-UniProt member index was built through `just ensure-panther-members`; the ignored index is not cited as a source or committed. Focused ModuleReview schema, ontology-label, reference-title, family/member and connection validation are logged under `.cache/androgen-panel/module-*.log`. A recursive coverage check confirms exactly 15 unique audited UniProt exemplars. The module history is scaffolded with `just new-history` and validated with the normal helper. No source caches or imported gene-annotation payloads were edited as part of the module rewrite.


## Independent integration QA

Root inspected the complete receptor/cofactor topology, 15-member panel, source scopes and 12 connections. Cofactor edges now encode their measured regulatory signs rather than using a generic input relation: the selected positive co-chaperone/coactivator effects and contextual NCOR1 repression remain machine-readable. Context conditions and evidence qualifiers are retained; no universal quantitative gate is inferred.
