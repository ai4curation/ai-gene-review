# mraY (Q88N79, PP_1334) — Pseudomonas putida KT2440

## Identity
- UniProt: Q88N79 (MRAY_PSEPK), Reviewed/Swiss-Prot.
- Gene: mraY; OrderedLocusNames=PP_1334.
- Product: Phospho-N-acetylmuramoyl-pentapeptide-transferase; EC 2.7.8.13.
- AltName: UDP-MurNAc-pentapeptide phosphotransferase.
- 360 AA; integral membrane protein (10 predicted transmembrane helices).
- Evidence level PE 3 (inferred from homology); annotations largely UniRule/IEA (HAMAP-Rule:MF_00038).
- Family: glycosyltransferase 4 family, MraY subfamily [UniProt "Belongs to the glycosyltransferase 4 family. MraY subfamily."].

## FUNCTION
MraY catalyzes the first committed, lipid-linked (membrane) step of peptidoglycan
biosynthesis: transfer of the phospho-MurNAc-pentapeptide moiety from the soluble
nucleotide precursor UDP-MurNAc-pentapeptide onto the membrane lipid carrier
undecaprenyl phosphate (bactoprenyl phosphate), generating lipid I and releasing UMP.
[UniProt "Catalyzes the initial step of the lipid cycle reactions in the biosynthesis of the cell wall peptidoglycan: transfers peptidoglycan precursor phospho-MurNAc-pentapeptide from UDP-MurNAc-pentapeptide onto the lipid carrier undecaprenyl phosphate, yielding undecaprenyl-pyrophosphoryl-MurNAc-pentapeptide, known as lipid I."]

This is the committed entry point to the membrane-associated ("lipid cycle") stage of
PG synthesis; lipid I is subsequently converted to lipid II by MurG and flipped across
the inner membrane for transglycosylation/transpeptidation.

## CATALYTIC ACTIVITY
UDP-N-acetyl-alpha-D-muramoyl-L-alanyl-gamma-D-glutamyl-meso-2,6-diaminopimeloyl-D-alanyl-D-alanine
+ di-trans,octa-cis-undecaprenyl phosphate = di-trans,octa-cis-undecaprenyl diphospho-N-acetyl-
MurNAc-pentapeptide + UMP. EC=2.7.8.13; Rhea:RHEA:28386.
[UniProt "EC=2.7.8.13"] [UniProt "Xref=Rhea:RHEA:28386"]

## COFACTOR
Mg(2+)-dependent transferase. [UniProt "Name=Mg(2+); Xref=ChEBI:CHEBI:18420;"]
Note: "metal ion binding" (GO:0046872) and "magnesium ion binding" are broad relative to
the specific transferase activity; magnesium is a catalytic cofactor, not the core MF.

## PATHWAY
Cell wall biogenesis; peptidoglycan biosynthesis. [UniProt "PATHWAY: Cell wall biogenesis; peptidoglycan biosynthesis."]
UniPathway: UPA00219.

## SUBCELLULAR LOCATION
Cell inner membrane (plasma membrane); multi-pass / polytopic membrane protein.
[UniProt "SUBCELLULAR LOCATION: Cell inner membrane"] [UniProt "Multi-pass membrane protein"]
Ten predicted transmembrane helices (FT TRANSMEM 25..45 through 338..358).

## Annotation-review reasoning
- Core MF: GO:0008963 phospho-N-acetylmuramoyl-pentapeptide-transferase activity — ACCEPT (exact EC 2.7.8.13 reaction).
- GO:0051992 (the Rhea-mapped undecaprenyl-phosphate transferase activity, RHEA:28386) is the same reaction described at substrate level — ACCEPT as a precise (equivalent) MF.
- GO:0016780 phosphotransferase activity, for other substituted phosphate groups — broad parent of GO:0008963; MARK_AS_OVER_ANNOTATED.
- GO:0009252 peptidoglycan biosynthetic process — ACCEPT (core BP, matches PATHWAY).
- GO:0071555 cell wall organization — ACCEPT (broad but correct BP; UniProtKB-KW Cell wall biogenesis/degradation).
- GO:0044038 cell wall macromolecule biosynthetic process — correct but is a broad TreeGrafter parent; KEEP_AS_NON_CORE (peptidoglycan biosynthetic process is the precise term).
- GO:0005886 plasma membrane — ACCEPT (matches Cell inner membrane location).
- GO:0016020 membrane — broad parent of plasma membrane; MARK_AS_OVER_ANNOTATED.
- No "metal ion binding"/"magnesium ion binding" GO annotations are present in this GOA, only the Mg2+ KW/COFACTOR; no removal needed for those terms.

## References
- [PMID:12534463] Nelson et al. 2002, Environ Microbiol — KT2440 genome sequence (source of the sequence; no functional MraY characterization).
