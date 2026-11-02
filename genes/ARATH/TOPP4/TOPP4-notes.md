# TOPP4 curation notes


## 2026-10-26 complete annotation audit

All 27 original rows reviewed, no NEW annotations. Direct target biochemical results support the PP1 MF and protein-dephosphorylation process. The PIF5 phosphorylation row is corrected to the measured removal reaction. The two PIF binding sources are kept distinct (AT1G09530/PIF3 versus AT3G59060/PIF5); direct PIF5 catalysis is not silently assigned to PIF3. RGA/GAI, PIF5, PIN1 and ATG13a substrate contexts were checked separately, including the opposite effects on DELLA versus PIF5 stability. Nuclear and cytoplasmic annotations are retained on direct target localization, with plasma-membrane observations described without manufacturing a new row. Full PMID:38851185 explicitly leaves the termination-module substrate unknown, so no RNA-polymerase-II-CTD phosphatase assertion is made. Protein-binding refinements use actual substrate reaction evidence where available; PP1R3 generic binding is removed as uninformative without rejecting the interaction.

All seeded rows were reviewed, with original term, evidence, source, supporting-entity and qualifier/NOT payloads preserved. The shared normal Falcon attempt and perplexity-lite fallback both failed; logs are retained under `.cache/module-audit-logs/autonomous-flowering-fetch/ARATH-TOPP4-provider.log`. No provider report was fabricated. Manual primary-literature assessment and normal publication fetching supplied this review. Source access limits are stated per reference/claim. Generic protein binding follows the current informative-function policy; its removal does not reject the physical interactions. Nuclear localization does not by itself exclude additional compartments.


## PR #5574 follow-up: PP1-complex evidence

Replaced the isolated construct-name quote with the full PMID:19329567 Results sentence reporting FLAG-Inh3 coprecipitation with GST-PP1c constructs, explicitly including GST-TOPP4 and the GST-only negative control (Figure 2D/E). The adjacent Results report binding of AtInh3 to all nine Arabidopsis TOPP isoforms and loss upon RVxF mutation. PMID:7678768 independently identifies TOPP4 among the five cloned PP1 catalytic subunits. These results justify the retained complex-membership ACCEPT. Native plant co-IP detects PP1c without resolving TOPP4 specifically; AtInh3 is not renamed PP1R3. All 27 seeded row payloads and actions are preserved, with no NEW annotation. Completed review status corrected to COMPLETE.
