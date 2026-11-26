# TF batch 1: carbon utilization

Date: 2026-11-08. Full GO re-review completed for BenR, HexR, PtxS and CbrB.
This batch follows the 20-case scoped calibration and reviews molecular function,
experimentally supported targets and pathway-regulatory roles together.

| Gene | Review | Structured relationships | Main outcome |
|---|---|---|---|
| BenR / Q88I42 | [GO review](../../../genes/PSEPK/BenR/BenR-ai-review.yaml) | [1 activation relationship](../../../genes/PSEPK/BenR/BenR-regulatory-evidence.yaml) | Refined activator/promoter function; withdrew the authored benzoate-catabolism execution annotation; physical directness and direct ligand binding remain unverified. |
| HexR / Q88P32 | [GO review](../../../genes/PSEPK/hexR/hexR-ai-review.yaml) | [3 direct repression relationships](../../../genes/PSEPK/hexR/hexR-regulatory-evidence.yaml) | Pedd, Pzwf and Pgap-1; removed carbohydrate-metabolism execution and proposed regulation of glucose metabolism. |
| PtxS / Q88HH7 | [GO review](../../../genes/PSEPK/ptxS/ptxS-ai-review.yaml) | [3 direct repression relationships](../../../genes/PSEPK/ptxS/ptxS-regulatory-evidence.yaml) | Pkgu, Pgad and autoregulatory PptxS; added experimentally measured 2-ketogluconate binding and regulation of the peripheral glucose pathway. |
| CbrB / Q88DX2 | [GO review](../../../genes/PSEPK/cbrB/cbrB-ai-review.yaml) | [5 direct relationships](../../../genes/PSEPK/cbrB/cbrB-regulatory-evidence.yaml) | crcZ/crcY, PP2810–13 and PP3420 activation, oprD repression; distinguished ChIP candidates from validated relationships and relief of CCR from execution of CCR. |

These 12 relationships are a documented subset, not complete regulons. Eleven
combine binding and functional regulation; BenR's promoter activation retains
`directness: unresolved`. Direct edges still differ in causal resolution: CbrB
oprD and PP3420 have binding plus expression evidence without functional binding-site
mutations. Each record preserves this limitation, condition, host strain and assay.
A promoter or operon edge is not expanded into separate direct-binding claims for
every downstream gene. iModulon memberships supply none of these target claims.

## Biological corrections and evidence limits

**BenR:** machine-validated support now quotes the cached primary evidence for
KT2442 BenR-dependent ben-gene activation and comparative PRS2000 benA reporter
activity. The earlier KT2440-derived construct observations remain in the notes;
the uncached Fig. 3 phrase is no longer used as a checked quotation. The reviewed molecular function is DNA-binding transcription
activator activity, without requiring a verified direct ligand-binding mechanism.
The UniProt FUNCTION comment describing TOL-plasmid XylS is recorded as a source
text defect; the downloaded source itself is unchanged.

