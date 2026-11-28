# MAF notes

`just deep-research human MAF --provider perplexity` failed because the provider was not available in this checkout, and retrying the available `claude-code` provider failed because Claude Code was not logged in. I therefore reviewed the cached GOA, UniProtKB, PANTHER and publication evidence manually.

MAF is a nuclear large-Maf bZIP transcription factor. UniProt records its MARE/cis-regulatory DNA binding, homo- and heterodimerization with bZIP factors, and transcriptional activator/repressor activity. The family-wide PAINT rows for `GO:0000978`, `GO:0000981`, `GO:0006357` and `GO:0005634` are anchored on the PTHR10129 root and are consistent with the conserved large-Maf/small-Maf bZIP transcription-factor activity.

PMID:25857263 is the best direct paper for the human megakaryocyte row: it reports that MAF is a miR-486-3p target in human CD34+ hematopoietic progenitors and that "MAF silencing in HPCs is able to reverse at least in part the effects of MYB silencing on erythroid versus megakaryocyte lineage choice." This supports a MAF role in megakaryocyte differentiation in the assayed progenitor cultures.

The ComplexPortal BACH1/BACH2 rows cite PMID:27052415 and PMID:33897412, which are Bach or Keap1/Nrf2 reviews. Those reviews describe Bach complexes with the small Maf proteins rather than a direct large-MAF repressor complex, so the papers do not themselves establish the large-MAF `GO:0000122` process rows. MAF itself can be a repressor according to UniProt, so the process term is retained but supported from the MAF entry rather than those Bach review papers.

The ATF4 integrated-stress-response row cites PMID:28566324. The cached full text identifies ATF4 as the key regulator of the mammalian mitochondrial stress response but does not mention MAF, so the `GO:0140467` projection through a ComplexPortal ATF4-MAF complex is over-annotated.

PMID:20102225 and PMID:23661758 are coiled-coil/bZIP interaction surveys. They support the idea that MAF-family bZIP proteins dimerize with other bZIP proteins, but they are not by themselves a reason to keep bare `GO:0005515` protein-binding rows.
