# psd review notes

## Identity and scope

- Target: `psd`, PP_4908, UniProt Q88DB9, *Pseudomonas putida* KT2440.
- Reviewed files: `psd-ai-review.yaml`, `psd-goa.tsv`, and `psd-uniprot.txt`.
- Consecutive-reaction context was checked against target PssA/PP_3664.

## Exact provenance

### Reviewed UniProt record

Source: `file:PSEPK/psd/psd-uniprot.txt`.

- `"DE   RecName: Full=Phosphatidylserine decarboxylase proenzyme"`
- `"DE            EC=4.1.1.65"`
- `"CC   -!- FUNCTION: Catalyzes the formation of phosphatidylethanolamine (PtdEtn)"`
- `"CC       from phosphatidylserine (PtdSer)."`
- `"CC       Name=pyruvate; Xref=ChEBI:CHEBI:15361;"`
- `"CC   -!- SUBUNIT: Heterodimer of a large membrane-associated beta subunit and a"`
- `"CC       small pyruvoyl-containing alpha subunit."`
- `"CC   -!- SUBCELLULAR LOCATION: Cell membrane"`
- `"CC       Peripheral membrane protein"`
- `"DR   GO; GO:0004609; F:phosphatidylserine decarboxylase activity; IEA:UniProtKB-UniRule."`
- `"DR   GO; GO:0006646; P:phosphatidylethanolamine biosynthetic process; IEA:UniProtKB-UniRule."`

The record further states that active-enzyme maturation is an autocatalytic cleavage at Ser252 that creates the N-terminal pyruvoyl group of the alpha chain.

### Consecutive-reaction statement

The Psd record labels this reaction `"step 2/2"` of phosphatidylethanolamine formation from CDP-diacylglycerol. The PssA record assigns EC 2.7.8.8, which forms the phosphatidylserine substrate.

Normalized exact support used in the YAML:

- `"Psd performs step 2/2, decarboxylating the phosphatidylserine product of PssA to phosphatidylethanolamine."`

## Curation conclusions

- Accept phosphatidylserine decarboxylase activity, phosphatidylethanolamine biosynthesis, and plasma-membrane localization as core.
- Keep the broad phospholipid biosynthetic process as non-core.
- Psd must not be conflated with PssA: PssA forms phosphatidylserine; Psd decarboxylates it.

## 2026-09-01 annotation-reviewer pass

All four current GOA rows were re-reviewed against the reviewed UniProt/HAMAP
record and the existing OpenScientist report. The specific decarboxylase
activity, plasma-membrane location, and phosphatidylethanolamine biosynthetic
process remain core; the broader phospholipid biosynthetic process remains
non-core. No current GOA row is PENDING.
