# RGS2: signaling-regulator evidence review

All original annotation payloads, evidence codes, references and qualifiers were preserved. No new annotations were manufactured to populate a module. Actual Falcon and fallback research attempts failed authentication/quota; this is manual literature research, not provider-generated prose.

The whole record was reviewed, including secondary physiology and localization. Existing assertion specificity is judged independently of evidence code. Native, heterologous, mutant and orthology-based results are distinguished below.

## GO:0001965 G-protein alpha-subunit binding — ACCEPT
RGS2 binds activated G alpha and accelerates its intrinsic GTP hydrolysis. Wild-type biochemical selectivity favors Gq; the engineered Gi-binding mutants in PMID19478087 must not be presented as wild-type Gi specificity. Cell-based beta2-adrenergic Gi regulation is a distinct demonstrated context.
Sources: PMID:19478087, PMID:21291891

## GO:0005096 GTPase activator activity — ACCEPT
RGS2 binds activated G alpha and accelerates its intrinsic GTP hydrolysis. Wild-type biochemical selectivity favors Gq; the engineered Gi-binding mutants in PMID19478087 must not be presented as wild-type Gi specificity. Cell-based beta2-adrenergic Gi regulation is a distinct demonstrated context.
Sources: PMID:19478087, PMID:21291891

## GO:0003924 GTPase activity — MODIFY
RGS2 is the GTPase-activating regulator, whereas G alpha binds and hydrolyzes GTP. Refine the assigned enzyme role to the existing GAP activity; this is not removal of RGS2 from the GTPase cycle.
Sources: PMID:19478087

## GO:0005515 protein binding — REMOVE
The interaction claim is not denied, but bare protein binding is uninformative under the project protein-binding policy. Specific G alpha binding and the independently established signaling functions are retained.
Source handling: original payload retained; no fabricated supporting quote.

## GO:0005516 calmodulin binding — UNDECIDED
The accessible PMID10747990 abstract establishes calmodulin binding to tested RGS proteins and explicitly discusses RGS4, but does not identify whether RGS2 was one of the individually assayed proteins. Full target-level results could not be recovered. RGS2 calmodulin binding is therefore unresolved rather than rejected from a paralog-focused abstract.
Sources: PMID:10747990

## GO:0005634 nucleus — KEEP_AS_NON_CORE
Nuclear and nucleolar pools are supported for the longer human translation products by localization experiments and curated isoform-specific UniProt statements. These locations are retained as contextual pools, without asserting that every RGS2 isoform is nuclear.
Sources: PMID:11278586, PMID:17901199

## GO:0005730 nucleolus — KEEP_AS_NON_CORE
Nuclear and nucleolar pools are supported for the longer human translation products by localization experiments and curated isoform-specific UniProt statements. These locations are retained as contextual pools, without asserting that every RGS2 isoform is nuclear.
Sources: PMID:11278586, PMID:17901199

## GO:0005737 cytoplasm — ACCEPT
RGS2 has an experimentally supported cytoplasmic/cytosolic pool in addition to its membrane-associated signaling pool. The isoform-localization experiments and cell imaging support soluble localization; no exclusivity is inferred.
Sources: PMID:11278586, PMID:17901199

## GO:0005829 cytosol — ACCEPT
RGS2 has an experimentally supported cytoplasmic/cytosolic pool in addition to its membrane-associated signaling pool. The isoform-localization experiments and cell imaging support soluble localization; no exclusivity is inferred.
Sources: PMID:11278586, PMID:17901199

## GO:0005739 mitochondrion — KEEP_AS_NON_CORE
The shorter translation product beginning at the fourth initiation site has curated experimentally supported mitochondrial localization in PMID17901199. Retain the root organelle assertion separately from the membrane/nuclear distributions of other isoforms; no submitochondrial topology is claimed.
Sources: PMID:17901199

## GO:0005886 plasma membrane — MODIFY
RGS2 is a peripheral intracellular regulator recruited to the cytoplasmic face of the plasma membrane, not a transmembrane receptor. Refine to the already asserted cytoplasmic-side location, supported by its membrane targeting and Gq interaction.
Sources: PMID:11278586, PMID:28784619

## GO:0009898 cytoplasmic side of plasma membrane — ACCEPT
The intracellular membrane-associated pool positions RGS2 to bind and inactivate receptor-activated Gq. Membrane targeting of RGS2 is experimentally supported; this does not exclude its soluble or isoform-specific organellar pools.
Sources: PMID:11278586, PMID:28784619

