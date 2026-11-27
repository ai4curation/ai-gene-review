# Methionine-cycle literature consultation

This is a durable, source-checked consultation for the bacterial SAM–SAH–homocysteine–methionine cycle. It does not edit the module, genes, families or project. `module-evidence.yaml` provides 18 normal-cache-titled `Reference` objects with manual assessments and 18 claim-specific `EvidenceItem` objects grouped by biological role. These objects are checked against the repository's production models and supporting-text validator.

Five genuine reviews were manually assessed. Four have complete available text that was read for the relevant mechanism: PMID21166890, PMID36891755, PMID33339190 and PMID42509803. PMID18953685 was read through its indexed catalytic section, while the normal cache remains abstract-only; direct PMC and publisher access limits are recorded. No abstract-only entry is described as a complete source.

The new full SAH-hydrolase reviews support reversible chemistry, internal NAD redox cycling and lineage-dependent structural variation. A specific 2026 generalization of strong SIH preference to Thermotoga is flagged as disputed, because primary17603473 reports that TM0172 hydrolyzes SIH and SAH approximately equally. This is not a blanket rejection of that review or an inference that the enzyme lacks either activity. No functional-loss node is manufactured from sequence motifs.

## Mechanistic recommendations

The four top-level capacities remain methionine adenosylation, chemically established SAH-producing methyl transfer, homocysteine recovery and homocysteine remethylation. The distributed methyl-transfer role should have a concrete exemplar such as the already COMPLETE main ECOLI CheR review, without becoming universally dependent on CheR's family. CheR follow-up in open PR6100 remains separately owned.

For homocysteine recovery, distinguish direct SahH hydrolysis, the Pfs **and** LuxS sequence, and the matched SAH-deaminase **and** SIH-hydrolase sequence. The latter is directly characterized biochemical capacity in T. maritima MSB8; native flux remains unconfirmed. TM0172/O51933 can also realize direct SAH hydrolysis. Family membership alone cannot force substrate exclusivity.

For remethylation, retain canonical folate-dependent MetE and cobalamin-dependent MetH, while representing experimentally supported alternatives honestly. MesD **and** MesX have a characterized oxygen-dependent, folate/B12-independent context with an unknown physiological methyl donor. Native ADP1 ACIAD3523/3524 genetics and S. koreensis complementation are different experiments. MesB cbdbA481 has direct methylcobalamin-dependent activity; its native corrinoid-protein donor is unresolved, so a specific donor partner must not be invented. The XC1 MmuM and split MetHaHb result is a further real donor/context boundary, currently abstract-only with unresolved exact protein IDs. These limitations do not make the two canonical branches exhaustive for Bacteria.

Donor, cofactor, oxygen and matched-partner gates should be separate from protein presence. Native M. smegmatis mc²155 MetE/MetH context is documented by **PMID33468593**, not the ADP1 studies18319726/18840283. A comparative route pair is not a complete native cycle panel. A strict native-flux profile must remain distinct from an enzyme-capacity profile.

## Source provenance and reproduction

The entire frozen root-worktree preflight was copied byte-for-byte into `preflight/`: 107 files, including its original manifest. `preflight-copy-receipt.json` records every original absolute path, durable destination and SHA256. Original manifests and source bytes retain their recorded paths and contents; their provenance was not rewritten. The dedicated source closure has no dependency on ignored cache files. `followup-sources/` contains separately acquired review XML and access attempts; challenge pages are marked failures and are not scientific evidence.

Normal publication fetching added thirteen missing files, without forcing a refresh. Existing6251075/9201956 and carboxy's33534785 were reused. Every cited title in the new module-ready evidence comes from its normal publication cache. The original 37 protected sources are verified unchanged in `source-preservation.json`. Original full preflight artifacts may include unrelated discovery hits or rejected accessions; only the curated reference ledger and identity decisions designate positive evidence.

Run from the repository root:

```sh
uv run python analysis/module_audits/bacterial_methionine_cycle/literature-consultation/build_consultation.py
uv run ruff check analysis/module_audits/bacterial_methionine_cycle/literature-consultation/build_consultation.py
```

The script validates each `Reference` and `EvidenceItem`, checks all eighteen quotations through the production supporting-text validator, and verifies all 107 imported preflight files. `validation.json` records normal publication input hashes. The handoff freezes the exact durable consultation and newly fetched publications; subsequent gene reviews and module edits require their own receipts.
