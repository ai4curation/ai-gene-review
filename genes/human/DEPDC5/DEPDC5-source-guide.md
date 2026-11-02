# DEPDC5 source guide

This guide distinguishes machine caches, separately recovered originals, literal database records and manual judgments. All normal caches retain their original bytes and access flags. A source marked abstract-only can have separately recovered original passages; the cache flag is not a statement that those passages were unavailable.

## Original evidence and access

| Source | Actual passage read | Access and limitation |
| --- | --- | --- |
| [23723238](https://pmc.ncbi.nlm.nih.gov/articles/PMC3728654/) | Original Results and Figures 3/4: GATOR complexes, human DEPDC5 localization and perturbation, complex GAP assay | Independently reviewed by the core consultant; separate Methods/SI and figure pixels not inspected. |
| [29590090](https://pubmed.ncbi.nlm.nih.gov/29590090/) | Original Results and selected figure/extended-data captions: DEPDC5 interfaces, isolated-subunit GAP comparison, assembly-mutant rescue | Independently reviewed by the core consultant; engineered truncations are not natural products. |
| [35338845](https://pubmed.ncbi.nlm.nih.gov/35338845/) | Full cached original selected Methods/Results: human complexes, NPRL2 catalytic finger, auxiliary RagC interface, single/multiple-turnover assays | Independently reviewed by the core consultant; membrane-switch arrangement remains a model. |
| [28199306](https://pubmed.ncbi.nlm.nih.gov/28199306/) | Original Results, Methods and controls for KICSTOR–GATOR1 association and lysosomal recruitment | Some imaging uses NPRL2 as the GATOR1 marker; do not call every image direct DEPDC5 localization. |
| [25457612](https://pubmed.ncbi.nlm.nih.gov/25457612/) | Original Results, Figures 3/5 and Methods: DEPDC5 knockdown weakens Sestrin-dependent mTORC1 inhibition | Human and mouse experiments distinguished; no direct Sestrin–DEPDC5 interaction inferred. |
| [25263562](https://pmc.ncbi.nlm.nih.gov/articles/PMC4223866/) | Main Results and Methods: Sestrin/GATOR2 co-IP, GATOR1 constructs and epistasis | Full original recovered; FLAG-DEPDC5 does not co-IP endogenous Sestrin2 in the reported experiment. |
| [17897319](https://doi.org/10.1111/j.1600-0854.2007.00643.x) | Publisher-indexed original Methods and **main Table 1** DEPDC5 row | Normal cache is abstract-only. Native human placental membranes; 20 peptides, 18.4% coverage, enrichment ratio 4.13. Historical IPI00005665/1572-residue designation is not unique-product peptide proof. |
| [23542697](https://doi.org/10.1038/ng.2599) | Original Results and online Methods: mouse neuronal and human neural-culture staining | Genuine public original PDF recovered; D19 peptide-blocking and no-primary controls. Authors describe localization as preliminary. Supplement downloaded but no claim to full supplementary reading. |
| [32296183](https://pmc.ncbi.nlm.nih.gov/articles/PMC7169983/) | Main Results paragraph introducing the nine-screen reference map; exact IntAct pair rows | Main original reports quadruplicate retesting and sequence confirmation. No supplementary Methods or pair-specific MAPPIT/GPCA validation claimed. |
| [22206000](https://doi.org/10.1371/journal.pone.0029099) | Original Methods and Results/Figures 3/4: MEOX2 promoter EMSA, mutant controls and reporter assays | Partner-class evidence; no DEPDC5 experiment. One-residue clone difference is kept explicit. |
| [29769719](https://pubmed.ncbi.nlm.nih.gov/29769719/) | Public original Extended Data Figures 2, 4 and 6, with related legends | Main body unavailable. A separately encountered two-page Chinese news/abstract document was identified and excluded as original assay evidence. |
| [39780017](https://www.nature.com/articles/s41586-024-07974-0/figures/1) | Complete public original Figure 1 legend | Published 8 January 2025; main body unavailable. Challenge to antibody specificity and degradation, not a retraction. |
| [39780003](https://www.nature.com/articles/s41586-024-07975-z/figures/1) | Complete public original Figure 1 legend | Published 8 January 2025; main body unavailable. Reply disputes tag/band/protocol interpretation. |
| [25046117](https://pmc.ncbi.nlm.nih.gov/articles/PMC4206535/) | Results/Figure 1 iml1-deletion autophagy assay | Budding-yeast donor evidence; no direct human assay inferred. |
| [33534698](https://pmc.ncbi.nlm.nih.gov/articles/PMC7857730/) | Results, Figure 4 and Methods for Pgk1-GFP processing/TORC1 response | Fission-yeast donor evidence; nitrogen-starvation and leucine/Gcn2 mechanisms distinguished. |
| [21900499](https://pmc.ncbi.nlm.nih.gov/articles/PMC3204073/) | Results/Figures 4/8: Iml1 complex co-IP and engineered domain deletions | Donor complex evidence; no natural human product inference. |
| [29199950](https://pmc.ncbi.nlm.nih.gov/articles/PMC5752196/) | Results/Figures 4/5: purification, mass spectrometry, pairwise co-IP and genetic interactions | Donor process/complex evidence; historical catalytic interpretation not substituted for human structures. |
| [23716719](https://pubmed.ncbi.nlm.nih.gov/23716719/) | Complete cached abstract and current donor GOA | Original assay details unavailable; this source alone does not establish human subunit catalysis. |

## Literal interaction records

All target records identify O75140-2, a 559-residue human product. Each partner has an array record (MI:0397), a pooling record (MI:1112) and the validated record below (MI:1356), with `negative=false`. Target and partner sequence/taxon ROGIDs were independently recomputed and matched. Array/pooling records identify the yeast expression host and Gal4 tags; host organism is not construct species. Repeated stages are not independent physiological studies.

| Source row (zero-based) | Exact partner | Validated IntAct / IMEx record | Decision |
| --- | --- | --- | --- |
| 1 | O75604 | EBI-24681385 / IM-25472-148768 | MODIFY |
| 2 | P49368 | EBI-24741275 / IM-25472-154060 | MODIFY |
| 3 | Q13257 | EBI-24703582 / IM-25472-150732 | KEEP_AS_NON_CORE |
| 4 | Q6FHY5 | EBI-24434236 / IM-25472-126818 | MODIFY |
| 5 | Q6W0C5 | EBI-24665620 / IM-25472-147375 | KEEP_AS_NON_CORE |
| 6 | Q96QG7 | EBI-24656502 / IM-25472-146569 | KEEP_AS_NON_CORE |
| 7 | Q9BSW7 | EBI-24642109 / IM-25472-145295 | KEEP_AS_NON_CORE |
| 8 | Q9UI95 | EBI-24775208 / IM-25472-157052 | KEEP_AS_NON_CORE |

The unreviewed Q6FHY5 partner is MEOX2, not an invented paralog assignment: its sequence matches reviewed MEOX2 except for one glutamine deletion outside the intact homeodomain. The refinement uses the established partner class without claiming identical activity of the clone. MTMR9 is an inactive phosphatase; MAD2L1/MAD2L2 roles in regulatory assemblies do not automatically satisfy a signaling-scaffold binding definition.

## Propagation and Reactome provenance

The actual PTHR13179 tree places PTN000323637 and PTN000995343 on the O75140 lineage. The five literal IBD terms are GO:0010508, GO:1904262 and GO:1990130 at PTN000323637; GO:0034198 and GO:0005765 at PTN000995343. Donors were reconciled to yeast P47170, fission-yeast O74788, fly Q9W0E3 and human O75140. Human self evidence is valid IBD grounding. Fly experimental GOA records were verified, but the separate 25512509/27672113 originals were not independently read. The mouse localization donor P61460 was checked against the actual 23542697 original.

The Reactome output component routes are explicit. Events 9639287, 9640237 and 9657619 lead through 9639281 → 9639274 → 9638242 → 9638222; event 9640254 leads through 9639274 → 9638242 → 9638222. Entity 9638222 identifies O75140, residues 1–1603, at GO:0005765. This supports location of DEPDC5-containing GATOR1, not amino-acid binding or event catalysis by DEPDC5.

IPR027244 maps the family to GTPase activator activity; the human subunit needs role-specific interpretation. IPR000591 maps the DEP domain to broad intracellular signaling; target-specific experiments justify the TORC1 refinement. Neither domain name transfers Wnt signaling or autonomous GAP chemistry to human DEPDC5.

## Products and policy

The official eight product identities and source sequence notes are preserved. VAR_SEQ reconstruction matched all-isoform FASTA, including the short HuRI product. Retention of the DEP-domain sequence does not establish equal function. Engineered truncations in structural studies are kept separate from natural products.

Positive binding without a supported finer term is retained as non-core under the standing [project curation instructions](https://github.com/ai4curation/ai-gene-review/blob/a87ae568676c4012ea4abe5393967aeff1b52ae7/projects/CLINGEN_MENDELIAN.md#curation-instructions). No NEW process or molecular-function row was added: the existing source assertions and explicit complex-contribution core cover the supported functions. The user’s process-redundancy rule is not interpreted as a blanket ban on new molecular functions.

## Core evidence and regulatory context

The YAML uses short literal cached anchors once each: PMID35338845 Results/Figure 4 for the NPRL2 catalytic residue and the following RagC subsection for DEPDC5 engagement; PMID23723238 Abstract for the starvation response; PMID28199306 Abstract for KICSTOR recruitment. The abstracts are concise anchors, while the separately read original passages in the table above provide the experimental context. Core GAP contribution is distinct from autonomous catalysis.

Original [PMID29590090](https://doi.org/10.1038/nature26158), Results on GATOR1 subunit interactions and Extended Data Figure 7, supports DEPDC5 association with SAMTOR/KICSTOR and identifies NPRL3-mediated GATOR2 association. It does not establish the methionine-direction statement in the UniProt SUBUNIT note. The dedicated [SAMTOR study](https://pmc.ncbi.nlm.nih.gov/articles/PMC5747364/), Figures 1, 3 and 4 and corresponding Results, directly shows stronger association after methionine starvation and weaker association after methionine or SAM restoration. These selected original passages were read; separate supplementary Methods and figure pixels were not inspected. This is regulation through the SAM sensor SAMTOR, not DEPDC5 metabolite sensing.

For AKT1/PIM1 regulation, the [PMID31548394 abstract](https://pubmed.ncbi.nlm.nih.gov/31548394/) and [UniProt PTM section](DEPDC5-uniprot.txt) support phosphorylation-mediated relief of DEPDC5 inhibition in the tested cancer-cell models. The full original was not independently read for this follow-up, and the result is not transferred to all alternative products.

## Curated pathway roles

Both [GO-CAM 646ff70100001312](https://amigo.geneontology.org/amigo/model/646ff70100001312) and [GO-CAM 646ff70100001561](https://amigo.geneontology.org/amigo/model/646ff70100001561) represent DEPDC5 small GTPase binding at the lysosomal membrane within TORC1 inhibition and an enclosing amino acid starvation response. The relevant activity identifiers are `646ff70100001542` and `646ff70100001735`. Model 646ff70100001561 additionally uses DEPDC5 as an input to a KLHL22-enabled activity. The distinction between an enabled activity and its input is preserved. These cached curated models corroborate role representation; they do not resolve the disputed degradation mechanism or supply independent experimental replication.
