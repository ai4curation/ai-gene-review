# GPAM notes


## 2026-09-08 paired review

Selected accession A0A9L0TTC1; ordinary UniProt record is TrEMBL and cites genome sequencing/submission rather than a gene-specific functional experiment. Human evidence is summarized in [the paired human investigation](../../human/GPAM/GPAM-notes.md). [Sequence comparison](GPAM-bioinformatics/RESULTS.md) records the exact target gaps and transfer limits. The targeted Europe PMC search found no decisive gene-specific horse functional assay warranting a separate horse Edison investigation; general omics/association hits were not counted as mechanistic validation.

The substrate donor is acyl-CoA and the acceptor is the sn-1 hydroxyl of glycerol-3-phosphate. Lysophosphatidic acid enters several glycerolipid routes, so pathway participation is broader than the one catalyzed reaction. The 2023 structural work reports an N-terminal catalytic domain and associated C-terminal domain, and replaces a conventional multi-pass-transmembrane picture with an amphipathic surface/N-terminal loop-helix membrane association mechanism. The UniProt record links this reaction to direct experimental sources; the acyl-CoA statement is therefore not an ARBA corroboration. Papers mainly describing another GPAT paralog may include GPAT1 comparator assays, so title alone cannot justify discarding their GO annotations.

Sources: [PMID:36522428](https://pubmed.ncbi.nlm.nih.gov/36522428/), [PMID:18238778](https://pubmed.ncbi.nlm.nih.gov/18238778/), [PMID:19075029](https://pubmed.ncbi.nlm.nih.gov/19075029/).

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

**Deep research.** `just deep-research-falcon HORSE GPAM --fallback perplexity-lite` failed (falcon: "Failed to authenticate"; perplexity fallback: HTTP 401 insufficient quota). No horse deep-research file exists; literature context comes from the human GPAM review, its falcon report (`genes/human/GPAM/GPAM-deep-research-falcon.md`), the human Swiss-Prot record and PMID:36522428.

**Identity of the benchmark accession.** A0A9L0TTC1 (790 aa) is NOT the canonical horse GPAM product. The UniProt horse reference proteome labels it "Isoform of A0A9L0TCA8"; A0A9L0TCA8 (828 aa, same length as human Q9HCL2) is the gene-centric canonical entry. Ensembl gene ENSECAG00000014742 has nine protein-coding transcripts; A0A9L0TTC1 is ENSECAT00000105322 (the Ensembl-canonical transcript is ENSECAT00000137388 = A0A9L0TA25, 900 aa). A0A9L0TTC1 lacks an in-frame 38-residue segment equivalent to human 370-407, which is conserved in human, mouse, rat and canonical horse GPAM and which in the human cryo-EM structure contains resolved catalytic-domain secondary structure (helix 380-390, strand 396-400, helices 401-403, 406-415). The HXXXXD motif, all six CoA-binding residues and the mitochondrial-localization region are retained. Activity of this isoform is untested. See [RESULTS-rereview.md](GPAM-bioinformatics/RESULTS-rereview.md).

**Evolutionary grounding.** PANTHER PTHR12563:SF16 (same subfamily as human GPAM). PAINT node PTN000970957 (Eumetazoa) carries IBD for GO:0004366, GO:0005739, GO:0006650 and GO:0019432; horse descends from it. No plasma-membrane term at any metazoan node; the plasma-membrane IEA derives from IPR028354 (GPAT_PlsB), shared with bacterial PlsB.

**Changes vs previous review.**
- gene_symbol corrected from the accession to GPAM.
- Description rewritten (project-independent; records the isoform status).
- GO:0006629 lipid metabolic process: ACCEPT -> MODIFY to GO:0019432 + GO:0008654 (correct-but-general rule; differs from the human review, which accepted it).
- GO:0031966 mitochondrial membrane: KEEP_AS_NON_CORE -> MODIFY to GO:0005741 (previous reason argued it was too general).
- GO:0004366, GO:0005741, GO:0008654, GO:0016024: ACCEPT, with gene-level/isoform caveat; GO:0005886 plasma membrane: REMOVE (bacterial PlsB mapping); GO:0016746/GO:0016747: MODIFY to GO:0004366.
- Support now cites PAINT/subfamily placement and feature retention (RESULTS-rereview.md) and the human Swiss-Prot curated text instead of a pairwise-identity statement; the older RESULTS.md is kept but no longer cited.
- core_functions adds triglyceride and phospholipid biosynthetic process as directly_involved_in; one suggested question and one experiment on the isoform.

**Next relative.** Canonical horse GPAM A0A9L0TCA8 has no review in the repo; its folder would be `genes/HORSE/GPAM__A0A9L0TCA8`. The PTHR12563 family review lists A0A9L0TTC1 as an SF16 representative; subfamily placement agrees, but the canonical A0A9L0TCA8 would be a better representative.

**Modules.** `modules/triacylglycerol_biosynthesis.yaml` (GPAM is the animal G3P-acylation annoton, grounded on human Q9HCL2).
