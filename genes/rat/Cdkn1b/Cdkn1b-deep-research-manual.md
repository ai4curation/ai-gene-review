# Cdkn1b (rat, UniProt O08769) - manual literature synthesis

No deep-research API was available for this session, so this file is a manual synthesis
written by the reviewer from cached publications (`publications/PMID_*.md`) and PubMed
searches. Every statement carries its provenance. Most rat papers in GOA are
abstract-only in the cache; full text was available for PMID:16987298 and for several
human/mouse donor papers (PMID:19056892, PMID:12529437, PMID:12698196).

## Identity

- Rat Cdkn1b encodes p27Kip1, a 197-aa Cip/Kip-family cyclin-dependent kinase inhibitor
  (UniProt O08769, unreviewed TrEMBL; RGD:69062; GeneID 83571). The record carries the Pfam
  CDI domain (PF02234, residues 31-79, "Cyclin-dependent kinase inhibitor") and long
  MobiDB-lite disordered regions at 1-34 and 86-197 [file:rat/Cdkn1b/Cdkn1b-uniprot.txt].
- PANTHER places it in PTHR10265:SF9 (CYCLIN-DEPENDENT KINASE INHIBITOR 1B)
  [file:rat/Cdkn1b/Cdkn1b-uniprot.txt].

## Core molecular function (mostly established on mouse/human orthologs)

- Mouse p27 was cloned as a cyclin D1-Cdk4 interactor: "p27 interacts strongly with D-type
  cyclins and Cdk4 in vitro and more weakly with cyclin E and Cdk2" and "Recombinant p27 is
  a potent inhibitor of cyclin D1-Cdk4 and cyclin A-Cdk2 protein kinase activity"
  [PMID:8033213].
- Structure of human p27 on cyclin A-Cdk2: p27 "binds the complex as an extended structure
  interacting with both cyclin A and Cdk2" and "inserts into the catalytic cleft, mimicking
  ATP" [PMID:8684460].
- Binding is sequential, folding-upon-binding, initiated on the cyclin: "Binding to
  Cdk2-cyclin A is accompanied by p27 folding" [PMID:15024385].
- Assembly factor role for cyclin D-CDK4: "p21(CIP), p27(KIP), and p57(KIP2) all promote
  the association of cdk4 with the" D-type cyclins [PMID:9106657]; in mouse fibroblasts
  "During G1, all of p27 was associated with cyclin D1.Cdk4 and was then redistributed to
  cyclin A.Cdk2 as cells entered S phase" [PMID:8534916].

## Rat-specific experimental evidence

- Rat liver regeneration: "High amounts of p27Kip1 bound to cyclin E-CDK2 were observed
  during the first 13 h after PH, when CDK2 activity was very low", and "p27Kip1 acts as a
  brake on cyclin E-CDK2 activity during the first 13 h after a PH" [PMID:10952244].
- In vitro, "Phosphorylation of histone H1 or E1A proteins by CDK2 complex was inhibited by
  p27, but, in contrast, p27 stimulated the phosphorylation of E1A proteins by CDK4"; p27
  binds adenovirus E1A through its N-terminal region [PMID:9675118] (species of the
  recombinant p27 not stated in the abstract; GOA attributes the IPI to rat).
- Rat thyroid FRTL-5 cells: Hsc73 (Hspa8) co-immunoprecipitates with p27 in a cell-cycle
  dependent way, maximal at G1/S, and ATP dissociates the complex [PMID:10198213].
- Rat cochlear explants: "Expression of short hairpin RNA targeting p27Kip1 ... led to
  measurable proliferation in the organ of Corti" [PMID:23612739].
- Rat pulmonary arterial smooth muscle cells: "P27 siRNA and TIMP3 siRNA could both
  attenuate the anti-proliferation effect of miR-222 inhibitor in PASMCs" [PMID:28854428].
- Rat cortical neurons: "p27 was present only in the neuronal nucleus", and glutamate
  reduces nuclear p27 because "p27 was degraded as a substrate of activated calpain 1"
  [PMID:16824045].
- Rat MENX syndrome: a homozygous germ-line frameshift in Cdkn1b causes a multiple
  endocrine neoplasia-like syndrome; "MENX-affected rats show dramatic reduction in
  p27(Kip1) protein" [PMID:17030811].
- Rat RG2 glioblastoma cells: n-butylidenephthalide treatment induces G0/G1 arrest, and
  p27 protein rises ("similar results for p27, Bax and AIF were detected in RG2 cells after
  treatment with BP") although RG2 lacks p53 and p16 [PMID:16987298, full text]. This is an
  expression-correlation finding; it does not test p27 function.
- Expression-change (IEP) studies in rat tissues/cells: p27 rises with high glucose in
  podocytes [PMID:15698433], after hindlimb hypoxia/ischemia [PMID:15799773], with cadmium
  in NRK-52E cells [PMID:16730872], with fluvastatin+everolimus in SMCs [PMID:18413661],
  and with genistein in aortic SMCs [PMID:18490856]; it falls with estrogen and ghrelin in
  pelvic-floor muscle [PMID:18496635].
- Reactome (rat): "Transcription from the rat Cdkn1b (p27Kip1) gene promoter is stimulated
  by recombinant human FOXO1 or recombinant human FOXO3" [Reactome:R-NUL-9620778].

## Regulation, localization and turnover (orthologs)

- Human p27 is nuclear in G0/early G1 and shuttles to the cytoplasm via CRM1 at G1/S; the
  export studies treat p27 as cargo [PMID:12529437].
- Human p27 degradation is triggered by Thr187 phosphorylation and recognition by
  SCF(Skp2)-Cks1 [PMID:16209941]; an alternative Wnt-induced turnover requires CUL4A/CUL4B
  [PMID:19056892]; an endolysosomal route is mediated by SNX6, with p27 "partially
  colocalize[d] in endosomes" [PMID:20228253].
- Cytoplasmic p27 binds stathmin and affects microtubule stability and cell motility
  [PMID:15652749].

## Organism-level roles (mouse genetics)

- p27-null mice show gene-dose-dependent gigantism, multiorgan hyperplasia, pituitary
  intermediate-lobe tumors and female sterility [PMID:8646781].
- p27 controls timely cell-cycle withdrawal of organ of Corti progenitors [PMID:10079221],
  cooperates with p57 for cell-cycle exit of lens fiber cells and placental trophoblasts
  [PMID:9784491], and with p21 for postnatal cardiomyocyte cell-cycle exit [PMID:24380855];
  p27-KO prostate shows increased epithelial proliferation and apoptosis [PMID:16014817].
