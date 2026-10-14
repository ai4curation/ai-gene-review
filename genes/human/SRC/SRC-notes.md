# SRC (human, P12931) review notes

Automated deep research was unavailable for this gene (no deep-research provider
keys in this environment). These notes were compiled manually from the UniProt
record, the cached publications in `publications/`, QuickGO, the GO-CAM index and
the GOA file. No `*-deep-research-*.md` file was created.

## Identity and regulation

- 536 aa; N-terminal myristoylated SH4/unique region, SH3, SH2, tyrosine kinase
  domain, C-terminal tail (UniProt). Catalytic activity EC 2.7.10.2 (UniProt,
  many IDA/EXP sources).
- Tail phosphorylation by CSK (Tyr530) and SH2-tail / SH3-linker clamps hold
  SRC inactive; activation-loop autophosphorylation (Tyr419) activates it
  [PMID:17921256 "Cytosolic c-Src is often self-restrained to an inactive conformation by both intramolecular and intermolecular interactions between its SH2 domain and phospho-Y527 and between its SH3 domain and SH2-kinase linker domains."].
- Tail dephosphorylation by PTPRA uses SH2 displacement
  [PMID:10698938 "We suggest that pTyr789 enables pTyr527 dephosphorylation by a pilot binding with the Src SH2 domain that displaces the intramolecular pTyr527-SH2 binding."].
- Autophosphorylation as a regulated step
  [PMID:17491594 "Binding of c-Src to the AF-6 PDZ domain interferes with phosphorylation of c-Src at Tyr527 by the C-terminal kinase, and reduces c-Src autophosphorylation at Tyr416, resulting in a moderately activated c-Src kinase."].
  Proposed as NEW `GO:0046777` protein autophosphorylation (comparator: LYN has
  it by IDA; LCK and FYN do not, so no convention against it).

## Binding modes (basis for protein-binding MODIFYs)

- SH2 to phosphotyrosine: PYK2 Tyr402
  [PMID:8849729 "Moreover, tyrosine phosphorylation of Pyk2 leads to binding of the SH2 domain of Src to tyrosine 402 of Pyk2 and activation of Src."];
  ERalpha pTyr537 [PMID:14963108 "ER interacts with Src's SH2 domain using phosphotyrosine 537, and this complex was further stabilized by MNAR-ER interaction."];
  PECAM-1 [PMID:9162084 "This association appears to be mediated by Src-SH2 domain, because PECAM-1 can be precipitated by a GST-Src-SH2 affinity matrix."];
  MVP [PMID:16441665 "We found MVP as a Src-SH2 binding protein in human stomach tissue."].
- SH3 to proline-rich motifs: CBL
  [PMID:17094785 "We previously showed that the primary interaction between Src and Cbl is mediated by the Src homology domain 3 (SH3) of Src binding to proline-rich sequences of Cbl."];
  p140Cap [PMID:17525734 "indicating that p140Cap and Src directly interact through the binding of the Src SH3 domain with the most carboxy-terminal proline-rich region of p140Cap"];
  integrin beta3 [PMID:16115959 "One exception is in platelets, in which a constitutive association between integrin αIIbβ3 and c-Src is mediated by direct interaction of the β3 cytoplasmic domain with the c-Src SH3 domain"];
  Kv1.5 [PMID:8953041 "This interaction was mediated by the proline-rich motif of hKv1.5 and the SH3 domain of Src."].
- C-terminal PDZ-binding motif: [PMID:17491594 "We describe the C-terminus of c-Src as a ligand for a PDZ (postsynaptic density 95, PSD-95; discs large, Dlg; zonula occludens-1, ZO-1) domain."];
  [PMID:17936276 "We demonstrate that the interaction of c-Src with LNX1 depends on the C-terminal PDZ ligand of c-Src."].
  The 21 PDZ-protein rows from the fragmentomics screen (PMID:36115835) were
  modified to PDZ domain binding on this basis.

## Sites of action

- Endosomes to focal adhesions on activation
  [PMID:7525268 "Mutation of this tyrosine dramatically redistributes c-Src from endosomal membranes to focal adhesions."].
- Focal adhesion turnover with FAK and dynamin-2
  [PMID:21411625 "This Src-FAK-Dyn2 trimeric complex is essential for FA turnover, as mutants disrupting the formation of this complex inhibit FA disassembly."]
  (basis for MODIFY of focal adhesion assembly to focal adhesion disassembly).
- Mitochondrial pool [PMID:12615910 "Here, we show that c-Src is also present within mitochondria, where it phosphorylates cytochrome c oxidase (Cox)."].
- Integrin-beta5 signalling [PMID:24036928 "In addition, the integrity of actin fibers and Src kinase activity contribute to integrin-β5-mediated signaling and VSF formation."].

## GO-CAM models containing SRC (gocams/index.tsv)

All five models use SRC as an enabler of protein tyrosine kinase (or protein
kinase) activity:
- 645d887900001502 Src-ZNRF1 axis controls TLR3 trafficking: GO:0004713 ->
  regulation of TLR3 signaling pathway, cytoplasm (PMID:37158982).
