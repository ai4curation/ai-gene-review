# CASP3 (Caspase-3) review notes

UniProt: P42574 (CASP3_HUMAN), 277 aa precursor. EC 3.4.22.56. Peptidase C14A family.
Synonyms: CPP32, Yama, apopain, SCA-1. Heterotetramer of two p17 (large) + p12 (small) subunits.

## Core identity / molecular function
- CASP3 is a cysteine-dependent aspartate-directed endopeptidase: cleaves substrates after Asp
  with strict requirement for Asp at P1 and P4 (preferred motif DxxD-|-). [UniProt CATALYTIC ACTIVITY,
  "Strict requirement for an Asp residue at positions P1 and P4. It has a preferred cleavage sequence of Asp-Xaa-Xaa-Asp-|-"]
- It is the principal effector/executioner caspase of apoptosis. Purified as "apopain" responsible
  for PARP cleavage, derived from proenzyme CPP32; related to ICE and C. elegans CED-3. [PMID:7596430,
  "This enzyme, named apopain, is composed of two subunits ... derived from a common proenzyme identified as CPP32 ...
  apopain/CPP32 is important for the initiation of apoptotic cell death"]
- Activated by upstream initiator caspases (CASP8, CASP9, CASP10) and granzyme B; PTM section confirms
  cleavage by granzyme B, caspase-6, -8, -10 generates the two active subunits. [UniProt PTM]
- Caspase-3 is the major executioner caspase, more promiscuous than caspase-7, and "appears to be the major
  executioner caspase during the demolition phase of apoptosis." [PMID:18723680]

## Substrate cleavage / downstream demolition (all DEPEND on the same MF, mostly downstream processes)
- PARP1 cleavage at 216-Asp|Gly-217 (hallmark execution substrate). [UniProt FUNCTION; PMID:16374543 nuclear
  caspase-3 activation and PARP cleavage early in camptothecin apoptosis]
- ICAD/DFF45 cleavage -> releases CAD/DFF40 endonuclease for oligonucleosomal DNA fragmentation. Apoptotic
  DNA laddering relies on cytosolic DFF40/CAD activated by caspase processing of ICAD. [PMID:22253444]
- GATA-1 cleavage in erythroid precursors; Hsp70 protects GATA-1 during terminal erythroid differentiation
  (link to erythropoiesis). [PMID:17167422]
- Phospholipid scramblase / PtdSer exposure: cleaves XKR8 and ATP11C flippase to drive apoptotic PtdSer "eat me"
  signal; also XRCC4 cleavage releases fragment activating Xkr4 scrambling. [PMID:24904167 ATP11C flippase;
  PMID:33725486 XRCC4/Xkr4]
- IL-18 processing in monocytes (CASP3 contributes along with CASP1). [PMID:9334240]; note newer UniProt text
  says CASP3 "cleaves and inactivates IL18" (context-dependent).
- Pyroptosis crosstalk: cleaves/activates gasdermin-E (GSDME/DFNA5) to switch apoptosis to secondary
  necrosis/pyroptosis and permit IL-1b release. [PMID:28459430 caspase-3 cleavage of a gasdermin (GSDME);
  PMID:33852854 GSDME permits IL-1b release; Reactome R-HSA-9647632 CASP3 cleaves GSDME]
  CASP3 also cleaves/inactivates GSDMD (Reactome R-HSA-9686088), generally inhibiting GSDMD pyroptosis.
- Antiviral / innate immunity restraint: cleaves cGAS, MAVS, IRF3 to suppress type I IFN during apoptosis;
  cleaves NF-kB members p65/RelA, RelB, c-Rel to dampen cytokine production. [PMID:30878284; PMID:36002459]
- Tau cleavage (Alzheimer link), BACE/GGA3 -> amyloid-beta (APP processing). [PMID:12888622; PMID:9736630;
  PMID:17553422]
- Many additional substrates curated by Reactome (desmosomal cadherins, fodrin/spectrin, ROCK1, gelsolin,
  beta-catenin, MST kinases, etc.) — these are CASP3 substrate-cleavage reactions, located in cytosol/nucleus.

## Localization
- Cytoplasm (UniProt SUBCELLULAR LOCATION, PMID:15003516). Procaspase cytosolic; active CASP3 also translocates
  to nucleus during apoptosis (PARP, DFF45 cleavage there). Nuclear localization is functional/active-site
  context (PMID:16374543 nuclear caspase-3 activation; Reactome R-HSA-211219 translocation to nucleus).

## Regulation
- S-nitrosylation of catalytic Cys163 keeps procaspase inactive; denitrosylated on Fas activation. [UniProt PTM;
  PMID:10213689]
- Inhibited by XIAP (BIR2) and ubiquitinated/inhibited by BIRC6/BRUCE (relieved by SMAC/DIABLO). [UniProt;
  PMID:11257232 XIAP structure]
- ADP-riboxanation at Arg207 by bacterial CopC blocks activation (microbial infection).

## Curation strategy
- CORE molecular function: GO:0004197 cysteine-type endopeptidase activity (many IDA + IBA) -> ACCEPT.
  Broader MF parents (GO:0008234 cysteine-type peptidase, GO:0008233 peptidase, GO:0004175 endopeptidase) ->
  ACCEPT as correct-but-general. GO:0004190 aspartic-type endopeptidase activity is WRONG (CASP3 is a cysteine
  protease that cleaves after Asp; it is not an aspartic protease) -> REMOVE.
- CORE biological process: apoptotic process (GO:0006915), execution phase of apoptosis (GO:0097194),
  proteolysis (GO:0006508), protein processing/maturation -> ACCEPT.
- Pyroptosis terms (GO:0070269, GO:0140639) -> ACCEPT (well supported IDA, gasdermin cleavage).
- Many tissue/process annotations (neuron/erythrocyte/keratinocyte differentiation, hippocampus development,
  synapse pruning, platelet formation, learning/memory, muscle differentiation) are downstream non-apoptotic or
  tissue-specific roles -> KEEP_AS_NON_CORE.
- Long list of IEA GO_REF:0000107 "response to X" stimulus terms (hypoxia, glucose, nicotine, ethanol, X-ray,
  metal ion, etc.) are ortholog-transferred stimulus/response terms, not core; mostly KEEP_AS_NON_CORE; a few
  questionable MF transfers (aspartic-type endopeptidase, CDK inhibitor, phospholipase A2 activator) -> REMOVE/
  MARK_AS_OVER_ANNOTATED.
- bare protein binding (GO:0005515, IPI, many) -> MARK_AS_OVER_ANNOTATED / KEEP_AS_NON_CORE (uninformative;
  many from interactome screens). Do not endorse as core.
- Reactome cytosol/nucleoplasm CC TAS (dozens) -> ACCEPT location, but these are substrate-cleavage reaction
  contexts; cytosol/nucleus are valid.

## Exact supporting quotes gathered (for supported_by)
- PMID:18723680: "Caspase-3 was found to be generally more promiscuous than caspase-7 and appears to be the
  major executioner caspase during the demolition phase of apoptosis."
- PMID:7596430: "This enzyme, named apopain, is composed of two subunits of relative molecular mass (M(r)) 17K
  and 12K that are derived from a common proenzyme identified as CPP32." / "suggesting that apopain/CPP32 is
  important for the initiation of apoptotic cell death."
- PMID:9334240: "the other is caspase-3, which cleaves both precursor and mature hIL-18 at Asp71-Ser72 and
  Asp76-Asn77 to generate biologically inactive products."
- PMID:16374543: "the activation of nuclear caspases-7 and -3, and poly(ADP-ribose) polymerase (PARP) cleavage,
  are early events in camptothecin-induced apoptosis."
- PMID:17167422: "Caspase-3 is activated during both terminal differentiation and erythropoietin-starvation-
  induced apoptosis of human erythroid precursors." / "Hsp70 prevents active caspase-3 from cleaving GATA-1 and
  inducing apoptosis."
- PMID:22253444: "the activation of, at least, caspase-3 is necessary for the proper cleavage of ICAD L/S."
- PMID:28459430: "GSDME was specifically cleaved by caspase-3 in its linker, generating a GSDME-N fragment that
  perforates membranes and thereby induces pyroptosis."
- PMID:30878284: "activated caspase-3 cleaved cGAS, MAVS, and IRF3 to prevent cytokine overproduction." /
  "Caspase-3 was exclusively required in human cells."
- PMID:36002459: "caspase-3 can mediate the cleavage of NF-κB members p65/RelA, RelB, and c-Rel via its protease
  activity."
- PMID:33725486: "Upon apoptotic stimuli, XRCC4, contained in the DNA repair complex, is cleaved by caspases,
  and its C-terminal fragment with an intrinsically disordered region is released into the cytoplasm."
- PMID:11257232: "We report the crystal structure of the second BIR domain of XIAP (BIR2) in complex with
  caspase-3, at a resolution of 2.7 A, revealing the structural basis for inhibition."
- PMID:8689682: "Cells undergoing apoptosis in vivo showed increased release of cytochrome c to their cytosol"
  (intrinsic/apoptosome upstream of CASP3 activation).
- PMID:15565177: "typical apoptotic features such as caspase-3 activation and cleavage of poly(ADP-ribose)-
  polymerase" (DIP/E2F1 intrinsic apoptosis).
- PMID:33852854: GSDME "cleaved by apoptosis-associated CASP3"; non-cleavable GSDME D270A "altered at the CASP3
  cleavage and activation site."

## Falcon deep research integration (2026-06-21)

Falcon (Edison) deep-research report is in `CASP3-deep-research-falcon.md`; it strongly corroborates the existing
review/annotations (executioner cysteine-aspartate protease, EC 3.4.22.56, DxxD specificity, CASP8/9 activation,
PARP1/ICAD/GSDME substrates, cytoplasmic+nuclear localization, non-apoptotic differentiation roles, IFN restraint),
adding no contradictions but a few refinements. All Falcon-sourced citations below are not yet independently verified
against full text.

New / refined points (beyond existing notes):
- Refined cleavage motif: native-lysate subtiligase N-terminomics gives a stronger CASP3 consensus DEVD↓(G/S/A) at
  P4-P1↓P1' (not just generic DxxD↓), with cleavage also gated by local structural accessibility. [Araya et al.,
  ACS Chem Biol 2021, doi:10.1021/acschembio.1c00456; Soni & Hardy, Biochemistry 2021, doi:10.1021/acs.biochem.1c00459]
  (not yet independently verified against full text)