## GO:0007186 G protein-coupled receptor signaling pathway — ACCEPT
RGS2 performs signal termination within GPCR signaling by accelerating G alpha GTP hydrolysis. This is direct regulatory participation rather than a mere expression association.
Sources: PMID:19478087, PMID:21291891

## GO:0008277 regulation of G protein-coupled receptor signaling pathway — MODIFY
The principal demonstrated regulatory action is attenuation of G protein signaling. Refine the unsigned regulation term to the existing negative-regulation term, while preserving separately supported context-specific downstream effects.
Sources: PMID:19478087, PMID:21291891

## GO:0045744 negative regulation of G protein-coupled receptor signaling pathway — ACCEPT
RGS2 accelerates G alpha inactivation and limits receptor signaling. Its biochemical Gq preference and cell-specific Gi-linked beta2-adrenergic termination are compatible; neither implies universal inhibition of every GPCR output.
Sources: PMID:19478087, PMID:21291891

## GO:0001975 response to amphetamine — KEEP_AS_NON_CORE
Rat source PMID26321241 reports RGS2 expression changes correlated with amphetamine intake in VTA and nucleus accumbens. Retain a contextual orthology-based stimulus-response annotation, not a claim that human RGS2 metabolizes amphetamine or necessarily drives addiction.
Sources: PMID:26321241

## GO:0045471 response to ethanol — KEEP_AS_NON_CORE
Chronic intermittent ethanol and withdrawal increased rat prefrontal RGS2 mRNA and protein. This supports a bounded conserved response annotation, not ethanol metabolism or a proven causal role in dependence.
Sources: PMID:28736108

## GO:0007283 spermatogenesis — MARK_AS_OVER_ANNOTATED
The traced mouse source PMID14581517 is a differential-expression survey of germ-cell stages. Expression during spermatogenesis alone does not establish that RGS2 performs a spermatogenic step, and no independent RGS2-specific functional mechanism was identified in this review. The transfer is over-specific for the demonstrated expression evidence, not proof that a reproductive role is impossible.
Sources: PMID:14581517

## GO:0010614 negative regulation of cardiac muscle hypertrophy — KEEP_AS_NON_CORE
Native mouse Rgs2 deletion under pressure overload increases Gq-linked hypertrophy and JNK activation, prevents adaptive increases in contractility and impairs relaxation (PMID19127022). These support the specific cardiac regulatory processes as comparative physiological functions, not constitutive human myocardial phenotypes or direct kinase activity.
Sources: PMID:19127022

## GO:0046329 negative regulation of JNK cascade — KEEP_AS_NON_CORE
Native mouse Rgs2 deletion under pressure overload increases Gq-linked hypertrophy and JNK activation, prevents adaptive increases in contractility and impairs relaxation (PMID19127022). These support the specific cardiac regulatory processes as comparative physiological functions, not constitutive human myocardial phenotypes or direct kinase activity.
Sources: PMID:19127022

## GO:0055119 relaxation of cardiac muscle — KEEP_AS_NON_CORE
Native mouse Rgs2 deletion under pressure overload increases Gq-linked hypertrophy and JNK activation, prevents adaptive increases in contractility and impairs relaxation (PMID19127022). These support the specific cardiac regulatory processes as comparative physiological functions, not constitutive human myocardial phenotypes or direct kinase activity.
Sources: PMID:19127022

## GO:0060452 positive regulation of cardiac muscle contraction — KEEP_AS_NON_CORE
Native mouse Rgs2 deletion under pressure overload increases Gq-linked hypertrophy and JNK activation, prevents adaptive increases in contractility and impairs relaxation (PMID19127022). These support the specific cardiac regulatory processes as comparative physiological functions, not constitutive human myocardial phenotypes or direct kinase activity.
Sources: PMID:19127022

## GO:0010855 adenylate cyclase inhibitor activity — KEEP_AS_NON_CORE
Alternative-initiation experiments directly show RGS2-dependent inhibition of adenylyl cyclase V with reduced efficacy of the shorter products. This secondary effector-inhibitory capability is retained independently of Gq GAP activity and is not evidence that RGS2 hydrolyzes cAMP.
Sources: PMID:17901199

## GO:0010976 positive regulation of neuron projection development — KEEP_AS_NON_CORE
PMID16820281 reports direct RGS2–tubulin interaction through residues 41–60, stimulation of microtubule polymerization, and gain/loss effects on NGF-induced neurites in PC12 cells. Retain the binding and neurite functions with this comparative cellular scope; they are distinct from the main GAP mechanism.
Sources: PMID:16820281

