# DNM1 evidence notes

## 2026-10-17: annotation review

DNM1 is human dynamin 1 (HGNC:2972; UniProtKB:Q05193), formerly named DNM. The review preserves all 79 source annotation objects produced by the normal fetch. The downloaded GOA contains 80 records: two presynapse ISS records have the same review identity but different database record identifiers/dates, and the normal seeder represents them once. No source row has been removed or relabeled and no new annotation is proposed. The actions are 23 ACCEPT, 24 KEEP_AS_NON_CORE, 30 MODIFY and 2 UNDECIDED.

The integrated core is GTPase-driven membrane remodeling and scission. Reconstituted nanotube closure requires GTP hydrolysis and occurs without a leaky membrane intermediate; assembly-dependent G-domain association couples hydrolysis to polymer behavior. The selected GO:0061791 GTPase motor activity does not require the particular twisting geometry stated by the more specific GO:1990606 definition. Different experimental systems support constriction, squeeze/release and conformational-change models. The structural and self-association annotations describe components of this same mechanism, rather than separate core activities. See [19084269](https://pubmed.ncbi.nlm.nih.gov/19084269/), [20428113](https://pubmed.ncbi.nlm.nih.gov/20428113/) and [30069048](https://pubmed.ncbi.nlm.nih.gov/30069048/).

Vesicle scission, receptor-mediated endocytosis and synaptic vesicle budding describe complementary roles of this activity. The checked is_a/part_of closures contain no ancestor/descendant relation between these three selected process terms, or between clathrin-coated pit and presynapse. In the receptor context, [10521508](https://pubmed.ncbi.nlm.nih.gov/10521508/) reports inhibition of CXCR4 internalization by dominant-negative dynamin-1 in COS-1 and HEK-293 cells. Its cached abstract does not identify that dynamin mutant, and it is not the PH-domain perturbation paper [10074457](https://pubmed.ncbi.nlm.nih.gov/10074457/).

### Interaction evidence

The [ClinGen project instruction](https://github.com/ai4curation/ai-gene-review/blob/d7d41d1bcafd935f12f3b5fad28c43e5f02ed60f/projects/CLINGEN_MENDELIAN.md#curation-instructions) retains supported generic interactions when a narrower function cannot be established. Consequently, association with DNM2, HTT, SPG11, NOS3 or mixed-species uncoating machinery remains non-core; it is not declared false because it is generic or obtained in a screen. Different literal partner assertions are assessed separately even when their GO term is identical.

SH3-domain binding refinements use evidence for the binding region, not just the partner's domain inventory. The SNX9 purified-pair/deletion experiments, SNX33 SH3-deletion experiments, human FBP17 and NOSTRIN construct experiments, and the GRB2 peptide/domain records provide that additional basis. Later AP-MS observations of the same pair supply association evidence; they do not by themselves demonstrate direct contact or the SH3 interface. LRRK2 binding is supported by the human N-terminal-fragment Y2H and full-length co-IP experiments; this does not assign kinase activity to DNM1. Human HTT 1–450 and SPG11 C-terminal fragments are explicitly distinguished from unmodified native full-length complexes.

The [source evidence guide](DNM1-source-evidence.md) records the assay and access limits. Reproducible extracts in [DNM1-bioinformatics](DNM1-bioinformatics/README.md) retain the primary interaction direction and complete accession groups. They do not turn gene-level protein groups into isoform-specific evidence.

### Context and unresolved evidence

The mRNA capture annotation is retained non-core. The original-author thesis table reports DNM1 in class III, with one qualifying isotope-labeling experiment, rather than among the individually validated PAR-CLIP proteins. UV crosslinking and denaturing oligo-dT enrichment support an RNA-associated pool without establishing a separate physiological RNA-regulation mechanism. The [thesis](https://refubium.fu-berlin.de/bitstream/handle/fub188/9034/Dissertation_Baltz.pdf?sequence=1) contains the literal row on PDF page 147; the reproducible extract preserves the measurements.

For [35220002](https://pubmed.ncbi.nlm.nih.gov/35220002/), mouse loss-of-function produces larger synaptic vesicles and pits. Human DNM1 rescues fluorescence-based endocytic endpoints, but the reported rescue is not an EM demonstration of vesicle-size restoration. The size-regulation assertion is retained non-core. The separate literal clathrin-cage assembly assertion remains UNDECIDED: the source measures pit geometry and accumulation, while the coat-assembly interpretation invokes earlier literature. That uncertainty does not deny DNM1's demonstrated scission activity or the measured vesicle phenotype.

For [23533145](https://pubmed.ncbi.nlm.nih.gov/23533145/), the genuine main article establishes expressed-prostatic-secretion urine preparation and exosome-enrichment/proteomics methods. The target supplementary workbook could not be recovered as a usable workbook; unsuccessful downloads were an access message or challenge page. The DNM1-specific exosome assertion therefore remains UNDECIDED, without alleging contamination or curator misattribution.

### Products and historical reagents

The four official products are Q05193-1 and Q05193-2, each 864 residues, and Q05193-3 and Q05193-5, each 851 residues. UniProt names Q05193-5 isoform 4. Their sequences were independently reconstructed from the two annotated splice changes and checked against official FASTAs. The 2010 GG construct joins human residues 6–320 and 726–750. The 2018 human 6DLU deletion construct matches residues 1–748, shared by products 1 and 3. Neither engineered reagent establishes equivalent activity of all four natural products. The earlier nanotube paper's cited purification protocol identifies human DNM1 cDNA but does not resolve the current splice product.

### Access and provenance

Normal fetch and publication caching succeeded. The configured Falcon research attempt failed authentication; the genuine perplexity-lite fallback failed with insufficient quota. No provider report was invented. Protected pre-existing publication, Reactome and family files are retained byte-for-byte. Newly obtained original articles and supplements informed the review without silently changing abstract-only cache flags. The source guide distinguishes cached content, separately recovered originals, source tables and unresolved access.

Six brief exact evidence anchors occur once each in the review: 8 words from 19084269, 12 from 20428113, 4 from 15252009, 8 from 15703209, 5 from 18353773 and 5 from 24282027. Other supports are reference-only. These notes and the evidence guide add no verbatim source excerpts. Source records and measurement tables are provenance, not additional biological conclusions.