- Scale of substrate repertoire quantified: ~906 putative substrates / 1126 cleavage sites in native lysates, of which
  577 sites and 257 substrates were novel vs the apoptosis DegraBase; substrates ~49% cytoplasmic and ~48% nuclear.
  [Araya et al., ACS Chem Biol 2021, doi:10.1021/acschembio.1c00456] (not yet independently verified against full text)
- CASP3 vs CASP7 non-redundancy: human GSDME is cleaved efficiently by CASP3 but not by CASP7 (attributed to CASP7 p10
  subunit / prime-side recognition differences), supporting CASP3 as the dominant/most proteolytically proficient
  executioner. [Blais & Denault, Biosci Rep 2026, doi:10.1042/bsr20254030; Mustafa et al., Cells 2024,
  doi:10.3390/cells13221838] (not yet independently verified against full text)
- New substrate: CAD (carbamoyl-phosphate synthetase 2/aspartate transcarbamylase/dihydroorotase, CAD enzyme of
  pyrimidine synthesis) cleaved at Asp1371 prior to degradation, linking CASP3 to pyrimidine synthesis control and
  chemosensitivity. [Tannous et al., Bioconjug Chem 2025, doi:10.1021/acs.bioconjchem.5c00151] (not yet independently
  verified against full text) — note potential ambiguity: report's "CAD" elsewhere also denotes caspase-activated DNase.
