# FGF23 (human, Q9GZV9) curation notes

## 2026-09-30 initial review

### Identity and molecular role
- Secreted endocrine member of the FGF family (FGF19 subfamily). Bone-derived (osteocytes/osteoblasts) phosphaturic hormone.
  [PMID:17086194 "FGF23 is a unique member of the fibroblast growth factor (FGF) family because it acts as a hormone that derives from bone and regulates kidney functions"]
- Receptor: alpha-Klotho (KL) + FGFR1c. Klotho converts FGFR1c into an FGF23-specific receptor.
  [PMID:17086194 "Thus, the concerted action of Klotho and FGFR1(IIIc) reconstitutes the FGF23 receptor."]
  [PMID:16436388 "The Klotho-FGFR complex binds to FGF23 with higher affinity than FGFR or Klotho alone."]
- Structural basis: 1:1:1 ternary complex; alpha-Klotho tethers FGF23 C-terminal tail; dimerisation still requires heparan sulfate.
  [PMID:29342138 "α-klotho simultaneously tethers FGFR1c by its D3 domain and FGF23 by its C-terminal tail"]
  [PMID:19966287 "the soluble ectodomains of FGFR1c and Klotho are sufficient to form a ternary complex with FGF23 in vitro"]
- Intrinsic FGFR affinity is modest without Klotho [PMID:16436388 "it has modest receptor affinity (K D = 200–700 nM)"].

### Inactivation / processing
- Cleavage at RXXR (176-179) by proprotein convertase (furin) inactivates; GALNT3 O-glycosylation blocks cleavage; FAM20C phosphorylation of Ser180 opposes glycosylation (UniProt PTM).
  [PMID:16638743 "GalNAc-T3 selectively directs O-glycosylation in a subtilisin-like proprotein convertase recognition sequence motif, which blocks processing of FGF23"]
  [PMID:19966287 "The phosphaturic activity of FGF23 is abrogated by proteolytic cleavage at the RXXR motif"]
- The cleaved C-terminal tail is a competitive inhibitor [PMID:19966287 "generating an endogenous inhibitor of FGF23"].

### Physiology (downstream outcomes of signalling in target cells)
- Kidney proximal tubule: reduces NaPi-2a, phosphaturia [PMID:11409890 "both wild-type FGF-23 and the ADHR mutant, FGF-23(R179Q), inhibit phosphate uptake in renal epithelial cells"]; [PMID:15040831 "accompanied with a reduction in renal mRNA and protein levels for the type IIa sodium-phosphate cotransporter"].
- Vitamin D: suppresses CYP27B1, induces CYP24A1 [PMID:15040831 "FGF-23 reduced renal mRNA for 25-hydroxyvitamin D-1alpha-hydroxylase and increased that for 25-hydroxyvitamin D-24-hydroxylase starting at 1 h"].
- Knockout: hyperphosphatemia, high 1,25(OH)2D [PMID:14966565 "The Fgf23 –/– mice displayed significantly high serum phosphate with increased renal phosphate reabsorption"].
- Parathyroid: Klotho-dependent MAPK/EGR1 and decreased PTH secretion (rat) [PMID:17992255 "FGF23 acts directly on the parathyroid through the MAPK pathway to decrease serum PTH"].
- Bone (in vitro overexpression): suppresses osteoblast differentiation / mineralization [PMID:18282132 "FGF23 overexpression suppresses not only osteoblast differentiation but also matrix mineralization independently of its systemic effects on Pi homeostasis"].
- Disease: ADHR gain-of-function (cleavage-resistant R176/R179) [PMID:11062477]; loss-of-function -> hyperphosphatemic familial tumoral calcinosis (UniProt).

### Curation decisions (key)
- Core MF: FGF receptor binding (GO:0005104; specifically type 1 FGFR binding GO:0005105 via FGFR1c) plus hormone activity (GO:0005179). Growth factor activity (GO:0008083) is an inherited family function; FGF23 acts as hormone rather than mitogen -> kept as non-core.
- Participation vs outcome: vitamin D catabolic process (IDA) is catalysed by CYP24A1, whose expression FGF23 signalling induces -> MODIFY to regulation terms. Phosphate ion homeostasis kept (hormones are conventionally annotated to the homeostatic process they regulate).
- Protein binding IPI rows: Klotho/FGFR1 rows -> MODIFY to FGF receptor binding; SMAD4 row (high-throughput neo-PPI screen) -> REMOVE (uninformative).
- IBA cytoplasm: FGF23 has a signal peptide and acts extracellularly -> REMOVE (is_active_in cytoplasm inherited from intracellular/non-classical family members).
- IBA neurogenesis / cell migration / positive regulation of cell proliferation: paracrine-FGF functions not supported for FGF23 -> MARK_AS_OVER_ANNOTATED.
- Rat/mouse Ensembl IEA "response to X" terms (leptin, IL-6, PTH, vitamin D, magnesium, sodium phosphate) describe regulation of FGF23 expression, i.e. the gene responds as a target, not the protein's function -> MARK_AS_OVER_ANNOTATED / KEEP_AS_NON_CORE as argued per row.

### Final action tally (2026-09-30)
ACCEPT 160 (of which 150 are the Reactome extracellular-region TAS rows), KEEP_AS_NON_CORE 11,
MODIFY 8, MARK_AS_OVER_ANNOTATED 8, REMOVE 2, NEW 1. No UNDECIDED.

- GO:0010966 regulation of phosphate transport (IDA) -> MODIFY to GO:2000119 negative regulation of
  sodium-dependent phosphate transport: direction and transport system are both established
  [PMID:11409890], [PMID:15040831 NaPi-2a reduction].
- GO:0042369 vitamin D catabolic process (IDA) and GO:0042359 vitamin D metabolic process (IEA) ->
  MODIFY to GO:0010957 negative regulation of vitamin D biosynthetic process. FGF23 catalyses no step;
  CYP24A1/CYP27B1 do, and FGF23 regulates their expression. GO has no "regulation of vitamin D
  catabolic process" term - raised in suggested_questions.
- GO:0046888 (IEA + ISS) -> MODIFY to GO:2000829 negative regulation of parathyroid hormone secretion,
  the hormone being known [PMID:17992255].
- NEW GO:0005179 hormone activity: FGF23 is a bone-derived circulating hormone; more informative than
  the inherited GO:0008083 growth factor activity, which is kept as non-core.
- propagation_review blocks added for the four IBA rows judged wrong (cytoplasm, proliferation,
  neurogenesis, cell migration), all traced to PANTHER:PTN000160075 with
  root_cause PROPAGATION_BAD.

### Module relevance (modules/fgfr_signaling.yaml)
The module's `endocrine_fgf_ligand` annoton uses GO:0005104 for FGF23, which this review accepts. The
review additionally settles that FGF23's specific receptor term is GO:0005105 (type 1 FGFR binding,
FGFR1c) and that its distinctive molecular function is hormone activity (GO:0005179) rather than
growth factor activity - the module may wish to note the endocrine-ligand hormone activity alongside
receptor binding. No module edits made.
