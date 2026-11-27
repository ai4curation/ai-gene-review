# fabK (Streptococcus pneumoniae R6, UniProtKB:Q8DR17) — curation notes

Reviewed for `modules/type_ii_fatty_acid_synthesis.yaml`, where FabK is the
representative of the flavin-dependent enoyl-ACP reductase variant of the
enoyl-reduction step. Both primary papers are abstract-only in `publications/`,
so every quote comes from those abstracts.

## Why this entry needs a review at all

The UniProt entry for the R6 protein (locus *spr0379*) is unreviewed and carries
an automatically generated name, "Probable nitronate monooxygenase", whose only
evidence is an ARBA association rule, with a FUNCTION comment about propionate
3-nitronate detoxification from the same rule. Those lines are unvetted
predictions and are not cited as support anywhere in this review. The GOA rows
inherit the same reading: one IEA row for `GO:0018580` nitronate monooxygenase
activity from InterPro, and one IBA row for generic oxidoreductase activity. The
protein itself is a well-characterized enzyme with a different activity.

## What FabK does

FabK is the enoyl-ACP reductase that completes each elongation cycle of type II
fatty-acid synthesis in *S. pneumoniae*
[PMID:12487627 "The enoyl-(acyl-carrier protein) (ACP) reductase catalyses the last step in each cycle of fatty acid elongation in the type II fatty acid synthase systems."].
It is the organism's only such enzyme — the gene could not be deleted
[PMID:12487627 "We were unable to delete the fabK gene from Strep. pneumoniae, suggesting that this is the only enoyl-ACP reductase in this organism."] —
and it specifically requires NADH
[PMID:12487627 "FabK specifically required NADH and the protein activity was stimulated by ammonium ions."].
It is a flavoprotein with one FMN per subunit, identified by MS
[PMID:12487627 "The visible absorption spectrum of the purified protein indicated the presence of a flavin cofactor that was identified as FMN by MS, and was present in a 1:1 molar ratio with protein."],
and the 1.7 Å structure shows that FMN sits in the active site of a TIM barrel
[PMID:18305197 "Each subunit formed a triose phosphate isomerase (TIM) barrel structure, and flavin mononucleotide (FMN) was bound as a cofactor in the active site."].
An inhibitor binds competitively with respect to NADH
[PMID:18305197 "Lineweaver-Burk plots indicate that the inhibitor binds competitively with respect to NADH, and uncompetitively with respect to crotonoyl coenzyme A."].

This fold and cofactor are what make FabK a separate module variant rather than a
FabI orthologue: it is triclosan-resistant, and FabI/FabL are Rossmann-fold
Tyr-(Xaa)6-Lys enzymes with no flavin.

## Why the nitronate monooxygenase row is removed

The structure paper states directly that FabK resembles 2-nitropropane
dioxygenase
[PMID:18305197 "The overall structure was similar to the enoyl-ACP reductase (ER) of fungal fatty acid synthase and to 2-nitropropane dioxygenase (2-ND) from Pseudomonas aeruginosa"].
That shared FMN/TIM-barrel fold is why the NMO-family signature IPR004136
matches, and the InterPro2GO mapping then asserts nitronate monooxygenase
activity. The entry also matches IPR017569 (putative type-II enoyl-ACP
reductase) and the NCBIfam model TIGR03151, which is the correct family
assignment. No alkyl nitronate has been assayed for FabK, so this is a
fold-level transfer with nothing behind it, not a measured secondary activity
to weigh under the promiscuous-activity tiers — hence `REMOVE` plus a
`WRONG_TERM` source defect against InterPro (cause `OVER_PROPAGATION`,
confidence `PROBABLE`, since only InterPro can confirm how the mapping is
scoped).

The generic `GO:0016491` IBA row from PANTHER node PTN002844975 (PTHR32332,
seeded by *P. aeruginosa* Q9I4V0) is sound at its own level — the clade really is
FMN-dependent oxidoreductases — but it stops short of what is known for this
protein, so it is `MODIFY`ed to `GO:0004318`, a descendant. The
`propagation_review` records the node as `SUPPORTS_TRANSFER` with a
`GRANULARITY_MISMATCH`: nothing is wrong with the IBD placement, it simply cannot
be more specific in a family that mixes reductases and monooxygenases.

Two `NEW` rows were added, both for things the entry lacks and the literature
establishes directly on this protein: `GO:0010181` FMN binding (IDA) and
`GO:0006633` fatty acid biosynthetic process (IMP). The process term passes the
participation test without difficulty — FabK catalyses one of the pathway's
reactions, so this is not a case of annotating a substrate or a merely required
factor.

## A caution for the family

Marrakchi et al. also show that FabK-*related* flavoproteins of *S. aureus* and
*B. subtilis* are **not** enoyl-ACP reductases
[PMID:12487627 "However, the genes did not complement a fabI (Ts) mutant and the purified flavoproteins were unable to reduce enoyl-ACP in vitro and did not exhibit NAD(P)H oxidase activity, indicating they were not enoyl-ACP reductases."].
So FabK membership in this broad family must not be propagated as enoyl-ACP
reductase activity; the module keeps experimentally characterized accessions as
exemplars and does not use PANTHER's PTHR32332 grouping to delimit the variant.
A curated rule (`rules/curated/`) conditioning the IPR004136 → GO:0018580
mapping on absence of an IPR017569/TIGR03151 match would be the durable fix; it
is recorded here and as a suggested question rather than written in this change.
