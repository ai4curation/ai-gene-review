# NAGS (N-acetylglutamate synthase, mitochondrial) — review notes

UniProt: Q8N159 (NAGS_HUMAN). Human, 534 aa precursor with N-terminal mitochondrial
transit peptide. EC 2.3.1.1.

## Core biology (verified)

- NAGS catalyzes: L-glutamate + acetyl-CoA = N-acetyl-L-glutamate (NAG) + CoA + H+
  (RHEA:24292, EC 2.3.1.1). This is the exact GO term GO:0004042
  "L-glutamate N-acetyltransferase activity, acting on acetyl-CoA as donor"
  (synonym: "N-acetylglutamate synthase activity").
  [PMID:12459178 "N-acetylglutamate synthase (NAGS, E.C. 2.3.1.1) is a mitochondrial enzyme catalyzing the formation of N-acetylglutamate (NAG), an essential allosteric activator of carbamylphosphate synthase I (CPSI), the first enzyme of the urea cycle."]
- NAG is the OBLIGATE allosteric activator of CPS1 (the first, rate-limiting enzyme of
  the urea cycle). Without NAG, CPS1 is inactive → hyperammonemia.
  [PMID:12459178 "Patients with NAGS deficiency develop hyperammonemia because CPSI is inactive without NAG."]
  [PMID:23894642 "an obligate cofactor for carbamyl phosphate synthetase I (CPSI) in the urea cycle"]
- Thus NAGS is the REGULATORY GATE of the urea cycle: not stoichiometrically part of the
  cycle, but the cycle cannot run without its product. In mammals NAG's role is entirely
  urea-cycle-related, NOT ongoing arginine biosynthesis (unlike bacteria/plants where NAG
  is the committed step of de novo arginine biosynthesis).
  [PMID:23894642 "In microorganisms and plants, NAG is further converted to NAG phosphate by NAG kinase (NAGK, EC 2.7.2.8) to continue the L-arginine biosynthetic pathway ... However, in mammals, NAG has an entirely different role as the essential cofactor for carbamyl phosphate synthetase I (CPSI) in the urea cycle"]
- Localization: mitochondrial matrix (of hepatocytes and enterocytes). Enzyme purified
  from human liver mitochondria.
  [PMID:7126172 "Acetyl-CoA:L-glutamate N-acetyltransferase (amino acid acetyltransferase, EC 2.3.1.1) was isolated from human liver mitochondria"]
- Regulation: activity INCREASED by L-arginine in mammals (opposite of bacterial NAGS,
  which is arginine-inhibited). L-arginine binds the AAK (amino-acid kinase) domain.
  [PMID:23894642 "in mammals, L-arginine enhances the NAGS activity"]
- Architecture: two domains — N-terminal AAK (amino-acid kinase-like, arginine binding /
  regulatory) and C-terminal NAT (GCN5-related N-acetyltransferase, catalytic). The NAT
  domain alone retains catalytic activity.
  [PMID:23894642 "the hNAT domain retains catalytic activity in the absence of the amino acid kinase (AAK) domain. Instead, the major functions of the AAK domain appear to be providing a binding site for the allosteric activator, L-arginine, and an N-terminal proline-rich motif that is likely to function in signal transduction to CPS1."]
- Quaternary structure: homodimer / homotetramer. [PMID:23894642 "native NAGS from human and mouse exists in tetrameric form"]
- Tissue: highly expressed in adult liver, kidney, small intestine. [UniProt TISSUE SPECIFICITY]

## Disease

NAGS deficiency (NAGSD; MIM:237310; MONDO:0009377) — autosomal recessive urea cycle
disorder, hyperammonemia without orotic aciduria; clinically indistinguishable from CPS1
deficiency. Uniquely treatable with carglumic acid (N-carbamyl-L-glutamate), a stable NAG
analogue that directly activates CPS1. [dismech N-Acetylglutamate_Synthase_Deficiency.yaml]

## Annotation-specific notes

- GO:0016747 (acyltransferase activity, transferring groups other than amino-acyl groups):
  IEA from InterPro GNAT domain (IPR000182). This is a broad parent of GO:0004042. Since the
  specific activity GO:0004042 is experimentally established and also present, GO:0016747 is
  an over-annotation (too general) → MODIFY to GO:0004042.
- GO:0006536 (glutamate metabolic process): IBA, true (NAG synthesis consumes glutamate) but
  broad; keep as non-core.
- GO:0006526 (L-arginine biosynthetic process): IBA + IEA. NAGS catalyzes step 1 of the
  L-arginine/ornithine biosynthetic pathway from glutamate (UniProt PATHWAY: UPA00068 UER00106,
  "N(2)-acetyl-L-ornithine from L-glutamate: step 1/4"). This is the canonical phylogenetic
  function of the family; accept, though in mammals the NAG product is primarily used to
  activate CPS1 rather than for net arginine synthesis. Accept (family-conserved committed step).
- GO:0090461 (intracellular glutamate homeostasis) IDA + GO:0000050 (urea cycle) IDA from
  PMID:21757002 (FXR paper). Cached publication is abstract-only (full_text_available: false);
  the BHF-UCL curator read the full text. Do not remove experimental annotations. urea cycle is
  a genuine core role; intracellular glutamate homeostasis is more peripheral → keep as non-core.
- GO:0005739 mitochondrion (HTP PMID:34800366; IDA PMID:7126172): broader than matrix but
  correct; accept.

## Deep research

Falcon deep-research file (NAGS-deep-research-falcon.md) did not land during the polling
window (~12+ min). Review grounded in UniProt Q8N159, seeded GOA, cached publications
(PMID:12459178, 7126172, 23894642, 21757002, 34800366), and dismech disorder entry.
