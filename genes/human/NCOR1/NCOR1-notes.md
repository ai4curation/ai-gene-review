# NCOR1 evidence and annotation notes

## 2026-10-26: Human nuclear-receptor coregulator review

NCOR1/N-CoR (O75376) organizes transcriptional repression machinery for many nuclear receptors and non-receptor transcription factors. The core activity is transcription corepressor activity. Histone deacetylases supply catalysis; NCOR1 supplies recruitment/scaffolding and supports HDAC3 activation. It is not itself assigned histone deacetylase catalytic activity.

[PMID:12628926](https://pubmed.ncbi.nlm.nih.gov/12628926/) explicitly describes purification of the human N-CoR complex and maps TBL1/TBLR1 contacts with NCOR1 RD1/RD4. [PMID:11931768](https://pubmed.ncbi.nlm.nih.gov/11931768/) identifies the GPS2/TBL1/NCOR1 assembly and extended SANT-domain activation of latent HDAC3; its JNK effect is mediated through the associated GPS2 subunit. [PMID:11804585](https://pubmed.ncbi.nlm.nih.gov/11804585/) distinguishes the HDAC3 enzymatic complex from class-II HDAC bridging. [PMID:15695367](https://pubmed.ncbi.nlm.nih.gov/15695367/) uses human-cell depletion followed by murine NCOR1 replacement to test the deacetylase-activating domain, so its replacement-species scope is not silently presented as purified human NCOR1 chemistry.

[PMID:18052923](https://pubmed.ncbi.nlm.nih.gov/18052923/) tests NCOR1/SMRT repression of thyroid-receptor target genes and context-dependent compensation. This argues against a single invariant cofactor requirement. For AR, [PMID:17505061](https://pubmed.ncbi.nlm.nih.gov/17505061/) describes antagonist-bound AR recruitment of SIRT1 and NCOR1 to responsive promoters. [PMID:20812024](https://pubmed.ncbi.nlm.nih.gov/20812024/) specifically reports FBI-1/ZBTB7A-enhanced NCOR1/SMRT recruitment to PSA upstream sequences. The existing negative AR-regulation term is retained as a receptor/cell context, not the coregulator's universal identity or proof that all liganded AR complexes contain NCOR1.

[PMID:20388878](https://pubmed.ncbi.nlm.nih.gov/20388878/) identifies ERalpha/corepressor recruitment in miR-221/222 repression, retained as contextual transcriptional regulation. [PMID:18326024](https://pubmed.ncbi.nlm.nih.gov/18326024/) directly includes NCOR1 in the spindle-localized HDAC3 complex and reports spindle defects after NCOR1 depletion. These existing secondary roles are retained; the paper title's emphasis on HDAC3 is not a reason to remove the NCOR1 assertions. Conversely, an NK-cell membrane proteomics claim remains unresolved without the target-level fraction/table evidence, rather than being rejected solely because NCOR1 is predominantly nuclear.

Specific PPARalpha/glycolysis/fatty-acid and donor locomotor claims remain uncertain where the source-specific downstream experiment was not inspected. The obsolete thyroid-receptor binding IBA is refined to current nuclear receptor binding; its original PAINT node is preserved with an explicit note that term maintenance is not a finding of phylogenetic failure.

## Evidence access and review method

Normal `fetch-gene` seeded the review and immutable UniProt/GOA sources. Default Falcon research with Perplexity-lite fallback was attempted concurrently with publication caching; both providers failed (authentication/quota errors in `.cache/module-audit-logs/NCOR1-research.log`). No manual text was written under a provider-generated filename. Primary PubMed/PMC caches were fetched through the normal tools; source files were not manually edited. The normal cache frequently contains only abstracts. Positive target-specific abstract statements can support a claim; missing target detail is recorded as UNDECIDED, never as a wrong-gene conclusion based solely on the title. Full-text inspection was targeted to the passages specified below, rather than a claim to have read every source in full.

All original annotation IDs, labels, evidence codes, qualifiers, supporting entities and isoform fields are preserved. Only review judgments and author-supplied synthesis are changed. No NEW annotations are proposed. Current GO term definitions/obsolescence were checked through QuickGO (2026-10-26; diagnostic JSON in `.cache/module-audit-logs/coregulator-terms.json`). Obsolete original source IDs remain intact; author-proposed replacements use current terms. The PAINT assertions are not treated as pairwise transfers or rejected based on donor count. No independent reconstruction of their whole phylogeny is claimed.

Bare protein binding is refined when the cited evidence resolves a useful partner class. Uninformative but verified cofactor associations are removed under the current GO:0005515 policy, without denying the interaction. Unresolved pair tables, constructs or electronic source claims remain UNDECIDED. Chromatin occupancy does not by itself establish direct or sequence-specific DNA recognition.

The review by Sun and Xu ([PMID:32449767](https://pubmed.ncbi.nlm.nih.gov/32449767/)) supplies broader context: animal models establish many endocrine, neural and behavioral roles, and coregulator functions overlap without being identical. Its expression maps are not direct evidence that every human ortholog executes every brain-development process. The review's target-specific mechanisms and animal-model scope were inspected; no cancer association is promoted to an intrinsic core molecular function.

## Decision coverage

110 source assertions reviewed; 56 ACCEPT, 7 KEEP_AS_NON_CORE, 8 MODIFY, 10 REMOVE, 29 UNDECIDED. The status is COMPLETE with explicit unresolved claims, not a statement that all evidence gaps have been closed.


## PR5554 member follow-up — 2026-10-26

GO:0000118 now quotes the original PMID18326024 statement explicitly identifying N-CoR within the HDAC3/TBL1/TBLR1 complex. The experiment localizes that complex to mitotic spindle; it is not mislabeled as a chromatin-purification experiment. NCOR1 complex membership does not assert deacetylase catalysis.

All original annotation payloads were compared before/after and preserved; only reviewer assessments, source evidence, and the specified core-function location were changed.
