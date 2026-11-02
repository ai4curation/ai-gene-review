# Mst27D / Q8IPI4

Q8IPI4 is the 424-residue Mst27D product. [PMID:37428798](https://pubmed.ncbi.nlm.nih.gov/37428798/), DOI https://doi.org/10.1371/journal.pgen.1010837, uses Mst27D-PA and explicitly defines the C-terminal region as residues 151–424, consistent with the selected full-length model. Full text was inspected. It directly distinguishes intact Mst27D lattice binding from EB1 plus-end tracking, and native postmeiotic expression from premature expression caused by SV40-terminated transgenes. These are biological grounds to challenge specific EB1-derived IBA transfers rather than donor-count arguments. Nine original GOA rows are retained with one new bundling annotation. ProtNLM microtubule binding is CNN; a questionable finer GOA annotation is not used to force LSP.

## Sequence and research provenance

The selected frozen UniProt record is retained in [Mst27D-uniprot-source.json](Mst27D-uniprot-source.json), with the complete original prediction metadata in [Mst27D-predictions-source.json](Mst27D-predictions-source.json). It maps the exact accession to this FlyBase gene; current sequence identity does not establish the historical predictor input. Gene-level experiments support conserved functions unless a relevant isoform difference is established. Falcon research was requested with perplexity-lite fallback alongside publication caching. Primary publications and sequence observations, rather than AI summaries or ARBA assertions, support the curated conclusions.

## Completed provider readback

The wrapper timed out and its fallback reported insufficient quota, but the original Falcon job later produced a complete report. The report and primary sources were inspected; no duplicate provider submission was made. The report supports Nup358 linkage and lattice-wide binding. Its mention of meiotic spindle enrichment must be interpreted with the primary study’s explicit correction for premature expression from SV40-terminated constructs. The endogenous-terminator and antibody experiments establish native accumulation after meiosis.


## Full annotation re-review — 2026-09-20

Re-read all 10 annotation rows and the existing Falcon report against the full primary study PMID:37428798. Fetched and inspected PTHR10623 PAINT: the eight original IBA rows trace to eukaryotic PTN000065701. The primary paper supports native postmeiotic expression, direct microtubule binding/bundling and Nup358 recruitment. The existing NEW bundling term is retained on biochemical/cellular assembly evidence plus stage-resolved mutant/rescue data, not solely on a fertility phenotype.

Plus-end binding/location remain UNDECIDED pending focused adjudication: "Mst27D binds all along MTs, contrasting with Eb1’s preference for growing MT plus ends" demonstrates altered preference, whereas GO:0051010 requires binding and does not specify preference. The comet-forming construct was the isolated C-terminal region, not a protein lacking the C terminus; the authors discuss possible heterodimerization with endogenous EB-family proteins. MTOC localization is assessed separately from spindle midzone, because GO:0005815 includes nucleating/anchoring structures outside mitosis. Polymerization/depolymerization regulation remains unresolved because the demonstrated bundling mechanism does not by itself adjudicate dynamic regulation.

The spindle-assembly rejection remains supported by target-specific native timing ("endogenous Mst27D accumulation starts after meiosis in early spermatids") and null analysis ("Until after meiosis, abnormalities were not detectable."). Midzone remains cautiously over-annotated. This is a branch/context challenge, not an argument from sparse or distant donors.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

This review does not use any ProtNLM2 output. Sources: the full text of PMID:37428798 (PMC10359004), the existing Falcon report (which adds only a 2025 Nup43 bioRxiv preprint that uses Mst27D-mCherry as a marker), PTHR10623 PAINT, and a new domain/subfamily analysis (`Mst27D-bioinformatics/RESULTS.md`, `domain_architecture.py`).

### Identity
Q8IPI4 (unreviewed TrEMBL; FlyBase FBgn0051907, isoforms A/B) is the full-length 424-aa Mst27D product. The paper's Mst27D-PA defines the C-terminal region as residues 151-424, and the InterPro RP/EB match covers residues 19-365. The entry is not a fragment or an alternative gene model. No Swiss-Prot entry exists for Mst27D; Q4V4W2 is a cDNA-derived entry with the same length.

### Evolutionary placement
PANTHER v19 geneinfo assigns Mst27D to PTHR10623:SF6 ("EB1, ISOFORM F-RELATED"). The same subfamily holds every other fly PTHR10623 member (Eb1 A1Z6P3, CG18190/EB-SUN A1ZBF1, CG32371, CG2955, CG15306). Human MAPRE1 is in SF20, MAPRE2 in SF7 and MAPRE3 in SF10. SF6 is therefore a fly-lineage EB expansion, and Mst27D has no one-to-one ortholog in human or yeast. The nearest characterised relative is the paralog Eb1 (FBgn0027066), which is also an IBA donor. Mst27D lacks the EBH domain (IPR004953/PF03271) and the EEY/F tail; Eb1, CG18190 and MAPRE1 all keep both. All eight IBAs come from the eukaryote-wide node PTN000065701.

The PTHR10623 family review (interpro/panther/PTHR10623) does not assign subfamilies and leaves GO:0051010 UNRESOLVED. This review does not disagree with any subfamily placement. It goes further on GO:0051010 for Mst27D only, using the target data below.

### Changes relative to the previous review
- GO:0008017 microtubule binding (IEA): ACCEPT changed to MODIFY, replacement GO:0099609 microtubule lateral binding (is_a child, verified in OLS). Evidence: full-length Mst27D and the Mst27D_CH-Eb1_CT chimera bind "all along the MTs". The core MF is now GO:0099609.
- GO:0051010 plus-end binding and GO:0035371 plus-end: UNDECIDED changed to MARK_AS_OVER_ANNOTATED. The domain swap places the loss of plus-end preference in the Mst27D CH domain itself. Comets appear only with the isolated CT fragment, which has no microtubule-binding domain, and the authors attribute them to heterodimerization with endogenous Eb1. The EBH domain and EEY tail are absent.
- GO:0005815 MTOC: UNDECIDED changed to MARK_AS_OVER_ANNOTATED. The basal-body region is "largely devoid of Mst27D-EGFP", and the dense-complex bundle "did not seem to be nucleated by the centrosome/basal body".
- GO:0051233 spindle midzone: MARK_AS_OVER_ANNOTATED changed to REMOVE, matching spindle assembly. Native protein is made only after meiosis, and spermatids have no spindles. The meiotic spindle signal came from prematurely expressed SV40-terminator transgenes.
- GO:0031110: kept UNDECIDED. The canonical plus-end mechanism has diverged, but the authors propose a bundling-based stabilization of microtubules that nobody has tested. A TIRF reconstitution is listed in suggested_experiments.
- GO:0005881 and GO:0035372: ACCEPT. Nup358 recruitment to microtubules is supported in the target, through a divergent CT region that replaces the EBH domain.
- NEW (retained): GO:0001578 microtubule bundle formation. Gain of function in S2R+ cells, chimera bundling and the proposed dimer cross-linking mechanism mean Mst27D does part of the work, not only that it is necessary.
- NEW (added): GO:0007290 spermatid nucleus elongation (IMP). Mst27D is the structural NPC-to-microtubule linker on which the nucleus elongates. This is a cell-intrinsic organelle-shaping process, not an organismal phenotype.
- NEW (added): GO:0005635 nuclear envelope (IDA). Mst27D is restricted to the NPC-containing nuclear envelope, and its enrichment there depends on Nup358.
- Core functions are split into two: (1) lattice binding and bundling; (2) NPC-to-microtubule linkage for nuclear elongation. Status set to COMPLETE.

### Modules
No module under modules/ contains Mst27D. The related module is modules/dmel_nuclear_pore_complex.yaml, which contains its binding partner Nup358.
