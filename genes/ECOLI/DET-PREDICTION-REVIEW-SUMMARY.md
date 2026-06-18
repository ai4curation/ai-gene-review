# E. coli DeepECTF (DET) prediction review — summary

Reviews of 7 *E. coli* K-12 genes. For each gene: a full `<GENE>-ai-review.yaml`
(annotation-by-annotation GO review + core functions) and a `review:` block added to
`<GENE>-det-predictions-review.yaml` assessing the DeepECTF EC prediction.

**Method / integrity notes**
- All DeepECTF prediction verdicts were derived independently from primary data
  (UniProt records, GOA, the DeepECTF paper PMID:37963869, primary literature, and
  in-house bioinformatics). The pre-filled stub `description` fields (which mirrored
  the de-Crécy-Lagard evaluation paper) were discarded and rewritten.
- **No de-Crécy-Lagard sources were used** (not PMID:40703034, 10.1093/g3journal/jkaf169,
  10.1101/2024.07.01.601054, nor other papers from that lab such as Thiaville 2014 or
  El Yacoubi). The only mentions of that name in the files are explicit "was not used"
  disclaimers.
- All 14 YAML files validate (`GeneReview` and `PredictionReview` target classes).

## DeepECTF prediction verdicts

| Gene | UniProt | Predicted EC | Verdict | error_type | Basis |
|------|---------|--------------|---------|-----------|-------|
| **fepE** | P26266 | 2.7.13.3 histidine kinase | REP | FREQUENCY_BIAS | Wzz-family polysaccharide co-polymerase (PCP-1; crystal structure); only ~18-aa cytoplasmic tail, no DHp/HATPase kinase module. Histidine kinase is the textbook default/frequency-bias label. |
| **yciO** | P0AFR4 | 2.7.7.87 TC-AMP synthase | PLI | PARALOG_OVERANNOTATION | Degenerate TsaC paralog: own alignment shows catalytic Asn lost (TsaC `STSANL` → YciO `STSLML`); TsaC is essential & non-redundant; in-vitro activity weak (0.07 U/mg) + uncoupled ATP hydrolysis. |
| **yegV** | P76419 | 2.7.1.92 5-dehydro-2-deoxygluconokinase | UNC | — | Uncharacterized PfkB sugar kinase; substrate unknown. Predicted substrate's pathway (myo-inositol catabolism) absent from K-12; operon (yegTUV/ADP-glucose) points elsewhere. |
| **ygfF** | P52037 | 1.1.1.47 glucose 1-dehydrogenase | UNC | — | Robust in-vitro activity (305 U/mg) but no K-12 glucose-1-DH pathway; SDR promiscuity; closest homolog is a 3-oxoacyl-ACP reductase (FabG-like). In-vivo role unresolved. |
| **yjdM** | P0AFJ1 | 3.11.1.2 phosphonoacetate hydrolase | NPI | IN_VITRO_NOT_IN_VIVO | Zinc-ribbon protein (YjdM family), not an alkaline-phosphatase-superfamily C-P hydrolase; *phnA/yjdM* shown genetically to have **no** role in phosphonate metabolism (Metcalf & Wanner 1993); "phnA" is a name collision with the *Pseudomonas* enzyme. |
| **yjhQ** | P39368 | 2.3.1.189 mycothiol synthase | NPI | PATHWAY_CONTEXT_IGNORED | GNAT acetyltransferase, but mycothiol biosynthesis is actinobacterial and absent from *E. coli* (uses glutathione). YjhQ is the verified antitoxin of the YjhX(TopAI)–YjhQ TA system. |
| **yrhB** | P46857 | 4.1.2.50 6-carboxytetrahydropterin synthase | NPI | PATHWAY_CONTEXT_IGNORED | 94-aa Imm35 (bacteriocin-immunity) protein, no PTPS tunnel fold, no homology to the enzyme; the step is dedicated to QueD (ygcM/b2765) in *E. coli*. yrhB itself remains uncharacterized. |

## Notable annotation-review outcomes (`-ai-review.yaml`)

- **fepE** — REMOVE the legacy `protein tyrosine kinase activity` (IBA from over-broad
  PANTHER PTHR32309) and the `ferric-enterobactin transmembrane transporter activity` /
  `ferric-enterobactin import` (IMP, 1987 polar-insertion proposal, superseded). Add NEW
  `O antigen biosynthetic process` (Wzz chain-length determinant; Tran & Morona 2013,
  Murray 2003, Kalynych 2012).
- **yciO** — TC-AMP synthase annotations marked MARK_AS_OVER_ANNOTATED (weak/promiscuous,
  not the dedicated function); dsRNA-binding IEA marked over-annotated. Supporting
  bioinformatics in `genes/ECOLI/yciO/yciO-bioinformatics/`.
- **yegV** — generic kinase/transferase IEAs accepted as appropriately general; substrate
  unknown; operon context (ADP-glucose-responsive yegTUV, glycogen) noted.
- **ygfF** — glucose-1-DH annotations kept as non-core (real in vitro, not the established
  physiological function); core MF set at the general SDR CH-OH oxidoreductase level.
- **yjdM** — phosphonoacetate hydrolase annotations marked over-annotated; NEW zinc ion
  binding (Zn-ribbon, CxxC knuckles) proposed as the defensible molecular function.
- **yjhQ** — GNAT acetyltransferase MF accepted; `protein binding` IPI accepted as the
  functionally meaningful antitoxin–TopAI interaction; antitoxin role recorded in core
  functions.
- **yrhB** — no GOA annotations; kept honestly uncharacterized (Imm35 domain has no GO
  mapping); function recorded as unknown with hypotheses in suggested questions.
