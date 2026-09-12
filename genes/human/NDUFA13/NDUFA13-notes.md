# NDUFA13 (GRIM-19) — review notes

UniProt: Q9P0J0 (NDUAD_HUMAN). HGNC:17194. Gene = NDUFA13; synonym GRIM19.
144 aa, 16.7 kDa. Chr 19.

## Identity and core role

NDUFA13 is an accessory ("supernumerary") subunit of the peripheral/matrix arm of
mitochondrial Complex I (NADH:ubiquinone oxidoreductase), and is also known as
GRIM-19 (Gene associated with Retinoid-IFN-induced Mortality 19) and Complex I-B16.6.

- UniProt FUNCTION: "Accessory subunit of the mitochondrial membrane respiratory
  chain NADH dehydrogenase (Complex I), that is believed not to be involved in
  catalysis (PubMed:27626371)." [file:human/NDUFA13/NDUFA13-uniprot.txt]
- It is a genuine stable structural subunit of the mature holoenzyme, non-catalytic
  for OXPHOS. Honest MF = structural molecule activity (GO:0005198); it
  contributes_to (but does not independently enable) the complex-level
  NADH:ubiquinone oxidoreductase activity (GO:0008137). part_of respiratory chain
  complex I (GO:0045271). BP: mitochondrial electron transport NADH to ubiquinone
  (GO:0006120) and Complex I assembly (GO:0032981).
