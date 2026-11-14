# lptA (P0ADV1, E. coli K-12) notes

## Provenance
- Provider deep research was NOT run for this gene; no `*-deep-research-*.md` file exists.
- Sources used: UniProt record (`lptA-uniprot.txt`), and cached publications
  PMID:17056748, PMID:18480051, PMID:18534617, PMID:20446753, PMID:20720015,
  PMID:21169485, PMID:22109962, PMID:22668317, PMID:29449493, PMID:18424520
  (full text where available); PMID:15911532, PMID:24140104, PMID:29176613 for proteomics/AP-MS rows.
- No new PMIDs fetched.
- Style/consistency model: `genes/PSEPK/lptA/lptA-ai-review.yaml`.

## Key points
- Periplasmic beta-jellyroll bridge protein; binds lipid A of LPS [PMID:18480051 "it interacts specifically with the lipid A domain of LPS"].
- Contacts LptC (IM) and N-LptD (OM) [PMID:22668317 "periplasmic LptA contacts both LptC at the IM and the N-terminal domain of LptD at the OM"].
- Reconstitution: LPS goes from LptBFGC to LptC then LptA [PMID:29449493 "transfer it to LptC and then to a periplasmic protein LptA"].
- Native LptA co-fractionates with OM [PMID:20446753 "LptA was also found to co-fractionate almost exclusively with these OM fractions"]. Cell outer membrane rows were kept as non-core; the P. putida LptA review makes the same call for its IEA row.

## Decisions
- GO:0017089 glycolipid transfer activity -> MODIFY to GO:0140332.
- GO:1990351 transporter complex -> MODIFY to GO:0062051 lipopolysaccharide transport system (consistent with lptB/lptC).
- GO:0042597 -> MODIFY to GO:0030288; GO:0046836 -> MODIFY to GO:0015920.
- Bare protein binding (4 rows) -> REMOVE under the protein-binding policy (interactions are real and are captured by GO:0062051).


## 2026-11-07 — cross-taxon Lpt audit, E. coli member consultation

All original annotation rows, reference findings and core roles were reassessed. Source payloads/order, qualifiers and historical NEW lifecycle remain unchanged. Targeted full-primary reading supports the existing division between LptB ATPase, membrane extractor subunit contributions, bridge transfer and terminal LptDE translocation. Abstract-only source details are not treated as disproven or silently relabeled as newly inspected full-text evidence. Generic location/assembly quotations were strengthened where appropriate; no new annotation was added. PMID42844470 updates whole-bridge regulation: E. coli proteins and an engineered LptC-LptA fusion support the structural analysis, with E. coli functional controls; LPS-null A. baylyi is an expression host, not a new organismal activity assay. The normal cache remains abstract-only; independently acquired publisher full text is documented in the shared literature consultation. The normal PAINT-loss check reports no IRD/IKR loss on this target lineage; this is not a whole-family uniformity claim. Default Falcon research was attempted normally and failed HTTP403 authentication; no provider report was created or overwritten. Manual source/ontology/preservation evidence is in analysis/module_audits/bacterial_lps_transport/ecoli-consultation/.
