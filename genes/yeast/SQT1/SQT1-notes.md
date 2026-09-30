# SQT1 notes

## 2026-09-29 re-review

SQT1 has no IBA rows in the current GOA export: every seeded annotation is either
an experimental IntAct or SGD assertion. The current local PANTHER family for the
UniProt family assignment, PTHR19857, contains P35184 in subfamily
PTHR19857:SF8. The current PAINT export for PTHR19857 has a
cytosol IBD at PTN008366535 seeded by SQT1, MDV1, and human AAMP, but no SQT1
IBA appears in the GOA rows under review, so there was no propagation row to
align.

The existing biology in the review remains sound: Sqt1 is best treated as the
dedicated carrier chaperone for Rpl10/uL16. Pausch et al. showed that Sqt1 is
one of the client-specific ribosomal-protein chaperones whose purification
selectively enriched its cognate RPL10 transcript, and that the Sqt1 WD-repeat
beta-propeller shields the N-terminal rRNA-binding residues of Rpl10 during
incorporation into pre-60S subunits
[PMID:26112308, "Affinity purification of four chaperones (Rrb1, Syo1, Sqt1 and Yar1) selectively enriched the mRNAs encoding their specific ribosomal protein clients (Rpl3, Rpl5, Rpl10 and Rps3)."].

The four GO:0005515 protein binding rows are all generic IPI imports from
IntAct, including a large inter-species screen and a high-throughput yeast
interactome. The relevant direct activity is not "protein binding" but
client-specific Rpl10 carrier chaperone activity; the GO:0051082 unfolded
protein binding row is already modified to GO:0140597 protein carrier
chaperone, so duplicating that replacement under each generic interaction would
not add useful signal. This re-review changed the four protein-binding rows
from legacy MARK_AS_OVER_ANNOTATED actions to REMOVE under the generic binding
policy.

The newer literature search found a 2023 primary paper that extends the same
Sqt1/Rpl10 carrier function to mature-ribosome repair after oxidative damage.
Yang et al. show that oxidized Rpl10 can be released by Sqt1 and then replaced,
in parallel with Tsr2-dependent release and replacement of oxidized Rps26
[PMID:37086725, "Oxidized Rps26 and Rpl10 are released from ribosomes by their chaperones, Tsr2 and Sqt1, and the damaged ribosomes are subsequently repaired with newly made proteins."]. A 2024 Annual Reviews article places this in the broader ribosome-repair literature and summarizes damaged eS26/uL16 release by Tsr2/Sqt1 in idle 80S ribosomes
[PMID:38724022, "To mitigate the harm from dysfunctional ribosomes, the damaged proteins are then selectively released from ribosomes via their chaperones Tsr2 and Sqt1, respectively, to allow for their relatively rapid turnover."].

The repair papers justify a peripheral GO:0034599 cellular response to oxidative
stress process annotation. Sqt1 is not just genetically required for oxidative
stress resistance as an upstream Rpl10 assembly factor: purified Sqt1 directly
releases oxidized Rpl10 from mature 60S particles, Sqt1 is recruited to
ribosomes after H2O2 treatment, oxidized Rpl10 persists in the Rpl10-binding
Sqt1_E315A mutant, and the mutant remains oxidant-sensitive even when its mild
slow-growth assembly phenotype is rescued with excess Rpl10
[PMID:37086725, "Oxidized Rps26 and Rpl10 are released from ribosomes by their
chaperones, Tsr2 and Sqt1, and the damaged ribosomes are subsequently repaired
with newly made proteins."]. This should stay out of the core function block's
`directly_involved_in` list, because the gene's principal role remains Rpl10
carrier chaperone activity during 60S assembly.
