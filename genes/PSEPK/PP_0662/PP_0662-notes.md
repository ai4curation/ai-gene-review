# PP_0662 curation notes

Q88Q36 has a submitted "threonine synthase" name, PLP cofactor prediction, and
Thr-synth-like domain/family assignments. Unlike Q88MU7, it has no curated EC,
Rhea reaction, UniPathway mapping, or GOA. It also lacks NCBIfam TIGR00260 and
InterPro IPR004450/IPR000634, which are present on canonical ThrC/Q88MU7. No MF
or BP is asserted solely from the submitted name and broad family evidence, and
the protein does not satisfy the terminal module step without biochemical or
genetic support.


## 2026-11-01 holistic bacterial threonine audit

Every existing row, core function and source claim was reviewed. Original machine payloads, raw GOA/UniProt bytes and existing provider reports are preserved. No IBA rows occur in this eight-gene panel, so no PAINT lineage verdict was required. The normal mod-description-deep-research command skipped these PSEPK genes because no MOD provider is configured. The existing genuine provider report was read and preserved unchanged; its claims were checked against primary papers and curated features.

No GOA rows exist for this target; none are manufactured to complete the route. The protein is nevertheless a plausible threonine-synthase-like paralog: it shares IPR051166 Threonine_Synthase, the N-terminal domain and PLP-enzyme fold. The sequence retains Lys112 in the homologous HGPT-containing region (GHNEWILQLFHGPTRSSKDFAAQLQARFVRH around residues 95–125). Canonical ThrC contains NSNEWVLELFHGPTLAFKDFALQLLGRLLDH. Missing TIGR00260, IPR004450 or PS00165 calls cannot establish functional loss; the prior categorical wording was corrected.

No target-specific substrate assay, complementation or locus-resolved auxotrophy evidence was recovered. PMID:20158506 abstract does not map its threonine auxotroph to PP_0662. The native 2025 ThrC clone instead maps to Q88MU7 by both terminal primers. Thus core_functions remains empty and the inherited report's unambiguous ortholog/physiological assignment is not adopted, while the plausible chemistry remains explicit. This is uncertainty, not a negative activity claim.

The full review PMID:19946135 was read for pathway chemistry and regulatory diversity; it cannot substitute for native primary assays. PMID:40236303 and the original supplementary DOCX provide native engineering context for the identified constructs, not an independently purified enzyme series. The review's broad evolutionary claims were not used to assert identical kinetics or universal essentiality. Focused schema/term/reference validation, helper-generated record sections, history validation and rendering are recorded in .cache/module-audit-logs/threonine-psepk-review/.
