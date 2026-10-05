# Lcp3 review notes

## Identity and scope (2026-09-08)

The benchmark target remains **A0A0B4KEF3**, the unreviewed Lcp3 isoform-B record. Current reviewed [P07188](https://rest.uniprot.org/uniprotkb/P07188.txt) maps to the same [FlyBase locus FBgn0002534](https://flybase.org/reports/FBgn0002534.html) and the same two RefSeq proteins. Both accessions encode the identical 112-residue sequence: [reproducible comparison](Lcp3-bioinformatics/RESULTS.md). FlyBase reports “Number of Unique Polypeptides” as 1 despite two transcripts. The current record's separate accession/isoform label therefore does not justify withholding the characterized Lcp3 function. This does not reconstruct the sequence used by the prediction pipeline in its original run.

Fetched resources include the target UniProt and GOA records; verbatim UniProt records for P07188, P07189 and P80519; and a FlyBase HTML snapshot with a plain-text extraction (`Lcp3-flybase.html` / `.txt`, fetched 2026-09-08, BeautifulSoup text extraction after removing script/style elements). No derived UniProt records were edited. The fetch command also retrieved the PTHR10380 family cache; no family label was invented.

## Biological evidence

Lcp3 is a structural larval cuticle protein, not an enzyme or signaling regulator. The direct primary sequence work is [Snyder et al., 1982, PMID:6817923](https://pubmed.ncbi.nlm.nih.gov/6817923/), DOI [10.1016/0092-8674(82)90466-4](https://doi.org/10.1016/0092-8674(82)90466-4). The cached abstract reports “Amino acid sequences of four of the five major third instar cuticle proteins have been determined.” This is group-level evidence; the P07188 record explicitly attributes Lcp3 nucleotide and partial protein sequence to this paper. The reviewed record's function is “Component of the larval cuticle.” Its precursor has a signal peptide at 1–16 and an R&R domain at 31–92. FlyBase independently records IDA assignments to the larval-cuticle structural term and cuticle extracellular matrix. These curator/source links establish biological grounding; they are not independent replications of the same historical experiments.

Supporting context is available in the cached abstracts of [Snyder et al., 1981, PMID:6168386](https://pubmed.ncbi.nlm.nih.gov/6168386/), DOI [10.1016/0092-8674(81)90241-5](https://doi.org/10.1016/0092-8674(81)90241-5), and [Silvert et al., 1984, PMID:6441593](https://pubmed.ncbi.nlm.nih.gov/6441593/), DOI [10.1021/bi00319a015](https://doi.org/10.1021/bi00319a015). The former links the cloned gene cluster to larval epidermal expression and cuticle proteins; the latter compares isolated larval and pupal proteins. These abstracts do not resolve every protein-specific assay. The full papers are unavailable in the local caches, and no detailed mechanical assay or new phenotype is claimed.

## Main GO review

All three seeded GOA rows are reviewed. The two broad structural terms (GO:0005214 and GO:0042302) are biologically sound but **MODIFY** to the supported larval-specific GO:0008010. GO:0062129, chitin-based extracellular matrix, is **ACCEPT**. GO:0008010 was verified through QuickGO on 2026-09-08: current molecular-function term, structural integrity of larval chitin-based cuticle. No existing GOA term IDs or evidence codes were rewritten. No additional biological-process term is necessary to express this protein's structural core.

## ProtNLM review

See the [claim-level narrative review](Lcp3-protnlm-function-review.md). The paragraph has a correct, broad cuticle core but a definite wrong-species clause. Its recorded TMalign donor P80519 has the same sentence and is a spider cuticle protein, providing a concrete donor-context lead. The exact record also has an incorrect Lcp4 name (with P07189 as its name donor), while the secreted location is sound. These are separate output fields and should not be conflated into one mechanistic explanation. No claim is made that the input sequence was wrong or that a common cuticle fold alone proves the donor's precise annotation.

The target's ARBA cuticle keyword and this review's own prose are not biological validation. Evidence comes from current sequence identity, the protein-sequencing publication provenance, and FlyBase/Swiss-Prot's experimentally grounded Lcp3 curation.

## Provider research assessment

[The Falcon/Edison literature report](Lcp3-deep-research-falcon.md) completed successfully on 2026-09-08 in 550.76 seconds; its delivered markdown artifact is retained. The report supports the larval cuticle structural function and distinguishes family-level chitin-binding inference from direct biochemical measurement. Its conservative extracellular-localization assessment reflects a search for imaging or layer-specific experiments; the independently checked P07188 identity and FlyBase IDA record provide stronger support for general cuticle-matrix residence without requiring layer-resolved imaging. No specific cuticle stiffness, endocrine regulation, null phenotype, or chitin-binding affinity was imported from the synthesis. Its Beagle promoter-insertion discussion is a literature lead, not independently verified evidence added to the YAML. The report itself is not counted as another experimental replication.

Final checks: all three GOA rows reviewed with no PENDING entries; main validation passes with one advisory that the available research report is not cited in annotation support; exact local supporting excerpts checked; sequence comparison and distinct Lcp4 control reproduced; history schema validates and HTML rendered.

The research-citation advisory is retained deliberately: primary sequence provenance, exact accession identity, and experimental FlyBase curation already ground the decisions. The provider report adds context but no decisive independent result; it is discussed above rather than cited as redundant support. The main review status is DRAFT because this advisory remains, despite all seeded annotations being reviewed.
