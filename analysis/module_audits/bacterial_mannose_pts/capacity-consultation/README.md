# Independent mannose PTS capacity and evidence audit

The final COMPLETE module passes **60 evidence-qualified scenarios, 13 model
mutations and 9 source/context-gate sensitivity tests**. Its three positive
profiles are the matched E. coli K-12 ManXYZ, L. lactis IL1403 PtnAB/C/D and
S. mutans UA159 ManL/M/N panels. Each has three reviewed gene products supplying
four physical roles. A fused IIAB protein fills both A and B; two distinct genes
are not required. No complete active L. curvatus CECT904 quartet was invented.

This is an assessment of supported capacity under stated inputs, not a claim of
measured native flux, sole-route necessity, or biological impossibility wherever
a profile returns false. No scientific files were changed by this consultation.

## What the tests actually execute

`check_capacity.py` imports the repository's production `compile_node`,
`iter_atoms`, `core_atoms` and `is_satisfied`. The actual module compiles into an
AND of `mannose_relay_activity` and `mannose_coupled_transport_activity`.
Neither stage alone satisfies the production circuit. The wrapper does not
replace this circuit with a hand-built graph.

The compiler does not expand protein-complex `active_units`, enforce domain
requirements, identify physical roles, check substrate/input chemistry, enforce
compatible partners, or connect the phospho-EIIB output to the transport input.
The relay atom has no flattened function/family/member/domain identifiers and
reports `is_grounded=false`; its underlying raw active units are nevertheless
explicitly grounded. The transport atom only exposes GO:0022870. A generic
all-atoms-true predicate passes all 57 negative cases. This is a demonstrated
compiler limitation, not a reason to invent a GO identifier for the relay.

The independent oracle reads the **actual raw module active units**, checks each
against reviewed role assignments, current raw UniProt family/domain records,
exact target taxonomy and matched-panel evidence, and then supplies the step
truth values to the production circuit. A final same-B identity check requires
the relay product and transport donor to refer to the same eligible EIIB-bearing
product. Its adversarial test deliberately erases the panel gate and gives the
two stages different B chains: both individual steps then pass but the joined
capacity still fails. Erasing the same-B gate exposes the expected false positive.
This fixture does not assert that such cross-species pairs work experimentally.

Positive membership is not established by a Boolean case label or by an isolated
GO/family match. All nine current reviews must be COMPLETE, have the supported
coupled-reaction contribution core, match the exact accession/taxon, and carry
the appropriate independent domains. The manual source-to-role adjudication is
bounded as described below; the closure checks every underlying released receipt
and quotation. This finite reviewed-panel oracle is intentionally not a classifier
of every possible mannose transporter.

## Evidence and biological limits

| Profile | Evidence qualifying the panel | Limits retained |
| --- | --- | --- |
| E. coli K-12 | Primary ManX domain/phosphoryl-transfer studies, native ManXYZ system work and 2019 ManYZ structure/counterflow; exact PDB-to-reference bridge for ManY and ManZ | Older biochemical caches are partly abstract-only. ManX has intra- and intersubunit transfer; ManYZ trimer-of-pairs stoichiometry does not fix whole-system stoichiometry. Counterflow is not the complete HPr-fed reaction. |
| IL1403 | Primary17284603 names ptnAB/C/D and genome AE005176; native deletion/co-isolation plus primary38047704 sugar-utilization variants; official locus/protein/genome bridge | Receptor rescue is not uptake-flux reconstitution. Some variants retain growth, and alternative transport/background mutations are possible. Component chemistry combines native system evidence with domain inference; E. coli histidine numbering and stoichiometry are not transferred. |
| UA159 | Primary12902269 PEP-dependent uptake and manL mutant, Fig1 plus primary17951382 locus bridge; primary24928869 complete-operon amino-sugar uptake assay | Alternative mannose uptake explains growth compensation. Amino-sugar operon assay is additional system support, not an independent mannose assay for each purified membrane protein. ManL-only rescue is partial; stable full-operon rescue was not obtained. |

C/D receptor behavior and membrane counterflow are separate outputs and do not
supply the missing IIAB relay. Functional membrane, available D-mannose,
phospho-HPr input, a usable phospho-EIIB handoff and supported interfaces are
explicit context gates. `phospho_EIIB` tests usable donor availability at the
transport step; it is not a requirement that every enzyme be phosphorylated
before the relay starts. Upstream PEP/EI/HPr regeneration is outside this module.
The modeled capacity therefore does not assert sufficient energy generation or
positive steady-state flux.

