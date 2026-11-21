# disA curation notes

## 2026-11-04 — c-di-AMP module audit

Identity: UniProtKB:P37573; Bacillus subtilis subsp. subtilis str. 168. All 11 machine annotation payloads and raw UniProt/GOA files are preserved. No NEW annotation rows were added.

An actual `just deep-research-falcon BACSU disA` call failed with HTTP 403 authentication failure. No provider report was authored manually; this journal records manual source research.

QuickGO definitions checked on 2026-11-04 distinguish GO:0004016 (ATP to monomeric cAMP) from GO:0106408 (two ATP to c-di-AMP). The former is MODIFY, including experimental rows where present, because full-text product measurements support the latter. Electronic GO:0006171 cAMP biosynthesis mappings were initially removed where present; the review follow-up below supersedes that decision with MODIFY to a proposed specific process. These are chemical identity corrections, not arguments from evidence-code rank. Source defects remain NOT_REPORTED.

The protein supplies the cyclase role in [bacterial c-di-AMP signaling](../../../modules/bacterial_c_di_amp_signaling.yaml). Membrane attachment applies to CdaA/DacA; DisA is soluble and chromosome-associated. No transport or host-response process is inferred merely from c-di-AMP-dependent phenotypes.

- [PMID:18439896 Structural biochemistry of a bacterial checkpoint protein reveals diadenylate cyclase activity regulated by DNA recombination intermediates.](https://pubmed.ncbi.nlm.nih.gov/18439896/): Assessed against the fetched primary publication. Cached abstract and curated UniProt context assessed; no claim of full-text inspection.
- [PMID:21566650 c-di-AMP reports DNA integrity during sporulation in Bacillus subtilis.](https://pubmed.ncbi.nlm.nih.gov/21566650/): Assessed against the fetched primary publication. Cached abstract and curated UniProt context assessed; no claim of full-text inspection.
- [PMID:34073022 DisA Limits RecG Activities at Stalled or Reversed Replication Forks.](https://pubmed.ncbi.nlm.nih.gov/34073022/): Assessed against the fetched primary publication. Full text available.

PMID:34073022 directly studies B. subtilis DisA and resolves the branched-DNA and c-di-AMP activities; the older PMID:18439896 structural work includes Thermotoga DisA and is not treated as a species-exclusive assay. DisA inhibits RecG-dependent remodeling by DNA-site competition rather than acting as a helicase. Broad DNA binding is refined to the existing junction-specific term, while general scanning remains in the summary.

### PAINT trace and validation

The downloaded PAINT IBD.gaf contains PTN002149835, GO:0004016, IBD, dated 20171208, seeded by Q8Y5E4/O31854/Q45589. The inspected Q8Y5E4 and Q45589 publications establish dinucleotide chemistry, so the correction addresses the ancestral activity label rather than donor number. The first `just paint-losses` attempt could not resolve lineage losses because the PANTHER tree service timed out. A retry after service recovery succeeded: the PTHR34185 tree resolves P37573 to PTN000873976, and `just paint-losses BACSU disA` reports no IRD or IKR loss on this gene’s lineage. This successful check supersedes the earlier UNKNOWN status; the chemical-product correction remains grounded in the primary assays.

Focused validation and HTML rendering pass. Generated HTML and local execution logs are excluded from the curation PR.

## 2026-11-04 — PR #5997 review follow-up

Expanded the UniProt cytoplasm quote to include its curated subcellular-location context, avoiding ambiguity with a keyword label. The record_section is derived with the repository helper. No annotation action, core function or machine payload changes.

Follow-up focused validation passes. Original machine annotation payloads and both raw-source SHA-256 hashes still match the preserved seed baseline.
