# PR6175 round-one capacity closure

This additive audit preserves the published capacity consultation and its historical receipts. Reproduce from the repository root:

```sh
uv run python analysis/module_audits/bacterial_isc_iron_sulfur_cluster_assembly/round1/capacity-consultation/check_round1.py
uv run ruff check analysis/module_audits/bacterial_isc_iron_sulfur_cluster_assembly/round1/capacity-consultation/check_round1.py
```

The wrapper imports the preserved checker and uses its actual production `compile_module`/`is_satisfied` path and evidence oracle. It supplies a new ledger containing only reviewed input-hash updates; role assignments, molecular functions, evidence tiers, donor-source bundles and interface decisions are unchanged. The old checker is not executed with its default output destination. Published receipts and results are not rewritten. Released reviewer manifests are snapshotted in this directory so reproduction does not depend on an ignored handoff file remaining locally available.

## Results

- All **38 original scenarios** retain their original outcomes.
- **11 additional scenarios** test folding-only and ATP-binding-only HscA descriptors versus the supported dedicated ATPase, in each of the three taxa, and prevent a complete canonical panel from being misrepresented as evidence for an excluded alternative context.
- The original **six gate sensitivities** and **two structural mutations** pass. Making optional IscA mandatory or requiring both HscA classifications breaks the expected profiles.
- The published circuit's seven atoms and four routes are unchanged. Every route requires one HscA realization, not both; optional IscA accounts for the other route choice.
- All **208 ordered annotation payloads across 18 reviews**, **126 protected source files**, and **13 prior audit artifacts** are preserved. Historical NEW actions remain unchanged. The parent-owned retired PSEPK HscA proposal does not supply a core activity or an oracle function claim.

`closure.json` records exact current module, engine and family-review hashes, old-to-new review hashes, release manifests and the description-only module change. `capacity-results.yaml` records the original scenarios against the new reviews. `additional-controls.yaml` records the extra outcomes. `prior-artifacts.json` pins the published audit files; `evidence-ledger.yaml` is an additive updated-input copy, not a replacement for the original ledger.

## Finding 8 and biological boundaries

The updated module description plainly excludes anaerobic Fdx-independent and scaffold-suppressor routes from the encoded Fdx-supported, HscBA-assisted profile. This follows finding8's explicit-scope option; it does not claim those biological alternatives have been modeled. Their oracle status is `OUTSIDE_CANONICAL_PROFILE`, not biologically impossible. Even when a supplied panel satisfies the canonical Boolean circuit, that alone cannot validate an excluded physiological context.

The HscA variants describe verified subfamily versus family-level classifications of **one biological activity**. This is a representational alternative, not an evolutionary or mechanistic pathway split. The exact representative identity, dedicated ISC signature, ATPase function, same-taxon context and cognate interfaces prevent a generic DnaK/Hsp70 match from satisfying it. Production `module_logic` does not independently enforce taxon or compatibility: those remain explicit evidence-oracle gates. A failed mixed-species fixture is not a prediction that cross-species complementation is impossible.

IscA remains optional. Broad Fe-S binding alone does not establish cluster delivery: AZOVI O31271 is a comparator, not a positive delivery witness. Correcting AZOVI IscU's binding-term refinement does not disturb its independently supported delivery core.

All three panels satisfy the supported-or-inferred profile. The separate-assay-only profile remains supported for ECOLI, while KT2440 remains inferred and AZOVI lacks a demonstrated cognate donor interface. Native AZOVI Fdx redox/essentiality plus specific identity support qualified inference; its HscBA experiment uses apo-Fdx as a **cluster recipient**, not an electron donor. The donor-role and donor-interface gates independently preserve this distinction. Assay-only here means separately assayed roles/interfaces, not simultaneous whole-pathway reconstitution or native flux.

The revised folding actions cannot create generic foldase capacity: all three HscA cores retain ATP hydrolysis, no HscA core asserts GO0044183/GO0140662, and no non-retired HscA folding row is accepted or NEW. ECOLI's negative model-client refolding assay is not transferred as a measured negative in the other taxa. The family assessment remains unresolved at broad scope; no lost-function ancestral node is invented.

No module, family, gene, project, historical receipt or source file was edited by this capacity closure. The root's aggregate curation history can reference this additive receipt. No full-corpus validation was run.
