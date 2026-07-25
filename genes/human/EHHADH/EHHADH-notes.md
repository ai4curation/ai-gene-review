# EHHADH (Q08426, ECHP_HUMAN) — Gene Review Notes

## Identity and overview

EHHADH is the human peroxisomal **L-bifunctional protein** (LBP; also "peroxisomal
bifunctional enzyme", PBE/PBFE; "multifunctional enzyme 1", MFE1). It is a single
723-residue polypeptide encoded on chromosome 3q26.3-3q28
[PMID:8188243 "localization of the corresponding gene on chromosome 3q26.3-3q28"].

The protein carries two (arguably three) catalytic activities of the peroxisomal
fatty-acid β-oxidation spiral in one chain:
- an N-terminal **2-enoyl-CoA hydratase / Δ3,Δ2-enoyl-CoA isomerase** module
  (EC 4.2.1.17; EC 5.3.3.8), and
- a C-terminal **L-3-hydroxyacyl-CoA dehydrogenase** module (EC 1.1.1.35, NAD+-dependent).

UniProt annotates the domain architecture directly:
`REGION 1..282 "Enoyl-CoA hydratase / isomerase"` and
`REGION 283..572 "3-hydroxyacyl-CoA dehydrogenase"`
[file:human/EHHADH/EHHADH-uniprot.txt "REGION          1..282"],
[file:human/EHHADH/EHHADH-uniprot.txt "REGION          283..572"].

UniProt FUNCTION: "Peroxisomal trifunctional enzyme possessing 2-enoyl-CoA
hydratase, 3-hydroxyacyl-CoA dehydrogenase, and delta 3, delta 2-enoyl-CoA isomerase
activities. Catalyzes two of the four reactions of the long chain fatty acids
peroxisomal beta-oxidation pathway"
[file:human/EHHADH/EHHADH-uniprot.txt "Peroxisomal trifunctional enzyme possessing 2-enoyl-CoA"].

## Reaction chemistry (steps 2 and 3 of peroxisomal β-oxidation)

The hydratase step: `a (3S)-3-hydroxyacyl-CoA = a (2E)-enoyl-CoA + H2O` (EC 4.2.1.17,
RHEA:16105) [file:human/EHHADH/EHHADH-uniprot.txt "a (3S)-3-hydroxyacyl-CoA = a (2E)-enoyl-CoA + H2O"].
The dehydrogenase step: `a (3S)-3-hydroxyacyl-CoA + NAD(+) = a 3-oxoacyl-CoA + NADH +`
`H(+)` (EC 1.1.1.35, RHEA:22432)
[file:human/EHHADH/EHHADH-uniprot.txt "a 3-oxoacyl-CoA + NADH +"].
Note the **L (3S)** stereochemistry: EHHADH generates/uses the (3S)-3-hydroxyacyl-CoA
intermediate, in contrast to the D-bifunctional protein HSD17B4, which uses the
opposite chirality: "With HSD17B4, catalyzes the hydration of trans-2-enoyl-CoA and
the dehydrogenation of 3-hydroxyacyl-CoA, but with opposite chiral specificity"
[file:human/EHHADH/EHHADH-uniprot.txt "the dehydrogenation of 3-hydroxyacyl-CoA, but with opposite chiral"].

The enzyme acts on a chain-length range; UniProt lists catalytic activity entries for
C6 (hexanoyl), C10 (decanoyl), C16 (hexadecanoyl) and the C16 dicarboxylic (hexadecanedioyl)
series. Kinetic parameters were measured for the dicarboxylic/long-chain substrates:
`KM=0.3 uM for (2E)-hexadecenedioyl-CoA` and `KM=10.4 uM for (2E)-hexadecenoyl-CoA`
[file:human/EHHADH/EHHADH-uniprot.txt "KM=0.3 uM for (2E)-hexadecenedioyl-CoA"].

## Direct enzymatic evidence (PMID:15060085, Ferdinandusse et al. 2004)

This is the key experimental paper (abstract-only in cache; `full_text_available: false`).
Using recombinant human LBP expressed in a yeast fox2 (DBP) deletion mutant plus patient
fibroblast studies, it showed that peroxisomes (not mitochondria) β-oxidize C16
dicarboxylic acid, and that "the main enzymes involved in beta-oxidation of C16DCA are
SCOX, both LBP and DBP, and sterol carrier protein X"
[PMID:15060085 "the main enzymes involved in \nbeta-oxidation of C16DCA are SCOX, both LBP and DBP"].
Importantly it states: "This is the first indication of a specific function for LBP,
which has remained elusive until now"
[PMID:15060085 "This is the first indication \nof a specific function for LBP, which has remained elusive until now"].
This paper is the IDA source in GOA for enoyl-CoA hydratase activity (GO:0004300),
(3S)-3-hydroxyacyl-CoA dehydrogenase (NAD+) activity (GO:0003857), long-chain (3S)-3-
hydroxyacyl-CoA dehydrogenase (NAD+) activity (GO:0016509), and fatty acid β-oxidation
(GO:0006635). The dicarboxylic-acid/omega-oxidation-product role and the C16DCA KM are
the defining physiological niche distinguishing EHHADH from HSD17B4/DBP.

## Subcellular localization

Peroxisomal matrix protein; imported via a C-terminal PTS1 (type-1 peroxisomal
targeting) tripeptide **SKL** at residues 721-723 (`MOTIF 721..723 "Microbody
targeting signal"`) [file:human/EHHADH/EHHADH-uniprot.txt "Microbody targeting signal"].
PMID:1651711 demonstrated PTS1-dependent import: "A tripeptide sequence, SKL, located
at the carboxyl-terminus of human bifunctional enzyme appears to be the targeting
signal for the peroxisomal importation"
[PMID:1651711 "SKL, located at the carboxyl-terminus of human bifunctional \nenzyme appears to be the targeting signal"],
and deletion of the last nine residues blocks import
[PMID:1651711 "A deletion of the last nine amino acid residues at the \ncarboxyl-terminus of this polypeptide prevents its peroxisomal import"].
Immunocytochemistry localized the bifunctional protein to peroxisomes of human kidney
proximal tubules [PMID:2895531 "bifunctional protein \n(enoyl-CoA hydratase, 3-hydroxyacyl-CoA dehydrogenase)"],
[PMID:2895531 "immunoreactive peroxisomes were \ndistinctly visualized in proximal tubular epithelial cells"], and of human liver
[PMID:9053548 "subcellular localization of peroxisomal proteins (catalase, the \nthree beta-oxidation enzymes"].

## Tissue expression

Liver and kidney, strongly in terminal proximal tubule segments:
"Liver and kidney. Strongly expressed in the terminal segments of the proximal tubule.
Lower amounts seen in the brain"
[file:human/EHHADH/EHHADH-uniprot.txt "Strongly expressed in the"]. Northern analysis
originally showed highest expression in liver and kidney
[PMID:8188243 "RNA analysis shows one band with highest intensity in liver and \nkidney"].

## Disease

Fanconi renotubular syndrome 3 (FRTS3, MIM:615605), autosomal dominant. The disease
variant is not caused by loss of β-oxidation but by **mistargeting** of EHHADH: the
p.E3K variant is "mistargeted to mitochondria; results in impaired mitochondrial
oxidative phosphorylation and defects in the transport of fluids across the epithelium
of renal proximal tubular cells"
[file:human/EHHADH/EHHADH-uniprot.txt "mitochondria; results in impaired mitochondrial oxidative"]. UniProt DISEASE:
"generalized dysfunction of the proximal kidney tubule resulting in decreased solute
and water reabsorption ... FRTS3 inheritance is autosomal dominant"
[file:human/EHHADH/EHHADH-uniprot.txt "generalized"]. (Source PMID:24401050, not in cache.)
The enzyme is absent in generalized peroxisome-biogenesis disorders: "Absent in patients
suffering with peroxisomal disorders such as Zellweger syndrome, neonatal
adrenoleukodystrophy and infantile Refsum disease"
[file:human/EHHADH/EHHADH-uniprot.txt "Absent in patients suffering with peroxisomal disorders"].

## Regulation / PTM

Enzyme activity is enhanced by acetylation: "Enzyme activity enhanced by acetylation"
[file:human/EHHADH/EHHADH-uniprot.txt "Enzyme activity enhanced by acetylation"];
"Acetylated, leading to enhanced enzyme activity"
[file:human/EHHADH/EHHADH-uniprot.txt "Acetylated, leading to enhanced enzyme activity"]
(sites Lys-165/171/346/584; source PMID:20167786, not in cache). EHHADH is a classic
PPARα target gene (peroxisome-proliferator inducible), consistent with its being one of
the four "classic" inducible peroxisomal β-oxidation enzymes, though that regulatory
detail is not quoted from the UniProt file here.

## Interactions

- **Catalase (CAT, P04040)** — enzyme binding, IPI, PMID:16781659. Yeast two-hybrid +
  affinity purification + co-IP showed L-bifunctional enzyme interacts with catalase:
  "catalase physically interacts with L-bifunctional enzyme (L-BFE)"
  [PMID:16781659 "catalase physically \ninteracts with L-bifunctional enzyme (L-BFE)"]; proposed to help localize catalase at
  the site of H2O2 production. This is a biologically plausible peroxisomal-matrix
  interaction (catalase detoxifies the H2O2 produced by acyl-CoA oxidase upstream in the
  same pathway).
- The large set of **GO:0005515 "protein binding" IPI** annotations
  (PMID:25416956, PMID:31515488, PMID:32296183, PMID:33961781, PMID:36217029,
  PMID:40205054) derive from high-throughput interactome maps (Y2H HuRI / affinity-MS /
  spatial proteomics / SARS-CoV-2 contactome). The IntAct partner lists in the UniProt
  entry (AARS2, ACTB, ACTG1, DES, MID1, SSNA1, TPP2, catalase-family, many TRIMs, etc.)
  are largely non-peroxisomal and non-specific; these are uninformative for EHHADH's
  molecular function and are marked over-annotated (bare "protein binding" is
  discouraged in core functions). PMID:36217029 is a SARS-CoV-2 N-protein interaction
  (xeno), of no relevance to native EHHADH function.

## Core function summary

Two (three) catalytic MFs, all peroxisomal-matrix, all in the fatty-acid β-oxidation
spiral:
1. **enoyl-CoA hydratase activity (GO:0004300)** — hydrates 2-trans-enoyl-CoA to
   L-(3S)-3-hydroxyacyl-CoA (step 2). IDA PMID:15060085.
2. **(3S)-3-hydroxyacyl-CoA dehydrogenase (NAD+) activity (GO:0003857)** — NAD+-dependent
   oxidation of L-(3S)-3-hydroxyacyl-CoA to 3-oxoacyl-CoA (step 3). IDA PMID:15060085;
   requires NAD+ binding (GO:0070403). The long-chain-specific variant GO:0016509 is a
   more precise child (IDA PMID:15060085).
3. **Δ3,Δ2-enoyl-CoA isomerase activity (GO:0004165)** — auxiliary activity for
   unsaturated-fatty-acid oxidation (ISS/IEA, by similarity to rat P07896).

Core BP: **fatty acid beta-oxidation (GO:0006635)**, specifically the peroxisomal
acyl-CoA-oxidase-initiated variant (GO:0033540); physiological niche is degradation of
medium/long-chain **dicarboxylic acids** (omega-oxidation products) and the branched-chain
substrate 2-methyl-2E-butenoyl-CoA. Core CC: **peroxisome (GO:0005777) / peroxisomal
matrix (GO:0005782)**.

## Annotation-review decisions (rationale)

- Experimental MF/BP/CC annotations sourced to PMID:15060085 (hydratase, dehydrogenase,
  long-chain dehydrogenase, β-oxidation) and the IDA peroxisome-localization annotations
  (PMID:9053548, PMID:2895531, PMID:1651711) → **ACCEPT** (core).
- IBA (GO_REF:0000033) for dehydrogenase, peroxisome, β-oxidation → **ACCEPT** (phylogenetically
  well-supported, matches experimental).
- ISS/IEA duplicates of the two core activities and peroxisome/β-oxidation → **ACCEPT**
  (consistent with experimental).
- GO:0004165 Δ3,Δ2-enoyl-CoA isomerase (ISS/IEA) and GO:0016863 (parent) → **KEEP_AS_NON_CORE**:
  a real auxiliary activity of the N-terminal module (by similarity), but not the defining
  core function; supported only by similarity, not human IDA.
- GO:0018812 "3-hydroxyacyl-CoA dehydratase activity" (RHEA IEA + Reactome TAS) → **MODIFY**
  to GO:0004300. The RHEA/Reactome mapping labels the hydratase reaction as a "dehydratase";
  GO:0004300 (enoyl-CoA hydratase) is the correct, curated term for this enzyme's step-2
  activity and is already independently annotated by IDA.
- Broad IEA parent terms (GO:0003824 catalytic activity; GO:0016491 oxidoreductase activity;
  GO:0016616 oxidoreductase acting on CH-OH … NAD/NADP; GO:0006631 fatty acid metabolic
  process) → **MARK_AS_OVER_ANNOTATED**: correct but uninformatively general; better specific
  terms are already present.
- GO:0070403 NAD+ binding (IEA:InterPro) → **ACCEPT** as non-core supporting activity of the
  dehydrogenase module.
- GO:0005829 cytosol (IEA:Ensembl and Reactome TAS) → **MARK_AS_OVER_ANNOTATED**: the cytosol
  annotations reflect the transient pre-import (PTS1-folded) cargo state in the Reactome
  peroxisomal-import pathway; the mature functional enzyme is peroxisomal-matrix, and IDA
  evidence localizes it to peroxisomes. Not a genuine steady-state functional location.
- GO:0019899 enzyme binding IPI PMID:16781659 (catalase) → **KEEP_AS_NON_CORE**: a specific,
  biologically plausible peroxisomal interaction, but not a molecular function per se.
  The IEA (Ensembl-projected) enzyme-binding duplicate → **MARK_AS_OVER_ANNOTATED**.
- All bare GO:0005515 "protein binding" IPI (6 HT-interactome PMIDs) → **MARK_AS_OVER_ANNOTATED**
  (per policy, never REMOVE an IPI); uninformative and dominated by non-peroxisomal HT hits.
- NAS annotations (PMID:8188243) for the two activities, β-oxidation, peroxisome → **ACCEPT**:
  author-stated but corroborated by experimental annotations.
- Reactome TAS for the two activities and peroxisomal-matrix/cytosol → ACCEPT (activities/matrix)
  or MARK_AS_OVER_ANNOTATED (cytosol import-intermediate).

## QA re-review — 2026-07-23

Conservative QA pass of `EHHADH-ai-review.yaml` (50 annotations). No edits made; the
review is biologically and curatorially sound and validates clean.

- Validation: `✓ Valid` under default, `--strict`, `--verbose`, and `--terms`. No
  warnings, no PENDING.
- Same-term action consistency: verified by hand across all recurring terms — each has a
  single consistent action across evidence types (GO:0003857 ACCEPT×6, GO:0004300 ACCEPT×4,
  GO:0006635 ACCEPT×5, GO:0005777 ACCEPT×6, GO:0005515 MARK_AS_OVER_ANNOTATED×6,
  GO:0018812 MODIFY×2, GO:0005829 MARK_AS_OVER_ANNOTATED×3, GO:0016863 over-annotated×2,
  GO:0004165 KEEP_AS_NON_CORE×2, GO:0019899 KEEP_AS_NON_CORE×2, GO:0005782 ACCEPT×3).
- `protein binding` (GO:0005515): all 6 HT-interactome IPIs are MARK_AS_OVER_ANNOTATED
  (none ACCEPT); correct per IPI-never-REMOVE policy.
- core_functions: two catalytic MFs (GO:0004300 hydratase, GO:0003857 dehydrogenase) are
  captured with specific curated terms, not over-generalized; ids all in correct GO aspect.
- Note (left as-is): the GO:0016509 long-chain-dehydrogenase annotations (IEA + IDA) use
  the verbatim supporting_text "KM=0.3 uM for (2E)-hexadecenedioyl-CoA", which is an
  *enoyl-CoA (hydratase-substrate)* KM from UniProt rather than a dehydrogenase-substrate
  KM. It is verbatim, demonstrates long-chain/dicarboxylic substrate handling, and the
  ACCEPT action is independently justified by the PMID:15060085 IDA; UniProt has no
  long-chain dehydrogenase-specific KM to substitute, so no change was warranted.
