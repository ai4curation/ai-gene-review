# DDX41 source and assay guide

This guide separates the imported annotation, the observation inspected, and the scope of the inference. Normal publication caches retain their original bytes and access flags. A false `full_text_available` value in a cache does not mean that a separately recovered original was unavailable.

## Identity and products

- Official human identity: [UniProt Q9UJV9](https://www.uniprot.org/uniprotkb/Q9UJV9/entry), HGNC:18674, 622 amino acids; no declared alternative product.
- PMID:26712909 suggests M132/M155 as possible starts of a smaller translation species but does not resolve its sequence. The later engineered 127–622 deletion is not a curated native product.
- Expression host, canonical record checksum, construct sequence and native isoform are different facts. A human-cell host does not establish an unspecified construct's species; an HTT checksum does not establish a full-length HTT construct.

## Original sources and stable locators

| Source | Actual inspected evidence | Access and scope |
|---|---|---|
| [11991638](https://pubmed.ncbi.nlm.nih.gov/11991638/) | Original Results complex assembly and Table 1, “Proteins found only in C complex”: Abstrakt/Q9UJV9; HeLa extract, AdML AG-to-GG substrate, native C-complex purification. | [Indexed original copy](https://www.researchgate.net/publication/11378078_Purification_and_characterization_of_native_spliceosomes_suitable_for_three-dimensional_structural_analysis) yielded the target table and methods window. Complete original download was not recovered. No specific DDX41 catalytic reaction follows from proteomic membership. |
| [21892174](https://pubmed.ncbi.nlm.nih.gov/21892174/) | [Original](https://pmc.ncbi.nlm.nih.gov/articles/PMC3671854/), DNA-binding experiments and ER/localization sections. | Human THP1 and mouse dendritic-cell observations are separated; recombinant binding and deletion experiments are distinguished from cellular necessity. Exact construct species is not guessed from host cells. |
| [23142775](https://pubmed.ncbi.nlm.nih.gov/23142775/) | [Original](https://pmc.ncbi.nlm.nih.gov/articles/PMC3501571/), cyclic-dinucleotide binding, competition and cellular-response experiments. | Mouse D2SC/BMDC/macrophage and human THP1/PBMC systems are distinct. Supplemental construct details not recovered are left unresolved. |
| [22365833](https://pubmed.ncbi.nlm.nih.gov/22365833/) | Original spliceosome-interaction screening methods; MINT target pair records ST3/ST6. | Human DDX41–NKAP two-hybrid and HEK293 anti-tag co-IP; association does not demonstrate DDX41 transcriptional repression. |
| [22658674](https://pubmed.ncbi.nlm.nih.gov/22658674/) | Original page 1394, “In Vivo Capture of HeLa RBPs,” and supplementary methods. | [Original plus supplement](https://rnajc.ucsf.edu/sites/rnajc.ucsf.edu/files/CastelloArticlePlusSupplementalJune2012.pdf) describes UV crosslinking, stringent oligo(dT) capture, RNase release and MS. Separate Table S1 was not recovered: target assignment is deferred to the curator, with independent CLIP corroboration. |
| [23222971](https://pubmed.ncbi.nlm.nih.gov/23222971/) | Original DDX41–TRIM21 association and expressed-protein localization experiments. | Tagged human-cell cytoplasmic colocalization does not independently resolve a soluble cytosolic fraction. TRIM21 performs ubiquitination. |
| [25416956](https://pubmed.ncbi.nlm.nih.gov/25416956/) | Original Results describing pairwise quadruplicate testing from fresh yeast colonies. | Identity-confirmed pairs were retained after at least three positive attempts. The literal SIAH1 and CEP70 records were assessed; orthogonal validation of the study set is not claimed for every individual pair. |
| [25920683](https://pubmed.ncbi.nlm.nih.gov/25920683/) | Original human splicing/association experiments and hematopoietic phenotypes. | Human K562/CD34+/U937/HEK293 evidence and mouse LSK observations are kept distinct. Neither RNA association nor perturbation directly measures RNA helicase activity. |
| [26030138](https://pmc.ncbi.nlm.nih.gov/articles/PMC4451243/) | Results “Validation of CSB interacting proteins by reciprocal co-immunoprecipitation,” and Fig. 5. | DDX41–CSB co-precipitation occurs with anti-Myc but not anti-FLAG in human CSIAN lysates. The weak-interaction negative-control example for SMARCA2 is not misdescribed as a DDX41-specific control. |
| [26712909](https://pubmed.ncbi.nlm.nih.gov/26712909/) | Original full-length/localization and M1I smaller-product experiments. | Full-length WT/R525H/R164W nuclear localization is distinguished from unresolved alternative initiation. |
| [28514442](https://pmc.ncbi.nlm.nih.gov/articles/PMC5531611/) | “Clone Construction and Cell Culture,” “Affinity-Purification Mass Spectrometry,” and background filtering. | C-terminal HA-FLAG constructs and cellular co-purification; the NKAP–DDX41 record is HEK293T. |
| [32296183](https://pmc.ncbi.nlm.nih.gov/articles/PMC7169983/) | “Generation and characterization of HuRI”: quadruplicate retesting, sequence confirmation and three assay configurations. | NKAPL and AIDA are exact positive pairs; the record does not establish DDX41's native physiological role with either partner. |
| [32703943](https://pmc.ncbi.nlm.nih.gov/articles/PMC7378245/) | Original FAM50A/DDX41 co-IP and cloning methods. | Sequence-confirmed full-length V5-DDX41 with endogenous FAM50A in U-87 MG cells; absence of a fresh MITAB match does not erase the original experiment. |
| [32814053](https://pubmed.ncbi.nlm.nih.gov/32814053/) | Original Results interaction-mating workflow and “Automated Y2H interaction screening,” ending before “PPI detection in cells using DULIP and LuTHy.” | [Complete original PDF](https://orbilu.uni.lu/bitstream/10993/55953/1/1-s2.0-S2211124720310354-main.pdf) recovered; literal HTT fragment features remain in the MITAB records. Native neuronal complexes and full-length HTT binding were not established by these records. |
| [33961781](https://pubmed.ncbi.nlm.nih.gov/33961781/) | Original construct, AP-MS and CompPASS-Plus methods. | Separate HEK293T/HCT116 target records preserve bait orientation. Co-complex recovery is not purified binary binding. |
| [33650667](https://pubmed.ncbi.nlm.nih.gov/33650667/) | Independently reviewed human expression and alternative-splicing experiments. | Perturbation does not identify an RNA-duplex-unwinding reaction. |
| [34473945](https://pubmed.ncbi.nlm.nih.gov/34473945/) | Independently reviewed snoRNA-associated RNA processing, human fusion assays and mouse hematopoietic alleles. | HyperTRIBE fusion/replication limits remain; downstream pseudouridylation and protein-synthesis effects do not assign those catalytic reactions to DDX41. |
| [35613581](https://pubmed.ncbi.nlm.nih.gov/35613581/) | Original Fig. 3 substrate assays; Fig. 4M nuclear/cytosol fractionation; cGAS/STING response experiments. | Tested RNA duplexes are negative, DNA unwinding is ATP dependent, and annealing is ATP independent. Intracellular remodeling balance is a model; cGAS makes cGAMP. |
| [36229594](https://pubmed.ncbi.nlm.nih.gov/36229594/) | Independently reviewed K562 UV-CLIP, spliceosome/transcription-factor associations and elongation experiments. | RNA binding near 5-prime splice sites does not by itself prove mature-mRNA-only binding; no purified RNA-duplex unwinding was measured. |

The original target table for PMID:22681889 and localization assay for PMID:25704810 remain unavailable; their RNA-binding and cytoplasmic-location claims are accepted with independent target evidence and curator deference. PMID:10607561 and PMID:19946888 retain unresolved annotation judgments after bounded recovery attempts. PMID:36780110 was assessed only at abstract level and is not used to assign a direct translation activity.

## Literal interaction records and partner classes

All row numbers below are zero-based imported annotation indices. Records were selected by target, partner and PMID, with both human identities and sequence/taxon checksums checked. The multiple records of one pair describe assay stages or contexts, not independent physiological mechanisms.

| Rows | Pair and literal anchor | Interpretation |
|---|---|---|
| 12 | DDX41–NKAP; MINT-8337673 / MINT-8331403 | Two-hybrid and anti-tag co-IP; GO:0001222 transcription corepressor binding. |
| 13 | DDX41–SIAH1; EBI-10581902 plus pooling/array records | GO:0031625 ubiquitin protein ligase binding. |
| 14 | DDX41–CEP70; EBI-10592580 plus pooling/array records | Positive non-core binding; no DDX41 centrosomal or microtubule mechanism inferred. |
| 15 | DDX41–ERCC6/CSB; original Fig. 5 | GO:0051117 ATPase binding; asymmetric co-IP retained. |
| 16 | NKAP–DDX41; EBI-21520423 | HEK293T AP-MS, tagged NKAP; GO:0001222. |
| 17 | NKAPL–DDX41; EBI-24640582 and four stage/configuration records | Non-core binding; human NKAPL's repression function is assigned by similarity, distinct from the directly supported NKAP class. |
| 18 | AIDA–DDX41; EBI-25270277 plus pooling/array records | Non-core binding without a DDX41 adaptor or signaling mechanism. |
| 19 | FAM50A–DDX41; original human-cell co-IP | Non-core association; no catalytic activity inferred. |
| 20 | HTT–DDX41; EBI-25957757, EBI-26126967, EBI-26112095, EBI-25972744, EBI-26281098, EBI-26266228 | HTT regions 1–511 and 1932–2642; polyglutamine/mutation features retained in source records. |
| 21 | DDX41–NKAP EBI-54702916; NKAP–DDX41 EBI-54932614 | HEK293T/HCT116 AP-MS respectively; GO:0001222. |

The binding refinements use the actual [NKAP FUNCTION record](https://www.uniprot.org/uniprotkb/Q8N5F7/entry), [SIAH1 catalytic record](https://www.uniprot.org/uniprotkb/Q8IUQ4/entry), [ERCC6 catalytic record](https://www.uniprot.org/uniprotkb/Q03468/entry), and current definitions of [GO:0001222](https://www.ebi.ac.uk/QuickGO/term/GO:0001222), [GO:0031625](https://www.ebi.ac.uk/QuickGO/term/GO:0031625) and [GO:0051117](https://www.ebi.ac.uk/QuickGO/term/GO:0051117). The current human NKAP FUNCTION record explicitly states “Plays a role as a transcriptional corepressor” and cites [PMID:19409814](https://pubmed.ncbi.nlm.nih.gov/19409814/) for its Notch-associated role. This is an experimentally curated partner-class assertion, not a claim that DDX41 mediates repression. GO:0001222 describes binding to a corepressor; it does not require that the observed interaction occur during transcription. Partner-function full originals were not separately reread for this class assessment. The generic thioester-E3 wording in SIAH1's FUNCTION prose is not used as a RING-ligase mechanism.

## Propagation and localization

The actual target lineage runs through mRNA-binding node PTN002776867, RNA-helicase node PTN002774595 and DDX41-related spliceosomal node PTN002776089 to leaf PTN002776112. Current IBD rows and donor experimental annotations were inspected. The RNA-helicase question concerns target substrate specificity, not weak donor count or illegitimate self-reference. No residue-loss argument was made.

The literal InterPro rules are IPR011545 to nucleic-acid/ATP binding, IPR014014 to RNA helicase, and IPR044113 to RNA helicase/ATP binding/splicing. Their individual assertions are assessed separately. RHEA:13065 supplies ATP hydrolysis, which agrees with target biochemistry.

HPA reports nucleoplasm as the main localization and nucleoli as an additional localization. Reactome human entity R-HSA-9769601 resolves to Q9UJV9 in nucleoplasm and is explicitly included in C-star/P complexes and release events. R-HSA-3134807 resolves to Q9UJV9 in cytosol and appears in DNA/cyclic-dinucleotide binding and TRIM21 ubiquitination events. These are localization assertions; no other component's catalytic activity is transferred.

## Review policy and research provenance

The [standing project instruction](https://github.com/ai4curation/ai-gene-review/blob/a87ae568676c4012ea4abe5393967aeff1b52ae7/projects/CLINGEN_MENDELIAN.md#curation-instructions) retains supported positive binding as non-core where a justified more informative term is unavailable. Broad terms with justified replacements use MODIFY even when another source row already carries that term. No new process or molecular-function row was required for the two cores; RNA binding, splicing, DNA-helicase refinement and cGAS/STING participation already have reviewed source coverage.

Normal fetch and PMID retrieval completed. Falcon authentication and its configured fallback's quota failed terminally, so manual primary-source work supplied the review and no provider-named report was fabricated. Original machine caches were preserved, and two additional primary sources, 21892174 and 23142775, were fetched through the normal CLI. Six short cache-verbatim quotations now anchor the substrate correction, ATP hydrolysis, cytosolic fractionation and RNA/splicing functions. Each appears once in the YAML. The exact NKAP FUNCTION quotation above provides the separate partner-class evidence.

The nuclear core retains the encompassing spliceosomal-complex term because the evidence spans C-complex identification and activated-spliceosome association. The more specific catalytic step 2 spliceosome annotation remains accepted; the broader core summary does not assert that every observed DDX41 spliceosome association is restricted to that single stage.
