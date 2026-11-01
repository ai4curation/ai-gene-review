# Lamp1 (mouse, UniProt P11438) - manual literature synthesis

No deep-research provider was available for this session. This file is a manual
synthesis from the cached publications in `publications/` and the UniProt record
(`Lamp1-uniprot.txt`). Each claim carries its provenance.

## Identity and structure

- Lamp1 encodes lysosome-associated membrane glycoprotein 1 (LAMP-1, CD107a, LGP-120),
  a single-pass type I membrane protein with a large, heavily N- and O-glycosylated
  luminal region made of two beta-prism subdomains separated by a proline-rich hinge,
  a single transmembrane helix and a short cytoplasmic tail carrying a
  lysosome-targeting tyrosine motif [file:mouse/Lamp1/Lamp1-uniprot.txt "TOPO_DOM 25..370 /note=\"Lumenal\""];
  [PMID:27663661 "we demonstrated that the subdomains of LAMP-1 and LAMP-2 adopt the unique β-prism fold"].
- LAMP-1 and LAMP-2 are "the most abundant protein components in lysosome membranes"
  [PMID:27663661]. Belongs to the LAMP family (PANTHER PTHR11506:SF27; Pfam PF01299).

## Localization

- Lysosomal and late endosomal limiting membrane; shuttles via the plasma membrane
  [file:mouse/Lamp1/Lamp1-uniprot.txt "This protein shuttles between lysosomes, endosomes, and the plasma membrane"].
- Used universally as a lysosome marker in mouse cells; dozens of MGI IDA annotations
  derive from marker use (e.g. [PMID:24841562 "LAMP1-positive late endosomes collapse to the perinuclear region upon Arl8b knockdown"];
  [PMID:26284655 "surrounded by membranes positive for the lysosomal marker protein Lamp1"]).
- Also on lysosome-related organelles: cytolytic granules of NK/CTL (appearing on the cell
  surface after degranulation) [PMID:23847195 "the lysosomal-associated membrane proteins (LAMPs) appear on the cell surface after CG exocytosis"],
  melanosomes [PMID:11266470 "punctate cytoplasmic structures which also contained the melanosome-resident proteins silver and LAMP-1"],
  phagolysosomes [PMID:23395172 "Hrg1 and Lamp1 protein strongly colocalized on the phagolysosomal membrane"],
  autolysosomes [PMID:26284655 "the vesicular structures positive for both Lamp1 and p62 represent autolysosomes"].

## Molecular function

- Direct inhibition of the lysosomal cation/proton channel TMEM175 (shown for human
  LAMP-1/LAMP-2): [PMID:37390818 "LAMP-1 and LAMP-2 directly interact with and inhibit the activity of the lysosomal cation channel TMEM175"];
  [PMID:37390818 "This LAMP inhibition mitigates the proton conduction of TMEM175 and facilitates lysosomal acidification to a lower pH environment crucial for optimal hydrolase activity"].
  The mouse protein carries this by similarity (UniProt FUNCTION, ECO:0000250 from P11279).
- Binds the TMD0 domain of the lysosomal peptide transporter TAPL/ABCB9 and stabilizes it
  against lysosomal degradation [PMID:22641697 "The interaction interface with LAMP was mapped to the four-transmembrane helices constituting the N-terminal domain of TAPL (TMD0)"];
  [PMID:22641697 "in LAMP-deficient cells, the half-life of TAPL is decreased by a factor of five"].

## Mouse genetics

- Lamp1-/- mice are viable and fertile with essentially normal lysosomes; LAMP-2 is
  upregulated [PMID:10212251 "LAMP-1-deficient mice are viable and fertile"];
  [PMID:10212251 "Lysosomal properties, such as enzyme activities, lysosomal pH, osmotic stability, density, shape, and subcellular distribution were not changed in comparison with controls"].
- Lamp1/Lamp2 double knockouts die at E14.5-16.5 with autophagic vacuole accumulation
  and cholesterol storage [PMID:15121881 "Taken together these findings indicate partially overlapping functions for LAMP-1 and -2 in lysosome biogenesis, autophagy, and cholesterol homeostasis"].
  Cholesterol storage is rescued by LAMP-2a but not LAMP-1 [PMID:15121881].

## Cytotoxic lymphocytes

- Surface CD107a protects NK cells from their own granule contents; Lamp1-/- mouse NK
  cells show increased degranulation-associated apoptosis
  [PMID:23847195 "deficiency of CD107a/LAMP-1 in mice resulted in increased NK cell apoptosis upon target cell-induced degranulation"].
- In human NK cells, LAMP1 is needed for perforin delivery to lytic granules and granule
  movement [PMID:23632890 "Reduction of LAMP1 expression affects the movement of lytic granules and results in decreased levels of perforin, but not granzyme B, in the granules"].

## Caveat on PMID:22147702

PMID:22147702 (alpha-TTP and chloroquine toxicity) uses an anti-rat LAMP-1 antibody as a
lysosomal marker in rat McARH7777 hepatoma cells [PMID:22147702 "Large vacuoles were stained by the antibody against LAMP-1, a major component of the lysosomal membrane"].
It contains no experiment on mouse Lamp1 function; it is background support for LAMP-1
as a lysosomal membrane marker only.
