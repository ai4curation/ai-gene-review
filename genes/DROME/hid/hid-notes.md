# hid notes

## Manual review summary

`hid` encodes Head involution defective, a Drosophila RHG-family IAP antagonist. The
core reviewed activity is N-terminal IAP-binding/BIR-domain binding to DIAP1 and
DIAP2, relieving caspase inhibition and allowing Dronc/DrICE signaling. The
mitochondrial tail anchor is supported by Haining et al. and the 2026 Mtch paper's
supplemental Hid staining.

## Direct IAP antagonism

- PMID:10481910: HID blocks DIAP1's ability to inhibit caspase activity.
- PMID:10675328, PMID:12021771, and PMID:14517550: Hid binds DIAP1 through the
  RHG/BIR interface; generic `protein binding` rows should be narrowed to DIAP1
  E3/BIR binding.
- PMID:15107838: RHG motifs bind the same DIAP1 BIR1 groove used for DrICE
  regulation, supporting protein sequestering activity.
- PMID:18166655: Hid binds DIAP2 BIR2/BIR3 and competes with DrICE for free
  DIAP2.

## Broad process rows

Top-level `apoptotic process` and `programmed cell death` rows from mis-specified
embryonic cells, mechanosensory bristles, the Reaper/Hid multimer paper, the
foundational Grether paper, and the CNS midline paper were narrowed toward
`GO:0097190 apoptotic signaling pathway` because Hid is a caspase-upstream signal
rather than execution machinery.

## Peripheral developmental and stress rows

Larval Tr2 tracheal remodeling, head involution, RBF/DNA-damage apoptosis,
starvation-autophagy screening, macroautophagy, larval midgut death, antennal
arista patterning, and Ack/Hid eye assays were retained as non-core or accepted
context rows. Generic development, ecdysone, organ growth, and gamma-radiation
response rows were marked over-annotated where the assay tracks upstream induction
of `hid` or a downstream developmental output rather than the Hid protein acting in
that process.

## Rows left unresolved

Rows from PMID:12919673, PMID:14960620, PMID:16168982, PMID:16980964, and several
PMID:21035895/PMID:15150408 subcellular or autophagic rows were left `UNDECIDED`
because the cached abstracts did not expose the specific FlyBase full-text
evidence.
