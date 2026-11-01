# CABLES1 (human, Q8TDN4) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: CABLES1 is being reviewed as the closest experimentally characterised
relative of fly Cables1 (A0A0B4KF19). No ProtNLM2 output was opened or used.

### Deep research

`just deep-research-falcon human CABLES1 --fallback perplexity-lite` failed:
falcon (Edison API) returned 403 "Failed to authenticate" and the perplexity-lite
fallback returned 401 "insufficient_quota". No deep-research file exists. The
review was built from primary literature cached in `publications/` (PubMed search
for Cables/ik3-1 papers, then `just fetch-pmid`).

### Evolutionary placement

- PANTHER PTHR22896 (CDK5 AND ABL1 ENZYME SUBSTRATE 1). Human CABLES1 is in
  PTHR22896:SF1 (UniProt DR line). CABLES2 sits in SF3/SF4; fly Cables1 and worm
  Y71F9B.6 are in SF0, a single-copy invertebrate lineage that is co-orthologous to
  both vertebrate paralogs. So fly Cables1 is NOT in the CABLES1 subfamily, and
  SF1-specific findings below should not be transferred to it without further
  evidence.
- The IBA rows for CABLES1 come from PTN002740135. QuickGO shows mouse Cables1
  (Q9ESJ1) carries the same two IBAs (cytosol, nervous system development) but
  human CABLES2 (Q9BTV7) carries neither (only the InterPro IEA), so PAINT placed
  these at a CABLES1-clade node, not at the family root. Fly Cables1 likewise does
  not receive them. Treat that as a deliberate PAINT decision.
- Donors for nervous system development: mouse Cables1 (MGI:1927065; IMP from
  antisense knockdown in cortical neurons, PMID:10896159) and zebrafish cables1
  (morphant study PMID:21268180). Donor for cytosol: human CABLES1 itself (the
  MGI-curated IDA from PMID:17101133).
- Domain content: Cyclin_N (PF00134) / cyclin-like fold in the C-terminal region,
  PIRSF025798 Cables, IPR012388 CABLES1/2. "Belongs to the cyclin family" but
  it does not activate CDKs [PMID:11733001 "p70ik3-1 does not activate cyclin-dependent kinase 3 (cdk3)-mediated phosphorylation of pRb, histone H1, or the C-terminal domain of RNA polymerase II"].

### What is experimentally established, and in which species

Human protein or human cells:
- CDK2 regulation: in HeLa cells "Cables enhanced cdk2 tyrosine 15 phosphorylation
  by the Wee1 protein kinase, an inhibitory phosphorylation, which led to decreased
  cdk2 kinase activity" [PMID:11585773]. Nuclear localization by fractionation in
  proliferating cells [PMID:11585773].
- p21 stabilization: endogenous CABLES1 knockdown in HEK293T/H1299 cells shortens
  p21 half-life; "Cables1 interferes with the proteasome (Prosome, Macropain)
  subunit alpha type 3 (PSMA3) binding to p21 and protects p21 from PSMA3-mediated
  proteasomal degradation" [PMID:24975575]; nuclear co-localization with p21.
- p63 stabilization: human CABLES1 cDNA in COS7/Hep3B/H1299 cells; "the amino
  terminus of Cables1 interacts with the TA domain and SAM of TAp63α" and
  "Cables1 stabilizes p63α by blocking ubiquitin-mediated proteasomal degradation
  of the protein" [PMID:20559324]. Endogenous interaction and the in vivo
  oocyte-death phenotype are mouse.
- Regulation by AKT/14-3-3: T44 and T150 phosphorylated by AKT, recruiting 14-3-3;
  overexpression induces apoptosis, stabilizes p21 and decreases Cdk2 activity
  [PMID:25361894].
- CDK5 binding: multiple AP-MS / kinase interactome screens (IPI rows).
- Human genetics: germline loss-of-function missense variants in Cushing's
  disease; variants have reduced ability to block corticotroph proliferation
  [PMID:28533356]. Human tumour IHC shows cytoplasmic and predominantly nuclear
  staining [PMID:28533356].

Mouse or rodent (ortholog evidence only, same SF1 subfamily):
- Cables links CDK5 and c-Abl, enhancing c-Abl phosphorylation of CDK5 Y15 and
  CDK5 activity; antisense knockdown inhibits neurite outgrowth [PMID:10896159].
- ik3-1 binds CDK3 and is a CDK2/CDK3 substrate [PMID:10873625, PMID:11733001];
  binds TDRD7 (Trap) [PMID:11527406]; binds p53 and p73 [PMID:11706030].
- Cables1-null mice: endometrial hyperplasia [PMID:14729625], oocyte quality
  defects [PMID:17912041].

### Decisions

- Bare protein binding (GO:0005515): CDK5 rows MODIFY to protein kinase binding
  (GO:0019901); TP63 row MODIFY to p53 binding (GO:0002039, which by definition
  covers the p53 family).
- Regulation of cell cycle (IEA InterPro) MODIFY to regulation of cyclin-dependent
  protein serine/threonine kinase activity (GO:0000079), a descendant; the sign is
  context-dependent (negative for CDK2 in human cells, positive for CDK5 in mouse
  neurons), so the neutral parent is used.
- Nervous system development IBA: KEEP_AS_NON_CORE. Supported by mouse and
  zebrafish perturbation plus the CDK5/ABL adaptor mechanism, but peripheral to
  the core molecular role and largely phenotype-based.
- Cytosol IDA (PMID:17101133): the cached abstract (abstract-only) is about NESH
  (Abi-3) and does not mention Cables. The curator may have seen a Cables1 control
  in the full text. Because cytoplasmic CABLES1 is independently supported
  (human tumour IHC, mouse neurons), the row is accepted with deference to the
  curator, and the reference choice is flagged as a question.
- NEW: protein stabilization (GO:0050821). CABLES1 itself binds p21/p63 and
  blocks their ubiquitination/PSMA3 access, so it performs the stabilizing step
  (participation, not mere necessity). Not proposed: generic negative regulation
  of cell proliferation (overexpression/phenotype-level).
