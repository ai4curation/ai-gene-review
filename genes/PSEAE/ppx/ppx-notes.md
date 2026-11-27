# ppx (PA5241, Q9ZN70) review notes

No deep-research API was available. Manual research on 2026-11-05: cached
publications (PMID:10382967 and PMID:24275100 abstract only; PMID:26576296 full
text), UniProt (reviewed), and QuickGO for the other PAINT seeds. PubMed MCP and
NCBI E-utilities returned server errors.

## Biology

- ppx encodes a 506-residue GppA/Ppx-family exopolyphosphatase, 41% identical to
  E. coli Ppx, located next to (and divergent from) ppk [PMID:10382967 "The
  predicted amino acid sequence of PPX is 41% identical with Escherichia coli
  PPX."]. Overproduced paPPX releases Pi from polyP of chain length 79 and 750
  [PMID:10382967 "Thus ppx encodes an enzyme that has exopoly(P)ase activity."].
- Purified recombinant paPpx: hydrolysis of polyP to polyPn-1 + Pi, activated by
  K+, NH4+ and Zn2+; Km 1.3-11 uM by chain length, kcat 40-57 s-1
  [PMID:26576296 "Pseudomonas aeruginosa exopolyphosphatase (paPpx; EC 3.6.1.11)
  catalyzes the hydrolysis of polyphosphates (polyP), producing polyPn-1 plus
  inorganic phosphate (Pi)."]. The same active site also transfers phosphate from
  polyP to ADP to make ATP [PMID:26576296 "We show that paPpx is also a
  polyphosphate:ADP phosphotransferase and that the active site is the same as
  that one involved in the hydrolase activity."], with kcat about 4 s-1, roughly
  a tenth of the hydrolase rate. This is a genuine secondary activity
  (KEEP_AS_NON_CORE for GO:0008976).
- Regulation and phenotypes [PMID:24275100, abstract only]: ppx is expressed from
  a sigma54/NtrC promoter under nitrogen limitation and a sigma70/PhoB promoter
  under Pi limitation; a ppx null mutant is altered in motility, pyocyanin,
  C6-C12 AHLs, rhamnolipids and biofilm [PMID:24275100 "Results obtained from the
  ppx null mutant demonstrated that Ppx is involved in the production of
  virulence factors associated with both acute infection (e.g. motility-promoting
  factors, blue/green pigment production, C6-C12 quorum-sensing homoserine
  lactones) and chronic infection (e.g. rhamnolipids, biofilm formation)."].
  These are downstream consequences of altered polyP/Pi homeostasis. Ppx does not
  catalyse rhamnolipid synthesis or make or sense AHLs, so the glycolipid
  biosynthetic process and quorum sensing rows are indirect-phenotype
  annotations (REMOVE, PSEUDOCAP WRONG_TERM, PROBABLE: the abstract states the
  data are mutant phenotypes, but I could not read the full text). Biofilm,
  swimming and swarming are organism-level process terms that GO routinely
  annotates from mutant phenotypes; kept as non-core.
- The "cellular response to nitrogen/phosphate starvation" IDA rows rest on
  promoter regulation (expression), which GO guidance does not treat as
  sufficient for "response to" terms; the abstract also notes that Ppx levels
  are held constant across conditions [PMID:24275100 "Molecular and physiological
  approaches used in this study indicated that P. aeruginosa maintains
  consistently proper levels of Ppx regardless of environmental conditions."].
  Marked as over-annotated.
- Location: peripheral membrane by similarity to E. coli Ppx (UniProt
  ECO:0000250); no direct data for P. aeruginosa.

## PseudoCAP IBA-seed assessment

Other seeds read from .cache/paint/IBD.gaf; their experimental MF rows checked in
QuickGO on 2026-11-05.

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN000768198 | GO:0016462 pyrophosphatase activity | 4 | 48 (39 taxa) | GO:0004309, IDA, PMID:10382967 (PseudoCAP); also EXP PMID:26576296 (UniProt) | SOUND | Overproduced enzyme releases Pi from polyP; confirmed with purified enzyme and kinetics in PMID:26576296. Exopolyphosphatase is_a pyrophosphatase. | E. coli Ppx P0AFL6, M. tuberculosis Ppx1 P9WHV5 (EXP GO:0004309, PMID:22880033), E. coli GppA P25552 (EXP/IDA GO:0008894) | Yes |
| PTN000768205 | GO:0004309 exopolyphosphatase activity | 2 | 8 (8 taxa) | as above | SOUND | as above | E. coli Ppx P0AFL6 | Yes |

The generic pyrophosphatase term at PTN000768198 correctly spans Ppx and GppA
(pppGpp 5'-phosphohydrolase); the exopolyphosphatase term sits on the Ppx
subclade. Both suit their clades. No PSEUDOCAP or GO_CENTRAL defect on the seed
rows. ppx itself receives the GO:0004309 and GO:0006798 IBAs from PTN000768205,
not the generic GO:0016462.

## Action summary

ACCEPT: GO:0004309 (EXP, IBA, IDA, IEA), GO:0006798 (IBA).
KEEP_AS_NON_CORE: GO:0008976 (EXP, IEA), GO:0005886 (ISS, IEA), GO:0044010,
GO:0071977, GO:0071978. MARK_AS_OVER_ANNOTATED: GO:0006995, GO:0016036.
TOO_GENERAL: GO:0006793. REMOVE: GO:0009247, GO:0009372 (PSEUDOCAP defects,
PROBABLE).
