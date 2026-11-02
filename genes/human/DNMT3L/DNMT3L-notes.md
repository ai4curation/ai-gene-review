# DNMT3L notes


## 2026-09-08 paired human–horse review



DNMT3L is a noncatalytic regulator of de novo DNA methyltransferases and chromatin-dependent gene repression. Its ADD domain recognizes chromatin context and supports interactions with repressive machinery, while its methyltransferase-like region interacts with DNMT3A and DNMT3B. DNMT3L contributes to imprint establishment and transposable-element silencing without itself serving as a conventional DNA methyltransferase.

## Noncatalytic epigenetic regulation

DNMT3L is related to de novo DNA methyltransferases but lacks the complete machinery of an active methyltransferase. The 2002 primary study demonstrates interaction with HDAC1, recruitment of deacetylase activity and HDAC-dependent repression, while the 2006 biochemical/cell study shows stimulation of DNMT3B and the importance of its interaction interface. These support enzyme activation and gene regulation independently of a catalytic DNA-methylation claim. Chromatin localization, imprinting, transposon repression and germ-cell developmental consequences should be distinguished by level of mechanism. The selected horse protein covers the entire human sequence and retains its ADD/chromatin-interaction architecture; its N-terminal extension is not an absence of the human core.

## Decisive inspected evidence

From [PMID:12202768](https://pubmed.ncbi.nlm.nih.gov/12202768/):

> We find that Dnmt3L can repress transcription and that this repression is dependent on HDAC1 and is relieved by treatment with the HDAC inhibitor trichostatin A.

## Evidence inventory

- [PMID:12202768: Dnmt3L is a transcriptional repressor that recruits histone deacetylase.](https://pubmed.ncbi.nlm.nih.gov/12202768/). [DOI:10.1093/nar/gkf509](https://doi.org/10.1093/nar/gkf509). The repository cache contains the abstract; source-specific claims beyond it remain unresolved.
- [PMID:16543361: Mutations in DNA methyltransferase DNMT3B in ICF syndrome affect its regulation by DNMT3L.](https://pubmed.ncbi.nlm.nih.gov/16543361/). [DOI:10.1093/hmg/ddl059](https://doi.org/10.1093/hmg/ddl059). The repository cache contains the abstract; source-specific claims beyond it remain unresolved.

## Transfer to the selected horse protein

The exact target is [A0A9L0T837](https://www.uniprot.org/uniprotkb/A0A9L0T837/entry), not an arbitrary horse record with a matching name. The reproducible [paired-sequence analysis](../../HORSE/DNMT3L/DNMT3L-bioinformatics/RESULTS.md) records identity, coverage and internal gaps. It supports homology but is not a reciprocal orthology test. Molecular properties are transferred only with the relevant domain, targeting and paralog constraints. The prediction-time sequence is not independently verified.

## Open evidence questions

The following annotation scopes need source-specific follow-up: ESC/E(Z) complex, negative regulation of DNA methylation-dependent heterochromatin formation, protein binding. Experimental annotations are not removed merely because a cached abstract omits the gene or a specific assay. High-throughput protein-binding rows require their actual partner or complex context before replacement with an informative molecular function.


Research provenance: external Falcon/Edison was attempted with Perplexity fallback. Some requests returned HTTP 429 and fallback returned insufficient-quota HTTP 401; successful external reports are preserved separately. Primary-source manual synthesis is explicitly labeled manual where no external report was available.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 prediction files were not opened or used. Sources: UniProt Q9UJW3, cached primary papers, the falcon deep-research report, PANTHER family review `interpro/panther/PTHR23068/PTHR23068-review.yaml`.

### Identity
- Q9UJW3 is the reviewed canonical human DNMT3L entry (386 aa, isoform 1 displayed; isoform 2 differs only by S332->SS, VSP_041295). It is not a fragment or alternative gene model. ADD domain 41-173 (atypical GATA- and PHD-type zinc fingers); C-terminal methyltransferase-like domain lacking catalytic motifs.
- PANTHER: PTHR23068:SF13 (DNA (CYTOSINE-5)-METHYLTRANSFERASE 3-LIKE), a separate subfamily from catalytic DNMT3A (SF10) and DNMT3B. The family review agrees (SF13 = non-catalytic regulatory branch). No disagreement on subfamily placement.

### Evolutionary grounding
- Most ISS/IEA rows are transfers from mouse Dnmt3l (Q9CWR8), a 1:1 ortholog in the same SF13 subfamily, so its experimental functions (imprinting, retrotransposon methylation, ESC/PRC2 role) transfer.
- IBA nodes: PTN001891074 (DNMT3L clade; donors mouse Dnmt3l + human DNMT3L) -> enzyme activator activity, appropriate. PTN002747444 (DNMT3 clade, donor DNMT3A) -> cytoplasm and negative regulation of transcription; DNMT3L has its own repression data [PMID:12202768 "We find that Dnmt3L can repress transcription and that this repression is dependent on HDAC1"]. PTN001497036 family root -> nucleus.
- Catalytic activity is NOT transferred from DNMT3A/3B: DNMT3L is "an enzymatically inactive regulatory factor" [PMID:17687327].

### Key decisions vs previous (templated) review
- Male meiosis I (IEA + ISS): REMOVE. Downstream phenotype: [PMID:15318244 "Loss of Dnmt3L from early germ cells also caused meiotic failure in spermatocytes, which do not express Dnmt3L."]
- Protein binding: HDAC1 -> MODIFY to histone deacetylase binding (GO:0042826); DNMT3A -> MODIFY to enzyme activator activity; RSL24D1 x3 and PDZD4 (binary Y2H screens) -> REMOVE (uninformative).
- Enzyme binding (HDAC1) -> MODIFY to histone deacetylase binding.
- Catalytic complex (x2) -> MODIFY to DNA methyltransferase complex (GO:0140020; verified is_a descendant via methyltransferase complex/transferase complex). Supported by DNMT3A-3L and DNMT3B-3L heterotetramer structures [PMID:25383530; PMID:32083663].
- ESC/E(Z) complex colocalizes_with and negative regulation of DNA methylation-dependent heterochromatin formation: previously UNDECIDED, now KEEP_AS_NON_CORE, supported by mouse ESC data [PMID:24074865 "Dnmt3L interacts with the Polycomb PRC2 complex in competition with the DNA methyltransferases Dnmt3a and Dnmt3b"].
- Heterochromatin, condensed nuclear chromosome, cytoplasm, cytosol, spermatogenesis, stem cell differentiation, negative regulation of DNA-templated transcription: KEEP_AS_NON_CORE.
- ACCEPT core: nucleus, enzyme activator activity, DNA methylation-dependent constitutive heterochromatin formation, genomic imprinting [PMID:11719692; PMID:11934864], TE silencing (both terms) [PMID:15318244], negative regulation of gene expression, epigenetic.
- NEW: histone H3 reader activity (GO:0140006; def covers unmodified H3) from the human DNMT3L-H3 tail co-crystal and peptide assays [PMID:17687327 "DNMT3L specifically interacts with the extreme amino terminus of histone H3; this interaction was strongly inhibited by methylation at lysine 4"]. MF the protein itself performs; not a process-substrate case.

### Relative to review next
- Mouse Dnmt3l (Q9CWR8), the 1:1 ortholog in SF13 and source of most transferred annotations; no review exists in genes/mouse/.

### Modules
- modules/pirna_mediated_germline_silencing.yaml mentions DNMT3L as part of the mammalian methylation machinery.
