# imuB curation notes

- ImuB lacks the conserved active-site residues required for Y-family polymerase activity. [PMID:20615954, "lack conserved active-site amino acids required for polymerase activity."]
- Ortholog experiments show that ImuB binds ImuA, DnaE2, and the beta clamp, supporting protein-macromolecule adaptor activity. [PMID:20615954, "DnaE2, as well as with the beta-clamp."]
- In P. putida, ImuB promotes stationary-phase mutant accumulation. [PMID:17331811, "accumulation of stationary-phase mutants up to two-fold."]

## Completion pass (ImuABC module curation)

- Status set to COMPLETE; the GO:0006281 MODIFY row now carries quotes and names its actual
  route: UniProt combined pipeline over UmuC domain IPR001126 plus TreeGrafter node
  PANTHER:PTN002440639 (not a PAINT IBA).
- KT2440 keeps GO:0019985 rather than GO:0042276: ImuB promotes mutation accumulation here
  but DnaE2 suppresses base substitutions, so the cassette's output in this organism is
  antagonistic rather than uniformly error-prone. [PMID:17331811]


## 2026-11-07 — comparative ImuABC annotation audit

Native PaW85 deletion and complementation in the AlkA-deficient background resolve the previous missing-genetics premise. The noncatalytic adaptor mechanism is still inferred from specific architecture and mycobacterial interaction studies; it is not a purified PSEPK binding experiment. Both historical NEW rows remain unchanged. Generic DNA repair is replaced laterally by TLS, not described as a GO descendant refinement.

The genuine existing provider research was read and preserved unchanged; primary sources control conclusions where reports are stale. PAINT-loss checking completed sequentially, but the target is not a leaf in the available cached family tree: loss status is unavailable, not demonstrated absent. Original ordered annotation payloads and historical NEW actions are preserved; no new row is added. Existing notes above are historical and superseded only where this dated audit explains a correction. All original raw, provider and publication bytes remain unchanged.
