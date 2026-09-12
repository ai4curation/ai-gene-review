# ACAA1 (human) review notes

UniProt: P09110 (THIK_HUMAN). Gene: ACAA1 (HGNC:82). Synonyms: ACAA, PTHIO.
Product: 3-ketoacyl-CoA thiolase, peroxisomal (peroxisomal thiolase 1).

## Core biology (grounded in UniProt P09110)

- ACAA1 catalyzes the **final, thiolytic-cleavage step of the peroxisomal fatty-acid
  beta-oxidation spiral**: a 3-oxoacyl-CoA (3-ketoacyl-CoA) is cleaved by coenzyme A to
  yield an acyl-CoA shortened by two carbons plus acetyl-CoA (EC 2.3.1.16).
  [file:human/ACAA1/ACAA1-uniprot.txt "Responsible for the thiolytic cleavage of straight chain 3-"] (line wraps to "keto fatty acyl-CoAs")
  Reaction: [file:human/ACAA1/ACAA1-uniprot.txt "Reaction=an acyl-CoA + acetyl-CoA = a 3-oxoacyl-CoA + CoA"] (physiological direction right-to-left).
- Acts on **straight-chain** substrates spanning short, medium, long, and very-long chains.
  [file:human/ACAA1/ACAA1-uniprot.txt "Catalyzes the"] "cleavage of short, medium, long, and very long straight chain 3-oxoacyl-CoAs".
- Plays an important role in **peroxisomal fatty acid beta-oxidation**.
  [file:human/ACAA1/ACAA1-uniprot.txt "Plays an important role in fatty acid peroxisomal"] (wraps to "beta-oxidation").
  PATHWAY: [file:human/ACAA1/ACAA1-uniprot.txt "Lipid metabolism; peroxisomal fatty acid beta-oxidation."]
- Localizes to the **peroxisome / peroxisomal matrix**; imported via a cleaved N-terminal
  PTS2 targeting signal recognized by PEX7 (co-receptor PEX5L). ACAA1 is a **homodimer**.
  [file:human/ACAA1/ACAA1-uniprot.txt "SUBCELLULAR LOCATION: Peroxisome"]
  [file:human/ACAA1/ACAA1-uniprot.txt "Homodimer (Ref.19). Interacts (via PTS2-type peroxisomal"]

## Division of labour among peroxisomal thiolases (important for over-annotation calls)

- The classic peroxisomal beta-oxidation "spiral 1" for straight-chain (V)LCFA is:
  ACOX1 (oxidase) -> EHHADH/HSD17B4 (bifunctional hydratase/dehydrogenase) -> **ACAA1 (thiolase)**.
- The **branched-chain / bile-acid** thiolytic step is carried by **SCPx/SCP2 (thiolase 2)**, not ACAA1.
  However, an older (1987) study of a single human patient concluded a **single** peroxisomal
  3-oxoacyl-CoA thiolase handled both VLCFA and coprostanoic (bile-acid intermediate) chain
  shortening: [PMID:2882519 "a single peroxisomal 3-oxoacyl-CoA thiolase is involved in the oxidative chain shortening of both very-long-chain fatty acids and the coprostanoic acids"].
  This predates the discovery of SCPx; current understanding assigns the bile-acid branch to SCPx.
  Bile-acid-related annotations to ACAA1 are therefore treated as non-core.

## Evidence per publication (cached)

- **PMID:2882519** (Schram 1987, abstract/full-text=abstract only). Human patient with peroxisomal
  3-oxoacyl-CoA thiolase deficiency; peroxisomal beta-oxidation of [14C]palmitoyl-CoA <10% of control;
  restored by adding purified rat thiolase. Establishes ACAA1 role in fatty acid beta-oxidation and
  in VLCFA + bile-acid chain shortening. [PMID:2882519 "peroxisomal 3-oxoacyl-CoA thiolase (acyl-CoA:acetyl-CoA C-acyltransferase, EC 2.3.1.16) was"] (wraps to "deficient").
  Note: GOA annotates GO:0120524 "long-chain fatty acyl-CoA oxidase activity" (IMP) and GO:0008775
  "acetate CoA-transferase activity" (EXP) to this paper — both are the WRONG molecular function
  (oxidase / CoA-transferase, not thiolase). Over-annotations, not removed (experimental).
