# EBP (Q15125) review notes

Deep-research provider (falcon) was OUT OF CREDITS (HTTP 402) at the time of review, so
no `EBP-deep-research-falcon.md` was generated. This review is grounded in the cached
UniProt record (`EBP-uniprot.txt`), the seeded GOA (`EBP-goa.tsv`), cached
`publications/PMID_*.md`, and cached `reactome/R-HSA-*.md`.

## Core biology

EBP = 3-beta-hydroxysteroid-Delta(8),Delta(7)-isomerase (sterol Delta8-Delta7 isomerase;
EC 5.3.3.5), historically identified as the emopamil-binding protein. It is a multi-pass
ER-membrane enzyme of the post-lanosterol cholesterol biosynthesis pathway.

- Catalyzes isomerisation of the Delta(8) double bond of sterol intermediates to Delta(7):
  zymostenol -> lathosterol (modified Kandutsch-Russell) and zymosterol ->
  cholesta-7,24-dien-3beta-ol (Bloch pathway).
  [PMID:8798407 "This endoplasmic reticulum-resident membrane protein catalyzes the conversion of delta8-sterols to their corresponding delta7-isomers"]
- Activity demonstrated by heterologous yeast complementation of erg2 deficiency and by
  Ala-scanning mutagenesis identifying catalytic residues (H77, E81, E123, T126, N194, W197).
  [PMID:9894009 "The human emopamil binding protein (hEBP) exhibits sterol Delta8-Delta7 isomerase activity (EC 5.3.3.5)"]
- 4 predicted transmembrane helices; EXPERA domain (PROSITE PS51751); EBP family.
- Localises to ER membrane and nuclear envelope; redistributes to cytoplasmic vesicles at
  mitosis. [PMID:10406945 "hSI and SR-BP-1 were associated with the endoplasmic reticulum and with the outer and inner membranes of the nuclear envelope"; "delocalized during the cell cycle at the mitosis step when the nuclear membranes disappeared"]

## Disease

- CDPX2 (X-linked dominant chondrodysplasia punctata / Conradi-Hunermann-Happle syndrome):
  loss of isomerase activity; accumulation of 8-dehydrocholesterol and 8(9)-cholestenol.
  [PMID:10391219 "defects in sterol-delta8-isomerase cause CDPX2 and suggest a role for sterols in bone development"]
  [PMID:10391218 delta8-delta7 sterol isomerase = Ebp mutated in tattered mouse / CDPX2]
- MEND syndrome (hypomorphic hemizygous male variants), from UniProt DISEASE.

## AEBS / ChEH (secondary/context activity)

EBP is a component of the microsomal antiestrogen binding site (AEBS), a hetero-oligomeric
complex with DHCR7, that carries cholesterol-5,6-epoxide hydrolase (ChEH) activity.
[PMID:20615952 "The AEBS, a hetero-oligomeric complex composed of 3beta-hydroxysterol-Delta8-Delta7-isomerase (D8D7I) and ... cholesterol-5,6-epoxide hydrolase (ChEH)"]
UniProt notes: "The precise role of each component of this complex has not been described yet."
So GO:0033963 cholesterol-5,6-oxide hydrolase activity is a genuine (complex-level, tamoxifen/AEBS)
activity but is not the isomerase's own core catalytic function -> KEEP_AS_NON_CORE.

## GO:0047750 cholestenol delta-isomerase activity

This is EC 5.3.3.5, exactly the enzyme's function (lathosterol <-> 5alpha-cholest-8-en-3beta-ol).
The three EXP annotations (PMID:8798407, 9894009, 12760743) plus the IEA(EC) all support this.
It is essentially synonymous/closely related to the C-8 sterol isomerase (GO:0000247) /
steroid Delta-isomerase (GO:0004769) grouping. ACCEPT.

## Protein-binding IPIs

GO:0005515 (x2, PMID:25910212, PMID:32296183) and GO:0042802 identical protein binding
(PMID:32296183, homodimer, consistent with UniProt Q15125-Q15125 IntAct self-interaction
and PMID:12760743 "Chemical cross-linking induced homodimerization of EBPL and EBP").
Bare "protein binding" IPIs from large-scale interactome screens are uninformative ->
MARK_AS_OVER_ANNOTATED per policy (do not REMOVE experimental IPIs). Identical protein
binding is corroborated by the documented homodimer, so ACCEPT (KEEP_AS_NON_CORE).

## Localization annotations

- ER / ER membrane: strongly supported (IDA PMID:10406945; IBA; UniProt). Core CC = ER membrane.
- nuclear envelope / nuclear membrane: supported by PMID:10406945 IDA -> KEEP_AS_NON_CORE.
- cytoplasmic vesicle: only during mitosis (PMID:10406945) -> KEEP_AS_NON_CORE.
- membrane (GO:0016020, IEA InterPro): correct but uninformative parent -> MARK_AS_OVER_ANNOTATED.

## Ossification / bone (GO:0043931 IMP PMID:10391219)

Downstream/indirect: the CDPX2 skeletal phenotype reflects the sterol defect, not a direct
role of EBP in ossification machinery. The paper says sterols play "a role ... in bone
development" -> KEEP_AS_NON_CORE (secondary developmental consequence).
