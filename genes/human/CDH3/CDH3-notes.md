# CDH3 review notes

## 2026-10-10 — primary-source review

P-cadherin is a type I classical cadherin with an adhesive ectodomain and intracellular catenin association. The two molecular cores are cadherin binding involved in cell-cell adhesion (GO:0098641) and beta-catenin binding (GO:0008013), operating at plasma membrane/adherens junctions. All 35 original assertions and both UniProt product records are preserved. The broad cadherin-binding IBA is refined through its review object, without adding a redundant NEW annotation.

The [standing ClinGen instruction](https://github.com/ai4curation/ai-gene-review/blob/f7dc8b60bf8be80744f75955c3c1a3c16bd73888/projects/CLINGEN_MENDELIAN.md#curation-instructions) governs generic binding. No GO:0005515 assertions occur in this intake. PAINT annotations retain their ancestral-node provenance; no donor-count argument, self-donor circularity argument or reconstructed tree placement is claimed.

### Direct adhesion and catenin evidence

[PMID:2793940](https://pubmed.ncbi.nlm.nih.gov/2793940/) reports human P-cadherin cDNA expressed in mouse NIH3T3 hosts and functional cell adhesion. The human target and mouse host are distinct. The accessible cache is abstract-only even though it contains a repeated-abstract section headed Full Text. It also explicitly distinguishes low human placental expression from mouse placental expression, so the historical name does not imply the same placental role in humans.

[PMID:24559158](https://pubmed.ncbi.nlm.nih.gov/24559158/) provides independent human EC1–2 biophysical evidence for calcium-dependent, specific homophilic association. Its authentic abstract was read; complete construct/control details were not accessed. Together with the cell assay, this supports the specific adhesion MF. Calcium binding is a supporting property, retained as non-core.

Selected full [PMID:18320359](https://pmc.ncbi.nlm.nih.gov/articles/PMC2673888/) Methods, Results and Fig.3 legend were read externally. Beta-catenin IP from a native human breast-tumor sample followed by P-cadherin WB appears in Fig.3c; Fig.3g is the negative IP control. This supports catenin association, without a purified binary-interface or fixed-stoichiometry claim. Figure pixels and every supplement were not inspected. The authentic normal cache remains abstract-only. Its clinical correlations are not treated as CDH3 migration experiments.

[PMID:10460003](https://pubmed.ncbi.nlm.nih.gov/10460003/) was read at abstract depth, supporting human bronchial expression. The original curated membrane localization is consistent with independent human target evidence. Exact fixed-main bytes are reused unchanged.

Reactome [R-HSA-419001](https://reactome.org/content/detail/R-HSA-419001) and [R-HSA-419002](https://reactome.org/content/detail/R-HSA-419002) consume [Classic Cadherin R-HSA-418977](https://reactome.org/content/detail/R-HSA-418977), whose actual member list includes human CDH3 R-HSA-198241 at the plasma membrane. These are curated family events, not independent experiments. Both fixed-main caches are preserved. The orthology donor [P10287](https://www.uniprot.org/uniprotkb/P10287/entry) was verified as mouse Cdh3.

### Hair, pigment and retinal contexts

The full [PMID:23143461 clinical report](https://jamanetwork.com/journals/jamaophthalmology/fullarticle/1390043) describes two siblings with a homozygous deletion of exons 12–13, lifelong sparse hair and progressive macular dysfunction. The normal cache is title-only; the actual external full report and legends resolve the clinical findings. This supports non-core retinal maintenance. Its congenital hair phenotype does not measure cycling directly; the retained hair-cycle assertion is independently supported by the experimental 2012 study, without changing the original source.

For [PMID:22696062](https://pubmed.ncbi.nlm.nih.gov/22696062/), the [institutional PDF](https://dea.lib.unideb.hu/server/api/core/bitstreams/3016ebd4-c874-4cfc-8212-702d3467ecfb/content) is a compilation. The matching 2012 article, DOI 10.1038/jid.2012.171, occupies printed pages 63–72; the leading 2013 manuscript is a different paper. Selected full Results, Methods and legends establish CDH3-specific siRNA experiments in adult human follicles, reduced Ki67 proliferation, premature catagen, and growth-factor/Wnt-associated changes with lithium and TGF-beta neutralization experiments. The original upstream regulatory qualifiers are retained, including the IGF1-expression scope; there is no direct IGF-receptor assay or CDH3 kinase claim. Full ultrastructural text reports precortical keratin clumps, but the exact keratinization step remains UNDECIDED.

For [PMID:23334344](https://pubmed.ncbi.nlm.nih.gov/23334344/), selected full Results/Methods and legends of the [accepted manuscript](https://dea.lib.unideb.hu/server/api/core/bitstreams/953cc0dc-7630-4ea2-8e2a-668cc5cec25b/content) distinguish already mature anagen-VI follicles and isolated follicular melanocytes. The supported melanin-regulation outcome is non-core; tyrosinase performs the catalytic step. Lithium does not restore MITF transcript, precluding an exclusive Wnt mechanism. Acquisition of follicular maturity remains UNDECIDED because that developmental transition is not resolved by the adult pigment assays. Normal caches for both articles remain unchanged abstract records; actual external access is separately recorded.

The third UNDECIDED assertion is cytoplasm/is_active_in. GO:0005737 excludes plasma membrane. Sporadic cytoplasmic staining does not establish activity in that pool, and a membrane-facing tail is insufficient. The possible distinct inherited role is preserved pending clarification; positive junctional function is represented separately.

### Intake and validation provenance

The normal fetch completed successfully before review. Authentic fresh source variants were archived before selecting unchanged fixed-main caches. Two added primary references were fetched normally. Falcon exceeded its bounded timeout; its owned orphan process was terminated after the launcher exited. The explicit Perplexity-lite fallback returned an insufficient-quota error. No provider report was produced or manually impersonated; the primary-source reading above supplies the research evidence.

Primary-source quotations are sparse, with reference-only support elsewhere; the aggregate authoring limit is 25 words per source. This is an authoring constraint, not a repository validation rule. No novel biological-process annotation or scientific computational result is asserted.
