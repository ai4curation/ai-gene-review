# Group A: border-gene paralogs and signalling modulators — remap notes

The decisions are in `A_border_signalling.tsv`, 15 rows. The checker (`check_remap.py`) reports 0 errors.
Every paper is abstract-only in the cache except PMID:17409353, which has full text.

## Border-gene paralogs (Xenopus laevis)

**pax3-b (Q0IH87): 2 rows → NTR neural plate border formation + GO:0014034.**
This matches the reviewed homeolog pax3-a. Msx1 induces Pax3 at the border, and Pax3 then commits border cells to crest
[PMID:15691759 "Msx1 induces Pax3 and ZicR1 cell autonomously, in turn, Pax3 combined with ZicR1 activates Slug in a WNT-dependent manner"].
The full text also shows a requirement downstream of the border-inducing signals
[PMID:17409353 "Pax3 is required for both NC and HG formation downstream of NPB-inducing signals"].
The paper uses unsuffixed Pax3 MO, the same reagent as for pax3-a.

**hes4-b (Q90VV1): 3 rows → NTR neural crest progenitor maintenance.**
This matches hes4-a and id3-a. Hairy2 keeps progenitors undifferentiated
[PMID:18710660 "maintains cells in a mitotic undifferentiated pre-neural crest state"]
[PMID:18721802 "Hairy2 acts downstream of FGF and BMP signals at the neural border to maintain cells in an undifferentiated state"].
It is not a fate specifier, because early overexpression represses crest
[PMID:18721802 "Hairy2 overexpression represses neural crest and upregulates neural border genes at early stages"].
Murato 2007 is the homeolog-resolved paper, and it supports hairy2b, not hairy2a, as the crest-acting copy
[PMID:17724611 "Xhairy2b expression in the neural crest is much higher than Xhairy2a expression, consistent with the results of individual knockdown experiments"].
So the hes4-b row from that paper is the well-grounded one. The disputed NOT row on hes4-a is unchanged.

**zic2-a (Q91689, 2 rows), zic4 (A0JC51), zic5 (Q9IB89) → NTR neural plate border formation + GO:0014034.**
These match zic1.
- Zic2 acts as a pre-pattern factor that induces crest [PMID:9634234 "Zic2 is therefore a vertebrate pre-pattern gene, encoding anti-neurogenic and crest-inducing functions"].
- PMID:9739105 is the same paper as the zic1 row [PMID:9739105 "the Xenopus Zic family may act cooperatively in the initial phase of neural and neural crest development"].
- Zic4 is expressed at the border like Zic1 [PMID:16871625 "Zic4 expression was detected mainly in the neural plate border"].
- Zic5 is the most crest-specific of the family [PMID:11091076 "Zic5 expression converts cells from an epidermal fate to a neural crest cell fate"]. GO:0014034 is best supported here.

Caveat: Zic2 is expressed broadly in the ectoderm, and Zic4/Zic5 data are largely gain-of-function. Within the Zic family, the border role is best established for Zic1. Mapping the paralogs the same way is a consistency choice.

## Signalling modulators

**bmper (zebrafish; A6H8K2 and Q5D734, both from the same ZFIN row) → GO:1905297 positive regulation of neural crest cell fate specification + GO:0030513 positive regulation of BMP signaling pathway.**
Bmper/Cv2 increases BMP signalling locally and is needed for crest fate, as opposed to preplacodal fate
[PMID:24089471 "Crossveinless 2 functions at this time in a positive-feedback loop to locally enhance BMP activity, and show that it is required for neural crest fate"].
It modulates the inducing signal and does not build the border, so a regulation term fits.

**mdkb (zebrafish, Q9DDG2) → NTR neural plate border formation.**
The paper explicitly describes border establishment
[PMID:18058915 "Midkine-b (Mdkb), is responsible for establishment of the neural plate border in zebrafish"].
Knockdown loses both crest and Rohon-Beard neurons. That is a border-territory phenotype, not a crest-specific one, so GO:0014034 and GO:0014036 are not added.

**grem1 (Xenopus, O73754, IEP) → REMOVE.**
The evidence is expression only
[PMID:9660951 "a novel antagonist of bone morphogenetic protein (BMP) signaling that is expressed in the neural crest"].

**LRP6 (human, O75581, IDA) → GO:1905294 positive regulation of neural crest cell differentiation.**
LRP6 is a Wnt co-receptor, and overexpressing it in Xenopus induces crest
[PMID:11029007 "LRP6 activated Wnt-Fz signalling, and induced Wnt responsive genes, dorsal axis duplication and neural crest formation"].
A dominant-negative LRP6 blocks crest. The more specific GO:0044335 (canonical Wnt in crest differentiation) is obsolete. The human LRP6 review keeps the GO:0014029 row as non-core; this regulation term is consistent with that.

**Chrd (mouse, Q9Z0E2) → UNDECIDED.**
The paper is about vascular patterning. It mentions crest only as background
[PMID:17685487 "Genetic inactivation of Chordin, an inhibitor of the Bone Morphogenetic Protein signaling pathway, results in neural crest defects affecting heart and neck organs"].
Those defects are in crest derivatives (pharyngeal and cardiac), which suggests cardiac or pharyngeal crest terms (e.g. GO:0061308) rather than border or crest formation. The cached text is abstract-only, and the MGI curator may have used data in the full text, so this row needs curator input rather than removal.
