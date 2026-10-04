# B9D1 curation notes

## 2026-09-30 — ClinGen Mendelian campaign

Human B9D1 is UniProt Q9UPM9, HGNC:24123 and NCBI Gene 27077. The normal source seed contains 30 distinct GOA annotation objects and two alternative products, Q9UPM9-1 and Q9UPM9-2. All source terms, identifiers, evidence codes, qualifiers, interaction partners and isoform metadata are preserved.

### Biological synthesis

B9D1 contributes to the MKS complex at the ciliary transition zone. Human-protein interaction experiments support an MKS1–B9D2–B9D1 arrangement, with B9D2 connecting the other two subunits. The complex helps establish the ciliary gate and its protein composition. Its interdependent localization and contribution to cilium assembly support one core unit with complex, location and process terms. A specific autonomous molecular activity remains unestablished; the molecular-function field is therefore omitted rather than populated from B9/C2-like domain resemblance [PMID:22179047](https://pubmed.ncbi.nlm.nih.gov/22179047/), [PMID:32726168](https://pubmed.ncbi.nlm.nih.gov/32726168/).

The five generic binding annotations all record B9D2 (Q9BPU9). These supported interactions are retained as non-core. The targeted three-hybrid experiments identify B9D2 as the bridge, so their architecture does not establish adaptor activity for B9D1. Large-screen pair tables were not independently inspected; absence from an abstract is not grounds for rejecting an experimental annotation.

### Evidence and assay limits

[PMID:19208769](https://pubmed.ncbi.nlm.nih.gov/19208769/) was read from its complete cached abstract and official figure captions. It distinguishes human ciliogenesis defects from the absence of comparable overt structural defects in worm mutants. The localization captions use tagged human orthologs in mouse IMCD3 cells; they should not be described as endogenous human-cell microscopy. Centrosome, basal-body and historical axonemal annotations remain compatible with the newer transition-zone findings. Full Methods and original images were not independently inspected.

[PMID:22179047](https://pubmed.ncbi.nlm.nih.gov/22179047/) is abstract-only in the cache. It reports interdependent B9D1/TMEM231/CC2D2A localization and altered ciliary membrane diffusion and composition after complex disruption. This supports a barrier assembly and protein-localization role without identifying an independent ligand-receptor activity for B9D1.

[PMID:32726168](https://pubmed.ncbi.nlm.nih.gov/32726168/) was examined in its available interaction and localization Results, Discussion and relevant Methods. Human constructs were tested by cell-lysate immunoprecipitation and three-hybrid assays. Tagged B9D1 localized to the transition zone in control RPE1 cells and depended on MKS1 and B9D2. The knockout lines in this paper target MKS1 and B9D2, not B9D1. Normal measured IFT localization and movement do not demonstrate normal permeability for every soluble protein. Original images, videos and supplementary data were not independently inspected.

[PMID:41165761](https://pubmed.ncbi.nlm.nih.gov/41165761/) was identified through PubMed and the JCI primary article. The complete available Results, Discussion and Methods distinguish human B9D1-knockout ciliogenesis, CP110-removal and ciliary tubulin-modification phenotypes from the detailed B9D2/TMEM67 trafficking and vesicle assays. The work supports ciliary organization, without assigning B9D1 an intrinsic tubulin-modifying activity or direct TMEM67 interaction. Original images and supplements were not independently inspected. Both normal full-text caches were recovered for final assessment.

The [PMID:40205054](https://pubmed.ncbi.nlm.nih.gov/40205054/) interaction source has a publisher correction, [PMID:41039152](https://pubmed.ncbi.nlm.nih.gov/41039152/). The complete available correction text and publisher PDF were read. They correct a duplicated loss-function equation; they do not retract the paper or withdraw the B9D1–B9D2 interaction. Original source and correction identifiers are both retained.

The three Reactome event summaries describe cytosolic context during ciliary assembly. They assign nucleotide exchange to RAB3IP and recruitment activities to their respective machinery, not to B9D1. Broad cytosolic and membrane-associated pools remain compatible with the focused transition-zone role.

### Propagation and receptor activity

The mouse receptor donor Q9R1S0 traces through MGI J:178421 to [PMID:21763481](https://pubmed.ncbi.nlm.nih.gov/21763481/), not PMID:21493627. The complete cached Methods, Results and Discussion were read. Mutant mouse fibroblasts retain cilia but fail to recruit Smoothened after SAG stimulation and show reduced Gli1/Ptch1 responses. GO:0008158 requires Hedgehog ligand recognition and signal transmission across a membrane; these experiments establish a ciliary localization mechanism, not intrinsic receptor activity. Both transferred receptor rows are therefore removed. The original images and supplements were not independently inspected. The human patient variant in this study concerns B9D2, not B9D1. The Smoothened pathway associations are retained as non-core consequences of ciliary organization.

The cilium-assembly ISS donor Q9NXB0 is human MKS1, not a mouse B9D1 ortholog. Its source identifier is preserved. The PAINT node was not reconstructed; independent functional evidence supports the retained process and complex annotations, without treating donor count as evidence strength.

The final review contains 14 ACCEPT, 13 KEEP_AS_NON_CORE, one MODIFY and two REMOVE decisions. The cilium IEA is refined to ciliary transition zone. There are no NEW assertions. A matching GO-CAM index entry was not found; no new process annotation is inferred from that absence.

### Research provenance

The normal Falcon command and configured fallback failed during dependency resolution before producing a provider report. This journal records manual primary-source research. Each of the two new donor/mechanistic references had one ordinary fetch attempt, which failed with DNS errors; their independently verified identities and original failure outputs support the existing reference-cache workflow. The ordinary reference-cache recovery returned full text for both papers. The final review incorporates those records, resolves the two receptor transfers and preserves every source annotation object and alternative product.

The newer study also distinguishes human B9D1 knockout results from B9D2-focused mouse, zebrafish and disease-variant experiments. Its preciliary centriole microscopy uses tagged MKS1/B9D2, with an acknowledged overexpression caveat. Neither complex association nor altered tubulin modifications is used to infer an autonomous B9D1 molecular activity.


## 2026-09-30 — PR #3579 evidence clarification

The [GO:0016020 definition](https://amigo.geneontology.org/amigo/term/GO:0016020) includes bilayer-associated proteins and complexes. Soluble B9D1 can therefore be membrane-associated through the B9 assembly without spanning the bilayer. The relevant Results of [PMID:41165761](https://pubmed.ncbi.nlm.nih.gov/41165761/) support a B9–TMEM67 module, while its named TMEM67 coimmunoprecipitation partners are B9D2 and MKS1. The revised reason makes the complex-mediated inference explicit and retains the limits on direct B9D1 lipid or TMEM67 contact. Ciliary transition zone remains the core location.

The historical axoneme reason now distinguishes the abstract from the Figure 2B caption of [PMID:19208769](https://pubmed.ncbi.nlm.nih.gov/19208769/): tagged human proteins were observed in mouse IMCD3 cells. This does not establish endogenous B9D1 incorporation into axonemal microtubules. The original images and complete Methods remain uninspected. The cilium-to-transition-zone refinement now acknowledges that its destination is already represented.

Manual reference assessments record the verified primary identifiers and actual read boundaries for PMID:19208769, PMID:22179047 and PMID:32726168. The middle record remains abstract-only. An explicit question documents why no subunit-specific molecular function has yet been assigned; no structural, adaptor or receptor activity was added.

The five supported generic B9D2 interactions remain non-core under the supplied ActionEnum: lack of specificity alone does not establish that an experimental interaction is incorrect. MKS complex membership provides a more informative component assertion, but it does not falsify those interaction records. The review remains 14 ACCEPT, 13 KEEP_AS_NON_CORE, one MODIFY and two REMOVE, with no NEW annotations or added literal excerpts. All original source objects and the core model are preserved.


## 2026-10-01 — Scope of the five retained B9D2 interactions

The [re-review of PR #3579](https://github.com/ai4curation/ai-gene-review/pull/3579#pullrequestreview-5365198735) identifies a distinction that the earlier explanation did not make clearly enough. The repository's generic-binding guidance generally recommends a supported, informative molecular-function replacement or removal for lack of functional information. It explicitly states that such removal does not declare the reported interaction false. The five generic-binding advisories therefore record a real departure from that default. This is a new review; the legacy allowance is not the basis for retention.

For this review, the supplied task instruction retains supported generic interactions outside the core when no justified specific replacement is available. That instruction governs the five `KEEP_AS_NON_CORE` decisions. This is a scoped explanation of those existing decisions, not a claim that they satisfy the repository's default exclusion criterion or a change to the skill, validator or other genes' reviews. Passing the other validation checks does not settle this policy disagreement.

All five source assertions identify the same partner, B9D2 (UniProt Q9BPU9). The targeted human-protein coimmunoprecipitation and three-hybrid experiments in [PMID:32726168](https://pubmed.ncbi.nlm.nih.gov/32726168/), read within the limits recorded above, independently support the MKS1–B9D2–B9D1 association. They identify B9D2 as the connecting subunit. They do not establish an autonomous adaptor activity for B9D1 or a purified binary interface. The other four assertions retain their distinct original studies; their exact screen pair records were not independently inspected. Corroborating the association does not reconstruct those four experiments.

MKS complex membership supplies the functional context, while the IPI rows retain the partner-specific association and its provenance. Substituting adaptor activity would add an unsupported mechanistic interpretation; converting a positively assessed association to `UNDECIDED` solely to silence a warning would change the recorded judgment without new evidence. The correction to PMID:40205054 remains scoped to its published equation correction, as already documented.

The [current B9D1 review](B9D1-ai-review.html) remains 14 ACCEPT, 13 KEEP_AS_NON_CORE, one MODIFY and two REMOVE decisions across all 30 source assertions, with two products, one core synthesis and no NEW annotations. The membrane, historical axoneme and receptor-transfer conclusions remain as documented in the earlier follow-up. This clarification adds no new source reading, quotations or claim of independently verified screen pairs; all canonical source caches retain their existing content and availability flags.
