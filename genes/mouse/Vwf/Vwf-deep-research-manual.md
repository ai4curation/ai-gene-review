# Vwf (mouse, UniProt Q8CIZ8) - manual literature research

No deep-research provider was available for this session; this file records the
literature work done manually from cached publications (`publications/PMID_*.md`),
the UniProt record (`Vwf-uniprot.txt`) and PubMed searches. Quotes are verbatim from
the cited source.

## Identity and domain architecture

- Mouse von Willebrand factor, 2813 aa precursor (Swiss-Prot Q8CIZ8; MGI:98941;
  GeneID 22371). The precursor is cleaved into the propeptide "von Willebrand
  antigen 2" (residues 23-763) and mature VWF (764-2813) [file:mouse/Vwf/Vwf-uniprot.txt].
- Domains: VWFD1-D4, TIL, three VWFA domains (A1 "binding site for platelet
  glycoprotein Ib"; A3 "principal binding site for collagens type I and III"), VWFC
  and a C-terminal cystine knot (CTCK); RGD "Cell attachment site" at 2507-2509
  [file:mouse/Vwf/Vwf-uniprot.txt].
- UniProt function (by similarity to human P04275 and PMID:10930441): "it promotes
  adhesion of platelets to the sites of vascular injury by forming a molecular bridge
  between sub-endothelial collagen matrix and platelet-surface receptor complex
  GPIb-IX-V" and "Also acts as a chaperone for coagulation factor VIII".

## Mouse genetic evidence

- Vwf knockout (Denis et al. 1998) [PMID:9689113 "The mutant mice exhibited defects in
  hemostasis with a highly prolonged bleeding time and spontaneous bleeding events in
  approximately 10% of neonates."]; FVIII reduced [PMID:9689113 "the factor VIII level
  in these mice was reduced strongly as a result of the lack of protection provided by
  vWf"]. Abstract only in cache.
- Arteriolar thrombosis (Ni et al. 2000, full text) [PMID:10930441 "In the vWF –/–
  mice, this early platelet deposition was dramatically reduced (Table 1 )."]
  and [PMID:10930441 "Although the occlusion time in vWF –/– mice was greatly
  prolonged, the thrombi that formed were well anchored to the vessel wall"].
- Venous platelet adhesion to VWF secreted on stimulated endothelium via GPIbalpha
  [PMID:11071623 "This adhesion process was dependent on von Willebrand factor (vWF)
  and independent of P-selectin."].
- Laser injury: VWF is needed for platelet accumulation but not platelet activation
  [PMID:17380206 "vWF plays a role in platelet accumulation during thrombus formation
  but is not required for platelet activation in vivo."].
- VWF-GPIb-V-IX triggers platelet procoagulant activity / fibrin formation at low shear,
  impaired with Vwf-/- mouse plasma [PMID:21037087 "VWF-induced activation of GpIb-V-IX
  triggers platelet procoagulant activity and anchorage of a star-like fibrin
  network"].
- Weibel-Palade body formation requires VWF [PMID:11274431 "We conclude that the
  absence of vWf, as found in severe von Willebrand disease, leads to a defect in
  Weibel--Palade body formation."]; leukocyte rolling is reduced in Vwf-/- mice
  [PMID:11274431 "We report a strong reduction of leukocyte rolling in venules of
  vWf-deficient mice."].
- Atherosclerosis reduced in LDLR-/-Vwf-/- mice [PMID:11520791 "the fatty streaks formed
  in the aortic sinus of LDLR-/-vWf-/- mice of either sex were 40% smaller"].
- Tspan18-knockout mice: histamine-induced VWF release reduced (VWF measured as a
  readout) [PMID:30573509 "Induced plasma vWF release was reduced by approximately 50%
  in the absence of Tspan18 (Figure 8A)."].
- MAGP1 (Mfap2) binds VWF [PMID:18281502 "von Willebrand factor was the only protein of
  the 3 that bound to MAGP1 in surface plasmon resonance studies"].

## Mechanism (from human VWF literature, cached)

- A1-GPIbalpha [PMID:15039442 "a direct interaction between the platelet receptor
  glycoprotein Ibalpha (GpIbalpha) and the A1 domain of the von Willebrand factor
  (VWF)"].
- Integrin alphaIIb-beta3 via RGD [PMID:24928861 "Platelet integrin α IIb β 3 binds an
  RGD motif in the VWC4 module"].
- Collagen binding [PMID:2056120 "Furthermore, we found that purified type VI collagen
  also bound vWF."].
- FVIII carrier [PMID:9759493 "VWF also is a carrier protein for blood clotting factor
  VIII, and this interaction is required for normal factor VIII survival in the
  circulation."].
- Multimerization [PMID:17895385 "Von Willebrand factor (VWF) dimerizes through
  C-terminal CK domains, and VWF dimers assemble into multimers in the Golgi by forming
  intersubunit disulfide bonds between D3 domains."].
- ADAMTS13 substrate [PMID:16221672 "ADAMTS13 controls the multimeric size of
  circulating von Willebrand factor (VWF) by cleaving the Tyr1605-Met1606 bond in
  theA2 domain."].
- BiP ("heavy chain binding protein") association during biosynthesis
  [PMID:3121636 "vWF was transiently associated with BiP and efficiently secreted"].

## Problem references in GOA

- PMID:7854452 (Schmidt et al. 1995) is the Hgf (scatter factor) knockout paper; the
  GOA rows (liver/placenta development) carry the Hgf allele MGI:1857656
  (Hgf<tm1Cbm>, checked on the MGI allele page) in With/From.
- PMID:8562500 is about CD24 (heat-stable antigen) as a P-selectin ligand; the abstract
  does not mention VWF.
- PMID:20097747 (requested for this session) is a rat myocardial infarction study in
  which an anti-vWF antibody is only an endothelial/capillary marker [PMID:20097747
  "Capillary density was assessed by a polyclonal antibody against von Willebrand factor
  (vWF)."]; it gives no information about Vwf function.
