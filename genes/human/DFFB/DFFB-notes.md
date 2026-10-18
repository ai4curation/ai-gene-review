# DFFB notes

## 2026-09-30

DFFB is the catalytic DFF40/CAD subunit of DNA fragmentation factor, complementary to
DFFA/ICAD. DFFA folds and inhibits DFFB; executioner-caspase cleavage of DFFA releases
DFFB to form the active nuclease that cleaves apoptotic chromatin DNA
[PMID:9108473 DFF, a heterodimeric protein that functions downstream of caspase-3 to
trigger DNA fragmentation during apoptosis., "purified from HeLa cytosol"; PMID:9671700
The 40-kDa subunit of DNA fragmentation factor induces DNA fragmentation and chromatin
condensation during apoptosis., "Purified DFF40 exhibited an intrinsic DNase"].

The direct molecular function is DNA endonuclease activity. Existing broader activity
rows for nuclease, DNA nuclease, and hydrolase activity are biologically true but should
be narrowed to `GO:0004520 DNA endonuclease activity`, and the top-level apoptosis/CIDE-N
row should be narrowed to `GO:0006309 apoptotic DNA fragmentation`
[PMID:9689044 Molecular cloning and characterization of human caspase-activated DNase.,
"CAD is responsible for the apoptotic DNA degradation"].

Small-scale annotations to chromatin, nucleus, nucleoplasm, cytosol, apoptotic DNA
fragmentation, and apoptotic chromosome condensation all fit the model. DFFB binds DNA
through the DFF40/CAD nuclease subunit before nuclease release [PMID:15572351 Interaction
of DNA fragmentation factor (DFF) with DNA reveals an unprecedented mechanism for
nuclease inhibition and suggests that DFF can be activated in a DNA-bound state., "DNA
binding by DFF is mediated by the"]. A cytosolic DFF40/CAD pool can control whether
cells execute apoptotic oligonucleosomal DNA laddering [PMID:22253444 Apoptotic DNA
degradation into oligonucleosomal fragments, but not apoptotic nuclear morphology,
relies on a cytosolic pool of DFF40/CAD endonuclease., "DFF40/CAD protein can be detected
in both the cytosolic and the nuclear subcellular compartments"].

The `GO:1902511 negative regulation of apoptotic DNA fragmentation` row belongs on DFFA,
not DFFB. DFFB is the inhibited nuclease in the inactive DFF40:DFF45 complex; DFFA is the
inhibitor/chaperone subunit [PMID:11371636 Solution structure of DFF40 and DFF45
N-terminal domain complex and mutual chaperone activity of DFF40 and DFF45., "which also
acts as a nuclease inhibitor before DFF40 activation"].

Generic `protein binding` rows to DFFA, including high-throughput HuRI, BioPlex, and Cell
Map recoveries of the known DFFA-DFFB edge, do not add molecular-function information
beyond DFF complex membership and the CAD nuclease model. The TOP2A interaction is kept
as secondary enzyme binding because it is a focused apoptotic-chromatin-condensation
observation rather than a blind screen [PMID:10959840 DNA topoisomerase IIalpha interacts
with CAD nuclease and is involved in chromatin condensation during apoptotic execution.,
"CAD binds to Topo IIalpha"].
