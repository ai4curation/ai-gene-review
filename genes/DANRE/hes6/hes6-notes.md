# hes6 (Q6P0J1): evidence and exact-input prediction review

The three emitted GO predictions are biologically supported but broad. Direct zebrafish biochemistry establishes DNA binding by the Her7:Hes6 heterodimer, so a blanket claim that Hes6 cannot contribute to DNA binding would be wrong.

## Input identity and functional boundary

Q6P0J1 is zebrafish hes6/her13.2, a 226-residue product with bHLH and Orange domains. It is not her6 or her8a. The 2012 paper directly studies Hes6 alongside Her1 and Her7. The three generic protein-binding GOA rows have donors Her1/Q90463, Myod1/Q90477 and Her7/Q9I9K1 respectively; the separate identical-protein-binding row records Hes6 self-association. The primary paper includes MyoD as a promiscuous bHLH interaction comparison.

## Biological evidence

- [PMID:15905406 — Zebrafish hairy/enhancer of split protein links FGF signaling to cyclic gene expression in the periodic segmentation of somites.](https://pubmed.ncbi.nlm.nih.gov/15905406/): The primary reporter and interaction experiments establish transcriptional repression and Her1 association for Her13.2/Hes6.

> Her13.2 augments autorepression of her1 in association with Her1 protein.


> her13.2 is required for periodic repression of the
> Notch-regulated genes her1 and her7, and for proper somite segmentation.

- [PMID:16545363 — her1 and her13.2 are jointly required for somitic border specification along the entire axis of the fish embryo.](https://pubmed.ncbi.nlm.nih.gov/16545363/): The primary abstract explicitly reports combined Her1/Her13.2 loss-of-function effects on somitic borders.

> joint inactivation of her1 and her13.2 leads to a complete loss of all somitic
> borders

- [PMID:20637625 — Segment number and axial identity in a segmentation clock period mutant.](https://pubmed.ncbi.nlm.nih.gov/20637625/): The period-mutant study supports clock-dependent segment number; target identity is independently corroborated by the full 2018 report.

> precise control of segmentation
> clock period in relation to axial growth ensures a species-specific segment
> number


> arguing
> against an instructive role of the segmentation clock in determining axial
> identities.

- [PMID:22911291 — Topology and dynamics of the zebrafish segmentation clock core circuit.](https://pubmed.ncbi.nlm.nih.gov/22911291/): Direct zebrafish biochemistry establishes partner-dependent DNA binding by Hes6 in the Her7:Hes6 heterodimer.

> only Her1 homodimers and Her7:Hes6 heterodimers have strong DNA binding activity and target similar DNA sites.


> all of the possible dimers between Her1, Her7 and Hes6 form


> even the bHLH containing factor MyoD, but not the negative control non-bHLH protein PPARγ, was co-purified by Her1, Her7, and Hes6 to a similar extent

- [PMID:29624170 — Segmentation of the zebrafish axial skeleton relies on notochord sheath cells and not on the segmentation clock.](https://pubmed.ncbi.nlm.nih.gov/29624170/): The full primary report directly generates and analyzes a hes6 mutant; its focus on notochord-derived centra does not make the Hes6 annotation a wrong-gene citation.

> The novel hes6 mutation was created by injection of a TALEN targeted against hes6 in wild type.


> her1;hes6 mutants (n=15)

## Exact non-GO claims

The complete emitted record is preserved in [hes6-protnlm-source.json](hes6-protnlm-source.json). Assessments below address the selected protein product; evidence on longer products is identified explicitly.

### Protein name

> Uncharacterized protein

UNSCORED: “Uncharacterized protein” has no ProtNLM evidence tag in the returned name field. It is an API default rather than a scored biological hypothesis.

## Emitted GO claims

All 3 emitted GO claims are individually assessed in [hes6-protnlm-predictions-review.yaml](hes6-protnlm-predictions-review.yaml).

## Family integration

Hairy/HES-family domains support dimer formation, but individual homo- and heterodimers differ strongly in DNA binding and regulatory effect. In zebrafish, Her7:Hes6 is directly DNA-binding while Hes6 homodimers are not in the tested assays. Neither a universal DNA-binding grant to every dimer nor a blanket non-DNA-binding label for Hes6 is appropriate. Somitogenesis and neurogenesis also require lineage- and tissue-specific evidence.

## Evidence limits

Full text was read for the 2005, 2012 and 2018 target studies, including the interaction controls and hes6-mutant figure captions. The 2006 and 2010 cache entries are abstract-only, with target relevance corroborated by the full later reports. The genuine Falcon research synthesis identifies useful clock studies; the conclusions here are anchored to the experiments themselves. Neural function remains unresolved rather than rejected because mesoderm is the best-studied context.
