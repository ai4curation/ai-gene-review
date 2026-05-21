# CASP1 (Sorghum bicolor) — Research Notes

UniProt: **C5YAP3** (CASP1_SORBI) — "Casparian strip membrane protein 1" / SbCASP1
Ordered locus: Sb06g033470 / SORBI_3006G273300 ; Chromosome 6 ; 229 aa
PANTHER: PTHR36488:SF11 ("CASP-LIKE PROTEIN" — the bona fide CASP subfamily, with CASP1-5/CASP1-6 type members)
Pfam: PF04535 (CASP_dom) ; InterPro: IPR006702 (CASP_dom), IPR006459 (CASP/CASPL)

## Summary / hypothesis under evaluation

SbCASP1 is a sorghum member of the CASP (CAsparian Strip membrane domain Protein)
family. CASPs are four-transmembrane-span MARVEL-domain plasma-membrane proteins. They
self-assemble into the Casparian Strip Membrane Domain (CSD), a stable, immobile
plasma-membrane scaffold in root endodermal cells. The CSD recruits and positions the
lignin-polymerization machinery (peroxidase PER64, the NADPH oxidase RBOHF, the
dirigent-like protein ESB1) that locally deposits the lignified Casparian strip — a
ring-like cell wall modification forming the root apoplastic diffusion barrier.

Direct experimental characterization (CASP1-CASP5) is in Arabidopsis; the rice ortholog
OsCASP1 is also characterized. SbCASP1 function is inferred by orthology (UniProt
"By similarity"), but the inference is strong: family-wide conservation of the four-TM
topology, the membrane-scaffold behaviour, and the Casparian-strip role in grasses.

## CASP family discovery and function

