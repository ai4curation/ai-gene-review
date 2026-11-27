# tom22 manual deep research

S. pombe tom22 (PomBase:SPAC17H9.16; UniProt O13813) encodes the fungal Tom22
family receptor/scaffold of the TOM complex. The protein has a predicted
cytosolic N-terminal domain, a single transmembrane span, and a short
intermembrane-space C-terminal domain, matching the topology needed for
receptor functions on both sides of the outer membrane.

The core experimental literature comes from budding yeast. Dekker et al. found
that Tom22 stably associates with Tom40 in the general import pore, unlike the
more loosely associated Tom20 and Tom70 receptors, and that the GIP complex
containing Tom40, Tom22, Tom5, Tom6, and Tom7 forms the central unit of the
outer membrane import machinery [PMID:9774667]. van Wilpe et al. then showed
that Tom22 is multifunctional: it binds preproteins through both cytosolic and
IMS domains, docks Tom20 and Tom70 through its cytosolic domain, and is required
for higher-level organization and tight channel gating of the TOM translocase
[PMID:10519552].

Annotation decisions: the TOM complex and mitochondrial outer membrane component
rows are accepted. `GO:0140436 mitochondrial signal sequence receptor activity`
is the core molecular function. `GO:0008320 protein transmembrane transporter
activity` is accepted only with `contributes_to`: Tom40 is the conducting pore,
while Tom22 binds substrates and organizes the TOM machinery that enables
transport. Matrix import is accepted as a core process; IMS import and the
TIM22/TIM23-SORT route rows are correct but non-core; generic `GO:0006886
intracellular protein transport` is over-broad.

GO-CAM consistency notes for 69729a3800007453: the model contains Tom22
activities whose molecular_function is the root `GO:0003674`. Because the S.
pombe GOA set already has `GO:0140436` by ISO and a `contributes_to GO:0008320`
IBA for Tom22, the root-MF Tom22 activities should be reviewed in the final
GO-CAM consistency pass.
