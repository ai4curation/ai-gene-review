# CPTP notes

Manual notes for the CPTP/CERK GO-CAM review batch. Falcon and the requested
Perplexity fallback were not available in this checkout, so no provider
`CPTP-deep-research-*.md` artifact was created.

## Core function

GLTPD1/CPTP is the C1P-specific soluble carrier of the GLTP-fold family. The
discovery paper shows purified GLTPD1 transferring AV-C1P between POPC donor
and acceptor vesicles, with no transfer of glycolipids, sphingomyelin,
phosphatidylcholine, phosphatidic acid or ceramide [PMID:23863933, "Testing of
lipid specificity revealed no transfer of galactosylceramide"].

CPTP directly binds the C1P headgroup. Crystal structures placed the C1P
phosphate in a cationic surface cavity formed by K60, R106 and R110, and K60A or
R106L nearly abolished C1P transfer [PMID:23863933, "K60A and R106L showing
almost no C1P transfer"].

In cells, CPTP is a cytosolic protein that also associates with TGN/endosomal,
nuclear and plasma-membrane pools [PMID:23863933, "CPTP resides in the cell
cytosol but associates with the trans-Golgi network, nucleus and plasma
membrane"]. CPTP knockdown raised C1P in heavy membranes and nuclear fractions
and lowered it in plasma membranes [PMID:23863933, "decreased levels in plasma
membranes"], consistent with transfer away from the TGN toward the plasma
membrane and other acceptors.

Mishra et al. support real but secondary regulatory outcomes of C1P handling:
CPTP knockdown or C1P-binding mutants induce autophagy and increase
NLRP3-dependent IL1B/IL18 release [PMID:29164996, "via a NLRP3 (but not NLRC4)
inflammasome-based mechanism"]. These rows are kept as non-core because CPTP
does not assemble autophagosomes or inflammasomes directly.

## Curation decisions

The direct phospholipid-binding row is modified to `GO:1902387` ceramide
1-phosphate binding because the same paper resolved C1P in the binding pocket
and assayed binding-site mutants.

The two `GO:0035627` ceramide transport rows are not false: `GO:1902389`
ceramide 1-phosphate transport is a child of the broader ceramide-family
transport term. The broad PAINT and Reactome rows are marked `TOO_GENERAL`
because C1P transport captures CPTP specificity and because CPTP does not move
unphosphorylated ceramide.

The direct NOT `GO:0046836` glycolipid transport row is retained because the
2013 transfer assays explicitly separated CPTP from GLTP-family glycolipid
carriers.

Nuclear outer membrane and endosome membrane are kept as credible secondary
locations. The TGN membrane, plasma membrane and cytosol rows are core to the
GO-CAM route.

## GO-CAM consistency

GO-CAM `68b0f0d000008519` models CPTP with `GO:1902388` C1P transfer activity,
`GO:1902389` C1P transport and cytosolic occurrence. Those calls agree with the
accepted rows in this review, so no CPTP-side GO-CAM defect is apparent.
