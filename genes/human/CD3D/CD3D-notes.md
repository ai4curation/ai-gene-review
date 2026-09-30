# CD3D (human, P04234) review notes

Part of the ADAPTIVE_IMMUNITY project, T cell receptor trunk (CD3D, CD3E, CD3G, LCK, ZAP70, LAT, LCP2, PLCG1, NFATC1).

## Session 2026-09-30

### Setup
- `just deep-research-falcon human CD3D --fallback perplexity-lite` FAILED: falcon timed out (600s) and the perplexity-lite fallback errored ("Provider 'perplexity' not available. Available: falcon, asta, openscientist"). No deep-research file exists; the review is based on UniProt, cached publications, Reactome and QuickGO. Re-run deep research later and reconcile.
- `just fetch-gene-pmids human CD3D`: 9/9 GOA PMIDs cached. Only PMID:11390434 and PMID:32296183 have full text; the rest are abstract-only.

### Biology summary
- Single-pass type I membrane protein; extracellular Ig-like domain, TM helix, cytoplasmic tail with one ITAM (Pfam PF02189; InterPro IPR003110). PANTHER PTHR10570:SF5 (CD3 gamma/delta family) (UniProt P04234).
- Assembly: CD3 delta-epsilon dimer pairs with TCR alpha in the ER [PMID:9485181 "The TCR/CD3 complex is assembled after a series of pairwise interactions involving the formation of dimers of CD3 epsilon with either CD3 gamma or CD3 delta."].
- Structure: [PMID:31461748 "The octameric TCR-CD3 complex is assembled with 1:1:1:1 stoichiometry of TCRαβ:CD3γε:CD3δε:CD3ζζ."]; ECD packs against TCR constant domains; TM barrel.
- Signaling: one ITAM per CD3 chain phosphorylated by LCK [Reactome:R-HSA-202165 "the TCR complex include 10 ITAMs with one ITAM in each of the CD3 chains including the three tandem ITAMs in each zeta chains."].
- Ubiquitinated after TCR activation [PMID:1323144 "at least one other TCR subunit, CD3 delta, was also ubiquitinated after activation of the receptor."].
- Disease: IMD19, T-B+NK+ SCID (UniProt).
- UniProt also notes interaction with CD4/CD8 coreceptors (PMID:12215456, not cached; not used).

### Decisions
- Core MF: GO:0004888 transmembrane signaling receptor activity (IBA/IC/IEA accepted), understood as exerted within the complex. Considered whether contributes_to would be more accurate; raised as a suggested question rather than altering.
- NEW MF: GO:0030159 signaling receptor complex adaptor activity (structural role in TCR-CD3 assembly). Participation test: CD3 delta supplies structure the assembly depends on. Comparator: CD3E (NAS, PMID:9886373) and CD3G (NAS, PMID:12794121) already carry GO:0030159 in human GOA (QuickGO query 2026-09-30).
- Core CC: GO:0042105 alpha-beta T cell receptor complex; plasma membrane.
- Core BP: GO:0050852 T cell receptor signaling pathway.
- Protein binding IPI (SGTB, HuRI Y2H) -> REMOVE (uninformative).
- Identical protein binding (in vitro oligomerization of isolated cytoplasmic domain, PMID:14967045) -> MARK_AS_OVER_ANNOTATED; one CD3 delta per complex in cryo-EM.
- MHC class II receptor activity (contributes_to, IDA PMID:1323144; abstract about ubiquitination) -> KEEP_AS_NON_CORE, deferring to curator; MHC-class restriction is not a CD3D property.
- Positive thymic T cell selection (IBA/IEA/ISS from mouse Cd3d) -> KEEP_AS_NON_CORE: TCR-CD3 signaling does the work of selection, so this is participation, but it is a developmental outcome and part of the knockout phenotype is loss of receptor assembly.
- Alpha-beta T cell activation, adaptive immune response, immune system process -> KEEP_AS_NON_CORE (broad/downstream).
- Clathrin-coated endocytic vesicle membrane (Reactome TAS) -> KEEP_AS_NON_CORE (CD3D is cargo).
- Cytoplasm NAS (fetal liver precursor cells with intracellular CD3 delta) -> KEEP_AS_NON_CORE (secretory-pathway pool of a membrane protein).

### Validation
- `just validate human CD3D`: valid, no errors or warnings. All 49 supporting_text quotes checked verbatim against cached publications/Reactome.
