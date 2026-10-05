# TyrRS ProtNLM2 function-description review

## Original prediction

> Catalyzes the attachment of tyrosine to tRNA(Tyr) in a two-step reaction: tyrosine is first activated by ATP to form Tyr-AMP and then transferred to the acceptor end of tRNA(Tyr)

Original wording and all model/source metadata are retained in [TyrRS-protnlm-source.json](TyrRS-protnlm-source.json).

## Assessment

**Supported conserved catalytic function (CNN at the gene-function level).** The predicted two-step tyrosine activation and transfer to tRNA matches the established activity of native 525-residue TyrRS-PA/Q9VV60. This is supported by the Drosophila aaRS catalogue and functional/complementation work. Existing GOA already includes experimentally supported tyrosine-tRNA ligase activity. The narrative does not claim the separate mammalian ligand/stress functions.

Sources: [PMID:26761199](https://pubmed.ncbi.nlm.nih.gov/26761199/), [PMID:19561293](https://pubmed.ncbi.nlm.nih.gov/19561293/), and the [FlyBase identity snapshot](TyrRS-flybase.txt). The exact paragraph and chicken Q5ZJ08 donor metadata are preserved in the source JSON.
