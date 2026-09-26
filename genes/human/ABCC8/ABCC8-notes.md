# Human ABCC8 / SUR1 review notes

## Identity, scope and research provenance (2026-09-26 UTC)

Human ABCC8 is UniProt Q09428, sulfonylurea receptor 1 (SUR1), distinct from ABCC9/SUR2. Reviewed all 64 seeded annotations without editing any original term, evidence, qualifier, supporting entity or isoform field. The seeded GO:0015272 NAS row explicitly carries `contributes_to`; its weaker complex-level assertion is retained. No NEW annotation or redundant process is proposed. The seven unresolved rows reflect source-specific access or tracing limits, not a claim that the original curators were mistaken.

Used the review, annotation-reviewer and core-function-synthesizer skills. `just fetch-gene human ABCC8` seeded the review; the Falcon job ran concurrently with `just fetch-gene-pmids human ABCC8`. The genuine Falcon report completed successfully in 592.18 seconds (2026-09-25 19:36:49–19:46:41 local report timestamps) under a 1200-second wrapper limit. No provider file was fabricated or altered, and no quota-exhausted Perplexity retry was attempted. Additional primary publications and Reactome entries were fetched through the repository caching tools. The provider report is a discovery/synthesis aid; primary evidence determines the actions.

## Core function and mechanism

Four SUR1 regulatory subunits associate with four Kir6.2 pore subunits. Human structures resolve ATP and ADP bound to SUR1 and a distinct ion-conduction pathway in Kir6.2 [PMID:29286281, *Molecular structure of human KATP in complex with ATP and ADP.*, “These structures support the role of SUR1 as an ADP sensor”]. Functional human SUR1 mutation assays separate surface trafficking from MgADP/diazoxide activation [PMID:24814349]. The full text uses surface-expression assays, rubidium efflux and patch clamp; most assayed mutations reach the surface yet fail normal activation. The R1419H report independently describes absent functional channels [PMID:25720052, abstract]. Human open-channel structures further support the regulator/pore distinction [PMID:34815345, abstract; PMC full-text retrieval failed].

SUR1 has ATPase activity: PMID:26181369 uses human SUR1 and SUR2A constructs, point substitutions, patch clamp and direct MgATPase assays, including isolated recombinant NBD2 constructs. A SUR1-focused title does not exclude the actual SUR2A comparator experiments in the full text. PMID:29286281 also reports purified human channel ATPase measurements. These experiments do not demonstrate stoichiometric ATP-driven K+ pumping. Conversely, absence of solute pumping does not imply a catalytically dead ATPase. PMID:30587573 shows ATP binding can activate channels without hydrolysis when inhibitory Kir6.2 nucleotide effects are minimized and SUR1 ATP affinity is increased. Its result is explicitly conditional; it does not prove that native SUR1 hydrolysis is irrelevant in every setting.

The core model therefore uses GO:0015459 potassium channel regulator activity, `contributes_to_molecular_function` GO:0015272, membership in GO:0008282 and plasma-membrane location, directly participating in potassium transport and regulation of insulin secretion. SUR1 directly performs regulatory work in the transport machinery. Insulin synthesis, granule proteolysis and a standalone K+ pump are not assigned.

## Live ontology checks and key term-scope corrections

Definitions were read from the [QuickGO term service](https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0015459,GO:0015272,GO:0008282,GO:1905605) on 2026-09-26. Additional individual lookups covered GO:0019829, GO:0031004, GO:0140359, GO:0099106 and GO:1990573.

