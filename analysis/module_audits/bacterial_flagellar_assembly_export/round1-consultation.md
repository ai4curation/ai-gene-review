# PR6138 round-1 annotation-reviewer consultation

Consultation date: 2026-11-06. Inspected local and published head `6e30fe576b9556ec082fbc13d91d35277f9cc976`; review [comment 6695224473](https://github.com/ai4curation/ai-gene-review/pull/6138#issuecomment-6695224473). Scope: blocking points 1, 4 and 5, plus the anatomical-refinement suggestion. Chemotaxis adjudication is separately owned by the integration reviewer. Source publications were read without modification or refresh.

## Verified ontology, not label-based inference

These are live official QuickGO results retrieved on the consultation date. The linked definition endpoint returns the complete term definition; ancestor endpoints explicitly request `is_a,part_of`. Responses and retrieval URLs are retained in the ignored `round1/member-corrections/` audit cache.

| Term | Definition and verified relationship |
|---|---|
| [GO:0016887 ATP hydrolysis activity](https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0016887) | Catalysis of ATP hydrolysis to ADP and phosphate; the definition explicitly permits its use to drive transport. |
| [GO:0008564 protein-exporting ATPase activity](https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0008564) | Defines transfer of protein across a membrane coupled to ATP + water consumption and ADP + phosphate formation. [Ancestor closure](https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0008564/ancestors?relations=is_a,part_of) **does not include GO:0016887**. |
| [GO:0030257 type III protein secretion system complex](https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0030257) | A protein-secretion complex, chiefly at the cytoplasmic membrane, with a cytoplasmic, probably membrane-associated ATPase. The definition does not expressly exclude flagellar systems. |
| [GO:0120102 bacterial-type flagellum secretion apparatus](https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0120102) | Names the flagellar membrane components and soluble FliI/FliH/FliJ components. [Ancestor closure](https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0120102/ancestors?relations=is_a,part_of) **does not include GO:0030257**, but does include GO:0009288. |
| [GO:0042802 identical protein binding](https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0042802) | “Binding to an identical protein or proteins.” This is not the bare GO:0005515 term. |
| [GO:0003774 cytoskeletal motor activity](https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0003774) | Explicitly covers torque producing flagellar rotation and energy from either nucleoside-triphosphate hydrolysis or an electrochemical proton gradient. The label alone does not restrict it to actin/microtubule motors. |
| [GO:0140605 proton motive force-driven motor activity](https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0140605) | Defines motor activity driven by an electrochemical proton gradient and explicitly mentions bacterial flagella. Both the [combined closure](https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0140605/ancestors?relations=is_a,part_of) and [is_a-only closure](https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0140605/ancestors?relations=is_a) **include GO:0003774**. |
| [GO:0005576 extracellular region](https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005576) | Space external to the outermost cell structure. |
| [GO:0009422 bacterial-type flagellum hook-filament junction](https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009422) | Region where hook and filament meet. [Ancestor closure](https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009422/ancestors?relations=is_a,part_of) **does not include GO:0005576**, but **does include GO:0009288**. |
| [GO:0009424 bacterial-type flagellum hook](https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009424) | Portion connecting filament to basal body. [Ancestor closure](https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009424/ancestors?relations=is_a,part_of) **includes GO:0009288 bacterial-type flagellum**. |

## Point 1: valid action-consistency correction, with a mechanistic qualification

In `genes/SALTY/fliI/fliI-ai-review.yaml`, retain GO:0016887 and GO:0030257 as ACCEPT, alongside the supported export activity and flagellar apparatus location. This agrees with the E. coli review and avoids describing absent ontology edges as hierarchy refinements.

The reviewer's stronger argument that replacing GO:0016887 necessarily discards the chemistry is overstated: GO:0008564 itself explicitly includes ATP hydrolysis in its net reaction. Absence of a graph edge is not proof of biological incompatibility. The reason for keeping both is their independently supported claims and current classification, not a claim that export lacks hydrolysis.

Primary support:

- PMID8943245, cached abstract: purified functional His-tagged Salmonella FliI has “an ATPase activity of 0.16 s-1 at 25 degrees C and pH 7” and requires Mg2+. This directly supports hydrolysis; it is not E. coli enzymology.
- PMID29946050, cached full text: in inverted membrane vesicles, the hydrolysis-defective E211Q protein can bind ATP, form a ring and associate with the gate, but did not support FlgD transport under the tested conditions. The paper concludes that export can be driven by FliI ATP hydrolysis without bulk PMF. This is a defined reconstitution, not a claim that native export always relies exclusively on ATP.
- PMID21934659 and PMID26916245 describe the export-associated FliH/FliI/FliJ machinery and basal-body-associated FliI ring. The complex interpretation does not identify flagellar FliI as an injectisome ATPase.

Only the two SALTY actions change; original payloads and historical NEW rows remain intact.

## Point 4: retain functional self-association; clarify evidence and core synthesis

Do not automatically downgrade ECOLI FliI GO:0042802 to KEEP_AS_NON_CORE. Homo-oligomerization builds its functional ATPase ring; this is a mechanistic assembly property, not an unrelated peripheral interaction. The bare-protein-binding exception does not apply automatically to this specific term. A core synthesis need not reproduce every accepted GO identifier as an independent activity.

PMID12787361, full primary text, reports sixfold rings and states: “Enzymatic activity of the FliI ATPase showed positive co-operativity, establishing that oligomerization and enzyme activity are coupled”. The experiments used purified Salmonella FliI, including full-length protein released from a GST fusion by thrombin; E. coli phospholipids were a reagent, not evidence that E. coli FliI was assayed. PMID21278755 independently reports FliJ-promoted FliI hexamer formation in the Salmonella system.

The E. coli PMID8604139 interaction table is not verified from its cached abstract. Its absence from the abstract is neither proof that the original curator was wrong nor direct evidence for the precise interaction. Preserve the experimental attribution and explicitly distinguish this source limitation from independent homolog evidence for the integrated self-association judgment. Incorporate homohexamer formation into the existing catalytic core description with the primary oligomerization support. Do not manufacture an independent new GO annotation, or claim newly verified E. coli kinetic measurements.

The initial self-association consultation left chemotaxis unchanged. Subsequent integration-review adjudication authorized MARK_AS_OVER_ANNOTATED for the original GO:0006935 NAS row: PMID31337100 supports export and construction, not FliI-mediated ongoing propulsion, steering or gradient-dependent motor regulation. Construction alone does not establish the guided-movement claim. This does not exclude all possible secondary roles, does not equate export components with torque-producing stators, and does not rely on the reviewer's incorrect assertion that UNDECIDED is limited to inaccessible publications. The exact export quote and original payload remain intact.

## Point 5: reviewer concern resolved by current ontology; old rationale is incorrect

Retain the GO:0003774 → GO:0140605 refinement in PSEPK FliF and FliG. The latter is a genuine is_a descendant, and the parent definition explicitly includes proton-gradient-driven flagellar rotation. Restoring “wrong kind of motor” would introduce an ontology error.

FliF supplies the MS-ring rotor structure; PMID39766194 describes its rotor and assembly-template roles. FliG contributes the rotor–stator torque interface, as synthesized in PMID31452860. These are comparative mechanism/structure sources, not KT2440-specific purified subunit motor assays. The activity belongs to the assembled machinery; isolated FliF is not thereby asserted to transport protons or generate torque autonomously. Any restored comparative residue-number quotation must not silently map those residue numbers to KT2440.

This worker changes only FliF's reason. Root owns FliG, including any strengthening of its source-specific interface and switching support.

## Suggestion 7: distinguish the two location relationships

For PSEPK FlgK/FlgL, the extracellular location is biologically sound, while the junction term provides the anatomical assignment. Because GO:0009422 is not under GO:0005576, describe the MODIFY as a nonhierarchical anatomical replacement. No action or scientific location claim needs reversal.

The reviewer extends this criticism to flagellum → hook in FlgE, but that counterexample is incorrect: GO:0009424 does descend from GO:0009288. Similarly, the separate FlgK/FlgL flagellum → junction rows are genuine part_of refinements. Do not blanket-rewrite those as lateral corrections.

## Implementation boundary

Authorized review edits: SALTY/fliI, ECOLI/fliI, PSEPK/fliF, PSEPK/flgK, PSEPK/flgL, corresponding append-only notes, new helper histories and derived renders. No module, family, project, raw-source, provider or publication-cache changes. Exact payload/source checks and focused validation records are retained in `.cache/module-audit-logs/flagellar-20261106/round1/member-corrections/`.
