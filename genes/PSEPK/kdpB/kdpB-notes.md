# kdpB curation notes

## Evidence assessment

PSEPK A0A140FWL1 is the P-type ATPase subunit of KdpFABC. Structural work on the
E. coli ortholog establishes the division of labor in which KdpA handles the
potassium pathway and ATP energy is harnessed by KdpB [PMID:28636601, "the
energy of ATP is harnessed by KdpB"]. UniProt independently identifies the
P-type ATPase family, ATP-binding region, and catalytic phosphorylation cycle
[file:PSEPK/kdpB/kdpB-uniprot.txt].

## Curation decision

ATP hydrolysis activity (GO:0016887) is KdpB's direct catalytic molecular
function. P-type potassium transmembrane transporter activity (GO:0008556) is a
property of the assembled pump, so KdpB contributes to it but does not provide
the complete activity independently.

## 2026-11-01 re-review pass

- Provider deep research was not run in this pass; the upgrade relies on the UniProt record
  (HAMAP/InterPro/NCBIfam family evidence) and cached E. coli ortholog publications, cited as
  orthology-based support.
- Every row now has a reason and verbatim support; correct-but-general terms changed to MODIFY
  with the specific term the gene already carries; a NEW part_of GO:0031004 (ISO from the E. coli
  ortholog) row added so the complex used in core_functions is reflected in annotations.


## Scoped Kdp module consultation — 2026-11-07

The target sequence confirms DKTGT beginning atAsp311. KdpB uses Mg-ATP and contributes both energy coupling and cytoplasmic ion release, rather than merely powering a separate KdpA channel. Magnesium binding is ACCEPT as an integral catalytic cofactor role; core prose explicitly records it. Older KdpC-contact work remains a historical reference but is no longer necessary support for ATP binding. E. coli Asp307 and KT2440 Asp311 numbering remain distinct.

Every original annotation row and its source payload/order was reviewed and preserved. No additional annotation rows were proposed. Full provenance and assay boundaries: `analysis/module_audits/bacterial_kdp_potassium_homeostasis/psepk-consultation/primary-scope.md`; sequence checks are adjacent. No IBA rows occur in these six reviews, so no IBA loss judgment is being made. Family membership and original historical ISO donors are retained independently of donor counts.

A genuine `just deep-research PSEPK kdpB --provider falcon` request failed HTTP403 authentication. Logs remain in `.cache/module-audit-logs/kdp-20261107/psepk-consultation/`; no provider report was manufactured.

Native KT2440 context is supplied by PMID38927284 full text: salt stress increases kdpA/B/D transcripts, but individual overexpression does not improve growth in the tested high-salt medium. This is not a purified activity assay or proof that the complete pump is unimportant. PMID26913973 publisher text corrects the historical kdpB pseudogene annotation; its local abstract cache remains unchanged. No salt-tolerance process assertion is added.
