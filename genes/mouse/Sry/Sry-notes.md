# Sry (mouse, Q05738) curation notes

Inputs: UniProt Q05738, GOA (52 rows), the OpenScientist report (leads only), cached papers.

- Sufficiency: a 14-kb Sry transgene masculinizes XX embryos [PMID:2030730 "It is now shown that Sry on a 14-kilobase genomic DNA fragment is sufficient to induce testis differentiation and subsequent male development when introduced into chromosomally female mouse embryos."].
- Endogenous SRY marks pre-Sertoli cells, which switch on Sox9 almost at once [PMID:16185683 "it appears that SRY expression marks the pre-Sertoli cell lineage and leads to up-regulation of Sox9 expression cell-autonomously."].
- Sox9/Fgf9 feed-forward loop represses Wnt4 [PMID:16700629].
- Isoforms: a cryptic second exon gives Sry-T, the essential stable form; Sry-S carries a C-terminal degron [PMID:33004521; UniProt FUNCTION lines].
- Repression via KRAB-O/KAP1 is shown in reporter assays only [PMID:19850934, PMID:15469996].
- Nuclear import via importin-beta [PMID:11535586] and exportin-4 [PMID:19349578].

Judgement calls (summary): generic DNA binding -> DNA binding, bending plus cis-regulatory sequence-specific binding; protein-binding rows -> transcription corepressor binding (KRAB-O), PDZ domain binding (NHERF2), DNA-binding TF binding (Oct4), REMOVE for unidentified far-western partners; spermatogenesis and the Sry-Oct4 "transcription regulator complex" marked over-annotated; enzyme binding (rat ISO, source untraceable) UNDECIDED.

Possible source defects (MGI): PMID:15879091 (a mast-cell TGF-beta1 paper) cited for male sex determination, and PMID:22514746 (a Tgif1 paper whose full text does not mention Sry) cited for nucleus. Both rows are accepted on other evidence and flagged as SUSPECTED WRONG_REFERENCE.
