# FGF3 evidence and access guide

The review retains all 99 imported source contexts. The 72 Reactome rows all assert extracellular location; they do not make 72 independent claims about FGF3 catalysis. Evidence below distinguishes the human gene, the species of an assayed protein, and the responding cell. No publication quotations were added.

## Primary sources

| Source | Operative locator and actual scope | Limit |
|---|---|---|
| [PMID:8663044](https://pubmed.ncbi.nlm.nih.gov/8663044/) | Original JBC 271:15292–15297, Methods p. 15293, Tables II–III and Figures 2–5. Mouse FGF3, mouse FGFR1b and human FGFR2b; receptor-transfected BaF3 DNA-synthesis responses. | Ortholog corroboration of the conserved human ligand function, not purified human FGF3 binding kinetics. |
| [PMID:20702560](https://pubmed.ncbi.nlm.nih.gov/20702560/) | Development 137:2989–3000, Methods and Figure 3/text. Exogenous FGF3 inhibits chick anterior-heart-field explant differentiation and beating; ERK pathway evidence is consistent. | FGF3 reagent species is unstated in the read Methods. The in vivo bead experiments use FGF8. |
| [PMID:16263090](https://pubmed.ncbi.nlm.nih.gov/16263090/) | Original abstract plus publisher Results preview, “Identification of ribosomal protein S2 as a FGF3 binding protein.” Mouse FGF3 bait and human B-cell library are explicit. | Complete Methods/remaining experiments unavailable. Human RPS2 does not establish a human FGF3 assay. Binding does not establish ribosome biogenesis. |
| [PMID:2470007](https://pubmed.ncbi.nlm.nih.gov/2470007/) | Original abstract: human sequence organization, predicted 239-aa protein and Tera-2 expression. | Full article unavailable. Five source-specific TAS contexts remain UNDECIDED; this does not negate independently supported ligand biology. |
| [PMID:17236138](https://pubmed.ncbi.nlm.nih.gov/17236138/) and [PMID:18435799](https://pubmed.ncbi.nlm.nih.gov/18435799/) | Original abstracts: recessive human FGF3 variants, inner-ear agenesis, microtia and microdontia. | Clinical developmental context. L6P secretion impairment is predicted, not experimentally measured in the accessible text. |
| [PMID:8076608](https://pubmed.ncbi.nlm.nih.gov/8076608/) | Original PMC abstract: one CUG-initiated mouse FGF3 form has competing nuclear/secretory targeting signals. | Scanned body not independently read. No human alternate-product definition inferred. |
| [PMID:11438656](https://pubmed.ncbi.nlm.nih.gov/11438656/) | Original abstract read; independent ROOT Methods read identifies mouse FGF3 cDNAs and signal-peptide-deleted pKC4.16. NoBP/EBP2 association and nuclear-mutant effects. | No endogenous human nuclear function, natural human isoform or FGF3 ribosome-biogenesis activity established. |

The [author-hosted 8663044 PDF](https://bpb-us-e2.wpmucdn.com/sites.wustl.edu/dist/8/2092/files/2019/08/Ornitz_FGF_specificity_JBC.pdf) and [20702560 publisher PDF](https://journals.biologists.com/dev/article-pdf/137/18/2989/1551149/2989.pdf) were read separately from the immutable abstract-only publication caches. Access to a full original is not inferred from the cache flag; nor is the cache rewritten after a separate read.

## Inference sources

[FGF3-evidence.yaml](FGF3-evidence.yaml) records source URLs/hashes and projections. The complete PANTHER v19 tree places human P11487 at PTN002479513, below PTN000160075. The actual target sequence in the 982-sequence MSA exactly matches the 239-aa canonical sequence. All 35 family assertions were inspected: 23 positive IBDs and 12 IRDs. Nine positives, and no negative assertion, lie on the FGF3 path. In particular, FHF divergence node PTN000160077 is not an ancestor of FGF3. This checks target inheritance, not every descendant paper.

The tree's aggregate `PANTHER_GO_SLIM_CC` field includes extracellular NOT strings. They are preserved in the projection as a source discrepancy with unresolved semantics; they are not substituted for literal PAINT node assertions. Current GOA, literal IBD/IRD records and actual ancestry are separately identified. The complete tree supersedes the earlier partial capture for this path check, without erasing the prior access limitation.

Five actual ARBA branches match FunFam `2.80.10.50:FF:000060`: ARBA00026583/269 (morphogenesis), ARBA00027538/61 (proliferation, excludes Fungi), ARBA00028689/231 and ARBA00028859/278 (developmental regulation), and ARBA00084988/10 (FGFR signaling, Metazoa). Indices are zero-based. InterPro's P11487 response matches IPR002209 at 33–187 and supplies its GO:0008083 mapping. These mechanisms are not independent experiments. GO_REF:0000044 maps the reviewed UniProt Secreted/SL-0243 location; it is not HPA evidence.

Reactome participant captures establish P11487 inclusion where individually marked in the evidence table. They do not resolve every nested complex compartment, and cytosolic enclosing complexes do not make the ligand a cytosolic enzyme. Remaining exact routes were not recovered after HTTP 429 responses; the location decisions use independent ligand evidence with the event-specific limit retained. Cached event summaries alone do not prove membership. No additional event-specific biological function is asserted.

## Products and ontology

P11487 has one displayed 239-aa sequence and no curated alternative splice products. The record predicts signal peptide 1–17 and annotates chain 18–239. No human CUG/AUG split or experimentally resolved human processing boundary is added from mouse constructs.

Official GO definitions and strict `is_a`/`part_of` ancestry were checked. GO:0008543 and GO:0008284 are not an ancestor/descendant pair. Broader developmental terms remain contextual because the cardiac response does not exhaust otic/craniofacial scope. The target had no match in the current GO-CAM index; no NEW annotation was proposed.

## Review follow-up: compartment and developmental specificity

The positive cytoplasm IBD at PTN000160075, inherited along the verified target path, is the affirmative support for the non-core active-compartment inference. The [GO:0005737 definition](https://www.ebi.ac.uk/QuickGO/term/GO:0005737) includes organelles but excludes the nucleus. Mouse nuclear-targeting studies therefore do not independently establish cytoplasmic activity, and passage through the secretory pathway is not proof of activity there. Those studies delimit what remains unverified for endogenous human FGF3. The broad ancestral node and absence of a cytoplasm statement from UniProt do not themselves demonstrate target-specific loss.

The five PMID:2470007 contexts retain term-specific uncertainty under the campaign's source-access instruction. Independently supported extracellular ligand, growth-factor and developmental claims remain positive elsewhere. [Strict GO:0008543 ancestry](https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0008543/ancestors?relations=is_a%2Cpart_of) includes signal transduction (GO:0007165), but not cell-cell signaling (GO:0007267); the latter cannot receive a hierarchy-based TOO_GENERAL decision from that pathway alone.

The otic question now distinguishes [inner ear development](https://www.ebi.ac.uk/QuickGO/term/GO:0048839), [inner ear morphogenesis](https://www.ebi.ac.uk/QuickGO/term/GO:0042472) and [otic vesicle development](https://www.ebi.ac.uk/QuickGO/term/GO:0071599). GO:0042472 descends from the retained GO:0009653 and is part of GO:0048839, so adding it as NEW would duplicate existing hierarchical coverage. Human LAMM abstracts establish developmental necessity without resolving the precise signaling stage or direct process assignment. PMID:8663044's original receptor-specificity/mitogenesis experiments do not assay inner-ear development, despite the broader grouping of functional statements under its UniProt ECO citation.

The [mouse comparator query](https://www.ebi.ac.uk/QuickGO/services/annotation/search?goId=GO:0048839&taxonId=10090&limit=200&page=1) contains Fgf3, Fgf8 and Fgf10 within the inspected first 200 of 696 records. The experimental MGI witnesses use `acts_upstream_of_or_within`; the inspected `involved_in` otic-placode entries are TAS assigned by ParkinsonsUK-UCL. This is a nonexhaustive annotation comparison, not a claim to have read those additional primary papers or to have demonstrated the corresponding direct human process. The question preserves these distinctions without replacing the broader developmental coverage with an ear-only assertion.
