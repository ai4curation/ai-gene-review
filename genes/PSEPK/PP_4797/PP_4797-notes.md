# PP_4797 curation notes

## Identity check

PP_4797/Q88DM8 is a 54-amino-acid protein. The current UniProt protein name,
"Lipoyl synthase", is a Google ProtNLM prediction, but the sequence record has
no radical-SAM or LipA domain. Instead, both InterPro and Pfam identify the
protein as alternative ribosome-rescue factor A (ArfA)
[file:PSEPK/PP_4797/PP_4797-uniprot.txt, "DR   InterPro; IPR005589; ArfA."]
[file:PSEPK/PP_4797/PP_4797-uniprot.txt, "DR   Pfam; PF03889; ArfA; 1."].

The sole GOA annotation, rescue of stalled cytosolic ribosome, is transferred
from that ArfA domain [file:PSEPK/PP_4797/PP_4797-goa.tsv,
"GO:0072344\trescue of stalled cytosolic ribosome"]. PP_4797 should therefore
be treated as an ArfA-like ribosome-rescue protein and excluded from the
protein-lipoylation module. Its misleading name and proximity to lipA/lipB make
it a useful diagnostic member of the ppu00785 batch.

## Initial annotation decision

The sole `rescue of stalled cytosolic ribosome` annotation is accepted because
it agrees with both the InterPro and Pfam ArfA assignments. No lipoate-related
annotation is proposed. The discrepancy is in the automated protein name, not
in the current GOA row.

## OpenScientist assessment

The completed OpenScientist report independently converges on ArfA identity
and summarizes the established ArfA-RF2 mechanism from proteobacterial
literature
[`file:PSEPK/PP_4797/PP_4797-deep-research-openscientist.md`]. It also states
the key limitation: PP_4797 itself has not been experimentally characterized
in *P. putida*. The species review therefore retains the immediate
ribosome-rescue process but does not promote ortholog-derived details about
RF2 selectivity or autoregulation into additional GO assertions.
