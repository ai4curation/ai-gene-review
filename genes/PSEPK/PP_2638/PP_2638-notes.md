
## 2026-11-06 taxon audit

Applied the annotation-reviewer and core-function guidance to the complete gene review. All inherited annotation payloads are preserved, including PP_2634's authored NEW process row. Status COMPLETE means annotation decisions are complete; it does not imply direct KT2440 experiments exist.

The normal command `just deep-research PSEPK PP_2638 --provider falcon` was attempted and failed with HTTP 403 authentication/access error. No Falcon report was produced or fabricated; the existing OpenScientist report and artifacts were preserved. These notes document the manual fallback. Source claims were evaluated against the target UniProt domain/feature annotations and original publications. No IBA rows occur in these targets, so there is no IBA lineage-loss decision. No bare GO:0005515 rows occur.

Shared source distinctions: PMID:23222542 and PMID:24704788 examine Rhodobacter sphaeroides BcsAB expressed heterologously, not KT2440 proteins. PMID:31604608 resolves an E. coli BcsC fragment (710-1157). PMID:39242554 includes Rhodobacter/E. coli chimeras and an engineered BcsC-TPR/BcsB fusion for the detailed interface; neither the fusion nor E. coli BcsB hexamer stoichiometry is transferred to KT2440. PMID:39394223 uses E. coli 1094 for native phenotype assays and a bcs-deleted BL21*(DE3) host for recombinant assembly. PMID:21507177 explicitly studies P. putida mt2 and gives operon-level physiological context; PMID:30889223 uses KT2442/KT2440-related backgrounds to study promoter regulation, not direct accessory-protein catalysis.

Normally fetched PMID:33563593 now has full text. PMID:19400787 remains abstract-only after normal force-fetch; accessible claims are supplemented by later full-text structures, so lack of its full text does not prevent the present inference. Root fetched PMID:39394223 full text. The full 2015 review PMID:26077867 was checked for architecture diversity. Reviews PMID:38688160, PMID:41617292 and PMID:39319708 were available as abstracts only and do not justify additional target molecular claims.

PF05420/IPR008410 and upstream TPR repeats independently support a BcsC-family channel. [PMID:31604608, "The membrane-integrated porin domain of BcsC forms a kidney-shaped 16-stranded β-barrel".] Added one missing molecular-function row, GO:0015159 polysaccharide transmembrane transporter activity, as ISS, and used it in the core. This describes the conserved channel-mediated cellulose export rather than polymerization or ATP-driven transport. QuickGO checked 2026-11-06: GO:0015159 is active and defines polysaccharide transfer across membranes. GO:0015288 porin activity is active but explicitly limits its substrate to less than 1000 Da, so its familiar name is inappropriate for the cellulose polymer. No active cellulose-specific transporter term was found in the name search. Retained both original rows. The E. coli pEtN decoration and exact BcsB-BcsC architecture are not claims about KT2440 product chemistry.

## PR2143 round17: bacterial process specificity

The BcsC-family channel contributes transport machinery to synthesis. Refine the original general process using MODIFY while preserving its machine payload; neither polymerase catalysis nor a direct KT2440 export assay is asserted.

QuickGO definitions checked on 2026-11-06 establish GO:0090540 as an is_a subtype of GO:0030244 with bacterial context. The parent and child share the cellulose chemistry criteria. Native output, intact-cell synthesis, crystallinity and fibrils are independent evidence questions, not extra requirements introduced by the bacterial subtype.

Original source/provider bytes and machine payloads are preserved. Supporting sources and target-specific limits are recorded in the reviewed annotation; no new annotation row is introduced in this follow-up.
