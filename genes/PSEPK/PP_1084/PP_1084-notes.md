# PP_1084 / tsaA annotation audit notes

## 2026-08-29 — qualifier-aware re-review

Reviewed `PP_1084-goa.tsv`, the UniProt Q88NW9 cache, both cached primary
publications, the Falcon research report, and the current
`projects/UNFOLDED_PROTEIN_BINDING.md` policy. The current GOA contains 13
qualifier-aware signatures: six `enables`, two `located_in`, and five
`involved_in`. Each is represented exactly once in the YAML. There are no IBA
annotations. Six IEA rows cite TreeGrafter node `PANTHER:PTN002242136`, but
these are TreeGrafter IEA annotations rather than PAINT IBA claims and therefore
do not receive an IBA propagation review.

The 13 current rows resolve to 6 ACCEPT, 4 KEEP_AS_NON_CORE, and 3
MARK_AS_OVER_ANNOTATED. The broad antioxidant activity, oxidoreductase activity,
and cellular response to stress rows are retained as over-annotations because
the current GOA already supplies the mechanistically specific peroxiredoxin,
thioredoxin peroxidase, hydrogen-peroxide catabolism, and oxidant-detoxification
terms. The self-interaction IPI is retained as non-core: the exact GOA
WITH/FROM is `UniProtKB:Q88NW9`, and UniProt records four IntAct self-interaction
experiments.

## Direct peroxidase/holdase evidence

PMID:21104173 is cached as full text, not abstract-only. Purified PpPrx reduced
H2O2 in a thioredoxin-coupled assay and directly suppressed thermal aggregation
of malate dehydrogenase and citrate synthase. The same paper explicitly reports
that foldase activity was not detected. It also found substantially greater
chaperone activity in the HMW fraction and greater peroxidase activity in the
LMW fraction [PMID:21104173, "PpPrx suppressed the thermal aggregation of the
model substrate MDH at 43°C in a concentration-dependent manner (Fig.2B). At a
subunit molar ratio of PpPrx to MDH of 0.5 vs. 1, MDH aggregation was completely
suppressed. PpPrx can also efficiently protect the thermal aggregation of CS
(Fig.2C), suggesting that PpPrx can indeed act as an efficient molecular
chaperone. However, foldase activity as another chaperone activity was not
detected (data not shown)."] [PMID:21104173, "The HMW complex fraction (F-1)
exhibited high chaperone activity about fivefold compare to LMW fraction (F-2)
and total protein fraction (Fig.3E), indicating that the chaperone activity of
PpPrx was significantly affected by the structural composition."]

PMID:26278368 is abstract-only. Its abstract independently supports that PpPrx
predominates as an HMW complex with chaperone activity and attributes the
PpPrx/PaPrx difference to the additional PpPrx cysteine, but assay-level claims
were anchored to the full-text 2011 study [PMID:26278368, "PpPrx predominates
with a high molecular weight (HMW) complex and chaperone activity, whereas PaPrx
has mainly low molecular weight (LMW) structures and peroxidase activity."]

## GO:0051082 and ontology gap

The author-supplied GO:0051082 claim is not one of the 13 current physical GOA
rows. It is retained machine-readably as a retired legacy claim and changed from
NEW to MODIFY toward an NTR. GO:0051082 is formally obsolete. Its two official
consider targets do not match the direct PpPrx evidence: GO:0044183 protein
folding chaperone is excluded by the reported absence of foldase activity, and
GO:0140309 has a carrier-specific definition requiring escort to an acceptor
molecule or location, which was not demonstrated. The directly supported
mechanism is aggregation prevention in situ. The review therefore uses
GO:0051082 only as an explicitly INTERIM core descriptor and proposes the
project-standard NTR, **holdase chaperone activity**, with the definition in
`projects/UNFOLDED_PROTEIN_BINDING.md` (see also go-ontology#30552 and
go-ontology#30962).

Evidence is sufficient to mark the one-gene review COMPLETE. Remaining
uncertainty concerns the in-vivo balance of HMW holdase and LMW peroxidase states
under physiological stress, not the existence of either biochemical activity.
