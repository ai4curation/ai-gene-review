# ftsY evidence notes

## 2026-08-11

This first-pass review uses the exact KT2440 UniProt record, the existing Falcon
retrieval, and conserved FtsY family/domain evidence. The membrane receptor,
SRP-binding, and reciprocal GTPase roles are conserved-family assignments; no
direct KT2440 FtsY experiment is claimed. Primary bacterial SRP literature and
organism-specific validation should be added before advancing the review beyond
DRAFT.

Primary cross-species bacterial evidence supports the conserved mechanism but
does not establish KT2440-specific behavior. Ffh and FtsY mutually stimulate
one another's GTP hydrolysis in the 4.5S-RNA-dependent targeting cycle
[PMID:11735405, "both Ffh and FtsY act as GTPase activating proteins for one
another"]. The abstract of a study characterizing a minimal bacterial SRP system
describes FtsY only by resemblance to the mammalian receptor; it does not report
a direct FtsY interaction experiment [PMID:12949169, "FtsY resembles the
mammalian SRP receptor"].

## 2026-11-02

Re-reviewed for the bacterial SRP cotranslational targeting module and set to
COMPLETE. Plasma membrane and membrane rows are refined to GO:0009898
cytoplasmic side of plasma membrane (HAMAP: peripheral membrane protein,
cytoplasmic side), matching the experimentally grounded E. coli FtsY review
(genes/ECOLI/ftsY), where in vivo imaging shows FtsY is almost exclusively
membrane-bound [PMID:19912622, "the vast majority of FtsY was localized to the
inner membrane"]. The cytoplasm row stays non-core.

## 2026-11-03

Phospholipid binding (GO:0005543), added to the E. coli FtsY review from direct
evidence [PMID:19414018, "both helices bind to negatively charged
phospholipids"], is not mirrored here. The KT2440 record has no curated
lipid-binding statement: its A-domain annotations are only MobiDB-lite disorder
and low-complexity regions. No family-level review establishes the lipid-binding
helices across PTHR43134:SF1. The A domain is weakly conserved
[PMID:18281057, "the weakly conserved N-terminal A-domain does not seem to be
essential"], so transfer from E. coli would be a sequence inference this review
cannot check.
