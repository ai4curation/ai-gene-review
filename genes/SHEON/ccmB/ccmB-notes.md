# ccmB evidence review

## 2026-11-06 cytochrome maturation audit

Persistent marker: CYTOCHROME-SHEON-ccmB-20261106.

Normal accession-aware fetch created the pristine scaffold; its complete original payloads and raw hashes were captured before editing in `.cache/module-audit-logs/cytochrome-20261106/rhodobacter-shewanella/SHEON-ccmB-baseline.json`. All original annotations are retained. Default Falcon research was attempted normally and failed with HTTP 403 authentication/access denial; this file records manual literature review, not a provider report.

PMID40026579 and PMID40167305 full texts and the genuine supplementary Table S2 were reviewed. See [identity and assay scope](ccmB-source-analysis/identity-and-assay-scope.md). Conditional overexpression efflux is retained as non-core; whole-cell HPLC does not directly demonstrate purified membrane translocation or exclude host export factors.

GO:0005886: ACCEPT. Functional CcmB-GFP localization and integral membrane architecture corroborate the plasma-membrane claim. The PAINT inheritance judgment is consistent with this target evidence; paint-losses found no annotated loss. A fusion assay is not an untagged protein localization experiment.

GO:0005886: ACCEPT. Functional CcmB-GFP localization and integral membrane architecture corroborate the plasma-membrane claim. The PAINT inheritance judgment is consistent with this target evidence; paint-losses found no annotated loss. A fusion assay is not an untagged protein localization experiment.

GO:0015232: KEEP_AS_NON_CORE. The MR-1 genomic-library, deletion/complementation and overexpression experiments show reduced cellular heme and increased extracellular heme by HPLC. They support conditional export capacity, not a demonstrated purified CcmB channel: whole-cell efflux does not isolate inner-membrane movement, exclude other host pumps, or resolve outer-membrane transit. Native untagged and His6 controls address the tag, not purified flux. E. coli CcmCD channel mapping challenges universal CcmB-conduit assignment but does not negate the MR-1 overexpression phenotype. Thus the inferred transport claim is retained only as non-core; native conduit identity remains unresolved.

GO:0015886: KEEP_AS_NON_CORE. The MR-1 genomic-library, deletion/complementation and overexpression experiments show reduced cellular heme and increased extracellular heme by HPLC. They support conditional export capacity, not a demonstrated purified CcmB channel: whole-cell efflux does not isolate inner-membrane movement, exclude other host pumps, or resolve outer-membrane transit. Native untagged and His6 controls address the tag, not purified flux. E. coli CcmCD channel mapping challenges universal CcmB-conduit assignment but does not negate the MR-1 overexpression phenotype. Thus the inferred transport claim is retained only as non-core; native conduit identity remains unresolved.

GO:0016020: MODIFY. Functional CcmB-GFP localization and integral membrane architecture corroborate the plasma-membrane claim. The PAINT inheritance judgment is consistent with this target evidence; paint-losses found no annotated loss. A fusion assay is not an untagged protein localization experiment.

GO:0017004: MODIFY. This is a lateral correction from assembly of a cytochrome-containing complex to cytochrome c biosynthesis, already supported by an IBA row. Functional complementation and machinery interactions support CcmB participation; no direct heme-ligation catalysis by CcmB is asserted.

GO:1903607: ACCEPT. Functional rescue by CcmB and its participation in the CcmACD machinery corroborate the PAINT-inferred biosynthetic role. The exact heme conduit is disputed, but that disagreement does not erase participation in maturation. Neither donor count nor a target appearing among seeds is grounds to dismiss the inheritance assertion.

## 2026-11-06 source packaging

Persistent marker CYTOCHROME-SHEON-ccmB-SOURCE-PACKAGING-20261106. Moved the full acquired primary PDF and extraction to the ignored audit acquired-sources cache, preserving byte hashes. The committed source analysis now contains only scoped strain/construct table excerpts and URL/hash provenance. Gene review assertions, quotes, machine payloads, UniProt/GOA files and normal publication caches were unchanged.


## PR6121 round-1 evidence correction (2026-11-06)

- GO:0015232 UNDECIDED: MR-1 efflux phenotypes do not resolve autonomous CcmB membrane-crossing activity.
- GO:0015886 ACCEPT: CcmB participates in heme trafficking, without an asserted autonomous transmembrane conduit.

Current GO definitions were checked against the official QuickGO API. All original annotation payloads, including authored NEW rows, are preserved. Primary scope and construct limits remain explicit; no raw UniProt/GOA, provider report or publication cache was edited. Scoped comparative proof is recorded in the round-1 audit.


## PR6121 reference-finding follow-up (2026-11-06)

Narrowed the top-level finding statements for PMID:40026579, PMID:40167305 to the claims established by their existing quoted passages. Annotation actions, core functions, quotes and source records are unchanged. The original 52-file handoff remains preserved and verified separately; this edit has a supplemental history and manifest.
