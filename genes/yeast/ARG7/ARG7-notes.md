# ARG7 (YMR062C, Q04728; ECM40) notes

- Mitochondrial ornithine acetyltransferase (ArgJ family, EC 2.3.1.35): "ARG7 gene encoding mitochondrial ornithine acetyltransferase, the enzyme catalyzing the fifth step in arginine biosynthesis"; "While forming ornithine, this enzyme regenerates acetylglutamate" [PMID:9428669].
- Modest bifunctionality (acetyl-CoA NAGS, EC 2.3.1.1): "overexpressed ARG7 can complement yeast arg2 and Escherichia coli argA mutations"; "The yeast enzyme is thus clearly, albeit modestly, bifunctional." [PMID:9428669]
- Inhibited by ornithine, insensitive to arginine [PMID:9428669]; deletion is arginine-leaky, implying an alternative route [PMID:9428669 "total deletion of the genomic ARG7 ORF resulted in an arginine-leaky phenotype"].
- Autoproteolytic processing into alpha/beta chains in the matrix [UniProt:Q04728, citing PMID:10753950].
- Mitochondrial matrix [PMID:205532; UniProt:Q04728].

## Curation decisions
- Core MF GO:0004358 (only IEA/RCA in GOA - no experimental row although PMID:9428669 characterises it); BP GO:0006592, GO:0006526; CC GO:0005759.
- GO:0004042 (acetyl-CoA NAGS) rows KEEP_AS_NON_CORE (genuine but minor; Arg2 is the physiological NAGS).
- RCA cytosol and RCA GO:0103045 L-methionine N-acyltransferase: REMOVE.


## 2026-10-26 systematic fungal annotation audit

Reviewed all 18 existing rows and the core functions with the review and annotation-reviewer workflows. Preserved every machine-sourced term, evidence code, qualifier, source identifier, WITH/FROM entry and row order. No new annotations were added in this audit.

PMID:9428669 supports modest acetyl-CoA-dependent activity and overexpression rescue, not replacement of dedicated NAGS under all native conditions. Leaky deletion implies another ornithine-release route whose enzyme is not identified. PMID:10753950 explicitly reports processing BEFORE mitochondrial targeting and loss of maturation/activity after T215A despite correct targeting. The prior matrix-cleavage claim is corrected without editing UniProt. The cytosol row is now UNDECIDED: native transient processing complicates a categorical exclusion, while leader-deletion localization does not establish a normal cytosolic catalytic pool. PMID:17651682 adds target-specific coupled-assay/deletion-extract evidence.

Normal publication caching completed. Normal Falcon research with Perplexity-lite fallback was attempted for this gene; authentication/quota failures prevented a generated report. Manual review used the actual cached primary sources and curated UniProt, and no provider-named research file was fabricated. Per-gene attempts and validation logs are in `.cache/module-audit-logs/arginine-yeast-ARG7-*`. Abstract-only or bibliographic-only sources are distinguished from full text in reference reviews; unavailable source details are not treated as experimental refutations.

Actions: ACCEPT 9, KEEP_AS_NON_CORE 3, MODIFY 5, UNDECIDED 1. Record sections were backfilled; focused schema/reference validation passed on the initial complete panel. Final targeted checks and HTML rendering are recorded in the audit logs.

## PR #5563 follow-up, 2026-10-26

Restored supported GO:0005739 mitochondrion rows to ACCEPT under the explicit root-organelle policy; existing matrix rows remain separate. Reasons distinguish organelle screens, direct targeting, publication-linked curated evidence and unavailable full text. No original annotation payload changed. Cytosol decisions use target-specific fractionation/processing evidence rather than relationship qualifiers or generic precursor transit. For Aga1, matrix inference does not imply universal post-import autoproteolysis.
