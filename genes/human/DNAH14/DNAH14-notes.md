# DNAH14 notes

## Identity
- UniProt Q0VDD8; canonical isoform 3507 aa with AAA modules, MT stalk (Pfam PF12777) and C-terminal domain; no Pfam DHC_N2 stem, unlike DNAH3 [file:human/DNAH14/DNAH14-uniprot.txt]. Mouse Dnah14 models are ~4500 aa (A0A571BGC3, 4596 aa), so the human canonical sequence may be N-terminally incomplete.
- Not among the IDA heavy chains assigned in human respiratory axonemes [PMID:37258679: IDAa DNAH12, IDAb/e DNAH7, IDAc DNAH3, IDAd DNAH1, IDAf DNAH2/DNAH10, IDAg DNAH6].

## Function (single study)
- [PMID:41686705 "DNAH14 was specifically localized to the midpiece of both human and mouse sperm."]
- [PMID:41686705 "Dnah14 KO mice exhibited subfertility, characterized by reduced sperm motility, sperm mitochondrial sheath anomaly, annulus mislocalization, and midpiece bending, whereas ciliogenesis in non-reproductive tissues remained unaffected."]
- Offspring of KO males: reduced survival and growth [PMID:41686705].

## Neurodevelopment (candidate, unresolved)
- Three NDD patients with compound heterozygous variants [PMID:35438214]; siblings with homozygous truncating variant plus FXN expansions [PMID:41596228].

## Curation decisions
- Dynein complex kept at general level (arm unknown). Motor activity accepted as predicted (full motor region incl. MT-binding stalk).
- Intermediate/light intermediate chain binding UNDECIDED (no data; IBDs seeded by cytoplasmic dynein).
- Axoneme (UniProt ECO:0000305) kept as non-core; NEW sperm midpiece IDA from PMID:41686705.

## PANTHER / IBA check
- Human Q0VDD8 and mouse A0A571BGC3 have identical IBA sets (6 terms) in QuickGO; no family split.

## Deep research
- Falcon deep research failed (Edison API authentication 503 errors on repeated attempts).
