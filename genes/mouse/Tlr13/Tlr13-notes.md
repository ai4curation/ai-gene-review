# Tlr13 (mouse, UniProt Q6R5N8, MGI:3045213) — curation notes

These notes come from the UniProt record, the GOA rows and the cached publications;
the Falcon deep-research report arrived after the review was written and is
cross-checked at the end of this file.
Unlike its Tlr11/Tlr12 neighbours, Tlr13 has no nomenclature ambiguity — the gene
symbol, the UniProt entry and the literature name all agree.

## Established biology

- Ligand. TLR13 recognises a short, conserved sequence of bacterial 23S ribosomal
  RNA: [PMID:22821982 "the orphan receptor TLR13 in mice recognizes a conserved 23S ribosomal RNA"]
  sequence that is the binding site of macrolide/lincosamide/streptogramin
  antibiotics. Methylation of that site, the mechanism of erythromycin resistance,
  abolishes recognition — 23S rRNA from resistant isolates and synthetic
  oligoribonucleotides carrying the modification [PMID:22821982 "failed"]
  [PMID:22821982 "to stimulate TLR13"]. Independently,
  [PMID:22896636 "Small interfering RNA against TLR13 reduced"] cytokine induction by
  bacterial RNA in dendritic cells, and the same study concludes that TLR13 is a
  receptor for bacterial RNA.
- Structure of recognition. The crystal structure of the ectodomain with a 13-nt
  single-stranded RNA shows sequence- and conformation-specific binding, and that
  [PMID:26323037 "The ssRNA induces TLR13 dimerization but assumes"] a stem-loop-like
  conformation quite unlike its conformation in the ribosome. The same work reports
  that [PMID:26323037 "a viral-derived 16-nt ssRNA"] predicted to adopt a similar
  fold also activates the receptor — which is the most concrete support for the
  earlier virus-related claim.
- Compartment and trafficking. It is an endosomal receptor. UniProt records
  "Endosome membrane" from PMID:22896636, and the UNC93B1 interaction was found by
  mass spectrometry of UNC93B immunoprecipitates:
  [PMID:17452530 "we identified TLR3, 7, 9, and 13 with extensive sequence coverage over the entire length of the proteins"].
- Signalling. [PMID:21131352 "MyD88- and TAK1-dependent TLR signaling pathway, inducing the activation of"]
  NF-kappa-B, with type I interferon induction through IRF7. The same paper reported
  a response to vesicular stomatitis virus; UniProt flags this as requiring further
  evidence, and the two 2012 papers plus the 2015 structure all converge on bacterial
  rRNA as the physiological ligand.
- Absence in human. UniProt notes that Tlr13 is not conserved in human and suggests
  a different human rRNA-sensing receptor may exist; chicken TLR21 is the
  phylogenetic neighbour that Keestra notes "displays similarity with mouse TLR13".

## Annotation decisions (summary)

- The ligand and pathway rows are the strongest part of the record and are accepted
  as-is: GO:0019843 rRNA binding (IDA, twice), GO:0034178 toll-like receptor 13
  signaling pathway (IDA, twice), GO:0045087 innate immune response (IDA, twice),
  GO:0002755 MyD88-dependent toll-like receptor signaling pathway (IGI with Myd88),
  GO:0005768 endosome and GO:0010008 endosome membrane.
- GO:0038023 (IBA) modified to GO:0038187 pattern recognition receptor activity: a
  defined PAMP is bound directly, with a structure of the complex.
- GO:0005886 plasma membrane (IBA) modified to GO:0010008 endosome membrane — the
  PAINT donors are surface TLRs and this receptor is endosomal.
- The two GO:0042802 identical protein binding rows are modified to GO:0042803
  protein homodimerization activity, which is what the structural and
  co-immunoprecipitation data show, and is informative.
- The two GO:0005515 protein binding rows record the UNC93B1 and MyD88 interactions.
  Both are modified rather than removed: UNC93B1 is a chaperone-like trafficking
  factor (GO:0051087 protein-folding chaperone binding), and the MyD88 interaction is
  TIR-domain-mediated (GO:0070976 TIR domain binding).
- GO:0009615 response to virus (IMP) is kept as non-core rather than accepted: the
  vesicular stomatitis virus result is the weakest claim in the record, is flagged by
  UniProt as needing further evidence, and the structural work supports only that a
  viral ssRNA of the right fold can activate the receptor.
- GO:0005737 cytoplasm (IDA) and GO:0043408 regulation of MAPK cascade (IGI with
  Map3k7) are kept as non-core: true but generic, and superseded by the endosome and
  MyD88-pathway annotations respectively.


