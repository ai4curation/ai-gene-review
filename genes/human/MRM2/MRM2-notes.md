# MRM2 (human, Q9UI43) review notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Scope: de novo review of human MRM2 (FTSJ2), the characterised mitochondrial member of
PANTHER subfamily PTHR10920:SF18, which will serve as the experimental reference for the
DROME/Mrm2 ortholog. ProtNLM2 output was not consulted.

### Deep research status

`just deep-research-falcon human MRM2 --fallback perplexity-lite` failed: falcon returned
"Edison API request failed: Failed to authenticate", and the perplexity-lite fallback hit
its 600 s timeout. No deep-research file was produced. The review is based on the cached
primary literature (`publications/`), the UniProt record and the PTHR10920 PAINT table.

### Evolutionary placement

- UniProt: `PANTHER; PTHR10920:SF18; RRNA METHYLTRANSFERASE 2, MITOCHONDRIAL`; HAMAP
  MF_01547 (RNA_methyltr_E) and "RNA methyltransferase RlmE family", i.e. the
  FtsJ/RlmE/RrmJ clade that 2'-O-methylates the A-loop uridine of LSU rRNA.
- PAINT (`interpro/panther/PTHR10920/PTHR10920-paint.tsv`): node PTN000100455 carries
  GO:0008650 (seeds SGD Mrm2 S000003104, E. coli RlmE P0C0R7, human MRM2), GO:0000027
  (seeds fly FBgn0038737, RlmE, human MRM2) and GO:0031167 (SGD, human). PTN000100456
  carries GO:0005739 (seeds mouse Mrm2 MGI:1915267, SGD Mrm2, human MRM2). Human MRM2 is
  itself a seed for all four IBD statements, so its IBA rows are inherited claims for
  which the target also has direct experimental grounding (not circular).

### What is experimentally established in human (vs inferred)

Established in human cells:
- Mitochondrial (matrix) localisation: endogenous protein cofractionates with matrix
  mtSSB1 and is proteinase K protected [PMID:25009282 "Cell fractionation experiments
  confirmed the mitochondrial localization of the three proteins, as the endogenous
  proteins cofractionated with the well-characterized mitochondrial matrix protein mtSSB1
  and were resistant to proteinase K treatment (Figure 2C)."]; foci near mtDNA nucleoids
  [PMID:24036117 "These proteins are confined to foci located in the vicinity of mtDNA
  nucleoids."].
- Site of action: Um1369 of 16S mt-rRNA (U3039 in mtDNA numbering) in the A-loop
  [PMID:25074936 DNAzyme assay; PMID:25009282; PMID:35177605 RNA LC-MS2 and
  transcriptome-wide 2'-O-Me profiling in MRM2 KO cells]. Catalytic residues K59 and D154
  (RlmE K38/D124 equivalents): K59A and D154A abolish the modification [PMID:35177605].
- MRM3-dependent Gm1370 and MRM2-dependent Um1369 are interdependent [PMID:35177605].
- Catalysis-independent assembly-factor role in mtLSU biogenesis: KO causes accumulation
  of immature mtLSU with disordered domains IV/V and bound MALSU1:L0R8F8:mtACP; K59A and
  D154A rescue mitochondrial translation [PMID:35177605 "As observed by the restoration of
  the expression of MT-CO2, both K59A and D154A MRM2 variants were able to rescue the
  defect in mitochondrial translation caused by knock-out of the endogenous gene despite
  their null methyltransferase activity."].
- MRM2 is bound to late mtLSU assembly intermediates in cryo-EM structures (GTPBP5 KO
  intermediates) [PMID:34135318 "Both the GTPBP5KO and GTPBP5IP mt-LSU assembly
  intermediates reveal several trapped assembly factors: the MTERF4-NSUN4 complex, MRM2,
  MTG1, and the MALSU1:L0R8F8:mt-ACP module"]; MTERF4/NSUN4 expose the A-loop for MRM2
  [PMID:34135320 abstract].
- GTPBP5 (MTG2) promotes Um1369 installation; GTPBP5 interacts with MRM2
  [PMID:32652011].
- Disease: homozygous p.Gly189Arg causes a MELAS-like syndrome (MTDPS17); yeast mrm2
  equivalent fails to complement respiration [PMID:28973171].

Inferred (not established for human MRM2 directly): the precise SAM-binding mode from the
SGC crystal structure (2NYU) is experimental, but the "proton acceptor" active site K194
in UniProt is by similarity to RlmE (ECO:0000250).

### Annotation decisions (summary)

- Nucleolus (IDA, PMID:11827451): REMOVE. Contradicted by all later work; the nucleolar
  signal came from an N-terminally GFP-tagged construct, which masks the N-terminal
  mitochondrial targeting sequence [PMID:24036117 "In that report, fusion of GFP on the N
  terminus of MRM2/FTSJ2 resulted in a nucleolar location."].
- mitochondrion (6 rows) -> MODIFY to mitochondrial matrix (GO:0005759), which the gene
  already carries and which fractionation supports.
- rRNA processing, rRNA methylation, methyltransferase activity, ribosomal LSU assembly:
  MODIFY to the specific terms the gene carries (GO:0000451, GO:0008650, GO:1902775).
- No NEW annotations. Mitochondrial translation and respiration defects in KO cells and
  the Drosophila developmental arrest are downstream consequences of an mtLSU assembly
  defect, not process participation.
