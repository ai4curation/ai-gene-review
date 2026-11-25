# SCARB2 / LIMP-2 (human, Q14108) curation notes

Deep research providers were unavailable in this environment; evidence from cached publications and
UniProt.

## Localization (benchmark-relevant)
- Principal location is the **lysosomal / late endosomal limiting membrane**, not the cell surface:
  UniProt `SUBCELLULAR LOCATION: Lysosome membrane ...; Multi-pass membrane protein`;
  [PMID:12356916 "LGP85 (LIMP II) is a type III transmembrane glycoprotein that is located
  primarily in the limiting membranes of lysosomes and late endosomes."]
- The large glycosylated domain faces the **lumen** (topologically equivalent to extracellular).
- A minor plasma-membrane pool exists and is the entry receptor for enterovirus 71 (UniProt,
  microbial infection FUNCTION), so the protein is partially surface-accessible; the many Reactome
  plasma-membrane rows were kept as non-core on that basis rather than accepted as the main site.
- Focal adhesion (single HDA hit) marked over-annotated; `lysosome` marked TOO_GENERAL beside
  lysosomal membrane; generic `membrane` modified to lysosomal + late endosome membrane.

## Function
- Cargo receptor for GBA1: [PMID:18022370 "the lysosomal integral membrane protein LIMP-2 is a
  specific binding partner of beta-glucocerebrosidase. This interaction involves a coiled-coil
  domain within the lumenal domain."] and "beta-glucocerebrosidase activity and protein levels were
  severely decreased in LIMP-2-deficient mouse tissues."
- Lipid binding/transport: [PMID:29199275 crystal structure of luminal-domain dimer with bound
  cholesterol and phosphatidylcholine; dimer prefers phosphatidylserine; "LIMP-2 facilitates
  transport of phospholipids into murine fibroblasts"]. Kept as non-core secondary activity.
- Organelle morphology: overexpression enlarges early and late endosomes/lysosomes [PMID:12356916].

## Review decisions
- `GO:0005044 scavenger receptor activity` (IBA/ISS/IEA/TAS) MODIFYed to `GO:0038024 cargo receptor
  activity`: the CD36/SR-BI family node is sound but SCARB2 has diverged to an intralumenal cargo
  receptor; a propagation_review records this against PANTHER:PTN000230217.
- `GO:0004888 transmembrane signaling receptor activity` likewise modified to cargo receptor
  activity.
- Nine generic `GO:0005515` rows removed per policy; enzyme binding (GBA1) accepted.
