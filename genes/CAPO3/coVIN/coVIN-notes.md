# coVIN (Capsaspora owczarzaki vinculin, CAOG_05123) - curation notes

Automated deep research was unavailable for this gene (no provider keys); these
notes are compiled manually from the UniProt record, InterPro, the cached
publications and the bioRxiv preprint of PMID:32857975 (read 2026-10-01).

## Identity

- UniProt A0A0D2WSN3 (ORF CAOG_005123; EMBL KJE94488.1; RefSeq XP_004346808.1),
  834 aa, unreviewed, submitted name "Vinculin"; "Belongs to the vinculin/alpha-catenin
  family" (ARBA). PANTHER PTHR46180 (VINCULIN).
- The paper's anti-vinculin antibody was raised against this protein: preprint methods
  [DOI:10.1101/2020.02.27.967653 "The vinculin-antigen is a polypeptide corresponding to
  the C-terminus region of one of the vinculin homologs (CAOG_05123, amino acid region
  335-834)"]. CAOG_05123 = CAOG_005123 = A0A0D2WSN3. The antigen ends at residue 834,
  the length of the UniProt model, so the gene model used matches.
- Second vinculin paralog in Capsaspora: A0A0D2UBD6 (CAOG_003344, 1038 aa, ProtNLM name
  "Vinculin", PTHR46180, two Pfam PF01044 hits). Checked via UniProt REST 2026-10-01.
  Only CAOG_05123 has been studied; nothing is known of CAOG_03344. Whether the
  antibody cross-reacts with it is not explicitly addressed in the text (the IP-MS
  supplement is described as showing "strong specificity").
- Not to be confused with the Capsaspora integrin beta 2 (CAOG_05058, A0A0D2WRB3),
  reviewed separately as coITGB2.

## Domain architecture (InterPro API, 2026-10-01)

- Pfam PF01044 Vinculin family 7-831; IPR017997 Vinculin 1-257 (N-terminal head);
  Gene3D alpha-catenin/vinculin-like bundles 1-131, 132-254, 497-618, 655-832;
  Gene3D "Vinculin, Vh2 four-helix bundle" 270-493; PRINTS PR00806 VINCULIN motifs
  691-780 (in the C-terminal bundle region).
- So: an N-terminal D1-like double bundle (talin-binding head in animal vinculins), a
  central bundle region, and a C-terminal five-helix-type bundle at the position of the
  vinculin tail (F-actin-binding in animals). At 834 aa it is shorter than vertebrate
  vinculin (1066 aa) and close in length to sponge vinculin (846 aa), which lacks domain
  D2 [PMID:29880641 "Op vinculin lacks domain 2, which typically distinguishes vinculin
  from α-catenin in other animals"]. Whether coVIN lacks D2 has not been established
  (no structural or careful alignment analysis done here).

## Experimental data (all from Parra-Acero et al. 2020; preprint full text, Curr Biol abstract only)

- Immunostaining of fixed adherent Capsaspora cells with the anti-CAOG_05123 antibody
  (rat polyclonal, Genecust) plus phalloidin:
  [DOI:10.1101/2020.02.27.967653 "Distinct patches of vinculin are observed in the
  filopodia."]; "both antibodies stain the cell body and multiple distinct patches along
  filopodia".
- Co-immunostaining with anti-integrin beta2 (β2E3): partial overlap
  ["Co-immunostaining showed a partial overlap, some patches contain both, whereas others
  have just one of the proteins"]. Authors' interpretation: "may represent anchorage
  sites of adhesion" (speculative; no further markers, no live imaging of vinculin).
- On fibronectin-coated versus BSA-coated coverslips, vinculin fluorescence intensity in
  filopodia increases (Fig. 3H) ["The overall fluorescence intensity of integrin β2 and
  vinculin staining within filopodia increased"], interpreted as recruitment.
- Antibody validation (Fig 3 supp 1): Western blots of the purified antigen and of
  soluble/insoluble Capsaspora extracts ("major bands at the predicted molecular
  weights"), IP + mass spectrometry versus IgG control ("strong specificity"), and
  no-primary-antibody controls for imaging. No knockout or pre-immune/antigen-competition
  control for vinculin.
- Life stage examined: adherent (filopodial) stage only, 2.5 h after seeding. Vinculin
  was not examined in cystic or aggregative stages.
- NO vinculin perturbation: the only functional perturbations are LatA/CK-666 (actin,
  Arp2/3) and the function-blocking anti-integrin β2 (β2GP1) antibody. No vinculin
  knockout, knockdown or binding assay. Vinculin talin-binding or F-actin binding was
  NOT tested for the Capsaspora protein.

## Context from other organisms (not transferred as experimental)

- Sponge (Oscarella pearsei) vinculin: talin-dependent F-actin binding
  [PMID:29880641 "In the presence of Op talin peptide, full-length Op vinculin bound to
  F-actin filaments"]; reviewed in genes/OSCPE/VIN1.
- Human VCL review (genes/human/VCL) cites the Capsaspora localisation as evidence that
  talin-activated actin coupling at cell-substrate contacts is ancestral; for Capsaspora
  itself only the localisation is shown.
- Origin of the adhesome [PMID:20479219 "all scaffolding proteins involved in the
  integrin adhesion apparatus (that is, α-actinin, vinculin, paxillin, and talin) are
  common among unikonts"]; the authors argued the scaffolds predate integrins and were
  co-opted ["an ancient scaffolding machinery was coopted to the integrin adhesion
  system"].

## Curation decisions (summary)

- actin binding / actin filament binding (IEA, InterPro2GO): ACCEPT as family/domain
  inference; not experimentally shown for coVIN.
- cytoplasm (IEA SubCell): ACCEPT; cell-body staining.
- cell adhesion (IEA InterPro2GO): ACCEPT at IEA level (vinculin-family proteins are
  structural linkers in adhesion complexes; vinculin is recruited to filopodia, the
  adhesive structures); but no vinculin-specific perturbation, so no experimental
  adhesion process term is added.
- NEW: filopodium (GO:0030175) IDA from the preprint immunostaining.
- Not added: focal adhesion / cell-substrate junction (patches are only suggested to be
  anchorage sites; no ultrastructure or other markers), talin binding, any
  adhesion-process term by IMP.

## Track C (propagation)

- No TreeGrafter (GO_REF:0000118), IBA or GO_REF:0000120 rows exist for this protein;
  all four rows are InterPro2GO or UniProt SubCell mappings. No animal tissue,
  junction or developmental term has reached coVIN.
