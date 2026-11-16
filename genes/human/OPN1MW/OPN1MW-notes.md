# OPN1MW (P04001) review notes

## Identity and paralogs

- UniProt P04001 OPSG_HUMAN, medium-wave-sensitive (M, green) cone opsin, 364 aa, Lys-312
  retinylidene. Downstream of OPN1LW in the X-linked tandem array; the array often carries
  further M copies, which UniProt keeps as separate entries (OPN1MW2, OPN1MW3). All rows here
  are on P04001. Only the first two genes of the array are expressed
  [PMID:10319869 "the green-red hybrid gene will only cause deutan defects when it occupies the second position of the pigment gene array"].
- One row (ISS from P04000) transfers activity from the L opsin, which differs at 15 of 364
  residues [PMID:8185948]; that is merged paralog evidence and is said so on the row.

## What was assayed

- Pigment: human green opsin in COS-7 cells regenerates with 11-cis-retinal, lambda max 530 nm
  [PMID:12051694 "The normal red and green opsins showed absorbance spectra with lambda(max) of 560 and 530 nm, respectively"].
  Native human green cone outer segments 531 nm [PMID:6140680 "green cones, 530.8 +/- 3.5 nm"].
- Transducin activation and phosphorylation: PMID:15773913 used intact ground squirrel and pig
  retinas; "recombinant M opsin" activated G(t) and lost activity when phosphorylated. The
  abstract does not say which species the recombinant opsin was, so the IDA rows on the human
  protein rest on mammalian M opsin, probably non-human. Function is conserved; accepted.
- Dimer: human green opsin expressed in Sf9 cells, H/D exchange MS [PMID:28402104 "green cone opsin exists as a dimer in both dark (inactive) and bleached (active) states"].
- Disease: C203R in green genes with deuteranomaly [PMID:1302020]; N94K, R330Q deutan
  [PMID:12051694]; W177R in LW and MW genes misfolds and causes cone dystrophy XLCOD5
  [PMID:20579627].

## Decisions in brief

Same scheme as OPN1LW and RHO: MF GO:0008020 (GO:0004930, GO:0009881 MODIFY to it); BP
GO:0141190 (ancestors MODIFY); CC GO:0120201 cone photoreceptor disc membrane (plasma
membrane, membrane and disc membrane rows MODIFY to it; cone discs are continuous with the
plasma membrane). Visual perception and absorption of visible light ACCEPT; identical protein
binding KEEP_AS_NON_CORE; cytokinesis screen hit MARK_AS_OVER_ANNOTATED; protein binding none.
NEW GO:0005502 11-cis retinal binding. Agrees with GO-CAM gomodel:69ea894900003563 and the
visual_phototransduction module (GO:0008020).
