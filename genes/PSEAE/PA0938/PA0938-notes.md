# PA0938 (Q9I520, Wzz2) review notes

No deep-research provider was available. Sources: UniProt record (TrEMBL), cached PMID:12534470 and
PMID:23955007 (abstract only; no PMC full-text XML obtainable), PMID:24309320 (full text in cache).
PubMed MCP searches on 2026-11-05 returned no hits (search service failing).

## Function

- PA0938 is a second functional Wzz (Wzz2) in PAO1; the wzz2 deletion keeps Wzz1 modality and the
  double mutant makes non-modal O-antigen
  [PMID:12534470 "As expected, the wzz2delta strain produced LPS with modal length imparted by Wzz1, and the wzz2delta/wzz1::Gm strain produced LPS O-antigen with a non-modal (random) length."].
- Wzz2 forms octamers and co-precipitates with O5 polymer
  [PMID:12534470 "In vivo protein cross-linking followed by Western immunoblotting indicated that Wzz1 forms dimers whereas Wzz2 forms octamers."].
- Phage D3 Iap peptide mimics the first TM segment of Wzz1/Wzz2; Iap inhibition is strongest without
  both Wzz proteins [PMID:23955007 "Sequence alignment analyses revealed a high degree of similarity between Iap and the first transmembrane segment (TMS) of either Wzz1 or Wzz2."].
  The abstract's topology predictions concern Iap, not Wzz2.
- PMID:24309320 (full text read): Wzy CL6 mutations alter Wzz1- but not Wzz2-specified modality;
  Wzz2-mCherry used for complementation of a wzz1 wzz2 double mutant. No cell-wall or peptidoglycan
  localisation of Wzz2 is reported anywhere in the text.
- Sequence: 442 aa; Phobius TM helices 28-49 and 392-412; Pfam PF02706 (Wzz N-terminal) and PF13807
  (GNVR motif, just before TM2; the motif is shared with Wzc but is not the kinase domain). The chain
  ends 30 residues after TM2, so there is no cytoplasmic BY-kinase domain. PANTHER PTHR32309:SF13
  (FepE subfamily: Wzz2 makes very long O-antigen like FepE).

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN000794252 | GO:0005886 plasma membrane | 5 | 62 (23 taxa) | GO:0005886 IDA PMID:12534470; GO:0005886 IDA PMID:23955007; GO:0098567 IDA PMID:12534470 (all PseudoCAP) | UNVERIFIABLE | The location is right (two TM helices flanking a periplasmic domain). PMID:12534470's abstract states no localisation assay; PMID:23955007's abstract reports sequence alignment and topology prediction (of Iap), so its IDA may rest on sequence analysis (SUSPECTED PSEUDOCAP WRONG_EVIDENCE_CODE). | E. coli Wzc P76387, Etk P38134, FepE P26266 (IDA plasma membrane); PAO1 Wzz1 G3XCY2 | Yes; three E. coli IDA seeds. No GO_CENTRAL defect for GO:0005886. |

Same node and same verdict as wzz (Wzz1). The node-level GO_CENTRAL defect for the GO:0004713 protein
tyrosine kinase IBD at PTN000794252 is recorded once on wzz; here the kinase IBA is removed and
cross-referenced.

Other PseudoCAP rows: GO:0009276 Gram-negative-bacterium-type cell wall, IDA PMID:24309320: the full
text reports no cell-wall localisation and Wzz2 is an inner-membrane protein: WRONG_TERM, CONFIRMED.
GO:0043165 outer membrane assembly (two IDA rows): over-annotation, as for wzz.

Defects recorded: PSEUDOCAP 2 (WRONG_EVIDENCE_CODE SUSPECTED on the PMID:23955007 plasma-membrane
row; WRONG_TERM CONFIRMED on the cell-wall row); GO_CENTRAL 0 here (1 node-level defect on wzz).
