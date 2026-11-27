
## 2026-11-06 taxon audit

Applied the annotation-reviewer and core-function guidance to the complete gene review. All inherited annotation payloads are preserved, including PP_2634's authored NEW process row. Status COMPLETE means annotation decisions are complete; it does not imply direct KT2440 experiments exist.

The normal command `just deep-research PSEPK PP_2634 --provider falcon` was attempted and failed with HTTP 403 authentication/access error. No Falcon report was produced or fabricated; the existing OpenScientist report and artifacts were preserved. These notes document the manual fallback. Source claims were evaluated against the target UniProt domain/feature annotations and original publications. No IBA rows occur in these targets, so there is no IBA lineage-loss decision. No bare GO:0005515 rows occur.

Shared source distinctions: PMID:23222542 and PMID:24704788 examine Rhodobacter sphaeroides BcsAB expressed heterologously, not KT2440 proteins. PMID:31604608 resolves an E. coli BcsC fragment (710-1157). PMID:39242554 includes Rhodobacter/E. coli chimeras and an engineered BcsC-TPR/BcsB fusion for the detailed interface; neither the fusion nor E. coli BcsB hexamer stoichiometry is transferred to KT2440. PMID:39394223 uses E. coli 1094 for native phenotype assays and a bcs-deleted BL21*(DE3) host for recombinant assembly. PMID:21507177 explicitly studies P. putida mt2 and gives operon-level physiological context; PMID:30889223 uses KT2442/KT2440-related backgrounds to study promoter regulation, not direct accessory-protein catalysis.

Normally fetched PMID:33563593 now has full text. PMID:19400787 remains abstract-only after normal force-fetch; accessible claims are supplemented by later full-text structures, so lack of its full text does not prevent the present inference. Root fetched PMID:39394223 full text. The full 2015 review PMID:26077867 was checked for architecture diversity. Reviews PMID:38688160, PMID:41617292 and PMID:39319708 were available as abstracts only and do not justify additional target molecular claims.

Retained the single inherited NEW cellulose biosynthetic process assertion; it is not a new proposal in this audit. Its support now includes structural participation rather than necessity alone. [PMID:39394223, "BcsQ buttresses the PilZ domain, likely stabilizing the catalytically competent state."] The target's BcsQ-specific signatures are strong identity evidence despite its generic submitted cellulose synthase name, which is recorded as a source defect. The protein is not BcsA and does not inherit glycosyltransferase activity.

PMID:33563593 reports "the BcsHisRQWT complex exhibited only weak adenosine triphosphatase (ATPase) activity in vitro" and BcsE-dependent inhibition. It models hydrolysis downstream of complex formation rather than demonstrating an ATP-powered cellulose transporter. Direct inspection of the unchanged 235-aa target sequence shows a divergent N-terminal region `MTSLALHGVRGGLGRSALLAALGYALQGVG`; no residue-by-residue alignment or motif conservation is asserted. No ATP-binding or hydrolysis row was added merely from the generic P-loop NTPase signature. The core states an inferred BcsQ assembly/stabilization role without forcing an MF term. Exact nucleotide specificity/activity, partners and polar localization remain target-specific knowledge gaps.

## PR2143 round17: bacterial process specificity

BcsQ supplies structural support to the synthase assembly. Its one historical authored NEW term is refined under an explicit exception, with the complete original annotation YAML archived at analysis/module_audits/bacterial_cellulose_biosynthesis/round17-PP2634-original-annotation.yaml. All 87 machine rows remain unchanged; this authored refinement is never counted as a preserved machine payload.

QuickGO definitions checked on 2026-11-06 establish GO:0090540 as an is_a subtype of GO:0030244 with bacterial context. The parent and child share the cellulose chemistry criteria. Native output, intact-cell synthesis, crystallinity and fibrils are independent evidence questions, not extra requirements introduced by the bacterial subtype.

Original source/provider bytes and machine payloads are preserved. Supporting sources and target-specific limits are recorded in the reviewed annotation; no new annotation row is introduced in this follow-up.
