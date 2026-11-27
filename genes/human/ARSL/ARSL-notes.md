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


## PR3382 follow-up: specific glycan activity

The preceding final-decision paragraph records the initial submitted review. This follow-up replaces the broad sulfuric-ester core with GO:0003943 N-acetylgalactosamine-4-sulfatase activity and proposes one matching NEW MF assertion, supported by human ARSL rescue and the Golgi-fraction experiment in PMID42103217. The original 12 source annotations, qualifiers, WITH/FROM lists and actions remain unchanged; the 13-row review now contains four ACCEPT, seven KEEP_AS_NON_CORE, one UNDECIDED and one NEW. No new process assertion is made. The core location is the already-supported Golgi stack, and the distal skeletal-development process is retained in its original TAS annotation rather than attached to the immediate biochemical core.

# ARSL core-function term assessment, 2026-09-28

The full PR3382 review and comment were read. Its substantive request for a more precise core molecular function is accepted. Its assertion that GO:0003943 has a lysosomal-lumen clause is not supported by the current official AmiGO definition. The cited repository report line is an ARSB-specific core-function description, not a GO definition. The current definition describes removal of 4-sulfate from GalNAc units in chondroitin and dermatan sulfate without imposing a compartment. [GO:0003943](https://amigo.geneontology.org/amigo/term/GO:0003943).

GO:0003943 and arylsulfatase activity GO:0004065 are separate children of sulfuric ester hydrolase activity GO:0008484 in the inspected hierarchy. Thus the proposed specific glycan activity does not repeat an ancestor or descendant of an existing aryl-sulfatase assertion. The latter describes artificial phenol-sulfate chemistry. [GO:0008484](https://amigo.geneontology.org/amigo/term/GO:0008484).

The similarly named chondro-4-sulfatase activity GO:0033887 names cleavage of an unsaturated disaccharide with a 4-deoxy-glucuronosyl component. That defined substrate was not the demonstrated substrate in the ARSL fraction experiment, so the superficially attractive name is insufficient grounds to select it. [GO:0033887](https://amigo.geneontology.org/amigo/term/GO:0033887).

The selected primary Results and Fig.3 caption in the immutable PMID42103217 cache were reread. Human WT ARSL, but not C86A, corrected the CS/DS 4-O-sulfation phenotype in rat RCS cells. Golgi-enriched fractions from WT, knockout and human-rescue cells were incubated with exogenous CS and assayed by HPLC. These support a proposed GO:0003943 assignment with IMP and explicit human-construct/rat-cell and mixed-fraction limits. They are not a purified-enzyme substrate-range or endo/exo assay. No lysosomal localization is inferred. [PMID:42103217](https://pmc.ncbi.nlm.nih.gov/articles/PMC13254587/).

No new process assertion is proposed from this review. The optional biosynthetic-process suggestion needs a separate term-parent and same-role comparator assessment; a PAPS transporter alone does not settle the role of a desulfating enzyme. The original skeletal-development TAS row is retained. The core summary can state the precise molecular activity and Golgi location without promoting a distal developmental outcome as its immediate reaction-level process. A new ontology term is unnecessary when the existing chemical activity term fits the observed reaction.

Read boundaries: official AmiGO definitions/hierarchies and local report line were inspected; OLS MCP is not available in this session. The attempted QuickGO API page was inaccessible through the web tool. No source record or provider report was edited.


## Target-specific urinary-exosome evidence before publication

The study-authored NIH/NHLBI Urinary Exosome Protein Database lists arylsulfatase E precursor (ARSE; current symbol ARSL), RefSeq NP_000038, with one displayed peptide and reference 2, which links to PMID19056867. The database introduction identifies healthy human urinary-exosome preparations and LC-MS/MS protein identification. The exact target row, column labels and study-reference link were independently read at https://esbl.nhlbi.nih.gov/UrinaryExosomes/ on 2026-09-28. This resolves the target-identification gap recorded earlier in this journal and supports retaining the existing extracellular-exosome HDA annotation as non-core. It does not establish a catalytic function in exosomes, vesicle topology, peptide uniqueness, a modern isoform assignment or contamination. The canonical PMID19056867 record remains abstract-only and unchanged; this separate web-table reading is not represented as cached full text.

The final 13-row review now has four ACCEPT, eight KEEP_AS_NON_CORE and one NEW. Only the existing exosome action changes from the earlier follow-up draft. The specific glycan-activity proposal and Golgi-stack core are unchanged. Earlier count paragraphs record historical states.
