# PHRF1 (human, Q9P1Y6) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: PHRF1 was selected as the closest experimentally characterised relative of S. pombe asr1
(O94400). Both, along with rat Phrf1 (Q63625) and mouse Phrf1 (A6H619), are in PANTHER subfamily
PTHR12618:SF20 (checked via UniProt PANTHER cross-references). S. cerevisiae ASR1 (Q06834) is in a different
family (PTHR45798:SF97). No ProtNLM2 output was consulted.

Deep research: `just deep-research-falcon human PHRF1 --fallback perplexity-lite` failed. Falcon returned
403 Forbidden on Edison auth, and perplexity-lite returned 401 insufficient_quota. The review is based on
cached primary literature read directly.

GOA had only 5 rows: 3 IPI protein binding to CSNK2B (screens), 1 HDA membrane (NK membrane proteome), and
1 ISS RNA polymerase binding (from rat rA9).

### Evidence summary (human unless stated)
- E3 ligase, established in cells by RING-mutant loss of function.
  - TopBP1 K73 mono-ubiquitination; C108A inactive [PMID:40052822 "Only WT PHRF1 restored TopBP1
    ubiquitination, whereas neither the C108A nor S925A mutant was able to do so"].
  - TGIF K130 ubiquitination [PMID:23911286 "we identify PHRF1 as a ubiquitin ligase that enforces TGIF decay
    by driving its ubiquitination at lysine 130"]. This paper is abstract-only in the cache.
  - PARP1 polyubiquitination [PMID:25855964 "indicating that the RING domain of PHRF1 is responsible for the
    ubiquitination of PARP1 in vivo"].
  - p53 (knockdown only) [PMID:41215711]. Weak; not annotated.
  - No reconstituted assay with purified components has been seen; UniProt calls the RING "degenerate".
- PHD reader of the unmodified H3 N-terminus. FP KD ~3 uM, nucleosome BLI KD ~1 uM. P221L abolishes binding
  and fails to rescue the DDR defect [PMID:40671529; PMID:31980037]. The earlier H3K36me2/3 claim
  [PMID:25855964] is contradicted by PMID:40671529 and recorded as DISPUTED.
- Localisation: soluble nuclear; nuclear speckles (SRSF1), weaker in Cajal bodies [PMID:40671529];
  transient recruitment to laser DSB sites [PMID:25855964]; stalled forks [PMID:40052822].
- NHEJ: PHRF1 knockdown lowers and overexpression raises end-joining; NBS1 binding through the SDTE motif
  (CK2-dependent) [PMID:25855964].
- TGF-beta: TGIF degradation leads to cPML release and Smad2 activation; TGIF depletion is epistatic
  [PMID:25683711].
- RNAPII: rat rA9 binds the CTD in Y2H [PMID:8692929]; human PHRF1 co-IPs RNA Pol II [PMID:40671529].

### Decisions
- Protein binding (x3): REMOVE (policy). The CSNK2B interaction is plausible (CK2 site in SDTE motif).
- Membrane HDA: MARK_AS_OVER_ANNOTATED. Bulk membrane proteomics, and the protein has no TM segment.
- RNA polymerase binding ISS: MODIFY to GO:0099122 RNA polymerase II C-terminal domain binding. The donor is
  in the same SF20 subfamily.
- NEW terms added: GO:0061630 ubiquitin protein ligase activity, GO:0006513 protein monoubiquitination,
  GO:0140006 histone H3 reader activity (no GO term exists for an H3K4me0 reader), GO:0016607 nuclear speck,
  GO:0035861 site of double-strand break, GO:2001034 positive regulation of NHEJ, and GO:0030511 positive
  regulation of TGF-beta receptor signalling.
- Not annotated: tumour suppression, APL, dendrite/memory phenotypes (mouse CKO), IgA class switching
  (cell-line only, not reproduced in primary B cells), migration/ZEB1, p53. These are downstream phenotypes
  or weakly supported.

### For transfer to SF20 relatives (e.g. S. pombe asr1)
- Most likely conserved: the RING-dependent E3 activity and the PHD H3 N-terminal reader function. Both
  domains form the shared core used to place asr1 in SF20.
- Do not transfer: the vertebrate TGIF/cPML/TGF-beta axis, TopBP1 K73 specifics, or NHEJ via the
  NBS1-binding SDTE motif. These map to regions outside the conserved core.
- The RNAPII CTD binding of rat rA9 has not been mapped to a region shared with fungi.
