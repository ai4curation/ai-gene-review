# COQ9 (human) — gene review notes

UniProt: O75208 (COQ9_HUMAN). Gene: COQ9 (HGNC:25302), synonym C16orf49. 318 aa precursor;
N-terminal mitochondrial transit peptide (1–44), mature chain 45–318. Two isoforms
(O75208-1 canonical; O75208-2 truncated, non-functional in the CoQ context).

## Core biology (what COQ9 is and does)

COQ9 is a **mitochondrial lipid-binding protein** essential for coenzyme Q10 (CoQ10 /
ubiquinone) biosynthesis. It is **non-catalytic**: it has no known enzymatic activity.
Its job is to **bind lipophilic CoQ-pathway intermediates (aromatic isoprenes) and
membrane phospholipids and present the substrate (5-demethoxyubiquinone, DMQ) directly to
the di-iron hydroxylase COQ7**, thereby activating the penultimate C6-hydroxylation step of
CoQ biosynthesis. COQ9 and COQ7 form a lipid-binding module within the larger COQ synthome
("complex Q" / COQ metabolon).

- Membrane-associated protein that "warps the membrane surface to access and bind aromatic
  isoprenes with high specificity, including ubiquinone (CoQ) isoprene intermediates and
  presents them directly to COQ7, therefore facilitating the COQ7-mediated hydroxylase step"
  [file:human/COQ9/COQ9-uniprot.txt "to access and bind aromatic isoprenes with high specificity, including"].
- Structural fold: TetR/TFR-family all-alpha (bacterial transcriptional-regulator) fold with a
  hydrophobic lipid-binding pocket; adopts an atypical TFR dimer orientation and is NOT
  predicted to bind DNA. UniProt notes it is "Structurally similar to the bacterial FadR
  protein (fatty acid metabolism regulator protein)"
  [file:human/COQ9/COQ9-uniprot.txt "Structurally similar to the bacterial FadR protein"].

## Key evidence by publication

- **PMID:25339443** (Lohman et al. 2014, PNAS; crystal structure 4RHP, abstract-only in cache):
  "COQ9 has structural homology to the TFR family of bacterial transcriptional" regulators;
  "Our structure also reveals a lipid-binding site"; mass-spec shows COQ9 associates with
  "multiple lipid species, including CoQ itself"; "COQ9 specifically interacts with COQ7
  through a series of conserved residues"; and "COQ9 might serve to present its bound lipid"
  to COQ7. Crystallized with di-palmitoyl-phosphatidylethanolamine bound (BINDING residue 244).
  Homodimer (SUBUNIT). Basis for GOA IDA: lipid binding (GO:0008289), protein homodimerization
  (GO:0042803), IPI with COQ7 (Q99807), ubiquinone biosynthetic process (ISS).
- **PMID:30661980** (Lohman et al. 2019, Mol Cell; structures 6AWL, 6DEW; full text available):
  COQ9 "repurposes the bacterial TetR fold to bind aromatic isoprenes" with high specificity,
  including CoQ intermediates; associates with cardiolipin-rich membranes and "warps the
  membrane surface to access this cargo"; identifies a molecular interface between COQ9 and
  the hydroxylase COQ7, motivating a model whereby COQ9 "presents intermediates directly to
  CoQ" enzymes. Basis for GOA IDA: isoprenoid binding (GO:0019840), ubiquinone biosynthetic
  process; IPI with COQ7.
- **PMID:38425362** (Nicoll et al. 2024, Nat Catal; full text available): in vitro
  reconstruction of the animal COQ metabolon (COQ3,4,5,6,7,9). "COQ9 has been shown to
  facilitate COQ7 activity in vivo"; and consistently, "addition of COQ9 increased catalytic
  efficiency by 1.5-fold, substantiating its role for COQ7 function". Confirms COQ9 is an
  accessory/activating partner of COQ7, not itself an enzyme. Basis for GOA IDA: isoprenoid
  binding and ubiquinone biosynthetic process.
- **PMID:36306796** (Manicki et al. 2022, Mol Cell; cryo-EM 7SSP/7SSS; NOT cached): multimeric
  human COQ7:COQ9 octamer with membrane lipids captured in a pseudo-bilayer; W240 required for
  the octamer. (Referenced via UniProt SUBUNIT; not a GOA reference here.)
- **PMID:27499296** (Floyd et al. 2016, Mol Cell; full text available): mitochondrial protein
  interaction map; source of ComplexPortal IDA mitochondrial inner membrane, IPI protein
  binding (COQ5 Q5HYK3, COQ8A Q8NI60, COQ7 Q99807, ACSF2 Q96CM8), and part_of ubiquinone
  biosynthesis complex (GO:0110142).
