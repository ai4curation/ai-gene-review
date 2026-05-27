# ycf4 notes

- Reviewed UniProt and GOA on 2026-05-10.
- UniProt identifies ycf4 as Photosystem I assembly protein Ycf4 [file:POPTR/ycf4/ycf4-uniprot.txt "RecName: Full=Photosystem I assembly protein Ycf4"].
- The function line supports photosystem I assembly rather than direct PSI structural membership [file:POPTR/ycf4/ycf4-uniprot.txt "Seems to be required for the assembly of the photosystem I complex."].
- Modified GO:0009522 photosystem I to GO:0048564 photosystem I assembly, and added GO:0048564 as a NEW supported annotation. Thylakoid/membrane terms were refined to chloroplast thylakoid membrane.

- Addressed PR #470 review on 2026-05-10: changed GO:0009522 photosystem I from cross-aspect MODIFY to REMOVE, while retaining separate NEW GO:0048564 photosystem I assembly.
- Addressed PR #470 third-cycle consistency suggestion on 2026-05-10: changed NEW GO:0048564 original_reference_id to the UniProt file because the term is absent from the GOA rows.
