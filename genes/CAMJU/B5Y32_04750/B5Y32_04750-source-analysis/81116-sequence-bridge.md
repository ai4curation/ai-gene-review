# Campylobacter 81116 sequence bridge and DsbB accession gap

The native experiments in PMID34948248 used C. jejuni 81116 (NCBITaxon:407148), whereas the two current UniProt records below use species taxon 197 and mnemonic CAMJU. The current ORF names are preserved; C8J aliases identify the assayed 81116 genome, not the current record's named strain.

| Protein | 81116 locus / ENA protein | Deleted UniProt | Current exact-sequence record | UniParc | Length |
|---|---|---|---|---|---|
| DsbA1 | C8J_0814 / ABV52413.1 | A8FLS6 | A0A1J6PBD5 / B5Y32_04750 | UPI00015D00ED | 213 |
| DsbA2 | C8J_0811 / ABV52410.1 | A8FLS3 | A0A1J6UFJ6 / F8Y55_09670 | UPI00015D00EA | 220 |
| DsbB | C8J_0812 / ABV52411.1 | A8FLS4 | No live exact-sequence record recovered | UPI00015D00EB | 260 |

The CP000814.1 CDS translations match the UniParc sequences exactly. The two live UniProt sequences match their respective full translations and list the same UniParc identifiers. The 81116 accessions are explicitly Inactive/DELETED with reason “Not part of a reference proteome”; their CAMJ8 mnemonic is archival. No inactive flat file was manufactured and no current record was relabeled as strain 81116.

RCSB 7PQ7 and 7PQ8 entity 1 contain native DsbA1 residues 21–213, preceded by M and followed by LEHHHHHH. RCSB 7PQF entity 1 contains native DsbA2 residues 27–220, preceded by MM and followed by LEHHHHHH. These exact mature-domain matches corroborate the assay identity while preserving the recombinant signal-sequence deletions and affinity-tag extensions. PDB SIFTS maps the structures to the live species-level records. No sequence mutation was silently ignored.

For DsbB, all nine UniProt accessions listed by UniParc were checked directly and are inactive: E1PNK2, A0A076G026, A0A0P0LGP0, A8FLS4, A0A0W8LJE3, A0A2X1H1W8, A0A0E1ETA1, U4NXJ4, E5ZGY8. The active UniParc cross-reference response contains 123 records but no UniProtKB record. This is a current-accession coverage gap, not absent biological evidence. DsbB was not seeded using a merely similar NCTC11168 protein. The paper identifies its cloned donor explicitly: “Campylobacter jejuni subsp. jejuni 81116 (NCTC11828—GenBank accession number CP000814)”.

## Functional scope

PMID34948248 reports that both DsbAs oxidatively fold reduced RNaseA, despite failing insulin reduction. GO0015035's reversible protein thiol/disulfide equation includes this oxidation; the insulin-negative result is not evidence against that MF. Neither RNase refolding nor similarity to DsbL establishes disulfide-isomerization activity in these proteins. E. coli complementation differs between the paralogs and is not native 81116 motility evidence. Some other C. jejuni strains have truncated DsbA2, so the intact81116 activity cannot be applied universally.

CjDsbB reoxidation used a detergent-solubilized, partially purified preparation with exogenous UQ1 or MK7. The authors state: “we decided to exclude the experimental variant without the CjDsbB protein in our analysis”. Thus the endpoint AMS assay lacks a no-enzyme reaction control. Similar 1/2-hour oxidation endpoints do not establish equal binding affinities; the peptide MST signal was too weak to quantify. The discussion explicitly says neither assay quinone naturally occurs in C. jejuni. Native dsbB mutation changes DsbA1 redox state and DsbA2 abundance, supporting a partner relationship, while native quinone identity remains unresolved. C8J_1298 is a separate dimeric oxidoreductase and is not conflated with either monomeric DsbA.

## Official acquisition endpoints and immutable response hashes

Full responses and genome text are retained only in the ignored campylobacter-panel cache. This file records scoped identity results, not an acquired full paper.

- https://www.ebi.ac.uk/ena/browser/api/embl/CP000814.1?download=false; SHA256 `6d5bd64f78100885700957ddfed03cd72759e80b7b0ffd41430043a1d05947e5`.

- https://rest.uniprot.org/uniprotkb/A0A1J6PBD5.json; SHA256 `f8ced9413723c6d785a331ad4c5044077c83a5fb0932db6c156765d99aa7b502`.

- https://rest.uniprot.org/uniprotkb/A0A1J6UFJ6.json; SHA256 `deb40f09b1270abdc32e2a81b6aaa6c110dd5d73ea25cb08abc314932565cc90`.

- https://rest.uniprot.org/uniprotkb/A8FLS4.json; SHA256 `852b9bcacc610656b3d571740bed4c76e05d8d95301bd3041aa8b48a24e21043`.

- https://rest.uniprot.org/uniparc/UPI00015D00EB/databases?database=UniProtKB&active=true&size=500; SHA256 `d4eac1371fbafda1ed9c546e4ab5e2cf59ab4ccff9f20b875208af72a92ccac2`.

- https://data.rcsb.org/rest/v1/core/polymer_entity/7PQ7/1; SHA256 `f546ef7738f816f7a0fb950c947403eb69642e28c1532494d514ebd17b71bf32`.

- https://data.rcsb.org/rest/v1/core/polymer_entity/7PQF/1; SHA256 `318c206cda7bff0b998f43de791726afbcb7cdff873d3e865211d4ae44c75204`.

- C8J_0814 full protein sequence SHA256 `fbc755cc63f5a24db725eb2e5e03f63d727a9ede63c11e2c99e965703b59e05c`.

- C8J_0811 full protein sequence SHA256 `d04fa8772d6bc338dde8c4381b89a1a40ab4909c7e80e92bcb90643ea2c54df3`.

- C8J_0812 full protein sequence SHA256 `17efc48df7e7f539143ff67bf2281f647f9cc5fe189c0ed9c78a18d1b4b49ad0`.

## Native substrate results and corrected phenotype

PMID25181355 measured reduced AstA activity in native 81116 dsbA2/dsbB mutants and reduced PhoX activity particularly in the dsbA1 mutant. These support client preferences but are not isolated-enzyme native-substrate kinetics. PMID32203539 explicitly reports that the old dsbA1 mutant's motility defect was caused by background mutations; the newly constructed mutant retained motility. Consequently the 2014 motility interpretation is not propagated to these current records.
