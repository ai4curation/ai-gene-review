# ffh evidence notes

## 2026-08-11

This first-pass review uses the exact KT2440 UniProt record and conserved SRP54
family/domain evidence. The record explicitly supports signal-sequence binding,
4.5S SRP RNA binding, GTPase activity, and participation in SRP-dependent
cotranslational targeting. The OpenScientist/Asta retrieval did not provide a
usable organism-specific primary study, so no direct KT2440 Ffh experiment is
claimed. Primary bacterial SRP literature should be added before advancing the
review beyond DRAFT.

Conserved bacterial evidence now anchors the family-level mechanism without
being presented as KT2440-specific. A kinetic study found that Ffh and FtsY
mutually stimulate one another's GTP hydrolysis and that 4.5S RNA accelerates
their association [PMID:11735405, "both Ffh and FtsY act as GTPase activating
proteins for one another"]. A separate bacterial study experimentally described
a minimal SRP composed of Ffh and a small SRP RNA and linked it to secretory
protein targeting [PMID:12949169, "the S. lividans SRP consists of Ffh, a
homologue of the mammalian SRP54 protein, and scRNA"]. Direct KT2440
essentiality and substrate-range evidence remain open.

## 2026-11-02

Re-reviewed for the bacterial SRP cotranslational targeting module and set to
COMPLETE. The Asta retrieval file returned no Ffh- or SRP-specific snippets
(its top hits concern unrelated Mycobacterium annotation), so it is not cited.
GO has renamed GO:0005048 to "signal sequence receptor activity"; labels were
updated. GO:0048500 and GO:1990904 rows are refined to the specific bacterial
complex GO:0048501 "signal recognition particle, plasma membrane targeting",
consistent with the new E. coli Ffh review (genes/ECOLI/ffh). The KT2440
cytoplasm row stays at cytoplasm because, unlike E. coli, no cytosolic-fraction
evidence exists for this strain. Experimental grounding for the conserved
mechanism comes from the E. coli ortholog (PMID:1331806, PMID:1701272,
PMID:7612669, PMID:11735405).

Provenance for the 2026-11-02 changes: the bacterial SRP is the Ffh/4.5S RNA
particle [PMID:1701272, "An antiserum to Ffh precipitated 4.5S RNA from E. coli
extracts"] that recognizes nascent signal sequences [PMID:1279430, "interacts
specifically with the signal sequence of a nascent secretory protein"], which
supports the plasma-membrane-targeting SRP term GO:0048501.
