# HDA1 notes

## 2026-05-13 Falcon incorporation

Falcon supports HDA1 as a nuclear chromatin-associated catalytic subunit of the HDA1 complex, with HDA2/HDA3 needed for full complex activity and targeting [file:yeast/HDA1/HDA1-deep-research-falcon.md "Hda1 functions in a multi-subunit histone deacetylase complex with Hda2 and Hda3, where Hda2/Hda3 are required for full Hda1 activity and targeting."]. It also summarizes the primary functional model as chromatin association, histone-tail deacetylation, and transcriptional repression [file:yeast/HDA1/HDA1-deep-research-falcon.md "Strong experimental evidence supports chromatin association, histone-tail deacetylation (H2B/H3 and context-dependent H4), and transcriptional repression."].

The strongest core function is hydrolytic histone deacetylase activity in the HDA1 complex, not generic hydrolase or generic protein binding. Falcon explicitly flags the generic hydrolase term as too broad [file:yeast/HDA1/HDA1-deep-research-falcon.md "Too broad; evidence is specific for histone lysine deacetylase/HDAC activity rather than generic hydrolase"] and treats protein/identical protein binding as partially supported but nonspecific compared with complex membership [file:yeast/HDA1/HDA1-deep-research-falcon.md "Some support for Hda1 self-interaction and partner binding, but broad GO terms are less informative than complex membership"].

Falcon supports H3/H2B deacetylation in promoter-proximal repression contexts and H4 deacetylation in highly transcribed coding regions [file:yeast/HDA1/HDA1-deep-research-falcon.md "Tup1 recruits Hda1 to deacetylate histones **H3 and H2B** at promoter-adjacent nucleosomes (e.g., ENA1), supporting histone-substrate specificity and a repression mechanism."] [file:yeast/HDA1/HDA1-deep-research-falcon.md "Modern spike-in normalized ChIP-seq/ChIP-qPCR demonstrates Hda1C-dependent **H4 deacetylation within coding regions** of highly transcribed genes."]. This means the previous review's H3/H2B emphasis was broadly correct, but the description needed to avoid implying that H4 is unsupported.

Non-core calls are important here. Falcon found weak support for cytoplasmic HDA1 localization, noting that cytosolic relocalization evidence in the retrieved set concerns Hda2/Hda3 rather than Hda1 itself [file:yeast/HDA1/HDA1-deep-research-falcon.md "No direct evidence for Hda1; cytosolic relocalization reported for Hda2/Hda3 under hypoxia, not Hda1"]. Positive transcriptional effects appear rare or indirect relative to the dominant repression/dampening model [file:yeast/HDA1/HDA1-deep-research-falcon.md "The dominant evidence supports repression/dampening via deacetylation."].

## 2026-09-02 Audit correction: GO:0005737 cytoplasm IBA should not be REMOVEd

The GO:0005737 (cytoplasm, is_active_in, IBA) row was previously marked `action: REMOVE`
on the grounds that HDA1's documented function is nuclear. That reasoning does not meet
the project's bar for overturning an IBA. Per the project IBA policy (see
`projects/IBA_REVIEW.md` and the IBA section of CLAUDE.md), an IBA encodes a PAINT
curator's judgment about where in the tree a function arose; the length of the WITH/FROM
donor list is not a proxy for evidential strength, and an IBA should be challenged only
with target-specific evidence of divergence or loss, not because other studies emphasize
a different compartment. Here the donor list is in any case broad -- 19 gene-product
donors spanning fly, mouse, rat and Arabidopsis plus human class II HDAC orthologs
(P56524/HDAC4 and Q9UBN7/HDAC6 among them), together with the ancestral node
PANTHER:PTN000065904 [file:yeast/HDA1/HDA1-goa.tsv]. Nucleocytoplasmic distribution is a
conserved property of this subfamily, and there is no HDA1-specific evidence
contradicting that ancestral capacity: the falcon report notes only that cytosolic
relocalization has been reported for the partners HDA2/HDA3 under hypoxia rather than
for HDA1 [file:yeast/HDA1/HDA1-deep-research-falcon.md "No direct evidence for Hda1;
cytosolic relocalization reported for Hda2/Hda3 under hypoxia, not Hda1"] -- an absence
of positive evidence, not evidence of loss. So `REMOVE` is not warranted.

The qualifier, however, is `is_active_in`, not `located_in`, and that distinction was
missed in the first pass. `is_active_in` asserts that HDA1 carries out its molecular
function in the cytoplasm, which is a stronger claim than the donor evidence supports.
The cytoplasmic activity anchoring this node in the donors is HDAC6 alpha-tubulin
deacetylation, executed by a class IIb-specific architecture (tandem catalytic domains
plus a ZnF-UBP domain) that HDA1 lacks; class IIa shuttling is driven by 14-3-3-binding
phosphosites that are likewise not an evident HDA1 feature. HDA1's only established
molecular function is chromatin-associated histone deacetylation, which is nuclear. The
falcon synthesis reaches the same conclusion in its own verdict line
[file:yeast/HDA1/HDA1-deep-research-falcon.md "Cytoplasm (CC): likely weak/incorrect for
Hda1 itself."], and flags such claims as weak or conditional
[file:yeast/HDA1/HDA1-deep-research-falcon.md "should be treated as **weak/conditional**"].

The action is therefore `MARK_AS_OVER_ANNOTATED` rather than `KEEP_AS_NON_CORE`: the
compartment is retained (the IBA-overturn bar is not met) while the activity claim
embedded in the qualifier is flagged as unestablished. `located_in GO:0005737` would be
the accurate form of this annotation.
