# unc-51 (Q23023) notes

Deep research: `just deep-research-falcon worm unc-51 --fallback perplexity-lite` failed on
2026-10-08 (falcon exited 137; perplexity provider not available). No deep-research file was
written. This review uses cached publications, PubMed searches and the UniProt record.

Accession: Q23023 (Swiss-Prot, 856 aa, Y60A3A.1). The only UniProt entry for unc-51.

## Key findings
- Founding paper: unc-51 encodes a Ser/Thr kinase needed for axonal elongation; a kinase-dead
  K->M mutant does not rescue and is dominant negative [PMID:7958904 "A Lys-->Met mutation created in vitro in the kinase domain led to the loss of rescuing activity and was dominant negative"].
- Ortholog of yeast Apg1/Atg1 [PMID:9224897 "We found overall homology of Apglp with C. elegans Unc-51 protein"].
- Axon outgrowth substrates: UNC-14 and VAB-8 [PMID:15539493 "show that VAB-8 and UNC-14 can be targets of UNC-51 kinase activity"].
- UNC-5 receptor localization [PMID:16887826 "These results suggest that UNC-51 and UNC-14 regulate the subcellular localization of the Netrin receptor UNC-5"].
- Axon guidance role is separate from autophagy [PMID:20392746 "In C. elegans, UNC-51 regulates the axon guidance of many neurons by a different mechanism than it and its homologs use for autophagy"].
- PHIP-1 phosphorylation in axon regeneration [PMID:36278516 "We demonstrate that UNC-51 phosphorylates PHIP-1 at Ser-112 and activates its catalytic activity"].
- Autophagy complex: binds EPG-1/ATG-13 [PMID:19377305 "directly interacts with, the C. elegans Atg1 homolog UNC-51"]; epg-9 mutants phenocopy unc-51 [PMID:22885670].
- Starvation mitochondrial loss is UNC-51 dependent but nonselective [PMID:30133321 "Autophagy mutants unc-51/Atg1 and atg-18/Atg18 maintained greater mtDNA content than wild-type worms during starvation"].

## Curation decisions
- 5 x protein binding IPI -> REMOVE (uninformative; substrates and complex captured elsewhere).
- Obsolete GO:0034045 (IBA) -> MODIFY to GO:0000407.
- Serine/threonine protein kinase complex (NAS) -> MODIFY to GO:1990316 Atg1/ULK1 kinase complex.
- Piecemeal microautophagy of the nucleus (IBA) -> MARK_AS_OVER_ANNOTATED (fungal NVJ process).
- Developmental and organismal phenotypes (dauer, lifespan, body size, male tail, embryo, necrosis,
  corpse clearance, sex myoblast migration) -> KEEP_AS_NON_CORE.

## For the module curator
UNC-51 has two core roles: (1) the catalytic kinase of the autophagy initiation complex and
(2) an autophagy-independent neuronal kinase for axon outgrowth/guidance. The module should model
only (1).
