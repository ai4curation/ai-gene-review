# CLPX (O76031) — Gene Review Notes

Human gene CLPX, "ATP-dependent clpX-like chaperone, mitochondrial" (HGNC:2088). EC 3.6.4.10.
633 aa precursor with N-terminal mitochondrial transit peptide (1..56); mature chain 57..633.

## Core identity and function

CLPX is the regulatory AAA+ ATPase/unfoldase subunit of the mitochondrial-matrix ClpXP
protease. It uses ATP binding and hydrolysis to recognize, unfold, and translocate substrate
proteins into the proteolytic chamber of the CLPP peptidase for degradation (mitochondrial
protein quality control).

- AAA+ ClpX family; contains a ClpX-type zinc-binding domain (ZB, residues 93..146, Zn coordinated
  by C105/C108/C127/C130) and a P-loop AAA+ ATPase module (ATP binding 294..301). [UniProt O76031]
- "ATP-dependent chaperone that functions as an unfoldase. As part of the ClpXP protease complex,
  it recognizes specific protein substrates, unfolds them using energy derived from ATP hydrolysis,
  and then translocates them to the proteolytic subunit (CLPP) of the ClpXP complex for degradation"
  [UniProt O76031 FUNCTION; ECO:0000269|PubMed:11923310, 22710082, 28874591].
- Catalytic activity: ATP + H2O = ADP + phosphate + H(+); EC 3.6.4.10 [UniProt O76031;
  ECO:0000269|PubMed:22710082, PubMed:28874591].

## Quaternary structure / ClpXP complex

