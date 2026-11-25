# ImuABC module capacity consultation

Reviewed 2026-11-07 against the live module and all eleven finalized original member reviews plus the subsequently released Myxococcus accessory review. The exact module/compiler hashes and immutable input hashes are recorded in `capacity-results.json` and `input-preservation.json`. No gene, family or module file was edited by this consultation.

## Assessment

The current required topology is biologically defensible for the three-component effector cassette: one ImuA-type accessory realizer, ImuB and DnaE2. ImuA and ImuA-prime are alternatives, not two required accessory proteins. RecA/LexA are optional induction context in this capacity boundary. This does not mean that a native inducible cassette functions without its transcriptional response: Caulobacter's reported damage induction is RecA-dependent. The model tests an available, active cassette in a compatible host replication environment, not its expression state or realized mutation rate.

The three positive panels have different evidence bridges. Pseudomonas physiology uses PaW85, explicitly stated isogenic to KT2440. Caulobacter physiology uses NA1000 derived from CB15. Mycobacterial evidence combines H37Rv genetics and target-protein yeast two-hybrid with M. smegmatis individual accessory, catalytic and clamp-interface tests. None is mislabeled as a purified three-protein reconstitution of the reference strain. The core molecular activities in the gene reviews distinguish these inferences from direct assays. All twelve reviews are COMPLETE; all nine effector proteins have supported TLS or error-prone-TLS core participation, and ImuB/DnaE2 carry the required adaptor/polymerase core functions.

The earlier stale RecA core quotation, Caulobacter strain ambiguity and asserted recruitment timing were corrected by root during consultation. Root also corrected the two remaining discrepancies identified here: the module's old claim that the PTHR32294 review excludes DnaE2 from DNA replication, and the inference that a genome carrying this cassette typically lacks Pol V merely because the systems are described as nonorthologous replacements. The current family review recognizes specialized TLS as a DNA-replication process and keeps proofreading target-dependent. No remaining scientific blocker was found in the audited eleven-member capacity interpretation.

## Capacity oracle and controls

`check_capacity.py` calls production `compile_node`, `iter_atoms`, `core_atoms` and `is_satisfied` on the current module, retaining its actual annoton IDs. Its positive expectations come from the independently documented matched experimental panels in `evidence-ledger.yaml`. It checks actual frozen UniProt family/domain cross-references, reviewed and supported core roles, the module's representative identities and required molecular functions, and the panel's target-taxon and compatibility evidence. It does not infer activity from a PANTHER or Pfam match.

For ImuA, the process-level core plus exact independently assessed accessory identity is used because target molecular activity remains unresolved. For ImuA-prime no unified family ID is asserted in the module, so exact reviewed identity and the characterized accessory relationship provide the bounded gate. No family ID is invented. GO0042276 entails GO0019985 according to the saved official QuickGO ancestor response; the checker verifies that relationship before accepting the specific process core.

The 63 cases cover three complete panels, every missing/single effector, optional regulators, no cassette-level evidence, family hits without reviewed cores, mixed taxa, wrong accessory, RecA substitution, missing adaptor or polymerase functions, unsupported/unreviewed cores, generic type-C or mixed SulA-family classification, and isolated ATP/DNA-binding activity. The mixed-panel negatives mean compatibility is unestablished in this evidence panel, not that every cross-species reconstitution is impossible. A separate deliberately naive accession-only oracle accepts a mixed-species assembly; this demonstrates the actual limitation that the evidence oracle corrects.

## Compiler and biological limits

- The production static compiler does not enforce taxa, assay conditions, pair compatibility, reaction substrates, clamp availability, stoichiometry, concentrations, recruitment timing, or causal connections. Those are not validated by a passing Boolean formula.
- `EXACTLY_ONE` is satisfiability OR in the production compiler. It does not require the alternative accessory protein to be absent. The direct compiler controls demonstrate that each alternative works, multiple alternatives need not be required, and coexistence is not rejected.
- The beta clamp, compatible replication machinery, lesion-containing primer/template, dNTPs and active expression state are external assumptions. If the module is later used to claim autonomous biochemical reconstitution or all-host genomic capacity, these assumptions need explicit resources/constraints rather than relying on this bounded cassette test.
- Actual family membership supports identity but cannot distinguish every inactive ImuB from all catalytic Y-family proteins. PF00817 is broad. Likewise generic PTHR32294/polymerase activity does not establish DnaE2 specialization, and mixed PTHR35369 membership does not identify an ImuA accessory role. Exact role/core gates prevent those transfers here.
- Q1D5A2/MXAN_3991 is a verified Myxococcus ImuA accessory witness, supported by the 2021 primary-promoter-to-locus/translation identity bridge and the separately released gene review. Its measured ATPase supports the specific role, but the entire Myxococcus cassette remains unestablished in this sparse panel. The 2024 supplement does not supply a complete synthetic construct sequence/accession; its linkage to the 2021 protein rests on name, length and residue/experimental context, not a second exact sequence match. Native imuA loss reduces rather than abolishes all induced mutagenesis: the required-accessory test describes the specified ImuA-containing implementation, not every residual TLS mechanism.
- The ATPase gate identifies an activity-bearing Myxococcus realizer. Measured hydrolysis does not establish causal necessity of ATP turnover for native TLS, and failure of that qualified branch is not a negative mutant-function prediction.
- Native mutation output is conditional. Pseudomonas stationary-phase antimutator and MMS-induced mutagenesis observations coexist; neither is converted into a universal property of TLS, of all ImuABC systems, or of all bacteria.

## Additional family scope risk

The verified Myxococcus ImuA record carries PTHR45900:SF1 and base PTHR45900 despite its RecA-like name. That membership must not automatically grant RecA strand exchange or GO0140664 damage sensing. Root corrected the family review's former FAMILY_WIDE sensor claim to UNRESOLVED, retaining positive canonical RecA evidence without asserting a negative ImuA activity result. The exact-member/core-role oracle already prevents Q1D5A2 from filling the optional RecA sensor atom. The current module likewise makes the exact activity qualification explicit; no family file was changed here.

## Reproduction

From the repository environment:

```sh
uv run python analysis/module_audits/bacterial_imuabc_damage_induced_mutagenesis/module-capacity-consultation/check_capacity.py
uv run ruff check analysis/module_audits/bacterial_imuabc_damage_induced_mutagenesis/module-capacity-consultation/check_capacity.py
```

The checker overwrites only its own results file, asserts the unchanged twelve reviews, twelve raw records and three Myxococcus identity/scope records, and fails visibly if the audited role structure or required molecular functions change. It is a focused evidence-panel consultation, not a full gene-corpus or module-schema validation.
