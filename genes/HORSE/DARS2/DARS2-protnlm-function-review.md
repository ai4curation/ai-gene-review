# DARS2: ProtNLM function-description review

Selected horse accession: [A0A9L0SB67](https://www.uniprot.org/uniprotkb/A0A9L0SB67/entry). Source: ProtNLM2 API snapshot 2026-09-08, frozen in [horse40-predictions.csv](../../../../projects/PROTNLM_EVALUATION/mammal-benchmark/horse40-predictions.csv).

## Exact model output

> Aspartyl-tRNA synthetase with relaxed tRNA specificity since it is able to aspartylate not only its cognate tRNA(Asp) but also tRNA(Asn). Reaction proceeds in two steps: L-aspartate is first activated by ATP to form Asp-AMP and then transferred to the acceptor end of tRNA(Asp/Asn)

## Claim-level assessment

### Attachment of aspartate to cognate tRNA(Asp)

**UNC for this selected sequence.** Biochemical characterization and the human enzyme structure support mitochondrial aspartate-tRNA ligase function, using ATP activation followed by transfer to tRNA. The activity is not novel for the horse gene: the gene-centric horse DARS2 product A0A3Q2HM61 already carries aspartate-tRNA ligase activity (GO:0004815) in GOA. A0A9L0SB67 is an exon-skipping isoform of the same gene that lacks human residues 341–376 [(gene-model comparison)](DARS2-bioinformatics/RESULTS-rereview.md). This segment lies inside the class II catalytic domain, at the start of the bacterial-type insertion domain (human residues 337–470), which in the human structure rotates to make the mitochondrial active site more open for tRNA binding. The N-terminal targeting region, the anticodon-binding domain and every annotated aspartate- and ATP-binding residue are retained, so the deletion does not remove a known catalytic residue. Whether this isoform folds, dimerizes or aminoacylates tRNA(Asp) has not been tested, so activity of this exact sequence is unresolved. [PMID:23275545](https://pubmed.ncbi.nlm.nih.gov/23275545/); [DOI:10.1093/nar/gks1322](https://doi.org/10.1093/nar/gks1322).

### Relaxed specificity permitting tRNA(Asn) as well as tRNA(Asp)

**UNC.** Human GOA contains experimental aspartate-tRNA(Asn) ligase assertions. The 2005 paper is available as an abstract that does not expose the relevant substrate assays; the accessible 2013 paper describes accommodation of mitochondrial and bacterial tRNA(Asp), which is not the same as tRNA(Asn) acceptance. This cannot be rejected merely because nondiscriminating AspRS enzymes are familiar in bacteria, nor accepted from annotation agreement. Inspect the original substrate panel or obtain an independent specificity assay. [PMID:15779907](https://pubmed.ncbi.nlm.nih.gov/15779907/); [DOI:10.1021/bi047527z](https://doi.org/10.1021/bi047527z).

## Evidence scope and limits

[Human–horse sequence comparison](DARS2-bioinformatics/RESULTS.md) records coverage, gaps and architecture caveats. Human experimental results support transfer where the relevant features are conserved; ARBA assertions and generated gene-review prose are not used as biological evidence. The human reference sequence and current horse sequence are not known to be the exact prediction-time inputs. Claim assessments are kept separate because a partly correct paragraph should not receive an undifferentiated verdict.
