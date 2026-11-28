# SCARB1 curation notes

Deep research was attempted with the same local command used for CD36, but no configured deep-research provider
other than `claude_code` was available to the `deep-research-client`. This review instead used the UniProt record,
GOA rows, PTHR11923 PAINT slice, Reactome records, and cached publication records cited by the GOA file.

## Functional outline

- SCARB1/SR-BI is the HDL receptor branch of the CD36/SR-B class B scavenger receptor family. It binds HDL and
  other lipoproteins at the plasma membrane, mediates selective uptake of HDL cholesteryl esters, and supports
  bidirectional exchange of unesterified cholesterol.
- The PTHR11923 SCARB1 node, PTN002629874, carries HDL/LDL-binding, cell-surface, caveola, cholesterol-efflux,
  cholesterol-import, plasma-lipoprotein-clearance, and apoptotic-cell-recognition IBD rows. Those assertions fit
  human SCARB1 better than the root scavenger-receptor row fits SCARB2.
- SCARB1 can bind LPS and phosphatidylserine and acts as a host entry factor for hepatitis C virus. Those are real
  secondary or infection-context activities rather than the central SR-BI cholesterol-transport role.
- Lysosomal and exosome HDA rows were treated cautiously. The close paralog SCARB2/LIMP-2 is the lysosomal cargo
  receptor, while SCARB1 is primarily a plasma-membrane/caveolar lipoprotein receptor.
