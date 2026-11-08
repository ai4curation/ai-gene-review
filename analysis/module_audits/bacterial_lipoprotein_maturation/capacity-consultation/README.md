# Independent lipoprotein maturation capacity audit

The final COMPLETE module has SHA256 `5eb2bc3fa15bc15ceca023e6928f5092665f5e65c9334ca7c49b8dc3a8a41e57`. This consultation edits only its own audit artifacts. It does not edit the module, genes, families or sources and does not run full-corpus validation or a member-index build.

## Outcome and experimental boundary

The audit passes35 evidence-qualified scenarios and detects10 deliberate mutations. All14 module representatives resolve to COMPLETE reviews with the correct raw-source taxon and supported core activities/contributions. The88 ordered rows comprise73 preserved initial payloads (including2 historical proposals),2 reused LhaT rows (including1 historical proposal), and13 newly authored proposals. All16 proposal rows remain active; “proposal present” is kept distinct from “newly authored in this audit.” Seven frozen consultation manifests and their external-source hashes are independently verified.

The module's shared capacity is Lgt AND LspA. Optional terminal reactions are not requirements for shared maturation and are not implied by passing that shared core. Product-specific queries separately require a supported terminal route and its external substrate/donor conditions. A mature lipoprotein supplied to an isolated terminal assay is explicit input, not proof that the candidate panel encodes the upstream pathway.

| Reviewed panel | What the evidence-qualified model can establish | What it does not establish |
|---|---|---|
| E. coli Lgt/LspA/Lnt | Complete canonical capacity under supported donor/substrate conditions | Universal activity of every homolog or exact native flux from a Boolean result |
| KT2440 Lgt/LspA/Lnt | Complete inferred capacity from curated family/sequence evidence | KT2440-specific turnover, essentiality or substrate repertoire |
| B. subtilis Lgt/LspA/LhaT | Complete N-acetylation capacity when acetylated carrier reaches the enzyme | A known carrier flippase or direct acetyl-CoA donation to LhaT |
| Bacteroides Lnb exemplars | Target-specific cellular N-acylation, with donor identity unresolved | Complete reviewed native upstream panels or purified-Lnb PG donation |
| S. aureus LnsAB | Compatible-pair terminal activity and purified Sa-pair PG-sn1 preference | Complete reviewed Sa upstream panel, universal pair compatibility or Se donor specificity |
| B. cereus Lit | Intramolecular sn-2 O-to-N transfer retaining two long chains | A third added long chain or a complete reviewed B. cereus upstream panel |

The BF Lnb rescue scenario deliberately combines an E. coli upstream panel with the experimentally tested B. fragilis clone. Its exception is tied to the documented engineered context. It is not a general license to combine proteins from unrelated native taxa. `panel_taxon` identifies the enzyme-source panel; assay hosts and recombinant production contexts are stated separately where they differ.

## Production engine versus biological oracle

`check_capacity.py` invokes the actual production `compile_node`, `core_atoms`, `iter_atoms` and `is_satisfied` implementations. It does not substitute a mock Boolean engine. The resulting circuit has seven reaction atoms and exactly two obligatory core atoms, Lgt and LspA.

The production compiler does **not** descend a protein-complex selector's `active_units`. Consequently, the LnsAB atom carries GO0016747 but no compiled A/B member IDs. The external oracle reads the module's actual nested selectors, requires both distinct roles, checks their official family assignments and their reviewed enabling versus contributing functions, and then uses the independently documented directional pairing assay. A source contract detects deletion of the LnsB unit. A separate weakened-oracle mutation demonstrates that failing to enforce the second partner yields a false-positive LnsA-only case.

Generic GO0016747 matching cannot distinguish Lnt, Lnb and LnsAB. Likewise GO0009003 alone cannot identify lipoprotein signal peptidase II, and PTHR40042 membership does not establish LhaT activity. The oracle requires the actual family selector or named exemplar, appropriate target activity evidence, panel compatibility and reaction-specific context. Synthetic generic-function/family candidates are clearly marked fixtures; they are neither invented accessions nor claims about real unassayed proteins.

Product labels are independently curated oracle outputs, not stoichiometries encoded by the production Boolean compiler:

- Lnt, Lnb and compatible LnsAB produce three-long-chain lipoprotein capacity.
- Lit relocates one existing chain and produces the two-long-chain lyso form.
- LhaT adds a short acetyl group to the two-long-chain substrate; this is distinct from adding a third long chain.

The final module notes explicitly disclose these compiler and oracle boundaries. No unreported engine fix is claimed.

## Source-dependent gates and sensitivities

LnsAB compatibility is directional. SaA+SeB and matchedSeA+SeB produce product in the S. aureus expression host; SeA+SaB does not despite SeA expression. The exact Se sequences are RefSeq/EMBL/UniParc-backed controls, not members silently promoted from failed deleted-UniProt fetches. Only the Sa pair has the purified donor-preference experiment. A successful cellular pairing cannot be reused as a measured purified Se PG-donor result. Neither failure nor success establishes all possible strain/variant combinations.

Lnb positive cellular results are retained without an assigned donor identity. Requiring PG for those results would improperly import Lnt/LnsAB chemistry; that mutation is detected. Conversely, a proposed purified-Lnb reaction with PG is not established by the available evidence and does not pass the evidence-qualified oracle.

LhaT requires an experimentally or independently supported activity assignment plus accessible acetylated lipid carrier. Acetyl-CoA alone fails: it acts upstream in carrier loading. The native carrier-crossing mechanism remains unknown. The known B. anthracis assay-negative homolog constrains universal activity transfer, but its unresolved canonical accession/ancestral placement is not invented. The sensitivity fixture tests the logically separate error of accepting an unassayed family-matching candidate. Current P54392 activity remains positive despite unresolved family-wide scope.

The10 detected mutations cover: dropped partner gate, ignored compatibility, universal LhaT activity, ignored donors, collapsed product chemistry, forced Lnb PG specificity, GO-only matching, ignored taxon context, forced mandatory Lnt in the actual circuit, and deletion of the LnsB unit from the actual module. Results list the cases detecting each mutation and distinguish oracle mutations from module mutations. These are bounded tests of the stated mechanism and evidence gates, not a whole-proteome benchmark.

A false capacity result means the defined input/evidence panel does not establish that profile. It is not interpreted as pathway absence or biochemical impossibility. In particular, missing reviewed upstream members in Bacteroides, Staphylococcus or B. cereus do not establish that those organisms lack Lgt/LspA. No capacity score is relabeled as measured native flux. Native product genetics, purified reactions, cellular complementation and target-homology inference retain their separate evidence scopes.

## Closure and reproduction

`check_closure.py` verifies the seven released manifests, all four family-review source dependencies, the final module hash, and11 manually assessed references (3 reviews and8 primary papers) with23 verbatim findings. Selected mechanism-defining quotes and source hashes are in closure-results.json. The E. coli/Bacillus handoff originally lived in ignored cache; its exact bytes are copied into released-ecoli-bacsu-handoff.json so this audit's reproduction does not depend on that ignored manifest.

Run from the repository root:

```
uv run python analysis/module_audits/bacterial_lipoprotein_maturation/capacity-consultation/check_capacity.py
uv run python analysis/module_audits/bacterial_lipoprotein_maturation/capacity-consultation/check_closure.py
uv run ruff check analysis/module_audits/bacterial_lipoprotein_maturation/capacity-consultation
```

The final input manifest includes the module,14 reviews with local evidence closure, released audit files, current family reviews and the production engine/dependency files. The consultation handoff freezes its own scripts, inputs and receipts. Full validation and publication remain root-owned.
