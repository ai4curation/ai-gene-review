# DYRK1A source and assay guide

This guide gives source access, organism/construct and measurement limits for the reviewed assertions. It is an authored navigation aid; the primary papers and deposited records remain the evidence. Zero-based row indices refer to the 125-row review. No new verbatim paper quotation is reproduced.

## Decisive original locators

| Source | Operative location and access | Evidence boundary |
|---|---|---|
| [23665168](https://pubmed.ncbi.nlm.nih.gov/23665168/) | Original human DYRK structural and enzyme Methods/Results, independently read | Engineered human fragments establish substrate phosphorylation and weak mature tyrosine autophosphorylation; not every natural product assayed. |
| [25620562](https://doi.org/10.1016/j.molcel.2014.12.026) | Authentic institutional original PDF, biochemical/rescue Methods/Results and Figure 6 | CTD phosphorylation and polymerase occupancy have separable kinase dependence; no detected direct motif-DNA binding. Normal cache remains abstract-only. |
| [29849146](https://pubmed.ncbi.nlm.nih.gov/29849146/) | Original Methods/Results, genuine supplementary methods and Figure 3 | DYRK1A histidine-rich targeting and purified IDR behavior are distinguished from the cyclin-T1 cellular experiments. |
| [24820035](https://pmc.ncbi.nlm.nih.gov/articles/PMC4197879/) | H3 kinase/mutant assays and HP1/Brg1/expression Methods/Results | Phosphorylation-dependent chromatin regulation, not ATP-dependent remodeling-machine activity. |
| [24327345](https://pubmed.ncbi.nlm.nih.gov/24327345/) | Human-brain fractionation and splice-antibody/complex Methods/Results | Positive multiple pools; antibody splice fragments do not establish full-product equivalence. |
| [20736167](https://pmc.ncbi.nlm.nih.gov/articles/PMC2975161/) | Construct Methods, interaction/substrate and stress Results | Mouse expression reagents plus endogenous human PC3 association; host identity is not construct species. |
| [20167603](https://pmc.ncbi.nlm.nih.gov/articles/PMC2857074/) | SIRT1 kinase/association and cellular stress Methods/Results | Mouse SIRT reagents and combined DYRK1A/3 perturbation; no assignment of substrate deacetylase activity to DYRK1A. |
| [22767602](https://pmc.ncbi.nlm.nih.gov/articles/PMC3436298/) | SRp55 binding/phosphorylation, speckle localization and Tau exon-10 Results/Methods | Rat DYRK1A expression constructs versus endogenous human association are separated. |
| [21215488](https://pubmed.ncbi.nlm.nih.gov/21215488/) | SRSF7/9G8 association, phosphorylation and Tau-splicing Results/Methods | Rat enzyme; different exon-choice effects across COS, HEK and N2a contexts. |
| [28377597](https://pmc.ncbi.nlm.nih.gov/articles/PMC5428843/) | Kinase/construct Methods and Tau exon-10 Results | Rat DYRK1A and rodent models, with human cell hosts; exon choice rather than a universal splicing-rate increase. |
| [25556849](https://doi.org/10.1111/jnc.13018) | Indexed author-uploaded original Methods/Results and captions; authenticated title/DOI | Human recombinant kinase/Tau chemistry and human APP-output experiments; insoluble-Tau endpoint in rat neurons. Publisher download failed; no original PDF or image pixels claimed. |
| [30773093](https://pmc.ncbi.nlm.nih.gov/articles/PMC6464593/) | RNF169 kinase assays, overexpression/knockout/rescue and HR reporter Results/Methods | Opposite perturbation effects retained; mouse rescue construct and phosphosite-label discrepancies not harmonized by guesswork. |
| [31024071](https://pmc.ncbi.nlm.nih.gov/articles/PMC6483993/) | Endogenous human complex, DNA-damage and inhibitor-control Methods/Results | Early repair effects and inhibitor specificity limits; no direct accumulation of DYRK1A at RNF169 damage foci. |

The source-specific reference assessments below record body access independently of the normal cache flag. For PMID:23602568, authentic indexed main text and a supplemental validation caption were read, but complete Methods and all selected validation figures were not recovered. For PMID:25556849 the accessible original was an indexed author-uploaded manuscript; later papers displayed on that page were excluded. Original publication title/identifier verification does not certify an unresolved specific assay.

## Deposited interaction evidence

The [reproducible extracts](DYRK1A-evidence/README.md) retain original workbook rows, network attributes and CSV fields. The chromosome-21 Table S3 has multiple DYRK1A bait labels, including a polyhistidine deletion and a separately labeled isoforme3; none is silently mapped onto a current human natural product. Relevant imported pairs include worksheet rows 710 (WT/USP54), 724 (WT/FAM53C), 782 (delta-polyHis/DYNLL1), 819 (delta-polyHis/USP54) and 824 (delta-polyHis/TRAF2). Nucleotide prey boundaries, PBS values and original labels are preserved.

The induced-neuron mmc4 workbook contains twelve selected partner identities in Interaction_Annotations and matching Interactor_Lists rows. The Broad-specific rows and aggregate rows are not counted twice as independent evidence. The OpenCell DYNLL1-bait record is physical CSV line 7906 (zero-based data index 7904), with a mixed DYRK1A/DYRK1B prey group. The two selected 2025 graph edges point from LZTS2 or DCAF7 bait to DYRK1A prey.

IntAct and MINT source joins were checked by literal publication, target and partner identifiers, retaining method, host, feature and reference-sequence fields. Their absence for some historic rows is not a negative experiment. A sufficient-binding-region feature and a parent-sequence ROGID answer different questions; neither alone proves an archived bait is unmodified full length.

## Complete binding annotation index

The activity of the partner and the assay supporting the pair are checked separately. A class refinement is not a claim that DYRK1A performs the partner's activity. Ordinary project-supported generic binding remains non-core where no evidence-backed subclass was established.

| Row | Imported source | Partner | Disposition | Replacement |
|---|---|---|---|---|
| 21 | PMID:14500717 | RANBP9 / Q96S59 | MODIFY | GO:0097110 |
| 22 | PMID:14593110 | DCAF7 / P61962 | MODIFY | GO:0097110 |
| 23 | PMID:15694837 | PHYHIP / Q92561 | KEEP_AS_NON_CORE | — |
| 24 | PMID:20736167 | SPRED2 / Q7Z698 | KEEP_AS_NON_CORE | — |
| 25 | PMID:20736167 | SPRED1 / Q7Z699 | KEEP_AS_NON_CORE | — |
| 26 | PMID:20940704 | DCAF7 / P61962 | MODIFY | GO:0097110 |
| 27 | PMID:23602568 | RB1 / P06400 | MODIFY | GO:0001221 |
| 28 | PMID:23602568 | RBL1 / P28749 | MODIFY | GO:0001221 |
| 29 | PMID:23602568 | DCAF7 / P61962 | MODIFY | GO:0097110 |
| 30 | PMID:23602568 | DYNLL1 / P63167 | MODIFY | GO:0045503 |
| 31 | PMID:23602568 | TROAP / Q12815 | KEEP_AS_NON_CORE | — |
| 32 | PMID:23602568 | LZTS2 / Q9BRK4 | KEEP_AS_NON_CORE | — |
| 33 | PMID:23602568 | FAM53C / Q9NYF3 | KEEP_AS_NON_CORE | — |
| 34 | PMID:26949739 | TROAP / Q12815 | KEEP_AS_NON_CORE | — |
| 35 | PMID:26949739 | LZTS2 / Q9BRK4 | KEEP_AS_NON_CORE | — |
| 36 | PMID:27173435 | DCAF7 / P61962 | MODIFY | GO:0097110 |
| 37 | PMID:27705803 | DCAF7 / P61962 | MODIFY | GO:0097110 |
| 38 | PMID:30561431 | TRAF2 / Q12933 | MODIFY | GO:0031625 |
| 39 | PMID:32296183 | KPRP / Q5T749 | KEEP_AS_NON_CORE | — |
| 40 | PMID:32707033 | RB1 / P06400 | MODIFY | GO:0001221 |
| 41 | PMID:32707033 | RBL1 / P28749 | MODIFY | GO:0001221 |
| 42 | PMID:32707033 | DCAF7 / P61962 | MODIFY | GO:0097110 |
| 43 | PMID:33961781 | DCAF7 / P61962 | MODIFY | GO:0097110 |
| 44 | PMID:33961781 | DYNLL1 / P63167 | MODIFY | GO:0045503 |
| 45 | PMID:33961781 | USP54 / Q70EL1 | MODIFY | GO:1990381 |
| 46 | PMID:33961781 | LZTS2 / Q9BRK4 | KEEP_AS_NON_CORE | — |
| 47 | PMID:33961781 | FAM53C / Q9NYF3 | KEEP_AS_NON_CORE | — |
| 48 | PMID:35016035 | DCAF7 / P61962 | MODIFY | GO:0097110 |
| 49 | PMID:35271311 | DYNLL1 / P63167 | MODIFY | GO:0045503 |
| 50 | PMID:35914814 | DYNLL1 / P63167 | MODIFY | GO:0045503 |
| 51 | PMID:35914814 | TRAF2 / Q12933 | MODIFY | GO:0031625 |
| 52 | PMID:35914814 | USP54 / Q70EL1 | MODIFY | GO:1990381 |
| 53 | PMID:35914814 | FAM53C / Q9NYF3 | KEEP_AS_NON_CORE | — |
| 54 | PMID:36950384 | IGF2BP3 / O00425 | KEEP_AS_NON_CORE | — |
| 55 | PMID:36950384 | DCAF7 / P61962 | MODIFY | GO:0097110 |
| 56 | PMID:36950384 | DYNLL1 / P63167 | MODIFY | GO:0045503 |
| 57 | PMID:36950384 | SATB1 / Q01826 | MODIFY | GO:0140297 |
| 58 | PMID:36950384 | FMR1 / Q06787 | KEEP_AS_NON_CORE | — |
| 59 | PMID:36950384 | ELAVL2 / Q12926 | KEEP_AS_NON_CORE | — |
| 60 | PMID:36950384 | ELAVL3 / Q14576 | KEEP_AS_NON_CORE | — |
| 61 | PMID:36950384 | TRIP12 / Q14669 | MODIFY | GO:0031625 |
| 62 | PMID:36950384 | FAM53C / Q9NYF3 | KEEP_AS_NON_CORE | — |
| 63 | PMID:36950384 | IGF2BP1 / Q9NZI8 | KEEP_AS_NON_CORE | — |
| 64 | PMID:36950384 | ZMYND8 / Q9ULU4 | MODIFY | GO:0001221 |
| 65 | PMID:36950384 | IGF2BP2 / Q9Y6M1 | KEEP_AS_NON_CORE | — |
| 66 | PMID:40205054 | DCAF7 / P61962 | MODIFY | GO:0097110 |
| 67 | PMID:40205054 | LZTS2 / Q9BRK4 | KEEP_AS_NON_CORE | — |

## Propagation and compartment provenance

Five IBA records were joined to their exact PAINT IBD nodes in the actual PTHR24058 tree. The 1,390-node tree and 1,390-sequence MSA contain the target PTN002514217 and exact 763-residue human sequence. Target-path descent, not donor count or the mere presence of a family name, grounds the transfer. The transcription/coactivator ancestor includes experimental human DYRK1B evidence, supplemented by target-specific human CTD/chromatin studies. The target appearing among donors is valid experimental grounding.

Mouse and rat donor annotation records were inspected directly. Mouse nuclear-speckle support includes human/rat transfers and location-vocabulary mapping; it is not reported as an independently read mouse microscopy experiment. Mouse axon/dendrite IDA records cite PMID:21878370, whose complete target-specific body was unavailable. Rat splice-factor sources were recovered and read. This distinction preserves curator evidence without fabricating a source assay.

HPA target HTML, rather than its overall XML score, supplied individual-location reliability: supported nucleoplasm and nuclear speckles, uncertain centrosome and cytosol. These uncertain calls are not used to negate separate positive cytoplasmic evidence or add a new centrosomal assertion.

Reactome R-HSA-1362270 was traced through catalytic activity 1362272 to human DYRK1A entity 1362267, residues 1–763 in nucleoplasm, and the LIN52 phosphorylation step. The existing DNA-repair GO-CAM 617b481400003575 was considered alongside the actual RNF169 experiments; a curator-modeled positive branch does not erase opposite knockout results.

## Reference access inventory

The full source-specific assessments are recorded once in the review YAML. Body access below records the actual operative original or database record, not just the machine-cache flag. It does not imply that all supplementary files or image pixels were read.

| Reference | Relevance | Access |
|---|---|---|
| GO_REF:0000002 | LOW | Method record |
| GO_REF:0000024 | LOW | Method record |
| GO_REF:0000033 | LOW | Method record |
| GO_REF:0000044 | LOW | Method record |
| GO_REF:0000052 | LOW | Method record |
| GO_REF:0000108 | LOW | Method record |
| GO_REF:0000116 | LOW | Method record |
| GO_REF:0000120 | LOW | Method record |
| [PMID:14500717](https://pubmed.ncbi.nlm.nih.gov/14500717/) | HIGH | Original-body gap |
| [PMID:14593110](https://pubmed.ncbi.nlm.nih.gov/14593110/) | HIGH | Original-body gap |
| [PMID:15694837](https://pubmed.ncbi.nlm.nih.gov/15694837/) | HIGH | Original-body gap |
| [PMID:17906291](https://pubmed.ncbi.nlm.nih.gov/17906291/) | HIGH | Original-body gap |
| [PMID:20167603](https://pubmed.ncbi.nlm.nih.gov/20167603/) | HIGH | Operative source accessed |
| [PMID:20736167](https://pubmed.ncbi.nlm.nih.gov/20736167/) | HIGH | Operative source accessed |
| [PMID:20940704](https://pubmed.ncbi.nlm.nih.gov/20940704/) | HIGH | Operative source accessed |
| [PMID:20981014](https://pubmed.ncbi.nlm.nih.gov/20981014/) | HIGH | Original-body gap |
| [PMID:22998443](https://pubmed.ncbi.nlm.nih.gov/22998443/) | MEDIUM | Original-body gap |
| [PMID:23415227](https://pubmed.ncbi.nlm.nih.gov/23415227/) | MEDIUM | Original-body gap |
| [PMID:23602568](https://pubmed.ncbi.nlm.nih.gov/23602568/) | HIGH | Operative source accessed |
| [PMID:23665168](https://pubmed.ncbi.nlm.nih.gov/23665168/) | HIGH | Operative source accessed |
| [PMID:24239188](https://pubmed.ncbi.nlm.nih.gov/24239188/) | MEDIUM | Original-body gap |
| [PMID:24327345](https://pubmed.ncbi.nlm.nih.gov/24327345/) | HIGH | Operative source accessed |
| [PMID:24820035](https://pubmed.ncbi.nlm.nih.gov/24820035/) | HIGH | Operative source accessed |
| [PMID:25556849](https://pubmed.ncbi.nlm.nih.gov/25556849/) | HIGH | Operative source accessed |
| [PMID:25620562](https://pubmed.ncbi.nlm.nih.gov/25620562/) | HIGH | Operative source accessed |
| [PMID:26949739](https://pubmed.ncbi.nlm.nih.gov/26949739/) | HIGH | Operative source accessed |
| [PMID:27173435](https://pubmed.ncbi.nlm.nih.gov/27173435/) | HIGH | Operative source accessed |
| [PMID:27705803](https://pubmed.ncbi.nlm.nih.gov/27705803/) | MEDIUM | Original-body gap |
| [PMID:28377597](https://pubmed.ncbi.nlm.nih.gov/28377597/) | HIGH | Operative source accessed |
| [PMID:28386764](https://pubmed.ncbi.nlm.nih.gov/28386764/) | MEDIUM | Operative source accessed |
| [PMID:29849146](https://pubmed.ncbi.nlm.nih.gov/29849146/) | HIGH | Operative source accessed |
| [PMID:30561431](https://pubmed.ncbi.nlm.nih.gov/30561431/) | HIGH | Operative source accessed |
| [PMID:30773093](https://pubmed.ncbi.nlm.nih.gov/30773093/) | HIGH | Operative source accessed |
| [PMID:32296183](https://pubmed.ncbi.nlm.nih.gov/32296183/) | MEDIUM | Operative source accessed |
| [PMID:32707033](https://pubmed.ncbi.nlm.nih.gov/32707033/) | HIGH | Operative source accessed |
| [PMID:33961781](https://pubmed.ncbi.nlm.nih.gov/33961781/) | HIGH | Operative source accessed |
| [PMID:35016035](https://pubmed.ncbi.nlm.nih.gov/35016035/) | MEDIUM | Original-body gap |
| [PMID:35271311](https://pubmed.ncbi.nlm.nih.gov/35271311/) | HIGH | Operative source accessed |
| [PMID:35914814](https://pubmed.ncbi.nlm.nih.gov/35914814/) | HIGH | Operative source accessed |
| [PMID:36950384](https://pubmed.ncbi.nlm.nih.gov/36950384/) | HIGH | Operative source accessed |
| [PMID:40205054](https://pubmed.ncbi.nlm.nih.gov/40205054/) | HIGH | Operative source accessed |
| [PMID:8769099](https://pubmed.ncbi.nlm.nih.gov/8769099/) | HIGH | Original-body gap |
| [PMID:8975710](https://pubmed.ncbi.nlm.nih.gov/8975710/) | HIGH | Original-body gap |
| [PMID:9070862](https://pubmed.ncbi.nlm.nih.gov/9070862/) | MEDIUM | Original-body gap |
| [PMID:9748265](https://pubmed.ncbi.nlm.nih.gov/9748265/) | HIGH | Original-body gap |
| [Reactome:R-HSA-1362270](https://reactome.org/content/detail/R-HSA-1362270) | HIGH | Operative source accessed |
| [PMID:11980910](https://pubmed.ncbi.nlm.nih.gov/11980910/) | MEDIUM | Original-body gap |
| [PMID:8631952](https://pubmed.ncbi.nlm.nih.gov/8631952/) | MEDIUM | Original-body gap |
| [PMID:21215488](https://pubmed.ncbi.nlm.nih.gov/21215488/) | HIGH | Operative source accessed |
| [PMID:22767602](https://pubmed.ncbi.nlm.nih.gov/22767602/) | HIGH | Operative source accessed |
| [PMID:21878370](https://pubmed.ncbi.nlm.nih.gov/21878370/) | MEDIUM | Original-body gap |
| [PMID:20123978](https://pubmed.ncbi.nlm.nih.gov/20123978/) | MEDIUM | Operative source accessed |
| [PMID:31024071](https://pubmed.ncbi.nlm.nih.gov/31024071/) | HIGH | Operative source accessed |
| [PMID:21127067](https://pubmed.ncbi.nlm.nih.gov/21127067/) | HIGH | Operative source accessed |
| [https://www.proteinatlas.org/ENSG00000157540-DYRK1A/subcellular](https://www.proteinatlas.org/ENSG00000157540-DYRK1A/subcellular) | MEDIUM | Operative source accessed |

## Official partner identities

The binding index above identifies the exact partner accession for every row. These directly read official records establish the partner class, separately from the source experiment establishing association. The record and the source-specific review reason disclose inferred versus direct activity support.

- [Q96S59: Ran-binding protein 9](https://www.uniprot.org/uniprotkb/Q96S59/entry).
- [P61962: DDB1- and CUL4-associated factor 7](https://www.uniprot.org/uniprotkb/P61962/entry).
- [Q92561: Phytanoyl-CoA hydroxylase-interacting protein](https://www.uniprot.org/uniprotkb/Q92561/entry).
- [Q7Z698: Sprouty-related, EVH1 domain-containing protein 2](https://www.uniprot.org/uniprotkb/Q7Z698/entry).
- [Q7Z699: Sprouty-related, EVH1 domain-containing protein 1](https://www.uniprot.org/uniprotkb/Q7Z699/entry).
- [P06400: Retinoblastoma-associated protein](https://www.uniprot.org/uniprotkb/P06400/entry).
- [P28749: Retinoblastoma-like protein 1](https://www.uniprot.org/uniprotkb/P28749/entry).
- [P63167: Dynein light chain 1, cytoplasmic](https://www.uniprot.org/uniprotkb/P63167/entry).
- [Q12815: Tastin](https://www.uniprot.org/uniprotkb/Q12815/entry).
- [Q9BRK4: Leucine zipper putative tumor suppressor 2](https://www.uniprot.org/uniprotkb/Q9BRK4/entry).
- [Q9NYF3: Protein FAM53C](https://www.uniprot.org/uniprotkb/Q9NYF3/entry).
- [Q12933: TNF receptor-associated factor 2](https://www.uniprot.org/uniprotkb/Q12933/entry).
- [Q5T749: Keratinocyte proline-rich protein](https://www.uniprot.org/uniprotkb/Q5T749/entry).
- [Q70EL1: Ubiquitin carboxyl-terminal hydrolase 54](https://www.uniprot.org/uniprotkb/Q70EL1/entry).
- [O00425: Insulin-like growth factor 2 mRNA-binding protein 3](https://www.uniprot.org/uniprotkb/O00425/entry).
- [Q01826: DNA-binding protein SATB1](https://www.uniprot.org/uniprotkb/Q01826/entry).
- [Q06787: Fragile X messenger ribonucleoprotein 1](https://www.uniprot.org/uniprotkb/Q06787/entry).
- [Q12926: ELAV-like protein 2](https://www.uniprot.org/uniprotkb/Q12926/entry).
- [Q14576: ELAV-like protein 3](https://www.uniprot.org/uniprotkb/Q14576/entry).
- [Q14669: E3 ubiquitin-protein ligase TRIP12](https://www.uniprot.org/uniprotkb/Q14669/entry).
- [Q9NZI8: Insulin-like growth factor 2 mRNA-binding protein 1](https://www.uniprot.org/uniprotkb/Q9NZI8/entry).
- [Q9ULU4: MYND-type zinc finger-containing chromatin reader ZMYND8](https://www.uniprot.org/uniprotkb/Q9ULU4/entry).
- [Q9Y6M1: Insulin-like growth factor 2 mRNA-binding protein 2](https://www.uniprot.org/uniprotkb/Q9Y6M1/entry).
- [Q13627: Dual specificity tyrosine-phosphorylation-regulated kinase 1A](https://www.uniprot.org/uniprotkb/Q13627/entry).
