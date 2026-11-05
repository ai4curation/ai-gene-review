# Vegfa (rat, UniProt P16612) - manual literature synthesis

No deep-research API was available for this review. This file is a manual synthesis
written by the reviewer from the cached publications in `publications/`, the rat and
human UniProt records, and the existing human VEGFA review
(`genes/human/VEGFA/VEGFA-ai-review.yaml`). Every assertion carries its source.

## Identity and structure

- Rat Vegfa (RGD:619991, GeneID 83785) encodes vascular endothelial growth factor A, a
  secreted, disulfide-linked homodimeric cystine-knot growth factor of the PDGF/VEGF
  family. UniProt: "Belongs to the PDGF/VEGF growth factor family." and
  "Homodimer; disulfide-linked (PubMed:7706320)." [file:rat/Vegfa/Vegfa-uniprot.txt]
- The rat protein was first purified from glioma cells: "Glioma-derived vascular
  endothelial cell growth factor (GD-VEGF) is a 46-kDa dimeric glycoprotein mitogen"
  and "The GD-VEGF homodimeric subunit is homologous to the platelet-derived growth
  factor A and B chains" [PMID:2320579].
- Alternative splicing yields VEGF-A188 (displayed), VEGF-A164, VEGF-A144 and VEGF-A120.
  Isoforms differ in their basic heparin/ECM-binding exons: "VEGF-A120 is acidic and
  freely secreted." while "VEGF-A188 is very basic, it is cell-associated after secretion
  and is bound avidly by heparin and the extracellular matrix"
  [file:rat/Vegfa/Vegfa-uniprot.txt]. In rat uterus "The VEG/PF gene is alternatively
  spliced and gives rise to three transcripts coding for proteins of 188, 164, and 120
  amino acids" [PMID:8344219].

## Molecular function

- Receptor ligand for the receptor tyrosine kinases VEGFR1/FLT1 and VEGFR2/KDR and for the
  co-receptor NRP1. UniProt: "Binds to the FLT1/VEGFR1 and KDR/VEGFR2 receptors, heparan
  sulfate and heparin." [file:rat/Vegfa/Vegfa-uniprot.txt]. Human/porcine-cell work:
  "Vascular endothelial growth factor (VEGF) is a homodimeric peptide growth factor which
  binds to two structurally related tyrosine kinase receptors denoted Flt1 and KDR."
  [PMID:7929439]; KDR "encodes a receptor for VEGF" [PMID:1417831]; "flt encodes a
  receptor for VEGF-VPF" [PMID:1312256]; NRP1 "binds vascular endothelial growth factor
  (VEGF)-A and is thought to act as a coreceptor" for KDR [PMID:21653826].
- Signalling through VEGFR2 drives chemotaxis and mitogenesis: "The KDR expressing cells
  showed striking changes in cell morphology, actin reorganization and membrane ruffling,
  chemotaxis and mitogenicity upon VEGF stimulation" [PMID:7929439].
- Rat in vitro evidence that VEGF acts through VEGFR2 on neural precursors: "the effect
  of VEGF was blocked by the VEGFR2/Flk-1 receptor tyrosine kinase inhibitor SU1498"
  [PMID:12181492, full text].
- Heparin/ECM: fibronectin binding is pH regulated [PMID:14570917]; rat glomerular
  VEGF localizes "to podocytes and in the basement membrane" [PMID:11940521].
- Secondary ligand activity for PDGF receptors: "VEGF-A binds to both PDGFRalpha and
  PDGFRbeta and induces tyrosine phosphorylation" in mesenchymal stem cells
  [PMID:17470632].
- Binding by the heparin-binding growth factor pleiotrophin (HARP) sequesters VEGF from
  VEGFR2 in rat C6 glioma cells [PMID:17881084].

## Biological processes (rat experimental evidence)

- Angiogenesis and alveolarization: "VEGF blockade decreases lung VEGF and VEGF receptor 2
  (VEGFR-2) expression in newborn rats and impairs alveolar development" [PMID:16230500].
- Coronary collateral growth requires VEGF [PMID:16203926]; postnatal coronary
  angiogenesis [PMID:11397779, abstract not cached].
- Ischaemic hindlimb angiogenesis promoted by VEGFA-transduced EPCs [PMID:23562340].
- Vascular permeability: soluble VEGFR2 "prevented I/R-mediated increase in lung vascular
  permeability in rats" [PMID:16793871]; VEGF increases glomerular endothelial
  permeability [PMID:16160062] and caveolae/fenestrae formation [PMID:11940521].
- Neurogenesis and neuroprotection: VEGF stimulates BrdU incorporation into neuronal
  precursors in vitro and in vivo [PMID:12181492]; hippocampal VEGF gene transfer
  increases neurogenesis in adult rats [PMID:15258583]; VEGF-A reduces retinal neuron
  apoptosis [PMID:17591953]; endogenous VEGF protects astrocytes during
  oxygen-glucose deprivation [PMID:18614764].
- Autocrine/paracrine mitogen for vascular smooth muscle cells downstream of MCP-1
  [PMID:14693680].
- Exercise-induced bone angiogenesis and bone gain depend on VEGF [PMID:15312247].
- VEGF secreted by activated T cells promotes a Th1 phenotype [PMID:15034080].

## Expression and regulation (IEP-type evidence)

- Hypoxia induces VEGF in cardiomyocytes; hypoxic myocyte medium induces endothelial
  COX-2 through VEGF [PMID:12881220].
- Estrogen rapidly induces uterine VEGF [PMID:8344219] through PI3K-dependent recruitment
  of ERalpha and HIF-1alpha to the promoter [PMID:17272396].
- Dexamethasone represses VEGF in glioma cells [PMID:10215998] and placenta
  [PMID:16959835]; FGF-2 induces VEGF-A via ATF-4 in smooth muscle cells [PMID:18617696];
  mechanical load induces VEGF mRNA in neonatal cardiomyocytes [PMID:19012730, full
  text]; doxorubicin increases VEGF-A release from cardiac endothelial cells
  [PMID:22326847]; diesel exhaust lowers cardiac VEGF [PMID:23887904, full text]; a
  hyaluronan-butyrate-retinoate ester increases VEGF transcription and secretion in rat
  cardiomyocytes and Stro-1 cells: "The HBR treatment enhanced the secretion of VEGF and
  HGF in the culture medium from both RCm and Stro-1 cells." [PMID:20097747, full text].
- Expression in mammary gland increases during pregnancy and lactation [PMID:10878616 via
  UniProt].

## Interpretation for GO review

The core, conserved function is that of an extracellular receptor ligand (growth factor)
for VEGFR1/VEGFR2 (with NRP1 and heparan sulfate as co-receptors) that drives endothelial
proliferation, migration/chemotaxis, survival and permeability, and thereby angiogenesis.
Many GOA rows are developmental phenotypes transferred from mouse knockouts, or
expression-response (IEP) rows, which are non-core. Transcription, mRNA-stability and
gene-expression rows reflect distal signalling outputs, not activities of VEGF-A itself.
