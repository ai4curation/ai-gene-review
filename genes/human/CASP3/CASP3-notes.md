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