- 646ff70100004025 mTORC1 via OTUB1 deubiquitination of RPTOR: GO:0004713 ->
  positive regulation of TORC1 signaling (PMID:35927303).
- 66c7d41500000715 CLEC12A inhibits neutrophil activation: GO:0004713 ->
  negative regulation of neutrophil activation (PMID:34234773).
- 6870555700001571 laminin/dystroglycan Rac1 signalling: GO:0004713 ->
  positive regulation of Rac protein signal transduction.
- 68d5ebd600001504 KISS1/KISS1R and osteoclasts: GO:0004672 -> osteoclast
  differentiation, cytoplasm.
These are consistent with the core kinase function; the corresponding process
rows were kept as non-core context-specific roles.

## Premetazoan evidence: ancestral versus animal-specific

- Choanoflagellates have an expanded tyrosine kinase / SH2 / PTP repertoire
  [PMID:18273011 "possesses a surprising abundance of tyrosine kinases and their downstream signalling targets."].
- Src and Csk regulation exist in Monosiga ovata, but unicellular Src stays
  partly active after Csk phosphorylation
  [PMID:16873552 "we show that the src gene family and its C-terminal Src kinase (Csk)-mediated regulatory system already were established in the unicellular M. ovata"];
  [PMID:16873552 "It can be phosphorylated by Csk at the negative regulatory site but still exhibits substantial activity even in the phosphorylated form."].
- M. brevicollis Src1 has mammalian-like domain functions, but SH2 and
  catalytic domains are not coupled, and MbCsk tail phosphorylation does not
  shut it down
  [PMID:18390552 "The kinase has the same domain arrangement as mammalian Src kinases, and we find that the individual Src homology 3 (SH3), SH2, and catalytic domains have similar functions to their mammalian counterparts."];
  [PMID:18390552 "In contrast to mammalian c-Src, the SH2 and catalytic domains of MbSrc1 do not appear to be functionally coupled."];
  [PMID:18390552 "MbSrc1 phosphorylated a peptide modeled on the Tyr-419 autophosphorylation sequence of mammalian Src, suggesting that MbSrc1 might also be capable of autophosphorylation."].
- Disputed: a later yeast/in vitro study (abstract only read) reports Csk
  inhibition of Src in Capsaspora and M. brevicollis
  [PMID:28939764 "Our results suggest that negative regulation of Src by Csk is more ancient than previously thought and that it might be conserved across all holozoan species."].
  This is the same dispute recorded in the human CSK review
  (genes/human/CSK/); SRC is kept consistent with it: tail phosphorylation by
  Csk is ancestral, strong inhibition outside animals is disputed.
- Capsaspora phosphoproteome changes across life stages include tyrosine
  kinases (abstract only)
  [PMID:27746046 "they affect key genes involved in animal multicellularity, such as transcription factors and tyrosine kinases."].
  No Src-specific substrate data were found in the cached text.

Summary:
- **Ancestral (in choanoflagellates):** non-receptor tyrosine kinase activity;
  SH3, SH2 and kinase domain architecture with SH2 phosphopeptide and SH3
  binding; C-terminal tail phosphorylation by Csk; probable activation-loop
  autophosphorylation.
- **Disputed:** whether Csk tail phosphorylation was strongly inhibitory
  before animals, and whether SH2 engagement was coupled to catalytic
  regulation.
- **Animal-specific on current evidence:** the substrate and partner network at
  focal adhesions (FAK/PYK2, p130Cas), adherens and gap junctions, PDZ scaffold
  interactions, and the receptor-specific pathways (RTK, cytokine, immune,
  osteoclast bone resorption, vascular permeability). No unicellular-relative
  study in the cache shows Src acting at adhesion structures.

## IBA nodes

- PTN002521528 (Src-family level): non-membrane spanning PTK activity,
  signaling receptor binding, cell differentiation.
- PTN002815154 (narrower node, seeded by rat/human Src): cell adhesion, EGFR
  signalling, progesterone receptor signalling, negative regulation of
  extrinsic and intrinsic apoptotic signalling. SRC itself is in the WITH/FROM
  for several of these, which reflects its own experimental grounding.
  None of these were removed; the broad differentiation/apoptosis ones are kept
  as non-core.

## Decision summary (550 GOA rows plus 1 NEW)

- Protein binding (186 rows): 62 MODIFY where the cited text defines the mode
  (phosphotyrosine residue binding, proline-rich region binding, PDZ domain
  binding, one receptor tyrosine kinase binding), 124 REMOVE.
- Kinase activity rows accepted; protein kinase activity rows modified to
  protein tyrosine kinase activity.
- Over-annotations: telomerase/transcription screen rows (PMID:21531765),
  vasodilation, heart rate, intestinal epithelial cell development (regeneration
  paper), TGF-beta receptor signalling (integrin arm only), positive regulation
  of dephosphorylation, signal complex assembly, PTK activator activity,
  phospholipase activator activity, positive regulation of phosphate metabolic
  process.
- REMOVE (non-PB): signaling receptor activator activity (ISS from rat; kinase
  effect mistyped as activator).
- UNDECIDED: SH2 domain binding (PMID:8070403; partner p130Cas lacks an SH2
  domain, abstract only).
