# ccoP1 (PA1552, Q9I3G5) review notes

## Review session 2026-11-05 (PseudoCAP IBA-seed protocol, tier 2)

Fetched with `just fetch-gene PSEAE Q9I3G5 --alias ccoP1` (symbol fetch hit
UniProt rate limits). Accession Q9I3G5 matches the worklist (rank 324).
Unreviewed TrEMBL entry, 318 aa. Reviewed together with ccoP2 (Q9I3G2), the
other seed of the same PAINT node. No deep-research provider was used; PubMed
searches returned API errors on 2026-11-05, so only the PseudoCAP-cited paper
was read (abstract only).

### Identity

- CcoP/FixP family: NCBIfam TIGR00782 ccoP; Pfam PF14715 FixP_N and two
  PF13442 Cytochrome_CBB3 domains; PANTHER PTHR33751:SF1. UniProt (PIRNR):
  binds 2 heme c groups per subunit. Phobius predicts two N-terminal TM helices
  (7-25, 57-76); the two cytochrome c domains are on the periplasmic side.
- CcoP is the diheme cytochrome c subunit of the cbb3-type oxidase: it takes
  electrons from donor cytochromes and passes them via CcoO to the
  heme b3-CuB centre of CcoN, where O2 is reduced. It has no catalytic centre
  of its own. (UniProt's FUNCTION text says the same but rests on ARBA only, so
  it is not quoted as support.)
- cbb3-1 subunits: ccoN1 Q9I3G3, ccoO1 Q9I3G4, ccoQ1 E1JGJ6, ccoP1 Q9I3G5.
  cbb3-2: ccoN2 Q9I3G0, ccoO2 Q9I3G1, ccoQ2 E1JGJ7, ccoP2 Q9I3G2.

### Literature

- Comolli and Donohue 2004 (PMID:14763990; abstract only):
  [PMID:14763990 "The opportunistic pathogen Pseudomonas aeruginosa is unusual
  in possessing two operons that each potentially encode a cbb3 oxidase (cbb3-1
  or cbb3-2)."] [PMID:14763990 "In highly aerated cultures, cbb3-1 abundance
  and expression were greater than that of cbb3-2, and only loss of cbb3-1
  influenced growth."] The abstract speaks of the loss of each isoform, which
  reads as operon-level mutants; it does not name a ccoP mutant.
- Same-day sibling PseudoCAP rows (cached `.cache/paint/pseudocap.tsv`): the
  same GO:0004129 IMP to PMID:14763990 (20190311) is on all eight cbb3
  subunits, N, O, Q and P of both operons. So the row attributes an operon-level
  (complex) phenotype to each subunit. For the catalytic subunit CcoN `enables`
  is right; for CcoP, a subunit that only feeds electrons to the catalytic
  site, `contributes_to` is the right qualifier (same convention as the Sha/Mrp
  subunit reviews PA1054-PA1059).

### Clade check (cached PAINT IBD/leaf GAF, 2026-11-05)

- PTN002435498 (GO:0004129 cytochrome-c oxidase activity): seeds are ccoP2
  (Q9I3G2) and ccoP1 (Q9I3G5) only, both PseudoCAP IMP PMID:14763990. 32 leaf
  IBAs in 12 taxa. Leaves include genuine CcoP/FixP subunits (Bradyrhizobium
  FixP Q03075, Neisseria FixP Q9JY60, Helicobacter CcoP O24958, Shewanella
  CcoP Q8EEL8, Vibrio VC_1439) but also:
  - soluble cytochromes c4: P. aeruginosa cc4 (P00106), Vibrio VC_0112,
    Neisseria NMB1805, Shewanella SO_0714/SO_0717/SO_4048/CytcB,
    Xanthomonas CycA and XCC2144, Deinococcus DR_2487;
  - cytochromes c552/c554 (Xanthomonas CycM, Vibrio VC_A0766, Rhodopirellula
    RB4408);
  - the cytochrome c subunit of the bc1 complex, QcrC, of M. tuberculosis
    (P9WP35) and Streptomyces coelicolor (Q9X808);
  - P. aeruginosa PvcD (paerucumarin biosynthesis) and PA2482, and a Trichoplax
    protein.
  Cytochrome c oxidase activity is wrong for the cytochromes c4/c552/c554
  (soluble electron carriers) and for QcrC (a subunit of ubiquinol-cytochrome
  c reductase). The property shared by the clade is electron transfer by
  c-type heme (GO:0009055). With both seeds coming from the same operon-level
  phenotype, the IBD has no seed that supports the node term for the clade.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN002435498 | GO:0004129 cytochrome-c oxidase activity | 2 | 32 (12 taxa) | GO:0004129, IMP, PMID:14763990 (PseudoCAP) | OVER-SPECIFIC | The cbb3-1 operon is needed for cbb3-1 oxidase activity, and CcoP1 is a subunit of that enzyme, so it contributes to the activity. But CcoP is the electron-entry diheme cytochrome c, not the catalytic subunit, and the same IMP was applied to all eight subunits of both operons; the right qualifier is contributes_to. PSEUDOCAP WRONG_QUALIFIER (PROBABLE). | ccoP2 Q9I3G2 only (same paper, same issue) | No. Both seeds are PseudoCAP subunit rows from one operon-level paper, and the node is a broad c-type cytochrome clade (cytochromes c4/c552/c554, bc1 QcrC, PvcD) for which COX activity is wrong. GO_CENTRAL WRONG_TERM (REPOINT to GO:0009055, CONFIRMED from the leaf list) filed here once; ccoP2 cross-references it. |

Defects filed here: PSEUDOCAP WRONG_QUALIFIER (PROBABLE) on the IMP row;
GO_CENTRAL WRONG_TERM (CONFIRMED) for PTN002435498 on the IBA row. The node
defect is recorded only here (cbb3-1 is the isoform with the growth phenotype
in the paper); `genes/PSEAE/ccoP2/ccoP2-notes.md` points here.

## Decisions summary

- ACCEPT: cytochrome-c oxidase activity (IBA, IMP; as contributes_to in
  core_functions), electron transfer activity (IEA), heme binding (IEA),
  plasma membrane (IEA).
- MODIFY: oxidative phosphorylation (IEA) -> aerobic electron transport chain.
- KEEP_AS_NON_CORE: proton transmembrane transport (IEA; pumping is done by
  the complex at CcoN).
- MARK_AS_OVER_ANNOTATED: iron ion binding (IEA; the iron is heme iron).