- Non-apoptotic cytoprotective autophagy / DDR: CASP3+CASP7 promote starvation- or proteasome-inhibition-induced
  cytoprotective autophagy and the DNA-damage response in breast cancer cells; loss reduces LC3B/ATG7 and H2AX
  phosphorylation, and is synthetic-lethal with BRCA1 deficiency. [Samarasekera et al., PLoS Biol 2025,
  doi:10.1371/journal.pbio.3003034] (not yet independently verified against full text) — relevant to existing
  GO:0016241 regulation of macroautophagy annotation.
- IFN restraint mechanism specified: CASP3/7 prevent MOMP-released mtRNA from triggering the MDA5/MAVS/IRF3 type I IFN
  pathway, keeping apoptosis immunologically silent. [Killarney et al., Nat Commun 2023, doi:10.1038/s41467-023-37146-z]
  (not yet independently verified against full text) — consistent with existing GO:0001818 negative regulation of
  cytokine production / cGAS-MAVS-IRF3 cleavage notes (PMID:30878284).
- Neural stem cell differentiation: non-apoptotic CASP3/7 events bias adult NSCs toward direct (division-independent)
  neuronal conversion, requiring transcription factor Atf3 (zebrafish tracer). [Rosa et al., Development 2024,
  doi:10.1242/dev.204381] (not yet independently verified against full text) — supports existing neuron-differentiation
  / non-core developmental annotations.
- Non-apoptotic synaptic role + context-dependent pro-oncogenic role: CASP3 drives synaptic pruning / dendritic-spine
  loss / LTD without death (Parkinson model), and via EndoG->nucleus and Src-STAT3 can promote oncogenic transformation.
  [Fieblinger et al., Int J Mol Sci 2022, doi:10.3390/ijms23105470] (not yet independently verified against full text) —
  consistent with existing synapse-pruning (GO:0098883) non-core annotations.

