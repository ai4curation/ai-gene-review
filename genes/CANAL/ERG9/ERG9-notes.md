# ERG9 notes

ERG9 is the C. albicans member of the canonical fungal squalene synthase lineage. The local
UniProt record places A0A1D8PI71 in `PANTHER:PTHR11626:SF2` (`SQUALENE SYNTHASE`), and the
PTHR11626 family review treats SF2 as the active squalene synthase subfamily while calling
out Arabidopsis SQS2 and Botryococcus SSL members as exceptions outside this canonical
Candida case [file:genes/CANAL/ERG9/ERG9-uniprot.txt, "DR   PANTHER; PTHR11626:SF2; SQUALENE SYNTHASE; 1."],
[file:interpro/panther/PTHR11626/PTHR11626-review.yaml, "Squalene synthase activity is conserved in
the single-copy orthologs of fungi, animals and plants, which make up most of SF2."].

Biologically, ERG9 sits at the branch where two molecules of farnesyl diphosphate are
committed to sterol synthesis as squalene. The 2024 fungal sterol-pathway paper is not direct
C. albicans ERG9 enzymology, but it gives a useful modern pathway statement: "farnesyl
pyrophosphate, the last product of the mevalonate pathway, is converted to squalene by
squalene synthase" [PMID:39060235].

The GOA-cited Song et al. paper is C. albicans specific but expression-only for this review.
It supports ERG9 belonging to the late sterol response rather than directly proving catalysis
or localization: ERG9 and ERG11 transcripts increased under lovastatin/fluconazole during
mid-logarithmic growth [PMID:14653518].

The plasma-membrane IDA row from PMID:19824013 should stay unresolved until the full
proteomics table is inspected. The abstract describes a subproteomic plasma-membrane
enrichment workflow, but it does not show whether ERG9 was a robust plasma-membrane resident
or a carryover ER-membrane hit in a membrane fraction.
