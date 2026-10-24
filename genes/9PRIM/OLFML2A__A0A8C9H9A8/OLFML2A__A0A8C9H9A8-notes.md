# OLFML2A (Piliocolobus tephrosceles, Ugandan red colobus; A0A8C9H9A8) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

### Scope and sources

- Target: A0A8C9H9A8 (TrEMBL, PE 4 Predicted, 655 aa; RefSeq XP_023072932.1; Ensembl gene
  ENSPTEG00000015637). It is the full-length product of the gene; A0A8C9H4D2 is a shorter (439 aa)
  entry from the same Ensembl gene lacking the N-terminal region and signal peptide.
- No ProtNLM2 file or prediction-evidence folder was opened or used.
- Deep research: `just deep-research-falcon 9PRIM OLFML2A --fallback perplexity-lite` FAILED on
  2026-10-21 (falcon: "Exception: Failed to authenticate"; perplexity-lite fallback: HTTP 401
  insufficient quota). No deep-research file exists for this gene; the review relies on the cached
  primary literature below, the UniProt records and the ortholog comparison.
- There is no experimental literature on the red colobus protein. All function claims are inferred
  from orthologs.

### Evolutionary grounding

- PANTHER: target, human OLFML2A (Q68BL7), mouse Olfml2a/photomedin-1 (Q8BHP7) and A0A8C9H4D2 all sit
  in PTHR23192:SF29 (OLFACTOMEDIN-LIKE PROTEIN 2A) [file:9PRIM/OLFML2A__A0A8C9H9A8/OLFML2A__A0A8C9H9A8-bioinformatics/RESULTS.md].
- Pairwise identity over aligned columns: 97.5% to human (99.5% target coverage), 84.0% to mouse
  (99.4% coverage); 98.4% to A0A8C9H4D2 over its 439 residues. Predicted signal peptide 1..27; two
  N-terminal CXCXCX9C motifs (residues 47 and 86); olfactomedin-domain cysteines conserved.
- PAINT (PTHR23192-paint.tsv): node PTN000573635 (taxon 33213, Bilateria) carries two IBDs:
  - GO:0005576 extracellular region, seeded by many members including mouse Olfml2a (MGI:2444741).
  - GO:0007165 signal transduction, seeded only by MGI:1202864, MGI:1860437 and UniProtKB:Q99972
    (myocilin); mouse Olfml2a is NOT among the seeds.
  - PAINT curators did not propagate mouse Olfml2a's own experimental MF terms (extracellular matrix
    binding, identical protein binding) or ECM organization to the family node. That is a decision
    about the family as a whole, not about the OLFML2A subfamily; within SF29 orthology to mouse is
    clear, so transfer of the photomedin-1 biochemistry to the red colobus ortholog is an
    ortholog-level (ISS-type) inference, and is recorded as such.

### Experimental findings on the mouse ortholog (photomedin-1)

- [PMID:15836428 "These proteins, named photomedin-1 and photomedin-2,
were secreted as disulphide-bonded dimers (photomedin-1) or oligomers/multimers
(photomedin-2) with O-linked carbohydrate chains"]
- [PMID:15836428 "Among
a panel of ECM components, including glycosaminoglycans, photomedins
preferentially bound to chondroitin sulphate-E and heparin."]
- Photomedin-1 is expressed in photoreceptor outer segments in mouse retina [PMID:15836428].
- Mouse GO (QuickGO, checked 2026-10-21): MGI IDA extracellular matrix binding (PMID:15836428), IPI
  identical protein binding (PMID:15836428), IDA located_in extracellular matrix (PMID:15836428,
  PMID:18757743), IDA acts_upstream_of_or_within extracellular matrix organization (PMID:18757743).
  The cached PMID:18757743 abstract is a whole-screen summary that does not name Olfml2a, so the ECM
  organization claim was not adopted.
- Human/rodent kidney: Olfml2a is expressed by podocytes and localizes to major processes
  [PMID:22913984]; this is expression/localization, not a function.

### Decisions

- GO:0005576 extracellular region (IEA, SubCell): ACCEPT. Signal peptide prediction plus mouse
  secretion data. The UniProt "Secreted" line itself is ARBA-derived, so it is not quoted as support.
- GO:0007165 signal transduction (IEA, TreeGrafter from PTN000573635 lineage): UNDECIDED, matching the
  human review. The IBD rests on noelin/myocilin seeds; no OLFML2A ortholog has evidence for a
  signaling mechanism, but there is also no evidence of loss.
- NEW GO:0050840 extracellular matrix binding (core, inferred from mouse IDA via SF29 orthology).
- NEW GO:0031012 extracellular matrix (location, inferred from mouse IDA via SF29 orthology).
- Not proposed: identical protein binding (assembly state, non-core), ECM organization (not supported
  by cached text), any retinal/kidney process (expression only).

### Experimentally established vs inferred (for downstream transfer)

Nothing is experimentally established in Piliocolobus tephrosceles. Everything in this review is
inferred from the mouse ortholog (secretion, disulfide-linked dimer, chondroitin sulfate E / heparin
binding) via PTHR23192:SF29 membership and >=84% identity, plus sequence features of the target
(signal peptide, CXCXCX9C motifs, olfactomedin domain).