| Existing assertion | Assessment |
| --- | --- |
| GO:0005267 potassium channel activity | Human mutant assays support SUR1 regulatory activity; MODIFY to GO:0015459. |
| GO:0015272 ATP-activated inward rectifier potassium channel activity | The actual definition refers to ATP-sensitive inward rectification and ATP pore block. Its label is not a reason to reject SUR1 contribution. ACCEPT the explicitly qualified NAS row; refine the separate mutant-pathway MF to SUR1-specific regulation. The resulting repeated-term warning is intentional and reflects the weaker `contributes_to` claim. |
| GO:0019829 ATPase-coupled cation transmembrane transporter activity | The definition is an ATP-coupled cation pump reaction. The primary biochemical experiment supports ATPase activity (GO:0016887), while hamster genetic channel assays support regulation (GO:0015459). |
| GO:0031004 potassium ion-transporting ATPase complex | Definition describes a K+-importing ATPase complex, including bacterial Kdp, not the Kir6/SUR channel. MODIFY to GO:0008282, whose definition explicitly includes Kir6.x and SURx subunits. |
| GO:0140359 ABC-type transporter activity | Definition requires primary-active solute translocation. SUR1's demonstrated role is regulation of the separate Kir pore. MODIFY to GO:0015459; do not infer catalytic-residue loss. |
| GO:0055085 transmembrane transport | Participation remains supported but can be refined to potassium ion transmembrane transport. |
| GO:1990573 potassium import across plasma membrane | The source complex is rat Kir6.2–SUR2B; refine to direction-independent potassium transport for human SUR1. Inward rectification does not establish physiological net influx. |

## Propagation audit

Read current QuickGO donor records for rat Q09429, mouse B2RUS7 and hamster A0A1S4NYG1/A0A1U7R319, and verified their UniProt identities. Every inferred row has named `source_entities` with a status and source-specific explanation. The Ensembl IDs identify the same rodent donor chains, not additional experiments. No other species' existing review for these donors was edited.

For PAINT, the source is the ancestral node: PTN002795584 (plasma membrane) is retained; PTN000657997 (transmembrane transport) is refined in scope without rejecting inherited participation; PTN009085477 (ABC active transport) is challenged specifically because of target-lineage regulatory specialization documented in human structures and physiology. Neither donor count nor the presence of ABCC8 among its own experimental descendants is used as an objection.

The current mouse B2RUS7 record had no experimental annotations; its negative-insulin-secretion row is inferred from rat. The positive glucose-stimulated insulin-secretion and ADP-binding donor rows were not recovered. ADP binding is independently proven on human SUR1 and retained, with the stale source chain recorded. The specific positive secretion claim remains UNDECIDED rather than being inverted solely from a simplified beta-cell model.

