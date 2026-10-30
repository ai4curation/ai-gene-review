# PP4_45660 (A0ABN5URH5), P. putida NBRC 14164: notes

Dashboard source: https://gene-annotate-dashboard.kbase.us/review/NZ_KZ987399.1_4576
(tier A, Dark-Function stratum, aux genome).

## Mapping
- The exact-sequence UniProt entries are deleted. The review is filed on the type-strain
  reference-proteome entry A0ABN5URH5 (PP4_45660). It is 93.1% identical over 405/405 aa
  (BERIL run `20261030T210853Z-final-putida-mapping`; the row is frozen in
  `PP4_45660-dashboard-prediction-evidence/uniprot_mapping_row.tsv`).
- The gene is not in KT2440. phmmer found no hit in UP000000556, and a UniProt query for
  PF11902 in that proteome returns nothing. KT2440 therefore has no Fitness Browser data
  for it.

## Conclusion
- The protein is a DUF3422 (PF11902)/COG4949 family protein of unknown molecular function.
- **Topology.** It has two alpha-helical TM segments at the C-terminus: DeepTMHMM puts them
  at 345-365 and 380-397, and Phobius at 348-368 and 380-399. There is no signal peptide.
  The ~345-residue N-terminal domain is predicted to be cytoplasmic. Read together, this is
  an inner-membrane-anchored protein with a large cytoplasmic domain.
- **Literature.** No paper describes any DUF3422 protein. PubMed has no hits for
  DUF3422, COG4949 or PF11902, and no family member is in Swiss-Prot.
- **Distant homologs (30-35% identity).** These have strong carbon-source fitness defects:
  *Phaeobacter* on L-proline, L-citrulline and L-ornithine, and *Caulobacter* on D-xylose.
  The substrates are unrelated, so no shared activity can be read from them.
- **Neighbourhoods are not conserved.**
  - *P. fluorescens* N2E2 and N2C3 share a dienoyl-CoA reductase / ACC deaminase /
    cytochrome b561 block.
  - N1B4 has an aspartate aminotransferase next to it instead.
  - In NBRC 14164 the neighbours are an NCS1 transporter, an aldehyde dehydrogenase and MscK.

## Names in UniProt
- "Membrane-anchored protein" is a ProtNLM machine name. It matches COG4949 and the
  topology, but it describes the protein rather than giving it a function.
- "Lysin" and "Egg lysin" are submitter names on many family members (46 in a 500-entry UniProt sample of
  2026-10-30). They have no supporting evidence. Egg lysin is a mollusc sperm protein, so
  these names are almost certainly propagated name-transfer artifacts. Neither name gives
  a function.

## Dashboard verdict
- **Recommended verdict: supported.** The call is correctly hedged.
- Corrected annotation (only a sharpening): "DUF3422/COG4949 family protein of unknown
  function, anchored in the inner membrane by two C-terminal TM helices".
- GO:0005886 plasma membrane: **COR**. It is novel, since GOA is empty, but it rests on
  prediction only.
- **Caveat on tier A.** The tier-A criterion comes from the fitness phenotypes of distant
  (about 35%) homologs, which the call itself admits do not resolve function.
- **Gap in the evidence.** The pipeline found three close *P. fluorescens* FW300 orthologs
  that are Fitness Browser organisms. Their fitness data was not shown in the evidence and
  was never checked:
  - Pf6N2E2_2210 (76.6%)
  - AO356_01705 (76.3%)
  - Pf1N1B4_5071 (72.2%)

  Source: run `20261030T211241Z-pp4-45660-fb-orthologs`, `fb_orthologs.json`.

## Tooling
- `just fetch-gene PSEPU PP4_45660 --uniprot-id A0ABN5URH5` worked for NCBITaxon:1211579
  with no workaround.
- `just fetch-gene-pmids` found no PMIDs.
- `just fetch-fitness` failed. PSEPU has no FEBA mapping, and fit.genomics.lbl.gov returns
  HTTP 403. The FW300 ortholog fitness therefore remains unchecked; it is the obvious next
  step, via BERDL `kescience.fitnessbrowser` or the browser.
- `core_functions` is left empty on purpose because the molecular function is unknown. This
  gives the expected validator warning.
