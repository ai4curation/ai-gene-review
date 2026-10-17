# DNAAF11 source guide

DNAAF11 is the current human symbol for LRRC6 ([HGNC:16725](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16725); [UniProt Q86X45](https://www.uniprot.org/uniprotkb/Q86X45/entry)). The review preserves all 53 imported annotation source objects, including their qualifiers, evidence types and supporting entities. Two raw records differing in annotation identifier/date normalize to the same final DynAP source row; no biological assertion was discarded.

## Assembly and location

The single core is outer and inner dynein-arm assembly in DynAPs. The evidence establishes participation in assembly and incorporation of axonemal arms, without demonstrating an autonomous LRRC6 motor, folding-chaperone, DNA-binding or transport activity. The three short supporting quotations appear only in the YAML core.

| Primary source | Evidence and boundary |
| --- | --- |
| [PMID:23122589](https://pubmed.ncbi.nlm.nih.gov/23122589/) | Human primary ciliary dyskinesia, dynein-arm ultrastructure and beating defects. Control nasal-brush LRRC6 staining occurs in cytoplasm and cilia; mutant loss provides a specificity control. |
| [PMID:23527195](https://pubmed.ncbi.nlm.nih.gov/23527195/) | Human airway cultures and knockdown show loss of dynein arms while cilia remain. LRRC6 is cytoplasmic/basal-body-proximal and absent from axonemes in this preparation. Reduced dynein transcripts do not establish direct DNA binding by LRRC6. |
| [PMID:33403504](https://pubmed.ncbi.nlm.nih.gov/33403504/) | Separately indexed original Figure 2c supports human control sperm-flagellum staining with mutant loss. Figure 4 germ-cell cytoplasmic localization uses mouse, as stated in the Methods. The normal cache remains abstract-only; indexed original sections, not image reanalysis, supply these distinctions. |
| [PMID:30561330](https://elifesciences.org/articles/38497) | Results on conservation of DynAPs and the Figure 1 supplement identify endogenous human airway LRRC6/DNAI1 foci. Tagged colocalization and dynamic experiments are separately Xenopus; see the construct and immunofluorescence Methods. |
| [PMID:33263282](https://elifesciences.org/articles/58662) | Tagged Xenopus LRRC6 and construct Methods corroborate DynAP organization. This is not an additional endogenous human localization experiment. |
| [PMID:27353389](https://pubmed.ncbi.nlm.nih.gov/27353389/) | Complete abstract supports mouse outer-arm targeting defects despite preserved 9+2 architecture and IC1–IC2 association. Full text was not recovered. Direct MGI cytosol annotations on [mouse O88978](https://www.ebi.ac.uk/QuickGO/annotations?geneProductId=UniProtKB%3AO88978&goId=GO%3A0005829) remain curator-supported, including spermatocyte and spermatid IDA records. |

The positive human ciliary observations are preserved alongside the negative airway result. Their discrepancy does not justify deleting every ciliary annotation. Broad cilium is refined to motile cilium. Broad cytoplasm is refined to the directly demonstrated DynAP location; microscopy of foci does not independently prove a separate diffuse cytosolic pool. Existing cytosol transfers retain their mouse donor grounding.

[GO:0120293](https://www.ebi.ac.uk/QuickGO/term/GO:0120293) is an intracellular membraneless organelle and cellular anatomical structure. It belongs in the core `locations` slot, not the protein-complex slot. The extracellular-region electronic row instead conflates fluid-movement processes with the location of the gene product. Cilia move extracellular fluid without making the intracellular assembly factor extracellular. This judgment does not depend on absence of a secretion signal.

## Interactions and partner classes

Three ZMYND10 sources remain positive with their experimental limits. [PMID:23891469](https://pubmed.ncbi.nlm.nih.gov/23891469/) includes tagged human LRRC6–ZMYND10 association and CS-region interaction, with separate rat tissue and Xenopus experiments. The normal [PMID:23891471](https://pubmed.ncbi.nlm.nih.gov/23891471/) cache is abstract-only; separately indexed primary Methods/Results identify human cDNA two-hybrid tests and GST-ZMYND10 pull-down of in-vitro-translated Myc-LRRC6 with GST control. [PMID:29601588](https://pubmed.ncbi.nlm.nih.gov/29601588/) supports ZMYND10-dependent stabilization of LRRC6. That direction is not inverted into autonomous LRRC6 folding activity.

[PMID:29916806](https://elifesciences.org/articles/34389), Results on LRRC6 interaction and the cell-culture/transfection Methods, distinguishes negative endogenous mouse testis association from positive transient human LRRC6/mouse Zmynd10 assays. The proposed relay is a mechanistic model; it does not independently demonstrate LRRC6 protein folding. Failure to detect an endogenous pair in one context does not negate every positive tagged assay.

The SCRIB associations are [IntAct EBI-9394895](https://www.ebi.ac.uk/intact/interaction/EBI-9394895) from [PMID:25036637](https://pubmed.ncbi.nlm.nih.gov/25036637/) and [EBI-54631541](https://www.ebi.ac.uk/intact/interaction/EBI-54631541) from [PMID:33961781](https://pubmed.ncbi.nlm.nih.gov/33961781/). Both are human HEK293T anti-tag association experiments with C-terminally tagged LRRC6. They do not resolve a direct binary interface or demonstrate a polarity function for LRRC6. The available caches are marked full text but contain short extracts; this review does not claim access to every original target table or Methods section.

The nine [HuRI pairs, PMID:32296183](https://pmc.ncbi.nlm.nih.gov/articles/PMC7169983/) were resolved against the literal IntAct records and exact protein sequence/taxon signatures. Each has positive validated two-hybrid evidence (MI:1356) plus pooled and array screen records. These are stages of one study. The main text reports quadruplicate retesting and sequence confirmation; no supplementary threshold or pair-specific orthogonal validation is assumed. Records can be retrieved through the [IntAct PSICQUIC target query](https://www.ebi.ac.uk/Tools/webservices/psicquic/intact/webservices/current/search/query/id:Q86X45?format=tab27&firstResult=0&maxResults=200).

| Literal partner | Disposition and scope |
| --- | --- |
| P26196, DDX6, 483 aa | Refine to [DEAD/H-box RNA helicase binding](https://www.ebi.ac.uk/QuickGO/term/GO:0017151). [DDX6 identity and helicase domains](https://www.uniprot.org/uniprotkb/P26196/entry) establish the partner class; no RNA-helicase activity is transferred to LRRC6. |
| P54274-2, TERF1, 419 aa | Retain non-core binding. Telomeric-DNA and spindle roles do not supply a specific LRRC6 binding-function term; no absolute compartment incompatibility is asserted. |
| Q6FHY5, MEOX2 clone, 303 aa | Refine to [DNA-binding transcription factor binding](https://www.ebi.ac.uk/QuickGO/term/GO:0140297). Comparison with [P50222](https://www.uniprot.org/uniprotkb/P50222/entry) finds only deletion of canonical Q81, outside the homeobox at residues 187–246. The reviewed record distinguishes DNA-dependent CDKN1A activation from DNA-independent CDKN2A activation. The source accession remains Q6FHY5; no native LRRC6 transcriptional pathway is inferred. |
| Q6PF05, TTC23L, 361 aa | Retain non-core binding; TPR domains and centrosomal/spindle localization do not establish a more informative activity class. |
| Q7RTT5, SSX7, 188 aa | Retain non-core binding; proposed transcription modulation does not establish a DNA-binding transcription-factor class. |
| Q7Z5L7-3, podocan isoform 3, 661 aa | Retain non-core binding. This tested product is cytoplasmic; the secreted isoform 1 cannot be substituted to claim a compartment mismatch or extracellular-matrix function. |
| Q96II8-3, LRCH3 isoform 3, 712 aa | Retain non-core binding. Complex association supports a possible cytoskeletal role, but the partner's own activity remains tentative; a regulator-binding refinement would exceed that class evidence. |
| Q9H8W4, PLEKHF2, 249 aa | Retain non-core binding. PH/FYVE domains and endosomal trafficking do not establish an LRRC6 adaptor or receptor-regulatory activity. |
| Q9Y333, LSM2, 95 aa | Retain non-core binding. Association with an RNA-related complex does not itself establish RNA binding by LRRC6 or a more specific pair function. |

The two class refinements describe qualitative capacity to bind the demonstrated partner class. They do not require an established native pathway, and they do not prove that the interaction occurs in motile cilia. Positive associations without a supported finer term follow the [project's generic-binding instruction](https://github.com/ai4curation/ai-gene-review/blob/d06a9a79482eeea9597a393455fb67fe5151be5b/projects/CLINGEN_MENDELIAN.md#curation-instructions).

## Inference, products and unresolved biology

The [PANTHER PTHR18849](https://www.pantherdb.org/panther/family.do?clsAccession=PTHR18849) reconstruction places the human leaf below the cytoplasm IBD at PTN007663797 and the outer-arm-assembly IBD at PTN007663798. Both ancestral placements are valid. Human target evidence appearing among descendants is legitimate experimental grounding, not circularity; donor count is not used to grade the inference.

The explicit matching condition sets were checked for ARBA00026971, ARBA00028703, ARBA00047243, ARBA00090010, ARBA00091170 and ARBA00091714 through the [UniProt ARBA rule service](https://rest.uniprot.org/arba/ARBA00026971). The sequence/family matches do not turn infertility into proof of a direct reproductive-development mechanism. The combined electronic reference [GO_REF:0000120](https://geneontology.org/GO_REF/0000120.html) describes combined annotation methods; each source row is assessed for its biological role separately.

The two official products are 466 and 414 residues. The short product retains canonical residues 1–408, including the CS domain at 301–396; residues 409–414 are replaced and 415–466 are absent. It is not CS-deficient, and it is not equivalent to an experimental premature-stop construct. No assay here establishes equivalent function of both natural products.

[PMID:10775177](https://pubmed.ncbi.nlm.nih.gov/10775177/) remains abstract-only: it identifies human and mouse cDNAs and reports mouse meiotic expression. Male-gonad and reproductive-development claims remain unresolved because expression and infertility do not resolve the molecular participation being asserted. [PMID:37328841](https://pmc.ncbi.nlm.nih.gov/articles/PMC10273532/) reports mouse organoid and tagged HeLa evidence for FOXJ1 nuclear accumulation; its discussion leaves the direct connection unresolved. This is retained as mechanistic context, without adding a transport activity or a new process annotation.