- **PMID:11734571** (Ferdinandusse 2001, abstract only). Peroxisomal beta-oxidation of C24:6n-3 ->
  C22:6n-3 (DHA formation); enzymes involved are SCOX (ACOX), DBP, and "both 3-ketoacyl-CoA thiolase
  and SCPx". [PMID:11734571 "the main enzymes involved in beta-oxidation of C24:6n-3 to C22:6n-3 are"] (wraps to "SCOX, DBP, and both 3-ketoacyl-CoA thiolase and SCPx"). Supports role in PUFA/DHA
  peroxisomal beta-oxidation. GOA annotates GO:0008775 (acetate CoA-transferase, EXP) to this paper
  via Reactome — wrong MF; over-annotation.
- **PMID:2318981** (Clayton 1990, abstract only). Bile acid profiles in a patient whose liver had NO
  immunoreactive peroxisomal 3-oxoacyl-CoA thiolase; accumulation of C27 bile-acid intermediates
  (varanic acid, THCA). [PMID:2318981 "whose \nliver contained no immunoreactive peroxisomal 3-oxoacyl-CoA thiolase"]. Supports VLCFA metabolic process (IMP) and bile acid metabolic process (IMP, non-core).
- **PMID:2365812** (Heikoop 1990, abstract only). RCDP fibroblasts: impaired maturation of peroxisomal
  3-oxoacyl-CoA thiolase; reduced thiolase activity reduces peroxisomal beta-oxidation of palmitoyl-CoA;
  peroxisomal localization via catalase-containing fractions. Supports fatty acid beta-oxidation (IMP)
  and peroxisome localization (IDA). [PMID:2365812 "The reduction of 3-oxoacyl-CoA \nthiolase activity results in a decrease in the rate of peroxisomal \nbeta-oxidation of palmitoyl-CoA."]
- **PMID:22057399** (Kunze 2011, full text). PTS2/PEX7 import; ACAA1 (acyl-CoA thiolase) is a mammalian
  PTS2-carrying protein "exerting the last step of fatty acid beta-oxidation". Mutagenesis of the PTS2.
  Supports peroxisome localization (IDA, is_active_in). [PMID:22057399 "acyl-CoA thiolase exerting the last step of fatty acid β-oxidation"].
- **PMID:25538232** (Kunze 2015, full text). PTS2-mediated import; trimeric PEX7-PEX5L-cargo complex.
  Supports peroxisome localization (IDA). Thiolase used as the prototypical PTS2 cargo.
- **PMID:18281296** (Omi 2008, abstract only). pLon does NOT process PTS2-containing 3-ketoacyl-CoA
  thiolase (PTL). Cited by GOA as a "protein binding" IPI with UniProtKB:Q86WA8 (LONP2). The paper's
  finding is essentially negative for thiolase processing; the physical-interaction annotation is a
  bare "protein binding" (uninformative) — MARK_AS_OVER_ANNOTATED per policy.
  [PMID:18281296 "does not process PTS2-containing"] (wraps to "3-ketoacyl-coenzyme A thiolase (PTL)").
- **PMID:32296183** (Luck 2020, HuRI). High-throughput binary interactome (Y2H). Source of two IntAct
  "protein binding" IPI calls (TFCP2/Q12800, FEM1A/Q9BSK4). Systematic Y2H hits, no functional context;
  bare protein binding -> MARK_AS_OVER_ANNOTATED.
- Localization IDA papers (peroxisome): PMID:9053548, PMID:1347505, PMID:17881773, PMID:2895531,
  PMID:19479899 — immunocytochemistry/fractionation placing thiolase in peroxisomes (human liver,
  kidney, testis, fibroblasts). All abstract-only in cache; consistent with authoritative peroxisome
  localization. Accept as non-core (redundant location support).
- **PMID:19946888** (membrane proteome of NK cells, HDA). Places ACAA1 in "membrane" — a soluble
  peroxisomal matrix enzyme; membrane is spurious co-fractionation. Over-annotation (HDA, keep-as-non-core/over).

## Molecular function assessment

