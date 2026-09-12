# MCCC1 (Q96RQ3) review notes

## Deep research status
`just deep-research-falcon human Q96RQ3` fails in this worktree: `scripts/deep_research_wrapper.py`
is executed under system Python 3.9.5, which cannot evaluate the `dict | None` annotation at import
time (`TypeError: unsupported operand type(s) for |: 'type' and 'NoneType'`). This is a pre-existing
environment/venv-selection issue, not a content problem. No `-deep-research-falcon.md` was produced;
I did NOT fabricate one. Review grounded in UniProt (Q96RQ3), the seeded GOA TSV, the dismech disorder
KB (`3-Methylcrotonyl-CoA_Carboxylase_Deficiency.yaml`), and cached `publications/PMID_*.md`.

## Verified biology
MCCC1 = biotin-containing **alpha subunit** of mitochondrial **3-methylcrotonyl-CoA carboxylase (MCC)**,
a biotin-dependent carboxylase (EC 6.4.1.4). MCC catalyses the ATP-dependent carboxylation of
3-methylcrotonyl-CoA -> 3-methylglutaconyl-CoA, the committed carboxylation step of **leucine catabolism**
(downstream of isovaleryl-CoA dehydrogenase / IVD; L-leucine degradation UniPathway UPA00363, step 2/3
to HMG-CoA). Holoenzyme is an **alpha6-beta6 dodecamer** of MCCC1 (biotin carboxylase + biotinyl/BCCP
domain, carries biotin at Lys681, binds ATP) and MCCC2 (carboxyltransferase). Mitochondrial matrix
(N-terminal transit peptide 1-41, cleaved at Tyr41/Thr42; PMID:16023992). Deficiency of MCCC1 or MCCC2 =
3-methylcrotonyl-CoA carboxylase deficiency (3-MCC / MCC1D, MIM:210200), a common newborn-screening
finding, often benign/asymptomatic.

## Key supporting quotes (verbatim, grep-verified in cache)
- PMID:17360195 (abstract-only cache): "a heteromultimeric complex that is composed of alpha and beta
  subunits which are encoded by distinct genes"; "the stoichiometry of alpha and beta subunits are at
  a one:one ratio"; Km ATP 45 uM, 3-methylcrotonyl-CoA 74 uM. -> FUNCTION, CATALYTIC ACTIVITY, SUBUNIT,
  ComplexPortal complex. (Chu & Cheng 2007.)
- PMID:11170888 full text: "MCC, an heteromeric enzyme consisting of α (biotin-containing) and β
  subunits"; "725-residue protein with a biotin attachment site"; fungal mccA null used to demonstrate
  "the involvement of MCC in leucine catabolism".
- PMID:11181649 abstract: "MCC is a heteromeric mitochondrial enzyme composed of biotin-containing
  alpha subunits and smaller beta subunits."
- PMID:11401427 abstract: "mitochondrial biotin enzyme and plays an essential role in the catabolism of
  leucine and isovalerate"; "biotin carboxylase, and biotin-carrier domains"; "abundantly expressed in
  mitochondria-rich organs".
- PMID:16023992 abstract: two subunits "are imported into the mitochondrial matrix by the classical
  pathway"; cleavage site "Tyr41/Thr42 ... for MCCalpha".
- PMID:22869039 (Tong review): "Biotin-dependent carboxylases include ... 3-methylcrotonyl-CoA
  carboxylase (MCC) ... They contain biotin carboxylase (BC), carboxyltransferase (CT), and
  biotin-carboxyl carrier protein components." Family-level (review), NAS/TAS -> mark biotin
  carboxylase activity / biotin metabolic process as over-annotated (component activities of one
  domain, not the holoenzyme's committed MF).
- PMID:32561715 (Son 2020, full text): "MCCC1, a key enzyme in the Leu metabolic pathway"; "the
  Leu-metabolizing enzyme MCCC1"; siRNA knockdown -> autophagy/mTORC1. This is a knockdown/autophagy
  study, NOT a direct carboxylase-activity assay; UniProt attaches the ECO:0000269 catalytic-activity
  to it alongside 17360195. Accept the enzyme/leucine-metabolism role; note the catalytic MF is more
  directly supported by 17360195.
- UniProt INTERACTION: MCCC1–MCCC2 (Q9HCC0, NbExp=8) and MCCC1–OXCT2 (Q9BYC2, NbExp=3). The GOA
  `protein binding` IPIs point to exactly Q9HCC0 (MCCC2, the obligate partner) and Q9BYC2 (OXCT2).

## Annotation strategy
- Core MF: GO:0004485 methylcrotonoyl-CoA carboxylase activity (holoenzyme MF; MCCC1 contributes the
  BC + BCCP half). Accept the contributes_to IDA/IBA/EXP/NAS/EC copies; these are the core function.
- GO:0004075 biotin carboxylase activity (NAS, review) and GO:0006768 biotin metabolic process (NAS):
  MARK_AS_OVER_ANNOTATED — biotin carboxylase is a partial-reaction/domain activity of the alpha
  subunit, not the committed cellular MF; biotin metabolic process conflates the biotin *cofactor*
  requirement with actual biotin biosynthesis/utilisation metabolism.
- GO:0009374 biotin binding (NAS) and GO:0005524 ATP binding (IEA), GO:0046872 metal ion binding (IEA):
  cofactor/substrate binding, real (biotin at Lys681, ATP-grasp domain). Accept binding; metal ion
  binding is a generic InterPro ATP-grasp Mg2+ inference — keep as accept (plausible for ATP-grasp).
- Localization: mitochondrial matrix (multiple IDA/IEA/TAS) ACCEPT (core). mitochondrion (IBA/IDA/HTP)
  accept as correct-but-less-specific. cytosol (Reactome TAS, R-HSA transit-of-cytosolic-carboxylases
  reactions) = transient import intermediate only -> MARK_AS_OVER_ANNOTATED (steady-state is matrix).
- Complex: GO:1905202 methylcrotonoyl-CoA carboxylase complex ACCEPT (core CC).
- BP: GO:0006552 L-leucine catabolic process ACCEPT (core BP). GO:0009083 branched-chain amino acid
  catabolic process (NAS) — parent of leucine catabolism, correct but less specific -> KEEP_AS_NON_CORE.
- protein binding IPIs (bare GO:0005515): MARK_AS_OVER_ANNOTATED per policy (do not REMOVE). The
  MCCC2 partner is captured by the complex term; OXCT2 is a proteomic co-purification.
