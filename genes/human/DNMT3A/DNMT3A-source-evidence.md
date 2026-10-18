# DNMT3A source evidence

This guide records the evidence behind the accompanying annotation decisions. It is an authored source-access guide, not an independent experiment or substitute for the cited publications. Annotation row numbers below are zero-based locators; term, reference and partner identifiers are the durable identifiers.

## Scope and source preservation

The review retains all 87 existing source objects, including partner accessions, evidence codes, qualifiers and original references. The normal fetched GOA has 88 raw records and 87 unique annotation tuples, exactly covering those existing objects. Its bytes match the previous snapshot, so no source retirement, replacement or hand-edited GOA was needed. The existing UniProt text, publication and Reactome caches, provider report and earlier history remain unchanged. Earlier notes remain a byte-identical prefix of the notes file.

The ordinary configured Falcon invocation returned the existing cached provider result. Its report body was unchanged, and fallback was not invoked. No fresh provider synthesis is claimed. The evidence assessments below use actual original text, curated interaction records, official product records and traced propagation sources.

Supported generic interactions are retained under the project's [explicit curation instructions](../../../projects/CLINGEN_MENDELIAN.md#curation-instructions). A generic term alone is not a reason to reject a positive experiment. Partner-class refinements require a verified pair, appropriate assay scope and an established partner class; co-purification is not described as purified direct contact.

## Three complementary molecular activities

