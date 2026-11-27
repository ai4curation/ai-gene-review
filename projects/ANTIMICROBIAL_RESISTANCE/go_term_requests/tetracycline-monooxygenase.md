---
title: "GO term request: tetracycline 11a-monooxygenase activity"
---

# GO new term request (draft): tetracycline 11a-monooxygenase activity

Draft for the geneontology/go-ontology new-term-request template. **Not filed.** The CARD team reviewed the gap behind this request and said they would support it.

- **Label:** tetracycline 11a-monooxygenase activity
- **Definition:** Catalysis of the reaction: a tetracycline + NADPH + O2 + H+ = an 11a-hydroxytetracycline + NADP+ + H2O.
- **Definition references:** RHEA:61444, PMID:15452119
- **Parent(s) (is_a):** GO:0016709 oxidoreductase activity, acting on paired donors, with incorporation or reduction of molecular oxygen, NAD(P)H as one donor, and incorporation of one atom of oxygen
- **Synonyms:** tetracycline destructase activity (RELATED); TetX monooxygenase activity (NARROW)
- **Cross-references:** EC:1.14.13.231; RHEA:61444; RHEA:50004 (tetracycline); RHEA:61452 (oxytetracycline)
- **ARO terms that would map to it:** ARO:3000036 tetracycline inactivation enzyme; ARO:3000205 tet(X)
- **Example gene products:** UniProtKB:Q01911 (TetX, Bacteroides fragilis); UniProtKB:B1MM05 (MabTetX, Mycobacteroides abscessus)

## References

- PMID:15452119 — TetX is a flavin-dependent monooxygenase conferring resistance to tetracycline antibiotics.
- PMID:16128584 — Tigecycline is modified by the flavin-dependent monooxygenase TetX.
- PMID:21402075 — Structural basis for a new tetracycline resistance mechanism relying on the TetX monooxygenase.
- PMID:2644186 — Novel aerobic tetracycline resistance gene that chemically modifies tetracycline.

## Notes

FAD-dependent class A monooxygenase that hydroxylates C11a of tetracyclines (including tigecycline), destroying the antibiotic. Existing GO:0047670 anhydrotetracycline monooxygenase activity is the biosynthetic step (EC 1.14.13.38) and is not appropriate. EC 1.14.13.231 has no GO term (no GO dbxref to the EC or to the Rhea reactions). The general term covers the tetracycline and oxytetracycline Rhea reactions as children if wanted.

All PMIDs, EC numbers and Rhea ids above were checked on 2026-11-27 (PubMed esummary titles; UniProt entries; Rhea search). GO ids were checked against the GO release used by `just validate-mappings`.
