# tom20 manual deep research

S. pombe tom20 (PomBase:SPAC6F12.07; UniProt O14225) encodes the Tom20 family
receptor of the mitochondrial outer membrane TOM complex. UniProt annotates it
as a single-pass mitochondrial outer membrane protein, and PomBase carries ISO
and IC annotations from the budding-yeast TOM20 ortholog for TOM-complex
membership and multiple TOM-mediated import routes.

The conserved Tom20 activity is recognition of N-terminal mitochondrial
presequences at the cytosolic face of the TOM translocase. Yamamoto et al.
tested budding-yeast Tom20 and found that a long mitochondrial presequence
contains two Tom20-binding elements; the N-terminal element was essential for
mitochondrial targeting, while a C-terminal element increased import efficiency
before inner-membrane translocation. Their summary is explicit: Tom20 recognizes
the presequence targeting signal and tethers it to the TOM40 complex to
increase import efficiency [PMID:21173275].

Dekker et al. separated the budding-yeast TOM architecture into a Tom40/Tom22
general import pore and more peripheral receptors. They found that Tom22 is
stably associated with Tom40, while Tom20 and Tom70 are more loosely associated
with the GIP and can appear in distinct subcomplexes [PMID:9774667]. van Wilpe
et al. then showed that Tom22 docks the peripheral Tom20 and Tom70 receptors and
stabilizes higher-order TOM organization [PMID:10519552].

Annotation decisions: mitochondrial outer membrane and TOM complex rows are
accepted; `GO:0030150 protein import into mitochondrial matrix` is core because
Tom20 is the presequence receptor for the TOM/TIM23 route. PomBase IC route rows
to IMS import, TIM23-SORT inner-membrane insertion, and beta-barrel outer
membrane insertion are correct but non-core. `GO:0006886 intracellular protein
transport` and ARBA `GO:0007006 mitochondrial membrane organization` are
over-broad. The PAINT tRNA-import row comes from budding-yeast TOM20; I found no
direct evidence for a conserved S. pombe Tom20 role in mitochondrial tRNA
import, so it is marked over-annotated and left as an expert question.

GO-CAM consistency notes for 69729a3800007453: the model's tom20 activity uses
`GO:0140436 mitochondrial signal sequence receptor activity`, occurs in
`GO:0005741 mitochondrial outer membrane`, is part of the TOM complex, and is
part_of `GO:0030150`. That agrees with this review.
