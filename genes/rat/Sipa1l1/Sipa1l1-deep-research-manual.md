# Sipa1l1 (rat, O35412) - manual literature synthesis

No deep-research API provider was available in this environment, so this synthesis was
assembled by hand from the cached publications (`publications/PMID_*.md`), the UniProt
record (`Sipa1l1-uniprot.txt`) and PubMed searches. Every claim carries its source.

## Identity and domain architecture

- Rat Sipa1l1 (SPAR, spine-associated Rap GTPase-activating protein; also SPA-1-like p1294 /
  SPAL) is a 1822-aa protein with a Rap-GAP domain (638-855), a PDZ domain (992-1068) and a
  C-terminal coiled coil (1753-1813) [UniProt O35412, FT DOMAIN/COILED].
- It belongs to the Rap/Ran GAP family (PANTHER PTHR15711) together with SIPA1, SIPA1L2,
  SIPA1L3 and RAP1GAP/RAP1GAP2.

## Molecular function: Rap GTPase-activating protein

- Roy et al. 2002 described SPAL as "a GTPase-activating protein (GAP) that is specific for
  Rap1" that binds the GK domain of PSD-95 family proteins and resides in the NMDA-R-PSD-95
  complex [PMID:12059963, abstract].
- Pak et al. 2001: "SPAR, a Rap-specific GTPase-activating protein (RapGAP), interacts with
  the guanylate kinase-like domain of PSD-95 and forms a complex with PSD-95 and NMDA
  receptors in brain" [PMID:11502259, abstract]. UniProt curates "Stimulates the GTPase
  activity of RAP2A" from this paper [UniProt CC FUNCTION, ECO:0000269 PubMed:11502259].
- Richter et al. 2007: "Overexpression of SPAR containing a functional GAP domain caused
  substantial inactivation of cotransfected Rap1 and Rap2" [PMID:18094260].
- GO:0046582 "Rap GTPase activator activity" is obsolete (OLS check, 2026-10), so the most
  specific current MF is GO:0005096 GTPase activator activity.

## Actin association

- "In heterologous cells, SPAR reorganizes the actin cytoskeleton and recruits PSD-95 to
  F-actin" and "The effects of SPAR on spine morphology depend on the RapGAP and
  actin-interacting domains" [PMID:11502259].
- "The Act2 domain has been shown to be sufficient for association with F-actin filaments in
  hippocampal neurons as well as heterologous cells" [PMID:19900557].

## EphA4 coupling

- "We have identified a novel interaction between the C terminus of the EphA4 receptor and
  the PDZ domain of ... SPAR. In neuronal cells, this binding mediates EphA4-dependent
  inactivation of the closely related GTPases Rap1 and Rap2" [PMID:18094260].
- "This result suggests that SPAR GAP activity is required for ephrin-A-dependent growth cone
  collapse." [PMID:18094260]. This is the mouse/rat-neuron evidence behind the ISO/ISS rows for
  ephrin receptor binding, ephrin receptor signaling pathway and regulation of axonogenesis.

## Dendritic spines and synaptic plasticity

- Overexpressed SPAR "causes enlargement of spine heads"; dominant negative SPAR constructs
  "cause narrowing and elongation of spines" [PMID:11502259].
- PSD-Zip70 (Lzts1) binds the GK-binding domain of SPAR; overexpression of that SPAR domain
  induced immature spines [PMID:15703396]. ProSAPiP1 (Lzts3) and PSD-Zip70 "bind and recruit
  SPAR to synapses" [PMID:16522626].
- PDLIM5 (and Enigma/PDLIM7) bind the SPAR Act2 region; PDLIM5 overexpression "caused dramatic
  loss of SPAR" [PMID:19900557].
- RNAi in rat hippocampal neurons: "silencing of SPAR reduced head width and spine density"
  [PMID:21382555].

## Regulated degradation (homeostatic plasticity)

- CDK5 primes SPAR (Ser-1367) for Plk2 polo-box docking; Plk2 phosphorylation leads to
  degradation; "RNAi knockdown of SPAR weakened synapses, and overexpression of a SPAR mutant
  resistant to Plk2-dependent degradation prevented synaptic scaling" [PMID:18498738].
- The E3 is SCF(beta-TRCP): "In the presence of Plk2, SPAR physically associated with the
  SCF(beta-TRCP) complex through a canonical phosphodegron" [PMID:18723513]; "GST-beta-TRCP1
  (and GST-beta-TRCP2) associated with SPAR, Plk2, and the N terminus of Cullin 1"
  [PMID:18723513]. These binding events make SPAR a substrate of the kinase and the ligase;
  they are not part of SPAR's own activity.
- Plk2 coordinately degrades SPAR (a Rap inhibitor) and activates PDZGEF1 to raise Rap
  activity: "degradation of SPAR (Rap inhibitor) and activation of PDZGEF1 (Rap activator)
  work additively to stimulate Rap" [PMID:21382555]. SPAR knockdown reduced surface
  GluA1/GluA2 in proximal dendrites [PMID:21382555].

## Contrary evidence from knockout mice

- Matsuura et al. 2022 (mouse): super-resolution microscopy found SIPA1L1 "mainly localized to
  general submembranous regions in neurons, but surprisingly, not to PSD"; interactor
  screening identified spinophilin and neurabin-1 "but rejected PSD-95/NMDA-R-complex
  components"; "Sipa1l1-/- mice showed normal spine size distribution and NMDA-R-dependent
  synaptic plasticity" but altered alpha2-adrenergic / adenosine A1 receptor responses and
  behavioural anomalies [PMID:35121636, abstract only]. This challenges the PSD localization
  and the necessity of SPAR for spine morphology in vivo, while leaving the overexpression and
  acute-knockdown data standing.

## Other

- PMID:15823548 (rat kidney papilla AQP2 immunoaffinity complex) names "SPA-1" in the
  abstract; whether Sipa1l1 itself was identified cannot be confirmed from the abstract.
- Human SIPA1L1 plasma membrane and actin cytoskeleton rows are HPA immunofluorescence
  (GO_REF:0000052; QuickGO query for O43166), the source of the rat ISO rows.
