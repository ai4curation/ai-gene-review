# degP manual review notes

Deep research and FEBA fitness summaries were unavailable for this newly seeded
review, so I grounded the review in `degP-uniprot.txt` plus the cached GOA
PMIDs.

## Core biology

DegP/HtrA is a Sec-exported HtrA-family protease-chaperone. The UniProt record
identifies residues 1-26 as a signal peptide and residues 27-474 as the mature
periplasmic serine endoprotease DegP. The mature protein has a trypsin-like
serine protease domain followed by two PDZ domains, and the catalytic triad is
His131, Asp161, Ser236 in UniProt numbering.

The core catalytic activity is serine endoproteolysis of misfolded envelope
proteins. Lipinska et al. purified HtrA/DegP and showed that "The HtrA protein
was shown to be a specific endopeptidase which was inhibited by
diisopropylfluorophosphate" [PMID:2180903]. Active-site mutagenesis later
showed that changing the catalytic Ser and His residues eliminated HtrA
proteolytic activity and high-temperature complementation [PMID:7557477].
Krojer et al. then dissected the mechanism: "DegP processively degrades
misfolded proteins into peptides of defined size" and PDZ1 presents misfolded
substrates to the catalytic site [PMID:18505836].

DegP is also a temperature-switched chaperone/protease. Spiess et al. reported
that the "heat shock protein DegP (HtrA) has both general molecular chaperone
and proteolytic activities" and that chaperone function dominates at low
temperature whereas proteolysis appears at elevated temperature [PMID:10319814].
This supports adding `GO:0044183 protein folding chaperone` as a NEW molecular
function alongside the existing `GO:0006457 protein folding` process row.

## Oligomerization

DegP homooligomerization is mechanistically central but best treated as
non-core structural context. Krojer et al. 2002 solved a DegP hexamer "formed
by staggered association of trimeric rings" [PMID:11919638]. Substrate binding
then drives higher-order cages: the 2008 Nature and PNAS papers both showed
that misfolded protein or substrate binding converts resting hexamers into
12-mer and 24-mer assemblies [PMID:18496527; PMID:18697939], and Kim et al.
showed that linked active-site and PDZ1 degrons are sufficient to trigger
cooperative cage assembly until intact substrate is depleted [PMID:21458668].

## OMP and envelope quality-control context

The SurA/Skp/OMP-biology context argues against annotating DegP as a direct
participant in every OMP phenotype. Sklar et al. conclude that SurA is the
primary route for bulk OMP transit to YaeT/BAM and that "DegP/Skp function to
rescue OMPs that fall off the SurA pathway" [PMID:17908933]. Ge et al.
identified beta-barrel OMPs as major natural DegP substrates but also concluded
that DegP primarily functions as a protease in vivo to eliminate unfolded OMPs
[PMID:24373465]. I therefore kept `protein quality control` and proteolysis as
core and did not add `GO:0043165 Gram-negative-bacterium-type cell outer
membrane assembly` or `GO:0140309 unfolded protein holdase activity`.

## Localization

DegP is periplasmic but can associate with the periplasmic face of the inner
membrane. Skorko-Glonek et al. found HtrA in the inner-membrane fraction and
interpreted the combined biochemical and genetic evidence as indicating that
"HtrA is a peripheral membrane protein, localized on the periplasmic side of
the inner membrane" [PMID:9083020]. Later work on membrane-bound bowl-like DegP
states showed that "membrane-bound DegP assemblies have the capacity to recruit
and process substrates in the bowl chamber" [PMID:19255437]. I accepted the
periplasmic rows as core and kept the plasma-membrane rows as non-core.

## Generic protein binding rows

All seeded `GO:0005515 protein binding` rows were removed rather than kept as
non-core. The OmpA/OmpC rows represent substrate recognition within the
protease/chaperone cycle [PMID:18496527; PMID:24373465]; the lysozyme and
beta-casein rows are xenogeneic model-substrate interactions [PMID:18697939;
PMID:20581825; PMID:20581826; PMID:21458668]; the OmpA interaction from the
RcsF paper is generic and not visible in the cached abstract [PMID:25525882];
and the beta-casein interaction from PMID:28642151 is explicitly from human
HtrA3, not E. coli DegP.
