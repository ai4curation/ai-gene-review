# asna-1 (C. elegans, UniProt P30632) - manual literature research

No deep-research provider was available for this review. This file records a manual
literature survey done with PubMed searches (`asna-1 elegans`, 11 hits) and the cached
publications in `publications/`. Full text was read where `full_text_available: true`.

## Identity and family

- ASNA-1 (ZK637.5, synonym tag-205) is the single C. elegans member of the ArsA/GET3
  ATPase family, the ortholog of yeast Get3 and human ASNA1/TRC40/GET3
  [file:worm/asna-1/asna-1-uniprot.txt "Belongs to the arsA ATPase family."].
- Domains: P-loop ATPase (Pfam PF02374 ArsA_ATPase; NCBIfam TIGR00345 GET3_arsA_TRC40;
  HAMAP MF_03112 Asna1_Get3). A zinc site formed by Cys285/Cys288 bridges the homodimer
  (HAMAP-predicted).

## Biochemistry

- Purified MBP-ASNA-1 is an ATPase whose activity is stimulated by As(III) and Sb(III)
  [PMID:17419726 "The ATPase activity of the ASNA-1 protein was dependent on the presence of As(III) or Sb(III)."].
  Abstract-only in cache.
- Kao et al. 2007 describe asna-1 as encoding an ATPase [PMID:17289575 "asna-1 encodes an ATPase that functions nonautonomously to regulate growth."]. Abstract-only in cache.

## Tail-anchored (TA) protein targeting

- Raj et al. 2021 (full text) show ASNA-1 is required for ER targeting of the TA protein
  SEC-61beta in the intestine, identify WRB-1 as its ER receptor, and show WRB-1 and
  SEC-61beta co-immunoprecipitate with ASNA-1::GFP
  [PMID:33883621 "Indeed, using Co-IP/MS/MS analysis SEC-61β was detected as an ASNA-1::GFP-interacting partner"]
  [PMID:33883621 "By means of Co-IP/MS/MS analysis, we detected WRB-1 as an interaction partner of ASNA-1::GFP"]
  [PMID:33883621 "This localization required ASNA-1 since, in the worm asna-1(ok938) protein null mutant8, the ER localization of GFP::SEC-61β was significantly decreased and the protein was instead detected in cytoplasmic foci"].
- ASNA-1 exists in reduced and oxidized states; the reduced form is needed for TA
  targeting and cisplatin resistance, while the oxidized (chaperone/holdase-like) form is
  compatible with insulin secretion
  [PMID:33883621 "We conclude that ASNA-1 exists in two alternative redox states, where formation of the oxidized state requires two conserved cysteines."].
- wrb-1 mutants share the TA targeting and cisplatin-sensitivity defects but not the
  insulin secretion defect, separating these functions
  [PMID:33883621 "These findings strongly support the conclusion that cisplatin sensitivity and TAP targeting defects are unlinked to insulin secretion defects."].
- Point mutants dHis164 and A63V (preferentially oxidized) are cisplatin sensitive and
  TA-targeting defective but insulin-secretion normal (Raj et al. 2022, PMID:36480541).

## Insulin secretion and growth

- asna-1 null mutants arrest reversibly at L1, have reduced DAF-28/insulin secretion;
  expression in sensory neurons and intestine
  [PMID:17289575 "asna-1 mutants are reduced in insulin secretion while overexpression of asna-1 mimics the effects of insulin overexpression."].
- ASNA-1 acts in neurons for DAF-28 secretion; it interacts with the ER chaperone
  ENPL-1/GRP94 (likely in its oxidized chaperone form), localizes to Golgi in neurons, and
  loss of asna-1 perturbs ER/Golgi trafficking pathways
  [PMID:36939052 "The punctate distribution of ASNA-1 in neurons was found to be in the Golgi, as ASNA-1:mNeonGreen colocalized with AMAN-2::wrmScarlet expressed in head neurons from the rawEx90 transgene"]
  [PMID:36939052 "Taken together, these data shows that the main role of ASNA-1 is at the level of ER and Golgi trafficking."].
- How ASNA-1 promotes insulin secretion mechanistically is not known; it does not bind
  proinsulin [PMID:36939052 "ASNA-1 interacts with ENPL-1 independently of its client-binding domain and does not interact with proinsulin"].

## Drug/metal sensitivity

- asna-1 mutants are hypersensitive to arsenite and antimonite (PMID:17419726) and to
  cisplatin (PMID:20966125; human ASNA1 rescues). In eukaryotes ArsA-family proteins have
  been repurposed for TA protein targeting, so these sensitivities are plausibly indirect
  consequences of loss of TA protein biogenesis or of redox-sensor function.

## Peripheral mentions

- PMID:23705068 (Zhu et al. 2013, sphingolipid-TORC1) uses asna-1(ok938) only as a control
  L1-arrest strain: neither mmBCFA nor d17iso-sphingolipid supplementation rescues it
  [PMID:23705068 "Neither C17ISO nor d17iso-SPA permits asna-1(−) animals to bypass L1 arrest."].
  It provides no information on ASNA-1 molecular function.
- PMID:22511947 (Billing et al. 2012) RNAi screen for asna-1-like larval arrest
  modifiers; context only.
- PMID:24058864 asna-1 mutants have elevated UPR activity; context only.
- PMID:14704431 and PMID:19123269: large-scale yeast two-hybrid maps reporting an
  ASNA-1/CEE-1 interaction; no functional follow-up.