Discrepancies / annotations to revisit:
- No direct contradictions with the existing review were found; Falcon is consistent with the curated picture.
- The execution/substrate-cleavage themes (autophagy regulation, IFN/cytokine restraint, NSC and synaptic roles) are
  already captured as ACCEPT or KEEP_AS_NON_CORE, so no action implied for those. The only candidate for a possible
  NEW supporting annotation is the CASP3-vs-CASP7 substrate-discrimination point, but this is a comparative-biochemistry
  observation rather than a new GO term for CASP3 itself; no annotation change recommended from Falcon alone.

## GO:0005515 re-review (2026-09-28)

- Re-reviewed all generic protein binding rows under the current policy: direct substrate-interaction papers were
  converted to `MODIFY` with `GO:0004197` as the replacement, uninformative interactome/inhibitor/regulator bindings
  were changed to `REMOVE`, and PMID:15246877 was left `UNDECIDED` because the cached abstract does not mention CASP3
  and the full text is unavailable.


## 2026-10-25 comparative apoptotic-execution review

Systematically examined all 199 rows, preserving every imported annotation payload. Decisions judge the biological claim, not the evidence code: independently established cysteine endopeptidase activity, cytosolic/nuclear localization and apoptotic execution are retained/refined even when one original citation is not sufficient alone. No experimental claim is rejected merely because the cached abstract foregrounds a different protein. Bare protein-binding removals mean uninformative annotation, not false interaction.

Species and paralogs: human CASP3/CASP7 have distinct natural-substrate profiles (PMID:18723680). Mouse CASP7 can cleave ICAD efficiently and contributes to strain-dependent compensation for Casp3 loss (PMID:15525783). The 129X1/SvJ versus C57BL/6J comparison in PMID:12152782 must not be conflated with the 129S1/SvImJ comparison in PMID:15525783. These results do not establish universal redundancy or a single obligatory executioner across tissues.

CASP6: full PMID:32029622 establishes direct CASP3/CASP7 cleavage of procaspase-6 in vitro (Fig. 6A), inhibitor-sensitive procaspase-6 processing in primary hepatocytes (Fig. 6B), and a CASP6–BID mitochondrial feedback mechanism; Fig. 6H uses HepG2 cells. It does not justify a universal initiator-caspase activation route. Full PMID:32298652 and public primary Figure 6A identify mouse CASP6/RIPK3 constructs despite the HEK293T host; native infection experiments also use mouse cells/mice. Human prior NEW adaptor annotation is retired/UNDECIDED; conserved contextual human immune claims remain explicitly comparative. Mouse IAV findings do not imply a requirement for all inflammasome triggers.

CASP7: full PMID:35705808 establishes mouse SMPD1 processing and membrane-pore repair. CASP7 performs proteolytic maturation; SMPD1 performs ceramide-producing lipid hydrolysis. Repair delays lysis in the tested settings, so this mechanism is not universally pro-lytic. PMID:22464733 distinguishes PARP1 cleavage from PARP1 poly-ADP-ribosylation activity.

Evidence handling: checked existing primary caches and retained unresolved precise cellular/stimulus claims as UNDECIDED where evidence could not establish the claim. 0 pre-existing nonverbatim deep-research quotations were removed from the optional quotation field; source citations and review rationales remain, with direct primary evidence preferred for core functions. Provider reports remain immutable. Existing reports were used where present; missing Falcon reports were attempted with perplexity-lite fallback, and failures are recorded in .cache/module-audit-logs/apoptosis-caspase-*-research.log. No missing report was fabricated. Sources were fetched through normal helpers only.

Verified UniProt PANTHER placement: PTHR10454 CASPASE; CASP3/Casp3 SF198 CASPASE-3, CASP6/Casp6 SF206 CASPASE-6, CASP7/Casp7 SF31 CASPASE-7. These are membership checks, not assertions of identical physiological deployment.

The annotation-reviewer consultation confirmed that true same-target catalytic/location claims should not be removed for citation weakness, and that substrate cleavage is not the same as the substrate's enzymatic reaction. Notes are comparative; only target-specific claims are asserted in the review.

Primary-support follow-up: 8 retained annotation rows received claim-specific primary/curated support; 26 precise contextual claims without adequate inspected support were explicitly set UNDECIDED. Provider citations remain in the bibliography but are no longer the sole asserted evidence for these retained claims.


## PR5558 source-specific transfer audit (2026-10-26)

Reassessed 25 previously templated UNDECIDED rows. The full per-row provenance, primary-study scope, access status and decision are recorded in genes/human/CASP3/CASP3-source-analysis/transfer-evidence-audit.tsv. Seed WITH/FROM and live QuickGO donor records were used only to trace publications; they are not evidence for a function, and no relationship qualifier was interpreted. All biological quotations come from the normally cached primary papers. No original row field, row count or core function was changed.