## GO:0048487 beta-tubulin binding — KEEP_AS_NON_CORE
PMID16820281 reports direct RGS2–tubulin interaction through residues 41–60, stimulation of microtubule polymerization, and gain/loss effects on NGF-induced neurites in PC12 cells. Retain the binding and neurite functions with this comparative cellular scope; they are distinct from the main GAP mechanism.
Sources: PMID:16820281

## GO:0017148 negative regulation of translation — KEEP_AS_NON_CORE
RGS2 directly interacts with eIF2B epsilon and inhibits translation through a region distinct from the determinants of G protein regulation. The independent primary evidence supports a secondary translation-control role rather than inferring it from altered proliferation.
Sources: PMID:19736320

## GO:0060087 relaxation of vascular associated smooth muscle — KEEP_AS_NON_CORE
PKGI-alpha binding and phosphorylation enhance RGS2-mediated restraint of vascular Gq signaling, supporting vascular smooth-muscle relaxation. This is signaling-mediated regulation, not a structural contractile role.
Sources: PMID:14608379

## GO:0060135 maternal process involved in female pregnancy — KEEP_AS_NON_CORE
The original rat myometrial study measured pregnancy-dependent expression and explicitly left its physiological role unknown. Independent mouse knockout experiments in PMID31030617 demonstrate RGS2-dependent uterine vascular remodeling and blood flow during pregnancy, supporting the conserved maternal process with a vascular, rather than proven direct parturition, mechanism.
Sources: PMID:12712095, PMID:31030617

## GO:0061052 negative regulation of cell growth involved in cardiac muscle cell development — KEEP_AS_NON_CORE
RGS2 loss enhances agonist-induced cardiomyocyte hypertrophy and cell growth in the native rat study; mouse pressure-overload genetics independently corroborates the antihypertrophic function. Retain the contextual cardiac growth regulation.
Sources: PMID:16380388, PMID:19127022

## GO:0071877 regulation of adenylate cyclase-inhibiting adrenergic receptor signaling pathway — KEEP_AS_NON_CORE
RGS2 ablation and overexpression identify it as a terminator of beta2-adrenergic Gi signaling in adult mouse cardiomyocytes and HEK293 assays. Retain this specific receptor/cell context without converting it into indiscriminate Gi GAP activity.
Sources: PMID:21291891

## GO:1900738 positive regulation of phospholipase C-activating G protein-coupled receptor signaling pathway — MODIFY
The traced mouse source PMID19127022 shows the opposite regulatory sign: Rgs2 loss enhances Gq signaling and PLCbeta inhibition rescues the exaggerated hypertrophy. RGS2 suppresses this PLC-activating branch; improved contractility is a downstream benefit of negative signaling regulation, not positive regulation of the Gq–PLC pathway.
Sources: PMID:19127022

## GO:1900924 negative regulation of glycine import across plasma membrane — UNDECIDED
The traced rat source PMID21798518 measures glycine-evoked electrical currents by whole-cell patch clamp, not glycine uptake. The live GO definition requires reduction of glycine import into the cell. This is a specific mismatch between the measured endpoint and the transferred transport claim; the inaccessible full text and lack of independent uptake evidence leave an actual RGS2 glycine-import mechanism unresolved.
Sources: PMID:21798518

## Research and access
Normal publication fetches and targeted refreshes are logged under `.cache/module-audit-logs/acetylcholine-*`. Canonical abstract-only caches were not manually rewritten. Full publisher recovery for cone localization is cited separately. PAINT assertions are treated as ancestral-node judgments, not pairwise transfers; target appearance among descendant evidence is not circular.

## Validation
Focused strict/schema, source/quote and ontology checks, record-section backfill, rendering and helper-generated history are recorded in the final panel proof.

## Final source and propagation audit

Original machine payloads and all qualifiers were compared with the authoritative baseline. There are no NOT assertions or new annotation rows in this 15-target panel. Full sources were inspected where a source-specific sign/mechanism challenge required them; unresolved fine-localization/source claims are retained as UNDECIDED rather than inferred absent. Bare binding removals apply the project policy and do not dispute experimental interactions.

UniProt/PANTHER placement inspected: `PTHR10845:SF43`. Broad G-alpha family PTHR10218 is GTP-BINDING PROTEIN ALPHA SUBUNIT; GRK PTHR24355 is G PROTEIN-COUPLED RECEPTOR KINASE/RIBOSOMAL PROTEIN S6 KINASE. Surprising official family names were not mechanically repointed. RGS6 current PTHR45746 placement does not invalidate a historical PAINT PTHR10845 assertion by itself.