The catalytic unit is DNA cytosine C5 methylation. [PMID:29414941](https://pubmed.ncbi.nlm.nih.gov/29414941/) directly tests human catalytic-domain constructs and includes measurable non-CpG activity. The broad DNA-cytosine methyltransferase term therefore avoids implying CpG exclusivity. CpG-island silencing is supported by the human promoter experiments in [PMID:23042785](https://pubmed.ncbi.nlm.nih.gov/23042785/); WT1 regulation of DNMT3A expression and downstream DNMT3A promoter occupancy are distinct observations.

The ADD and PWWP modules supply complementary recognition activities. [PMID:19834512](https://pubmed.ncbi.nlm.nih.gov/19834512/) directly tests human ADD recognition of the H3 amino terminus and its K4 methylation state. [PMID:30478443](https://pubmed.ncbi.nlm.nih.gov/30478443/) tests human PWWP recognition of H3K36me2/me3. These reader activities do not constitute new annotation rows. Their functional chromatin compartment is distinct from the additional nucleoplasmic pool detected by imaging.

The W330R developmental-valley phenotype in PMID:30478443 concerns Polycomb/H3K27me3-marked regions, with altered DNA methylation and local loss of H3K27me3. It does not establish the formation of **constitutive** heterochromatin required by [GO:0006346](https://www.ebi.ac.uk/QuickGO/term/GO:0006346). Row 55 retains the reality of the experiments while marking that process interpretation over-annotated.

## Products and assay constructs

Official products are Q9Y6K1-1, 912 residues; Q9Y6K1-2, 723 residues; and Q9Y6K1-3, 166 residues. The second replaces canonical residues 1–213 with a distinct 24-residue amino terminus. The third replaces residues 151–166 and lacks the remainder of the canonical sequence. Product identifiers, names and sequence-change identifiers are retained exactly.

The frequently studied historical **DNMT3A2** reagent is not identified by its suffix alone. In [PMID:32968275](https://pubmed.ncbi.nlm.nih.gov/32968275/), it is human residues 224–912, a 689-residue construct. Deposited structural sequences independently support that mapping. The full DNMT3B3 partner is a catalytically inactive 770-residue product that anchors the nucleosome acidic patch. The resolved complex supports association, not binding to an active methyltransferase solely because the partner is named DNMT3B. The ADD/PWWP densities are incomplete; that is not a negative binding experiment.

The 166-residue natural product lacks the canonical reader and catalytic regions. This limits transfer of the full-length/domain assays, but is not evidence that the short product has no biological role.

## Interactions and original access

| Source | Actual evidence inspected | Important limit |
| --- | --- | --- |
| [16357870](https://pubmed.ncbi.nlm.nih.gov/16357870/) | Original abstract; genuine supplementary Methods; exact EED/EZH2 interaction records; [2007 correction](https://doi.org/10.1038/nature05710) and corrected figure-map text | Human HeLa co-IP is distinct from historical fragment experiments. Corrected S1 labels DNMT3A as 908 residues, so its species/current-product mapping is not assumed. |
| [16682412](https://pubmed.ncbi.nlm.nih.gov/16682412/) | Original abstract and exact curated GST pull-down record: DNMT3A 480–620 with SETDB1 1–527 | Full main text was unavailable. The positive direct-domain assertion and partner class support a bounded refinement; no unseen protocol is supplied. |
| [16983096](https://pubmed.ncbi.nlm.nih.gov/16983096/) | Separately recovered PMC Methods/Results: GST/IVT association, reciprocal human-cell co-IP, fractionation and ChIP | The protected cache's full-text label did not mean it contained those Methods/Results. Viral recruitment does not establish a universal native complex. |
| [17713477](https://pubmed.ncbi.nlm.nih.gov/17713477/) | Separately recovered full PMC original; mouse recombinant complexes and activity assays | The proteins are mouse, including Dnmt3a 220–908 and catalytic 623–908 constructs. No human product equivalence is inferred. |
| [19234465](https://pubmed.ncbi.nlm.nih.gov/19234465/) | Human K562 co-IP and GST-PRMT5/IVT-DNMT3A binding; WT and catalytic-mutant PRMT5 comparisons | Its H4R3me2s-reader claim was not reproduced under the conditions of PMID:19834512. This specific disagreement does not negate the PRMT5 pair. |
| [19798101](https://pubmed.ncbi.nlm.nih.gov/19798101/) | Mouse ESC Np95/Dnmt3a2 co-IP and fusion-protein interaction assays | A human host cell does not make a mouse expression construct human. |
| [21976679](https://pubmed.ncbi.nlm.nih.gov/21976679/) | Separately recovered human-cell CREM-alpha co-IP and promoter experiments | Native complex evidence does not isolate a purified binary interface. |
| [23435381](https://pubmed.ncbi.nlm.nih.gov/23435381/) | Human PTENpg1 antisense-alpha RNA co-IP, ChIP and depletion/recruitment experiments | RNA association is within a native complex, not a purified direct RNA-contact assay. DNA and histone methylation are performed by different factors. |
| [24074865](https://pubmed.ncbi.nlm.nih.gov/24074865/) | [Institutional original and supplement](https://iris.unito.it/bitstream/2318/141912/1/cell7105_proofs.pdf), selected Results and Methods | Figure 6D tests human DNMT3A–EZH2 co-IP with inducible murine Dnmt3L; purified Ezh2–Dnmt3L binding is a separate experiment. The normal cache remains abstract-only. |
| [24656771](https://pubmed.ncbi.nlm.nih.gov/24656771/) | Human WT/R882H purification, coexpression and gel-filtration experiments | Coexpression and mixing separately purified proteins are different tests. No natural-product mapping was established from the paper's name alone. |
| [25383530](https://pubmed.ncbi.nlm.nih.gov/25383530/) | Original abstract and genuine publisher extended-data captions describing human complex structure, activity and gel filtration | Full main text remained unavailable; captions are not represented as a complete Methods read. |
| [32051553](https://pubmed.ncbi.nlm.nih.gov/32051553/) | Human U251 ZNF263 AP-MS/co-IP/ChIP | Co-complex association does not establish a purified binary contact. |
| [32968275](https://pubmed.ncbi.nlm.nih.gov/32968275/) | Human construct Methods and resolved DNMT3A2/DNMT3B3 complex | The DNMT3B3 partner is inactive and the DNMT3A2 construct is 689 residues. |

The 2007 EZH2 correction identifies omitted lanes in Figures 2a, 2c, 4a and S1 and supplies corrected panels. It states that conclusions are unchanged. The correction is recorded without inferring retraction or ignoring the corrected numbering. The [original supplementary Methods](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fnature04431/MediaObjects/41586_2006_BFnature04431_MOESM1_ESM.doc) and [corrected panels](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fnature05710/MediaObjects/41586_2007_BFnature05710_MOESM289_ESM.pdf) are public. Figure text and labels were read; no independent band quantification is claimed.

### Screening records

The [IntAct query](https://www.ebi.ac.uk/Tools/webservices/psicquic/intact/webservices/current/search/query/id%3AQ9Y6K1?format=tab27&firstResult=0&maxResults=10000) was saved with its request, timestamp and SHA-256. Its 77 returned records were cross-matched by literal source PMID and partner accession; each matching record retains all 42 original fields. The counts below are records, not independent experiments.

| Source | Partner | Matching records | Scope |
| --- | --- | ---: | --- |
| 25416956 | P23497 SP100 | 3 | Discovery and validated Y2H |
| 25416956 | P56279 TCL1A | 3 | Discovery and validated Y2H |
| 31515488 | P56279 TCL1A | 2 | WT/variant Y2H; disruptive and nondisruptive variant features kept distinct |
| 32296183 | P32242 OTX1 | 3 | Discovery and validated Y2H |
| 32296183 | P56279 TCL1A | 5 | Multiple fusion configurations; not five independent physiological validations |
| 32296183 | Q6FHY5 historical MEOX2 clone | 4 | Y2H plus a separate complementation record |
| 32296183 | Q8N8E2 ZNF513 | 3 | Discovery and validated Y2H |
| 32296183 | Q99750 MDFI | 3 | Discovery and validated Y2H |
| 32814053 | O76024 WFS1 | 3 | Discovery and validated Y2H |
| 33961781 | P56279 TCL1A | 3 | AP-MS, including spoke expansion |
| 33961781 | Q9UBC3 DNMT3B | 1 | Non-expanded AP-MS record |

The Q6FHY5 parent/reference sequence differs from reviewed MEOX2 P50222 by deletion of Q81 outside the homeobox. This sequence comparison is separate from any annotated sufficient-binding region in an interaction record. The historical accession remains in the source annotation. Binary interaction and established transcription-factor class support only the bounded partner-class refinement; they do not establish shared promoter targets. WFS1 is retained despite its different normal compartment, because that difference does not negate the tested screening reagent.

## Propagation and contextual processes

The PANTHER family tree places the human target at PTN002507582 below all four relevant IBD assertions: PTN001497036/nucleus, PTN000552637/DNA-cytosine methyltransferase, and PTN002747444/cytoplasm and negative transcriptional regulation. The saved whole IBD GAF is dated 2026-08-28 and identifies PANTHER 19. Target self-evidence is legitimate descendant grounding. There is no donor-count or self-circularity objection.

Mouse and rat experimental donor records were joined separately to their publications. Mouse centromeric/pericentric localization, meiotic XY-body localization, Dum-lncRNA association, conditional cysteine automethylation and piRNA-linked germline methylation retain their organism and assay limits. The slow automethylation reaction is a conditional side activity, not a separate established human physiological core.

Exposure-associated expression is not automatically a role executed by DNMT3A. Full rat lead, folate/methyl-deficiency and ethanol studies support real changes in DNMT3A abundance or total methyltransferase activity, but do not isolate a DNMT3A-specific executing response mechanism. These are over-annotation judgments, not claims of false experiments. Several other exposure and hepatocyte-apoptosis sources remain abstract-only and are UNDECIDED. The rat oxygen-glucose-deprivation study is different: targeted Dnmt3a reduction changes injury outcomes, supporting a contextual hypoxic-injury role. None establishes direct oxygen sensing.

## Locations and Reactome paths

The current [HPA DNMT3A XML](https://www.proteinatlas.org/ENSG00000119772.xml) reports supported nucleoplasmic ICC/IF localization in A-431, U-251MG and U2OS cells. Its iPSC record adds vesicle staining. These records were inspected without interpreting image pixels or proposing an additional vesicle annotation. Nucleoplasm, whose definition excludes chromosomes, is kept distinct from chromatin-associated catalytic and reader functions. Broad nuclear refinements use target-level evidence and do not claim that every original source measured both pools.

The exact [DNMT3A entity R-HSA-212287](https://reactome.org/content/detail/R-HSA-212287) resolves to Q9Y6K1, residues 1–912, in nucleoplasm. Saved typed paths are:

- [212222](https://reactome.org/content/detail/R-HSA-212222) input → 212315 set → member 212287.
- [212269](https://reactome.org/content/detail/R-HSA-212269) catalystActivity → 212303 → physicalEntity 212288 → component 212315 → member 212287.
- [5212679](https://reactome.org/content/detail/R-HSA-5212679) input → 212287.
- [9710490](https://reactome.org/content/detail/R-HSA-9710490) catalystActivity → 212303 → physicalEntity 212288 → component 212315 → member 212287.

These are curated model assignments, not direct fractionation assays. The combined PRC2 event does not make DNMT3A a histone methyltransferase. Disagreement about H4R3me2s recognition is recorded separately from the location assertion.

## Access and quotation limits

Normal cache flags describe the stored cache, not every separately recovered source. In particular, the original normal caches for 17713477, 19786833, 19834512, 21976679 and 23042785 remain abstract-only even where full originals were separately read. The 16983096 cache's full-text flag does not supply its missing Methods/Results. The 25383530 recovery provides extended captions but not full main text. For 12138111, the specific nuclear-matrix assay remains unresolved; no experimental removal is based on its unavailable full text.

Four new short primary excerpts are used once each in the YAML, with reference-only support elsewhere: 19834512 (11 words), 19234465 (8 words), 32968275 (7 words), and 23435381 (15 words). Exact machine counts in the delivery ledger govern if typography changes tokenization. The two inherited core excerpts and pre-existing notes are inventoried separately; their preservation is not a claim that all historical repository quotations total at most 25 words. No newly reproduced source exceeds 25 words in aggregate. No quote in this guide is offered as independent primary evidence.
