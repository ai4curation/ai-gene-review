# GAMT (human) — review notes

UniProt: Q14353 (GAMT_HUMAN). Gene: GAMT (HGNC:4136), chr 19p13.3. EC 2.1.1.2.
236 aa, ~26 kDa. Class I-like SAM-binding methyltransferase superfamily, RMT2 family.

## Core molecular function

GAMT is guanidinoacetate N-methyltransferase, the second and terminal enzyme of
endogenous creatine biosynthesis. It transfers a methyl group from
S-adenosyl-L-methionine (SAM/AdoMet) to guanidinoacetate (GAA), yielding creatine
and S-adenosyl-L-homocysteine (SAH).

- UniProt FUNCTION/CATALYTIC ACTIVITY [UniProtKB:Q14353]:
  "Converts guanidinoacetate to creatine, using S-adenosylmethionine as the methyl donor"
  Reaction: guanidinoacetate + S-adenosyl-L-methionine = creatine + S-adenosyl-L-homocysteine + H(+);
  Rhea:RHEA:10656; EC=2.1.1.2.
- PATHWAY [UniProtKB:Q14353]: "Amine and polyamine biosynthesis; creatine biosynthesis;
  creatine from L-arginine and glycine: step 2/2." (AGAT/GATM makes GAA in step 1; GAMT methylates it in step 2.)
- Substrate binding residues (UniProt features): SAM at residues 20, 50, 69-74, 90-92, 117-118, 135;
  guanidinoacetate at 42, 46, 135, 171-172. Confirmed by human crystal structure with SAH
  (PDB 3ORH; SGC) and rat ternary-complex structures.
- The reaction obligatorily consumes SAM and releases SAH (a coproduct that is itself a
  product-inhibitor of methyltransferases), so the activity is also an S-adenosylmethionine
  catabolic / SAH-producing process.

## Quantitative role as a SAM methyl-group consumer

Creatine synthesis is one of the largest single consumers of methyl groups in the body.
[ScienceDirect topic overview, web] "Creatine biosynthesis consumes 40% of methyl groups
produced as S-adenosylmethionine" — the GAMT step is the methylation event, making GAMT a
major sink for SAM-derived methyl groups and a node linking creatine metabolism to
one-carbon / methionine metabolism.

## Localization

GAMT is a soluble cytosolic enzyme. Rat liver subcellular fractionation localizes GAMT
activity to the cytosolic fraction; human Reactome places the reaction in the cytosol
(GO:0005829). The IBA pan-ancestor "nucleus" call (GO:0005634) has no direct experimental
support for GAMT and is best treated as an over-annotation; GAMT is a soluble metabolic
enzyme with no described nuclear function. "cytoplasm" (GO:0005737) is supportable but is a
broad localization rather than the defining function.

## Tissue expression

- UniProt TISSUE SPECIFICITY [UniProtKB:Q14353, PMID:8651275]: "Expressed in liver."
- Human Protein Atlas: "Tissue enhanced (liver, skeletal muscle, tongue)."
- Liver is a central organ of creatine synthesis: GAA produced largely by kidney (AGAT) is
  released into circulation and methylated to creatine in liver. Brain (astrocytes,
  oligodendrocytes) also expresses GAMT for local CNS creatine synthesis.

## Disease: GAMT deficiency / Cerebral creatine deficiency syndrome 2 (CCDS2, MIM:612736)

Autosomal recessive. GAMT deficiency was the first described inborn error of creatine
metabolism.
- [PMID:8651275 "In two children with an accumulation of guanidinoacetate in brain and a
  deficiency of creatine in blood, a severe deficiency of guanidinoacetate methyltransferase
  (GAMT) activity was detected in the liver."]
- [PMID:8651275 "It causes a severe developmental delay and extrapyramidal symptoms in early
  infancy and is treatable by oral substitution with creatine."]
- UniProt DISEASE: "developmental delay and regression, intellectual disability, severe
  disturbance of expressive and cognitive speech, intractable seizures, movement
  disturbances, severe depletion of creatine and phosphocreatine in the brain, and
  accumulation of guanidinoacetic acid in brain and body fluids."
- Many disease-causing missense variants abolish enzymatic activity in functional assays
  (e.g. W45R, M50L, H51P, A54P, L159P, L166P, L197P, R208P; characterized in PMID:24415674,
  PMID:26003046, PMID:26319512), confirming that loss of GAMT catalytic activity is the
  molecular basis of disease. UniProt FUNCTION also notes "Important in nervous system
  development (PubMed:24415674)" — this is a downstream organismal consequence of creatine
  deficiency rather than a distinct direct molecular role.

## Annotation-relevant judgments

- MF: guanidinoacetate N-methyltransferase activity (GO:0030731) — core; well supported
  (IMP from PMID:8651275 enzyme-deficiency demonstration; IBA; IEA from EC/Rhea/InterPro).
- MF: methyltransferase activity (GO:0008168, Reactome TAS) — correct but a generic parent of
  GO:0030731; over-general, mark as over-annotated.
- BP: creatine biosynthetic process (GO:0006601) — core (IDA PMID:8651275; IBA; IEA; TAS).
- BP: creatine metabolic process (GO:0006600, Reactome TAS) — correct but parent of the more
  specific biosynthetic term; keep as non-core.
- BP: muscle contraction (GO:0006936, TAS PMID:8547310) — GAMT is not part of the muscle
  contraction machinery; this is a distal physiological consequence of creatine availability,
  not a direct GAMT process. Over-annotation.
- CC: cytosol (GO:0005829, Reactome TAS) — supported localization; keep as non-core.
- CC: cytoplasm (GO:0005737, IBA) — broad, supportable; keep as non-core.
- CC: nucleus (GO:0005634, IBA) — unsupported pan-ancestor localization; over-annotation.
- MF: protein binding (GO:0005515) — three IPI annotations from high-throughput interactome
  screens (PMID:28514442, PMID:32296183, PMID:33961781; partners include FARS2/O95363,
  RAB24/Q969Q5, TRIM39/Q9HCM9-2 per UniProt IntAct). Bare "protein binding" is uninformative
  and no functional consequence is established; over-annotation per curation guidelines.
  The interactions are real (IPI) so REMOVE is not appropriate; MARK_AS_OVER_ANNOTATED.

## Interaction-paper PMIDs (cached, abstract-level high-throughput screens)
- PMID:28514442 Huttlin et al., BioPlex "Architecture of the human interactome..."
- PMID:32296183 Luck et al., HuRI "A reference map of the human binary protein interactome."
- PMID:33961781 Huttlin et al., BioPlex 3.0 "Dual proteome-scale networks..."
None characterize a specific GAMT binding function.

## Sources
- UniProtKB:Q14353 (cached uniprot.txt)
- PMID:8651275 (cached; abstract)
- Web: ScienceDirect "Guanidinoacetate Methyltransferase" overview (40% SAM methyl groups);
  GATM/GAMT local creatine synthesis (ScienceDirect S0006899321004844).
</content>
</invoke>
