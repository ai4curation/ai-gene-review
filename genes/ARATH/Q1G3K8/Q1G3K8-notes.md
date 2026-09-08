# Q1G3K8 / AT4G28556 / RIC7 review notes

## 2026-09-07 — evidence and scope

Q1G3K8 is the 216-aa CRIB-domain RIC7 protein at AT4G28556. The separately
encoded AT4G28560/F4JLB7 protein is a 450-aa LRR protein also called EXLRR12.
The detailed database-name investigation, TAIR comparisons, Cornell citation,
and JBrowse figure are in the
[project report](../../../projects/PROTNLM_EVALUATION/F4JLB7-RIC7-locus-identity.md).
The [sequence/primer analysis](Q1G3K8-bioinformatics/RESULTS.md) connects the
published Wu and Hong RIC7 primers to AT4G28556. It distinguishes experimental
targets without assuming that every older construct exactly matches the current
canonical sequence.

### ROP binding and localization

[Wu et al. 2001, PMID:11752391](https://doi.org/10.1105/tpc.010218),
Tables 1, 2 and 4 and the ROP1-binding/localization experiments, support RIC7
interaction with active ROP1, cytoplasmic and apical plasma-membrane localization,
and inhibition of elongation upon expression in tobacco pollen tubes. This is
heterologous overexpression evidence, not an Arabidopsis loss-of-function
demonstration of an endogenous inhibitory role. The publication cache is
abstract-only; relevant full-text passages and primer table were inspected via
indexed PMC text. The primer mapping supplies target-identity evidence.

[Jeon et al. 2008, PMID:18178769](https://doi.org/10.1105/tpc.107.054544),
Figure 7 and its associated Results, explicitly concern AT4G28556 and demonstrate
preferential interaction with GTP-loaded ROP2. GFP-RIC7 redistributes from a
predominantly nuclear pool in darkness to the membrane/cytoplasm with light;
active ROP2 recruits it to the membrane, whereas inactive ROP2 does not.
The experiments express Arabidopsis RIC7 in Vicia faba guard cells. Nuclear
localization is supported, but a nuclear biochemical role is not established.
The local cache is abstract-only and foregrounds ROP2; the RIC7 findings were
checked in indexed full-text Figure 7/Results and agree with the experimentally
sourced [Swiss-Prot entry](https://rest.uniprot.org/uniprotkb/Q1G3K8.txt).

### Stomatal physiology and Exo70B1

[Hong et al. 2016, PMID:26451971](https://doi.org/10.1111/nph.13625),
published online in 2015, provides Arabidopsis mutant, complementation and
overexpression evidence for restraint of stomatal opening and identifies
Exo70B1 as an interacting downstream component. The local abstract directly
supports the new negative-regulation-of-opening annotation. Methods and Results
also describe accelerated ABA-induced closure in ric7 and rescue by the native
promoter construct. The closure finding complements the later Zhu et al. evidence for the proposed stomatal-closure regulation annotation. The transcript
primers map exactly to NM_001036663.2; promoter-fragment boundaries and the physical
insertion have not been independently reconstructed. The report of an insertion
in the second intron is consistent with the multi-exon AT4G28556 model.

### Review decisions

All 14 seeded GOA annotations were reviewed. The root ND molecular-function
annotation is better represented by small GTPase binding; nuclear localization
and pollen-tube-growth inference are retained as non-core. The remaining
localization and signaling annotations agree with the target evidence.
Negative regulation of stomatal opening and regulation of stomatal closure are proposed as new IMP annotations.
The molecular activity is ROP binding/effector function; RIC7 is not itself a
GTPase, GEF or kinase. Exo70B1 interaction does not make RIC7 an exocyst subunit.

GO:0031267 (small GTPase binding) and GO:1902457 (negative regulation of stomatal
opening) were checked against the QuickGO ontology service on 2026-09-07.
The 14 original GOA term/evidence/source records were retained unchanged.

### Generated research assessment

The falcon report generated on 2026-09-07 usefully examines the 2001 pollen
experiments but misses Jeon et al. (2008), Hong et al. (2016), and Zhu et al. (2021). Its assertions
that downstream partners, loss-of-function phenotypes and non-pollen roles are
unknown are contradicted by those primary studies. It is retained as generated
provenance and was not used to support those negative assertions. The review
uses the primary literature, experimentally sourced Swiss-Prot record and
reproducible sequence checks. The validator's suggestion to cite the generated
report is therefore intentionally not followed.

### Zhu et al. 2021: ABA and ROS

[PMID:33586611](https://doi.org/10.1080/15592324.2021.1876379) is available
in the cache with full text. The ric7-2 and ric7-3 promoter insertions increase
RIC7 expression; they are gain-of-expression lines, not null mutants. Their
reduced ABA-induced closure and lower ROS accumulation support a regulatory
role. Both reported qRT-PCR primers map exactly to AT4G28556. The study does
not establish RIC7 as a ROS-producing enzyme, scavenger or DNA-binding
transcription factor, and expression changes in other genes are downstream
readouts. The shared closure phenotype with the independently characterized
Hong lines supports the process assignment.