The live [ComplexPortal CPX-185 entry](https://www.ebi.ac.uk/intact/complex-ws/complex/CPX-185) identifies “Inward rectifying potassium channel complex, Kir6.2-SUR2B”, systematic name `4xAbcc9:4xKcnj11`, in rat. A homologous-complex transfer can support shared channel biology, but this does not establish a human SUR1 direction-specific influx role. The normal beta-cell pathway described in Reactome:R-HSA-1296024 involves K+ efflux. No claim that the source study misidentified its protein is made.

## Rodent source evidence and limits

| Source | Finding and curation consequence |
| --- | --- |
| PMID:23828271 | Glibenclamide analogues in streptozotocin-treated rats alter systemic glucose/lipids; accessible abstract does not resolve intracellular glucose homeostasis or LDL-clearance mechanism. Both precise transfers UNDECIDED. |
| PMID:21527399; PMID:25891870 | Pregnancy-dependent SUR1 expression and pharmacological uterine relaxation. Contextual non-core roles; drug subtype specificity and gestational stage limit generalization. |
| PMID:24114458 | Rat SAH experiments include SUR1 antisense and glibenclamide, reduced IgG extravasation/TNF and better spatial learning; human autopsy tissue provides injury-associated SUR1/TRPM4 proximity. Memory/learning effects remain non-core. |
| PMID:15613469 | Rat SUR1 pH-dependent extracellular-zinc modulation, with SUR2A comparison and mutational analysis. Retained as contextual modulation; no unperformed human residue alignment is asserted. |
| PMID:17174476 | Risperidone changes SUR1 mRNA in rat PC12 cells, without the described rat-brain response. A xenobiotic expression response, not xenobiotic export. |
| PMID:23149556 | Glibenclamide after rat stroke increases doublecortin-positive cell migration, later neuronal production and angiogenesis. These existing injury/repair associations are non-core. The exact glial-proliferation assay is not resolved from the abstract, so that transfer remains UNDECIDED. |
| PMID:14645230 | Syntaxin-1A/SUR1 interaction and KATP inhibition in islet/insulinoma-related experiments do not resolve the precise synaptic-vesicle and presynaptic localization assertions from the accessible abstract. Both UNDECIDED. |
| PMID:17285300 | Full text reports renal Abcc8 transcriptional downregulation in endotoxemia. Response to LPS is non-core and does not imply LPS transport. |
| PMID:18854840 | Full text shows that SUR1 inhibition reduces IgG leakage and restores junctional ZO-1 after rat SAH. The transferred negative BBB-permeability sign is reversed relative to this intervention. MODIFY to positive regulation (GO:1905605), corroborated by antisense in PMID:24114458. |
| PMID:18084728 | Hypothalamic SUR1 expression under insulin-induced hypoglycemia is a contextual insulin response, distinct from pancreatic control of secretion. |
| PMID:15647111 | Full text includes antibody controls and rodent cardiac immunolocalization of SUR1 at sarcolemma. Retained as tissue-specific, without claiming universal dominance over SUR2A in ventricle. |
| PMID:15962003 | Kir6.2 mutant assays show SUR1 MgATP-dependent activation and effects of SUR1 nucleotide-domain mutations; direct channel regulation supports positive regulation of K+ transport. |
| PMID:15163199 | KATP openers inhibit insulin secretion, with additional mitochondrial effects described. Human SUR1 disease and channel data independently support its core restraint of secretion. |
| PMID:23633925 | Rat blood-tumor barrier/glyburide study supports a contextual junctional-disruption role, corroborated by the accessible SAH full text. |
| PMID:28842488 | Hamster donor annotations derive from genetic SUR/Kir channel experiments. Abstract describes flux and patch clamp, not a demonstrated ATP-coupled cation-pump reaction. Missing full text is not treated as wrong-gene evidence. |

## Source-specific unresolved experiments and research-report limits

PMID:20610380 is abstract-only despite attempted PMC and publisher retrieval. Its abstract foregrounds ankyrin-B/Kir6.2 in cardiac cells. Do not infer absence of SUR1 experiments from that framing. KATP-complex membership is independently established by the human structure and accepted; the source-specific transmembrane-transporter-binding IPI assignment remains UNDECIDED pending its full experiment.

Full-text retrieval attempts used cached PMC metadata, PMC/Europe PMC and publisher routes. Several articles returned restricted XML, challenge pages, empty redirect content or HTTP 403; those responses were not treated as paper evidence. The relevant seven uncertain annotations are intracellular glucose homeostasis, LDL clearance, synaptic-vesicle membrane, presynaptic membrane, positive glucose-stimulated secretion, the source-specific IPI binding assignment, and negative glial proliferation. Known ATPase/channel biology permits scope corrections on independently established mechanisms even when a particular donor article is abstract-only.

The report's SUR1–TRPM4 discussion is contextual. PMID:23255597 reports heterologous and rat injury-associated FRET/co-immunoprecipitation and channel effects; PMID:22291026 reports no corresponding coupling in a different heterologous system. PMID:24114458 adds human injury-tissue association but does not provide a native human complex structure. No new universal TRPM4 complex or nonselective-channel core function is manufactured from these mixed contexts. The question remains explicit in suggested follow-up work.

Read all seven cached Reactome entries. Their normal, loss-of-function, activating-variant and drug-binding contexts are distinguished. In particular R-HSA-265682 describes inhibitory ATP occupancy on Kir6.2; direct human structures, rather than that event alone, establish SUR1 ATP binding.

## Review completion and checks

Final initial counts: 25 ACCEPT, 17 MODIFY, 15 KEEP_AS_NON_CORE, seven UNDECIDED. All 64 seeded rows and their original fields are preserved, including three alternative products and the contributes_to qualifier. No GO-CAM index entry was found for ABCC8/Q09428. No NEW biological-process term was necessary, so no comparator-based gap claim is made. Core synthesis keeps channel regulation, complex contribution and insulin control together and excludes downstream injury phenotypes.

Targeted gene validation, append-only history validation, rendering and a rendered-content check are performed before PR publication. The GO:0015272 mixed-action warning is deliberate: the qualified complex-level activity and SUR1-specific replacement assess different assertion strengths. Repository-wide baseline validation is coordinated by the parent agent rather than duplicated here.
