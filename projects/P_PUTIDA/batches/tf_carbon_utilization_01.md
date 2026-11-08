# TF batch 1: carbon utilization

Date: 2026-11-08. Full GO re-review completed for BenR, HexR, PtxS and CbrB.
This batch follows the 20-case scoped calibration and reviews molecular function,
experimentally supported targets and pathway-regulatory roles together.

| Gene | Review | Structured relationships | Main outcome |
|---|---|---|---|
| BenR / Q88I42 | [GO review](../../../genes/PSEPK/BenR/BenR-ai-review.yaml) | [1 activation relationship](../../../genes/PSEPK/BenR/BenR-regulatory-evidence.yaml) | Refined activator/promoter function; withdrew the authored benzoate-catabolism execution annotation; physical directness and direct ligand binding remain unverified. |
| HexR / Q88P32 | [GO review](../../../genes/PSEPK/hexR/hexR-ai-review.yaml) | [3 direct repression relationships](../../../genes/PSEPK/hexR/hexR-regulatory-evidence.yaml) | Pedd, Pzwf and Pgap-1; removed carbohydrate-metabolism execution and proposed regulation of glucose metabolism. |
| PtxS / Q88HH7 | [GO review](../../../genes/PSEPK/ptxS/ptxS-ai-review.yaml) | [3 direct repression relationships](../../../genes/PSEPK/ptxS/ptxS-regulatory-evidence.yaml) | Pkgu, Pgad and autoregulatory PptxS; distinguished glucose/gluconate response from experimentally measured 2-ketogluconate binding. |
| CbrB / Q88DX2 | [GO review](../../../genes/PSEPK/cbrB/cbrB-ai-review.yaml) | [5 direct relationships](../../../genes/PSEPK/cbrB/cbrB-regulatory-evidence.yaml) | crcZ/crcY, PP2810–13 and PP3420 activation, oprD repression; distinguished ChIP candidates from validated relationships and relief of CCR from execution of CCR. |

These 12 relationships are a documented subset, not complete regulons. Eleven
combine binding and functional regulation; BenR's promoter activation retains
`directness: unresolved`. Direct edges still differ in causal resolution: CbrB
oprD and PP3420 have binding plus expression evidence without functional binding-site
mutations. Each record preserves this limitation, condition, host strain and assay.
A promoter or operon edge is not expanded into separate direct-binding claims for
every downstream gene. iModulon memberships supply none of these target claims.

## Biological corrections and evidence limits

**BenR:** KT2440-derived PP_3159/PP_3161 reporter constructs establish activation;
KT2442 experiments provide physiological context, and PRS2000 work remains
comparative evidence. The reviewed molecular function is DNA-binding transcription
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
  the reference metadata and declared publication references.
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
