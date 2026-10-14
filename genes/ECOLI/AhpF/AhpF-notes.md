# AhpF review notes

## 2026-10-02

- `just fetch-gene ECOLI AhpF` seeded UniProtKB:P35340 with 20 current GOA
  annotations. GOA has already migrated away from the obsolete
  `GO:0008785 alkyl hydroperoxide reductase activity`; the current molecular
  function rows include the InterPro-derived
  `GO:0102039 NADH-dependent peroxiredoxin activity`, which is over-scoped for
  AhpF alone, and a PAINT IBA row for `GO:0004791 thioredoxin-disulfide
  reductase (NADPH) activity`.
- Falcon deep research and the `perplexity-lite` fallback were unavailable on
  this EC2 process because no deep-research provider credentials were set. The
  review below is therefore based on the UniProt record plus cached GOA
  references.
- `just fetch-fitness ECOLI AhpF` could not write a fitness sidecar because no
  local FEBA database was installed and the LBL bulk source was unreachable.

## Function synthesis

- UniProt describes AhpF as alkyl hydroperoxide reductase subunit F and notes
  that it can use NADH or NADPH to reduce dyes directly or alkyl hydroperoxides
  when combined with AhpC: `It can use either NADH or NADPH as electron donor for
  direct reduction of redox dyes or of alkyl hydroperoxides when combined with
  the AhpC protein` [file:ECOLI/AhpF/AhpF-uniprot.txt].
- AhpF is not itself the peroxiredoxin peroxide-reducing subunit. Bieger and
  Essen summarize the division of labor: `The AhpF component ... channels
  electrons from NAD(P)H via a series of disulfides towards the AhpC component,
  which finally reduces the hydro-peroxide substrates` [PMID:10666639].
- Dip et al. solved EcAhpF and EcAhpC structures, showed EcAhpF binding to
  EcAhpC by isothermal titration calorimetry, and proposed a hydroperoxide
  scavenger model in which dimeric, extended AhpF forms a complex with the AhpC
  ring to accelerate AhpC catalysis [PMID:25372677].
- Kamariah et al. describe bacterial AhpF as a dedicated peroxiredoxin
  reductase that catalyzes rapid reduction of AhpC by accepting reducing
  equivalents from NADH and shuttling electrons from its C-terminal domain
  through the N-terminal domain to AhpC [PMID:28270505].
- The AhpF catalytic cycle depends on FAD and NADH binding in the C-terminal
  domain plus two redox-active disulfide centers. Kamariah et al. identify the
  C-terminal FAD/NADH-binding domain and Cys345/Cys348 redox center, the
  N-terminal Cys129/Cys132 redox center that reduces AhpC, and a 197-209 linker
  that allows the N-terminal domain to alternate between CTD- and AhpC-facing
  states [PMID:28270505].

## Annotation review cues

- `GO:0047134 protein-disulfide reductase [NAD(P)H] activity` is the best
  existing GO molecular function for AhpF scope. `GO:0102039
  NADH-dependent peroxiredoxin activity` names the EC 1.11.1.26
  hydroperoxide-consuming reaction and should be treated as a whole-system
  AhpC/AhpF activity that AhpF contributes to.
- `GO:0004791 thioredoxin-disulfide reductase (NADPH) activity` is mechanistically
  adjacent but should not be accepted as-is for AhpF. AhpF is a
  class-II pyridine nucleotide-disulfide oxidoreductase with a thioredoxin
  reductase-like C-terminal module, but the physiological electron acceptor is
  AhpC rather than thioredoxin and the curated AhpC/AhpF reaction is
  NADH-linked.
- AhpF genuinely participates in peroxide detoxification and hydrogen peroxide
  catabolism even though AhpC performs the peroxide attack: AhpF regenerates
  oxidized AhpC and supplies the electrons required for continuous peroxidase
  turnover.
- The specific complex term `GO:0009321 alkyl hydroperoxide reductase complex`
  is supported by the AhpC/AhpF structural/interaction paper and is better than
  the generic ARBA `GO:0032991 protein-containing complex` row.
- The HDA/IDA cytosol rows are high-throughput localization or proteomics rows.
  Their cached abstracts do not foreground AhpF, so use conservative support
  text from the high-throughput papers or the UniProt flatfile for soluble
  cytosolic localization; do not second-guess the experimental rows merely
  because the cached entries are abstract-only.