The single PTHR33799:SF1 includes fused ManX and IIA-only LevD. PTHR32502 spans
IIC, IID and soluble downstream carbohydrate proteins. Domains and physical
roles are required independently; one C-like member cannot fill D, and family
membership alone is insufficient. Family reviews retain their explicit uncertain
mannose scope. No arbitrary subfamily is interpreted as a universal positive or
negative grant.

Bacillus LevDEFG is a source-reported fructose/no-mannose comparator. That negative
statement is explicit in primary2117666's abstract, which is the accessed scope;
we do not claim to have read its full negative assay. The actual official LevD/E
split architecture is preserved in the family consultation. The oracle's false
mannose result does not deny their fructose phosphorelay. L. curvatus CECT904's
full primary and U28163 support separate A/B/C plus partial D (87 residues), and
bounded heterologous B complementation. Inactive UniProt records, an incomplete
IID and a different current WDN19 proteome do not supply a reviewed native quartet.

Unsupported cross-panel combinations return false because compatible capacity
has not been demonstrated, not because all cross-species interfaces are impossible.
The actual CECT904 complementation is evidence against that latter universal claim.

## Negative cases and mutations

Each native profile is challenged by removing each A/B/C/D role, removing each
role's domain evidence while retaining broad classification, removing the fused
chain, and changing each input/interface context. Further cases test cross-panel
mixtures, absent source support, C-for-D substitution, IIA-only/general-family
candidates, receptor-only and counterflow-only systems, LevDEFG, and uptake
compensation after UA159 ManL loss. Role ablations and domain-evidence erasures
are computational sensitivity fixtures, not newly performed biological mutants.

The 13 model mutations remove each of the five role occurrences, remove each of
the five domain constraints, replace the transport activity, or make either step
optional. The oracle reads these changes from the model, so defects alter case
outcomes or violate the production required-core contract. Nine gate-erasure
controls show specific false positives when HPr, B donor, membrane, mannose,
interface, source, domain, panel or same-B continuity requirements are omitted.

## Exact closure and preservation

`check_closure.py` verifies **339 inputs**, all five original consultation
manifests and the additive ManX follow-up. Only the exact three ManX review/notes/
render paths are permitted to supersede their original E. coli receipt hashes;
old and new hashes must match the explicit authorized receipt. The original
manifest and all original receipt bytes remain unchanged. This consultation
modifies neither those receipts nor their source files.

All **93 ordered annotation payloads** match the original 63 E. coli rows and
30 newly seeded IL1403/UA159 rows. Both historical NEW rows remain active; no row
was added, retired or deleted. All 43 original/seed protected source files, the
nine additional original provider/prediction files and seven pre-existing target
history files are unchanged. Other accessed inputs and current sources are also
included in the hash closure. Six source-to-locus identity bridges remain bounded
as locus/strain bridges, not independently sequenced assay constructs.

The checker validates **109 unique document/source quotations** in the gene and
family reviews and **14 separately sourced literature findings** against the
actual accessed text. External full texts remain in their original ignored cache;
the literature consultation's durable exact excerpts, acquisition provenance and
source hashes are included. Abstract-only publication caches are never silently
upgraded or replaced. Source matching does not itself establish assay relevance;
the manual source/claim distinctions above and in the released consultations
remain part of the scientific assessment.

Outputs use sorted deterministic iteration. `inputs.json` freezes the final
module, current reviewed inputs and production code hashes and is verified on
subsequent runs. No project/tracker render or shared member-index cache is treated
as a frozen scientific input. Before first release, the initial draft closure was
expanded to include seven existing history files; its unreleased predecessor was
archived in the ignored capacity cache. The final released closure is immutable.

```sh
uv run python analysis/module_audits/bacterial_mannose_pts/capacity-consultation/check_capacity.py
uv run python analysis/module_audits/bacterial_mannose_pts/capacity-consultation/check_closure.py
uv run ruff check analysis/module_audits/bacterial_mannose_pts/capacity-consultation
```

No whole-corpus run, commit, push, source rewrite, or gene/module/family change
was performed by this capacity consultation. Root owns final corpus validation
and publication.