- Subunit membership confirmed by MS immunopurification of human Complex I
  [PMID:12611891 "These polypeptides include the GRIM-19 protein, which is claimed to
  be involved in apoptosis"] and by CRISPR-KO+proteomics defining accessory subunits
  as integral [PMID:27626371 "25 subunits are strictly required for assembly of a
  functional complex"].
- Essential for CI assembly/activity: KO/knockdown destroys CI assembly and electron
  transfer [PMID:15367666 "elimination of GRIM-19 destroys the assembly and electron
  transfer activity of complex I"]; germline R57H mutation causes CI instability and
  mitochondrial disease MC1DN28 [PMID:25901006 "induces CI instability", "the
  abundances of NDUFA13 protein, CI holoenzyme and super complexes were drastically
  reduced"].
- Location: mitochondrial inner membrane, matrix side, single-pass TM (residues
  30-51). Structurally resolved in cryo-EM Complex I / megacomplex (PDB 5XTB-9TI4;
  PMID:28844695).

## Moonlighting role (genuine, non-core secondary functions)

GRIM-19 was DISCOVERED as an apoptosis/cell-death regulator, independent of its
later-recognized Complex I role. These moonlighting activities are real and
experimentally supported — treat as KEEP_AS_NON_CORE, not over-annotation.

- Discovery: isolated in an antisense knockout screen for genes mediating
  IFN-beta + all-trans-retinoic-acid (IFN/RA)-induced tumor-cell death; primarily
  nuclear on discovery, IFN/RA-inducible [PMID:10924506 "Overexpression of GRIM-19
  enhances cell death in response to IFN/RA. GRIM-19 is primarily a nuclear protein
  whose expression is induced by the IFN/RA combination."].
- Negative regulator of STAT3: binds STAT3 (not STAT1/2/5A), inhibits
  STAT3-dependent transcription without blocking STAT3 phosphorylation/DNA binding;
  requires the STAT3 TAD and Ser727 [PMID:12867595 "GRIM-19 inhibits transcription
  driven by activation of STAT3, but not STAT1"; "our studies identify a specific
  inhibitor of STAT3"]. Independent report [PMID:12628925 "GRIM-19 represses Stat3
  transcriptional activity and its target gene expression"].
  → NDUFA13's own GOA has this captured as GO:0045892 (negative regulation of
  DNA-templated transcription, IDA, PMID:12867595). More precise MF/BP would be
  GO:1904893 (negative regulation of receptor signaling pathway via STAT).
- Apoptosis / HtrA2 axis: GRIM-19 binds the mitochondrial serine protease HtrA2/OMI
  and augments IFN/RA-dependent cell death and XIAP destruction [PMID:17297443
  "GRIM-19 physically interacts with HtrA2 and augments cell death in an IFN/all-trans
  retinoic acid (RA)-dependent manner"; "the HtrA2-driven destruction of the
  antiapoptotic protein X-linked inhibitor of apoptosis (XIAP) is augmented"].
  Basis for GO:1900119 (pos reg execution phase of apoptosis), GO:0045732 (pos reg
  protein catabolic process), GO:0061133 (endopeptidase activator activity, IC),
  GO:0035458 (cellular response to IFN-beta), GO:0071300 (cellular response to RA).
- STAT3 mitochondrial import: GRIM-19 acts as a chaperone recruiting STAT3 into
  mitochondria and integrating it into Complex I [PMID:23271731 "GRIM-19 ... acts as
  a chaperone to recruit STAT3 into mitochondria"; "GRIM-19 enhances the integration
  of STAT3 into complex I"]. This underpins GO:0045039 (protein insertion into
  mitochondrial inner membrane, IDA). Note: STAT3 is imported by GRIM-19, not a
  generic membrane-insertase; the term is broader than the specific chaperone role.
- NOD2/innate immunity: interacts with NOD2/CARD15 and is required for NOD2-mediated
  NF-kB activation and antibacterial responses in intestinal epithelium
  [PMID:15753091 "GRIM-19 is required for NF-kappaB activation following NOD2-mediated
  recognition of bacterial muramyl dipeptide"]. Basis for the NOD2 protein-binding
  IPI.

## Localization annotations

- Mitochondrion / mitochondrial inner membrane (matrix side): strongly supported
  (IDA/EXP, PMID:12628925, 15059901, 15367666, 12611891, 28844695, HPA, Reactome).
- Nucleus / nucleoplasm / cytoplasm: supported for the moonlighting pool
  [PMID:10924506 "GRIM-19 is primarily a nuclear protein"; PMID:12628925 SUBCELLULAR
  LOCATION Nucleus]. UniProt: "May be translocated into the nucleus upon IFN/RA
  treatment." Keep as non-core (secondary pool).

## Protein-binding (GO:0005515) IPI annotations

Bare "protein binding" is uninformative. Per policy, NEVER REMOVE a bare protein
binding IPI — MARK_AS_OVER_ANNOTATED. The biologically meaningful partners (STAT3,
NOD2, HtrA2) are captured via specific MF/BP terms; the HTT/HTRA2 large-scale
interactome & aggregation-map hits (PMID:17500595, 31617661, 32814053, 40205054)
are HTP and non-informative as MF.

## Dubious / IEA to scrutinize

- GO:0005524 ATP binding (NAS, PMID:10924506): the discovery paper does not
  demonstrate ATP binding; NDUFA13 is a non-catalytic accessory subunit with no
  nucleotide-binding motif. UniProt does NOT list ATP binding as a function. This NAS
  is an over-annotation (author speculation). MARK_AS_OVER_ANNOTATED (NAS, not IEA;
  cannot REMOVE experimental, but NAS is a statement without experiment — still, keep
  conservative: over-annotated).
- GO:0005634 nucleus IEA (GO_REF:0000044, SubCell mapping): duplicates the
  experimental EXP nucleus annotation; keep as non-core.

## Disease

- Hurthle cell thyroid carcinoma (HCTC) susceptibility (somatic/germline variants;
  PMID:15841082).
- Mitochondrial complex I deficiency nuclear type 28 (MC1DN28), autosomal recessive,
  R57H (PMID:25901006).

## Core function synthesis

1. Structural constituent of Complex I (GO:0005198), contributing to NADH:ubiquinone
   oxidoreductase activity (GO:0008137), part_of respiratory chain complex I
   (GO:0045271), in mitochondrial inner membrane (GO:0005743); involved in
   mitochondrial electron transport NADH->ubiquinone (GO:0006120) and CI assembly
   (GO:0032981).
2. Moonlighting: negative regulator of STAT3 signaling / pro-apoptotic cell-death
   regulator (non-core, but genuine and well documented).
