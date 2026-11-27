# ced-3 notes

## 2026-09-30 APOPTOSIS manual review

CED-3 is the core C. elegans executioner caspase. The local UniProt record
summarizes the main substrate biology: CED-4 activates the CED-3 zymogen;
CED-3 cleaves DCR-1, CED-8, DRP-1, CNT-1, and FEM-1 in apoptotic execution;
and the same catalytic activity is reused outside whole-cell apoptosis for
GSNL-1 cleavage during synapse pruning and for LIN-14/LIN-28/DISL-2 cleavage in
the miRNA/heterochronic timing pathway.

- Canonical activity and activation: CED-3 is an Asp-directed cysteine
  endopeptidase that undergoes proteolytic activation
  [PMID:8654923, "the full-length CED-3 protein undergoes proteolytic
  activation"]. CED-4 is the upstream apoptosome adaptor, with the CED-4
  octamer binding the CED-3 zymogen to facilitate autocatalytic maturation
  [PMID:24065769, "CED-4 forms an octameric apoptosome, which binds the CED-3
  zymogen"].
- Apoptotic execution: CED-3 cleaves DCR-1 to create a DNase fragment that
  promotes chromosome breaks [PMID:20223951, "DCR-1 was cleaved by the CED-3
  caspase"], cleaves CED-8 to drive phosphatidylserine exposure
  [PMID:24225442, "CED-8 ... is a substrate of the CED-3 caspase"], and cleaves
  CNT-1 so that truncated CNT-1 suppresses AKT survival signaling
  [PMID:25383666, "whose cleavage by CED-3 activates an N-terminal cleavage
  product"].
- Local, non-apoptotic synapse pruning: the GSNL-1 paper directly supports
  CED-3 cleavage of a gelsolin-family substrate during RME-neuron presynaptic
  material elimination, so synapse/pruning rows are kept as non-core and rows
  claiming CED-3 itself depolymerizes actin were narrowed to synapse pruning
  [PMID:26074078, "caspase CED-3 cleaves GSNL-1 at a conserved C-terminal
  region"].
- Non-apoptotic heterochronic development: the miRNA enhancer paper supports a
  real CED-3 cleavage branch for LIN-14, LIN-28, and DISL-2, but the cached
  abstract does not verify every exact organismal endpoint, so heterochronic
  rows are non-core while locomotion, vulval, and embryo-development endpoints
  are left undecided [PMID:25432023, "regulates multiple developmental events
  through proteolytic inactivation"].
- Restraint and localization: CSP-2, CSP-3, and NPP-14 are CED-3 zymogen
  inhibitors, so their interaction evidence should not annotate CED-3 to
  cysteine-type endopeptidase activator activity or to negative regulation of
  execution [PMID:19575016, "CSP-2 associates with the CED-3 zymogen and
  inhibits its autoactivation"; PMID:18776901, "CSP-3 associates with the large
  subunit of the CED-3 zymogen"; PMID:27723735, "NPP-14 interacts with the
  CED-3 zymogen prodomain"].
- Over-annotation calls: the Salmonella row is a host/pathogen survival output
  of germline apoptosis, not bacterium-specific molecular work by CED-3
  [PMID:11226309, "ced-3 and ced-4 mutants are hypersensitive to
  S. typhimurium-mediated killing"]. The PAR-4/STRD-1/MOP-25/PIG-1 cell
  extrusion paper is specifically about caspase-independent shedding of cells
  that would otherwise survive in ced-3 mutants, so its cell-adhesion and
  developmental-apoptosis rows are endpoint over-annotations
  [PMID:22801495, "PIG-1 promotes shed-cell detachment"].
