# MVK (mevalonate kinase, Q03426) — review notes

## Core biology
MVK encodes mevalonate kinase (MK; EC 2.7.1.36), a GHMP-kinase-family enzyme
that catalyses the ATP-dependent, Mg2+-requiring phosphorylation of
(R)-mevalonate to (R)-5-phosphomevalonate — the first committed step after
HMG-CoA reductase in the cytosolic mevalonate/isoprenoid pathway (Rhea:RHEA:17065).

- Catalytic activity + function established by recombinant-enzyme kinetics and
  mutagenesis: [PMID:9325256 "cDNA encoding human mevalonate kinase has been
  overexpressed and the recombinant enzyme isolated. This stable enzyme is a
  dimer of 42-kDa subunits"]; catalytic base Asp-204 ["support assignment of a
  crucial catalytic role to Asp-204"]; Glu-193 implicated in liganding the MgATP
  cation.
- Ser-146 catalytic/ATP-orienting role and disease-relevant T243:
  [PMID:11278915 "V(max) for S146A is diminished by 4000-fold"], and the
  disease-associated T243I: [PMID:11278915 "the 65-fold activity decrease
  associated with the inherited human T243I mutation"].
- Substrate specificity for (R)-mevalonate + Mg2+-ATP is stated in UniProt:
  reaction (R)-mevalonate + ATP = (R)-5-phosphomevalonate + ADP + H+ (RHEA:17065),
  cofactor Mg(2+).
- Feedback regulation: farnesyl/geranylgeranyl diphosphate competitively inhibit
  MK at the ATP site — [PMID:9392419 "only MKase was inhibited through
  competitive interaction at the ATP-binding site"], structurally confirmed by
  [PMID:18302342 "Farnesyl thiodiphosphate competes" with substrate ATP]. This
  makes MK a regulatory node: [PMID:9392419 "MKase may occupy a central
  regulatory role in the control of cholesterol and nonsterol isoprene
  biosynthesis"].

## Localisation
Human MK is cytosolic, NOT peroxisomal, despite an earlier peroxisomal proposal:
[PMID:14730012 "We exclusively found a cytosolic localisation of both endogenous
human MK ... No indication of a peroxisomal localisation was obtained"]. The GOA
NOT|located_in peroxisome (IDA, PMID:14730012) encodes this. The ISS peroxisome
annotations (GO_REF:0000024, from rat P17256) are contradicted by the direct
human data and by [PMID:14680974], which found the pathway enzymes function
independently of peroxisomes. UniProt still lists a peroxisome location by
similarity to P17256, but the experimental human evidence is cytosolic.

## Disease
Loss-of-function MVK variants cause mevalonate kinase deficiency (MKD), a
spectrum from milder hyperimmunoglobulinaemia D and periodic fever syndrome
(HIDS; MIM 260920) to severe mevalonic aciduria (MEVA; MIM 610377) with
psychomotor retardation, dysmorphism, and recurrent febrile crises:
- MEVA first molecular characterization: [PMID:1377680].
- HIDS caused by MVK mutations that reduce MK activity/stability:
  [PMID:10369261 "revealed reduced activities of mevalonate kinase"].
- MVK variants also cause porokeratosis (POROK3; MIM 175900) per UniProt.

The GO:0050728 "negative regulation of inflammatory response" IMP
(PMID:16732551) is an indirect disease-physiology inference: reduced MK/isoprenoid
output drives the autoinflammatory HIDS phenotype. The cited paper is an AA
amyloidosis case report of HIDS patients and does not itself demonstrate an
inflammatory-regulation molecular activity of MVK; treat as over-annotation
(disease consequence, not a direct core molecular/biological role).

## Interactions
Homodimer (UniProt SUBUNIT "Homodimer"; PMID:9325256 dimer of 42-kDa subunits) —
supports GO:0042802 identical protein binding (self-interaction Q03426–Q03426 in
IntAct high-throughput screens PMID:16189514, 25502805, 26871637, 31515488,
32296183). Heterotypic "protein binding" IPIs are from proteome-scale interactome
screens (POT1/Q9NUX5 in PMID:21044950; RNF141/Q8WVD5 in PMID:32296183); bare
GO:0005515 is uninformative — mark as over-annotated per policy.
