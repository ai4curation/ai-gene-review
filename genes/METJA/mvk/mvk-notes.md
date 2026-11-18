# mvk (MJ1087, Q58487) — Methanocaldococcus jannaschii mevalonate kinase

## Identity check

- Stub `id: Q58487` (MVK_METJA), gene `mvk`, ordered locus MJ1087, NCBITaxon:243232. 312 aa,
  PE 1, PDB 1KKH and 1VIS. PANTHER PTHR43290:SF2 (MEVALONATE KINASE), HAMAP MF_00217,
  NCBIfam TIGR00549, InterPro IPR022937 (archaeal mevalonate kinase).
- No FlyBase/SGD/WormBase style MOD description applies (archaeon). No deep-research provider
  file was generated (no provider keys in this campaign); this notes file records the manual
  literature search.

## Literature search (2026-11-18)

Queries (NCBI E-utilities / Europe PMC):
- `"MJ1087"` -> 1 hit, PMID:22865846 (pantoate kinase paper; MJ1087 only mentioned), not used.
- `jannaschii AND "mevalonate kinase"` -> 63 hits. Primary papers on this protein: PMID:10497066,
  PMID:12880770, PMID:11751891, PMID:42808591; structural-genomics PMID:16021622 (PDB 1VIS);
  pathway context PMID:16621811; applied use PMID:40842514. Others are on orthologs
  (M. mazei PMID:21908638, PMID:30521590; Methanosaeta/Methanocella PMID:28869407) and were not
  needed for gene-level claims.
- `"phosphomevalonate decarboxylase"`, `Haloferax AND mevalonate`, `Hemmi H[au] AND mevalonate AND
  archae*` -> archaeal pathway context: PMID:24375100 (H. volcanii PMD + IPK), PMID:24327557
  (Dellas 2013), PMID:30224495 (A. pernix trans-anhydromevalonate 5-phosphate route).

## What each paper shows

- Recombinant MJ1087 is a thermostable mevalonate kinase, a homodimer of 36 kDa subunits
  [PMID:10497066 "The purified protein had a dimeric structure composed of identical subunits"]
  with Michaelis constants for both substrates [PMID:10497066 "The Michaelis constant (K(m)) for
  (RS)-mevalonate was 68.5 microM and was 92 microM for ATP"]. UniProt (ECO:0000269 to this paper)
  records Mg2+ as cofactor and competitive inhibition by farnesyl and geranyl diphosphate; the
  cached copy is abstract only.
- Site-directed mutants: Arg196 essential, Lys272-Glu14 salt bridge maintains the active site
  [PMID:12880770 "The results from kinetic studies showed that Arg196 is an essential residue for
  the function of the enzyme."]. Abstract only.
- Crystal structure at 2.4 A, GHMP fold, active site in the N/C-domain cleft, Asp155 putative
  catalytic base [PMID:11751891 "Asp(155), an invariant residue among MVK sequences, is located
  close to the putative phosphate-binding site and has been assumed to play the catalytic role."].
  Abstract only.
- 2026 engineering study on the same enzyme (full text): mevalonate phosphorylation assayed by ATP
  consumption; I10S raises kcat fivefold at 22 C [PMID:42808591 "mevalonate kinase activity was
  assayed by ATP utilization assay for phosphorylation activity of mevalonate"].
- MjMvk was chosen as step 1 of a thermophilic "Archaea I" cell-free pathway [PMID:40842514 "The
  mevalonate kinase from the thermophile Methanocaldococcus jannaschii (MjMvk) was selected as the
  optimal variant for the initial step of the thermophilic mevalonate pathway"].

## Pathway context: does the protein perform the classical reaction?

Yes. The archaeal "modified" mevalonate pathways diverge only after mevalonate 5-phosphate
(MVA5P). M. jannaschii lacks recognisable PMK and DMD genes, and its IPP-forming step is an
isopentenyl phosphate kinase (MJ0044), not a diphosphomevalonate decarboxylase
[PMID:16621811 "The MJ0044 gene product was found to phosphorylate isopentenyl phosphate,
generating isopentenyl diphosphate."]. The MVK step (MVA -> MVA5P) is shared by the classical,
Archaea I (PMD + IPK; PMID:24375100) and Archaea III (MVA5P dehydratase + decarboxylase + IPK;
PMID:30224495) routes, so the kinase reaction itself is the classical EC 2.7.1.36 reaction, and
biochemistry on this protein confirms it. What happens to MVA5P downstream in M. jannaschii
itself (PMD-like decarboxylation versus the A. pernix dehydratase route) has not been shown
biochemically for this organism; it does not affect this gene's annotation.

GO:0019287 (IPP biosynthesis, mevalonate pathway) is defined by formation of IPP "via the
intermediate mevalonate", so it covers the modified archaeal routes as well as the classical one.

## IBA rows (PTHR43290, node PTN000048555)

- PTN000048555 is the family root node (taxon field empty) carrying GO:0004496, GO:0019287 and
  GO:0005829. `just paint-losses METJA mvk` reports no IRD/IKR on this lineage. The only IRD in
  the family (PTN002214956, GO:0004496 and GO:0019287) sits on the eukaryotic branch that also
  carries the plant glucuronokinase IBD (PTN008680403, GO:0047940, seed AT3G01640), not above
  Q58487.
- MJ1087 is inside the clade that inherited mevalonate kinase activity, and direct biochemistry
  on it confirms the function, so the MF and BP IBAs are sound for this member. The cytosol IBA is
  a soluble enzyme in an organism with no endomembranes; sound.

## Decisions (summary)

- MVK activity (IBA, IEA): ACCEPT, core.
- IPP biosynthesis, mevalonate pathway (IBA, IEA): ACCEPT, core.
- ATP binding: ACCEPT (Km for ATP measured; P-loop/GHMP ATP motif).
- Mg ion binding: KEEP_AS_NON_CORE (cofactor; Mg2+ requirement).
- isoprenoid biosynthetic process (IEA): ACCEPT (not an ancestor of GO:0019287 in GO; archaeal
  isoprenoid lipids are the end product).
- kinase activity, phosphotransferase alcohol acceptor (InterPro2GO from IPR006206, which also
  covers galactokinases): TOO_GENERAL beside GO:0004496.
- cytoplasm (IEA), cytosol (IBA): ACCEPT.
