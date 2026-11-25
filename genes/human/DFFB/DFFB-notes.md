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

## 2026-10-26: comparative execution-phase source audit

All45 existing rows were reviewed. Direct DNA endonuclease activity and apoptotic DNA fragmentation remain the core. Stable DFF complex membership is retained as core, and the broad cytoplasmic term is refined to cytosol.

Normal force fetch recovered full PMID:11371636. Its experiments show DFF40 folds the DFF45 N-terminal domain, after which DFF45 assists DFF40 folding. The prior categorical REMOVE of negative regulation of apoptotic DNA fragmentation therefore overstated a simple nuclease-versus-inhibitor division: DFF40 does structural work in maturation of its inhibitor. The exact negative-regulation process contribution remains UNDECIDED; this does not assign direct ICAD inhibition to CAD or reject the established nuclease activity.

PMID:10959840 reports that CAD association enhances TOP2A decatenation in vitro. The enzyme-binding row is refined to enzyme activator activity (live QuickGO GO:0008047), with explicit contextual scope. This capacity is not promoted to a second core mechanism and does not establish that all CAD-associated condensation proceeds by TOP2A activation. Condensation remains an experimental process assertion, including its independent/parallel routes; it is not mechanically paired with a nuclease MF in a separate core. The structural paper reports regulatory-domain oligomerization, not an unqualified physiological dimer stoichiometry.

The normal Falcon research request with Perplexity-lite fallback was attempted for this gene. Falcon authentication and fallback quota checks failed; no provider report was fabricated. Normal publication caching completed independently. This manual primary-source audit is the research record.

Review/annotation-reviewer workflows were applied, with independent annotation-reviewer consultation on claim consistency and the distinctions among Acinus condensation, ICAD folding/inhibition, and AIF death pathways. Row count: 45; actions: ACCEPT=27, KEEP_AS_NON_CORE=3, MODIFY=9, REMOVE=5, UNDECIDED=1. No imported annotation payload was edited and no new row was added in this session.
