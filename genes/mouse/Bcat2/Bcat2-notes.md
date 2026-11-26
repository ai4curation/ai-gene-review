# Bcat2 (mouse, O35855) notes

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

New review, written without reference to any ProtNLM2 output. Mouse Bcat2 is the reference
for transfer to human BCAT2 (O15382), so the notes below separate what is shown in mouse from
what is inferred.

### Deep research
- `just deep-research-falcon mouse Bcat2 --fallback perplexity-lite` failed: Edison/falcon returned
  403 Forbidden at auth, and the perplexity-lite fallback also exited non-zero. No deep-research file
  exists. The review relies on the cached GOA publications plus a PubMed search
  ((Bcat2 OR BCATm) AND mice/mouse, 68 hits), from which I cached PMID:36443523, PMID:32029896,
  PMID:20133434, PMID:27886623 and PMID:9165094. PMID:20736162 (KIC/insulin secretion in BCATm KO
  islets) failed to fetch.

### Evolutionary placement
- PANTHER PTHR11825:SF39 (mitochondrial BCAT), the same subfamily as human BCAT2 and rat Bcat2.
  BCAT1 is in SF70; no BCAT1-specific property is transferred here.
- PAINT: PTN000214535 carries the Leu/Ile/Val:2-oxoglutarate transaminase MFs and the Ile and Val
  catabolic process BPs; PTN000214536 carries mitochondrion. Mouse Bcat2 (MGI:1276534) seeds the BP and
  CC nodes. PAINT did not propagate L-leucine catabolic process. Mouse has direct IMP evidence for that term,
  so the row is accepted on that evidence, not by transfer.

### Experimentally established in mouse
- Loss of BCAT activity and protein in the ENU splice-site mutant, with BCAA elevation and an MSUD-like
  disease [PMID:14755340 "deficiency in both BCAT-2 protein and its enzyme activity"].
- Targeted knockout: elevated plasma BCAAs [PMID:17767905 "BCATm(-/-) mice exhibited elevated plasma BCAAs"].
- Bcat2-/- tissues have a lower glutamate/2-oxoglutarate ratio and reduced [13C]-KIV to valine reamination,
  which shows the reverse reaction in vivo; endogenous BCAT2 co-immunoprecipitates with BCKDHA in kidney
  mitochondria [PMID:36443523 "we provide evidence for the formation of a mitochondrial BCAA metabolon
  involving BCAT2 and branched-chain α-keto acid dehydrogenase"]. The proximity labelling in that paper
  used human BCAT2 in cells.
- Location: mitochondrion (fractionation per UniProt ECO:0000269, PMID:14755340; HDA proteomics
  PMID:14651853, PMID:18614015). The matrix sublocation is a curator IDA from the same paper; full text
  is not cached.

### Inferred, not measured in mouse
- Kinetics and specificity for each BCAA, PLP cofactor, homodimer, and the transit peptide boundary all
  come from rat or human (UniProt ECO:0000250). Rat BCATm expressed in COS-1 cells is active
  [PMID:9165094].

### Downstream phenotypes, not counted as process participation
- Energy expenditure, insulin/glucose tolerance (PMID:17767905), exercise intolerance (PMID:20133434),
  WAT browning after adipose deletion (PMID:35075301), and PDAC progression (PMID:32029896). Energy
  homeostasis and regulation of hormone levels are marked over-annotated. Brown fat cell
  differentiation is kept as non-core because its acts_upstream_of_negative_effect qualifier already
  describes the upstream metabolic role.

### Other decisions
- Nucleoplasm (ISO from human): over-annotated. The cached human GOA no longer carries the term.
- L-leucine biosynthetic process (ISO from rat): over-annotated. Reamination salvages existing carbon
  skeletons, and leucine is essential in mammals.
- LIF response (IEP, ES-cell transcriptome): over-annotated. An expression change is not participation.
