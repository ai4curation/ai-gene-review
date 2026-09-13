# GND1 bioinformatics

Sequence-level check of the NADP+ versus NAD+ coenzyme-specificity determinants of
C. albicans 6-phosphogluconate dehydrogenase (Gnd1, A0A1D8PFS4), following the
determinants summarised in Hanau & Helliwell 2022 (PMID:35234135).

    python3 check_coenzyme_motifs.py            # uses ../GND1-uniprot.txt
    python3 check_coenzyme_motifs.py OTHER.txt  # any UniProt flat-file record

Outputs `results.json`; findings are summarised in `RESULTS.md`.
