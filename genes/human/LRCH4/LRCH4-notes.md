# LRCH4 literature notes

## Evidence boundary

LRCH4 is much less directly characterized in humans than the current annotation set can
make it appear. The decisive functional paper is a mixed-species study dominated by mouse
macrophage and mouse in vivo experiments, with a smaller direct human-cell experiment. Its
abstract explicitly says that LRCH4 is "widely expressed across murine tissues" and that
"Silencing Lrch4 attenuates cytokine induction by LPS and multiple other TLR ligands and
dampens the in vivo innate immune response." [PMID:30523158, "It is widely expressed across
murine tissues and has two expression variants that are both regulated by lipopolysaccharide
(LPS)."; "Silencing Lrch4 attenuates cytokine induction by LPS and multiple other TLR
ligands and dampens the in vivo innate immune response."]

The full text does contain a direct human experiment, but it used engineered HEK293 cells
stably expressing TLR4/MD-2/CD14 or TLR2 rather than a native human immune-cell system.
Endogenous human LRCH4 siRNA reduced ligand-induced IL-8 in both systems and did not reduce
the TNF-alpha-induced response. [PMID:30523158, "HEK293 cells stably expressing either
TLR4/MD-2/CD14 or TLR2 were transfected with Lrch4 siRNA or Scr siRNA and then exposed to
LPS or Pam3CSK4, respectively."; "As shown in Fig. 2G, Lrch4 siRNA attenuated IL-8
induction by both ligands in HEK293 cells"; "Lrch4 silencing did not affect induction of
IL-8 by HEK293 cells in response to stimulation with TNFα"]

This species/context split supports retaining the TLR/raft biology as plausible and
experimentally grounded, while labeling the detailed membrane-raft mechanism as chiefly
mouse evidence rather than established native-human macrophage biology.

## Membrane, LPS and lipid-raft evidence

The 2019 study describes LRCH4 as a membrane protein with nine LRRs in a predicted
ectodomain and reports that LRCH4 promotes LPS docking in lipid rafts. [PMID:30523158,
"Lrch4 is a membrane protein with nine LRRs in its predicted ectodomain."; "Lrch4 promotes
proper docking of LPS in lipid raft membrane microdomains."] LRCH4 depletion reduced
surface ganglioside signal and CD14 abundance/display. [PMID:30523158, "Lrch4 silencing
reduces cell surface gangliosides, a metric of raft abundance, as well as expression and
surface display of CD14, a raft-resident LPS co-receptor."]

The underlying mouse work supports a role in raft abundance/organization and LPS delivery,
not proof that LRCH4 is itself an LPS receptor. Biotin-LPS co-precipitation was explicitly
interpreted as direct *or indirect*. [PMID:30523158, "Lrch4 was detected in the biotin-LPS
pulldown (but not in cells treated with nonbiotinylated LPS, as expected), suggesting that
it interacts either directly or indirectly with LPS."]

The longest mouse product was predicted to contain a C-terminal transmembrane segment;
the shorter predicted mouse variant lacked it, but the authors cautioned that physiological
expression of the predicted variants had not been verified. [PMID:30523158, "Lrch4 variant
1 (680 AAs) is as described above, whereas variant 2 (649 AAs) is truncated C-terminal to
the CH and omits the TMD, consistent with a soluble protein."; "Physiological expression
of the predicted variants has not been verified to our knowledge."] Human O75427 is a
683-aa reviewed protein with a predicted C-terminal transmembrane segment, but exact
sidedness and endogenous organelle distribution should not be inferred from sequence alone.

## DOCK-family interactions and localization

The 2020 systematic Rho-regulator study supplies the strongest direct interaction evidence.
The publisher PDF figure legend states that LRCH4 bound the C-Dock subfamily members DOCK6,
DOCK7 and DOCK8 but not DOCK9, and that the DOCK7 DHR2 fragment was sufficient in the
anti-tag immunoprecipitation assay. [PMID:32203420, "LRCH4 binds all C-Dock RhoGEFs, but
not DOCK9. The DOCK-DHR2 domain is sufficient for binding."] The same study observed
LRCH4 at the endoplasmic reticulum and recruitment of DOCK8 there; deleting the putative
LRCH4 transmembrane region moved the proteins toward the cell periphery. [PMID:32203420,
"showing the recruitment of DOCK8 to the endoplasmic reticulum by LRCH1 and LRCH4, or to
the cell periphery by LRCH4-ΔTMR"]

These experiments establish reproducible binding and localization effects in transfected
HEK293T/MDCK cells. They do **not** establish an endogenous stable LRCH4-DOCK complex, a
specific Rho GTPase regulated by LRCH4, or a direct link between the DOCK interaction and
LRCH4's TLR/raft phenotype. The GOA rows from PMID:24255178 also list DOCK7 and SUGT1,
whereas older/global screens list MDFI, several keratin-associated proteins and a set of
membrane/ER proteins. Those screen-level pairs are useful hypotheses, not core functions.

## Direct human expression and disease-context evidence

Human platelet RNA and protein were detected directly. E. coli K12 exposure reduced LRCH4
RNA in two analysis pipelines, but did not produce a visible LRCH4 protein abundance or
molecular-weight change under the tested conditions. [PMID:30385858, "For the RNAs of HMBS
(logFC = +5.73), ATP2C1 (logFC = -3.13) and LRCH4 (logFC = -4.07) changes were detectable
by thromboSeq and Tuxedo pipelines."; "By Western blot analysis we could demonstrate the
presence of HMBS, ATP2C1 and LRCH4 proteins in platelets before and after E. coli K12
exposure"; "We detected no visible concentration difference or molecular weight change of
ATP2C1 and LRCH4 in platelets after E. coli K12 exposure."] This supports regulated human
expression during bacterial exposure, not a causal platelet function.

In HT29 colorectal-cancer cells, LRCH4 siRNA reduced proliferation, migration and invasion
and reduced YAP and TGF-beta/Smad outputs. [PMID:38383956, "Here, we reported that the
knockdown of LRCH4 inhibited the proliferation, migration and invasion in HT29 cells.";
"The activity of Yes-Associated Protein (YAP), a transcription factor in the Hppo-YAP
signaling pathway, was significantly inhibited by LRCH4-siRNA."; "the TGF-β/Smad signaling
pathway, as the downstream pathway of Yap, was also inhibited by LRCH4 knockdown."] This is
a single cancer-cell context with no direct biochemical LRCH4 target, so it should remain
non-core.

## Seeded-reference audit and negative boundaries

- PMID:16449650 is a SAP25/mSin3 paper whose abstract and full PMC text localize SAP25,
  not LRCH4: [PMID:16449650, "A fraction of SAP25 is located in promyelocytic leukemia
  protein (PML) nuclear bodies, and PML induces a striking nuclear accumulation of SAP25."]
  Searches of the full article for LRCH4, O75427, LRN and LRRN aliases found no LRCH4
  evidence, so the PML-body citation is a source miscitation rather than an LRCH4 nuclear
  function.
- A live QuickGO check on 2026-08-18 returned the mouse source rows
  `Q921G6 / GO:0001765 / IDA / PMID:16449650` and
  `Q921G6 / GO:0034123 / IDA / PMID:16449650`. Thus the source miscitation is present on
  the current mouse raft-assembly and TLR-signaling rows as well as on the human PML-body
  chain. PMID:30523158 independently supports the mouse raft and TLR biology, but does
  not repair those mechanical source records.
- PMID:9799793 discovered the chromosome 7q22 locus but only reported sequence similarity:
  [PMID:9799793, "Two genes showed weak similarity to an insulin-like receptor and a
  neuronal protein with a leucine-rich amino-terminal domain."] It does not experimentally
  support nervous-system development.
- PMID:16189514, PMID:19060904, PMID:24255178, PMID:25416956 and PMID:32296183 are broad
  interaction maps. Their GOA/IntAct pairs should not be converted into stable-complex or
  pathway claims without follow-up.
- A single calponin-homology domain is not evidence of actin binding. No direct LRCH4-actin
  assay was found.
- LRCH1's DOCK8-CDC42/T-cell mechanism and LRCH3's DOCK7-MYO6-septin mechanism must not be
  transferred to LRCH4. The LRCH4-specific experiments support C-Dock binding/localization
  but do not identify the downstream GTPase or a septin/myosin complex.

## Literature-search note

PubMed/Europe PMC searches through 2026-08-18 identified the 2019 LRCH4 innate-immunity
paper, the 2018 human-platelet study, the 2020 Rho-regulator interaction study and a 2024
HT29 colorectal-cancer knockdown paper as the primary mechanistic literature most relevant
to this review. A June 2026 colorectal-cancer manuscript was present as a preprint and was
not used as established evidence. No convincing human disease-causing LRCH4 allele,
isoform-specific physiological function, direct actin-binding experiment, or native stable
LRCH4 complex was identified.