## Deep-research cross-check (2026-09-30)

Compared `Tlr13-deep-research-falcon.md` against the finished review. Right gene, no naming
ambiguity, and it confirms the whole of the review's picture: sequence-specific recognition of a
short conserved 23S rRNA motif, endosomal site of action, absolute UNC93B1 dependence,
ligand-induced dimerisation, MyD88-dependent signalling to NF-kappa-B and MAP kinases, myeloid
expression, and absence from the human genome. This was also the report with the most genuinely
new content, because it covers a 2020-2025 literature the review had not seen.

Two threads were followed into primary papers.

**1. Host defence against Streptococcus pneumoniae — taken up as the review's only new
annotation.** `publications/PMID_32209688.md` (mBio 2020, full text):
[PMID:32209688 "Collectively, these data indicate that mice with single defects in TLR7, TLR9, or TLR13 have moderately impaired antipneumococcal defenses in the brain resulting in late-onset lethality"],
microglia lacking the receptor produce less CXCL1 and TNF, and
[PMID:32209688 "the simultaneous absence of TLR7, TLR9, and TLR13 was associated with extreme susceptibility to infection"]
because resident macrophages cannot recruit neutrophils. `publications/PMID_38358825.md`
(JCI Insight 2024, full text) adds double-knockout evidence:
[PMID:38358825 "TLR13 and TLR2 are major pneumococcal sensors in the subarachnoid space"], with
[PMID:38358825 "the concerted activity of cell-surface TLR2 and endosomal TLR13 as drivers of brain pathology in meningitis"].

Added as `NEW` GO:0050830 defense response to Gram-positive bacterium (IMP), and to
`core_functions.directly_involved_in`. The CLAUDE.md tests: participation is satisfied by the
receptor's own work, since it binds the 23S rRNA ligand directly (with a structure of the
complex) and that recognition is the step initiating chemokine output — this is not a bare
necessity argument. The comparator check settles the term choice: mouse Tlr2, the surface sensor
of the same bacterium and the partner in the double knockout, carries GO:0050830 by IMP from
three papers, so a sensing receptor conventionally takes it. Two caveats are recorded in the
row's reason: the Gram-positive child is used because every phenotype is with *S. pneumoniae*
even though the rRNA ligand is not Gram-positive-specific, and the same signalling is protective
in the lung but drives brain damage in meningitis, so only the protective side is annotated.

**2. Microbiome RNA and tissue-protective macrophages — recorded but not annotated.**
`publications/PMID_39853307.md` (J Exp Med 2025, full text) shows that lysosomal RNA stress in
RNase T2-deficient mice drives macrophage accumulation in spleen and liver
[PMID:39853307 "TLR13 activation by microbiota-derived ribosomal"] RNAs, maturing into
IL-10-expressing and tissue-clearance-gene-expressing Kupffer cells, with resistance to
acetaminophen and LPS/D-galactosamine liver injury. Cited as in vivo support on the GO:0019843
rRNA-binding row, since it shows the physiological ligand is ribosomal RNA of commensal origin,
and summarised in `description`. No process annotation is proposed: the phenotype was obtained
in an RNase-deficient background, and terms for macrophage accumulation or hepatoprotection would
attribute to this receptor an outcome produced by the macrophages it activates.

Also added to `description`, from PMID:32209688, that human TLR8 is regarded as performing the
equivalent endosomal bacterial-RNA sensing, which sharpens the review's bare statement that
humans lack the gene.

Not taken up: the LXR-alpha/MafB, Syk, ERK, mTOR and beta-catenin components of the hepatic
program, and the CD5L/C1qb/Axl/Tgm2 output, are downstream of the receptor; the meningitis
therapy work (chloroquine plus anti-TLR2 antibody) is pharmacological and not receptor-specific,
since chloroquine blocks endosomal acidification generally; the reported responses to
*Klebsiella pneumoniae* and streptococci of other groups come through a review; and the report's
15-nucleotide consensus motif differs from the 13-nucleotide ligand in the crystal structure, so
no residue-level claim was changed. The GO:0009615 response-to-virus row stays KEEP_AS_NON_CORE —
the report gives no new viral evidence and treats bacterial rRNA as the ligand throughout.

Actions: every existing annotation unchanged; one `NEW` row added. Other changes are
`description`, `core_functions` (one process term, two new supporting quotes), one new
`supported_by` quote on the rRNA-binding row and four new references (three PMIDs plus the Falcon
file).
