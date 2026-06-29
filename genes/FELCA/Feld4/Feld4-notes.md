# Fel d 4 (cat lipocalin, UniProt Q5VFH6) — curation notes

Curated from the ALLERGENS backlog (worklist: `uv run ai-gene-review fetch-gene FELCA Q5VFH6 -u Q5VFH6`).
Dir/file alias `Feld4` (UniProt entry ALL4_FELCA has no gene symbol).

- Secreted **lipocalin** (calycin superfamily); minor cat allergen, binds IgE.
- Function: odorant/pheromone carrier; acts as a **kairomone** detected by the prey
  vomeronasal organ, inducing fear in mice
  [file:FELCA/Feld4/Feld4-uniprot.txt "May be a pheromone carrier. Acts as a kairomone, detected by"]
  (UniProt FUNCTION cites PMID:20478258).
- Curation: ACCEPT odorant binding (IBA/IEA) + extracellular region (IBA/IEA);
  MARK_AS_OVER_ANNOTATED generic small molecule binding (GO:0036094); add NEW
  pheromone binding (GO:0005550) as a specific refinement.
- Core function: pheromone/odorant binding (lipocalin carrier) in extracellular region.
- Contrast with Fel d 1: evolved function is **characterized** (lipocalin carrier),
  so low function-uncertainty despite allergenicity.
