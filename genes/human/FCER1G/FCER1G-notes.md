# FCER1G (FcRgamma, P30273) review notes

## Session 2026-10-05

### Sources
- UniProt P30273 (`FCER1G-uniprot.txt`)
- GOA: 76 annotations (28 are Reactome TAS plasma membrane rows)
- Cached publications: GOA-cited PMIDs plus additionally fetched PMID:8611682, 8313472,
  18776906, 17050534, 19098920, 23395392
- Deep research: `just deep-research-falcon human FCER1G` was launched in parallel (see status below)

### Gene summary
- 86-aa single-pass type I TM adaptor; extracellular region only ~5 residues; cytoplasmic ITAM (54-82),
  ITAM tyrosines Y65/Y76 [file:human/FCER1G/FCER1G-uniprot.txt "Adapter protein containing an immunoreceptor tyrosine-based activation motif (ITAM) that transduces activation signals from various immunoreceptors"]
- FcepsilonRI = alpha + beta + two disulfide-linked gamma chains [PMID:1535625 "The high affinity IgE receptor (Fc epsilon RI) is a tetrameric hetero-oligomer composed of an alpha chain, a beta chain, and two disulfide-linked gamma chains."]
- Homodimer or CD247 heterodimer assembles with CD16A [PMID:28652325 "The observation that CD16A associates equally well with human CD247 and FcεR1γ homodimers, as well as the heterodimer"]
- Needed for surface expression and signaling of human FcgammaRI but not IgG binding [PMID:8611682 "suggesting FcR gamma-chain not to be critical for hFc gamma RI ligand-binding capacity"; "This documents the FcR gamma-chain to be indispensable for both surface membrane expression and function of human Fc gamma RI in vivo."]
- KO mice: loss of phagocytosis, ADCC, mast cell allergic responses [PMID:8313472 "Defects in NK cell-mediated antibody-dependent cytotoxicity and mast cell-mediated allergic responses are evident in these animals"]
- Phospho-ITAM binds SYK tandem SH2 domains with nM affinity [PMID:8810294 "high affinity binding requires both tyrosine residues to be phosphorylated"]
- GPVI collagen receptor in platelets [PMID:9280292 "GPVI couples collagen-stimulation of platelets to phosphorylation of the Fc receptor gamma-chain leading to activation of Syk and phospholipase Cgamma2"]
- C-type lectins: Dectin-2 [PMID:17050534 "dectin-2 is a PRR for fungi that employs signaling through FcRgamma to induce innate immune responses"], Mincle [PMID:18776906 "Mincle selectively associated with the Fc receptor common gamma-chain"]
- IL-3R beta chain in basophils (mouse) [PMID:19098920 "FcRgamma associated constitutively with the common beta-chain of the IL-3 receptor and signaled by recruiting the kinase Syk."]
- CD36 internalization (mouse) [PMID:23395392 "By coupling to FcRgamma, CD36 is able to engage Src-family kinases and Syk"]
- IgSF receptors: ILT7/LILRA4 [PMID:16735691], CD300c [PMID:20959446], CD300d [PMID:22291008], TARM1 [PMID:26311901]

### Curation decisions (key points)
- IgE binding / IgG binding (IEA from mouse): REMOVE. Gamma chain does not bind Ig; ligand binding is by alpha chains (PMID:8611682).
- transmembrane signaling receptor activity (InterPro IEA): MODIFY -> protein-macromolecule adaptor activity (GO:0030674), matching the convention used for TYROBP and CD247.
- protein binding IPIs: MODIFY -> signaling receptor binding (GO:0005102) for receptor partners (ILT7, CD300c, CD300d, TARM1, CD64); MODIFY -> SH2 domain binding (GO:0042169) for SYK (PMID:8810294); REMOVE for PMID:9280292 (SYK listed as partner but abstract only supports GPVI co-association/phosphorylation).
- Fc-epsilon receptor signaling IMP (PMID:16735691): full text is about ILT7-FcRgamma in pDCs, not FcepsilonRI -> MODIFY to GO:0002429. The IBA to the same term is accepted (term correct for the gene). This produces a consistent-action warning in validation, which is deliberate.
- serotonin secretion by platelet: MARK_AS_OVER_ANNOTATED (distal to receptor-proximal role).
- NEW: GO:0002223 stimulatory C-type lectin receptor signaling pathway (comparator check: TYROBP has it by IDA, SYK has it); GO:0033000 Fc-gamma receptor I complex (definition explicitly names the FcepsilonRI gamma chain dimer); GO:0038065 collagen-activated signaling pathway (GP6 carries it).

### Deep research status
- Falcon deep research was launched in parallel; see final section for outcome.
- Falcon deep research SUCCEEDED (`FCER1G-deep-research-falcon.md`, ~27 min). Consistent with the review:
  FcRgamma is a ligand-free receptor-assembly/ITAM adaptor [file:human/FCER1G/FCER1G-deep-research-falcon.md "Its partner receptor recognizes the extracellular ligand."];
  notes that human adaptive NK cells can use CD247 instead of FcRgamma for CD16A signaling, so mouse KO ADCC phenotypes do not fully transfer to human.
