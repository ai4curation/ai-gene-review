# HADH (Q16836) review notes

Gene: HADH (HGNC:4799); aka SCHAD, HAD1, HADHSC, M/SCHAD.
Protein: Hydroxyacyl-coenzyme A dehydrogenase, mitochondrial (HCDH_HUMAN). 314 aa precursor;
12-aa mitochondrial transit peptide; mature 13-314. EC 1.1.1.35.

## Core enzymatic function (SCHAD, EC 1.1.1.35)

HADH catalyzes the third step of the mitochondrial fatty-acid beta-oxidation spiral: the
NAD+-dependent oxidation of L-(3S)-3-hydroxyacyl-CoA to 3-ketoacyl-CoA.

- UniProt FUNCTION: "Mitochondrial fatty acid beta-oxidation enzyme that catalyzes the third
  step of the beta-oxidation cycle for medium and short-chain 3-hydroxy fatty acyl-CoAs (C4 to
  C10)" [Q16836 UniProt, ECO:0000269|PubMed:10231530, 11489939, 16725361].
- Reaction (Rhea:22432): "a (3S)-3-hydroxyacyl-CoA + NAD(+) = a 3-oxoacyl-CoA + NADH + H(+)";
  EC=1.1.1.35 [Q16836 UniProt CATALYTIC ACTIVITY].
