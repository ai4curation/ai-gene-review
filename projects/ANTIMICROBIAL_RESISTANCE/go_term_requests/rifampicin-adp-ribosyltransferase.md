---
title: "GO term request: rifampicin ADP-ribosyltransferase activity"
---

# GO new term request (draft): rifampicin ADP-ribosyltransferase activity

Draft for the geneontology/go-ontology new-term-request template. **Not filed.** The CARD team reviewed the gap behind this request and said they would support it.

- **Label:** rifampicin ADP-ribosyltransferase activity
- **Definition:** Catalysis of the reaction: rifampicin + NAD+ = 23-O-(ADP-D-ribosyl)rifampicin + nicotinamide + H+, the transfer of a single ADP-ribose group from NAD+ to the 23-hydroxyl of a rifamycin antibiotic.
- **Definition references:** PMID:18349144, PMID:9869590
- **Parent(s) (is_a):** GO:0016763 pentosyltransferase activity
- **Synonyms:** rifampin ADP-ribosyltransferase activity (EXACT); rifamycin ADP-ribosyltransferase activity (BROAD); Arr activity (NARROW)
- **Cross-references:** no EC number found; no Rhea reaction found (Rhea searched for rifampicin, 2026-11-27: monooxygenase, phosphotransferase and transport reactions only)
- **ARO terms that would map to it:** ARO:3000390 rifampin ADP-ribosyltransferase (Arr)
- **Example gene products:** UniProtKB:I6NK65 (Arr-2, Klebsiella pneumoniae (unreviewed)); UniProtKB:D0E7L0 (Arr-2, Pseudomonas aeruginosa (unreviewed))

## References

- PMID:18349144 — Rifamycin antibiotic resistance by ADP-ribosylation: Structure and diversity of Arr.
- PMID:9869590 — ADP-ribosylation as an intermediate step in inactivation of rifampin by a mycobacterial gene.

## Notes

Mono-ADP-ribosylation of a small molecule. GO:0003950 NAD+ poly-ADP-ribosyltransferase activity (polymer) and GO:1990404 NAD+-protein mono-ADP-ribosyltransferase activity (protein acceptor) are both wrong for Arr. Parent follows GO:0003950, which sits under GO:0016763. The reaction equation should be checked by GO against a Rhea entry if one is created; we found none. No reviewed UniProt entry exists, so the examples are unreviewed.

All PMIDs, EC numbers and Rhea ids above were checked on 2026-11-27 (PubMed esummary titles; UniProt entries; Rhea search). GO ids were checked against the GO release used by `just validate-mappings`.
