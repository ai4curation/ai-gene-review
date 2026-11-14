# Four-member annotation consultation — 2026-11-07

Reviewed BACSU groEL/P28598 and groES/P28599, MYCTU groEL2/P9WPE7 and groES/P9WPE5. The frozen baseline actually contains **64** rows (13 + 7 + 28 + 16), correcting the task's stated 65. All original payload fields and row order are preserved exactly. Eight raw source files and 25 cited publication caches remain byte-identical to their protected hashes.

Decisions: 36 ACCEPT, 15 KEEP_AS_NON_CORE, 1 MODIFY, 9 UNDECIDED, 3 REMOVE; no historical or active NEW rows. REMOVE is restricted to bare protein binding under the explicit project policy. BACSU GroEL's generic folding activity is refined to its existing ATP-dependent activity. Both GroES proteins retain the valid general folding-chaperone term: its current definition includes assistance through binding a protein-containing complex. GroES cores enable chaperone binding and contribute to ATP-dependent folding, without asserting an independent ATPase.

The essential MYCTU GroEL2 cycle is supported by complementation with cognate/E. coli cochaperonin despite weak oligomerization in standard preparations (PMID22834700). Target ATP-independent refolding in lower oligomers (PMID15327959) is retained as an additional observed mode. Surface/capsule adhesion and cleaved-form host-mitochondrial localization are treated as real, non-core activities, not dismissed because E. coli differs. MYCTU GroES metal IBA and IDA rows are both retained based on direct target evidence. BACSU metal and both new GroES ATP-binding rows remain unresolved rather than asserting an untested loss.

Other unresolved claims concern exact mycobacterial membrane/wall localization, the GroES culture-filtrate identification, and the target interpretation of heterologous transcription/heat experiments. Experimental rows were not removed merely because full text or target tables were unavailable.

Primary-method provenance:
- `genes/BACSU/groEL/groEL-source-analysis/PMID12082092-methods-reading.md`: purified HrcA activation used E. coli GroEL/GroES; native Bacillus experiments separately establish GroE dependence and GroEL affinity capture.
- `genes/MYCTU/groES/groES-source-analysis/PMID12837792-reading.md`: target calcium coordination and E. coli comparison are distinguished from speculative ATP transport.

Both papers were accessed externally beyond the cached abstract, so their reference entries do not falsely mark full text unavailable. Shared machine-fetched publication caches were not rewritten. Four additional primary sources (15327959, 18227175, 24830429, 12837792) were fetched normally into previously missing files.

Four real Falcon attempts failed HTTP403 authentication; no provider report was fabricated. Four PAINT checks found no IRD/IKR losses, without claiming a new reconstruction of node placement. Standard record-section backfill added 80 fields in two passes, leaving no ambiguous or unmatched quotes. Four focused validations, four renders/content checks and four generated-history validations pass. Two nonblocking warnings suggest NEW complex rows for GroES; the supported complex remains in the core and no annotation was manufactured solely to silence the warnings.

Reproduce the exact preservation and role-boundary checks from repository root:

```sh
uv run python analysis/module_audits/bacterial_groel_groes_chaperonin_folding/new-cage-member-consultation/verify.py
```

Full logs and exact handoff hashes are in `.cache/module-audit-logs/groel-20261107/new-cage-consultation/`. No module/family/project edits, full validation, commit, push or merge were performed by this consultation.
