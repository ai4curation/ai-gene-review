# Fel d 2 / Serum albumin (cat ALB, UniProt P49064) — curation notes

Curated from the ALLERGENS backlog (`fetch-gene FELCA ALB -u P49064`).

- **Serum albumin** (ALB/AFP/VDB family); the abundant plasma multi-ligand carrier.
  Minor, cross-reactive allergen (Fel d 2; mammalian-albumin cross-reactivity,
  pork-cat syndrome).
- Function (largely ISS from human/bovine albumin): binds fatty acids, metal ions
  (Zn/Ca/Mg/Na/K), hormones, bilirubin, drugs; main role = regulation of colloidal
  osmotic pressure of blood; major plasma zinc transporter; binds enterobactin to
  limit bacterial iron uptake
  [file:FELCA/ALB/ALB-uniprot.txt "Binds water, Ca(2+), Na(+), K(+), fatty acids, hormones,"]
  [file:FELCA/ALB/ALB-uniprot.txt "enterobactin and inhibits enterobactin-mediated iron uptake of E.coli"].
- Curation: ACCEPT fatty acid binding, enterobactin binding (IBA/IEA/ISS),
  extracellular region; MARK_AS_OVER_ANNOTATED DNA binding (GO:0003677 — not a bona
  fide function; promiscuous/ISS artifact), generic small molecule binding and
  protein-containing complex; KEEP_AS_NON_CORE the many secondary ligand-binding and
  response terms (oxygen, PLP, toxic substance, cytoplasm, blood microparticle, etc.).
- Core functions: (1) fatty-acid/small-molecule plasma carrier (osmotic regulation);
  (2) enterobactin sequestration (nutritional immunity).
- Contrast with Fel d 1: evolved function **thoroughly characterized**.
