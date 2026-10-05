# STAT5A (P42229) curation notes

Human STAT5A, "Signal transducer and activator of transcription 5A", HGNC:11366,
gene ID 6776, chromosome 17q11.2. 794 aa. STAT family transcription factor;
close paralog of STAT5B (~94% identity). Reviewed alongside the existing
`genes/human/STAT5B/STAT5B-ai-review.yaml` for consistency, but graded on STAT5A
evidence.

## Core biology (synthesis)

STAT5A is a latent cytoplasmic, cytokine/hormone-activated, sequence-specific
RNA polymerase II transcription factor. Domain architecture (UniProt + InterPro):
N-terminal oligomerization domain, coiled-coil domain, p53-like DNA-binding
domain (IPR035858 STAT5a/5b DBD), linker, SH2 domain (589-686), C-terminal
transactivation domain. It binds gamma-activated-sequence (GAS) elements
(TTCN3GAA).

Activation cycle: cytokine/hormone binds its receptor -> receptor-associated JAK
kinases phosphorylate receptor tyrosines -> STAT5A SH2 docks and is
phosphorylated at **Tyr-694** -> reciprocal SH2-phosphotyrosine interactions form
a parallel dimer (and N-terminal-mediated tetramers) -> nuclear translocation ->
GAS-element binding -> transcriptional regulation with cofactors (NCOA1/SRC-1,
CBP/p300); terminated by SOCS/CIS and phosphatases.

- UniProt FUNCTION: "Carries out a dual function: signal transduction and
  activation of transcription... Binds to the GAS element and activates
  PRL-induced transcription. Regulates the expression of milk proteins during
  lactation." [ECO:0000269|PubMed:15534001]
- UniProt PTM: "Tyrosine phosphorylation is required for DNA-binding activity and
  dimerization. Serine phosphorylation is also required for maximal
  transcriptional activity."
- [PMID:8631883 "human Stat5 activation is also dependent on Tyr-694 in Stat5A and Tyr-699 in Stat5B, indicating that these tyrosines are required for dimerization"]

Deep research (falcon) highest-confidence annotation: "STAT5A is a
receptor-activated DNA-binding transcription factor that mediates cytokine and
hormone signals, principally through Tyr694 phosphorylation, SH2-dependent
dimerization, nuclear accumulation and GAS-element-dependent transcription." The
prolactin-PRLR-JAK2 axis in mammary epithelium is its clearest relatively
non-redundant context.

## Localization

- Cytoplasm (latent) and nucleus (after phosphorylation).
- UniProt SUBCELLULAR LOCATION: "Cytoplasm... Nucleus... Note=Translocated into
  the nucleus in response to phosphorylation." [ECO:0000269|PubMed:15534001]
- EXP nucleus + cytoplasm from PMID:15534001; HPA IDA cytosol/nucleoplasm;
  IBA is_active_in nucleus and cytoplasm.

## Upstream activators (each an IDA/experimental cytokine context; non-core)

All are contexts of the same core Tyr694/SH2/GAS mechanism.

- IL-2: [PMID:7719937 "the principal IL-2-inducible component... designated hStat5"];
  [PMID:8631883 "both Stat5A and Stat5B are activated by interleukin-2 (IL-2)"];
  [PMID:8580378 "STAT5 was found to be the predominant STAT transcription factor used by IL-2 in human T cells"].
- IL-15 (and IL-2): [PMID:7568001 "IL-2 and IL-15 rapidly induced the tyrosine phosphorylation of STAT3 and STAT5"].
- IL-7 / TSLP: [PMID:20974963 "the role of JAK1 and JAK2 in TSLP-mediated STAT5 phosphorylation... in contrast to the known activation of JAK1 and JAK3 by the related cytokine, IL-7"].
- IL-9: [PMID:10919676 "STAT5 is an important mediator of IL-9-driven proliferation"].
- IL-3 (basophils, FcERI): [PMID:22102340 "STAT5 in human basophils is activated through both the IL-3 and the FcepsilonRI signaling pathway"].
- IL-4 (CD8+ T cells): [PMID:17200144 "IL-4 induces the Jak3-mediated phosphorylation and nuclear migration of STAT1, STAT3, and STAT5"].
- IL-5 / eosinophils: [PMID:12393707 "STAT5 plays a critical role in eosinophil differentiation of primary human hematopoietic cells"] (STAT5a specifically).
- Thrombopoietin / Mpl: [PMID:9122198 "unlike STAT3, STAT5 is partially phosphorylated in the absence of any tyrosine residues in the Mpl cytoplasmic domain"].
- Prolactin / PRLR: [PMID:9516478 "Stat5 is specifically activated by PRL treatment, demonstrating that Stat5 is a physiological substrate downstream of PRLR"];
  [PMID:20075866 "PIKE-A directly associates with both signal transducer and activator of transcription 5a (STAT5a) and prolactin (PRL) receptor, which is essential for PRL-provoked STAT5a activation"].
- ERBB4/HER4 (nuclear chaperone, milk-gene expression): [PMID:15534001 "ERBB4 localizes to the nuclei of secretory epithelium while regulating activities of the signal transducer and activator of transcription (STAT) 5A transcription factor essential for milk-gene expression"; "both proteins bind to the endogenous beta-casein promoter"].

## Target genes / DNA binding examples

- BCL6 repression: [PMID:16819511 "STAT5 can bind inducibly and regulate transcription at one of these regions, identifying BCL6 as a STAT5 target gene"]. Note: this IPI-with-BCL6 "protein binding" annotation actually describes DNA-binding to the BCL6 gene, not a STAT5A-BCL6 protein complex.
- beta-casein (CSN2) promoter (Reactome; ERBB4).

## Protein interactions (mostly generic protein binding, GO:0005515)

