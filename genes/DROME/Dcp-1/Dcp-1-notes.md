# Dcp-1 notes

## 2026-09-30

Created the Drosophila `Dcp-1` review for the APOPTOSIS conserved-comparator
slice from the seeded GOA rows, UniProt record, and cached primary literature.
No provider-generated deep-research file was used.

## Core executioner-caspase role

Dcp-1 is a short-prodomain Drosophila effector caspase. The cloning paper
identified "Drosophila caspase-1 (DCP-1)" and reported it was structurally and
biochemically similar to C. elegans CED-3
[PMID:8999799 DCP-1, a Drosophila cell death protease essential for
development, "caspase, named Drosophila caspase-1 (DCP-1), was identified and
found to be"]. Genetics later placed Dcp-1 downstream of Dronc, partially
redundant with DrICE: Dcp-1 single mutants had reduced eye-disc apoptosis, and
`drice/dcp-1` double mutants completely suppressed developmental apoptosis
[PMID:16980627 DRONC coordinates cell death and compensatory proliferation,
"developmental apoptosis in the eye disc was completely suppressed in
drice/dcp-1 double mutants"]. In vCrz neurons, the two effector caspases again
cooperate for programmed removal during metamorphosis
[PMID:21120926 Drosophila caspases involved in developmentally regulated
programmed cell death of peptidergic neurons during early metamorphosis, "vCrz
PCD requires both ice and dcp-1 functions"].

GOA rows to top-level `GO:0006915 apoptotic process`,
`GO:0010623 programmed cell death involved in cell development`, and
`GO:0012501 programmed cell death` were therefore biologically sound but
too broad. They were narrowed to `GO:0097194 execution phase of apoptosis`.

## Contextual non-core branches

Dcp-1 is reused outside the generic apoptosis-execution core.

- In oogenesis, dcp-1 loss blocks nurse-cell cytoplasmic dumping and the
  cytoskeletal/nuclear events that accompany nurse-cell death
  [PMID:9422696 Requirement for DCP-1 caspase during Drosophila oogenesis,
  "inhibiting this transfer. dcp-1- nurse cells were defective in the
  cytoskeletal"]. DrICE and Dcp-1 also act redundantly during late oogenesis
  [PMID:17464325 The Drosophila caspases Strica and Dronc function
  redundantly in programmed cell death during oogenesis, "effector caspases
  drice and dcp-1 also display"].
- Starvation-induced oogenesis engages Dcp-1 and the IAP Bruce at autophagy
  checkpoints [PMID:18794330 Effector caspase Dcp-1 and IAP protein Bruce
  regulate starvation-induced autophagy during Drosophila melanogaster
  oogenesis, "At these two stages, the effector caspase Dcp-1 and the
  inhibitor"]. A later mitochondrial study showed that pro-Dcp-1 interacts with
  SesB and promotes autophagic flux by lowering SesB/ATP
  [PMID:24862573 The Drosophila effector caspase Dcp-1 regulates
  mitochondrial dynamics and autophagic flux via SesB, "Dcp-1 promotes
  autophagy by negatively regulating SesB and"].
- Dcp-1 also represses Drosophila Toll signaling by cleaving/degrading DIF,
  the Toll-pathway NF-kappaB factor [PMID:36002459 Apoptotic caspase inhibits
  innate immune signaling by cleaving NF-kappaBs in both Mammals and Flies,
  "Drosophila effector caspases, drICE and DCP-1, also mediated"].
- In the larval neuromuscular system, Dcp-1 belongs to the Eiger/Wengen,
  Debcl, Dark, and Dronc prodegenerative branch that can be separated from
  normal NMJ development [PMID:22153373 Glial-derived prodegenerative
  signaling in the Drosophila neuromuscular system, "mutations in eiger,
  dcp-1, debcl, and dark show no obvious NMJ phenotype"].

The direct nurse-cell, mitochondrial, Toll, and NMJ rows were retained as
`KEEP_AS_NON_CORE`. Broader ovarian transport, starvation-response, and
oogenesis rows were narrowed where possible to `GO:0045476 nurse cell apoptotic
process` or `GO:0016239 positive regulation of macroautophagy`.

## Rows left unresolved

The BIR-domain and generic DIAP1 `GO:0005515 protein binding` rows are
plausible, but the local abstracts only establish IAP-caspase antagonism in
general [PMID:10481910 The Drosophila caspase inhibitor DIAP1 is essential for
cell survival and is negatively regulated by HID, "disrupting productive
IAP-caspase interactions"] and active DrICE binding by DIAP2
[PMID:16485033 Systematic in vivo RNAi analysis of putative components of the
Drosophila cell death machinery, "DIAP2 binds active drICE"]. I left the
Dcp-1/DIAP1 rows `UNDECIDED` pending full-text verification of the
Dcp-1-specific interaction and any BIR-domain mapping.

The neuron-remodeling rows were also left `UNDECIDED`: the cached abstract says
fly effector caspases work in neurite pruning, but does not expose a direct
Dcp-1 perturbation [PMID:20445064 Axonal degeneration is regulated by the
apoptotic machinery or a NAD+-sensitive pathway in insects and mammals,
"parallel to the fly effector caspases"].

## Wrong-gene neuronal granule rows

Three UniProtKB localization imports were removed. PMID:17178403 and
PMID:21267420 study the Drosophila mRNA-decapping enzyme `Dcp1`/`Dcp1p` in
P-body-like neuronal ribonucleoprotein granules, not the caspase `Dcp-1`
[PMID:17178403 Staufen- and FMRP-containing neuronal RNPs are structurally and
functionally related to somatic P bodies, "RNA-degradative enzymes Dcp1p and
Xrn1p/Pacman"; PMID:21267420 The Me31B DEAD-Box Helicase Localizes to
Postsynaptic Foci and Regulates Expression of a CaMKII Reporter mRNA in
Dendrites of Drosophila Olfactory Projection Neurons, "including the mRNA
hydrolases, Dcp1, and Pcm/Xrn-1"].
