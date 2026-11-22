# ULK2 curation notes

## Manual annotation review

This review used the seeded `ULK2-ai-review.yaml`, `ULK2-goa.tsv`, the UniProt Q8IYT8 flat
file, cached PMID:18936157 and PMID:28389568, full cached PMID:17389358 for the mouse neuronal
evidence behind the axon PAINT nodes, the existing human ULK1 review, and
`interpro/panther/PTHR24348/PTHR24348-paint.tsv`.

`just paint-losses human ULK2` reported no IRD or IKR loss on the Q8IYT8 lineage. The IBA
review therefore judged each positive IBD node directly:

- PTN002805221 supports cytoplasm and protein serine/threonine kinase activity within the
  Atg1/ULK branch.
- PTN000681272 supports phagophore assembly site, cytosol, autophagosome, autophagosome
  assembly and regulation of autophagy.
- PTN000681273 supports the obsolete PAS-membrane row, mitophagy, starvation response,
  reticulophagy and piecemeal microautophagy of the nucleus.
- PTN000681276 and PTN008401638 support axon extension and negative regulation of collateral
  sprouting from mouse Ulk1/Ulk2 sensory-neuron evidence.

PMID:18936157 is abstract-only locally but explicitly names ULK1 and ULK2 as mammalian Atg1
homologs in autophagy activation, and states that ULK1/2 function is controlled by
autophosphorylation and the CTD. It also maps CTD regions that direct membrane association and
ATG13 binding. That supports the broad ULK2 autophagy, kinase, autophosphorylation and
early-autophagic-membrane rows without needing to add unsupported new substrate terms.

The three `GO:0034045 obsolete phagophore assembly site membrane` rows were `MODIFY`ed to
`GO:7770114 phagophore membrane`. Local SL/GO:0034045 project notes record live QuickGO's
obsoletion and replacement, and the underlying ULK2 membrane association is experimentally
supported rather than spurious.

Generic `GO:0005515 protein binding` was removed under the project protein-binding policy. The
reported ATG13 interaction is kept as evidence for CTD-mediated autophagy function, but the
generic term does not identify a molecular function.

The axon-extension and negative-collateral-sprouting IBAs were kept as non-core. The PAINT nodes
are specific to the ULK1/2 clade and full PMID:17389358 directly tested mouse Ulk1/2 knockdown
in NGF-treated sensory neurons, reporting impaired NGF endocytosis, excess arborization and
stunted axon elongation.

Reticulophagy and mitophagy were kept as conditional non-core selective-autophagy contexts. The
ULK2 product can provide conserved initiation machinery when selective ER or mitochondrial
turnover recruits that machinery, without being the cargo receptor or making these the main
function. In contrast, `GO:0034727 piecemeal microautophagy of the nucleus` was left
`UNDECIDED`: the PAINT row is genuine and seeded by yeast ATG1, but the specific
microautophagic topology has not been separated for human ULK2 from generic nucleophagy or
other macroautophagy routes.

PMID:28389568 is also abstract-only locally and foregrounds IRGM-mediated ULK1 phosphorylation
during HCV-triggered autophagy. The ULK2 IGI row is biologically coherent with the redundant
ULK1/2 autophagy branch and with PMID:18936157, but the full-text genetic details were not
re-read here.
