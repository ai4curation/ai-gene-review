# SERP2 / RAMP4-2 (Stress-associated endoplasmic reticulum protein 2) — review notes

UniProt: Q8N6R1 (SERP2_HUMAN), 65 aa; AltName "Ribosome-associated membrane protein RAMP4-2". Single-pass ER membrane protein (TM 38-58). Paralog of SERP1/RAMP4; member of the RAMP4 family.

## Core identity / function
- Small translocon-associated ER membrane protein that stabilizes/protects nascent membrane and secretory proteins during ER stress; SERP1 paralog.
  - UniProt FUNCTION (by similarity to mouse Q9R2C1): "Interacts with target proteins during their translocation into the lumen of the endoplasmic reticulum. Protects unfolded target proteins against degradation during ER stress. May facilitate glycosylation of target proteins after termination of ER stress. May modulate the use of N-glycosylation sites on target proteins." [UniProt Q8N6R1]
  - UniProt SUBUNIT: "Interacts with SEC61B, SEC61A1 and the SEC61 complex. Interacts with CANX." -> translocon-associated.
- No dedicated primary characterization paper in the GOA; function inferred by orthology/paralogy (RAMP4 family) and supported by phylogenetic (IBA) annotations. Less experimentally characterized than SERP1.

## Annotation assessment
- GO:0005783 endoplasmic reticulum (IBA is_active_in; IEA) — CORE site of action/localization, ACCEPT.
- GO:0005789 ER membrane (IEA, ISS) — CORE localization, ACCEPT.
- GO:0016020 membrane (IEA, ISS) — generic parent; KEEP_AS_NON_CORE.
- GO:0030968 ER unfolded protein response (IBA involved_in) — CORE process; stress-associated, acts during ER stress. ACCEPT.
- GO:0005515 protein binding (IPI PMID:25416956; large HuRI set PMID:32296183) — bare protein binding; KEEP_AS_NON_CORE. Partners are largely membrane/secretory proteins consistent with translocon-substrate role.

## Core function summary
SERP2/RAMP4-2 is a Sec61-translocon-associated single-pass ER membrane protein (SERP1/RAMP4 paralog) that binds and stabilizes nascent membrane/secretory proteins during ER stress and facilitates their subsequent N-glycosylation; functions in the ER unfolded protein response. Function is established largely by orthology/paralogy.
