# SUCLG2 (Q96I99) notes

## 2026-11-11 first review

Written as part of the evolutionary review of the succinyl-CoA synthetase families; see genes/yeast/LSC2/LSC2-bioinformatics/RESULTS.md.

- SUCLG2 is the GTP-specific beta subunit; with SUCLG1 it forms the GDP-forming enzyme, crystallised as the human heterodimer [PMID:32627745 "Human GTP-specific SCS (GTPSCS), an αβ-heterodimer, was produced in Escherichia coli"].
- Phylogeny: SUCLG2 is in the G-type clade (PAINT node PTN000929335) with pig, mouse, invertebrate, choanoflagellate and Dictyostelium subunits, all with Gln at position 20 of the mature subunit (Gln57 of the human precursor). SUCLA2 and the fungal beta subunits are in the other daughter clade of a duplication that predates animals [file:yeast/LSC2/LSC2-bioinformatics/RESULTS.md "Because Dictyostelium and the choanoflagellate Monosiga each have one gene in each clade, the duplication predates the divergence of animals, fungi and amoebozoa."].
- NOT GO:0004775 (ADP-forming) IBA accepted. Evidence is descent plus the key residue [PMID:16481318 "interactions of the guanine base with a glutamine residue (Gln-20beta) and with backbone atoms provide the specificity"] plus the pigeon enzyme [PMID:9765290 "Two succinyl-CoA synthetases, one highly specific for GTP/GDP and the other for ATP/ADP, have been purified to homogeneity from pigeon liver and breast muscle"]. No assay of the human enzyme with ADP was read; recorded as a suggested question.
- ATP binding (IEA from InterPro IPR013815, ATP-grasp subdomain) modified to GTP binding. The signature is named for the fold; in the G-type subunit the fold binds GTP [PMID:16481318 "GTP is bound in the ATP-grasp domain"]. This InterPro2GO mapping is wrong for the whole G-type clade and is a candidate for a curated rule conditioned on the subfamily or the Gln20 site.
- GO:0042709 succinate-CoA ligase complex IBA marked too general beside GO:0045244 (GDP-forming), the same treatment as LSC2, S. pombe SPCC1620.08 and now SUCLA2.
- Protein binding IPI rows removed under the policy. The HSC20 (HSCB) rows are a real screen hit of unknown significance [PMID:24606901 "we identified interacting partners of the cochaperone HSC20"].
- Reactome CLPXP rows (R-HSA-9838035, R-HSA-9838289): matrix location accepted; the cached summaries do not name SUCLG2, so client status was not checked.
- Direct localization not in GOA [PMID:25370487 "Specificity of SUCLG2 antiserum was supported by co-localization with mitotracker orange staining of paraformaldehyde-fixed human fibroblast cultures, delineating the mitochondrial network."].

### Affinage

Trust gates clear. Recorded with correctness DISPUTED: its grounding with transcription regulator activity and nucleus rests on one 2026 prostate cancer cell-line study (PMID:42252434, not cached), and "catalytic activity, acting on a protein" is wrong. Verified claims: beta-subunit identity, dependence on SUCLG1, mitochondrial network staining, and the mtDNA knockdown result [PMID:21295139 "knockdown of SUCLG2 by shRNA in both patient and control fibroblasts resulted in a significant decrease in mtDNA amount, decreased NDPK and cytochrome c oxidase activities, and a marked growth impairment"]. mtDNA maintenance was not proposed as a NEW process: it is a downstream consequence, and what the enzyme itself contributes is not known (recorded as a knowledge gap).

### Not done

No falcon or perplexity deep research (keys not available). PMID:37904651 is cached in full but was not read in detail.
