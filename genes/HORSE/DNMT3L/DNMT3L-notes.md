# DNMT3L notes


## 2026-09-08 paired review

Selected accession A0A9L0T837; ordinary UniProt record is TrEMBL and cites genome sequencing/submission rather than a gene-specific functional experiment. Human evidence is summarized in [the paired human investigation](../../human/DNMT3L/DNMT3L-notes.md). [Sequence comparison](DNMT3L-bioinformatics/RESULTS.md) records the exact target gaps and transfer limits. The targeted Europe PMC search found no decisive gene-specific horse functional assay warranting a separate horse Edison investigation; general omics/association hits were not counted as mechanistic validation.

DNMT3L is related to de novo DNA methyltransferases but lacks the complete machinery of an active methyltransferase. The 2002 primary study demonstrates interaction with HDAC1, recruitment of deacetylase activity and HDAC-dependent repression, while the 2006 biochemical/cell study shows stimulation of DNMT3B and the importance of its interaction interface. These support enzyme activation and gene regulation independently of a catalytic DNA-methylation claim. Chromatin localization, imprinting, transposon repression and germ-cell developmental consequences should be distinguished by level of mechanism. The selected horse protein covers the entire human sequence and retains its ADD/chromatin-interaction architecture; its N-terminal extension is not an absence of the human core.

Sources: [PMID:12202768](https://pubmed.ncbi.nlm.nih.gov/12202768/), [PMID:16543361](https://pubmed.ncbi.nlm.nih.gov/16543361/).

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 output was not consulted. Deep research (`just deep-research-falcon HORSE DNMT3L --fallback perplexity-lite`) failed: falcon and the perplexity-lite fallback both exited non-zero, and no deep-research file was produced. The review is based on cached primary literature read directly.

### Identity of the benchmark accession
- A0A9L0T837 (426 aa, TrEMBL) is the Ensembl-canonical product (ENSECAT00000080350 / ENSECAP00000084444) of horse DNMT3L (ENSECAG00000009690). The second Ensembl model, F6YVL8 (403 aa, ENSECAT00000010000), is identical over the first 351 residues. It lacks 4 residues (RRDV) and the conserved C-terminal tail. No Swiss-Prot horse entry exists. [file:HORSE/DNMT3L/DNMT3L-bioinformatics/RESULTS-rereview.md]
- Against human Q9UJW3 (386 aa): 77.7% identity, 100% human coverage. The extra 40 N-terminal horse residues correspond to an extension that mouse Q9CWR8 also has, so this is not a fragment or artefact. All human ADD-domain cysteines are conserved, and human F261 (DNMT3A interface; F261A abolishes binding, PMID:17713477) = horse F301.
- PANTHER PTHR23068:SF13 (DNMT3L subfamily), the same subfamily as human and mouse DNMT3L. The family review interpro/panther/PTHR23068/PTHR23068-review.yaml places A0A9L0T837 in SF13 as well, so there is no disagreement about placement.

### Key evidence (mouse/human orthologs, same subfamily)
- Maternal imprint establishment requires Dnmt3L [PMID:11719692 "removal of Dnmt3L prevented methylation of sequences that are normally maternally methylated"; PMID:11934864].
- Retrotransposon de novo methylation in prospermatogonia [PMID:15318244 "Deletion of the Dnmt3L gene prevented the de novo methylation of both long-terminal-repeat (LTR) and non-LTR retrotransposons"]. The same paper reports that spermatocytes "do not express Dnmt3L", so the meiotic failure is indirect.
- Stimulates DNMT3A/3B through its C-terminal domain, acting as a substrate exchange factor [PMID:15671018]. Forms a heterotetramer in which DNMT3A/3B provide the two active sites [PMID:17713477].
- The ADD domain reads H3 tails unmethylated at K4 [PMID:17687327].
- In ESCs it antagonises methylation at bivalent promoters by competing with DNMT3A/3B for PRC2 [PMID:24074865]. This is a single study.

### Changes vs previous review
- gene_symbol corrected from A0A9L0T837 to DNMT3L. Description rewritten.
- male meiosis I: REMOVE (indirect phenotype; DNMT3L is absent from spermatocytes).
- DNA methylation-dependent constitutive heterochromatin formation: MODIFY to GO:0141196 (pericentric tandem repeats are methylated normally in nulls).
- catalytic complex: MODIFY to GO:0140020 DNA methyltransferase complex.
- heterochromatin, condensed nuclear chromosome: ACCEPT changed to KEEP_AS_NON_CORE.
- ESC/E(Z) complex and negative regulation of DNA methylation-dependent heterochromatin formation: UNDECIDED changed to KEEP_AS_NON_CORE, now that the mouse IDA/IMP source (PMID:24074865) has been traced.
- stem cell differentiation: MARK_AS_OVER_ANNOTATED.
- negative regulation of DNA-templated transcription (IBA): KEEP_AS_NON_CORE.
- NEW: GO:0140006 histone H3 reader activity (ISS from the human/mouse ADD-domain structure). This is DNMT3L's own binding activity, not a process it is needed for.

### Relative
Human DNMT3L (Q9UJW3) is in the same SF13 subfamily, is the structurally and biochemically characterised ortholog, and is the donor of the PAINT DNMT3L node PTN001891074. genes/human/DNMT3L/ has a review marked COMPLETE, but its rationales are the same generic boilerplate this horse review used to have. For example, it keeps male meiosis I as non-core (KEEP_AS_NON_CORE), leaves ESC/E(Z) complex and GO:0090310 UNDECIDED, and leaves the six protein-binding IPIs UNDECIDED. It would benefit from the same re-review. Mouse Dnmt3l (Q9CWR8) carries most of the genetic evidence and has no review in the repository.

Modules: modules/pirna_mediated_germline_silencing.yaml mentions DNMT3L.
