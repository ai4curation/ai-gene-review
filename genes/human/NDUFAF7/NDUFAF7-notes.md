# NDUFAF7 (Q7L592) — review notes

## Summary of gene function

NDUFAF7 (NADH dehydrogenase [ubiquinone] complex I assembly factor 7; formerly C2orf56;
orthologue of *Dictyostelium* MidA) is a **mitochondrial matrix protein arginine
methyltransferase** and an assembly factor for respiratory chain Complex I (NADH:ubiquinone
oxidoreductase). It is **not** a structural subunit of the mature holoenzyme.

- It is a SAM-dependent (7-β-strand / class I fold) protein methyltransferase that
  **symmetrically dimethylates Arg-85 of the core Complex I subunit NDUFS2**
  [PMID:24089531 "it is responsible for the methylation of residue Arg-85 in the NDUFS2 subunit of complex I"; PMID:24089531 "a that is responsible for the symmetrical dimethylation of Arg-85 of the NDUFS2 subunit of complex" (i.e. "...enzyme that is responsible for the symmetrical dimethylation of Arg-85...")].
- The methylation occurs early in assembly and stabilizes an early ~400-kDa peripheral-arm
  intermediate [PMID:24089531 "This methylation step occurs early in the assembly of complex I and"; PMID:24089531 abstract "probably stabilizes a 400-kDa subcomplex that forms the initial nucleus of the peripheral arm and its juncture with the membrane arm"].
- Loss of NDUFAF7 (siRNA / morpholino / germline KO) causes a **specific Complex I assembly
  defect** in human fibroblasts and zebrafish, and germline disruption of the mouse orthologue
  is embryonic-lethal [PMID:24838397 "Knockdown of NDUFAF7 by siRNA in human fibroblasts produced a specific complex I assembly defect, as did morpholino-mediated knockdown of the zebrafish ortholog. Germline disruption of the murine ortholog was an early embryonic lethal."].
- The G124V mutation, predicted to disrupt the methyltransferase motif, impairs assembly —
  linking the catalytic activity to the assembly function [PMID:24838397 "Expression of an NDUFAF7 mutant (G124V), predicted to disrupt methyltransferase activity, impaired complex I assembly"].

## Catalytic activity / EC

UniProt records **EC 2.1.1.320** and the RHEA reaction (RHEA:48108): L-arginyl-[protein] +
2 SAM = N(omega),N(omega)'-dimethyl-L-arginyl-[protein] + 2 SAH + 2 H+
[file:human/NDUFAF7/NDUFAF7-uniprot.txt "EC=2.1.1.320"]. The product is a **symmetric**
ω-N(G),N(G')-dimethylarginine, so the correct MF is GO:0035243
(protein-arginine omega-N symmetric methyltransferase activity), the term GOA already assigns
by IBA/IEA/IMP. OLS def of GO:0035243: "Catalysis of the addition of a second methyl group to
methylated peptidyl-arginine ... resulting in symmetrical peptidyl-N(omega),N'(omega)-dimethyled
arginine residues." NDUFAF7 is a type II (symmetric) arginine methyltransferase that adds both
methyls.

## Localization

- Mitochondrial matrix: confirmed directly. [PMID:24089531 "the presence of NDUFAF7 in the mitochondrial matrix has been confirmed"]. UniProt: "Mitochondrion" with a cleaved N-terminal transit peptide (residues 1–46) [file:human/NDUFAF7/NDUFAF7-uniprot.txt "TRANSIT ... Mitochondrion"].
- Multiple IDA/EXP/HTP mitochondrion annotations (PMID:20406883, 24089531, 24838397, 28837730,
  34800366) all agree — mitochondrion / mitochondrial matrix is well supported.
- **Extracellular region (GO:0005576, HDA, PMID:22664934)** derives from a tear-fluid
  proteomics survey (breast-cancer vs control); the cached full text does not mention NDUFAF7
  by name and this is an isolated high-throughput mass-spec detection in a secreted body fluid.
  Biologically implausible as a functional location for a matrix enzyme with a mitochondrial
  transit peptide; over-annotation.

## Interactions

- **NDUFS2** is the physiological substrate/interactor [PMID:20406883 "both proteins interact with the mitochondrial complex I subunit NDUFS2"; PMID:24089531 "interacts with the NDUFS2"]. UniProt SUBUNIT: "Interacts with NDUFS2". The GO:0019899 enzyme-binding IPI (PMID:20406883, with UniProtKB:O75306 = NDUFS2) captures this and is informative (substrate binding), so KEEP.
- **LRRK2** (Q5S007): NDUFAF7 recovered as an LRRK2 interactor in two interactome screens
  (PMID:24510904 LRRK2 screen; PMID:29513927 ROCO-protein interaction network). UniProt lists
  the IntAct interaction Q7L592–Q5S007. These are bare "protein binding" (GO:0005515) IPI
  annotations of unclear functional significance; not core function.

## Disease

- Heterozygous D266E is a candidate susceptibility variant for pathologic myopia; decreases
  Complex I activity and ATP [PMID:28837730 "The mutation D266E in NDUFAF7 impaired complex I activity, which resulted in decreased ATP levels in cultured cells."]. UniProt VARIANT 266 D->E. This is consistent with, and downstream of, the Complex I assembly function.

## Curation decisions (see -ai-review.yaml)

- **Core MF**: GO:0035243 protein-arginine omega-N symmetric methyltransferase activity
  (ACCEPT the IBA/IMP; IEA supported; MODIFY the vague NAS GO:0008168 methyltransferase activity
  up to the specific term).
- **Core BP**: GO:0032981 mitochondrial respiratory chain complex I assembly (ACCEPT).
- GO:0019918 peptidyl-arginine methylation to symmetric dimethyl-arginine (IMP) — ACCEPT
  (the specific protein-modification process; core, mechanistically upstream of assembly).
- Mitochondrion / mitochondrial matrix CC — ACCEPT (best experimental: matrix).
- GO:0005515 protein binding IPI (LRRK2 x2) — MARK_AS_OVER_ANNOTATED (uninformative; not core).
- GO:0019899 enzyme binding IPI (NDUFS2) — KEEP_AS_NON_CORE (informative substrate binding).
- GO:0008168 methyltransferase activity NAS — MODIFY to GO:0035243.
- GO:0005576 extracellular region HDA — MARK_AS_OVER_ANNOTATED (tear-fluid MS artifact).
- Reactome mitochondrial-matrix TAS x8 — ACCEPT (consistent with matrix localization; from the
  Complex I biogenesis pathway reactions).
</content>
</invoke>