[PMID:21593871 "These 'CASPs' (Casparian strip membrane domain proteins) specifically
mark a membrane domain that predicts the formation of Casparian strips."] — Roppolo et al.
2011 Nature identified the CASP family (CASP1-5 in Arabidopsis) as the first molecular
factors establishing a plasma-membrane and extracellular diffusion barrier in plants.

[PMID:21593871 "CASP1 displays numerous features required for a constituent of a plant
junctional complex: it forms complexes with other CASPs; it becomes immobile upon
localization; and it sediments like a large polymer."] — CASP1 behaves as a membrane
scaffold: forms homo/hetero-complexes, becomes immobile, sediments as a large polymer.

[PMID:21593871 "CASP double mutants display disorganized Casparian strips, demonstrating
a role for CASPs in structuring and localizing this cell wall modification."] — Genetic
loss of function: casp1 casp3 double mutants have disorganized Casparian strips. This is
the key evidence that CASPs *organize* a specific cell wall structure.

[PMID:24920445 "CASPARIAN STRIP MEMBRANE DOMAIN PROTEINS (CASPs) are four-membrane-span
proteins that mediate the deposition of Casparian strips in the endodermis by recruiting
the lignin polymerization machinery."] — Roppolo et al. 2014 Plant Physiol. CASPs are
4-TM proteins; they mediate Casparian strip deposition by recruiting the lignin
polymerization machinery.

[PMID:24920445 "CASPs show high stability in their membrane domain, which presents all
the hallmarks of a membrane scaffold."] — The CASP membrane domain is a stable scaffold.

[PMID:24920445 "CASPLs were found in all major divisions of land plants as well as in
green algae; homologs outside of the plant kingdom were identified as members of the
MARVEL protein family."] — The broader CASP-like (CASPL) family is pan-plant and even in
green algae; outside plants the homologs are MARVEL-domain proteins. This places CASP in
the MARVEL tetraspan superfamily.

[PMID:24920445 "The CASP first extracellular loop was found conserved in euphyllophytes
but absent in plants lacking Casparian strips."] — The first extracellular loop is
conserved specifically in euphyllophytes (which have Casparian strips). This is an
evolutionary correlate of Casparian-strip-forming capacity, relevant to the bona-fide
CASP subfamily (SF11) that SbCASP1 belongs to.

## The lignin-polymerization machinery recruited by CASPs

[PMID:23940370 "Casparian strips span the cell wall of adjacent endodermal cells to form
a tight junction that blocks extracellular diffusion across the endodermis. This junction
is composed of lignin that is polymerized by oxidative coupling of monolignols through
the action of a NADPH oxidase and peroxidases. Casparian strip domain proteins (CASPs)
correctly position this biosynthetic machinery by forming a protein scaffold in the
plasma membrane at the site where the Casparian strip forms."] — Hosmani et al. 2013
PNAS: the Casparian strip is lignin; CASPs position the lignin-biosynthetic machinery
(NADPH oxidase + peroxidases). ESB1 (dirigent-like) is part of this machinery and is
localized to the Casparian strip in a CASP-dependent manner.

[PMID:26124109 "Casparian strip formation is initiated by the localization of the
Casparian strip domain proteins (CASPs) in the plasma membrane, at the site where the
Casparian strip will form. Localized CASPs recruit Peroxidase 64 (PER64), a Respiratory
Burst Oxidase Homolog F, and Enhanced Suberin 1 (ESB1), a dirigent-like protein, to
assemble the lignin polymerization machinery."] — Kamiya et al. 2015 PNAS: explicit list
of recruited components (PER64 peroxidase, RBOHF NADPH oxidase, ESB1 dirigent). The
transcription factor MYB36 directly regulates CASP1, PER64 and ESB1.

## The Casparian strip and the endodermal diffusion barrier

[PMID:21735349 "A differentiated endodermal cell can be defined by the presence of the
'Casparian strip' (CS), a cell wall modification described first by Robert Caspary in
1865."] — Alassimone et al. 2011 review: the Casparian strip is the defining cell wall
modification of the differentiated endodermis.

[PMID:21735349 "free diffusion via the apoplast in vascular plants is blocked at the
level of the endodermis ... The recent isolation of a novel protein family, the CASPs,
that localizes precisely to a domain of the plasma membrane underneath the CS"] — CASPs
localize to a plasma-membrane domain directly underneath the Casparian strip; the
endodermis blocks apoplastic diffusion.

[PMID:21593871 "Its defining features are the Casparian strips, belts of specialized cell
wall material that generate an extracellular diffusion barrier."] — Casparian strips are
belts/rings of specialized cell wall material forming the apoplastic diffusion barrier.

The Casparian strip GO cellular-component term is **GO:0048226** "Casparian strip"
(a cellular anatomical structure). The biological-process term **GO:0160073**
"Casparian strip assembly" exists ("The aggregation, arrangement and bonding together of
a set of components to form a Casparian strip") — this is the precise process term for
what CASP proteins do.

## CASP conservation in grasses / sorghum

The PANTHER family PTHR36488 has 6602 members across 1073 taxa, all land plants/algae.
The bona-fide CASP subfamily SF11 ("CASP-LIKE PROTEIN") includes named Casparian strip
membrane proteins from rice, grape, sorghum, etc. SbCASP1 (C5YAP3, Sb06g033470) is in
SF11. Sorghum has multiple SF11 members: SbCASP1 (C5YAP3) and SbCASP2 (C5YLC9,
Sb07g000300), plus CASP4 (C5Y9U6) in the broader CASP-like SF12, mirroring the
Arabidopsis CASP1-5 / rice OsCASP1-2 expansion.

[PMID:24920445 GENE FAMILY / NOMENCLATURE — cited in the SbCASP1 UniProt entry as the
reference for the CASP family and SbCASP1 nomenclature] — Roppolo et al. 2014 is the
phylogenetic/nomenclature study that named CASP-family members across plant genomes,
including the sorghum SbCASP genes.

### Direct grass evidence — rice OsCASP1

[PMID:36600916 "Casparian strip membrane domain proteins (CASPs) form a transmembrane
scaffold to recruit lignin biosynthetic enzymes for Casparian strip (CS) formation."] —
Yang et al. 2022: the CASP scaffold-and-recruit mechanism holds in rice (a grass /
Poaceae, like sorghum).

[PMID:36600916 "Rice CASP1 is highly similar to AtCASPs ... The loss of OsCASP1 function
alters the expression of the genes involved in suberin biosynthesis and the deposition of
suberin in the endodermis and sclerenchyma and leads to delayed CS formation and uneven
lignin deposition in SLRs."] — OsCASP1 loss-of-function delays Casparian strip formation
and causes uneven lignin deposition; functional CASP role is conserved in grasses.

[PMID:36600916 "Our findings suggest that OsCASP1 could play an important role in
nutrient homeostasis and adaptation to the growth environment."] — Grass CASP1
contributes to nutrient homeostasis via the endodermal barrier.

[PMID:37653341 "A plant-type tight junction, the Casparian strip (CS)-Casparian strip
membrane domain (CSD) that seals the paracellular space between adjacent endodermal
cells ... The GAPLESS protein forms a tight complex with OsCASP1 in the plasma membrane,
thereby mediating the CS-CSD junction."] — Song et al. 2023 Nat Plants: in rice, OsCASP1
is a core component of the CS-CSD junctional complex; a new GAPLESS protein family
tethers the plasma membrane to the Casparian strip via OsCASP1. Confirms OsCASP1 is the
grass CASP scaffold protein and that the CSD/Casparian-strip tight-junction biology is
conserved in Poaceae.

## Assessment of the retired SPKW annotation (GO:0071555 cell wall organization)

The retired SwissProt-keyword-derived annotation maps the UniProt keyword
"Cell wall biogenesis/degradation" (KW-0961, present in the SbCASP1 entry) to
GO:0071555 "cell wall organization".

This is **biologically correct and informative**: CASP proteins organize the formation of
a specific, localized cell wall structure (the lignified Casparian strip). The UniProt
FUNCTION text for SbCASP1 itself states it "Regulates membrane-cell wall junctions and
localized cell wall deposition" and is "Required for ... the subsequent formation of
Casparian strips, a cell wall modification of the root endodermis". Experimentally,
Arabidopsis casp double mutants have "disorganized Casparian strips" [PMID:21593871] —
i.e. loss of CASP disrupts cell wall organization. So GO:0071555 captures genuine biology
and GOA's removal of this SPKW annotation is a **loss of correct information**.

However, GO:0071555 is broad. A **more specific and more accurate** term is available:
- **GO:0160073 "Casparian strip assembly"** — exact process; precise MODIFY target.
- GO:0009664 "plant-type cell wall organization" — also more specific (cellulose/pectin
  plant cell wall) and a child of GO:0071555.

Recommended action for the retired SPKW annotation: **MODIFY** to GO:0160073 (Casparian
strip assembly), retaining `retired: true`. GOA's *removal* was not the ideal outcome —
the keyword carried real, plant-specific biology — but the original broad term GO:0071555
was suboptimal; the correct response is to replace it with the specific term, not delete
the biology. This gene exemplifies the "unique-but-correct, informative, plant-specific"
category of SPKW annotations.

## Subcellular location (GO:0005886 plasma membrane)

UniProt SUBCELLULAR LOCATION: "Cell membrane; Multi-pass membrane protein. Note=Very
restricted localization following a belt shape within the plasma membrane which coincides
with the position of the Casparian strip membrane domain in the root endodermis." The
four predicted TRANSMEM helices (FT 68-88, 116-136, 158-178, 206-226) confirm a tetraspan
plasma-membrane protein. CASP1 in Arabidopsis localizes to the plasma membrane (the CSD)
[PMID:21593871]. GO:0005886 "plasma membrane" is correct but generic; a more precise term
is GO:1990877 "Casparian strip" / the CSD-specific component — see below.

OLS check: GO:0048226 "Casparian strip" is a cellular_component (cellular anatomical
structure). There is no separate GO CC term for the "Casparian strip membrane domain"
distinct from the plasma membrane; the CSD is a plasma-membrane subdomain. GO:0005886
plasma membrane is therefore the appropriate (if generic) CC; ACCEPT.
