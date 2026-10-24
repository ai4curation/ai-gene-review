# DARS2 notes


## 2026-09-08 paired review

Selected accession A0A9L0SB67; ordinary UniProt record is TrEMBL and cites genome sequencing/submission rather than a gene-specific functional experiment. Human evidence is summarized in [the paired human investigation](../../human/DARS2/DARS2-notes.md). [Sequence comparison](DARS2-bioinformatics/RESULTS.md) records the exact target gaps and transfer limits. The targeted Europe PMC search found no decisive gene-specific horse functional assay warranting a separate horse Edison investigation; general omics/association hits were not counted as mechanistic validation.

Mitochondrial aspartate-tRNA synthetase must accommodate structurally unusual mitochondrial tRNA(Asp); the 2013 structure compares that accommodation with bacterial AspRS. Cross-aminoacylation of bacterial and mitochondrial tRNA(Asp) is a taxonomic/substrate-structure breadth claim, whereas acceptance of tRNA(Asn) is a different aminoacylation-specificity claim. The human GOA includes the latter, so the original experiments matter. The inspected 2013 full text did not settle that point and the 2005 characterization is abstract-only in the cache. Retaining uncertainty is appropriate. Matrix localization is the primary placement, but additional membrane-associated or extracellular activities cannot be dismissed just from that default.

Sources: [PMID:15779907](https://pubmed.ncbi.nlm.nih.gov/15779907/), [PMID:23275545](https://pubmed.ncbi.nlm.nih.gov/23275545/).

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 output was not opened or used. Deep research (`just deep-research HORSE DARS2 --provider falcon --fallback perplexity-lite`) failed: falcon "Failed to authenticate", perplexity-lite HTTP 401 insufficient quota. No deep-research file was written; the review uses the cached human DARS2 papers and the new analyses below.

### Identity of the benchmark accession

- A0A9L0SB67 (616 aa) is an **alternative isoform** of horse DARS2, not the canonical product. All four horse UniProt DARS2 entries come from one Ensembl gene, ENSECAG00000004044 (chr5, 7 protein-coding transcripts). A0A9L0SB67 = ENSECAT00000125808 (16 exons); it differs from ENSECAT00000043786 (A0A3Q2HM61, 652 aa, 17 exons) only by skipping one 108-nt in-frame exon (chr5:9524240-9524347) [file:HORSE/DARS2/DARS2-bioinformatics/RESULTS-rereview.md].
- A0A3Q2HM61 is the gene-centric canonical DARS2 entry in the horse reference proteome (UP000002281) and is 1:1 colinear with human Q6PI48 (643 paired residues, 89.9% identity). The Ensembl canonical (F6STJ2, 668 aa) carries one extra 48-nt exon absent from human. No horse DARS2 entry is Swiss-Prot reviewed.
- The skipped exon removes human-equivalent residues 341-376, at the start of the bacterial-type insertion domain (human 337-470 [PMID:23275545 "did not enable visualization of the bacterial insertion domain (residues 337–470, Supplementary Figure S1)"]), including the acetylated K368. All ATP/aspartate-binding residues (244-247, 266-268, 535, 542, 584-587), the arginine-rich transit region and the OB-fold anticodon-binding domain are retained. Whether the isoform is stable or active is unknown.

### Phylogenetic grounding

Unpruned PANTHER 19 PTHR22594 tree: horse DARS2 leaf PTN001475968 and human PTN002503203 share the path PTN000502375 > PTN000502597 (SF5 root) > PTN000502598 > ... > PTN000502607. PTN000502597 carries the PAINT IBDs for aspartate-tRNA ligase activity and aspartyl-tRNA aminoacylation (donors yeast MSD1, E. coli AspS, human DARS2); PTN000502598 carries mitochondrion. PAINT did not propagate human-only aspartate-tRNA(Asn) ligase activity (GO:0050560) or mitochondrial asparaginyl-tRNA aminoacylation (GO:0070145); those are treated as deliberate omissions and not transferred.

### Changes to the review

- gene_symbol set to DARS2 (Ensembl/PANTHER symbol for this gene) instead of the accession.
- nucleotide binding: KEEP_AS_NON_CORE -> TOO_GENERAL (entailed by ATP binding / ligase).
- nucleic acid binding: KEEP_AS_NON_CORE -> MODIFY to tRNA binding (OB-fold anticodon domain; conserved tRNA-contacting residues [PMID:23275545 "Otherwise, almost all residues making direct and specific interactions with bases at both ends of the Eco tRNA are conserved in the human enzyme"]).
- ATP binding: ACCEPT -> KEEP_AS_NON_CORE (component of the ligase reaction).
- cytoplasm: KEEP_AS_NON_CORE -> MODIFY to mitochondrion (PAINT PTN000502598 level; human mt-AspRS in soluble and membrane mitochondrial fractions [PMID:30006346 "This experiment reveals that the mt-AspRS is distributed in both the soluble and membrane fractions"]).
- tRNA aminoacylation for protein translation: ACCEPT -> MODIFY to GO:0070146 mitochondrial aspartyl-tRNA aminoacylation. Beware GO:0070145 is the asparaginyl term.
- aminoacyl-tRNA ligase activity and ligase activity: MODIFY to aspartate-tRNA ligase activity (unchanged).
- Core function now names GO:0070146 and mitochondrion; description rewritten to state the isoform status.
- Previous review's supporting quotes from RESULTS.md (pairwise identity) replaced with RESULTS-rereview.md; RESULTS.md kept as a reference.

### Relative to review next

Same-gene canonical product A0A3Q2HM61 (652 aa) has no review in the repo (`genes/HORSE/DARS2` is keyed to A0A9L0SB67), so the next target is `genes/HORSE/DARS2__A0A3Q2HM61`. Human DARS2 (Q6PI48) has a full review in genes/human/DARS2 (status DRAFT, no PENDING rows).

### Family and modules

- interpro/panther/PTHR22594/PTHR22594-review.yaml lists this accession and Q6PI48 under SF5; placement agrees. Minor issue: the family review's preferred_name/summary describe the family as "Aspartyl/asparaginyl" whereas PANTHER's official name is "ASPARTYL/LYSYL-TRNA SYNTHETASE"; and it lists the exon-skipping isoform rather than the canonical horse product as a representative.
- Module: modules/mitochondrial_trna_charging_and_initiator_formylation.yaml (human DARS2 is a part).