- CLPX forms a homohexameric ring; hexamerization requires ATP binding [UniProt O76031 SUBUNIT].
- ClpXP complex = two CLPP heptameric rings (a tetradecamer) flanked by a CLPX hexameric ring at
  each end — a symmetry-mismatched assembly. [PMID:11923310 "Complexes of a double heptameric ring
  of hClpP with hexameric hClpX rings bound on each side are stable in the presence of ATP..."].
- "hClpXP displays both ATP-dependent proteolytic activity and ATP- or ATPgammaS-dependent peptidase
  activity" [PMID:11923310]. Substrate selection is dependent solely on the Clp ATPase (CLPX), not CLPP
  [PMID:11923310 "substrate selection... is dependent solely on the Clp ATPase"].
- Isolated hClpP is a stable heptamer with no proteolytic activity; in the presence of ATP, hClpX
  binds and induces assembly into the active tetradecamer with protease and greatly increased
  peptidase activity [PMID:16115876 "hClpX must exert an allosteric effect on hClpP to promote a
  conformation that stabilizes the tetradecamer"; "The hClpXP complex has protease activity and
  greatly increased peptidase activity"]. This supports CLPX as a CLPP peptidase activator
  (GO:0016504 peptidase activator activity) and the contributes_to ATP-dependent peptidase activity.

## Substrate recognition (mechanism)

- A Walker B mutant (E359A) of human CLPX lacks ATPase activity but still mediates casein degradation
  by hCLPP, similar to the ClpP-activator ADEP; most model substrates recognized by the N-terminal
  domain, some dock directly to the pore-1 motif [PMID:22710082 "Although this mutant lacks ATPase
  activity, it retains the ability to mediate casein degradation by hCLPP... human CLPXP exhibits a
  similar mode of substrate recognition and is deregulated by ADEPs"]. E359A maps to UniProt MUTAGEN
  359 "E->A: Abolishes ATP hydrolysis" [UniProt O76031]. This paper supports IDA ATP hydrolysis
  activity and the part_of endopeptidase Clp complex; the ATP metabolic process annotation derived
  from the same paper is a generic transfer.

## Heme biosynthesis / ALAS regulation (CLPP-independent chaperone role)

- Mitochondrial ClpX activates δ-aminolevulinate synthase (ALAS), the first/rate-limiting enzyme of
  heme synthesis, by accelerating incorporation of the pyridoxal 5'-phosphate (PLP) cofactor
  [UniProt FUNCTION; PMID:25957689 (Kardon et al. 2015, "Mitochondrial ClpX activates a key enzyme for
  heme biosynthesis and erythropoiesis")]. UniProt: "Thanks to its chaperone activity, it also functions
  in the incorporation of the pyridoxal phosphate cofactor into 5-aminolevulinate synthase, thereby
  activating 5-aminolevulinate (ALA) synthesis, the first step in heme biosynthesis."
- CLPX also mediates heme-induced turnover of ALAS (degradation); the balance of activation vs.
  degradation tunes ALAS activity [PMID:28874591 "a model that integrates both mechanisms... acceleration
  of PLP cofactor incorporation (activation), and promotion of ALAS protein turnover (degradation)"].
- Dominant ATPase-active-site variant p.Gly298Asp (G298D) inactivates ATPase activity; mutant/WT
  coassembly yields reduced-activity enzyme, increasing ALAS protein stability, ALA and protoporphyrin
  IX (PPIX) accumulation → erythropoietic protoporphyria 2 (EPP2, MIM:618015)
  [PMID:28874591; UniProt VARIANT 298]. This PMID supports EXP ATP hydrolysis activity.

## Localization

- Mitochondrion (skeletal muscle and heart highest expression) [PMID:11003706 — cloning, mito transit
  peptide, transport into mitochondria; subcellular location and tissue specificity].
- Mitochondrial matrix [UniProt SUBCELLULAR LOCATION; PMID:10525407 (matrix localization of the human
  ClpP/Clp system; note this paper is primarily about hClpP, the partner peptidase)].
- Mitochondrion matrix / mitochondrion nucleoid; CLPX controls mtDNA nucleoid distribution by regulating
  TFAM activity, and interacts with TFAM [UniProt; PMID:22841477 (Kasashima et al. 2012, not in goa as a
  nucleoid CC source)]. The IDA nucleoid annotation in GOA derives from PMID:18063578, a nucleoid
  proteomics/cross-linking study (CLPX identified among nucleoid-associated proteins).
- The ISS mitochondrial inner-membrane annotation (GO_REF:0000024, from mouse Q9JHS4) is a peripheral/
  weak transfer; CLPX is a soluble matrix protein that can associate with the inner membrane indirectly
  (e.g., via the matrix face). Best treated as non-core.

## Notes on specific GOA annotations

- protein binding (GO:0005515, IPI) appears 3x (PMID:15522782, 11923310, 16115876), all reflecting the
  CLPX–CLPP interaction (WITH/FROM Q16740 = CLPP). Bare "protein binding" is uninformative; the specific
  function (peptidase activator / Clp complex assembly) is captured by GO:0016504 and the complex CC terms.
- GO:0009368 "endopeptidase Clp complex" and GO:0009841 "mitochondrial endopeptidase Clp complex":
  CLPX is genuinely part_of the mitochondrial ClpXP complex (ComplexPortal CPX-6177). The non-mitochondrial
  parent term GO:0009368 is less precise than GO:0009841 for human.
- GO:0006508 proteolysis / GO:0030163 protein catabolic process / GO:0051603 (obsolete) — CLPX participates
  in ClpXP-mediated proteolysis; protein catabolic process / quality control is core. proteolysis (GO:0006508)
  is acceptable but somewhat general.
- GO:0046034 ATP metabolic process (IDA, PMID:22710082) is a generic over-annotation derived from the ATPase
  assay; CLPX's biology is protein degradation, not ATP metabolism per se.
- GO:0006457 protein folding (IEA, InterPro) — ClpX is an unfoldase/chaperone, not a folding catalyst;
  the more specific GO:0140662 "ATP-dependent protein folding chaperone" is the appropriate MF and is also
  annotated. The bare BP "protein folding" is an InterPro transfer that mischaracterizes the unfoldase role.
- GO:0004176 ATP-dependent peptidase activity (contributes_to, PMID:16115876) — peptidase activity resides in
  CLPP; CLPX contributes by activating/assembling CLPP. contributes_to qualifier is appropriate.
