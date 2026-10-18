# GA3 (ent-kaurene oxidase, KO, CYP701A3; At5g25900; UniProt Q93ZB2) - curation notes

- Folder symbol GA3 (TAIR symbol; UniProt primary gene name is KO, synonyms CYP701A3/GA3/KO1). Accession Q93ZB2 = KO1_ARATH verified.
- Falcon deep research attempted and failed (exit code 1).

## Function
- Three oxidations ent-kaurene -> ent-kaurenoic acid (RHEA:32323) [PMID:9952446 "the single enzyme GA3 (ent-kaurene oxidase) catalyzes the three steps of gibberellin biosynthesis from ent-kaurene to ent-kaurenoic acid"].
- ga3-1 lacks KO activity; genomic complementation [PMID:9671797].
- Mechanism: intermediates retained, first hydroxylation rate-limiting [PMID:20698828].

## Location
- Outer face of chloroplast envelope [PMID:11722763 "targeted to the outer face of the chloroplast envelope"]; LOPIT proteomics place it with ER markers [PMID:16618929, PMID:22923678]. Recorded as an open question (plastid envelope vs ER vs contact sites).

## Curation decisions
- Generic P450 MF terms (monooxygenase, GO:0016705, GO:0016709 IBA) -> MODIFY to GO:0052615.
- oxygen binding IMP (TIGR legacy) -> MODIFY to GO:0052615 (mutant shows loss of KO activity, not O2 binding).
- iron ion binding over-annotated (heme iron); heme binding non-core.
