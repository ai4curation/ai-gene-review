---
title: "GO term request: macrolide esterase activity"
---

# GO new term request (draft): macrolide esterase activity

Draft for the geneontology/go-ontology new-term-request template. **Not filed.** The CARD team reviewed the gap behind this request and said they would support it.

- **Label:** macrolide esterase activity
- **Definition:** Catalysis of the hydrolysis of the macrocyclic lactone (ester) bond of a macrolide antibiotic such as erythromycin, giving the ring-opened, inactive hydroxy acid.
- **Definition references:** PMID:22303981
- **Parent(s) (is_a):** GO:0052689 carboxylic ester hydrolase activity
- **Synonyms:** erythromycin esterase activity (NARROW); macrolide lactonase activity (EXACT)
- **Cross-references:** EC:3.1.1.- (UniProt P07684 EreA and P05789 EreB carry EC 3.1.1.-; no full EC number); no Rhea reaction found (Rhea searched for erythromycin, 2026-11-27)
- **ARO terms that would map to it:** ARO:3000320 macrolide esterase
- **Example gene products:** UniProtKB:P07684 (EreA, Escherichia coli); UniProtKB:P05789 (EreB, Escherichia coli)

## References

- PMID:22303981 — Mechanism and diversity of the erythromycin esterase family of enzymes.

## Notes

Ere enzymes open the macrolactone ring, inactivating 14- and 15-membered macrolides. An 'erythromycin esterase activity' child could be added if a substrate-specific term is wanted; the family-level term is the one the ARO family maps to.

All PMIDs, EC numbers and Rhea ids above were checked on 2026-11-27 (PubMed esummary titles; UniProt entries; Rhea search). GO ids were checked against the GO release used by `just validate-mappings`.
