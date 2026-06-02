# LAMP1 review notes

## Core function

LAMP1 encodes a heavily glycosylated type I lysosomal membrane glycoprotein.
UniProt describes the protein as a lysosome, endosome, late endosome, cell
membrane, and cytolytic granule membrane protein that shuttles through the
endolysosomal/secretory-lysosome system [file:human/LAMP1/LAMP1-uniprot.txt].
The most informative current molecular function is regulation of lysosomal pH:
LAMP1 and LAMP2 directly interact with TMEM175 and inhibit TMEM175 cation/proton
channel activity, which facilitates lysosomal acidification and hydrolase
activity [PMID:37390818 "LAMP-1 and LAMP-2 directly interact with and inhibit the activity of the lysosomal cation channel TMEM175"].

The core GO interpretation should therefore keep `GO:0005765 lysosomal membrane`
as the primary location, accept `GO:0007042 lysosomal lumen acidification`, and
accept `GO:0008200 ion channel inhibitor activity` as the best available broad
MF term for the TMEM175 inhibition mechanism. The local GO cache does not contain
a more specific proton-channel or TMEM175-channel inhibitor term.

## Proteostasis network context

The Proteostasis Network places LAMP1 under
`Autophagy-Lysosome Pathway|Autophagic lysosome reformation|Regulation of autolysosome morphology`.
The node is marked `no_mapping`, so PN membership alone is not evidence for a GO
annotation. The workbook note says LAMP1 recruits clathrin to tubules during ALR,
but the locally cached Rong et al. ALR abstract supports clathrin and PI(4,5)P2
as central ALR components without providing a LAMP1-specific statement
[PMID:22885770 "clathrin and phosphatidylinositol-4,5-bisphosphate ... regulate ALR"].
I am therefore not adding a new ALR/lysosome-organization annotation from the PN
row alone. Expert follow-up should ask whether the LAMP1-specific clathrin
recruitment evidence is in figures or supplemental material that should support
a future annotation.

## Secondary functions and contexts

LAMP1 has a non-core but well-supported role in cytotoxic lymphocyte secretory
lysosomes. LAMP1 RNAi in NK cells reduces cytotoxicity, disturbs lytic-granule
movement, and reduces perforin delivery to lytic granules [PMID:23632890
"LAMP1 silencing causes inhibition of NK-cell cytotoxicity"]. Surface LAMP1 also
protects NK cells from degranulation-associated self-damage by reducing perforin
binding [PMID:23847195 "Surface CD107a/LAMP-1 protects natural killer cells from degranulation-associated damage"].
These support NK-cell and cytolytic-granule annotations, but they are not the
general core function of LAMP1.

LAMP1 also stabilizes the lysosomal polypeptide transporter TAPL/ABCB9. The TAPL
paper reports LAMP1/LAMP2 as abundant TAPL interactors and shows that TAPL
half-life is reduced in LAMP-deficient cells [PMID:22641697 "LAMP proteins retain TAPL on the limiting membrane of endosomes"].
This supports protein stabilization as a secondary process, while generic
enzyme/protein-binding annotations are not informative.

LAMP1 is a host factor/receptor for Lassa virus entry in acidic endolysosomal
compartments; this is a valid host-pathogen context but not a normal human core
function [PMID:24970085 "Lassa virus ... involved a pH-dependent switch to ... LAMP1"].

## Annotation decisions

- Accept lysosomal membrane, endosome membrane, and late endosome membrane as the
  core membrane locations; modify broader lysosome/endosome/membrane terms to
  those more specific membrane terms.
- Keep plasma membrane, cell surface, cytolytic granule membrane, azurophil
  granule membrane, ficolin-1-rich granule membrane, extracellular exosome, and
  other trafficking/localization terms as non-core contexts.
- Remove cytosol/cytoplasm annotations because LAMP1 is an integral membrane
  protein; the cytosolic tail does not justify annotating the whole protein to
  cytosol.
- Accept lysosomal lumen acidification and ion channel inhibitor activity as core
  TMEM175-dependent functions.
- Modify broad protein binding to more informative terms where possible:
  TMEM175 binding to ion channel inhibitor activity, Lassa virus binding to virus
  receptor activity, and ABCB9/TAPL binding to protein stabilization.
- Keep NK-cell degranulation/cytotoxicity and perforin transport terms as
  non-core, cell-type-specific functions.

## Deep research provenance

Falcon deep research was started with `just deep-research-falcon human LAMP1`.
The provider timed out after 600 seconds and no `LAMP1-deep-research-falcon.md`
file was generated in the gene folder. This review therefore relies on cached
GOA/UniProt, cached publications, PN mappings, and these notes.
