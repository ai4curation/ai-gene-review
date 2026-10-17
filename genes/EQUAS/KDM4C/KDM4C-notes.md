# KDM4C (donkey, Equus asinus; UniProt A0A9L0K3L6) - review notes

## Sources used

- Donkey UniProt record (unreviewed, Ensembl ENSEASP00005055940.1), 1052 aa: `KDM4C-uniprot.txt`. JmjN, JmjC, PHD/EPHD and double Tudor domains.
- Donkey GOA: 11 IEA rows (5 TreeGrafter GO_REF:0000118 from PANTHER:PTN001322185; 3 UniRule GO_REF:0000104; nucleus and H3K9 demethylase via GO_REF:0000120; H3K9me2/me3 demethylase via EC mapping GO_REF:0000003).
- Human KDM4C (Q9H3R0) UniProt record fetched 2026-10-14: `KDM4C-bioinformatics/human-KDM4C-Q9H3R0-uniprot.txt`.
- Alignment and active-site check: `KDM4C-bioinformatics/RESULTS.md`.
- Cached publications: PMID:16603238 (JMJD2 family trimethyl demethylases; abstract), PMID:17277772 (JMJD2C/LSD1 and androgen receptor; abstract).
- Human QuickGO (2026-10-14) comparator: IDA/IMP for H3K9 demethylase, H3K9me2/me3 demethylase, H3K36 demethylase, chromatin, positive regulation of transcription by RNA polymerase II; IBA for chromatin remodeling, regulation of gene expression, nucleus, chromatin. No experimental DNA-templated transcription (GO:0006351) annotation.

## Sequence

- [RESULTS.md "The donkey KDM4C protein matches human KDM4C at 91.44% identity over 1052 paired residues, covering 99.62% of the human sequence."]
- [RESULTS.md "All human 2-oxoglutarate-binding residues (Y134, N200, K208, K243), catalytic Fe-binding residues (H190, E192, H278) and Zn-binding residues (C236, H242, C308, C310) of the JmjC domain are conserved"]

## Function

- [human UniProt "Histone demethylase that specifically demethylates 'Lys-9' and 'Lys-36' residues of histone H3"]
- [PMID:16603238 "subfamily members also functioned as trimethylation-specific demethylases"]
- [PMID:17277772 "JMJD2C as the first histone tridemethylase regulating androgen receptor"]; [PMID:17277772 "results in demethylation of trimethyl H3K9 and in stimulation of androgen"].

## Review decisions (summary)

- Accept: chromatin, nucleus, chromatin remodeling, regulation of DNA-templated transcription, histone demethylase activity, H3K9 demethylase, H3K36 demethylase, H3K9me2/me3 demethylase.
- regulation of gene expression: KEEP_AS_NON_CORE (broad).
- metal ion binding: KEEP_AS_NON_CORE (Fe(II) and Zn(2+) sites conserved; cofactor binding, not the function).
- DNA-templated transcription: MARK_AS_OVER_ANNOTATED (KDM4C regulates transcription via chromatin; it does not synthesize RNA).
