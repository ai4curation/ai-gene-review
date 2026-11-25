# Comparative acetoin-system checks

The module separates four native implementations: Pseudomonas putida KT2440,
Cupriavidus necator H16, historical Pelobacter carbinolicus (currently
Syntrophotalea carbinolica), and Bacillus subtilis 168. PpG2 Adh/AcoC are
comparative exemplars. PP0556/AcoX is reviewed as an unresolved accessory rather
than assigned a catalytic step.

Run from the repository root:

```sh
uv run python modules/bacterial_2_3_butanediol_acetoin_catabolism-source-analysis/check_families.py
uv run python modules/bacterial_2_3_butanediol_acetoin_catabolism-source-analysis/check_routes.py
```

The family check uses the normal live UniProt lookup and official PANTHER labels.
It checks each declared family/subfamily against its exact representatives.
The ignored member index is a validation cache, never cited as evidence. An
existing cache retains its original rows, alternate placements and gap markers;
only missing observed members are appended. The Pseudomonas AcoC descriptor has
no single PANTHER ID because its close exemplars occupy different current
families. Their shared lipoyl/alpha-beta-hydrolase architecture is recorded
without asserting the canonical E2 fold found in Pelobacter and Bacillus.

The route check evaluates 27 cases. Whole-system cases require both native E1
subunits, native E2 and the assigned native E3. Foreign subunits do not complete
a native assembly. KT2440 and H16 remain unresolved at E3 even if a foreign AcoL
is supplied. Optional butanediol entry can be bypassed when acetoin is available.
Seven structural routes represent the four native cores plus three alternative
KT2440 entry choices; they do not demonstrate physiological flux.

Nine additional entry-only cases use an explicit local condition predicate.
NAD-BDH accepts R,R/meso substrate with NAD; PedE requires calcium/PQQ and PedH a
usable lanthanide/PQQ. Expression and electron-transfer competence must also be
supplied for PQQ entry. These are transparent assay/physiology assumptions: the
general module compiler does not evaluate free-text chemical or metal contexts.
An identified native cytochrome partner or acetoin transporter is not invented.

## Evidence distinctions

- PMID:1898934 reports purified Pelobacter E1/E2/E3 reconstitution; PMID:8110297
  maps the purified components to genes. These accessible abstracts explicitly
  support the claims used, even though full-text retrieval did not succeed.
- PMID:2061286 supports native H16 E1 and fast-migrating AcoC identification;
  its E2 chemistry is an inference. PMID:10368162 supplies native Bacillus
  pathway genetics and component motifs, with a clone/reference AcoC difference.
- PMID:34513815 establishes KT2440 PP0552 NAD specificity and three stereoisomer
  entry routes. One sentence reverses the lanthanide regulatory direction; the
  measured growth results and original PMID:28655819 experiments determine the
  interpretation. The discrepancy is assessed in the module reference entry.
- PMID:20508247 supplies cross-species mechanism and explicitly calls shared E3
  recruitment presumptive. PMID:17558661 is an abstract-only historical review;
  PMID:37644496 supplies stereochemical context, rather than native pathway proof.
- GO:0019152 is acetoin/diacetyl redox chemistry, not acetoin cleavage.
  GO:0052934 defines primary alcohol oxidation, not secondary butanediol oxidation.
  The module uses GO:0016624 for assembled E1 and GO:0016614 for the secondary
  PQQ-entry reaction, with explicit substrate and product descriptors.

Gene-specific sequence and preservation analyses are kept with their reviewed
members. No GOA file is used as functional evidence and no ancestral PAINT node
is inferred for the module without node-specific evidence.
