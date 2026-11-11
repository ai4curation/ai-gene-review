# FOXJ3 (donkey): benchmark model versus full-length gene model (re-review, 2026-10-21)

Reproduce from this folder with:

    uv run --script compare_gene_models_rereview.py ../FOXJ3-uniprot.txt donkey-A0A8C4PFN5-uniprot.txt human-Q9UPW0-uniprot.txt alignment_rereview.json

`donkey-A0A8C4PFN5-uniprot.txt` was downloaded from the UniProt REST API on 2026-10-21. Full output is in `alignment_rereview.json`. The earlier files in this folder (`RESULTS.md`, `alignment.json`, `compare_to_human.py`) are unchanged.

## Gene models

UniProt lists five donkey FOXJ3 entries, all unreviewed (TrEMBL): A0A8C4PFN5 (623 aa), A0A9L0JPR6 (614 aa), A0A9L0JKH1 (580 aa, the benchmark), A0A9L0KDI8 (179 aa) and A0A9L0J7H9 (150 aa). A0A8C4PFN5, A0A9L0JPR6 and A0A9L0JKH1 are translations of transcripts of the same Ensembl gene, ENSEASG00005001210 (chromosome 5), and all are in PANTHER subfamily PTHR46078:SF3 (FORKHEAD BOX PROTEIN J3). No donkey FOXJ3 entry is reviewed.

## Result

The benchmark A0A9L0JKH1 (580 aa) is 100% identical to the full-length donkey model A0A8C4PFN5 (623 aa) over all 580 of its residues. The only difference is an internal deletion: A0A8C4PFN5 residues 211-253 (43 aa) have no partner in A0A9L0JKH1. This is an alternative transcript of the same gene (an internal exon-skipping isoform), not a fragment and not a different gene.

The full-length model A0A8C4PFN5 aligns to reviewed human FOXJ3 Q9UPW0 (622 aa) over all 622 human residues with 98.23% identity, with one inserted donkey residue (364). The human fork-head DNA_BIND feature (77-168) aligns gap-free to both donkey models, and the donkey fork-head DNA_BIND feature (78-173) is gap-free between the two donkey models.

The missing 43-residue segment is not the segment removed in human isoform 2 (Q9UPW0-2 lacks human 177-210, per the human record's VAR_SEQ). Whether a donkey or human transcript skipping the 211-253 segment is expressed is not established by these data.

## Limitations

Gene models are Ensembl predictions; none of the donkey isoforms has transcript-level experimental support in UniProt. Identity of the fork-head domain implies conserved DNA-binding residues but does not test DNA binding.
