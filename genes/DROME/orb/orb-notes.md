# orb / Q8IMZ2

The selected Q8IMZ2 sequence has 559 residues. [Exact comparison](orb-bioinformatics/RESULTS.md) with long Orb Q9VCN7 establishes an identical 552-residue C-terminal region containing the RNA-binding machinery. This supports broad functional transfer, while not proving identical N-terminal regulation. [PMID:27791065](https://pubmed.ncbi.nlm.nih.gov/27791065/) directly compares Orb and Orb2 RNA-binding preferences; only Orb findings are transferred. [PMID:15737929](https://pubmed.ncbi.nlm.nih.gov/15737929/) establishes Orb-dependent translation and localization. [PMID:11809824](https://pubmed.ncbi.nlm.nih.gov/11809824/) full text directly assays Orb expression and mutant cysts despite its MEI-218 title. The 13 GOA rows are reviewed; broad binding annotations are specified, while developmental consequences remain noncore.

## Sequence and research provenance

The selected frozen UniProt record is retained in [orb-uniprot-source.json](orb-uniprot-source.json), with the complete original prediction metadata in [orb-predictions-source.json](orb-predictions-source.json). It maps the exact accession to this FlyBase gene; current sequence identity does not establish the historical predictor input. Gene-level experiments support conserved functions unless a relevant isoform difference is established. Falcon research was requested with perplexity-lite fallback alongside publication caching. Primary publications and sequence observations, rather than AI summaries or ARBA assertions, support the curated conclusions.

## Completed provider readback

The wrapper timed out and its fallback reported insufficient quota, but the original Falcon job later produced a complete report. The report and primary sources were inspected; no duplicate provider submission was made. The report supports Orb-specific CPEB RNA binding and translational regulation, distinguishing Orb2. It does not establish differences among Q8IMZ2 isoforms; local sequence comparison supports retention of the RNA-binding machinery.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

Identity: Q8IMZ2 (559 aa, unreviewed TrEMBL) is the shared product of orb transcripts C and E. It is an N-terminally truncated isoform of the gene; the UniProt gene-centric canonical product is Q9VCN7 (915 aa, isoform A/G; no Swiss-Prot entry exists for fly orb). The existing exact comparison ([RESULTS.md](orb-bioinformatics/RESULTS.md)) shows residues 8–559 identical to Q9VCN7 364–915, so the isoform keeps RRM1, RRM2 and the ZZ zinc-binding domain but lacks the N-terminal ~356 residues (low-complexity/regulatory region). Other gene products: Q8IMZ3 (913), E1JIU4 (617).

Evolutionary grounding: PANTHER PTHR12566:SF9 (CPEB1 subfamily), consistent with [PMID:27791065 "Drosophila Orb and Orb2 are single members of the CPEB1 and CPEB2 subfamilies of the CPEB proteins, respectively."]. SF9 also contains vertebrate CPEB1 (human Q9BZB8, Xenopus Q91572) and worm cpb-3. The interpro/panther/PTHR12566 family review agrees with this placement. PAINT IBAs (node PTN000286163, whole CPEB family) are attached only to canonical Q9VCN7 (mRNA 3'-UTR binding, translation repressor activity GO:0000900, ribosome binding, negative regulation of cytoplasmic translation, cytoplasm, nucleus, neuron projection, synapse); none are on Q8IMZ2. Those are left to the canonical review.

Literature added (cached): [PMID:10525352 "the osk 3' UTR can be UV cross-linked to Orb protein in ovarian extracts"], [PMID:12538512 "Orb-mediated cytoplasmic polyadenylation stimulates oskar translation"], [PMID:18434412 "Both Wispy and PAP interact with Orb genetically and physically in an ovarian complex."], plus [PMID:30865627] on microtubule repolarization.

Changes vs the previous review:
- regulation of translation (IEA) ACCEPT -> MODIFY to positive regulation of translation (GO:0045727); fly evidence is activation by polyadenylation. Orb does part of the work (target recognition and recruitment of PAP/Wispy), so this is participation, not just necessity.
- translation regulator activity kept ACCEPT (not refined to activator activity), because the family includes repressor function and Orb acts via polyadenylation rather than directly on the ribosome.
- The cytoplasm IDA row cites a nanos paper whose abstract never mentions Orb; accepted per curator, with independent support from PMID:11809824 immunostaining.
- Quotes rebuilt from primary data; review TAS (PMID:11700288) kept as a reference but not used as support.
- Developmental rows (germ cell development, oocyte D/V and A/P axis specification, germ plasm oskar mRNA localization) remain KEEP_AS_NON_CORE: Orb acts on the determinant mRNAs directly, but these are developmental deployments of the core activity.
- Not added: cytosolic mRNA polyadenylation (GO:0180011) and P-body/cell cortex locations, which are FlyBase annotations on the canonical product; they belong to that review.

Next relative: the canonical product Q9VCN7 has no review in the repo (genes/DROME/orb is keyed to Q8IMZ2), so it should be reviewed as genes/DROME/orb__Q9VCN7. No modules reference orb/CPEB.
