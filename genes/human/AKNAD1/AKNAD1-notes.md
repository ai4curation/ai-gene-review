# AKNAD1 (Q5T1N1) review notes

## 2026-10-03: PAINT/affinage review

AKNAD1 is a dark paralog of AKNA.
- **Affinage:** the trust gates clear, but the result is empty ("No mechanistic discoveries found in literature.").
- **Europe PMC search** (AKNAD1 OR C1orf62): 58 hits. All are expression, CNV-association or GWAS mentions, and none studies the protein.

GOA has one row, a microtubule IBA:
- **Source:** node PTN000487658, with mouse Akna (MGI:2140340) as donor.
- **Node span:** it inherits to both AKNA and AKNAD1 across vertebrates, amphioxus (7739) and sea urchin (7668). That is 34 gene products, per QuickGO withFrom.
- **The split:** the AKNA-only node PTN002726534 carries the richer terms (centrosome, delamination, EMT, neuroblast terms), and AKNAD1 does not inherit them.
- **Decision:** I read this as a deliberate PAINT judgment that microtubule association is ancestral to the family. There is no AKNAD1-specific evidence against it, so the IBA is ACCEPTed. The whole gene is recorded as a WHOLLY_DARK knowledge gap.

## Round 1 (PR #3946 review)

- `projects/paint/human-no-IBA.tsv` lists human AKNA as having no IBA rows. That fits the reading above. PAINT does not emit IBAs to the gene that supplies the experimental evidence, and AKNA's experimental grounding is its mouse ortholog's IDA rows plus HPA. Human AKNA's centrosomal rows therefore arrive as ISS/IEA rather than IBA.
- The QuickGO withFrom listing for PTN000487658 includes AKNA and AKNAD1 orthologs from fish (8090), frogs (8355, 8364), birds (9031, 9258) and mammals, plus amphioxus and sea urchin. This listing is the basis for saying the family is present across vertebrates.
