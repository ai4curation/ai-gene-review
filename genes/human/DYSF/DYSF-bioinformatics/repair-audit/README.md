# DYSF repair participation and titin specificity

The audit supports one new process assertion, GO:0001778 plasma membrane repair, and refines the existing titin interaction to GO:0031432. Source GOA dictionaries remain unchanged.

Dysferlin contributes to membrane-fusion machinery; it is not the membrane lesion being repaired. Human-cell phenotypes ([PMID:24967968](https://pubmed.ncbi.nlm.nih.gov/24967968/)) are combined with direct biochemical participation ([PMID:27226605](https://pubmed.ncbi.nlm.nih.gov/27226605/)), rather than treating necessity alone as sufficient. See the [source guide](../../DYSF-source-guide.md) for original-access and assay boundaries.

The complete human exact-term query contains 106 rows. Closer membrane-fusion comparators SYT7 and MYOF carry GO:0001778 through ISS; these are not independent human experiments. ANO5 has an IMP annotation and CHMP3 has IDA/IEA annotations. Together these records do not support a convention excluding this class of repair participant. Comparator annotation is a convention check, not the experimental evidence for DYSF.

The term lies under wound healing and membrane organization. None of the four imported DYSF process terms describes repair or is present in its ancestor list; no additional repair descendant is proposed. The captured GO-CAM index has no O75923/DYSF matches. The existing [Reactome event](https://reactome.org/content/detail/R-HSA-5263633) includes dysferlin in repair machinery. Its older membrane-patch account is not treated as the uniquely established mechanism.

GO:0031432 is a current molecular-function child of GO:0008092 and names the recorded titin partner. The existing fragment-interaction and tissue-proximity evidence retains its limits.

## Reproduction

`sources.json` records exact URLs and hashes. The small compressed archive contains genuine full QuickGO responses, including the complete comparator query. `verify.py` uses only the Python standard library and derives `RESULTS.json`; it does not infer biology from annotation counts.

From this directory:

```sh
python3 verify.py --check
python3 verify.py --check --gocam-index ../../../../../gocams/index.tsv
```

The second command additionally checks the separately versioned repository index. A newer index deliberately fails its hash check and requires a fresh documented comparison. Primary articles are not embedded in this artifact; ordinary publication caches and linked originals carry the literature evidence.