**HexR:** the 2026 paper [PMID:41260329](https://pubmed.ncbi.nlm.nih.gov/41260329/)
reports carbon-source-dependent effects beyond the established glucose-pathway
repression. Its abstract informed the biological summary, but unavailable full text
and supplementary target tables prevented additional activating-edge assertions.
The proposed glucose-regulation GO term rests on the older KT2440 experimental
regulatory mechanism, with term-parent and comparator checks documented.

**CbrB:** GO:0061985 carbon catabolite repression inherits the decrease-in-metabolism
meaning of its parent. CbrB activation of CrcZ/CrcY counteracts downstream Hfq/Crc
repression, so the earlier authored NEW CCR annotation and core process association
were withdrawn. The mechanism is retained as explicit pathway-regulatory context.
No claim that CbrB performs downstream catabolic reactions is introduced.

**Scope:** all existing GO rows were assessed and core functions synthesized.
Unknown mechanism, ligand contact or regulon member is not filled from a family
name or expression module. Gene descriptions remain biological summaries;
assay/strain details and curation decisions reside in notes and evidence records.

The prescribed provider commands returned cached Falcon material for BenR/CbrB.
HexR/PtxS provider research failed authentication/quota, so primary-literature
research was documented manually. PSEPK has no configured MOD-description provider;
FEBA retrieval was unavailable. Neither gap was filled with fabricated files or
claims. Several publication caches are abstract-only; reference reviews and notes
identify which primary full-text sections were inspected online.

## Validation and reproduction

- `just validate PSEPK GENE` passed for all four genes. The only remaining advisories
  concern preferring primary evidence without citing available research summaries.
- The [sidecar schema and interpretation policy](../tf_census/regulatory-evidence.md)
  define target, sign, directness, strain, assay and pathway-context fields.
- `validate_regulatory_evidence.py` checks all 12 relationships against that schema,
  the reference metadata, declared publication references and verbatim source quotations.
  The gene-validation recipe and the whole-repository quote gate include these sidecars.
- Focused regression tests cover bad identity/reference joins, missing assay data,
  duplicate assertions and accidental pathway-execution encoding, alongside the
  existing census/importer regressions.
- Gene and project history records capture the work. The
  [batch manifest](tf_carbon_utilization_01.manifest.json) records final artifact hashes.

```bash
just validate PSEPK BenR
just validate PSEPK hexR
just validate PSEPK ptxS
just validate PSEPK cbrB
uv run python projects/P_PUTIDA/validate_regulatory_evidence.py \
  genes/PSEPK/{BenR,hexR,ptxS,cbrB}/*-regulatory-evidence.yaml
just --justfile projects/P_PUTIDA/tf_census/justfile check
```

## Queue

- [x] BenR
- [x] HexR
- [x] PtxS
- [x] CbrB
- [ ] Next batch: GacA, FleQ, RpoS and Hfq, keeping transcriptional control,
  sigma-factor activity and post-transcriptional control separate.
- [ ] Remaining calibration cases, followed by system/family batches from the census.

The calibration table records 4 full re-reviews and 16 scoped-only assessments;
existing review files for other genes are not counted as newly validated work.

## PR review follow-up — 2026-11-11

The revision adds PtxS effector-binding and pathway-regulation proposals from
PMID:20581202 and PMID:18245293; replaces BenR notes-as-evidence with primary quotes
and explicit strain/inference caveats; preserves BenR metabolic context using
GO:0062013; records CbrB source defects; and links the CbrB module and target evidence.
HexR evidence is target-specific and its KDPG term-granularity question is explicit.
The BenR comparison now contains only the ten published members. The stale quote
baseline was pruned with the repository helper. Provider research is unchanged.

Regulatory quotations now pass through the shared reference validator in both the
project checker and the default CI quote scope. A regression test rejects the old
BenR figure phrase against its abstract-only PMID even when source_url is supplied.

### Review dispositions

Follow-up to [the latest review](https://github.com/ai4curation/ai-gene-review/pull/6208#issuecomment-6790688055):

| Request | Resolution |
| --- | --- |
| 1–2: PtxS coverage | Added the measured effector-binding MF and the missing KT2440 regulon reference; proposed pathway regulation with participation, comparator and ontology checks recorded in notes. |
| 3–4: BenR support | Replaced notes-as-evidence with PMID:11053377 and PMID:18156252 quotations, promoted the first to high relevance, and retained explicit PRS2000/KT2442 provenance. GO:0000987 is an inference; the sidecar still does not claim verified physical directness. |
| 5: Uncached BenR figure quote | Removed it from the checked evidence. The earlier author-manuscript observations remain in notes; only checkable primary text is quoted in the sidecar. |
| 6: Quote-validation coverage | Registered regulatory sidecars in the shared quote checker's default scope, called that same checker from the project validator, and wired companion validation into `just validate`. No bespoke text matcher or new baseline waiver. |
| 7: CbrB source defects | Structured DE/AlgB and CC:PATHWAY defects now export. The name mismatch is confirmed; the pathway transfer is probable and explicitly requests checking. |
| 8: Existing mechanism module | Gene reference/core description and sidecar interpretations point to the module; the module points back to the target-evidence record. |
| 9: Stale baseline | Ran `just local-quote-baseline --prune`; 44 stale entries removed, including the entire BenR key. |
| 10: HexR quote specificity | The reviewer withdrew this objection because the second quote already names the promoters. The first quote is now also HexR-specific. |
| 11–12: Pathway context and term gap | BenR's metabolic row now refines to GO:0062013; HexR has a KDPG-specific term question. |
| 13: PP3420 table | Verbatim cell values are separated with ellipses, with column labels in assay and the source's decimal comma explicitly documented. |
| 14: Legacy comparison | Replaced the obsolete 13-gene analysis with the ten published members and explicit withdrawal of the three non-members and unsupported target conclusions. |
| 15: Non-pilot importer availability | PR description explicitly states that E. coli and B. subtilis routes are unavailable until their datasets are verified. |
| Dependency and taxon notes | Documented the development dependency group and intentional KT2440-only pilot scope; LinkML imports are local to validator construction. |
| Repository policies | Both LinkML-only and provider-preservation policies remain intact; no CLAUDE.md or provider-output change in this follow-up. |

Validation: all four `just validate PSEPK GENE` runs passed; 79 focused tests
(including the cached-publication integration cases) passed; the whole-repository
quote gate had zero blocking failures (222 existing baselined failures and 324
unchecked sources elsewhere). Module schema and semantic checks passed with the
existing two unresolved representative-member warnings and three declared
phosphorelay-conformance warnings. Ruff passed.
