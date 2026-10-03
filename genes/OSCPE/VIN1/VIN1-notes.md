# VIN1 (vinculin, Oscarella pearsei, UniProt A0A3B6UES5) -- review notes

Automated deep research was unavailable for this gene (no deep-research provider
keys in this environment). These notes were written manually from the cached full
text of the single primary paper (PMID:29880641, Miller et al. 2018 J Biol Chem)
and the UniProt Swiss-Prot entry (VINC_OSCPE). No other literature on this protein
is known to exist.

## Identity and structure

- 846 aa member of the vinculin/alpha-catenin (VIN) family; groups with animal
  vinculins in phylogeny, but lacks domain D2 that is typical of vinculins
  [PMID:29880641 "However, Op vinculin lacks domain 2, which typically distinguishes vinculin from α-catenin in other animals"].
- O. pearsei has three VIN-family proteins: vinculin, alpha-catenin and an
  "uncharacterized" clade member
  [PMID:29880641 "The O. pearsei genome encodes three VIN-family proteins: vinculin, α-catenin, and a member of the uncharacterized animal VIN-family clade"].
- Crystal structure 2.3 A (PDB 6BFI); overall more vinculin-like than
  alpha-catenin-like; monomer by SEC-MALS
  [PMID:29880641 "indicating that it is a monomer in solution, a property of mammalian vinculin but not αE-catenin"].

## Biochemistry (recombinant protein, in vitro)

- ITC: full-length VIN1 and its D1 domain (1-257) bind a synthetic Op talin
  vinculin-binding-site peptide (TLN residues 598-621), but not an Op beta-catenin
  peptide [PMID:29880641 "Full-length Op vinculin and Op vinculin D1 bound Op talin peptide"];
  [PMID:29880641 "Moreover, Op vinculin bound talin but not β-catenin"].
  D1 binds with Kd ~82 nM, full length ~1.1 uM, i.e. partial autoinhibition.
- F-actin co-sedimentation: VIN1 alone does not bind F-actin, but does so in the
  presence of talin peptide
  [PMID:29880641 "Like vertebrate vinculins, Op vinculin did not bind F-actin significantly above background at concentrations up to 15"];
  [PMID:29880641 "In the presence of Op talin peptide, full-length Op vinculin bound to F-actin filaments"].
  Note: rabbit skeletal muscle actin was used.
- Beta-catenin was the only alpha-catenin-type partner tested; it did not bind.
  Alpha-catenin, cadherin and integrin binding were not tested.

## Localization (endogenous protein in sponge tissue -- NOT heterologous expression)

- Affinity-purified antibody against Op vinculin, validated by Western blot,
  antigen competition and IP; immunostaining of fixed O. pearsei tissue
  (pinacoderm, choanoderm), co-stained with phalloidin.
- Four patterns: belt-like zone at cell-cell contacts in pinacoderm;
  filopodial/lamellipodial extensions of motile mesohyl cells; base of the
  microvillar collar of choanocytes plus belt at cell-cell contacts in choanoderm;
  cytoplasmic signal in pinacoderm
  [PMID:29880641 "a belt-like zone at points of cell–cell contact in the pinacoderm"];
  [PMID:29880641 "in filopodial/lamellopodial extensions of motile cells within the mesohyl"];
  [PMID:29880641 "at the base of the microvillar collar of choanocytes within the choanoderm"].
- Co-localizes with F-actin in every context
  [PMID:29880641 "In each cellular context, Op vinculin appeared to co-localize with actin filaments, indicating an evolutionarily conserved interaction with the actin cytoskeleton."].
- Junctions are not ultrastructurally defined
  [PMID:29880641 "The localization of Op vinculin to cell–cell contacts in the pinacoderm and choanoderm is consistent with a possible AJ in these tissues, despite the lack of ultrastructural evidence"].
- The "cell-ECM contact" interpretation is inferred from filopodial localization in
  migratory cells; no integrin/talin co-staining was done.

## Curation decisions (summary)

- protein binding IPI (with TLN) -> MODIFY to talin binding GO:1990147.
- actin filament binding IDA -> ACCEPT (talin-dependent, autoinhibited alone).
- filopodium / cortical cytoskeleton IDA -> ACCEPT (endogenous sponge tissue).
- NEW cell-cell junction (GO:0005911) IDA from the belt-like cell-cell contact
  staining; caveat that the junction type is not defined ultrastructurally.
- No NEW process terms: function in cell adhesion is proposed, not tested
  (no genetic perturbation in sponges).
