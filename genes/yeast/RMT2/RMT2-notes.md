# RMT2 curation notes

Automated deep research was attempted with
`just deep-research-falcon yeast RMT2 --fallback perplexity-lite`, but Falcon was
not available in this runner and the Perplexity fallback resolved to the same
unavailable deep-research client. This review therefore uses cached GOA
publications, the UniProt record, the local PTHR32379 PAINT slice, and a manual
web search for newer RMT2 literature.

RMT2 encodes the S. cerevisiae type IV protein arginine methyltransferase, a
class I-like SAM-binding methyltransferase that forms N5/delta-monomethylarginine
on proteins rather than the omega-N methylarginine products made by the Hmt1/Hsl7
PRMT branch. The original YDR465C/RMT2 discovery mutant specifically disrupted
delta-nitrogen arginine methylation of yeast proteins, and the later direct
biochemical paper expressed and purified Rmt2, identified ribosomal protein L12
as the substrate, and mapped the methyl-acceptor site to Arg67.

The PTHR32379 PAINT table separates the family cleanly. `PTN001282244`, the
broad eukaryotic root, carries `GO:0005634`, `GO:0005737`, and the generic
`GO:0008757` SAM-dependent methyltransferase activity. The vertebrate
`PTN001285367` branch carries guanidinoacetate methyltransferase activity and
creatine biosynthesis. The fungal `PTN001285370` branch carries `GO:0019702`
protein arginine N5-methyltransferase activity. RMT2 receives only the root
localization rows and the fungal activity row. The InterPro2GO row from
RMT2-family `IPR017408` to parent `GO:0016274` is true but redundant because
RMT2 already carries the precise fungal-node `GO:0019702` activity.

For the biological process side of the same chemistry, GO has
`GO:0035246 peptidyl-arginine N-methylation`, which covers Rmt2's modification
of Rpl12 Arg67 without using the omega-N-specific process children. A missing
child for peptidyl-arginine N5-methylation would mirror `GO:0019702`.

The Rmt2 localization evidence is broader than the core activity. Genome-scale
and stress-localization rows place Rmt2 in both nucleus and cytoplasm, and
PMID:17448464 directly reported immunofluorescence/fractionation evidence for
both compartments plus co-purification with Nup49, Nup57 and Nup100. These rows
are useful context, but no compartment-specific methylation event has been
established.

The 2016 ribosomal-protein methyltransferase paper supports the two
`GO:0045903 positive regulation of translational fidelity` rows: rmt2 deletion
was included in ribosome-profile and dual-luciferase reporter assays and Rmt2 was
part of the group required for accurate translation. I kept these annotations as
non-core because the mechanistic paper does not show that Rmt2 itself performs a
translation step; it methylates Rpl12, and failed methylation likely explains the
later ribosome-biogenesis/translation phenotypes.

Nomenclature note: the 2002 Rpl12-substrate abstract calls recombinant S.
cerevisiae RMT2 a "Type III protein-arginine methyltransferase" under the
terminology of the time. The later type IV label distinguishes Rmt2's
delta/N5-monomethylarginine product from omega-N type I, II and III PRMT
products.

Manual web search on 2026-11-06 found one newer S. cerevisiae Rmt2 mention:
Luciano et al. 2026, "A systematic interactome of Saccharomyces cerevisiae SET1C
expands its functional landscape and identifies candidate regulatory
connections" (eLife, DOI:10.7554/eLife.109886), reported Rmt2 enrichment with
Snf2-GFP in set1-null purifications as an ancillary mass-spectrometry result. The
paper did not establish Snf2 as an Rmt2 substrate or a direct Rmt2 chromatin
function, so it does not justify a GO annotation change.
