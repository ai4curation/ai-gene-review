# HOXA2 (donkey, A0A9L0JBM7) notes

## Sources
- Donkey UniProt A0A9L0JBM7 (unreviewed; function text and location are ARBA/PROSITE predictions).
- Human HOXA2 O43364 and mouse Hoxa2 P31245 UniProt records fetched into HOXA2-bioinformatics/ (O43364-uniprot.txt, P31245-uniprot.txt).
- Experimental GO annotations of human/mouse orthologs from QuickGO: HOXA2-bioinformatics/ortholog_experimental_goa.txt.
- No HOXA2 review exists for human or mouse in this repository; the key primary papers (e.g. PMID:15634706, PMID:25889273) are not in the local publication cache, so ortholog evidence is taken from the GOA records rather than full text.

## Biology
- Human/mouse HOXA2: [file:EQUAS/HOXA2/HOXA2-bioinformatics/O43364-uniprot.txt "Sequence-specific transcription factor which is part of a"] developmental regulatory system providing positional identity on the anterior-posterior axis; nuclear.
- Mouse Hoxa2 is a sequence-specific DNA-binding transcriptional repressor of RNA polymerase II targets [file:EQUAS/HOXA2/HOXA2-bioinformatics/ortholog_experimental_goa.txt "P31245 Hoxa2 enables GO:0001227 \"DNA-binding transcription repressor activity, RNA polymerase II-specific\" IDA PMID:15634706"], and also has IDA support for positive regulation of RNA Pol II transcription (PMID:18787068).
- Mouse Hoxa2 developmental roles: second pharyngeal arch identity, middle ear and skeletal morphogenesis, hindbrain rhombomere 2/3 development (IMP/IGI/IDA rows in ortholog_experimental_goa.txt).
- Human disease: microtia, hearing impairment and cleft palate (MHICP) [O43364-uniprot.txt].

## Donkey sequence
- 97.6% identity; homeodomain 60/60 identical; hexapeptide identical [file:EQUAS/HOXA2/HOXA2-bioinformatics/RESULTS.md].

## Decisions
- Core: DNA-binding TF activity, RNA Pol II-specific (ACCEPT), repressor activity (ACCEPT), cis-regulatory region sequence-specific DNA binding (ACCEPT), nucleus (ACCEPT), regulation of transcription by RNA Pol II (TreeGrafter, ACCEPT), negative regulation of transcription by RNA Pol II (ACCEPT).
- Generic DNA binding, DNA-binding TF activity, regulation of DNA-templated transcription: TOO_GENERAL (entailed by the accepted specific terms).
- Developmental processes: pharyngeal system development and embryonic skeletal system development ACCEPT; muscle structure development KEEP_AS_NON_CORE.