- **PMID:28927698** (Stefely & Pagliarini 2017, Trends Biochem Sci; review; full text): defines
  "complex Q" / CoQ-synthome; "Complex Q is thought to contain proteins required for the
  terminal stage of CoQ biosynthesis (COQ3–COQ9)"; "Most eukaryotic CoQ is generated at the
  inner mitochondrial membrane". Basis for ComplexPortal NAS ubiquinone biosynthetic process.
- **PMID:32296183** (Luck et al. 2020, HuRI): high-throughput binary interactome (Y2H). Source
  of many low-specificity IPI protein-binding partners (ADIPOQ, BMP10, etc.), most of which are
  not biologically meaningful CoQ-pathway interactors. Treat as over-annotation of bare
  "protein binding".
- **PMID:34800366** (Morgenstern et al. 2021): high-throughput human mitochondrial proteome —
  supports mitochondrial localization (HTP).
- **PMID:20833797** (Zhao et al. 2011): phosphoproteome of muscle mitochondria — supports
  mitochondrial localization (HDA).
- **PMID:19375058** (Duncan et al. 2009, AJHG; NOT cached): nonsense mutation in COQ9 causes
  autosomal-recessive neonatal-onset primary CoQ10 deficiency (COQ10D5). Disease basis in
  UniProt DISEASE record.

## Localization

Mitochondrion (UniProt SUBCELLULAR LOCATION, by similarity to mouse Q8K1Z0). Functions on the
matrix face of the mitochondrial inner membrane as part of the CoQ synthome; associates with
cardiolipin-rich membranes (PMID:30661980). GO terms in GOA: mitochondrion (GO:0005739),
mitochondrial inner membrane (GO:0005743). Reactome adds inner-membrane TAS localizations for
the CoQ-pathway reaction steps.

## Curation decisions (summary)

- **ACCEPT** core, experimentally-grounded annotations: lipid binding (GO:0008289, IDA
  PMID:25339443), isoprenoid binding (GO:0019840, IDA PMID:38425362 & PMID:30661980),
  ubiquinone biosynthetic process (GO:0006744, multiple IDA/ISS/IBA), ubiquinone biosynthesis
  complex (GO:0110142, IPI PMID:27499296), protein homodimerization activity (GO:0042803, IDA
  PMID:25339443), mitochondrion / mitochondrial inner membrane localizations.
- **KEEP_AS_NON_CORE**: the specific COQ7 IPI (GO:0005515, PMID:25339443 / PMID:30661980 with
  Q99807) — real and functionally important but "protein binding" is uninformative for the MF;
  the meaningful biology is captured by the lipid/isoprenoid binding + complex membership +
  ubiquinone biosynthetic process. Keep as non-core rather than remove (never REMOVE an IPI).
- **MARK_AS_OVER_ANNOTATED**: the many bare "protein binding" IPI annotations from the HuRI
  binary interactome (PMID:32296183) and non-CoQ IntAct partners (PMID:27499296 ACSF2) — bare
  GO:0005515 with no functional MF content; policy is MARK_AS_OVER_ANNOTATED (not REMOVE) for
  IPI protein binding.
- No catalytic MF is asserted. COQ9 is not a hydroxylase/monooxygenase. The UniProt DR line
  `GO:0008047 enzyme activator activity; IEA:Ensembl` is NOT in GOA (not an existing
  annotation), but it is biologically apt: COQ9 activates the COQ7 hydroxylase step by
  presenting substrate. It is used in `core_functions` (contributes_to) to capture the
  presenter/activator role without inventing a catalytic activity.

## Core function modeling

1. Lipid/isoprenoid binding (GO:0008289 / GO:0019840) — binds membrane phospholipids and
   lipophilic CoQ intermediates (aromatic isoprenes incl. DMQ) in a hydrophobic TetR-fold
   pocket. directly_involved_in ubiquinone biosynthetic process (GO:0006744); in_complex
   ubiquinone biosynthesis complex (GO:0110142); location mitochondrial inner membrane.
2. Substrate presentation / COQ7 hydroxylase activation — molecular_function lipid binding
   with contributes_to_molecular_function enzyme activator activity (GO:0008047), reflecting
   that COQ9 presents DMQ to COQ7 and increases COQ7 catalytic efficiency (~1.5-fold in vitro).
3. Homodimerization (GO:0042803) — forms homodimers and higher-order COQ7:COQ9 tetramers/octamers.
