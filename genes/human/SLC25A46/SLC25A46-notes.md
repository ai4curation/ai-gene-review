# SLC25A46 (Q96AG3) — review notes

## Summary of gene function

SLC25A46 is a **divergent, "modified" member of the SLC25 mitochondrial carrier
family** that has been recruited to the **outer** mitochondrial membrane (OMM) and
has **lost the classical solute/metabolite-carrier (transport) function** of the
family. It is the mammalian counterpart of yeast Ugo1 and regulates
**mitochondrial membrane dynamics** — acting in a **pro-fission / anti-fusion**
manner — and controls **cristae architecture** (via the MICOS complex) and
**mitochondrial phospholipid distribution** (via ER–mitochondria contact / EMC
machinery). Loss of function causes an autosomal-recessive neurodegenerative
spectrum: Charcot–Marie–Tooth type 2 with optic atrophy (HMSN6B / "optic atrophy
spectrum disorder"), Leigh syndrome, and lethal congenital pontocerebellar
hypoplasia (PCH1E).

## Key evidence (with provenance)

### It is a modified/degenerate carrier that has lost transport function
- SLC25A46 is a member of the SLC25 (mitochondrial solute carrier) family but the
  carrier consensus residues are absent, so it is not a conventional transporter:
  [PMID:27390132 "These sequences are not conserved in SLC25A46"] and
  [PMID:27390132 "it does not likely have a conventional metabolite carrier function"].
- UniProt classifies it as a member of the mitochondrial carrier (TC 2.A.29) family
  by similarity only, while naming it a "Mitochondrial outer membrane protein":
  [file:human/SLC25A46/SLC25A46-uniprot.txt "Belongs to the mitochondrial carrier (TC 2.A.29) family."].
- Carrier homologs recruited to the OMM (Ugo1, MTCH1, MTCH2) perform functions
  "unrelated to metabolite transport": [PMID:26168012 "unrelated to metabolite transport"];
  SLC25A46 is "a highly derived carrier protein": [PMID:26168012 "human SLC25A46 is also a highly derived carrier protein"].
- Implication: SLC25 family / InterPro transmembrane-transporter MF propagations to
  SLC25A46 would be over-annotations. (GOA currently carries no transporter-activity
  MF annotation for SLC25A46 — the only MF terms present are protein binding /
  protein-containing complex binding.)

### Subcellular location = OUTER mitochondrial membrane
- Integral OMM protein by proteinase-K protection / carbonate extraction and
  colocalization with the OMM marker TOM20 (not inner-membrane markers):
  [PMID:26168012 "SLC25A46 is an integral outer membrane protein"],
  [PMID:26168012 "co-localizes more with the MOM marker (TOM20)"],
  [PMID:27390132 "SLC25A46 behaves as an outer membrane protein"].

### Molecular role = protein–protein / complex interactions, not catalysis
- Interacts with mitofilin/IMMT (MIC60): [PMID:26168012 "Mitofilin was among the top hits in this assay"].
- Interacts with the fusion machinery (MFN2, OPA1) and MICOS core components:
  [PMID:27390132 "components of the MICOS complex (MIC60, MIC19)"];
  [PMID:27390132 "SLC25A46 functions upstream of the MICOS complex and is required for the maintenance of mitochondrial cristae architecture"].
  Note: in the Abrams paper SLC25A46 did NOT co-IP MFN2/OPA1 in that assay
  [PMID:26168012 "SLC25A46 does not interact with MFN2 or OPA1, but forms a complex with mitofilin"];
  the Janer paper (cross-linking IP) detected the MFN2/OPA1/MICOS interactions.
- Interacts with the ER membrane protein complex (EMC), linking to ER→mito lipid transfer:
  [PMID:27390132 "SLC25A46 interacts with components of the EMC complex, involved in lipid transfer from the ER to the mitochondria"].
- So the honest MF is an adaptor / protein-containing-complex-binding role
  (GO:0044877), NOT transporter activity. Bare "protein binding" (GO:0005515) IPI
  annotations are uninformative; the specific complex-binding term is preferred.

### Core biological process = pro-fission regulation of mitochondrial dynamics
- Overexpression fragments mitochondria; knockdown causes hyperfusion:
  [PMID:26168012 "SLC25A46, unlike ANT2, leads to mitochondrial fragmentation in cell lines"];
  [PMID:26168012 "used siRNA to knockdown SLC25A46 and found it to cause mitochondrial hyperfusion"];
  [PMID:26168012 "SLC25A46 acts in a pro-fission manner"];
  [PMID:27543974 "SLC25A46 is a pro-fission mitochondrial outer membrane protein important in the regulation of mitochondrial dynamics"];
  [PMID:27543974 "overexpression of the wild-type protein led to mitochondrial fragmentation and disruption of the mitochondrial network"].

### Downstream consequences: cristae, respiration, phospholipids
- Loss disrupts MICOS → shortened cristae; secondary complex IV (COX) assembly defect:
  [PMID:27390132 "assembly defect in complex IV in subject fibroblasts"].
- Altered mitochondrial phospholipid composition (ER–mito lipid transfer role):
  [PMID:27390132 "phospholipid composition is altered in subject mitochondria"];
  [PMID:27390132 "Loss of SLC25A46 alters mitochondrial phospholipid composition"].
- These (complex IV assembly, phospholipid homeostasis) are best treated as
  DOWNSTREAM/secondary effects of the primary membrane-dynamics defect, not the
  core molecular function. IMP annotations to them (respiratory chain complex IV
  assembly; phospholipid homeostasis) are kept but as non-core.

### Disease
- HMSN6B (CMT2 + optic atrophy), MIM 616505 [file:human/SLC25A46/SLC25A46-uniprot.txt
  "Neuropathy, hereditary motor and sensory, 6B, with optic"].
- PCH1E (lethal congenital pontocerebellar hypoplasia), MIM 619303
  [PMID:27543974 title]; severity inversely correlates with mutant-protein stability.
- Leigh syndrome (T142I) [PMID:27390132 title].

## Annotation-review decisions (rationale highlights)

- **Transporter MF**: none present in GOA → nothing to remove; but flagged in notes
  that any SLC25-family transporter MF would be an over-annotation (transport-dead).
- **protein binding (GO:0005515) IPI** (IntAct/interactome, and PMID:26168012 vs IMMT):
  never REMOVE per policy; the numerous binary-interactome IPIs (PMID:25416956,
  PMID:32296183) are MARK_AS_OVER_ANNOTATED (bare, uninformative "protein binding");
  the mitofilin/IMMT IPI (PMID:26168012) is MODIFY → protein-containing complex
  binding (functionally meaningful adaptor interaction).
- **protein-containing complex binding (GO:0044877) IDA** (PMID:27390132): ACCEPT —
  the defining, informative MF (binds MFN2/OPA1/MICOS/EMC).
- **mitochondrial fission (GO:0000266)** (IDA PMID:26168012, IMP PMID:27390132/27543974,
  IBA): ACCEPT as core BP.
- **cristae formation (GO:0042407)** IMP: ACCEPT (core downstream architecture role).
- **mitochondrial outer membrane (GO:0005741)** (IDA/IMP/IBA/IEA): ACCEPT.
- **mitochondrion (GO:0005739)** (IDA HPA; HTP): KEEP_AS_NON_CORE (correct but less
  specific than OMM).
- **mitochondrial membrane fission (GO:0090149)** IEA: ACCEPT (accurate, more specific
  membrane-level fission term; consistent with mitochondrial fission).
- **mitochondrion organization (GO:0007005)** IEA (ARBA): KEEP_AS_NON_CORE (correct but
  very general parent of the specific fission/cristae terms).
- **respiratory chain complex IV assembly (GO:0008535)** IMP, **phospholipid
  homeostasis (GO:0055091)** IMP, **protein-containing complex assembly (GO:0065003)**
  IMP: KEEP_AS_NON_CORE — real but downstream/secondary consequences of the membrane
  dynamics defect, not the primary function.
- **axon development (GO:0061564)** IBA: KEEP_AS_NON_CORE — organismal/neuronal
  phenotype (motor-neuron/RGC axon defects on knockdown) rather than the cell-level
  molecular role; reflects tissue vulnerability to loss of mitochondrial dynamics.
