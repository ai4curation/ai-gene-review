# FIG4 source guide

The review uses the fetched [human UniProt record](FIG4-uniprot.txt), the immutable annotation seed represented by [FIG4-goa.tsv](FIG4-goa.tsv), and the primary sources summarized in [FIG4-source-evidence.md](FIG4-source-evidence.md). The GOA table is annotation provenance, not scientific support for its own assertions.

## Literature access

Full text is cached for PMIDs 16954148, 17572665, 18950639, 19037259, 19118816, 21655088, 24598713, 28514442, 32296183, 33098764, 33961781 and 35271311. The scope actually read is stated in the reference assessments and evidence document; a full-text cache flag does not mean every figure or supplement was inspected.

PMIDs 14574404, 15489334, 17556371, 17909536, 21705420, 23623387 and 9039502 are abstract-only in the normal caches. PMID:17556371 supports substrate breadth and Sac3 endosome/complex evidence; PMID:17909536 supplies the specific rat-donor activities and cellular outcomes. Neither full substrate panels nor inaccessible assay details are claimed. PMID:23623387 has a PMC identifier but its fetched normal cache is still abstract-only. No cache was edited to manufacture full text.

The nine Reactome caches are R-HSA-1660516, R-HSA-1660517, R-HSA-1676005, R-HSA-1676020, R-HSA-1676174, R-NUL-1675886, R-NUL-1675925, R-NUL-1675982 and R-NUL-1676051. Normal markdown summaries were supplemented by direct entity-graph inspection using `https://reactome.org/ContentService/data/query/<stable-id-or-database-id>`. The chimeric flags, human Q92562 constituents and locations were verified on the actual reaction/complex/protein chain, rather than inferred from the prefix or summary species label.

Exact physical-association records can be inspected in [IntAct](https://www.ebi.ac.uk/intact/) using the accessions in the evidence table. Partner identities were checked in UniProt, including [human VAC14](https://www.uniprot.org/uniprotkb/Q08AM6/entry), [human GORASP2](https://www.uniprot.org/uniprotkb/Q9H8Y8/entry), [human PIKFYVE](https://www.uniprot.org/uniprotkb/Q9Y2I7/entry) and [mouse Pikfyve](https://www.uniprot.org/uniprotkb/Q9Z1T6/entry). [Rat Fig4 A6KTC8](https://rest.uniprot.org/uniprotkb/A6KTC8.json) supplies donor identity and current RGD-linked cross-references. Present-day annotation-service absence is not treated as negative experimental evidence.

## Reproducing the small PAINT slice

The existing PTHR45738 entries and metadata were reused from main. The new slice is derived from upstream data using the repository's normal parser and serializer:

1. Retrieve the [original IBD.gaf](https://data.pantherdb.org/ftp/downloads/paint/current/IBD.gaf) and the complete [PTHR45738 tree](https://www.pantherdb.org/services/oai/pantherdb/treeinfo?family=PTHR45738). For this review the IBD source had upstream last-modified date 2026-08-28. The topology API identifies release 19; these retain separate provenance.
2. Traverse every `annotation_node` under `search.tree_topology.annotation_node`, collecting each `persistent_id`; normalize singleton/list `children.annotation_node` values. This gives 470 family nodes. Locate the exact human Q92562 leaf and its ancestral path.
3. Pass the original IBD text to `ai_gene_review.etl.panther_paint.parse_ibd_gaf`, then pass `PTHR45738`, the complete node set, the parsed index and the normal family directory to `write_family_paint`.
4. Verify the three-row output and join each incoming IBA's GO identifier and PTN000127900 to a positive original IBD assertion. Do not promote the third, nonincoming component assertion to a new gene annotation.

| Source | Bytes | SHA256 |
| --- | ---: | --- |
| Original IBD.gaf | 7,600,851 | `0c672914e10c1f79d3fb365077d843a92e518eb6eee2aac00c67150274adf569` |
| Complete PTHR45738 tree response | 1,916,446 | `3c1c48b7ea4c70db0d391be81a7aae9e3e6f693e03b38af2d358e9e874c6d54d` |
| PTHR45738 family alignment response | 2,281,093 | `36fa5dab2c0666623c510ce6fdb0864f8819c02b27f31ebce597df05668e75fe` |
| Derived normal PAINT slice (3 data rows) | 412 | `a24fa48c7e427ffc676a22952999fb20eb9dcea066683d284e67a6ddfe25d2ec` |

The [family alignment endpoint](https://www.pantherdb.org/services/oai/pantherdb/familymsa?family=PTHR45738) and [target gene endpoint](https://www.pantherdb.org/services/oai/pantherdb/geneinfo?geneInputList=Q92562&organism=9606) support the human leaf/sequence identity check. The slice selection uses the complete tree instead of downloading the much larger leaf GAF. It does not assert that separately dated topology and IBD datasets are identical releases, or that expanded GO-slim summaries are original PAINT assertions.

## Ontology follow-up, 2026-10-28

Fresh official QuickGO responses distinguish labels and synonyms from the actual graph. [GO:0006661](https://www.ebi.ac.uk/QuickGO/term/GO:0006661) retains broad phosphoinositide-biosynthesis exact synonyms, but the PI-phosphate branch is separate. The complete is_a/part_of ancestor results for GO:0036092, GO:0046854 and GO:1903102 exclude GO:0006661; this is not a declaration that missing edges prove disjointness. The source-evidence document explains the independent chemical reason for the three over-annotation decisions.

The [explicit GO:0043813 to GO:0036092 path](https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0043813/paths/GO:0036092?relations=is_a,part_of) is one part_of edge. It supports correct direct PI3P production while leaving the physiological importance of that product to biological assessment. [GO:0097110](https://www.ebi.ac.uk/QuickGO/term/GO:0097110) describes binding a scaffold protein, and [GO:0004722](https://www.ebi.ac.uk/QuickGO/term/GO:0004722) includes protein serine phosphatase activity as a narrow synonym.

| Official response | Bytes | SHA256 |
| --- | ---: | --- |
| [terms.json](https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0006661,GO:0036092,GO:0043813,GO:0097110,GO:0046854,GO:1903102,GO:0004722) | 6,248 | `5f85faee53867d9bf826c05bc6711869aac9b76f94df0c367cadd4db8e6f8a5f` |
| [ancestors.json](https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0006661,GO:0036092,GO:0043813,GO:0097110,GO:0046854,GO:1903102,GO:0004722/ancestors?relations=is_a,part_of) | 7,828 | `268eacd0ea27a504a8fb04109235e398a5e7fb8c72fa9bbea84f1c12953442b6` |
| [paths-43813-36092.json](https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0043813/paths/GO:0036092?relations=is_a,part_of) | 118 | `ca501fae84ab2104071f8aeb01dd91e746faba5611f6db2773841a8e4fe46abd` |
| [paths-36092-6661.json](https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0036092/paths/GO:0006661?relations=is_a,part_of) | 47 | `07920d8594aec48d49ad0f36504e8c658eebf70a2e03f274e61899a21cc4c8ed` |
| [paths-46854-6661.json](https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0046854/paths/GO:0006661?relations=is_a,part_of) | 47 | `07920d8594aec48d49ad0f36504e8c658eebf70a2e03f274e61899a21cc4c8ed` |