Per curation policy, bare GO:0005515 "protein binding" is uninformative and is
removed (the interaction may be real; removal is about term informativeness, not
truth). Partners in existing annotations:
- PTPN1/PTP-1B (P18031), phosphatase-substrate: [PMID:12237455 "IR-like motifs in Trk autophosphorylation domains, and STAT 5 phosphopeptides"] (STAT5 phosphopeptide bound by PTP-1B substrate-trapping mutant).
- BCL6 (P41182) via PMID:16819511 (see above; really DNA binding to BCL6 locus).
- AGAP2/PIKE-A (Q99490-2): PMID:20075866 (real, required for PRL->STAT5a activation).
- EGFR (P00533): MaMTH PMID:24658140; EGFR-network rewiring PMID:31980649 (HT).
- TCF12 (Q99081): HuRI interactome PMID:25416956 (HT binary).
- EBF4 (Q9BQW3): [PMID:35939714 "EBF4 binding to STAT3, STAT5, and MAP kinase 3"] - annotated as GO:0140297 DNA-binding transcription factor binding (informative, kept non-core).

## Notable / ambiguous annotations

- GO:0042301 phosphate ion binding (IEA from mouse Stat5b P42230): biologically
  this reflects the SH2 domain's recognition of phosphotyrosine, not free
  inorganic phosphate. MODIFY -> GO:0001784 phosphotyrosine residue binding
  (SH2-dependent; well supported by Tyr-694/dimerization mechanism, PMID:8631883).
- GO:0038026 reelin-mediated signaling pathway (IDA, PMID:29581031,
  acts_upstream_of_or_within): the cached publication (abstract only) is
  "IL-7-induced phosphorylation of the adaptor Crk-like and other targets" and
  concerns IL-7/CrkL/Stat5 in D1 cells; it does not mention reelin in the
  available text. Cannot verify the reelin link -> UNDECIDED (per enum: use when
  unable to access relevant publication content).
- GO:0019530 taurine metabolic process (ISS, acts_upstream_of_positive_effect,
  from mouse Stat5b): highly indirect narrow transfer -> MARK_AS_OVER_ANNOTATED
  (matches STAT5B treatment).
- GO:0040014 regulation of multicellular organism growth / GO:0060397 GH
  receptor signaling: predominantly a STAT5B (GH/IGF1) function; for STAT5A these
  are transferred/shared -> KEEP_AS_NON_CORE.
- GO:0001938 pos. reg. endothelial cell proliferation + GO:0043536 pos. reg.
  blood vessel endothelial cell migration (IMP, PMID:20489169, miR-222 targets
  STAT5A): experimental but context-specific (neovascularization) -> KEEP_AS_NON_CORE.
- GO:2000329 negative regulation of Th17 lineage commitment (IDA PMID:20696842,
  CD69/Jak3/Stat5): experimental, specific immune context -> KEEP_AS_NON_CORE.

## Retracted paper (do not cite as support)

- PMID:11773439 (TC-PTP/PTPN2 negative regulation of PRL signaling) was RETRACTED
  (PMID:24319783). Not present in existing_annotations; not used.

## Action-policy reminders applied

- GO:0005515 protein binding: REMOVE (never MARK_AS_OVER_ANNOTATED). Interaction
  reality is not disputed; the term is uninformative.
- Experimental (IDA/IMP) cytokine-context annotations kept (as non-core), not
  removed on abstract-only grounds.
- IBA rows treated as PAINT/IBD phylogenetic judgments (STAT5A within the STAT
  clade); accepted at appropriate specificity.

## Review completion (2026-09-26)

All 117 GOA annotations reviewed and the review file set to `status: COMPLETE`.
All supporting_text quotes were verified as (whitespace-normalized) verbatim
substrings of the cached publications before writing. Validation passes with 0
errors and 0 warnings (`uv run ai-gene-review validate --verbose --terms`).

Action breakdown: KEEP_AS_NON_CORE 74, ACCEPT 25, MODIFY 10, REMOVE 6,
MARK_AS_OVER_ANNOTATED 1, UNDECIDED 1.

Key decisions:
- Core MF terms (GO:0000981, GO:0000978, GO:0001228) and JAK-STAT/cytokine
  process terms (GO:0007259, GO:0019221, GO:0045944, GO:0090575) ACCEPTed.
- GO:0003700 (general DNA-binding TF activity) rows all MODIFY -> GO:0000981
  (RNA Pol II-specific), matching STAT5B.
- GO:0005515 protein binding (6 rows) all REMOVE (uninformative), never
  MARK_AS_OVER_ANNOTATED. Note GO:0005515/PMID:16819511 (BCL6) really reflects
  DNA binding to the BCL6 locus, captured by DNA-binding TF activity terms.
- GO:0042301 phosphate ion binding MODIFY -> GO:0001784 phosphotyrosine residue
  binding (SH2 mechanism; GO:0001784 verified MF via QuickGO).
- GO:0038026 reelin signaling UNDECIDED (cached PMID:29581031 is abstract-only,
  about IL-7/CrkL, does not mention reelin).
- GO:0019530 taurine metabolic process MARK_AS_OVER_ANNOTATED (indirect ISS).
- Cytokine-context IDA rows (IL-2/3/4/5/7/9/15, TPO) and HPA sub-compartment
  IDA localizations (nucleoplasm/cytosol) KEEP_AS_NON_CORE; Reactome TAS
  localizations KEEP_AS_NON_CORE as pathway-specific duplicates.
- Two core_functions authored: (1) GAS-element RNA Pol II transcription factor
  activity (GO:0000981); (2) phosphotyrosine-dependent SH2 signal transduction
  (GO:0001784). Deep-research (falcon) cited in core_functions supported_by.
</content>
