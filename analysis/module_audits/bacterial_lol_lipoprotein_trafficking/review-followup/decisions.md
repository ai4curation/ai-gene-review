# PR6188 independent follow-up

Reviewed published head `3e39404c7489f005bdaba72cce4eabfe0db0337b`, review 5811879438 and [detailed comment 6706032620](https://github.com/ai4curation/ai-gene-review/pull/6188#issuecomment-6706032620). The immutable pre-edit snapshot covers 17 reviewed proteins and 148 ordered rows, including 14 existing NEW proposals. This follow-up adds, deletes and retires none.

## 1. LolB location specificity

The requested refinement is supported for Q88PX4 and Q6F8J1. Their specific HAMAP MF_00233 or TIGR00548 identity, secretion signal and lipidated mature cysteine support the anchored LolB architecture. Positive LolA-to-LolB transfer in PMID9384574 supplies the periplasmic interface evidence; neither target is claimed to have undergone direct topology measurement. GO0031241 explicitly includes proteins attached to the periplasm-facing outer-membrane leaflet. The two GO0009279 rows now MODIFY to GO0031241, and both core locations match. E. coli and F. johnsoniae location decisions remain unchanged. The F. johnsoniae inference still explicitly distinguishes SPII architecture/native trafficking evidence from target topology measurement.

## 2. Annotation-specific reasons

The mixed LolB/LolD sentence is removed. PSEPK LolB reasons describe terminal cargo acceptance/insertion; LolD reasons describe ATP-driven release. All five KT2440 reviews now have row-specific reasons explaining the relevant function, compartment, refinement or coupled contribution. Shared ortholog-versus-target assay scope is recorded in notes and reference assessments instead of repeating the same caveat in every row. Positive role-specific inference remains explicit where needed. The existing LolD transmembrane-transport REMOVE and C/E/D complex-contribution judgments are preserved.

## 3. Module labels: parent-owned correction

`module-record-labels.json` contains exact names, RecName/SubName status, frozen UniProt paths and hashes for all 17 proteins. In particular A5FL25 is `Hypothetical lipoprotein`, A5FI22 is `Possible lipoprotein carrier protein LolA`, Q6F8J1 is `Outer-membrane lipoprotein LolB`, Q9EYM2 is `Lipoprotein-releasing system ATP-binding protein LolD`, and A0ACM8PZZ0 is `Transport protein of outer membrane lipoproteins (ABC superfamily, membrane)`. This is a provenance-label correction, not a withdrawal of source-established function. Functional intent belongs in preferred_term and the biological description. Root owns the module edit; this consultation does not change the module.

## 4 and 6. One insertion activity concept

There are five occurrences, including PSEPK LolB in addition to the reviewer's four. All now share the exact definition: "Directly binding a mature lipoprotein and promoting incorporation of its lipid anchor into the bacterial outer membrane." All use GO0140318 protein transporter activity as parent. This states the common terminal activity without requiring a separate periplasmic donor, which would improperly exclude a bifunctional carrier/insertase.

Fresh QuickGO definitions are archived in `ontology.json`. GO0140598 describes carriage with cargo, GO0140306 describes inner-membrane release, and GO0032977 requires a transmembrane-domain-containing protein client. Lipoprotein lipid-anchor insertion is not captured by the latter term merely because both involve a membrane. The same parent and definition remove the export collision while preserving every gene's distinct evidence: E. coli positive transfer/incorporation, target-specific ortholog inference for KT2440/ADP1, native UW101 trafficking plus structural inference, and the explicitly bounded engineered Caulobacter construct. No direct native Caulobacter insertion assay or purified UW101 insertion chemistry is newly asserted.

## 5. Fjoh_2111: relation precision and destination-specific process

The literal CACAO qualifier `acts_upstream_of_or_within_positive_effect` includes *within*; it is broader than an inferred carrier-role relation, but is not logically incompatible with direct participation. The transport claim remains ACCEPT. A source_defects entry asks CACAO to CHECK the more precise `involved_in` relation with SUSPECTED confidence. It explicitly says this is not a confirmed error. No original qualifier, ECO identifier, evidence entity, reference or term is rewritten, and no false GO-term replacement is invented solely to change a relation.

Native UW101 deletion/complementation and reduced outer-membrane GldJ/GldK abundance, together with the specific LolA architecture, support inferred carrier participation. Those findings also support GO0044874 in the independently synthesized core summary. The previous reason rejected only a false descendant refinement from GO0042953, not the localization biology. Its revised wording now states that distinction directly. The core summary need not mechanically produce an additional annotation row; neither comparison to sibling insertases nor a validator coverage suggestion is by itself evidence of a missing annotation. No NEW row is manufactured. The retained source evidence supports a combined experimental/computational interpretation, not purified target transfer kinetics. Gliding and T9SS remain downstream client-dependent consequences.

## 7. ATP binding and the core summary

No further change is warranted. ATP binding is an integral substrate-engagement step and correctly ACCEPTed, while the concise LolD core summary represents the ATPase/release mechanism. A core_functions list is a synthesis, not an exhaustive mirror of every ACCEPTed binding term. Adding a redundant second core entry is unnecessary. Existing positive binding actions and the ATP-hydrolysis activity remain unchanged.

## Family, module and dependency consequences

The reviewed family scope and PAINT assertions do not require alteration for these findings; no family file is changed. Root should update module record labels using the supplied map. Locations now agree with its existing classical-LolB annoton, and the shared proposed activity name is unchanged, so no capacity topology change is requested. Prior frozen manifests remain historical; apply this release's exact additive supersession map rather than rewriting old receipts. The ECO-import PR6186 dependency hold is unchanged. Focused tests run against the existing Lol checkout, which already contains the proposed dependency code; their success does not establish that the upstream dependency has merged.
