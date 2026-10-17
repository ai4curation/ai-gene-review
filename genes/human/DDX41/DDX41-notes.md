# DDX41 review notes

## 2026-10-17 — source-based review

Human DDX41 is UniProt Q9UJV9 (HGNC:18674), with a 622-amino-acid canonical sequence. The official reviewed record declares no alternative product. The approximately 55-kDa species studied after start-loss mutation has unresolved candidate starts M132/M155. The engineered 127–622 construct in the later DNA study is not a separately identified natural isoform ([PMID:26712909](https://pubmed.ncbi.nlm.nih.gov/26712909/), [PMID:35613581](https://pubmed.ncbi.nlm.nih.gov/35613581/)).

All 48 imported annotations were reviewed, retaining their terms, evidence codes, source identifiers, qualifiers and supporting entities. In particular, the spliceosomal-complex source retains its `colocalizes_with` qualifier. The resulting actions are 23 ACCEPT, 10 MODIFY, 9 KEEP_AS_NON_CORE and 6 UNDECIDED. No NEW annotation was added. Two core functions describe RNA binding during nuclear spliceosomal processing and DNA remodeling associated with cytosolic cGAS/STING signaling.

### RNA processing and substrate specificity

Native human C-complex proteomics explicitly identifies Abstrakt/Q9UJV9 in Table 1. The original Methods assemble complexes in HeLa nuclear extract on a substrate arrested after the first catalytic step, supporting the existing catalytic-step-2 spliceosome annotation and its curator inference to splicing ([PMID:11991638](https://pubmed.ncbi.nlm.nih.gov/11991638/)). Later human perturbation, protein-association and RNA CLIP experiments support DDX41 participation in spliceosomal RNA processing. They do not establish that DDX41 performs the splice-site transesterification chemistry ([PMID:25920683](https://pubmed.ncbi.nlm.nih.gov/25920683/), [PMID:36229594](https://pubmed.ncbi.nlm.nih.gov/36229594/)).

The direct biochemical study tests 3-prime- and 5-prime-tailed 13-bp RNA duplexes negatively, with DDX43 as a positive control, while demonstrating ATP-dependent DNA unwinding and ATP-independent DNA strand annealing. Its RNA-helicase IDA row is therefore refined to the observed DNA-helicase activity. The result concerns the tested substrates and conditions; it is not proof that DDX41 cannot remodel RNA in another assembly ([PMID:35613581](https://pubmed.ncbi.nlm.nih.gov/35613581/)).

The actual PAINT lineage contains the RNA-helicase IBD node PTN002774595 and the deeper mRNA-binding node PTN002776867. Independent experimental donor records ground those placements. Q9UJV9 appearing among descendants is legitimate and is not labeled circular. RNA-helicase IBA and electronic rows remain UNDECIDED because target substrate requirements are unresolved. The mature-mRNA-binding IBA is retained as non-core; GO:0003729 excludes introns, so splice-site CLIP alone is not presented as its direct experimental proof. The nuclear core uses GO:0003723 RNA binding.

### Protein associations and molecular-function specificity

The positive interaction records were assessed by exact target, partner, publication, experimental stage and construct features. Three NKAP rows are refined to transcription corepressor binding, the SIAH1 row to ubiquitin protein ligase binding, and the ERCC6/CSB row to ATPase binding. These describe established partner classes, without assigning repression, ubiquitination or repair chemistry to DDX41. The CSB study detects DDX41 by anti-Myc coimmunoprecipitation but not reciprocal anti-FLAG recovery ([PMID:26030138](https://pubmed.ncbi.nlm.nih.gov/26030138/)).

The CEP70, NKAPL, AIDA, FAM50A and HTT associations remain non-core generic binding. Their positive observations are preserved; more informative catalytic or adaptor functions are not established. The HTT records use regions 1–511 and 1932–2642, and a canonical sequence checksum does not turn those fragments into full-length assay constructs ([PMID:32814053](https://pubmed.ncbi.nlm.nih.gov/32814053/)). Qualitative binding capacity does not demonstrate a native physiological complex or quantitative stoichiometry.

This treatment follows the user's [project-specific curation instruction](https://github.com/ai4curation/ai-gene-review/blob/a87ae568676c4012ea4abe5393967aeff1b52ae7/projects/CLINGEN_MENDELIAN.md#curation-instructions). Supported broad annotations with justified specific replacements use MODIFY, including where another row already represents the specific term. These refinements do not add new source assertions.

### Localization, signaling and access limits

HPA staining and exact Reactome entity paths support nucleoplasm and cytosol. Reactome's ubiquitination event treats DDX41 as the substrate of TRIM21, and exon ligation/remodeling events do not assign the other complex components' chemistry to DDX41. Conditional ER association is retained as non-core with mouse endogenous and tagged human-cell contexts distinguished ([PMID:21892174](https://pubmed.ncbi.nlm.nih.gov/21892174/)). DDX41 contributes to cGAS/STING signaling, while cGAS synthesizes cGAMP; the proposed intracellular balance between DNA unwinding and annealing remains a model.

Source-specific uncertainty remains for the second RNA-capture study, BTK-associated localization, the historical apoptosis source and NK-cell membrane proteomics. Original access was attempted, and title/abstract limitations were not converted into removal decisions. The first RNA-capture source has recovered original methods but an unrecovered separate protein table; its target assignment is transparently deferred to the GO curator and supported by independent DDX41 CLIP.

The normal Falcon research request and configured fallback both failed (authentication and quota errors); no provider report was created or fabricated. Manual original-source assessment continued. Original machine caches and their access flags were preserved, including cases with separately recovered originals. The [source and assay guide](DDX41-source-guide.md) records those distinctions and stable locators.


## 2026-10-17: evidence quotations and consistent retained claims

The RNA-binding capture annotation from PMID:22681889 and cytoplasm annotation from PMID:25704810 are now accepted with independent target evidence and curator deference. Their original target-level assays remain unavailable, and the reference reviews preserve that limitation. The revised totals are 25 ACCEPT, 10 MODIFY, 9 KEEP_AS_NON_CORE and 4 UNDECIDED across the same 48 imported source rows.

Six short exact cached quotations support the decisive DNA-versus-RNA substrate result, ATP hydrolysis, cytosolic accumulation, splicing perturbation and direct RNA association ([PMID:35613581](https://pubmed.ncbi.nlm.nih.gov/35613581/), [PMID:25920683](https://pubmed.ncbi.nlm.nih.gov/25920683/), [PMID:36229594](https://pubmed.ncbi.nlm.nih.gov/36229594/)). Biological findings are recorded separately from access assessments. The unnecessary concentration detail was removed from the RNA-unwinding rationale; the positive/negative substrate conclusion is unchanged.

The [source guide](DDX41-source-guide.md) now quotes and links the curated human NKAP corepressor record. The retained GO:0001222 refinements identify the bound partner class; they do not assign a transcription-repression mechanism to DDX41. The two functional cores remain RNA-associated spliceosomal processing and DNA remodeling linked to cGAS/STING signaling. The spliceosomal core uses an encompassing complex term because the cited studies cover more than one spliceosomal stage. No NEW annotation, natural alternative product or existing source-field change is introduced.