- Core MF = **acetyl-CoA C-acyltransferase activity (GO:0003988)** = 3-ketoacyl-CoA thiolase,
  EC 2.3.1.16. Definition confirmed via OLS: "acyl-CoA + acetyl-CoA = CoA + 3-oxoacyl-CoA."
- GO:0003985 (acetyl-CoA C-acetyltransferase, EC 2.3.1.9, "2 acetyl-CoA = acetoacetyl-CoA + CoA"):
  UniProt lists this only by similarity (ECO:0000250|UniProtKB:P21775, rat). It is the acetoacetyl-CoA
  thiolase reaction (short-chain condensation), a minor/ancestral activity for ACAA1. Non-core.
- GO:0050633 (acetyl-CoA C-myristoyltransferase, EC 2.3.1.155): a specific-chain-length instance of the
  thiolase reaction (tetradecanoyl-CoA + acetyl-CoA = 3-oxohexadecanoyl-CoA + CoA). Correct chemistry but
  overly specific; subsumed by GO:0003988. Keep as non-core.
- GO:0016746 / GO:0016747 (generic acyltransferase): correct but far too general (InterPro IEA). Over-broad.
- GO:0120524 (long-chain fatty acyl-CoA OXIDASE activity): WRONG — that is the ACOX1 step
  (acyl-CoA + O2 = enoyl-CoA + H2O2), not thiolysis. IMP annotation from PMID:2882519, which measured
  thiolase DEFICIENCY, not oxidase activity. Over-annotation (experimental -> MARK_AS_OVER_ANNOTATED).
- GO:0008775 (acetate CoA-transferase activity): WRONG — "acyl-CoA + acetate = fatty acid + acetyl-CoA",
  a CoA-transferase, not a thiolase. EXP annotation via Reactome to PMID:11734571. Over-annotation.

## Localization / process assessment

- Core CC = **peroxisome (GO:0005777)** / **peroxisomal matrix (GO:0005782)**. Strong IDA + IBA support.
- Core BP = **fatty acid beta-oxidation (GO:0006635)** and the peroxisomal specialization
  **fatty acid beta-oxidation using acyl-CoA oxidase (GO:0033540)**.
- GO:0000038 (VLCFA metabolic process, IMP PMID:2318981): correct, accept (core-adjacent BP).
- GO:0008206 (bile acid metabolic process, IMP/ISS): the bile-acid branch is now attributed to SCPx;
  the 1987/1990 patient data predate that; keep as non-core.
- GO:0036109 (alpha-linolenic acid metabolic process) and GO:0033540 via Reactome/ALA metabolism: correct
  peroxisomal beta-oxidation context (DHA synthesis). Accept.
- GO:0010124 (phenylacetate catabolic process, IBA): bacterial/plant phenylacetate degradation context;
  not a human ACAA1 function. Over-annotation from phylogenetic propagation.
- Reactome CC calls cytosol / extracellular region / specific granule lumen (neutrophil degranulation
  R-HSA-6798749): ACAA1 has been detected in neutrophil secretory granule proteomes and appears in the
  neutrophil-degranulation Reactome pathway, but as a peroxisomal matrix enzyme these are non-core /
  bystander localizations. Cytosol reflects the pre-import (PTS2 cargo) state. Keep as non-core / over.

## Action summary rationale

- ACCEPT: core thiolase MF (GO:0003988, the best-supported ISS/IBA/TAS), peroxisome/peroxisomal matrix CC,
  fatty acid beta-oxidation BP (IBA/ISS/IMP), GO:0033540, GO:0036109, GO:0000038.
- KEEP_AS_NON_CORE: bile acid metabolic process; acetyl-CoA C-acetyltransferase (ISS/IEA);
  acetyl-CoA C-myristoyltransferase (specific-chain instance); redundant localization IDA calls;
  generic acyltransferase.
- MARK_AS_OVER_ANNOTATED: GO:0120524 (oxidase, IMP), GO:0008775 (CoA-transferase, EXP),
  bare protein binding IPIs (3x), membrane (HDA), cytosol/extracellular/specific granule (Reactome TAS),
  generic acyltransferase IEAs, phenylacetate catabolic process (IBA).
- No REMOVE used (no clearly-wrong IEA that isn't better handled as over-annotation; experimental
  annotations never removed).
</content>
</invoke>
