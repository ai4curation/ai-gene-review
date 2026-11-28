---
title: "GO term request: rifampicin monooxygenase activity"
---

# GO new term request (draft): rifampicin monooxygenase activity

Draft for the geneontology/go-ontology new-term-request template. **Not filed.** The CARD team reviewed the gap behind this request and said they would support it.

- **Label:** rifampicin monooxygenase activity
- **Definition:** Catalysis of the reaction: rifampicin + NAD(P)H + O2 = rifampicin para-naphthoquinone carboxamide + NAD(P)+ + H2O + H+.
- **Definition references:** RHEA:58696, RHEA:58712, PMID:29398560
- **Parent(s) (is_a):** GO:0016709 oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
- **Synonyms:** RIFMO activity (EXACT); Rox activity (NARROW)
- **Cross-references:** EC:1.14.13.211; RHEA:58696 (NADPH); RHEA:58712 (NADH)
- **ARO terms that would map to it:** ARO:3000445 rifampin monooxygenase
- **Example gene products:** UniProtKB:Q5YTV5 (Rox, Nocardia farcinica); UniProtKB:F2R776 (Rox, Streptomyces venezuelae); UniProtKB:P95598 (Iri, Rhodococcus equi)

## References

- PMID:29398560 — Rox, a Rifamycin Resistance Enzyme with an Unprecedented Mechanism of Action.
- PMID:29578336 — Structural Evidence for Rifampicin Monooxygenase Inactivating Rifampicin by Cleaving Its Ansa-Bridge.
- PMID:19942945 — Monooxygenation of rifampicin catalyzed by the rox gene product of Nocardia farcinica: structure elucidation, gene identification and role in drug resistance.
- PMID:8980786 — Monooxygenase-like sequence of a Rhodococcus equi gene conferring increased resistance to rifampin by inactivating this antibiotic.

## Notes

Flavin-dependent monooxygenase that hydroxylates C2 of the naphthyl group and linearizes the ansa bridge. GO:0050264 rifamycin-B oxidase activity is a different (biosynthetic) reaction and GO:0004497 monooxygenase activity is too general. EC 1.14.13.211 has no GO term.

All PMIDs, EC numbers and Rhea ids above were checked on 2026-11-27 (PubMed esummary titles; UniProt entries; Rhea search). GO ids were checked against the GO release used by `just validate-mappings`.
