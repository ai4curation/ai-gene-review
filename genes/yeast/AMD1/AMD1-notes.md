# AMD1 (YML035C, UniProt P15274) notes

## Function
- AMP deaminase EC 3.5.4.6 "Reaction=AMP + H2O + H(+) = IMP + NH4(+)" [UniProt:P15274]; Zn cofactor by similarity.
- Cloning and mutant: "A yeast strain deficient in AMP deaminase activity was produced and shown to be deficient in AMP deaminase protein by Western blot analysis." [PMID:2690949]
- "AMP deaminase (AMPD) is such an interconversion enzyme that allows IMP synthesis from AMP." [PMID:19635936]; "a defect in AMP deaminase is associated with a severe GDP/GTP pool depletion" (in adenine medium) [PMID:19635936].
- Paralogs Yjl070c and Ybr284w lack AMP/adenosine/adenine deaminase activity; "the effect of YJL070c was dependent on the presence of Amd1p" [PMID:19635936].
- Adenylate pool contraction on glucose pulse: "Conversion of AXPs into inosine was facilitated by AMP deaminase, Amd1, and IMP-specific 5'-nucleotidase, Isn1." [PMID:20087341]

## Pathway / YeastCyc
- AMP-DEAMINASE-RXN in PWY3O-1, PWY3O-2220, PWY3O-285; YeastCyc lists EC 3.5.4.17 (adenosine-phosphate deaminase) as well as 3.5.4.6; only 3.5.4.6 is supported.
- Default cytosol compartment acceptable (cytoplasmic HDA).

## Decisions
- Core MF GO:0003876; BP GO:0032264 IMP salvage; cytosol.
- MODIFY 4 "guanine salvage" rows (GO:0006178 defined as forming guanine base) -> GO:0032264 IMP salvage; full text of PMID:19635936 read: Amd1 supplies IMP from adenine-derived AMP for GMP synthesis.
- MODIFY deaminase activity -> GO:0003876. REMOVE 4 protein binding rows (Yjl070c x3, Prp40 WW).
