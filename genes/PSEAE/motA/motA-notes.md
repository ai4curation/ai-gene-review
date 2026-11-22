# motA (PA4954, Q9HUL1) notes

## Review session 2026-11-05 (PseudoCAP IBA-seed protocol, tier 2)

Fetched with `just fetch-gene PSEAE Q9HUL1 --alias motA`; accession matches the
worklist. Unreviewed TrEMBL entry, named `motA` by the PAO1 genome annotation.
No deep-research provider key was available; literature is the stator papers
already used for motB (genes/PSEAE/motB).

### Identity and literature

- MotA-family protein, four predicted TM helices (UniProt FT TRANSMEM 7..29,
  35..58, 170..190, 202..227), PF01618 MotA_ExbB + PF20560 MotA_N, TIGR03818
  MotA1, PTHR30433:SF4.
- P. aeruginosa has two stators. MotAB is PA4954-PA4953, MotCD is
  PA1460-PA1461 [PMID:15629949 "One pair of proteins was designated MotAB
  (PA4954-4953) based on the current annotation of the P. aeruginosa PAO1
  genome and on the sequence similarity of the P. aeruginosa PA4954-4953
  proteins to the well-characterized E. coli stator proteins MotAB"].
  **Caution:** Doyle et al. 2004 (PMID:15375113) use the opposite names, calling
  PA4954-PA4953 *motCD* and PA1460-PA1461 *motAB*.
- Either stator supports swimming; loss of both MotA homologues abolishes
  motility [PMID:15375113 "Mutation of both genes encoding the MotA homologs or
  MotB homologs was sufficient to abolish motility."].
- The motAB single mutant swarms normally [PMID:15629949 "The Δ motAB mutant is
  able to swarm as well as the WT in agar concentrations up to 0.7%."]; the
  motCD mutant does not swarm on 0.5% agar or firmer; the double mutant neither
  swims nor swarms.
- Kuchma et al. 2015 (abstract only) report that motAB mutation *stimulates*
  swarming and relieves c-di-GMP repression
  [PMID:25349157 "Mutating the motAB genes restores swarming motility to a
  strain with artificially elevated levels of c-di-GMP as well as stimulates
  swarming in the wild-type strain, while overexpression of MotA from a plasmid
  represses swarming motility."].
- Chemotaxis is intact in stator mutants [PMID:15375113 "Therefore, the radial
  expansion defect observed for motAB strains in semisolid motility agar cannot
  be attributed to polar effects that disturb chemotaxis."], so the InterPro2GO
  chemotaxis row is an over-annotation.

## PseudoCAP IBA-seed assessment

The node-level GO_CENTRAL defect for PTN001252377 is recorded once, in
genes/PSEAE/motC (motC, PA1460, is the co-seed and has the direct single-mutant
swarming phenotype). The verdicts below are consistent with it and with the
parallel MotB node PTN001251133 (genes/PSEAE/motB).

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN001252377 | GO:0071978 bacterial-type flagellum-dependent swarming motility | 2 (Q9HUL1, G3XD73) | 29 (19 taxa) | GO:0071978, IMP, PMID:15629949 and PMID:25349157 (PseudoCAP) | INDIRECT-PHENOTYPE | MotA is a genuine stator subunit, so flagellar motility is its own process, but neither seed paper shows a swarming requirement for motAB: the single mutant swarms like wild type (PMID:15629949) or better (PMID:25349157), and the defect needs the motCD double mutant. The term is kept as non-core context for the gene. | motC (G3XD73), sound: the motCD single mutant fails to swarm at 0.5% agar or above and motCD in trans restores swarming | Yes, for P. aeruginosa — the motC seed carries it. But the node term is still too specific for the 29-leaf clade (Aquifex, Thermotoga, Helicobacter, Leptospira, Rhodopirellula stators, no swarming data), so a GO_CENTRAL repoint to GO:0071973 is requested on motC. |

Stator complex (GO:0120101) at the same node is seeded by E. coli MotA (P09348)
and is sound; it is accepted as the core location.

## Decisions summary

- ACCEPT: flagellum-dependent cell motility (IMP), stator complex (IBA), plasma
  membrane (IEA).
- KEEP_AS_NON_CORE: swarming motility (IBA, IEA, IMP x2).
- MARK_AS_OVER_ANNOTATED: chemotaxis (IEA, InterPro2GO).
- Counts: ACCEPT 3, KEEP_AS_NON_CORE 4, MARK_AS_OVER_ANNOTATED 1.
- Defects: PSEUDOCAP 2 (WRONG_EVIDENCE_CODE on the PMID:15629949 row,
  SUSPECTED; WRONG_TERM/CHECK on the PMID:25349157 row, SUSPECTED — abstract
  only). GO_CENTRAL 0 here; the node defect is on motC.
