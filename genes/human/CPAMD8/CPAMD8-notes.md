# CPAMD8 research notes

## 2026-10-12: Development is established; the molecular effector remains unresolved

CPAMD8 is the accepted human symbol for HGNC:23228 and UniProt Q8IZJ3. The historical alias VIP is ambiguous: the unrelated vasoactive intestinal peptide gene has UniProt P01282. None of that peptide's functions are transferred here.

Human recessive variants cause a spectrum of anterior-segment abnormalities. The original study combines family segregation, abnormal splicing in patient RNA or minigenes, and developmental expression in the lens, iris, cornea and retina. This supports the existing eye-development IMP annotation; camera-type eye development is a more precise term for the demonstrated human structures. Expression is corroboration, not the sole basis for assigning participation. The molecular step that CPAMD8 performs is not identified. [PMID:27839872, "CPAMD8 splice-site mutations caused aberrant pre-mRNA splicing"](https://pubmed.ncbi.nlm.nih.gov/27839872/)

Independent 2020 studies extend the human phenotype to congenital and juvenile glaucoma. The actual Bonet-Fernández paper also examines F0 mosaic zebrafish with two independent targeted deletions, control-injected embryos and ocular histology. Abnormal anterior chambers and matrix organization support a developmental requirement, without establishing a direct matrix-assembly or protease-regulatory activity. Its Discussion calls the inhibitor mechanism putative. The Siggs paper provides clinical genetics and adult-eye RNA-seq, which likewise do not resolve a biochemical mechanism. [PMID:32274568](https://doi.org/10.1007/s00439-020-02164-0), [PMID:32085876](https://pubmed.ncbi.nlm.nih.gov/32085876/)

The 2024 study reports altered anterior chamber and lens geometry in double heterozygous cpamd8/adamtsl4 zebrafish, using wild-type and single-heterozygous sibling controls. Its cultured-protein retention and ER-stress experiments are ADAMTSL4 assays. They are not CPAMD8 localization or activity measurements, and the genetic interaction does not establish direct binding between the proteins. [PMID:38891949](https://pmc.ncbi.nlm.nih.gov/articles/PMC11171635/)

The 2026 abstract describes CPAMD8 knockdown in primary human ciliary-muscle myofibroblasts grown in a three-dimensional Matrigel system. Aggregate growth and selected expression responses change. Full Methods/Results were inaccessible, so these observations are kept at abstract scope and do not establish a direct TGF-beta receptor interaction or a new proliferation/signaling process annotation. [PMID:42692183](https://pubmed.ncbi.nlm.nih.gov/42692183/)

## Biochemical activity and localization

The original 2004 abstract explicitly reports Kazal-domain heparin binding and ionic membrane association. The heparin observation supports a narrow molecular-function proposal. It does not identify an endogenous heparan-sulfate ligand, establish the full-chain affinity, or show that the interaction drives eye development. No experimental isoform or construct coordinates are assigned because the original Methods/Results were not recovered. [PMID:15177561, "CPAMD8 binds to heparin"](https://pubmed.ncbi.nlm.nih.gov/15177561/)

The inhibitor IEA comes from the actual broad InterPro entries IPR001599 and IPR002890, not from the Kazal domain. These entries include macroglobulin/complement-family proteins and map to endopeptidase inhibitor activity. Their presence does not by itself establish CPAMD8-specific inhibition; the accessible target evidence also does not refute it. The annotation therefore remains UNDECIDED. An empty formal core-function list and an MF_DARK knowledge gap preserve this distinction: a measured interaction and a developmental requirement do not yet identify the physiological molecular core.

Membrane-associated and soluble extracellular pools are compatible. The original ionic-association result and reviewed UniProt support peripheral plasma-membrane association. Separately, the actual 2020 paper reports N- and C-terminal CPAMD8 fragments in human aqueous and vitreous humor using three antibodies. The latter is the evidence for a soluble pool under the current extracellular-region definition, which excludes cell-surface attachment. The original normal cache is abstract-only; the publisher PDF Methods and main Results were independently read, but supplementary Figure S7 was not recovered. No transmembrane helix, GPI anchor, exact cleavage mechanism or fragment-specific activity is inferred. [PMID:15177561, "membrane associated via ionic interaction."](https://pubmed.ncbi.nlm.nih.gov/15177561/), [PMID:32274568, "C-terminal CPAMD8 fragments in aqueous humor (AH)"](https://doi.org/10.1007/s00439-020-02164-0)

## Products and coordinate boundaries

Current reviewed Q8IZJ3 has two products: the displayed 1,885-residue sequence and a 1,815-residue alternative sequence. VSP_031137 replaces residues 1809–1815, and VSP_031138 deletes residues 1816–1885; reconstruction matches the official isoform FASTA. Both retain the current annotated Kazal-like region at 1706–1757. This sequence correspondence does not prove equivalent activity or localization.

The 2016 paper uses publication-specific 1,932- and 1,863-residue CPAMD8-1a/1b names. Those historical names and coordinates are not silently equated to the current products. The cDNA-resource clone BAC11400.1 is separately flagged by UniProt for erroneous initiation/truncation; its partial sequence does not replace the current complete alternative product. Processing into fragments is observed, but no functionally distinct cleavage-product class is asserted without activity-resolved evidence.

## Public source guide

- [Original 2004 biochemical abstract](https://pubmed.ncbi.nlm.nih.gov/15177561/): explicit Kazal-domain heparin binding and ionic membrane association; full original assays unavailable.
- [Original 2016 developmental paper](https://pubmed.ncbi.nlm.nih.gov/27839872/): patient variants/splicing and human developmental expression, actual unique main text read.
- [Original 2020 publisher PDF](https://link.springer.com/content/pdf/10.1007/s00439-020-02164-0.pdf): Methods pp1211–1213; ocular-fluid and tissue Results p1220; Figure8 p1222; putative inhibitor discussion pp1227–1228. Supplementary FigureS7 was not inspected.
- [Original 2020 clinical/RNA-seq PDF](https://research-management.mq.edu.au/ws/portalfiles/portal/164698018/Publisher_version_open_access_.pdf): Methods pp759–760, ocular-expression Results p763 and Discussion p765.
- [Original 2024 full article](https://pmc.ncbi.nlm.nih.gov/articles/PMC11171635/): sections2.5 and4.10, Figure7 caption; direct cellular protein assays elsewhere concern ADAMTSL4.
- [2026 primary-cell study abstract](https://pubmed.ncbi.nlm.nih.gov/42692183/): full assay details unavailable.

Exact source identities, hashes, current term definitions and read boundaries are recorded in [the manual evidence index](CPAMD8-evidence-index.yaml).


## 2026-10-12: Inhibitor architecture, localization scope and provenance clarification

The current reviewed sequence does contain an independently annotated Kazal-like domain at residues 1706–1757, with IPR002350, PF07648 and SSF100895 family assignments. Both reconstructed products retain this region. That architecture supports a possible inhibitor function and must be considered separately from the actual IEA's broader IPR001599/IPR002890 source mappings. The original 2004 abstract combines inhibitor-like and follistatin-like domain terminology but reports heparin binding, not an explicit endopeptidase-inhibition result. Domain classification does not settle activity in this target; nor does the follistatin-like label establish inactivity. Full original biochemical Methods/Results remain unavailable. The inhibitor call remains UNDECIDED, with the positive architectural hypothesis made explicit. [PMID:15177561](https://pubmed.ncbi.nlm.nih.gov/15177561/), [reviewed Q8IZJ3 domain feature](https://www.uniprot.org/uniprotkb/Q8IZJ3/entry)

The soluble fragments reported in aqueous and vitreous humor fit extracellular localization. The original main Results at printed page 1220 and Discussion at pages 1227–1228 distinguish these fragments from intact protein; supplementary Figure S7 remains uninspected. Current official QuickGO and OLS mark GO:0005615 extracellular space obsolete and replaced by GO:0005576. The existing extracellular-region term is therefore retained, with no inference of intact-chain detection or fragment-specific activity. [PMID:32274568](https://doi.org/10.1007/s00439-020-02164-0), [current GO:0005615 record](https://www.ebi.ac.uk/QuickGO/term/GO:0005615)

Extracellular secretion and peripheral membrane association are basic cellular dispositions of CPAMD8, supported separately by the fluid-fragment and ionic-association observations. They are retained as core localization context rather than a downstream perturbation phenotype. This does not identify what molecular activity CPAMD8 performs there: the formal activity-oriented core synthesis remains empty and the physiological MF remains unresolved. The propagation classification and the MF knowledge gap therefore address different claims.

The manual evidence index is a guide to source identity, public locations, sequence reconstruction and read limits, not an independent experiment or extra corroborating source. Duplicate annotation reasons and their self-citations have been removed; the review YAML is the single location for those judgments. Original raw source records and public primary-source locators remain available in the index. Earlier notes remain a chronological record; this clarification supersedes their implication that the broad InterPro mappings alone exhaust the inhibitor-domain evidence.


## Ontology verification, 2026-10-12

Fresh [QuickGO](https://www.ebi.ac.uk/QuickGO/term/GO:0005615) and [OLS](https://www.ebi.ac.uk/ols4/ontologies/go/classes?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FGO_0005615) responses independently confirm that GO:0005615 is obsolete and replaced by GO:0005576. The [completed GO issue](https://github.com/geneontology/go-ontology/issues/31545), closed on 2026-04-23, records the obsoletion proposal and subsequent cleanup of the replacement term's comment. Its closing date is not used as a claimed ontology release date. Older repository term-label caches do not override these current records.

The extracellular-location rationale now links the ontology evidence directly. The evidence index distills the term status, replacement, retrieval times, source URLs and response hashes. All annotation actions, original source fields, products, references, quotations and molecular-function uncertainty remain unchanged; the independent ocular-fluid fragment evidence remains positive.
