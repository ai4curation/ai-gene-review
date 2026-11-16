# OPN1SW (P03999) review notes

## Identity

- UniProt P03999 OPSB_HUMAN, short-wave-sensitive (S, blue) cone opsin, 345 aa, Lys-290 retinylidene, autosomal, 43% identical to the
  L/M pigments [PMID:2937147 "The red and green pigments show 96 percent mutual identity but only 43 percent identity with the blue pigment"].

## What was assayed

- Native human blue cone outer segments absorb at 419 nm [PMID:6140680 "blue cones, 419.0 +/- 3.6 nm"].
- Dominant missense variants cause tritanopia [PMID:1531728 "to detect in four of nine unrelated tritanopic subjects two different point mutations in the gene encoding the blue-sensitive opsin"].
- No cached paper assays transducin activation by the human S pigment. The GPCR activity rests
  on the opsin-clade IBA, an ISS from the human L opsin (P04000, a 43%-identity paralog) and the
  Reactome events; the GO-CAM gomodel:69ea894900003713 uses the same function.
- Skin papers (PMID:31380578 dermal fibroblasts, PMID:31730232 melanocytes, PMID:30168605
  skin IHC): mRNA by OPN1-SW primers, but protein by an "anti-OPN1" antibody that does not name
  the S pigment, no knockdown control; the studies are about OPN3. Rows from them (plasma
  membrane, perinuclear region, cellular response to UV-A) are weak; same view as the RHO review
  of the same two papers.
- PMID:9089077 (blue opsin gene sequences and evolution) is cited for TAS location and process
  rows it does not assay; PMID:2937147 is the cloning paper.

## Decisions in brief

As for OPN1LW, OPN1MW and RHO: MF GO:0008020 (GPCR activity, signaling receptor activity
MODIFY to it); BP GO:0141190 (ancestors MODIFY); CC GO:0120201 cone photoreceptor disc membrane
(plasma membrane, membrane, ciliary membrane and disc membrane rows MODIFY to it). Inner segment
KEEP_AS_NON_CORE (biosynthetic, as RHO). Perinuclear region UNDECIDED (abstract-only skin IHC).
UV-A response MARK_AS_OVER_ANNOTATED. NEW GO:0005502 11-cis retinal binding (Reactome TAS).
