# apt curation notes

## 2026-08-13 first-pass review

The reviewed UniProt entry assigns Apt to the one-step adenine salvage reaction,
forming AMP from adenine and PRPP [UniProtKB:Q88F33, "Catalyzes a salvage
reaction resulting in the formation of AMP"]. The assignment is computational
(HAMAP MF_00004 and Rhea 16609), not a direct assay of the KT2440 protein.

The two localization rows are retained as non-core context. They are not copied
to the module because cytoplasm/cytosol adds no step-defining information. The
PANTHER family is PTHR11776, and the current PSEPK protein is in PTHR11776:SF7;
the exact UniProt exemplar is required because that subfamily's display label is
generic.
