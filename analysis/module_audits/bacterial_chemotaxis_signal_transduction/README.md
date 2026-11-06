# Bacterial chemotaxis comparative audit

The module retains Bacteria as its taxonomic scope and describes a reusable
flagellar chemotaxis mechanism. It does not imply that every bacterium has the
mechanism, that every branch co-occurs, or that Wsp, Chp and other nonflagellar
systems can substitute for the motor-output pathway.

The 36 curated references include comparative treatments and primary experiments
for the individual activities and causal edges. Forty-six completed reviews cover
E. coli, P. putida, B. subtilis, H. pylori, S. meliloti, V. alginolyticus and
V. vulnificus. The linked gene notes distinguish reference accessions from assayed
strains, including the Sinorhizobium RU11/001 proteins, Helicobacter SS1/G27/PMSS1
experiments and the Vibrio functional and structural strains.

The topology separates transmembrane and cytoplasmic receptors, CheW and CheV
coupling, motor-output and phosphate-sink receivers, FliN- and FliY-containing
switches, and proton- and sodium-driven stators. Methylation feedback, CheC/CheD
binding feedback, CheV receiver adaptation and selected-receptor deamidation are
separate optional mechanisms. Accelerated reset can use coexisting CheZ, CheC,
FliY, CheX or CheA-mediated phosphate drainage, with ChePep, CheS and CheT supplying
distinct supported roles. Optionality is relative to basal machinery and does not
predict normal behavior after deleting a native component.

Run the reproducible checks from the repository root:

```sh
uv run python modules/bacterial_chemotaxis_signal_transduction-source-analysis/check_audit.py
```

The checker verifies all 431 machine-sourced annotation payloads and all 92 frozen
UniProt/GOA files. Of 455 historical rows, two authored proposals have explicit
archives: the PP_4332 broad signaling proposal was refined to receptor-complex
adaptor activity, and an uninformative FliY protein-binding proposal was retired.
Twenty-nine additional NEW rows give 483 current rows. Twenty-two inherited
provider artifacts remain byte-identical to the base; new Falcon attempts failed
with HTTP 403 and were replaced with honestly labeled literature-based notes.

The 65 capacity cases use the production module compiler with an explicit oracle.
Each ordinary selector requires both family/domain membership and reviewed
function. Descriptive families without established IDs require independently
reviewed role identity. Each complex requires every active unit and its supported
activity or contribution to the assembled complex. A contribution never counts as
an independently enabled activity. Negative controls reject incomplete stators,
CheC as canonical CheZ, FliN as catalytic FliY, and a generic receiver as a
motor-output CheY.

These checks establish curated-panel role capacity, not native expression,
stoichiometry, behavior or arbitrary taxonomic applicability. The KT2440 panel
supplies complete-root cases. Other taxa principally supply component and
subcircuit cases. The mixed-species FliY C-ring case is explicitly a synthetic
role-coverage case and does not establish cross-species assembly compatibility.

Focused gene, family, module and history checks pass. Four module advisories remain:
one unconfigured Pfam label namespace, and three family-function scope warnings.
The latter are retained because the existing family scope vocabulary cannot express
the CheA eukaryotic IRD exclusion or the mixed FliN/FliY catalytic architecture.
Those warnings do not negate the experimentally supported exemplar functions.
Full-corpus validation finished across 10,559 reviews. Schema, ontology, best-practices
and 54 pathway-reference checks pass. Its exit status is 1 because of 19 reference
errors in 17 unchanged yeast reviews; `preexisting-reference-failures.yaml` records
the exact errors and 23 unchanged input blobs. There are 27,993 best-practice
advisories. Module publication, remote review/CI and actual merge remain outstanding. See `audit-progress.yaml` for the recorded stage and the separate
preservation and capacity reports for reproducible results.