Response terms can include changes in enzyme production/gene expression, so a drug-dependent abundance change is not automatically rejected for lacking a gene knockout. This does not make CASP3 a drug receptor or prove apoptotic activation. Conversely, an expression marker accompanying a behavioral test does not establish swimming locomotion. Cellular-component claims were assessed from donor localization: neuronal cell bodies from rat PrP106-126 injury, and postsynaptic/glutamatergic compartments from the mouse spine study. Neuronal differentiation has independent neurosphere inhibition support alongside the rat observational source and existing PAINT inference; no ancestral reconstruction or universal neuronal requirement was invented.

Nine claims remain unresolved across the two reviews, each with a specific cited assay/access limit: axon bundling, hippocampal anatomical development, glucose or nicotine stimulus specificity, exact anterior neural-fold fusion, and steady-state T-cell population homeostasis. Full PMID:21515572 establishes the Casp3 hith2 encephalocele phenotype but does not by itself identify anterior-fold fusion; the Scrib crn2 phenotype in the same paper is kept separate without accusing the curator of a gene mix-up. Full PMID:18701083 supports activated-T-cell restraint during anergy, while the original PMID:12970760 abstract foregrounds B cells and does not expose every T-cell assay. No negative verdict is inferred from a title or missing abstract detail.

Normal PMID force-fetches were used to recover available full text; the first21515572 fetch failed, and a normal retry obtained full text. PMID16103108 and18701083 were resolved through EuropePMC and fetched normally. Existing provider reports were not rewritten or fabricated. The normal caches still lack full text for several donor studies, explicitly recorded in publication-access.json.

