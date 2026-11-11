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
  the AhpC protein` [file:ECOLI/ahpF/ahpF-uniprot.txt].
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


## 2026-10-26 — native AhpC/AhpF module re-review

Re-reviewed every original annotation against native E. coli evidence and cross-species donor comparisons. The 53 ordered original annotation payloads and four raw UniProt/GOA files are preserved; no NEW rows are added. Actual Falcon plus perplexity-lite fallback attempts failed, as did FEBA retrieval (no reachable local or remote source); publication retrieval succeeded. Logs are in `.cache/module-audit-logs/alkyl-hydroperoxide-classical/`. No generated provider report or fitness result was fabricated.

The current raw P35340 record gives `GN Name=ahpF`. The historical `genes/ECOLI/AhpF/AhpF-*` artifacts are relocated to `genes/ECOLI/ahpF/ahpF-*`, retaining raw bytes. Earlier journal references to the uppercase folder describe the prior state and are superseded by this update. Existing history identity is frozen and `superseded_by` records the new canonical target. Dependent PANTHER family citations and three project machine indexes are updated as a necessary rename consequence; this is not a new family or taxon assignment.

Native E. coli work establishes the NADH→AhpF→AhpC relay [PMID:28270505, “The mutants also exhibited a decrease in H2O2 reduction by the AhpF-AhpC ensemble.”]. The peroxide-attacking AhpC and NADH-oxidizing AhpF perform different chemical steps. Existing reviews retain explicit individual molecular functions and record contribution to the overall NADH-dependent reaction. This is judged from the chemistry, not an ordinary GOA relationship string. The GO convention for assigning the whole-system MF to the catalytic subunit remains a question. No arbitrary thioredoxin or AhpF partner from another species is substituted into the native route.

Native genetics distinguishes low endogenous peroxide removal from high-peroxide catalase capacity [PMID:11717276, “These data demonstrate that in wild-type cells Ahp rather than catalase is the primary scavenger of an endogenous inducer of the OxyR regulon.”]. Broad oxidative response is refined to both hydrogen-peroxide and alkyl-hydroperoxide responses, rather than keeping a common ancestor as non-core. Core cell-redox homeostasis is retained as direct maintenance of the peroxide environment; it is not simply an ancestor of cellular oxidant detoxification. QuickGO definitions and children were retrieved on 2026-10-26 and saved with the actual lookup logs.

### Acceptor and cofactor scope

The PAINT-node refinement from GO:0004791 to GO:0047134 is grounded in the native E. coli AhpC-facing N-terminal relay and NADH/FAD electron-transfer architecture. It is not an argument from the number of donor genes and does not claim an absolute inability to reduce thioredoxin. PMID:10828978 studies Salmonella AhpF expressed in E. coli; the expression host does not make it a native E. coli AhpF experiment. The normally recovered full CiteSeerX PDF shows ineffective standard thioredoxin-coupled assays but extremely slow thioredoxin reduction during long incubations. This bounds a family-wide negative, not a new physiological E. coli thioredoxin pathway.

The broad flavin-binding annotation is refined to the already-present FAD-binding term. The broad NAD-binding term is refined to both NADH and NAD+ binding because native structural evidence describes both substrate and product states [PMID:28270505, “the substrate (NADH)- and product (NAD + )-bound crystal structures revealed that the NADH domain has to rotate back-and-forth by about 65°”]. No exclusive NADH-versus-NADPH kinetic ratio is transferred from Salmonella. The paired peroxide-reduction experiments establish the physiological route tested, while the native AhpF abstract also permits NAD(P)H electron input [PMID:10666639].

### Final paired-reaction decision after annotation-reviewer consultation

The preceding historical MODIFY treatment of GO:0102039 is superseded. Native E. coli genetics and reconstitution establish the AhpCF coupled reaction, and the ordinary GOA relationship string is inert in this review. Both AhpC rows and the AhpF row are ACCEPT, consistent with the separately reviewed Salmonella and Bacillus components. This accepts the real coupled activity without asserting that an isolated subunit catalyzes both half-reactions. The individual molecular functions and `contributes_to_molecular_function` core representation remain explicit. H. pylori's NADH rows are a different biological question because the tested native donor is NADPH through thioredoxin, not AhpF.
