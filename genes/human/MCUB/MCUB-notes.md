# MCUB review notes

## Summary

MCUB is an MCU paralog in the mitochondrial inner membrane, but it is not a
second pore-forming calcium uniporter. It associates with the human uniplex and
acts as a dominant-negative subunit: Lambert et al. showed that increased MCUB
displaces MCU from the functional mtCU complex, reduces MICU1/MICU2
association and lowers mitochondrial calcium uptake. The NOT ion-channel ISS
row transferred from mouse is therefore biologically coherent.

PTHR13462 is mostly coherent at the level of uniplex membership and
mitochondrial calcium homeostasis. MCUB is the main human exception for
positive calcium-import and pore-channel molecular functions. PAINT already
adds IRDs at `PTN002668518` for the ancestral `GO:0005262` and `GO:0015292`
rows and places `GO:0019855` calcium channel inhibitor activity on the same
MCUB branch. The ancestral `GO:0036444` calcium import into the mitochondrion
IBD still descends into MCUB and needs a matching IRD at `PTN002668518`.

The direct ComplexPortal `GO:0036444` NAS row is best read as a component-level
over-propagation from the uniplex complex to MCUB: the row sits in a
2025-10-15 ComplexPortal batch that also propagated mitochondrial calcium
homeostasis and uniplex component terms to MCU and MCUB. MCUB is structurally
part of the variant pore, but the Lambert et al. row supports the inhibitory
`GO:0110099` negative-regulation term rather than positive calcium import.

Bare `GO:0005515` protein-binding rows from proteome-scale interaction
screens do not specify a molecular function beyond untyped binding, so this
review removes that term and keeps the specific uniplex and inhibitory
activities instead.
