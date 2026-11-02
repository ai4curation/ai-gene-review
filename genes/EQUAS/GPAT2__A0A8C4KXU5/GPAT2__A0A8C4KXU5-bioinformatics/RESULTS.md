# GPAT2 (donkey A0A8C4KXU5): comparison with reviewed mammalian GPAT2 orthologs

Reproduce from this folder with:

    uv run --script compare_to_orthologs.py ../GPAT2__A0A8C4KXU5-uniprot.txt results.json Q14DK4-uniprot.txt Q6NUI2-uniprot.txt D3ZI76-uniprot.txt

Reference records were downloaded from the UniProt REST API on 2026-10-21: reviewed mouse Gpat2 Q14DK4
(801 aa; the protein characterised experimentally), human GPAT2 Q6NUI2 (795 aa) and rat Gpat2 D3ZI76 (801 aa).
Full output is in `results.json`.

## Evolutionary basis

The donkey entry and all three reviewed references carry the same PANTHER subfamily, PTHR12563:SF15
(GLYCEROL-3-PHOSPHATE ACYLTRANSFERASE 2, MITOCHONDRIAL), read from each record's PANTHER cross-reference.
That shared subfamily, not the alignment identity below, is the basis for treating A0A8C4KXU5 as the donkey
GPAT2 ortholog. The other mitochondrial GPAT, GPAT1 (GPAM; mouse Q61586, human Q9HCL2), is in a different subfamily, PTHR12563:SF16 (interpro/panther/PTHR12563/PTHR12563-entries.csv).

## Result

| Reference | Identity (paired) | Reference coverage | Donkey coverage | HXXXXD (ref 205-210) | Donkey residues at ref TM1 / TM2 |
|---|---|---|---|---|---|
| mouse Q14DK4 | 83.75% | 99.88% | 100.0% | HKSLLD -> HKSLLD at donkey 205 | aligned / aligned |
| human Q6NUI2 | 88.04% | 99.87% | 99.25% | HKTLLD -> HKSLLD at donkey 205 | aligned / aligned |
| rat D3ZI76 | 84.5% | 99.88% | 100.0% | HKSLLD -> HKSLLD at donkey 205 | aligned / aligned |

Against each reference only one reference residue (363) has no donkey partner. The donkey HXXXXD acyltransferase
motif is HKSLLD at residues 205-210, the same positions as the motif whose H and D were mutated in the mouse
rescue experiment of PMID:23611983. Donkey segments aligned to the two predicted mouse transmembrane helices
(mouse 306-332 and 450-472) are AWLGLVVEAVKVGIVPDALLVPVAITY and VLHASVASSAVMSTAIMATLLLF, both hydrophobic and
gap-free. A0A8C4KXU5 is therefore a full-length GPAT2 model across the acyltransferase domain, both
membrane-spanning segments and the conserved C-terminal region.

## Limitations

The donkey record itself carries no transmembrane predictions; the positions above are transferred by
alignment from UniProt sequence-analysis predictions (ECO:0000255) on the mouse record. Retention of the
catalytic motif does not show that the donkey protein is enzymatically active, and none of the functions
of GPAT2 has been measured in donkey. The MILI/PIWIL2-binding region of GPAT2 is not mapped, so its
conservation cannot be assessed.
