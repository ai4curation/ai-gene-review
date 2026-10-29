# POLD2: horse-human sequence comparison

Reproduce from this folder with:

    uv run --script compare_horse_to_human.py human-P49005-uniprot.txt ../POLD2-uniprot.txt alignment.json 293

`compare_horse_to_human.py` is a copy of the donkey POLD2 comparison script (genes/EQUAS/POLD2/POLD2-bioinformatics/compare_to_human.py) with labels changed; `human-P49005-uniprot.txt` is the reviewed human POLD2 record copied from that folder (downloaded from UniProt on 2026-10-14). BLOSUM62 global alignment, gap open -10, extension -0.5.

## Result

The horse sequence F7DA84 (469 residues) aligns to human P49005 (469 residues) with 95.1% identity (446 identical of 469 paired residues), 100% coverage of both sequences and no gaps. No human region lacks a horse partner, so the N-terminal OB-fold domain (Pfam PF18018) and the C-terminal DNA polymerase alpha/delta/epsilon subunit B (inactive calcineurin-like phosphoesterase fold, Pfam PF04042) are complete. Human Asp293, whose Asn substitution destabilises Pol delta in patients (PMID:31449058), is conserved as Asp293 in horse.

F7DA84 is therefore a full-length product of horse POLD2, not a fragment or alternative gene model.

## Limitations

Pairwise identity supports homology; orthology rests on PANTHER (both in PTHR10416:SF0, a family with one subfamily) and on the horse IBA rows from PAINT nodes PTN000045935/PTN000045936. Interaction surfaces were not tested individually.
