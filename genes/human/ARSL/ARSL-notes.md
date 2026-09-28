# ARSL evidence notes

## 2026-09-28: identity, sources and functional scope

ARSL (HGNC:719; UniProt P51690; human Gene415), formerly ARSE, encodes arylsulfatase L/E. The initialized review contains 12 GOA assertions. Its UniProt record reports no alternative-products section. The completed review preserves all original source identities, qualifiers and WITH/FROM lists.

The complete normal abstracts of PMID7720070, PMID9192838 and PMID9497243 were read and checked against official PubMed/PMC or publisher records. Full bodies of these historical papers were not accessed. PMID7720070 establishes CDPX mutations and sulfatase activity after COS-cell expression. PMID9497243 reports expressed human ARSE in Cos7 cells, glycosylation, Golgi localization and loss of activity for four of five tested patient substitutions. The fifth behaved like wild type. PMID9192838 explicitly discusses ARSE activity while describing ARSF discovery: its title is not evidence of a wrong-gene citation. [PMID:7720070](https://pubmed.ncbi.nlm.nih.gov/7720070/), [PMID:9192838](https://pubmed.ncbi.nlm.nih.gov/9192838/), [PMID:9497243](https://pubmed.ncbi.nlm.nih.gov/9497243/).

### Recent substrate evidence changes the older account

The older UniProt/source account identifies activity on artificial aryl sulfates without a physiological substrate. A current literature search found Maddaluno et al., *Arylsulfatase L is a Golgi chondroitin sulfatase regulating skeletal development* (2026; PMID42103217; DOI10.1016/j.jbc.2026.113111; PMC13254587). The review incorporates this paper; an unqualified present-day claim that the substrate is unknown would be outdated. [Primary article](https://pmc.ncbi.nlm.nih.gov/articles/PMC13254587/), [PubMed record](https://pubmed.ncbi.nlm.nih.gov/42103217/).

The complete abstract and indexed primary Results passages, figure1/figure3 captions, and relevant Methods passages were read. Human ARSL rescues the rat RCS knockout phenotype, whereas the human C86A catalytic mutant does not. The study associates ARSL with removal of the 4-O sulfate from chondroitin sulfate during Golgi proteoglycan maturation. The substrate experiment uses Golgi-enriched fractions and HPLC; it is not a purified-enzyme substrate-specificity assay. Proximity labeling identifies candidate neighboring proteins, not pairwise direct binding. Medaka Ol-Arsd results are in vivo model evidence, not an experiment in human cartilage. The full article, all image panels and supplements have not yet been read.

The Methods passages inspected specify rat chondrosarcoma cells; a selected CRISPR clone; sucrose-gradient Golgi enrichment; proteinase-K protection with/without detergent; a cell-lysate 4-methylumbelliferyl-sulfate assay; and HPLC analysis of media and Golgi preparations. Figure3 compares wild type, knockout, human wild-type rescue and catalytic-mutant rescue in conditioned medium, and wild type/knockout/human-rescue Golgi fractions with exogenous CS. These experiments support the catalytic model while leaving purified-enzyme kinetics, full substrate range and endo/exo specificity as separate questions. Golgi desulfation during biosynthesis does not automatically establish lysosomal chondroitin catabolism or a direct TGF-beta signaling activity.

### Localization and processing

The Human Protein Atlas assigns ARSL to the Golgi with Supported gene-level reliability. Its HPA060518 antibody has Supported ICC validation; Hep-G2 shows Golgi staining, whereas the displayed A-549 and U2OS entries have no staining. HPA070651 has no ICC result in the compared table. These are the site's text annotations; image pixels were not independently evaluated. [Subcellular data](https://www.proteinatlas.org/ENSG00000157399-ARSL/subcellular), [antibody validation](https://www.proteinatlas.org/ENSG00000157399-ARSL/summary/antibody).

The Reactome ER-lumen assertion was traced through the actual participant sets. Reaction R-HSA-1614362 has precursor ARS set R-HSA-1614312 as input and active ARS set R-HSA-1614309 as output. The ARSE members R-HSA-1614365 and R-HSA-1614351 both resolve to P51690/ARSL and carry ER-lumen locations. SUMF1 is the catalyst; ARSL is the sulfatase being matured. This supports a processing-stage location, not an ER-resident catalytic core or ARSL-mediated activation of other sulfatases. This paragraph records an author-derived graph inspection, not a new independent experiment. [Reaction](https://reactome.org/content/detail/R-HSA-1614362), [precursor member](https://reactome.org/content/detail/R-HSA-1614365), [modified member](https://reactome.org/content/detail/R-HSA-1614351).

The stable PANTHER/PAINT source assertion retains its own target P51690 in WITH/FROM: this is expected when target experimental evidence helped ground the ancestral inference. The ancestral placement and MSA were not independently replayed. No inferred family label or new ancestral claim is introduced.

### Exosome read boundary

The preserved canonical PMID19056867 cache is abstract-only, despite a repeated-abstract section headed Full Text. Its urinary-exosome LC-MS/MS experiment is relevant, but the ARSL/ARSE-specific supplementary identification row has not been inspected. A richer recovered copy remains quarantined; it does not replace the existing shared cache. The original HDA annotation should remain unresolved until its target-specific evidence can be examined, without treating an uninspected table as negative evidence. [Primary paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC2637050/).

### Research and curation boundaries

The required falcon and fallback perplexity-lite research attempt failed on network resolution and generated no report. Manual evidence notes remain here. The original source caches and provider outputs are not edited. The first normal fetch of PMID42103217 failed on network resolution. The normal fetcher subsequently recovered an XML full-text cache. Its title, PMID, DOI and PMCID match the primary article. Selected original Results, figure captions and Methods were read in that cache; availability of the full body does not mean every section, image or supplement was independently reviewed. The local GO-CAM index has no ARSL/ARSE/P51690 match. No NEW biological-process assertion has been made; any proposed extension requires its own performer, comparator and ontology-parent checks.

### Final annotation decisions

All 12 source assertions were reviewed: four ACCEPT, seven KEEP_AS_NON_CORE and one UNDECIDED. The catalytic core uses sulfuric ester hydrolase activity in the Golgi and a conservatively qualified chondroitin substrate account. Artificial aryl-sulfate hydrolysis remains supported assay chemistry, while ER localization describes maturation. The uninspected urinary-exosome target identification remains unresolved. No NEW annotation was added.
