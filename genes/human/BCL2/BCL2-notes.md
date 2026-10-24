# BCL2 annotation re-review, 2026-09-20

All 200 previous review rows were read individually: 199 source annotations and one
reviewer-proposed NEW row. The 199 source records are preserved. Available primary
abstracts, existing Falcon research, UniProt functional/localization text, and the
specific full texts below were evaluated. Full-gene review does not mean that every
underlying article was accessible in full; unresolved experiments remain UNDECIDED.

## Inherited functions and conditional BCL2 activity

The six original IBA rows trace to **PANTHER:PTN000135648**, in **PTHR11256**.
The fetched PAINT table places both positive and negative apoptosis regulation at
this ancestor, together with mitochondrial localization, channel activity,
cytochrome-c release, DNA-damage signaling and ligand-withdrawal signaling. The
target's experimental P10415 channel evidence is legitimate descendant grounding,
not circularity. See `interpro/panther/PTHR11256/paint.tsv` and `entries.csv`.
The available node assertions and target lineage do not establish a BCL2-specific
loss of these conditional functions. GO:0097192 ligand-withdrawal signaling can
include its mitochondrial checkpoint; it is not restricted to a death-receptor
complex. Broad signaling/transport/location terms need not be replaced simply
because more specific terms also apply.

**Channel capacity:** full cached [PMID:9144199](https://pubmed.ncbi.nlm.nih.gov/9144199/)
uses purified human BCL2 residues 1–218 lacking the terminal anchor. The authors
observe discrete planar-bilayer channels at pH 7.4; acid increases insertion.
Deletion of helices 5/6 distinguishes nonspecific perturbation from discrete
activity. This is distinct from the pH dependence of bulk liposomal dye/ion efflux.
The exact excerpt is “discrete channel activity was observed with random openings
and closings.” The report explicitly leaves conducting monomer versus dimer
unresolved. Channel activity and transmembrane transport are therefore retained
as contextual capacity, while GO:0046930 pore-complex membership is UNDECIDED.
Do not generalize PMID:9219694's acidic-pH liposome result into an absence of all
neutral-pH channels or into proof of the physiological channel mechanism.

**Proapoptotic conversion:** full cached
[PMID:18835031](https://pubmed.ncbi.nlm.nih.gov/18835031/) tests Nur77 peptide
binding, BCL2 loss/rescue, BH3 mutants and reconstituted membranes. Exposed BCL2
BH3 neutralizes BCLXL; in that system converted BCL2 is **not a direct BAX
activator**. Its regulatory work is more than loss of a protective substrate.
The Nur77 protein study [PMID:14980220](https://pubmed.ncbi.nlm.nih.gov/14980220/)
was additionally read as a full PDF: Figure 5 measures diffuse cytochrome-c
staining after BCL2 + Nur77/ΔDBD coexpression. BCL2 Y108K still colocalizes but
does not support release; endogenous BCL2 depletion reduces drug-induced death.
Figure 7 distinguishes the BH3-exposure mechanism and BAK-dependent cell contexts.
These support retaining positive apoptosis regulation and cytochrome-c release
as conditional roles. They do not establish a constitutive BCL2 cytochrome-c pore.
The shared human/mouse focused OpenScientist adjudication remains pending.

## Source-specific corrections

**DNA binding — direct assay identity, not an inference from protein location.**
The full [PMID:12086670 paper](https://eurekamag.com/research/003/657/003657662.pdf)
was accessible through the web PDF parser although direct local download returned
an anti-bot page. Results/Figure 3 state “MITF directly occupies the BCL2 promoter
in vivo.” Anti-MITF chromatin immunoprecipitation and anti-MITF EMSA supershifts,
including wild-type/mutant E-box comparisons in melanoma cells, identify MITF as
the DNA-binding protein. BCL2 is the regulated locus and survival effector.
GO:0043565 is removed for this source after reading the actual assay. The same
paper remains useful for BCL2-dependent melanocyte survival and pigmentation.

**Polyubiquitination — substrate versus performer.** The full
[PMID:16717086 paper](https://dash.harvard.edu/server/api/core/bitstreams/7078ebc7-954e-4242-ad18-5a3dd8d6c144/content)
was read, including Methods, Results, Figure 3G and Discussion. Human BCL2 was
expressed in Bcl2-null fibroblasts, immunoprecipitated in strong RIPA buffer to
dissociate partners, and probed for ubiquitin. The exact sentence is “The BCL-2 IP
was probed for ubiquitin.” MG132 increases the modified material. The experiment
identifies BCL2 as substrate; PP2A regulates its phosphorylation and stability.
No catalytic, scaffold or cofactor contribution of BCL2 to ubiquitin transfer is
shown. Remove GO:0000209 on that specific basis. The phosphorylation-mutant stress
responses and PP2A binding remain valid, independent functions.

**Adaptor versus binary interaction:** the full
[PMID:26858413 study](https://pmc.ncbi.nlm.nih.gov/articles/PMC4776483/) reports
a binary HBx/BCL2 structure, quantitative binding and interface mutants. It
supports BH3 binding rather than an assay of BCL2 assembling two other molecules.
Weak measured affinity is capacity, not absence. The separate mouse-derived
adaptor inference is left UNDECIDED because PMID:12617961 reports calcineurin
targeting and BCL2-dependent calcineurin/IP3-receptor association; these findings
are plausible but do not settle a simultaneous human ternary assembly.

**Autophagy:** full PMID:21358617 shows mitochondrial BCL2/AMBRA1 interaction and
LC3/chloroquine flux controls; a nonbinding AMBRA1 fragment escapes inhibition.
This is demonstrated inhibitory work and is accepted as a core regulatory role.
Full PMID:17446862 supplies the BECN1 BH3 interaction context. The old description
dismissing this as crosstalk was removed. Full PMID:19180116 includes BCL2 as a
pull-down control despite emphasizing BCLXL; PMID:19959994 measures BCL2/BECN1
dissociation. A title naming a paralog is not evidence of misattribution.

**Partner-specific binding:** full PMID:18719108 maps BCL2 interaction to ASPP2
ankyrin/SH3-region peptides, supporting SH3-domain binding. p53 interaction uses
its DNA-binding domain (PMID:16443602), not a BH3 domain. Nur77 uses the BCL2 loop;
PP2A, IP3R, AMBRA1, CISD2, G0S2, BAG1 and other partners are not automatically
BH3 ligands. Generic protein-binding rows are modified only when a supported
informative function exists; otherwise they are removed as uninformative,
without rejecting the physical interaction. Missing interface evidence is
UNDECIDED. Full source checks included 18835031, 19180116, 19959994, 23954414,
19521340, 25609812, 26004684, 21458670, 29749471 and 31206022. Beclin2/BCL2 binding
does not by itself prove the same mapped BH3 interface as Beclin1. BDA366-induced
conversion and NuBCP9-induced conversion should not be assumed mechanistically
identical merely because both expose a proapoptotic state.

**Population expansion and stimulus responses:** full PMID:28280358 Figure 4
uses CCK-8 and separate Annexin measurements. Rescue supports net population
growth, without distinguishing faster division from reduced death.
PMID:1373874 explicitly expresses human BCL2 in mouse pre-B cells and reports a
context-dependent twofold net growth advantage. These are retained as non-core.
The 17875758 CLL study could only be retrieved in portions: expression/pathway
analysis and HEM1 intervention do not resolve the BCL2-specific BCR, proliferation
and xenobiotic annotations; those source rows remain UNDECIDED. GO:0030307 cell
growth is separately uncertain in the calcium-flux source PMID:8022822.

Full PMID:10620603 Methods/Results demonstrate human BCL2 protection against Vpr
cytotoxicity in cells and membrane reconstitution. GO:0051607 includes protection
of the cell and does not require suppression of viral replication. Its protease
binding row remains UNDECIDED: the paper tests Vpr/ANT/VDAC and discusses a
separate HIV-protease cleavage study, without an identifiable BCL2/protease-binding
assay. By contrast PMID:16950491 reports BCL2-dependent productive HSV2 infection
in human U937 cells; regulation of viral replication can coexist with protection
from virus-induced death. Iron, nicotine, cytokine, radiation-conditioned-medium
and toxin response annotations are retained with their actual response/readout
scope, without inventing direct sensing or detoxification.

**Compartments and tissue roles:** orthology sources for cytosol, pigmentation,
hair morphogenesis, myelin and several process terms are mouse P10417 via Ensembl.
PMID:12617961 detects endogenous BCL2/calcineurin in cytosol as well as membrane
fractions; membrane anchoring does not prove exclusion. Pigment/hair roles are
retained as tissue-specific survival contributions. The exact myelin-sheath
image could not be verified from PMID:7953633, so that narrow location is
UNDECIDED. Nuclear, ER and mitochondrial annotations can coexist.

## Research reuse, limits and withdrawn proposal

The existing Falcon report was read. A full scan of provider JSON query/report
bodies found no prior BCL2-specific hypothesis report. Existing cached Ewing,
Hashimoto and bipolar reports mentioning BCL2 were inspected (cache identifiers
be5d8a18, 6f85c8a0, bb4e6f1f and ff21733c); disease-level discussion was not used
as a substitute for primary mechanistic evidence. No duplicate OpenScientist
request was launched. The shared conversion/channel report is coordinated by
the root reviewer.

The old NEW GO:1901029 is withdrawn because it duplicates the already represented
mitochondrial-permeability regulatory branch; its supported mechanism remains
in core functions. No new annotations were added. PMID:36599 remains a preserved
source identifier with UNDECIDED rows and a WRONG_IDENTIFIER reference review:
the fetched record is a Streptococcus antibiotic-resistance paper, and no
verified canonical replacement was established.


## Focused OpenScientist report incorporated (2026-09-21)

Read the complete [shared human/mouse report](BCL2-hypotheses/conditional-proapoptotic-and-channel-capacities/openscientist.md), including findings, evidence table, recommendations and limitations. Its central conclusion, "The proapoptotic capacity is real but proteoform- and context-dependent," agrees with the primary-based restoration already made. Its cleavage and Nur77 discussion adds independent consideration of PMID:9395403 and PMID:14980220. The specific work performed by converted BCL2 is supported more precisely by full PMID:18835031: exposed BH3 neutralizes BCLXL inhibition, allowing Bax-dependent membrane permeabilization, without directly activating Bax.

The report correctly lists the PMID:9144199 neutral-pH 18-pS channel assay, but repeatedly calls permeabilization acidic-only. That statement describes the carboxyfluorescein-vesicle experiment in PMID:9219694, not an absence of all neutral-pH ion conduction. The previously read full channel paper explicitly says, "When the His 6 -Bcl-2 (ΔTM) protein was applied to planar bilayers at neutral pH in symmetric 0.5 M KCl, discrete channel activity was observed with random openings and closings." Native membrane relevance remains unresolved; artificial membrane conditions do not erase demonstrated capacity. GO:0055085 has no bulk-transport requirement.

The report admits the PAINT placement was "inferred from annotation presence, not from direct inspection of the PANTHER tree." Its annotation-count narrative is not used as a lineage analysis; the independent PTN000135648 check above remains the provenance. Likewise, it reviewed sequence conservation but no mouse functional primary assays, so the mouse reviewer must retain species-specific source assessment. Its recommendation to add IDA annotations for already represented terms is not adopted: no redundant NEW rows.

GO:0046930 pore complex stays UNDECIDED because the report does not identify multimeric assembly or resolve the channel paper's explicit monomer-versus-dimer uncertainty. Channel capacity and a protein-complex location are separate assertions. No action changes were required after report incorporation; the restored NONCORE calls remain grounded in primaries, and the report is marked DISPUTED for these mechanistic and coverage limits. Findings and limitations were shared with the mouse Bcl2 reviewer.


## Recovery PR review: generic binding policy (2026-09-22)

Applied the repository policy to the re-reviewed GO:0005515 rows. Removal concerns
the uninformative function label and does not refute the source interaction.
Rows whose target-specific assays remain inaccessible are UNDECIDED. Source
assertions and supporting evidence are preserved.

- PMID:29849149: ACCEPT -> REMOVE
- PMID:9463381: ACCEPT -> REMOVE
