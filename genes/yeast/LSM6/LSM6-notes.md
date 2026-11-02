# LSM6 (Q06406, YDR378C) — curation notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: S. cerevisiae LSM6 is the experimentally characterised donor (SGD:S000002786) at the
Lsm6-specific PAINT node PTN000111600, which supplies U6 snRNP, tri-snRNP, P-body, nucleolus,
snoRNA-containing RNP and SSU-rRNA maturation IBAs to the Lsm6 branch (including S. pombe lsm6,
Q9UUI1). This review was done without consulting any ProtNLM2 output.

### Deep research

`just deep-research-falcon yeast LSM6 --fallback perplexity-lite` failed: falcon (Edison) returned
"Failed to authenticate" and the perplexity-lite fallback returned HTTP 401 (insufficient quota).
No deep-research file was produced. The review is based on the cached publications (mostly
abstract-only; full text for PMID:24513854, PMID:29717126, PMID:30059503 and the large interactome
papers) and the curated UniProt record.

### Evolutionary grounding

- PANTHER: Q06406 is in PTHR11021:SF1 "U6 SNRNA-ASSOCIATED SM-LIKE PROTEIN LSM6", the same
  subfamily as human LSM6 (P62312) and S. pombe lsm6 (Q9UUI1)
  [file:interpro/panther/PTHR11021/PTHR11021-entries.csv]. PTHR11021 as a whole also contains
  canonical SmF; the family review flags that U2/U5 snRNP membership belongs to the SmF branch
  and must not be transferred to Lsm6.
- PAINT: the mRNA splicing IBA comes from the deeper node PTN000111530 (SmF + Lsm6), which is
  consistent with both branches acting in splicing. The Lsm6-specific node PTN000111600 carries
  U6 snRNP, tri-snRNP, P-body, nucleolus, snoRNA-containing RNP and maturation of SSU-rRNA. It does
  NOT carry the decapping (GO:0000290), Lsm1-7-Pat1 complex, tRNA processing or rRNA processing
  terms that yeast LSM6 has experimentally. Treated as a deliberate PAINT decision (these are
  complex-level or possibly indirect roles), not as a gap to fill.

### Experimentally established in S. cerevisiae (direct evidence on Lsm6)

- U6 snRNA association / Lsm2-8: Lsm proteins co-IP U6 and pre-RNase P RNA
  [PMID:10369684 "Immunoprecipitation revealed that an evolutionarily related subgroup of seven
  Sm-like proteins is directly associated with the nuclear U6 and pre-RNase P RNAs."]; purified U6
  snRNP = U6 snRNA + Prp24 + 7 LSm proteins [PMID:11720284 "The U6 snRNP is composed of the U6
  snRNA, Prp24, and the 7 Sm-Like (LSM) proteins."].
- Tri-snRNP: Lsm6p identified by MS in purified tri-snRNP [PMID:10449419 "These include four
  Sm-like proteins (Lsm2p, Lsm5p, Lsm6p and Lsm7p)"]; also PMID:10377396 ("a set of U6 snRNP
  specific Sm proteins").
- Lsm2-8 ring structure (Lsm6 is a ring subunit; 3' U residues contacted by Lsm3/2/8/4)
  [PMID:24240276]; Lsm6 R74 (invariant Arg) needed for high-affinity U-rich 3'-end binding
  [PMID:24513854 "mutation of the conserved Arg to Ala in any of the Lsm6/3/2/8/4 subunits results
  in drastic reduction of binding affinity"]. Lsm2-8 accelerates Prp24-mediated U4/U6 annealing
  [PMID:29717126].
- Lsm1-7 / mRNA decay: Lsm1-7 is a distinct complex associated with Pat1 and Xrn1; lsm6 deletion
  stabilises reporter mRNAs that accumulate capped [PMID:10747033 "Deletions of LSM1, 6, 7 and
  PAT1 genes increased the half-life of reporter mRNAs."]; Lsm1-7 mutations inhibit decapping
  [PMID:10761922]. Crystal structures place Lsm6 in the Lsm1-2-3-6-5-7-4 ring [PMID:24139796,
  PMID:24513854].
- Nuclear mRNA decay: lsm6 deletion stabilises nucleus-retained mRNAs [PMID:15485930 "strongly
  stabilized in strains lacking Lsm6p or the nucleus-specific Lsm8p protein"]. Not annotated in
  GOA; not added as NEW (see below).
- Lsm2-7 / snR5 in nucleolus [PMID:15075370].

### Complex-level or indirect evidence (not Lsm6-specific)

- GO:0000290 IMP cites PMID:15716506, an LSM1 mutagenesis paper; the annotation to LSM6 is a
  complex-level (ComplexPortal) inference. The function is nonetheless supported directly for
  Lsm6 by PMID:10747033 and PMID:10761922, so ACCEPT.
- pre-tRNA, pre-rRNA and U3 processing (PMID:12077351, PMID:12438310, PMID:14627812): the
  abstracts report depletion of the essential Lsm2-5/Lsm8; Lsm6 is non-essential and not named in
  the abstracts. Curators (full text) annotated LSM6 by IMP; kept as non-core. UniProt notes the
  involvement "may be indirect".

### Decisions

- 29 GO:0005515 protein-binding rows (intra-ring Lsm partners and Pat1): REMOVE per policy; the
  information is captured by the Lsm2-8 / Lsm1-7-Pat1 / U6 snRNP CC terms.
- RNA binding IDA (contributes_to) rows: MODIFY to U6 snRNA binding (PMID:10369684) and snoRNA
  binding (PMID:15075370), keeping contributes_to.
- Sm-like protein family complex (ARBA IEA): MODIFY to Lsm2-8 complex and Lsm1-7-Pat1 complex.
- No NEW process terms: nuclear mRNA decay and tri-snRNP assembly (U4/U6 annealing) are
  complex-level activities; recorded in core-function descriptions / suggested questions rather
  than asserted as new annotations.
