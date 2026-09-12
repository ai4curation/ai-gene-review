# CHMP7 notes

## Review focus

CHMP7 is an ESCRT-III-like / ESCRT-II-III hybrid protein with two literature-supported contexts: an older endosomal sorting role through CHMP4B association, and a stronger, CHMP7-specific nuclear-envelope role in recruiting ESCRT-III to reforming nuclear-envelope holes during anaphase. For this review, the core function should emphasize LEMD2/LEM2-dependent recruitment of CHMP7 and downstream ESCRT-III factors to the nuclear envelope for nuclear membrane closure, with endosomal sorting kept as supported but secondary PN context.

## Direct evidence

- Horii et al. described CHMP7 as an ESCRT-III-related protein with SNF7-related domains and reported a positive CHMP4B interaction, no EAP20 interaction, cytoplasmic/perinuclear distribution, ubiquitinated-protein accumulation in GFP-CHMP7-expressing cells, and a dominant-negative effect on virus-like particle release [PMID:16856878 "CHMP7, a novel ESCRT-III-related protein, associates with CHMP4b and functions in the endosomal sorting pathway"] [PMID:16856878 "positive interaction between the C-terminal half of CHMP7 and CHMP4b"] [PMID:16856878 "interaction was not observed between CHMP7 and EAP20"].
- Vietri et al. showed that ESCRT-III is transiently recruited to the reassembling nuclear envelope during late anaphase and that CHMP7 specifically recruits ESCRT-III/VPS4 to sites where the reforming nuclear envelope engulfs spindle microtubules [PMID:26040712 "ESCRT-III-like protein CHMP7 to sites where the reforming nuclear envelope engulfs spindle microtubules"].
- The same paper supports a core nuclear-envelope sealing role: "ESCRT-III, VPS4 and spastin cooperate to coordinate nuclear envelope sealing and spindle disassembly" at NE-microtubule intersection sites [PMID:26040712 "coordinate nuclear envelope sealing and spindle disassembly at nuclear envelope-microtubule intersection sites"].
- Gu et al. identified LEM2/LEMD2 as the upstream nuclear adaptor. They found that "CHMP7 and LEM2 enrich at the same region of the chromatin disk periphery" during nuclear envelope reformation, that CHMP7 binds the LEM2 C-terminal domain, and that recruitment of CHMP7/CHMP2A/IST1 depends on LEM2 [PMID:28242692 "CHMP7 and LEM2 enrich at the same region of the chromatin disk periphery"] [PMID:28242692 "CHMP7 can bind directly to the C-terminal domain of LEM2 in vitro"] [PMID:28242692 "recruits Cmp7p/CHMP7 and downstream ESCRT factors to the nuclear envelope"].
- UniProt summarizes the same model: CHMP7 is "required to recruit the ESCRT-III complex to the nuclear envelope (NE) during late anaphase" and is "Recruited to the reforming NE during anaphase by LEMD2" [UniProt:Q8WUX9 "required to recruit the ESCRT-III complex to the nuclear envelope (NE) during late anaphase"] [UniProt:Q8WUX9 "Recruited to the reforming NE during anaphase by LEMD2"].

## Annotation decisions

- Accept as core: nuclear envelope, nuclear membrane reassembly, ESCRT III complex, membrane fission, and protein localization to chromatin / chromatin disk periphery where this represents LEMD2-dependent recruitment of CHMP7 and downstream ESCRT factors to the reforming nuclear envelope.
- Accept or keep only with careful wording: ESCRT complex membership and nuclear-envelope localization are direct, but CHMP7 is better described as an upstream ESCRT-III-like recruitment/adaptor factor than as a generic CHMP4-like filament subunit.
- Modify broad or misleading nuclear/cell-cycle terms: exit from mitosis, nuclear pore, chromatin location, and spindle-assembly wording should be interpreted through the specific CHMP7 role in nuclear membrane reassembly and nuclear-envelope sealing rather than as broad mitotic progression, stable nuclear-pore membership, or spindle assembly.
- Keep endosomal sorting/MVB annotations as non-core or modify broad vacuolar wording to MVB/late-endosome-to-lysosome wording. PMID:16856878 supports an endosomal-sorting phenotype, but the stronger CHMP7-specific mechanism is nuclear-envelope ESCRT recruitment.
- Treat viral budding annotations as over-annotated for CHMP7. The direct evidence is dominant-negative overexpression affecting virus-like particle release, not a demonstrated endogenous core viral-budding function.
- Keep autophagy/amphisome/lysosomal membrane, plasma membrane repair, cytoplasm/cytosol/nucleoplasm, kinetochore/midbody, and broad ESCRT cell-cycle annotations as non-core pathway contexts unless the annotation can be tied directly to nuclear-envelope sealing or CHMP7-dependent ESCRT recruitment.
- Mark generic GO:0005515 protein binding as over-annotated. The meaningful molecular interactions are CHMP7-LEMD2 and CHMP7-CHMP4B, not undifferentiated protein binding.

## Description cleanup note

The YAML `description` field was revised to keep it as a standalone biological summary. Project-specific curation framing moved here instead.

- Moved out of the YAML description: the prior wording described the CHMP4B-associated endosomal sorting evidence as secondary specifically in the Proteostasis Network context.
