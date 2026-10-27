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

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 prediction files were not opened or used.

### Identity

- A0A9L0K3L6 is the full-length donkey KDM4C gene product (1052 aa vs 1056 aa for human Q9H3R0; RESULTS.md: 91.44% identity, 99.62% human coverage, only single-residue indels at human 396, 474, 488-489). Not a fragment or isoform; JmjN, JmjC, PHD/ePHD and both Tudor domains present, all JmjC Fe/2OG/Zn ligands conserved.
- PANTHER (donkey UniProt): PTHR10694:SF104 "LYSINE-SPECIFIC DEMETHYLASE 4C", the same subfamily as human Q9H3R0 and mouse Q8VCD7 (interpro/panther/PTHR10694/PTHR10694-entries.csv). No family review exists under interpro/panther/PTHR10694 (entries + metadata only), so no placement disagreement to report. TreeGrafter rows come from PTN001322185.
- Evolutionary grounding: [PMID:21914792 "KDM4A–C, which are highly conserved in all vertebrates, and demethylate both H3K9 and H3K36"]; [PMID:21914792 "each of KDM4A/B/C preferentially catalyze demethylation at Lys-9 rather than Lys-36"].

### Deep research

- `just deep-research-falcon EQUAS KDM4C --fallback perplexity-lite` failed: falcon "Failed to authenticate"; perplexity-lite fallback HTTP 401 insufficient_quota. No deep-research file was produced. Review proceeds from cached literature: PMID:16603238, PMID:17277772 (abstracts), and newly cached full texts PMID:21914792 (KDM4C structure 2XML, KDM4 kinetics/phylogeny) and PMID:28262558 (KDM4C H190A/E192A inactive control).

### Changes vs the previous review

- histone demethylase activity (GO:0032452) and histone H3K9 demethylase activity (GO:0032454): ACCEPT -> TOO_GENERAL (entailed by accepted GO:0140684).
- regulation of gene expression (GO:0010468): KEEP_AS_NON_CORE -> TOO_GENERAL (entailed by GO:0006355).
- metal ion binding (GO:0046872): KEEP_AS_NON_CORE -> MODIFY to iron ion binding + zinc ion binding [human UniProt "Binds 1 Fe(2+) ion per subunit. {ECO:0000269|PubMed:21914792}"; PMID:21914792 "nickel (substituting iron) ion is coordinated by the conserved HX(E/D)"]; human has IDA zinc ion binding.
- histone H3K36 demethylase activity (GO:0051864): ACCEPT -> MODIFY to GO:0140681 histone H3K36me2/H3K36me3 demethylase activity (trimethyl-state activity, parallel to GO:0140684); core function updated.
- regulation of DNA-templated transcription kept as ACCEPT (directionality shown only for AR coactivation in human cells); DNA-templated transcription kept MARK_AS_OVER_ANNOTATED; chromatin, nucleus, chromatin remodeling, H3K9me2/me3 demethylase kept ACCEPT.
- No NEW annotations. Tudor-domain methylated-histone binding raised as a question only (no KDM4C-specific cached evidence).

### Relative

- Closest experimentally characterised relative: human KDM4C (Q9H3R0), same PANTHER subfamily SF104 (ortholog). No genes/human/KDM4C review exists in the repo -> needs review.
- Modules: no module under modules/ mentions KDM4C, JMJD2 or PTHR10694.
