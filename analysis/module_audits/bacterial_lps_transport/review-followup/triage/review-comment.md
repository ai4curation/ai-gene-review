**Claude finished @cmungall's task in 9m 8s** —— [View job](https://github.com/ai4curation/ai-gene-review/actions/runs/42360618584)

---
### Review: PR #6190 — bacterial LPS transport module audit

- [x] Gather context (diff scope, changed curation files)
- [x] Load `aigr-pr-review` skill conventions
- [x] Review `modules/bacterial_lps_transport.yaml`
- [x] Review new + modified gene reviews
- [x] Review six PANTHER family reviews
- [x] Verify PMIDs, PANTHER labels, GO ancestry, local-file quotes
- [x] Check CI / validation status
- [x] Post review

---

### Summary checklist

- [x] Schema validation passes — *"Build and test" run [42360618629](https://github.com/ai4curation/ai-gene-review/actions/runs/42360618629) is green. `just`/`uv` are unavailable in this runner, so I could not re-run `just validate-all` locally; I verified quotes, GO ancestry and PANTHER labels by hand instead.*
- [x] All PMIDs verified as real — every cited PMID resolves to a cached `publications/PMID_*.md`, including the new PMID:41285762, PMID:41407669, PMID:42844470, PMID:15192148, PMID:21705335.
- [x] Supporting text matches publication content — spot-checked the new quotes against the caches (allowing for line wrapping); all present verbatim. Local `file:` quotes in `analysis/module_audits/.../primary-evidence.md` and `tree-evidence.md` also match.
- [x] GO terms correct and specific — checked the non-obvious ones against QuickGO ancestry captured in `ecoli-consultation/go-ancestors.json`: `GO:0140332` is **not** under `GO:0017089`, and `GO:0015920` is **not** under `GO:0046836`, so the two LptH `MODIFY`s are correctly described as lateral specificity corrections rather than refinements. All seven PANTHER labels are verbatim-correct against `interpro/panther/panther.obo`.
- [ ] Review actions well-justified — mostly yes; one family-scope downgrade loses information (#2 below).
- [x] Core functions accurately identified — with one evidence-attachment slip (#3).
- [x] No over-annotation issues missed — the LptM/LptY accessory roles are modelled as optional, taxon-qualified, and explicitly non-autonomous. Good restraint.

**What is strong here.** This is careful work. The `yedD`/LptY `source_defects` entry is correct and well-evidenced: UniProt P31063 carries only a `{ECO:0000255|PROSITE-ProRule:PRU00303}` "Cell membrane; Lipid-anchor" prediction, and PMID:41285762 identifies the protein as an OM lipoprotein — `MODIFY` to `GO:0009279` plus a `REPOINT` defect is exactly right. The `lptH` naming decision (folder/`gene_symbol` `lptH` against UniProt's `lptA`, with the collision against the lipid A phosphoethanolamine transferase documented in `description`, module `notes` and `reference_review`) is the right call and is properly justified. Separating the meningococcal LptD-dependent delivery endpoint from canonical LptDE, rather than asserting a general LptE bypass, is a genuinely good piece of modelling, and the H44/76-vs-MC58 strain/sequence distinction is held consistently throughout. Dropping the PMID:15919996 aggregate-topology quote from the PSEPK localization rows (and marking it `MEDIUM` / `full_text_unavailable`) is a real improvement.

---

### 🟡 IMPORTANT

**1. Gitignored `.cache/` artifacts committed, including copyrighted publisher full text — and seven notes cite cache files that were *not* committed.**

`.gitignore:65` ignores `.cache`, yet this PR force-adds nine files under it. One of them, `.cache/module-audit-logs/lps-20261107/literature-consultation/2024-review.txt`, is the full text of PMID:38816673 (`© The Author(s), under exclusive licence to Microbiological Society of Korea`, Springer), and `AEQZ01.dat.gz` is a 1.6 MB genome blob. Everything else from this audit already lives under `analysis/module_audits/bacterial_lps_transport/`, which is the established home for consultation material.

Worse, the inverse also holds: seven PSEPK notes files point at cache paths that are **not** in the PR —

```
.cache/module-audit-logs/lps-20261107/psepk-consultation/falcon-{lptA,lptB,lptC,lptD,lptE,PP_0982,PP_0983}.log
```

`ls -R .cache/module-audit-logs/` shows only the `literature-consultation/` directory. So the provenance pointers in the notes are dangling while unrelated cache content is committed. Please pick one convention: drop the `.cache/` additions and either move the needed provenance into `analysis/module_audits/…` or remove the path citations from the notes.

[Fix this →](https://claude.ai/code?q=On%20branch%20cmungall%2Faigr-lps-taxon-audit%2C%20remove%20the%20committed%20.cache%2F%20files%20(.cache%2Fmodule-audit-logs%2F%20and%20.cache%2Fpanther_trees%2F)%20since%20.gitignore%20line%2065%20ignores%20.cache%20and%202024-review.txt%20is%20copyrighted%20publisher%20full%20text.%20Then%20fix%20the%20seven%20dangling%20references%20to%20.cache%2Fmodule-audit-logs%2Flps-20261107%2Fpsepk-consultation%2Ffalcon-*.log%20in%20genes%2FPSEPK%2F*%2F*-notes.md%20--%20those%20files%20are%20not%20committed.&repo=ai4curation/ai-gene-review)

**2. `PTHR45772` `GO:0015920` scope: `SUBFAMILY_ONLY` → `UNRESOLVED` discards a correct, useful narrowing.**

`interpro/panther/PTHR45772/PTHR45772-review.yaml` previously said:

```yaml
scope: SUBFAMILY_ONLY
scope_reason: LPS export is specific to the LptB subfamily; the amino-acid ATPases of the family do not participate in it.
applicable_subfamilies:
- id: PANTHER:PTHR45772:SF10
```

and now says `scope: UNRESOLVED` with `applicable_subfamilies` deleted. The new `scope_reason` is entirely about uncertainty *inside* SF10 (Deinococcus Q9RSJ0, Thermotoga Q9X0E4, plant/algal-labelled leaves). That is a fair point, but it does not disturb the *between*-subfamily fact the old value encoded — the amino-acid ABC ATPase clades (SF7/SF11, which this same file still assesses as "Amino-acid clade only … LptB excluded") certainly do not export LPS. `UNRESOLVED` is defined in the schema as "Investigated but undecided", so the file now says nothing about the one thing that was decided, and the main downstream use of this assessment (stopping `GO:0015920` spreading onto amino-acid transport ATPases) is lost.

`SUBFAMILY_ONLY` with `applicable_subfamilies: [PTHR45772:SF10]` plus `member_exceptions` for Q9RSJ0/Q9X0E4 expresses both facts — and this PR already uses `member_exceptions` that way in `PTHR30189` for the two *Ricinus* leaves. (The `PTHR30189`/`PTHR38098` `FAMILY_WIDE` → `UNRESOLVED` moves are more defensible, since those families really are one subfamily spanning LPS and non-LPS diderms; it is specifically the loss of `applicable_subfamilies` on PTHR45772 I'd push back on.)

[Fix this →](https://claude.ai/code?q=On%20branch%20cmungall%2Faigr-lps-taxon-audit%20in%20interpro%2Fpanther%2FPTHR45772%2FPTHR45772-review.yaml%2C%20restore%20scope%3A%20SUBFAMILY_ONLY%20with%20applicable_subfamilies%20PANTHER%3APTHR45772%3ASF10%20for%20the%20GO%3A0015920%20term%20assessment%2C%20and%20record%20the%20Deinococcus%20Q9RSJ0%20and%20Thermotoga%20Q9X0E4%20uncertainty%20as%20member_exceptions%20plus%20scope_reason%20text%20instead%20of%20collapsing%20the%20whole%20assessment%20to%20UNRESOLVED.&repo=ai4curation/ai-gene-review)

**3. `genes/ECOLI/lptE` — core function supported by a quote about two other proteins.**

`genes/ECOLI/lptE/lptE-ai-review.yaml:711-714` attaches to the *LptE LPS-binding / luminal-plug* core function:

> Whereas LptY binds and stabilizes the periplasmic LptD β-taco domain that functions as LPS receptor, LptM intercalates the lateral gate of the β-barrel domain, promoting its opening and access by LPS.

The sentence is about LptY and LptM and says nothing about LptE, so it does not support that core function. (The identical quote in `genes/ECOLI/lptD/lptD-ai-review.yaml` *is* on-topic — both clauses describe LptD domains — so this is a single misplaced row, not a systematic problem.) Either drop it or replace it with an LptE-specific sentence from the same paper.

[Fix this →](https://claude.ai/code?q=On%20branch%20cmungall%2Faigr-lps-taxon-audit%2C%20in%20genes%2FECOLI%2FlptE%2FlptE-ai-review.yaml%20around%20line%20711%2C%20the%20first%20core_functions%20entry%20(LptE%20binds%20LPS%20and%20acts%20as%20the%20luminal%20plug)%20has%20a%20supported_by%20quote%20from%20PMID%3A41285762%20that%20is%20entirely%20about%20LptY%20and%20LptM%20and%20does%20not%20mention%20LptE.%20Remove%20it%20or%20replace%20it%20with%20an%20LptE-specific%20verbatim%20quote%20from%20the%20same%20cached%20publication.&repo=ai4curation/ai-gene-review)

**4. Curation framing has migrated into `description` and family `summary` fields.**

CLAUDE.md asks the top-level `description` to be a project-independent biological summary a biologist can read cold, with curation commentary kept in notes / `review.reason`. Several of the new and rewritten descriptions end on defensive framing instead:

- `genes/ECOLI/lptM:12-14` — "…it is not an autonomous transporter or oxidoreductase and is not universally required across bacterial LPS pathways."
- `genes/ECOLI/yedD:12-13` — "…its role is structural support within the transport machinery rather than an autonomous transport reaction."
- `genes/NEIMB/lptE:12-13` — "This supports an assembly/stability role without requiring LptE to be an indispensable LPS translocation factor in MC58 or in every meningococcal condition."

The same pattern shows up in the family `summary` rewrites, where concrete biology was traded for hedging. `PTHR33529` lost "six transmembrane helices and a periplasmic beta-jellyroll domain … V-shaped cavity that LPS enters laterally … ATP hydrolysis by the cytoplasmic LptB dimer", the YjgP/YjgQ former names and the Slr0882 naming note; `PTHR30189` lost "N-terminal periplasmic beta-jellyroll domain … C-terminal 26-stranded beta-barrel" and the Imp/OstA synonym. The caveats are worth keeping — they just belong in `coherence_reason`, `scope_reason`, `notes` or `review.reason`, with the architectural description retained in `summary`.

---

### 🔵 SUGGESTIONS

**5. Neisseria primary evidence is routed through a file this PR authored.** All the PMID:21705335 quotes in the three Neisseria reviews cite `file:analysis/…/neisseria-consultation/primary-evidence.md` rather than the PMID. The reasoning (cache is abstract-only, full text acquired externally) is sound and documented with a SHA256, but it means the quote validator checks those sentences against a file added in the same PR. Adding the full text to `publications/PMID_21705335.md` would let the quotes be validated against the publication itself.

**6. Prefer the factual quote over the methodological one.** `supporting_text: "Sequence identity supports protein-role transfer in a matched biological context."` appears as `supported_by` on roughly ten annotation rows across `NEIMB/lptE`, `NEIMB/lptH` and `NEIMH/lptD`. That sentence is the audit's own methodological premise, not evidence. The checkable fact — "All three matches are exact and unique among 2,423 translated CDSs." — is already quoted in the `references` block and would be the stronger citation on those rows.

**7. `genes/NEIMH/lptD:29-38`.** The `GO:0009279` `ACCEPT` reason states "The H44/76 protein is experimentally localized to purified outer membranes in PMID15192148", but the quote supplied is "Thus, Imp functions in LPS transport to the outer leaflet of the OM." — a functional conclusion, not a localization result. Either add the fractionation sentence from the paper or soften the reason to match what is quoted.

**8. Terminal-step variant coverage vs the declared taxon envelope.** The module declares `NCBITaxon:2 Bacteria` but its `terminal_lpt_profiles` REALIZER set offers only two taxon-gated variants (Gammaproteobacteria and *N. meningitidis*), so other LPS-bearing diderms — Bacteroidetes, Alphaproteobacteria — match no terminal profile. `capacity-consultation/README.md` makes clear the compiler does not enforce context, so this is not an operational failure, and the module `notes` do say Bacteria is an envelope rather than a capacity claim. A one-line note on the variant set that absence of a profile means "not curated here", not "no capacity", would stop a reader drawing the wrong inference.

**9. Diff readability.** A large share of the 123k added lines is YAML re-wrapping of untouched prose, interleaved with the substantive edits, plus multi-thousand-line JSON artifacts. Splitting a mechanical reflow commit from the scientific commit would make the next audit of this size much easier to review.

---

**Verdict:** requesting changes for the four 🟡 items — chiefly the committed/dangling `.cache/` provenance (#1), the `PTHR45772` scope regression (#2), and the misattached LptE quote (#3). None of these touches the core biology, which is sound; the LPS-transport modelling and the Neisseria strain discipline are the strongest parts of this PR.
 · [branch `cmungall/aigr-lps-taxon-audit`](https://github.com/ai4curation/ai-gene-review/tree/cmungall/aigr-lps-taxon-audit)
