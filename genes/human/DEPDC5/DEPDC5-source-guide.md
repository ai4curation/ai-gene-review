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
| [17897319](https://doi.org/10.1111/j.1600-0854.2007.00643.x) | Publisher-indexed original Methods and Table 1 DEPDC5 row | Normal cache is abstract-only. Native human placental membranes; 20 peptides, 18.4% coverage, enrichment ratio 4.13. Historical IPI00005665/1572-residue designation is not unique-product peptide proof. |
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

## Fixed evidence digests

These SHA-256 values identify the inspected raw bodies or literal source reconstructions. Indexed entries are read locators, not claims that every line or figure was examined. The dated manual ledger separately records exact selected windows and attribution to the independent core consultation. No new publication quotation is used in the YAML.

| Evidence | SHA-256 |
| --- | --- |
| 24 oriented interaction records | `5ac82e26ff6cecff79d60a664b68eedc6702e99cbc74a558dec31fba3fed3d8d` |
| PAINT target lineage and IBD | `7f3a113fafbe1556e1dfb3e26a7b87de4af1323826bca2151ae64ace8c58c6e8` |
| Native lysosomal target-table indexed response | `a6174fe19e3b846e755828b09387d781fac9d10795f11ab5beaac3156f938d3b` |
| Neuronal localization original PDF | `471d3f05593f87f8a8028f0c9b4b1c4fa0dba18db1f71f5c5701a7b80bb520ce` |
| 2018 public publisher body/extended data | `d9448d2a9d0f9ccc16318c15beb00075572dc46888dc7cf77dcf1c5c98b81652` |
| 2025 challenge Figure1 | `5f927a96223599c6587d37b85db181bef1cb78e3eb5f9d9a04da44be69f9c864` |
| 2025 reply Figure1 | `219935deb83819397c641c0eaa99939338d5b34bc2b143d9c57dbf801156e7a3` |
| Manual owner read ledger | `50d412eb761d9ad24880ee9a4e58f511f24e8337a4e9423c06e32b9778811315` |
| Independent core synthesis | `64a2bf53621c5d851b28f9cf7d686926b1129a7c7b9ab50e188989eaa04bda73` |