- Row 8 (zero-based), GO:0030182 neuron differentiation: KEEP_AS_NON_CORE; primary PMID:16103108. The PAINT assertion traces to PANTHER:PTN002573018, with rat Casp3 experimental grounding. This is an inherited-node judgment, not a donor-count or pairwise-similarity test; no target-specific loss is inferred. The rat donor publication PMID:15248196 distinguishes active-caspase-3-positive proliferating/differentiating cerebellar cells from apoptotic cells. Independent PMID:16103108 goes beyond colocalization: caspase activity rises in nonapoptotic differentiating neuronal populations and peptide inhibition impairs neurosphere differentiation. The inhibitor experiment is not a caspase-3-specific genetic knockout, but together with the PAINT/conserved caspase context it supports a non-core neuronal differentiation role, not universal dependence of all neurons. The abstract does not specify the neurosphere species, so no direct human or mouse assay is invented.
- Row 37 (zero-based), GO:0001554 luteolysis: KEEP_AS_NON_CORE; primary PMID:25332219. Provenance trace: GO_REF:0000107 via UniProtKB:P55213|ensembl:ENSRNOP00000014096. The traced rat corpus-luteum study measures luteal apoptosis over regression, uses an active-caspase-3 antibody, and perturbs ER stress with TUDCA in PGF2alpha-treated luteal cells. This supports the conserved apoptotic-effector contribution to structural luteolysis. It does not establish identical upstream endocrine control in humans, a direct steroidogenic activity, or universal necessity of CASP3 for every stage of luteal regression.
- Row 38 (zero-based), GO:0001666 response to hypoxia: KEEP_AS_NON_CORE; primary PMID:18466900. Provenance trace: GO_REF:0000107 via UniProtKB:P55213|ensembl:ENSRNOP00000014096. The rat donor evidence is an altitude-induced hippocampal injury study measuring caspase activity, active caspase-3 and apoptotic cells; its perturbations concern p75NTR/NMDA signaling. A second traced study, PMID:24089674, measures caspase-3 in hypoxic-ischemic neonatal rat brain after miR-210 manipulation. Retain conserved execution within a hypoxic-stress response as non-core, without attributing oxygen sensing or a direct human hippocampal experiment to CASP3.
- Row 45 (zero-based), GO:0007413 axonal fasciculation: UNDECIDED; primary PMID:25898930. Provenance trace: GO_REF:0000107 via UniProtKB:P55213|ensembl:ENSRNOP00000014096. The rat source PMID:25898930 examines PrP106-126-induced spinal-neuron axonal degeneration, DR6 knockdown and caspase-6 inhibition/siRNA. Its accessible abstract localizes cleaved caspase-3 to somata and reports axonal protection from caspase-6 manipulation. GO:0007413 specifically denotes collecting axons into bundles, not any axonal injury phenotype. The normal force-fetch remained abstract-only; it cannot establish whether a separate caspase-3-dependent bundling assay appears in the full text. Retain uncertainty about this exact transfer, not a claim that CASP3 lacks any neuronal function or that the curator confused paralogs.
- Row 49 (zero-based), GO:0009410 response to xenobiotic stimulus: KEEP_AS_NON_CORE; primary PMID:18274634. Provenance trace: GO_REF:0000107 via UniProtKB:P55213|ensembl:ENSRNOP00000014096. The full rat donor study measures myocardial caspase-3 protein expression during baicalin/octreotide treatment of severe acute pancreatitis. GO:0009410 includes changes in enzyme production and gene expression after a xenobiotic; it does not require that CASP3 be the drug receptor or upstream sensor. Retain the broad contextual response inference, not the authors' cardioprotection mechanism as a CASP3-specific function. Protein abundance is not itself proof of catalytic activation or apoptotic myocardial death; the paper reports very little myocardial apoptosis.
- Row 50 (zero-based), GO:0009749 response to glucose: UNDECIDED; primary PMID:19356108. Provenance trace: GO_REF:0000107 via UniProtKB:P55213|ensembl:ENSRNOP00000014096. The traced rat donor reference concerns HO-1/carbon monoxide/adiponectin treatment in streptozotocin diabetes. Its cached abstract explicitly describes TNF-alpha-induced endothelial caspase-3 activity, not a defined glucose-exposure assay. GO:0009749 requires a glucose stimulus; diabetes alone does not identify that stimulus. The full experimental article remains unavailable in the inspected cache, so a glucose-specific experiment cannot be confirmed or excluded. Retain UNDECIDED rather than treat a diabetic-model context as direct glucose-response evidence or assert that the annotation is false.
- Row 51 (zero-based), GO:0010038 response to metal ion: MODIFY; primary PMID:18598848. Provenance trace: GO_REF:0000107 via UniProtKB:P55213|ensembl:ENSRNOP00000014096. The traced source PMID:18483861 treats cultured rat cardiomyocytes with the platinum drug carboplatin; it does not by itself isolate a free-metal-ion stimulus. Independent PMID:18598848 directly tests cobalt chloride in rat PC12 cells and measures the caspase cascade. Thus the broad metal-response claim is supported at least for cobalt, and is refined to the already-present response-to-cobalt-ion term, rather than removed. This neither attributes metal binding to CASP3 nor equates carboplatin exposure with isolated platinum-ion sensing.
- Row 52 (zero-based), GO:0010165 response to X-ray: KEEP_AS_NON_CORE; primary PMID:18239382. Provenance trace: GO_REF:0000107 via UniProtKB:P55213|ensembl:ENSRNOP00000014096. The rat source compares locally X-irradiated nephritic kidneys with nonirradiated nephritic controls and measures increased active caspase-3/7 together with tissue apoptosis. Retain a conserved executioner response to irradiation as non-core. This is not DNA-repair activity, a direct human kidney experiment, or proof that CASP3 alone mediates the therapeutic effect.
- Row 53 (zero-based), GO:0014069 postsynaptic density: KEEP_AS_NON_CORE; primary PMID:21151119. Provenance trace: GO_REF:0000107 via UniProtKB:P70677|ensembl:ENSMUSP00000147767. This cellular-component transfer traces to mouse Casp3 and PMID:21151119, not to the rat stimulus-response papers. The donor study detects local caspase-3 activity in hippocampal spines and connects it to calcineurin-dependent loss of postsynaptic GluR1. Retain the experimentally curated postsynaptic compartment as a comparative non-core localization. The available abstract supports the local synaptic pool but does not reproduce the full postsynaptic-density fractionation/imaging methods; no direct human localization assay is claimed.
- Row 55 (zero-based), GO:0021766 hippocampus development: UNDECIDED; primary PMID:18459132. Provenance trace: GO_REF:0000107 via UniProtKB:P55213|ensembl:ENSRNOP00000014096. The rat donor study measures active/precursor caspase-3 distribution, nuclear morphology and developmental age in CA1, CA3 and dentate gyrus. This is genuine region-specific expression evidence, but the available abstract does not establish the precise contribution of CASP3 to hippocampal anatomical development, as distinct from expression in developing tissue or removal of individual cells. The full article has not been available in the inspected cache. Preserve this contextual process claim as unresolved without rejecting the measured expression or inferring target-specific loss.
- Row 57 (zero-based), GO:0030182 neuron differentiation: KEEP_AS_NON_CORE; primary PMID:16103108. Provenance trace: GO_REF:0000107 via UniProtKB:P55213|ensembl:ENSRNOP00000014096. The rat donor publication PMID:15248196 distinguishes active-caspase-3-positive proliferating/differentiating cerebellar cells from apoptotic cells. Independent PMID:16103108 goes beyond colocalization: caspase activity rises in nonapoptotic differentiating neuronal populations and peptide inhibition impairs neurosphere differentiation. The inhibitor experiment is not a caspase-3-specific genetic knockout, but together with the PAINT/conserved caspase context it supports a non-core neuronal differentiation role, not universal dependence of all neurons. The abstract does not specify the neurosphere species, so no direct human or mouse assay is invented.
- Row 60 (zero-based), GO:0032025 response to cobalt ion: KEEP_AS_NON_CORE; primary PMID:18598848. Provenance trace: GO_REF:0000107 via UniProtKB:P55213|ensembl:ENSRNOP00000014096. The rat PC12 donor experiment directly applies CoCl2 and measures apoptotic caspase activities, DNA fragmentation and their attenuation by estradiol. Retain the conserved stress-execution response to cobalt as non-core. The evidence concerns chemically induced hypoxic stress, not a cobalt cofactor requirement, direct metal receptor, or a native human tissue assay.
- Row 61 (zero-based), GO:0032355 response to estradiol: KEEP_AS_NON_CORE; primary PMID:18598848. Provenance trace: GO_REF:0000107 via UniProtKB:P55213|ensembl:ENSRNOP00000014096. The same traced PC12 study tests estradiol pretreatment and measures decreased caspase-cascade activity under cobalt stress. A response term can include reduced activity; it does not imply that estradiol activates CASP3. Retain this conserved, context-dependent modulation as non-core, without assigning estrogen-receptor activity or claiming an unchallenged human neuronal response.
- Row 62 (zero-based), GO:0032496 response to lipopolysaccharide: KEEP_AS_NON_CORE; primary PMID:18289516. Provenance trace: GO_REF:0000107 via UniProtKB:P55213|ensembl:ENSRNOP00000014096. The rat donor study injects LPS into pregnant animals and measures a time-ordered caspase cascade and cleaved caspase-3 in fetal brain. Retain execution downstream of this inflammatory stimulus as a non-core comparative response. Maternal/fetal injury is not direct LPS recognition by CASP3, and the result must not be generalized to all tissues or treated as an innate immune receptor mechanism. Normal refresh still lacks complete full text; the specific activation time course is explicit in the abstract.
- Row 64 (zero-based), GO:0035094 response to nicotine: UNDECIDED; primary PMID:18477628. Provenance trace: GO_REF:0000107 via UniProtKB:P55213|ensembl:ENSRNOP00000014096. The rat PC12 source tests nicotine during tunicamycin versus thapsigargin ER stress. Its accessible abstract reports GRP78, caspase-12, XBP1 and ATF6 changes, but does not expose a caspase-3-specific result. This is not a wrong-paralog verdict: CASP3 could have been assayed in the full text, which was not available in the inspected cache. The exact CASP3 nicotine-response transfer therefore remains unresolved, with a source and specific missing assay identified.
- Row 67 (zero-based), GO:0042542 response to hydrogen peroxide: KEEP_AS_NON_CORE; primary PMID:18479463. Provenance trace: GO_REF:0000107 via UniProtKB:P55213|ensembl:ENSRNOP00000014096. The donor experiment uses rat H9c2 cardiomyocytes and directly measures peroxide-induced caspase-3 cleavage/activity and protection after short leptin pretreatment. Retain the conserved oxidative-stress execution response as non-core, not peroxide detoxification or sensing. The 1-hour versus 24-hour pretreatment difference is a source-specific limitation, not a universal leptin/CASP3 relationship.
- Row 68 (zero-based), GO:0043025 neuronal cell body: KEEP_AS_NON_CORE; primary PMID:25898930. Provenance trace: GO_REF:0000107 via UniProtKB:P55213|ensembl:ENSRNOP00000014096. Unlike the axon-bundling process claim transferred from the same paper, this cellular-component assertion has direct support in the rat source abstract: cleaved caspase-3 is enriched in neuronal cell bodies during prion-peptide injury. Retain the conserved somatic neuronal pool as a non-core localization. The experimental condition does not establish exclusive somatic localization in every neuron or direct localization in the target species.
- Row 70 (zero-based), GO:0043200 response to amino acid: KEEP_AS_NON_CORE; primary PMID:18423997. Provenance trace: GO_REF:0000107 via UniProtKB:P55213|ensembl:ENSRNOP00000014096. The full rat spinal-cord study applies glutamate and measures activated caspase-3 after excitotoxic exposure. Retain the amino-acid-stimulus response in this injury context, not amino-acid biosynthesis or nutrient sensing. The paper explicitly notes persistent staining when little further cell loss occurs, so caspase-3 staining is not equated with inevitable rapid apoptosis or a universal human spinal injury mechanism.
- Row 74 (zero-based), GO:0045471 response to ethanol: KEEP_AS_NON_CORE; primary PMID:23102656. Provenance trace: GO_REF:0000107 via UniProtKB:P55213|ensembl:ENSRNOP00000014096. The full rat hippocampal study detects increased total caspase-3 after repeated ethanol exposure but no detectable cleaved caspase-3. The second donor PMID:30926569 reports ethanol-modulated caspase-3 expression in rat kidney/liver. A response term includes enzyme-production/expression changes, so retain the contextual response without claiming activation in the hippocampal experiment. Do not relabel the first study as evidence that CASP3 executes the observed neurodegeneration; the authors instead discuss nonapoptotic pathways.
- Row 76 (zero-based), GO:0051384 response to glucocorticoid: KEEP_AS_NON_CORE; primary PMID:18288275. Provenance trace: GO_REF:0000107 via UniProtKB:P55213|ensembl:ENSRNOP00000014096. The full donor study measures thymic caspase-3 immunostaining and apoptotic index after dexamethasone treatment in rats with severe pancreatitis. Retain this contextual glucocorticoid response as a comparative non-core claim. Its caspase-3 measurement is protein abundance rather than a purified activity or CASP3-specific perturbation assay, and it does not establish direct glucocorticoid-receptor binding or universal steroid responses.
- Row 77 (zero-based), GO:0071887 leukocyte apoptotic process: KEEP_AS_NON_CORE; primary PMID:26861981. Provenance trace: GO_REF:0000107 via UniProtKB:P55213|ensembl:ENSRNOP00000014096. The traced donor study uses the rat LT12 acute myeloid leukemia line and photodynamic therapy, with apoptosis measurements and sequential cleavage of effector caspases/PARP. The activated executioner contributes directly to leukocyte-lineage cell apoptosis; retain that conserved contextual process as non-core. This does not prove the same photosensitizer response in every primary leukocyte or a universal requirement for CASP3 rather than CASP7.
- Row 78 (zero-based), GO:0072347 response to anesthetic: KEEP_AS_NON_CORE; primary PMID:27498600. Provenance trace: GO_REF:0000107 via UniProtKB:P55213|ensembl:ENSRNOP00000014096. The neonatal-rat source exposes pups to sevoflurane and measures cleaved caspase-3 immunohistochemically alongside neuronal apoptosis, with CAPE as the intervention. Retain the comparative stress-execution response to this anesthetic as non-core. The result is not anesthetic sensing, a claim that all anesthetics are neurotoxic, or direct evidence in human infants.
- Row 79 (zero-based), GO:0098693 regulation of synaptic vesicle cycle: KEEP_AS_NON_CORE; primary PMID:33303681. Provenance trace: GO_REF:0000107 via UniProtKB:P70677|ensembl:ENSMUSP00000147767. This transfer traces to native mouse hippocampal experiments in PMID:33303681. Full text tests caspase inhibition/activation, autophagic flux and activity-induced vesicle-pool depletion/recovery. Retain the conserved nonapoptotic modulation as non-core, without making CASP3 a structural vesicle protein or assuming that every synapse uses this regulatory route. Pharmacological pathway measurements do not establish an exclusive CASP3 substrate mechanism in human terminals.
- Row 81 (zero-based), GO:0098978 glutamatergic synapse: KEEP_AS_NON_CORE; primary PMID:21151119. Provenance trace: GO_REF:0000107 via UniProtKB:P70677|ensembl:ENSMUSP00000147767. This cellular-component transfer traces to mouse hippocampal spines in PMID:21151119, where local caspase-3 activity, calcineurin and AMPA-receptor changes accompany altered glutamatergic transmission. Retain a comparative non-core synaptic pool, not a claim that all CASP3 resides at glutamatergic synapses or that it is a neurotransmitter receptor. The source is a mouse model, not a direct human localization assay.
- Row 83 (zero-based), GO:1990418 response to insulin-like growth factor stimulus: KEEP_AS_NON_CORE; primary PMID:33574912. Provenance trace: GO_REF:0000107 via UniProtKB:P55213|ensembl:ENSRNOP00000014096. The full donor study administers IGF-1 to aged splenectomized rats and detects hippocampal caspase-3 expression changes. Response-to-stimulus terms include changes in enzyme production/gene expression, so retain this contextual expression response as non-core. It does not demonstrate that CASP3 is an IGF receptor, directly transduces IGF1 signaling, or mediates the observed behavioral rescue.
