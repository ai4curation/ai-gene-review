# wetA (Aspergillus nidulans) — curation notes

UniProt: P22022 (WETA_EMENI). Late regulator of the brlA -> abaA -> wetA
conidiation cascade. Member of the `conidiation_regulatory_cascade` module.

## Core biology (with provenance)

- **Required for conidial wall maturation / impermeability.** wetA is needed for
  synthesis of the cell-wall layers that make conidia impermeable; wetA mutants
  ("wet-white") take up water and autolyse instead of maturing.
  [PMID:1986246 "The Aspergillus nidulans wetA gene is required for synthesis of cell wall layers that make asexual spores (conidia) impermeable"].
- **Late tier, activated by brlA and abaA.**
  [PMID:1986246 "wetA is activated during conidiogenesis by sequential expression of the brlA and abaA regulatory genes"].
- **Activates spore-specific gene expression.** Forced wetA expression in hyphae
  drives accumulation of spore-specific transcripts (but not brlA/abaA).
  [PMID:1986246 "Aspergillus nidulans wetA activates spore-specific gene expression"].
- **Maturation defect is Stage II/III.** wetA6 conidia form normally but fail to
  mature (inner wall layer fails to condense).
  [PMID:2180753 "Conidia of the wetA6 mutant strain formed normally but failed to mature during Stages II and III"].

## Curation judgments

- Core roles (ACCEPT): conidium formation/maturation (GO:0048315), asexual spore
  wall assembly (GO:0042243), positive regulation of transcription of
  spore-specific genes (GO:0045944, GO:0006357), positive regulation of conidium
  formation (GO:0075307).
- Non-core (KEEP_AS_NON_CORE): pigment biosynthetic process (GO:0046148) — an
  indirect downstream consequence of WetA activating spore-wall/pigment genes,
  not a core enzymatic role.
- **MF not asserted.** WetA acts as a developmental regulator of gene expression,
  but a specific sequence-specific DNA-binding activity is not firmly established
  (GOA assigns wetA no molecular-function term). The module annoton and
  core_functions therefore assert no molecular_function for WetA.
