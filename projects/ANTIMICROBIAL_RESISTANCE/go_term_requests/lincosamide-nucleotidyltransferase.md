---
title: "GO term request: lincosamide nucleotidyltransferase activity"
---

# GO new term request (draft): lincosamide nucleotidyltransferase activity

Draft for the geneontology/go-ontology new-term-request template. **Not filed.** The CARD team reviewed the gap behind this request and said they would support it.

- **Label:** lincosamide nucleotidyltransferase activity
- **Definition:** Catalysis of the transfer of a nucleotidyl group (typically AMP) from a nucleoside triphosphate to a hydroxyl group of the methylthiolincosamide sugar of a lincosamide antibiotic such as lincomycin or clindamycin, with release of diphosphate.
- **Definition references:** PMID:10103201, PMID:20004168
- **Parent(s) (is_a):** GO:0016779 nucleotidyltransferase activity
- **Synonyms:** lincosamide adenylyltransferase activity (NARROW); lincomycin nucleotidyltransferase activity (NARROW)
- **Cross-references:** none found: no EC number and no Rhea reaction for lincosamide nucleotidylation (Rhea searched for lincomycin and clindamycin, 2026-11-27)
- **ARO terms that would map to it:** ARO:3000221 lincosamide nucleotidyltransferase (LNU)
- **Example gene products:** UniProtKB:Q9WVY4 (LinB, Enterococcus faecium (unreviewed)); UniProtKB:P06107 (LinA, Staphylococcus haemolyticus)

## References

- PMID:10103201 — A new resistance gene, linB, conferring resistance to lincosamides by nucleotidylation in Enterococcus faecium HM1025.
- PMID:20004168 — Structure and mechanism of the lincosamide antibiotic adenylyltransferase LinB.

## Notes

Lnu enzymes modify the 3- and/or 4-hydroxyl of the methylthiolincosamide sugar (ARO:3000221 definition); which position each subfamily uses should be stated per member, not in this term. Parent follows GO:0034068 aminoglycoside nucleotidyltransferase activity, which sits directly under GO:0016779. If GO prefers adenylyltransferase, use GO:0070566 adenylyltransferase activity as the parent and label 'lincosamide adenylyltransferase activity'. Because no Rhea reaction exists, the definition is in prose; a Rhea request could accompany this one.

All PMIDs, EC numbers and Rhea ids above were checked on 2026-11-27 (PubMed esummary titles; UniProt entries; Rhea search). GO ids were checked against the GO release used by `just validate-mappings`.
