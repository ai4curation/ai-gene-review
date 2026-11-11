# UGT73C5 (At2g36800, DOGT1, ZOG3; Q9ZQ94) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: UGT73C5 is reviewed as the experimentally characterised reference for the
UGT73C cluster of PTHR48047 (it seeds PAINT node PTN008730368). No ProtNLM2 output was
consulted.

### Deep research

`just deep-research-falcon ARATH UGT73C5 --fallback perplexity-lite` failed: falcon
raised `Exception: Failed to authenticate` (Edison client JWT), and the perplexity-lite
fallback returned HTTP 401 `insufficient_quota`. No deep-research file exists. The
review is built from the cached primary literature (all six GOA PMIDs cached; only
PMID:16214889 has full text) and the curated UniProt record.

### Evolutionary placement

- PANTHER: PTHR48047 (GLYCOSYLTRANSFERASE), subfamily PTHR48047:SF153
  "UDP-GLYCOSYLTRANSFERASE 73C5-RELATED" (UniProt DR line and
  `interpro/panther/PTHR48047/PTHR48047-entries.csv`).
- PAINT: PTN008730368 carries a single IBD, GO:0035251 UDP-glucosyltransferase
  activity, seeded by AT1G73880, AT2G36750 (UGT73C1), AT2G36790 (UGT73C6), AT2G36800
  (UGT73C5), AT3G53160 and AT5G03490 (`PTHR48047-paint.tsv`). PAINT did **not**
  propagate any of UGT73C5's acceptor-specific experimental terms (trans/cis-zeatin
  O-glucosyltransferase, quercetin 7-O/4'-O-glucosyltransferase, brassinosteroid
  metabolic process, detoxification). That omission is read as deliberate: only the
  donor-level activity (UDP-glucose) is considered ancestral to the node; the acceptor
  specificities are treated as member-specific.
- Paralogs: UGT73C5 is one of seven UGT73C genes, six in a tandem array on chromosome 2
  [PMID:16214889 "UGT73C5 belongs to a clade of seven genes, six of which are found in a
  tandem repeat on chromosome 2"]; UGT73C6 is 87% identical [PMID:16214889].

Implication for transfer: only UDP-glucosyltransferase activity is phylogenetically
grounded for UGT73C-cluster relatives in other subfamilies (e.g. SF229). The
brassinosteroid 23-O-, DON 3-O-, zeatin O- and quercetin glucosylations are
experimentally established for UGT73C5 itself (Arabidopsis) and must not be
transferred as such.

### Experimentally established in Arabidopsis (this protein)

1. DON detoxification: identified in a yeast cDNA-library screen; transfers glucose from
   UDP-glucose to the C-3 hydroxyl of deoxynivalenol; the glucoside is inactive in a
   wheat-germ translation assay; also detoxifies 15-ADON but not nivalenol; overexpression
   enhances DON tolerance; gene induced by DON, SA, ethylene, JA
   [PMID:12970342, abstract only].
2. Brassinosteroid 23-O-glucosylation: BL and CS are glucosylated only at the 23-OH (in
   planta feeding, yeast expression); overexpression gives BR-deficient dwarfism rescued
   by epiBL, reduced typhasterol/6-deoxoCS/CS; RNAi silencing abolishes detectable
   BL-23-O-glucoside in seedlings; RNAi lines have slightly longer hypocotyls in low
   fluence red/blue light [PMID:16214889, full text]. The authors note "the data do not
   provide conclusive evidence" that glucosylation is the cause of inactivation.
3. Cytokinin O-glucosylation in vitro: one of three UGTs (with UGT85A1, UGT73C1) forming
   O-glucosides of trans-zeatin and dihydrozeatin in a 105-UGT screen [PMID:15342621,
   abstract only]; UniProt curated adds in vitro activity on cis-zeatin,
   dihydrozeatin-9-N-Glc and olomoucine, and "not induced by cytokinin treatment".
4. Quercetin: low 7-O and 4'-O glucosylation in vitro in a 91-UGT screen
   [PMID:15352060, abstract only; specifics from UniProt curated FUNCTION].

### Localization

No targeted localisation study. HDA ER call comes from microsomal proteome profiling
(PMID:28887381; gene only in supplementary tables). UniProt "Membrane; single-pass"
is ECO:0000305 inference from a predicted helix (146-162, ECO:0000255); family 1 UGTs
have a soluble GT-B fold, so a true TM span is doubtful. AtSubP chloroplast prediction
(ISM) has no supporting transit-peptide feature; removed.

### Decisions summary

- GO:0035251 IBA: ACCEPT (core MF; the target is itself a seed).
- GO:0008194 (IDA, IEA) and GO:0046527 (IDA, IEA): MODIFY -> GO:0035251.
- GO:0050403 trans-zeatin, GO:0050502 cis-zeatin, GO:0080044/GO:0080046 quercetin:
  KEEP_AS_NON_CORE (in vitro screens, physiological relevance unshown).
- GO:0016131 BR metabolic process: ACCEPT.
- GO:0098754 detoxification: ACCEPT.
- GO:0071456 cellular response to hypoxia (HEP): MARK_AS_OVER_ANNOTATED.
- GO:0005783 ER (HDA): KEEP_AS_NON_CORE; GO:0016020 membrane (IEA): MARK_AS_OVER_ANNOTATED;
  GO:0009507 chloroplast (ISM): REMOVE.
- Proposed new term: brassinosteroid 23-O-glucosyltransferase activity (no GO term found
  by OLS searches for "brassinosteroid glucosyltransferase" / "brassinolide").
