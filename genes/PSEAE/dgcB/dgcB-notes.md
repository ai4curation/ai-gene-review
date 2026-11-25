# dgcB (PA5399, Q9HTG5) — research notes

## Identity

- UniProt Q9HTG5 (unreviewed), 653 aa, gene `dgcB`, ordered locus `PA5399`,
  *P. aeruginosa* PAO1 (NCBITaxon:208964). Matches the worklist entry (rank 35).
- UniProt has only a SubName, "DgcB, Dimethylglycine catabolism", and no
  FUNCTION, CATALYTIC ACTIVITY or SIMILARITY block; protein existence level 4
  (Predicted). Everything in the record is signature- or ARBA-derived.
- Architecture: five Phobius transmembrane helices in the N-terminal third
  (6-26, 68-87, 93-113, 134-153, 159-179), two PROSITE 4Fe-4S ferredoxin-type
  domains (236-266 and 311-342, PS51379, with PS00198), two copies of the
  cysteine-rich CCG domain (Pfam PF02754), DUF3483 (PF11982), Fer4_8 (PF13183),
  alpha-helical ferredoxin fold (SSF46548, IPR009051).
- PANTHER PTHR43255 / PTHR43255:SF1. The PANTHER family is
  "Heterodisulfide reductase iron-sulfur subunit C"; its members include
  *M. thermautotrophicus* HdrC (O27906), *B. subtilis* FadF (P45866),
  *Syntrophomonas wolfei* EtfAB:quinone oxidoreductase (Q0AZ32) and the
  membrane-anchored ferredoxin Csal_0991 (Q1QYW0). This is a family of
  **electron-transfer Fe-S subunits**, not of methyl-group-removing
  flavoenzymes — relevant to which half of DgcAB does the demethylation.

## What the primary paper shows

Wargo, Szwergold and Hogan 2008 (PMID:17951379) mapped the glycine betaine (GB)
catabolic route of *P. aeruginosa* genetically. For `dgcAB`:

- [PMID:17951379, "with mutations in the dgcAB (PA5398-PA5399) genes, which exhibit homology to"]
  [PMID:17951379, "genes that encode other enzymes with demethylase activity, are required for the"]
  [PMID:17951379, "conversion of DMG to sarcosine."]
- GB is a choline catabolite:
  [PMID:17951379, "intermediate in the catabolism of choline and carnitine, can serve as a sole"].
- `dgcAB` is induced by GB and DMG through the AraC-family regulator GbdR:
  [PMID:17951379, "growth on GB and DMG and for the induction of gbcA, gbcB, and dgcAB in response"].

The evidence for the DMG → sarcosine step is a **transposon-mutant growth
phenotype plus 13C NMR metabolite accumulation**, not an enzyme assay. The full
text (PMC2293255, read through PubMed Central; the local cache is abstract-only)
is explicit that no biochemistry was done: it states that characterization of the
biochemical activities of the `dgcA` and `dgcB` gene products remains a subject
for future research, describes PA5398 as a predicted flavin mononucleotide
oxidoreductase similar to a putative *Mesorhizobium loti* N-methylproline
demethylase, and PA5399 as a probable membrane-spanning ferredoxin Fe-S
oxidoreductase. The `dgcB` transposon mutant accumulated mostly DMG in the
13C-choline experiment.

So the pathway placement of `dgcB` is solid, but the specific enzymology is not:

- No reaction was measured, so neither of the two GO molecular functions on the
  gene is established. They are also **mutually exclusive mechanisms** for the
  same conversion: GO:0047865 dimethylglycine dehydrogenase activity is
  "N,N-dimethylglycine + electron-transfer flavoprotein + H2O = sarcosine +
  formaldehyde + reduced electron-transfer flavoprotein", whereas GO:0047866
  dimethylglycine oxidase activity is "N,N-dimethylglycine + H2O + O2 =
  formaldehyde + H2O2 + sarcosine". A single enzyme system does one or the other.
- The domain content points to a division of labour within DgcAB: the FMN
  oxidoreductase DgcA (PA5398) is the plausible site of methyl removal, while
  DgcB, with five transmembrane helices, two 4Fe-4S clusters and two CCG
  domains, has the architecture of the membrane-anchored electron-transfer
  subunit (as in HdrC and EtfAB:quinone oxidoreductase, its PANTHER relatives).
  On that reading `contributes_to` would fit DgcB better than `enables`, and the
  rest of the electron path (to menaquinone? to an ETF?) is unknown.
- The paper also reports that multiple `dgcA` rescue constructs failed to
  restore growth in the dgcA deletion, which the authors discuss in terms of
  complex stoichiometry or cotranscription — further reason to treat DgcAB as
  one system rather than two independent enzymes.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN000229983 | GO:0016491 oxidoreductase activity | 1 (sole seed) | 33 (17 taxa) | GO:0047865 dimethylglycine dehydrogenase activity \| IDA \| PMID:17951379 \| PseudoCAP; GO:0047866 dimethylglycine oxidase activity \| IDA \| PMID:17951379 \| PseudoCAP | INDIRECT-PHENOTYPE | The two seeding rows assert specific catalytic activities that the cited paper never measured: its evidence for dgcAB is loss of growth on DMG by transposon mutants plus 13C NMR accumulation of DMG, and its full text states that characterizing the biochemical activities of DgcA and DgcB remains future work. The two seeded terms also specify incompatible chemistries (ETF-dependent dehydrogenase versus O2-dependent oxidase), so at most one can be right, and the paper cannot distinguish them. The PAINT curator's generalisation to `oxidoreductase activity` is the right instinct and the node term is defensible on independent grounds — PTHR43255 is a family of Fe-S electron-transfer oxidoreductase subunits (HdrC, FadF, EtfAB:quinone oxidoreductase) and PA5399 itself has two 4Fe-4S ferredoxin domains and two CCG domains — but the IBD that propagates it to 33 leaves in 17 taxa has no measured activity anywhere in its support chain. The IBA on this gene is retained; the seed rows are marked over-annotated and the thinness of the IBD's grounding is reported. |

Defects recorded in the review: `PSEUDOCAP` `WRONG_EVIDENCE_CODE` (IDA should be
IMP for both molecular-function rows), `PSEUDOCAP` `WRONG_TERM` / `CHECK` (the
two mutually exclusive activity terms, possibly on the wrong subunit of DgcAB),
and `GO_CENTRAL` `CHECK` on PTN000229983 (sole seed is an indirect phenotype).

## Pathway context

choline → betaine aldehyde → glycine betaine (GB) → *GbcAB* → dimethylglycine
(DMG) → **DgcAB** → sarcosine → *SoxBDAG* → glycine. GbdR (PA5380, AraC family)
induces `gbcAB` and `dgcAB` in response to GB or DMG. GB and its products serve
as carbon or nitrogen sources, and the pathway is also the route by which
*P. aeruginosa* disposes of the osmolyte it accumulates.

## Open questions

- Which subunit removes the methyl group, and what is the immediate electron
  acceptor of DgcB's 4Fe-4S clusters (membrane quinone, an electron-transfer
  flavoprotein, or DgcA itself)?
- Is the one-carbon product free formaldehyde or a tetrahydrofolate adduct, as
  for the mammalian dimethylglycine dehydrogenase?
- Is DgcAB a stable membrane complex, as the failed `dgcA` complementation
  hints?
