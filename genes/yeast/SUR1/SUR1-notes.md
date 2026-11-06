# SUR1 (CSG1/BCL21; YPL057C, P33300) notes

## Identity and activity
- GT32 (OCH1-like) glycosyltransferase; catalytic subunit of IPC mannosyltransferase, IPC + GDP-Man -> MIPC (EC 2.4.1.370) [UniProt:P33300] [PMID:9323360 "Like CSG2, SUR1/CSG1 is required for IPC mannosylation."].
- Similarity to OCH1 [PMID:9323360 "A 93-amino acid stretch of Csg1p shows 29% identity with the alpha-1, 6-mannosyltransferase encoded by OCH1."].
- Redundant paralog CSH1 (YBR161W) with different substrate specificity; csg1 csh1 double mutant has no mannosylated sphingolipids [PMID:12954640 "Deltacsg1 cells exhibited only a reduction in the synthesis of mannosylated sphingolipids compared with wild-type cells, whereas the Deltacsg1 Deltacsh1 double deletion mutant exhibited a total loss."].
- Two complexes with regulatory subunit Csg2 [PMID:12954640 "These results suggested that two distinct inositol phosphorylceramide mannosyltransferase complexes, Csg1p-Csg2p and Csh1p-Csg2p, exist."].

## Location
- UniProt: membrane, multi-pass (ECO:0000305). GOA: Golgi (NAS, PMID:12954640); vacuole/vacuolar membrane only from HTP datasets (PMID:26928762, PMID:19001347).

## Curation decisions
- PTHR32385 PAINT places `GO:0000030 mannosyltransferase activity` and `GO:0051999 mannosyl-inositol phosphorylceramide biosynthetic process` on `PANTHER:PTN001285482`, the fungal IPC mannosyltransferase node seeded by SGD `SUR1`/`CSH1`, the three S. pombe `imt` paralogs, the CGD Candida seed, and A. fumigatus `Q4WDG6`.
- The 2022 N-glycan paper is newer direct S. cerevisiae family context: Sur1 carries an N-glycan on Asn224 that helps determine the activity toward specific MIPC subtypes [PMID:35713525 "Sur1 N224Q and Csh1 N51Q mutants exhibited a decrease in the activity to synthesize specific MIPC subtypes for each enzyme, suggesting that these N-glycans play a role in substrate recognition through their catalytic domains."].
- Protein binding (IPI with CSG2) removed as uninformative; captured by mannosyltransferase complex (GO:0031501).
- `GO:0006688 glycosphingolipid biosynthetic process` and `GO:0030148 sphingolipid biosynthetic process` are true but broad parents of the exact MIPC biosynthesis step, so the review modifies them to `GO:0051999`.
- `GO:0006676 M(IP)2C metabolic process` is over-annotated: Sur1 makes MIPC, the precursor that Ipt1 converts to M(IP)2C, but Sur1 does not catalyze the M(IP)2C-forming step.
- Module note: SUR1 and CSH1 are paralogous catalytic subunits, both requiring CSG2; YeastPathways reaction (IPC + GDP-Man -> MIPC) is correct.
