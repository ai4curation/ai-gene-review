# btl (breathless) – manual literature synthesis

No deep-research API was available for this review. This file was written by hand from
the cached publications in `publications/` and the UniProt record (Q09147, FGFR2_DROME).
Each statement carries its source.

## Identity and structure

- Breathless (Btl; FGFR2_DROME, Q09147; FlyBase FBgn0285896; GeneID 39564) is one of the two
  *Drosophila* FGF receptors; the other is Heartless (Htl). It is a 1052-aa single-pass type I
  membrane protein with a signal peptide (1-19), an extracellular region with five Ig-like C2
  domains (23-585), a transmembrane helix (601-626) and a cytoplasmic split tyrosine kinase domain
  (712-1000) [UniProt Q09147 FT lines]. UniProt: "Belongs to the protein kinase superfamily. Tyr
  protein kinase family. Fibroblast growth factor receptor subfamily."
- Original cloning: [PMID:1849109 "The Drosophila homolog of the vertebrate fibroblast growth factor
  receptor (FGF-R) was isolated by low-stringency hybridization"], and
  [PMID:1325393 "A Drosophila homolog of the fibroblast growth factor (FGF) receptor was isolated and
  structurally characterized"].

## Ligand and signalling mechanism

- Ligand is Branchless (Bnl), an FGF homolog: [PMID:8978613 "bnl encodes a homolog of mammalian
  fibroblast growth factors (FGFs) and appears to function as a ligand for the breathless receptor
  tyrosine kinase"].
- Bnl binds Btl at the recipient cell surface; endogenous tagged ligand and receptor colocalize
  [PMID:30328809 "In trans-heterozygous btl:cherryendo/bnl:gfpendo animals, all the Bnl:GFP puncta in
  the ASP colocalized with Btl:Cherry"]; Btl is on cytonemes that contact the Bnl source
  [PMID:21493861 "Each ASP had only a few long (>30 μm) cytonemes, most of which contained Btl:Cherry
  puncta."].
- Signal transduction requires the FGFR-specific adaptor Dof/Stumps/Heartbroken, which forms a
  complex with activated Btl and is tyrosine phosphorylated, then recruits Csw (SHP2) to activate
  Ras/MAPK [PMID:15082772 "expression of constitutive active Btl or Htl led to strong tyrosine
  phosphorylation of Dof"; "full-length Dof or the minimal Dof600 protein formed a complex with the
  activated version of both Drosophila FGFRs upon induction"]; [PMID:9809073 "Dof is an intracellular
  protein that is essential for signal transmission by the FGFR and acts downstream of the receptor
  and upstream of Ras"]; [PMID:9778498 heartbroken "acts downstream of the two FGF receptors but either
  upstream of or parallel to RAS1"]; Src64B also binds phospho-Dof [PMID:20154139].
- The intracellular domain mainly supplies a generic RTK signal: [PMID:11714681 "the intracellular
  domain of the fibroblast growth factor receptors (FGFRs) Breathless (Btl) and Heartless (Htl) can be
  functionally replaced by the intracellular domains of Torso (Tor) and epidermal growth factor
  receptor (EGFR)"].
- btl transcription is positively fed back by Bnl/Btl–MAPK signalling [PMID:12175485 "late btl
  expression is a target of Branchless/Breathless signaling"]. Surface level is controlled by
  endocytic machinery (Hrs/Stam, dVHL) [PMID:20422006; PMID:20516215].

## Biological roles

### Embryonic tracheal system (core)
- Required for tracheal cell migration and primary branch formation: [PMID:1325393 "The tracheal
  cells fail to migrate in severe mutants and remain within the tracheal pits."]; temporal
  requirement at onset of migration and for tracheole (terminal branch) formation [PMID:8541215].
- Graded activity patterns secondary and terminal branch fates [PMID:8918892 "spatially regulated
  BTL activity guides tracheal cell migration and quantitatively regulated BTL activity determines
  the patterns of secondary and terminal branching cell fates"]; required to activate secondary
  branching markers [PMID:8625828].
- Tip (lead) cell selection by competition in FGFR activity [PMID:16760977 "those with the highest
  FGF receptor activity take the lead positions"].
- FGF acts as a chemoattractant read by individual cells [PMID:26342211].
- Filopodial activity of tip cells [PMID:12015974 "Bnl/FGF signaling affects the formation of dynamic
  filopodia"]; FGF-dependent extensions contacting bridge-cells for branch interconnection
  [PMID:12034756].
- Tracheal invagination itself does not need btl [PMID:1849109 "In embryos homozygous for a deletion
  of several genes including the DFGF-R locus, the initial formation of the tracheal pits is not
  affected."] – relevant to the GO:0035202 tracheal pit formation annotation (PMID:16818611, abstract
  only, which is about Crossveinless-c and EGFR).

### Larval/pupal trachea
- Air sac primordium (ASP): FGF is mitogen and chemoattractant [PMID:12194851]; Fgf directs migration
  at the tip [PMID:16326394]; Bnl/Btl induces Vein via Pnt [PMID:26632449]; proliferation vs
  endoreplication of tracheal progenitors [PMID:31237953].
- Terminal cells: activated Btl (λBtl) increases branching and cell growth [PMID:21750259] and
  ectopic lumen formation, dependent on Zpr1 [PMID:23029159 "overexpression of this activated form of
  the FGFR in terminal cells resulted in increased lumen formation"; loss-of-function could not be
  tested "because tracheal cells mutant for btl fail to outgrow or undergo branching"].

### Other tissues (non-core)
- Midline glia migration in embryo [PMID:1325393]; retinal basal glia in eye disc, where Btl
  restricts the onset/extent of migration [PMID:22384378 "Bnl expressed by the eye tissue activates
  nonautonomous Btl signaling in the glial cells to regulate the temporal onset and extent of RBG
  migration"].
- Border cell migration in ovary: btl is a target of Slbo/C/EBP and genetically enhances slbo
  [PMID:7671793].
- Male genital disc: FGF recruits mesodermal cells expressing its receptor [PMID:12062107].
- Adult brain dorsal cluster neuron axon retraction [PMID:17032066 "blocking the activities of the
  FGFR Btl [54] or the Rac1 GTPase [50] significantly increased the number of DCN axons crossing"].
- Lymph gland progenitor maintenance via vascular-niche Bnl [PMID:33395389]; lamellocyte Btl in wasp
  egg melanization [PMID:32396065].
- NMJ: btl heterozygosity enhances Smn knockdown NMJ defects, but has no effect alone
  [PMID:21300852].
