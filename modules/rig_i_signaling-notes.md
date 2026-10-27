# RIG-I signaling module notes

## 2026-10-27 — ATG13/ASB1 membership triage (issue #3922)

**Question.** Should ATG13 be represented in this module, and is its nonautophagic role in
MAVS polyubiquitination a mechanism distinct from canonical autophagy?

**Answer.** Yes to both, but as an **optional** amplifying part, not as a core transduction
step, and without bringing autophagy machinery into the module.

### What the evidence supports

The mechanism is mapped to a residue and a region, which is what distinguishes it from a
generic co-regulator claim. ATG13 binds the MAVS aa 180-360 region
[PMID:42704283 "we identified the aa 180–360 of MAVS as the key domain for its interaction with ATG13"],
and the modified lysine is identified
[PMID:42704283 "when the lysine at position 348 of MAVS was mutated to arginine (K348R), ATG13 failed to increase the K63-linked polyubiquitination of MAVS"].

ATG13 is non-catalytic in this role
[PMID:42704283 "The ATG13 protein itself lacks E3 ubiquitin ligase activity, thus precluding it from directly polyubiquitinating MAVS."],
so the ligase was identified separately. ASB1 binds MAVS but not the flanking pathway
components
[PMID:42704283 "Immunoprecipitation analysis revealed an interaction between ASB1 and MAVS but not between ASB1 and RIG-I or TBK1"],
and reporter epistasis places it at the MAVS step rather than downstream
[PMID:42704283 "ASB1 enhances RIG-I N- and MAVS-mediated IFN-β and ISRE reporter activity without increasing the expression of TBK1, IKKϵ, or IRF3-5D"].
The ligase identity is CRL5: ASB1 is the substrate receptor
[PMID:42704283 "As ASB1 is the substrate-recognition subunit of the Cullin-RING E3 ligase complex 5 (CRL5)"]
and the scaffold is required
[PMID:42704283 "knockdown of Cullin 5 attenuated the ATG13-induced enhancement of MAVS K63-linked polyubiquitination"].

The claim is not overexpression-only. Endogenous loss of function moves the modification
[PMID:42704283 "ATG13 knockdown reduced the K63-linked polyubiquitination of endogenous MAVS"],
the ATG13 effect runs through ASB1
[PMID:42704283 "ASB1 knockdown attenuated the ATG13-mediated increase in MAVS K63-linked polyubiquitination"],
and both proteins have an antiviral output in human lung epithelial cells
[PMID:42704283 "the knockdown of ATG13 resulted in a significant increase in the titre of the influenza virus in A549 cells"],
[PMID:42704283 "ASB1 knockdown enhanced IAV titres, indicating that ASB1 directly suppresses IAV replication"].
The link from the modification to signalosome activation is MAVS oligomerization
[PMID:42704283 "ATG13 enhanced the oligomerization level of MAVS"].

### Why this is distinct from autophagy

Three independent lines, which is why only the adaptor role is modeled and the ULK1 complex
is left out of the module. Domain mutants that disable the autophagy-relevant interactions
retain the MAVS activity
[PMID:42704283 "both mutants retained the ability to increase the activity of the MAVS downstream reporter"];
early autophagy inhibition does not remove it
[PMID:42704283 "ATG13 retained its function in promoting MAVS-mediated IFN signalling even after the addition of 3-MA"];
and the substrate is not on an autophagic membrane
[PMID:42704283 "MAVS did not colocalize with LC3 in cells"].

### Why optional rather than core

The modeling convention is that regulation stays outside the module core unless the pathway
definition requires it. Every perturbation here changes the magnitude of MAVS signalling, not
its existence: knockdown lowers ubiquitination and raises viral titre, it does not abolish
RIG-I/MAVS signal transduction. The precedent in this repository is the context-dependent LYN
regulator in `modules/b_cell_receptor_signaling.yaml`, modeled as a part with a
`POSITIVELY_REGULATES` connection and described as "a context-dependent activating
contribution, not a unique obligatory initiator". The same shape is used here: part 4
(`mavs_k63_polyubiquitination`, `optional: true`) positively regulates
`mavs_signalosome_assembly`.

### Scope limits recorded rather than asserted away

One group, influenza A only (H9N2 and H1N1), human cell lines (HEK-293T, A549, THP-1), no in
vivo or primary-cell data, and the ASB1-upstream-of-TBK1 placement uses overexpressed pathway
components. Other K63 ligases have been reported for MAVS
[PMID:42704283 "TRIM31 and TRIM22 increase the K63-linked polyubiquitination of MAVS, thereby increasing the activation of the interferon pathway"],
so no alternative-ligase `variant_set` is asserted until those ligases are themselves reviewed
and a second independent study constrains the set. This is
recorded as the module's `knowledge_gaps` entry, since whether the axis generalizes decides
whether the part is promoted to the core or re-modeled as a pathogen-specific branch.

### Follow-up not done here

`genes/human/ATG13` carries no innate-immunity content and does not assert GO:0097027; the
module validator correctly reports this as a `FUNCTION_UNREVIEWED` coverage advisory. Adding
the role to the ATG13 gene review, and creating reviews for the missing members MAVS, RIGI and
ASB1, are separate pieces of work.
