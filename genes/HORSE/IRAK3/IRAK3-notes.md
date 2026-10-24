# IRAK3 notes


## 2026-09-08 paired review

Selected accession A0A3Q2HDT6; ordinary UniProt record is TrEMBL and cites genome sequencing/submission rather than a gene-specific functional experiment. Human evidence is summarized in [the paired human investigation](../../human/IRAK3/IRAK3-notes.md). [Sequence comparison](IRAK3-bioinformatics/RESULTS.md) records the exact target gaps and transfer limits. The targeted Europe PMC search found no decisive gene-specific horse functional assay warranting a separate horse Edison investigation; general omics/association hits were not counted as mechanistic validation.

The 1999 discovery study observed negligible autophosphorylation yet restoration of an IL-1 response in IRAK-deficient cells. The 2002 genetic study established physiological negative regulation: IRAK-M prevents IRAK/IRAK4 release from MyD88 and restricts cytokine induction and endotoxin sensitivity. The 2021 human structure explains a noncanonical inactive catalytic site, a distinctive homodimer and a possible IRAK4-interaction surface. ATP-pocket retention or weak nucleotide binding cannot establish active kinase catalysis. The positive cell-reconstitution result and inhibitory physiological feedback should coexist in the synthesis rather than being flattened into an unconditional activator or inhibitor. The selected horse N-terminal deletion reaches its death-domain start, so receptor-complex assembly needs specific checking.

Sources: [PMID:10383454](https://pubmed.ncbi.nlm.nih.gov/10383454/), [PMID:12150927](https://pubmed.ncbi.nlm.nih.gov/12150927/), [PMID:33238146](https://pubmed.ncbi.nlm.nih.gov/33238146/).

## Conserved noncanonical catalytic-loop configuration

The published human IRAK3 CGS291–293 and DFA311–313 motifs map to horse CGS249–251 and DFA269–271 in the frozen UniProt sequences. This supports conservation of the noncanonical pseudokinase configuration. It does not establish that the shortened horse N-terminal interaction region assembles normally, nor exclude every alternative catalytic mechanism. [Primary structural study](https://pubmed.ncbi.nlm.nih.gov/33238146/); [computed mapping](IRAK3-bioinformatics/pseudokinase-motifs.json); [reproduction script](IRAK3-bioinformatics/map_pseudokinase_motifs.py).

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

Deep research: `just deep-research-falcon HORSE IRAK3 --fallback perplexity-lite` failed (falcon timed out and the perplexity-lite fallback also failed), so no horse deep-research file exists. The review uses the cached primary papers (PMID:10383454, PMID:12150927, PMID:33238146) and the human IRAK3 review/deep research.

### Identity of the benchmark accession

A0A3Q2HDT6 (567 aa) is a **non-canonical alternative Ensembl gene model** of horse IRAK3, not the canonical product. [RESULTS-rereview.md](IRAK3-bioinformatics/RESULTS-rereview.md); script `compare_gene_models_rereview.py`; output `results-rereview.json`.

- Ensembl gene ENSECAG00000026958 has three protein-coding transcripts. The canonical one is ENSECAT00000029063 (14 exons, 614 aa) = UniProt **F6QZW8** = RefSeq XP_023499869.1 (isoform X1). A0A3Q2HDT6 is ENSECAT00000032597 (12 exons), with an alternative first exon downstream of the canonical one. A third model, A0A5F5PKF5 (553 aa, isoform X2), lacks most of the death domain.
- Benchmark residues 4-567 are an exact substring of F6QZW8 from residue 51: the benchmark replaces canonical residues 1-50 with "MIT". It lacks the 45-residue N-terminal extension and the first residues of the PROSITE death-domain boundary (64/66 human DD residues align), but keeps the Pfam death-domain match, the complete pseudokinase domain (human 165-452 = horse 123-410) with the IRAK3-specific CGS/DFA configuration, and the C terminus.
- No horse IRAK3 entry is in Swiss-Prot. GOA projects the PAINT IBAs (IL-1-mediated signaling, LPS-mediated signaling, Toll signaling, cytoplasm/nucleus) and the Ensembl-Compara ortholog IEAs only to F6QZW8. That is why the benchmark carries just two InterPro2GO rows. Its sparse annotation comes from the gene model, not from the biology.
- Human Ser110 (phosphorylated by IRAK1, PIN1 isomerisation site, IL-33 pathway; PMID:29686383) is Asn in all horse models, so the IL-33/PIN1 nuclear mechanism was not transferred.

### Evolutionary grounding

The horse gene is in PANTHER PTHR24419:SF7 (IRAK3) with human Q9Y616 (80.5% identity to the benchmark). The PANTHER family review `interpro/panther/PTHR24419/PTHR24419-review.yaml` places it in SF7 as well, so there is no placement disagreement. One caveat for that review: it lists A0A3Q2HDT6 as the SF7 horse representative. F6QZW8 would be the better representative. Mouse Irak3 Q8K4B2, the knockout donor for the negative-regulation function, currently has a PANTHER cross-reference to PTHR27001:SF929 in UniProt, an odd placement. Its orthology to human/horse IRAK3 rests on gene identity (MGI/HGNC/VGNC orthology) and on alignment: 76% identity to human, with the death domain, pseudokinase domain and DFA motif all conserved.

### Annotation decisions

- GO:0005524 ATP binding (IEA, InterPro): KEEP_AS_NON_CORE. Weak ATP affinity measured for human IRAK3, and the pseudokinase domain is complete in the benchmark.
- GO:0007165 signal transduction (IEA, death domain): MODIFY, previously UNDECIDED, to GO:0002755 MyD88-dependent TLR signaling pathway and GO:0070498 IL-1-mediated signaling pathway. These are the PAINT-supported pathways of the clade. The caveat that this alternative product has not been tested for Myddosome assembly is recorded.
- NEW: GO:0034122 negative regulation of TLR signaling pathway and GO:0043242 negative regulation of protein-containing complex disassembly (mouse KO, PMID:12150927), plus GO:0019901 protein kinase binding (IRAK4, PMID:33238146). The kinase-activity terms were not proposed: the IRAK3 active site is noncanonical, and PAINT did not propagate protein kinase activity to IRAK3. The positive cytokine and IL-33 outputs were not proposed either, because they depend on Ser110, which horse does not have.

### Next relative

Same-gene canonical product F6QZW8 (horse IRAK3, Ensembl canonical, 614 aa). It has no review in the repo; its folder would be `genes/HORSE/IRAK3__F6QZW8`. Human IRAK3 (Q9Y616) already has a complete review at genes/human/IRAK3.

Modules: there is no IRAK3 part yet. Relevant modules are `modules/toll_like_receptor_signaling.yaml` (IRAK-TRAF6 signalosome), `modules/il1_signaling.yaml`, `modules/tlr4_md2_lps_signaling.yaml` and `modules/tlr2_heterodimer_lipopeptide_signaling.yaml`.

## 2026-10-21 — NEW rows withdrawn from the alternative gene model (PR #5303 review)

The re-review had proposed NEW rows (GO:0034122, GO:0043242, GO:0019901) on this benchmark accession because GOA propagates the
gene's annotations, including PAINT IBA rows, to one representative product per gene and not to
alternative transcript models. The same terms are already annotated in GOA on the canonical horse
product of this gene (IRAK3__F6QZW8, reviewed in `genes/HORSE/IRAK3__F6QZW8/`). Filling that propagation
convention on a second product of the same gene is not a curation gap, so the rows were withdrawn
for consistency across the cohort. The gene-level function is unchanged and is recorded on the
canonical product's review; this file's description and core functions still describe it.
