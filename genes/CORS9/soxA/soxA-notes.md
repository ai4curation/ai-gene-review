# soxA (Corynebacterium sp. U-96) review notes

## 2026-11-04 — initial review (Claude, AI-assisted)

- Reviewed from scratch from the INITIALIZED stub. No provider deep-research
  file was generated in this session (no API keys); sources were the cached
  abstracts (PMID:7240129, 17395614, 20675294, 15946648, 15914915, 11902668,
  9185627; for soxB also 1939012, 15240125, 3202887, 6158947) and the UniProt
  record. PMID:7240129 and PMID:6158947 have no cached abstract; their content
  was taken from UniProt comments that cite them with ECO:0000269.
- PMID:7887617 and PMID:11035956 concern the monomeric Arthrobacter sarcosine
  oxidase, not this heterotetramer; not cited.
- GO:0008115 is defined by the folate-free reaction (H2O + O2 + sarcosine =
  formaldehyde + glycine + H2O2; RHEA:13313). The heterotetramer's
  physiological reaction with tetrahydrofolate (EC 1.5.3.24, RHEA:70455) gives
  5,10-methylenetetrahydrofolate and suppresses formaldehyde release
  [PMID:9185627 "only the heterotetrameric sarcosine oxidases can use
  tetrahydrofolates as substrates"]. All GO:0008115 rows (EXP and IEA) are
  therefore KEEP_AS_NON_CORE in all four subunit reviews, and the core function
  uses proposed_molecular_function "sarcosine oxidase
  (5,10-methylenetetrahydrofolate-forming) activity" (same proposed_name as the
  PSEPK reviews and the module).
- Qualifier: SoxB carries the FAD substrate site and the covalent FMN, so
  enables is kept for SoxB. SoxA, SoxD and SoxG GO:0008115 rows carry
  WRONG_QUALIFIER source_defects (enables -> contributes_to).
- Structure ligand inventory (genes/CORS9/soxA/soxA-bioinformatics/): NAD in
  chain A, FAD+FMN in chain B, Zn in chain D, nothing in chain C; no Fe-S in any
  of six PDB entries. SoxA GO:0051536 iron-sulfur cluster binding (InterPro2GO
  from IPR001041) was REMOVEd on this basis.
- NEW rows: part_of GO:0032921 for all four; NAD+ binding (SoxA); FAD and FMN
  binding (SoxB); zinc ion binding (SoxD).


## 2026-11-06 comparative module audit

Persistent marker DMG-CORS9-soxA-20261106. Reviewed every original row, inherited proposal, core and cited source. Default Falcon was attempted normally because no provider artifact existed; HTTP403 authentication/access failure is logged. These are manual notes, not a fabricated provider report.

- Retained all original actions and inherited NEW rows, including SoxA Fe-S rejection.
- Moved the full-complex proposed THF reaction out of autonomous subunit core MF; retained its top-level term proposal and represented conserved oxidative contribution with GO0016647.
- Confirmed PDB chain/accession/construct boundaries independently via PDBe/SIFTS.

Original machine payloads, inherited NEW rows and raw files are protected by original-members-baseline.json. Source limitations are explicit: many original primary citations remain abstract-only, with curated UniProt evidence and direct deposited structure mappings used for corroboration. No inaccessible experimental annotation was rejected merely for missing full text.

Full PMID15914915 was subsequently acquired by the PSEPK reviewer from the official J-STAGE publisher PDF. Its scoped assembly-evidence.md excerpt documents flavin-free, unstable isolated beta/beta-delta constructs. This supports complex-level contributions without proving all possible isolated-beta preparations inactive.
