# cav (HOAP; Q95RV2) curation notes

- [PMID:12510197 "caravaggio, a mutation in the HOAP-encoding gene, causes extensive telomere-telomere fusions in larval brain cells, indicating that HOAP is required for telomere capping"]; [PMID:12510197 "HOAP is specifically enriched at mitotic chromosome telomeres"].
- DNA binding: [PMID:11408576 "is shown to bind specific satellite sequences and the telomere-associated sequence in vitro"].
- HP1a binding: [PMID:12826664 "Here we show direct physical interactions between the HOAP protein and HP1 and specific ORC subunits"]; needs both HP1 hinge and chromoshadow, so no single domain-binding term fits -> protein binding rows removed.
- Telomere maintenance IMP (PMID:16203987) -> MODIFY to telomere capping, following mre11/rad50/nbs convention (Drosophila has no telomerase).
- Centromeric staining faint [PMID:12417578 "we see faint HOAP staining at the centromeres of the large autosomes"] -> non-core.
- GO:0042162 label "telomeric repeat DNA binding" fits poorly with sequence-independent binding to retrotransposon arrays; raised as a question.
- Review-bot round (PR #4475): terminin-membership MODIFY rows now quote sentences that name this subunit's complex (terminin composition), not Ver-only text.
- Review-bot round: GO:0042162 telomeric repeat DNA binding rows MODIFY to GO:0003691 double-stranded telomeric DNA binding (definition is sequence-agnostic: double-stranded telomere-associated DNA); core MF updated; parallels GO:0043047 for MTV subunits.
