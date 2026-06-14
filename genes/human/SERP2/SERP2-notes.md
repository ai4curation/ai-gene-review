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

## Falcon deep-research findings (incorporated 2026-06)
- SERP2 = RAMP4-2: UniProt AltName for Q8N6R1 is "Ribosome-associated membrane protein RAMP4-2", so RAMP4-2 experimental data map to SERP2. (Falcon flagged that primary texts did not always print the Q8N6R1/C13orf21 accession, but the UniProt name equivalence is unambiguous.)
- NEW direct experimental finding: RAMP4-2 (SERP2) is a tail-anchored ER protein and a substrate for intramembrane proteolysis. Among tail-anchored candidates tested, RAMP4-2 was the only one efficiently cleaved by SPPL2c, and it was also cleaved by SPP [PMID:30733280; Niemeyer et al. EMBO Rep 2019, DOI 10.15252/embr.201846449; Falcon report pages 3-6]. This implicates SERP2 in regulated ER-membrane proteostasis/turnover and is a substrate property not previously captured. Added as reference (MEDIUM relevance); no new GO annotation asserted (no cached verbatim text).
- HA-RAMP4-2 (SERP2) cleavage is used as the readout substrate for SPPL2c activity/regulation in a 2023 study, corroborating the SPPL2c-substrate relationship [PMID:37261541; Contreras et al. Cell Mol Life Sci 2023, DOI 10.1007/s00018-023-04823-7]. Added as reference (LOW; tool-substrate use).
- Family-level structural context: RAMP4-family proteins localize at the Sec61 lateral gate and may act as a dynamic, gating-modulating translocon component [PMID:38787756; Vismpas & Forster eLife 2024 Insight, DOI 10.7554/eLife.98548]. The underlying structural data are for RAMP4/SERP1, so this is inference for the paralog SERP2, not SERP2-specific evidence. Added as reference (MEDIUM, family context).
- Gemmer & Forster 2020 translocon review supplies background RAMP4-family/Sec61 association [PMID:32019826]. Added as reference (LOW).
- Possible disease link (NOT added to YAML; gene-level only): an intergenic SNP (rs9525931) near SERP2 showed a female-specific association with asthma in a 2023 CLSA GWAS [Odimba et al., J Asthma Allergy 2023, DOI 10.2147/JAA.S404670]. This is an intergenic-locus association, does not establish SERP2 molecular function, and was left notes-only.
- No existing actions/annotations were changed; additions are reference-level only. None of these papers are cached in publications/, so no paraphrased verbatim supporting_text and no supported_by changes were made.