- Substrate preference is short/medium chain. [PMID:10231530 "Human heart short chain
  L-3-hydroxyacyl-CoA dehydrogenase (SCHAD) catalyzes the oxidation of the hydroxyl group of
  L-3-hydroxyacyl-CoA to a keto group, concomitant with the reduction of NAD+ to NADH, as part
  of the beta-oxidation pathway."]
- Homodimer; crystal structures solved with NAD+/substrate. [PMID:10231530 "The homodimeric
  enzyme has been overexpressed in Escherichia coli, purified to homogeneity, and studied using
  biochemical and crystallographic techniques."]
- Catalytic mechanism: His158 general base, Glu170 electrostatic assist [PMID:10231530
  "His 158 serves as a general base, abstracting a proton from the 3-OH group of the substrate.
  Furthermore, the ability of His 158 to perform such a function may be enhanced by an
  electrostatic interaction with Glu 170"].
- Conformational interdomain shifting on cofactor/substrate binding [PMID:10840044
  "significant shifting of the NAD(+)-binding domain relative to the C-terminal domain occurs
  in the ternary and substrate-bound complexes"].

Distinct from HADHA (the long-chain, membrane-bound MTP alpha subunit). HADH is a soluble
matrix homodimer.

## Subcellular location

Mitochondrion matrix. [Q16836 UniProt SUBCELLULAR LOCATION "Mitochondrion matrix
{ECO:0000305|PubMed:8687463}."] Confirmed by high-confidence mitochondrial proteomics
[PMID:34800366 mitochondrial proteome, HTP]. Note a legacy LIFEdb IDA "cytoplasm" annotation
(GO:0005737) likely reflects an overexpressed GFP-fusion artifact, not the native location.

## Tissue expression

Expressed in liver, kidney, pancreas, heart and skeletal muscle. [PMID:8687463 "Northern blot
analysis reveals SCHAD mRNA to be expressed in liver, kidney, pancreas, heart and skeletal
muscle."] Notably expressed in islets of Langerhans [PMID:21990309 "highly expressed in heart,
liver, adipose tissue, and in the islets of Langerhans within the pancreas"].

## Moonlighting / regulatory role: GDH inhibition and insulin secretion (HHF4 / HHF7)

Loss-of-function HADH mutations cause hyperinsulinaemic hypoglycaemia. This was the FIRST
fatty-acid-oxidation defect associated with hyperinsulinism, revealing a link between FAO and
insulin secretion.

- First patient / P258L: [PMID:11489939 "This is the first defect in fatty acid beta-oxidation
  that has been associated with hyperinsulinism and raises interesting questions about the ways
  in which changes in fatty acid and ketone body metabolism modulate insulin secretion by the
  beta cell."] The P258L variant abolishes catalytic activity [PMID:11489939 "Expression studies
  showed that the P258L enzyme had no catalytic activity."]; <5% residual activity in
  fibroblast mitochondria [PMID:11489939 "In fibroblast mitochondria, the activity was less than
  5% that of controls."].
- All early patients had hyperinsulinism, suggesting a regulatory role [PMID:16725361 "All
  these patients presented with hypoglycemia associated with hyperinsulinism (HI). This
  association suggests that there is a role for M/SCHAD in regulating the pancreatic secretion
  of insulin."].
- MECHANISM (protein-protein, partly enzyme-independent): HADH binds and inhibits glutamate
  dehydrogenase 1 (GLUD1); loss of this inhibition de-represses GDH-driven amino-acid-stimulated
  insulin secretion. UniProt records this from mouse ortholog (Q61425): [Q16836 UniProt
  FUNCTION "Plays a role in the control of insulin secretion by inhibiting the activation of
  glutamate dehydrogenase 1 (GLUD1), an enzyme that has an important role in regulating amino
  acid-induced insulin secretion (By similarity)."] and [Q16836 UniProt SUBUNIT "Interacts with
  GLUD1; this interaction inhibits the activation of glutamate dehydrogenase 1 (GLUD1) (By
  similarity)."] This GDH-inhibition mechanism is the basis for it being "partly independent of
  beta-oxidation activity" — the protein-protein interaction is a separate molecular function
  (enzyme inhibitor activity) from the dehydrogenase catalysis.
- Mouse Hadh-/- KO: elevated insulin, low glucose [PMID:21990309 "Blood glucose concentrations
  in the fasted and postprandial state were significantly lower in hadh(-/-) mice, whereas
  insulin levels were elevated."]; islets hypersecrete insulin [PMID:21990309 "insulin secretion
  in response to glucose and glucose plus palmitate was elevated in isolated islets of knockout
  mice."]

Disease (UniProt): HADH deficiency [MIM:231530] (hypoglycemia, hepatoencephalopathy, myopathy/
cardiomyopathy, sudden death) and Hyperinsulinemic hypoglycemia familial 4 (HHF4) [MIM:609975].
(OMIM also uses HHF7 in some sources; UniProt entry uses HHF4.)

## Thermogenesis / body weight (mouse; ISS in human)

Mouse KO data implicate Hadh in adaptive thermogenesis and body-weight regulation.
[PMID:21990309 "our data indicate that SCHAD is involved in thermogenesis, in the maintenance
of body weight, and in the regulation of nutrient-stimulated insulin secretion."] and
[PMID:21990309 "during cold exposure, knockout mice were unable to clear triglycerides from the
plasma and to maintain their normal body temperature, indicating that SCHAD plays an important
role in adaptive thermogenesis."] The GO term positive regulation of cold-induced thermogenesis
(GO:0120162) is ISS from mouse — a downstream physiological consequence of impaired FAO, not a
distinct molecular function; treat as non-core.

## Spermatogenesis (By similarity, mouse)

UniProt: [Q16836 UniProt FUNCTION "Plays a role in the maintenance of normal spermatogenesis
through the reduction of fatty acid accumulation in the testes (By similarity)."] Keyword-derived
GO:0007283 (IEA from UniProtKB-KW). Downstream/By-similarity; non-core.

## Annotation-review reasoning summary

- Core MF: GO:0003857 (3S)-3-hydroxyacyl-CoA dehydrogenase (NAD+) activity — strongly supported
  by EXP/IDA (PMID:10231530, 11489939, 16725361), IBA, TAS. ACCEPT (core).
- NAD+ binding GO:0070403 (IDA PMID:10840044) — ACCEPT; molecular detail of the catalytic MF.
- identical protein binding GO:0042802 (IDA PMID:10231530) — homodimer; ACCEPT but non-core
  (descriptive of quaternary structure; the homodimer crystal structure supports it).
- GO:0016509 long-chain (3S)-3-hydroxyacyl-CoA dehydrogenase activity (IEA RHEA) — HADH prefers
  short/medium chain; long-chain is HADHA. UniProt does list a long-chain Rhea reaction "By
  similarity" (ECO:0000250|UniProtKB:P00348, pig). MODIFY/over-annotation: the defining,
  preferred function is short/medium-chain; long-chain is at best minor. Mark as over-annotated /
  keep non-core rather than core. Use MARK_AS_OVER_ANNOTATED (does not contradict but misrepresents
  preference).
- GO:0016491 oxidoreductase activity, GO:0016616 (CH-OH donor, NAD acceptor) — correct but
  generic parents of GO:0003857; KEEP_AS_NON_CORE.
- GO:0016740 transferase activity (UniProtKB-KW, in DR lines) — NOT in GOA tsv, so not a row to
  review; the "Transferase" keyword is spurious for HADH (it is an oxidoreductase). Not in scope.
- GO:0006631 fatty acid metabolic process (IEA InterPro), GO:0006635 fatty acid beta-oxidation
  (IBA, IDA, IEA) — beta-oxidation is the specific correct BP. ACCEPT GO:0006635 (core BP);
  GO:0006631 is the generic parent -> KEEP_AS_NON_CORE.
- mitochondrion GO:0005739 (IBA is_active_in, IDA HPA, IEA, HTP, TAS) and mitochondrial matrix
  GO:0005759 (IEA SubCell, TAS Reactome x7) — matrix is correct specific location. ACCEPT matrix
  (core); mitochondrion = generic parent, KEEP_AS_NON_CORE.
- cytoplasm GO:0005737 (IDA LIFEdb GO_REF:0000054) — overexpressed fusion-protein localization;
  HADH is matrix. MARK_AS_OVER_ANNOTATED (not native).
- Insulin-secretion terms: regulation of insulin secretion GO:0050796 (ISS UniProtKB GO_REF:0000024
  from mouse Q61425; also IEA Ensembl) — well-supported moonlighting role; KEEP_AS_NON_CORE
  (genuine but secondary). negative regulation of insulin secretion GO:0046676 (IEA Ensembl) is
  more precise and matches the GDH-inhibition mechanism -> KEEP_AS_NON_CORE.
- response to insulin GO:0032868, response to hormone GO:0009725, response to activity GO:0014823,
  response to xenobiotic GO:0009410 (all IEA Ensembl from rat ortholog) — generic transcriptional/
  physiological responses, weakly informative; KEEP_AS_NON_CORE (not contradicted, low value).
- positive regulation of cold-induced thermogenesis GO:0120162 (ISS x2) — mouse KO phenotype;
  KEEP_AS_NON_CORE.
- Reactome mitochondrial protein degradation rows (R-HSA-9838035/9838081/9838093/9838289) are
  CLPXP/LONP1 "binds/degrades matrix proteins" reactions — they annotate matrix LOCATION via
  HADH being a substrate, NOT a degradation function. The located_in GO:0005759 they assert is
  correct. ACCEPT as location evidence (non-core).

## core_functions plan

1. (3S)-3-hydroxyacyl-CoA dehydrogenase activity (GO:0003857) / fatty acid beta-oxidation
   (GO:0006635) / mitochondrial matrix (GO:0005759). PRIMARY.
2. Enzyme inhibitor activity (GO:0004857) toward GLUD1 / negative regulation of insulin
   secretion (GO:0046676). SECONDARY moonlighting (By similarity / ISS — flag full_text basis).
