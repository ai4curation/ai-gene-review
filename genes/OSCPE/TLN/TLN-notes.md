# TLN (talin, Oscarella pearsei, UniProt A0A3G2LGI8) -- review notes

Automated deep research was unavailable for this gene (no deep-research provider
keys in this environment). These notes were written manually from the cached full
text of the only paper on this protein (PMID:29880641, Miller et al. 2018 J Biol
Chem), which is primarily about the sponge vinculin VIN1, and from the UniProt
Swiss-Prot entry (TLN_OSCPE).

## Identity and domains

- 2531 aa talin; conserved talin architecture: FERM head, talin rod with
  vinculin-binding sites, C-terminal I/LWEQ actin-binding domain
  [PMID:29880641 "As in their mammalian counterparts, Op talin has an N-terminal FERM domain followed by a talin middle domain, vinculin-binding sites, and an I/WLEQ domain."].
- Has an extra predicted PTB domain after the FERM domain
  [PMID:29880641 "Just C-terminal to the FERM domain, Op talin also has a predicted phosphotyrosine-binding domain that is not present in mouse talin."].
- InterPro: Talin_cent, VBS, I/LWEQ, FERM, Talin1/2 VBS2, IBS2B; PANTHER PTHR19981.

## Experimental data

- The ONLY experiment on TLN: a synthetic peptide corresponding to TLN residues
  598-621 (homologous to the mouse talin vinculin-binding site 605-628) was made
  and used in ITC and actin co-sedimentation with recombinant VIN1
  [PMID:29880641 "In a MUSCLE alignment Mm talin 605–628 correspond to residues 598–621 in Op talin"].
- The peptide binds VIN1 (full-length and D1) and activates VIN1 F-actin binding
  [PMID:29880641 "Full-length Op vinculin and Op vinculin D1 bound Op talin peptide"];
  [PMID:29880641 "In the presence of Op talin peptide, full-length Op vinculin bound to F-actin filaments"].
- Full-length TLN protein was never expressed; TLN localization, integrin binding,
  actin binding and membrane binding were NOT examined in sponge.

## Family background (as stated in PMID:29880641)

- [PMID:29880641 "integrins anchor to the actin cytoskeleton through interactions with a large number of cytoplasmic proteins including talin, vinculin, and paxillin"]
- [PMID:29880641 "The N-terminal domain D1 of vinculin binds talin, and the C-terminal domain binds F-actin"]

## Curation decisions (summary)

- protein binding IPI (with VIN1) -> MODIFY to vinculin binding GO:0017166
  (peptide-level evidence).
- IEA localization/MF rows accepted on family-conservation grounds, except:
  ruffle and structural constituent of cytoskeleton (MARK_AS_OVER_ANNOTATED),
  cell-cell adhesion (MODIFY to cell-matrix adhesion, the integrin-linked context).
- No NEW annotations: no sponge-specific experimental evidence beyond the VBS peptide.
