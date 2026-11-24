# RAB1A notes

## Deep research

Automated deep research was attempted for RAB1A with the retained shared runtime, but no provider API key was available in the environment. The manual review used the seeded GOA rows, the cached UniProt flat file, cached primary publications, relevant Reactome records, the GO-CAM `65692e7e00001822` source and review, and a PAINT loss check.

The PAINT loss check reported that `PTHR47977` could not be checked because `P62820` is not a leaf of that tree, and found no IRD or IKR loss on the RAB1A lineage.

## Literature synthesis

RAB1A is a Rab small GTPase: the original human Rab cloning paper produced human Rab proteins recombinantly and found that "All six proteins bind GTP and exhibit GTPase activities" [PMID:2501306].

Its central route is ER-to-Golgi traffic. TBC1D20 is the ER-localized Rab1 GAP, and overexpressing active TBC1D20 blocks secretory cargo movement out of the ER and disrupts the Golgi [PMID:17684057, "TBC1D20 is the ER-localized GAP for Rab1"]. Bacterial VirA/EspG GAPs independently confirm the same step by inactivating host Rab1 and disrupting ER-to-Golgi traffic [PMID:22939626, "Specific inactivation of Rab1 by VirA/EspG disrupts ER-to-Golgi trafficking"].

RAB1A also contributes to early autophagy. VirA-mediated Rab1 inactivation helps *Shigella flexneri* escape autophagy-mediated host defense [PMID:22939626, "S. flexneri intracellular persistence requires VirA TBC-like GAP activity"], and C9orf72 links Rab1a to the ULK1 initiation complex to facilitate ULK1 trafficking to the phagophore [PMID:27334615, "facilitate its trafficking to the phagophore and initiate autophagosome formation"].

Secondary routes include Kifc1-dependent minus-end motility of early endocytic vesicles [PMID:21303926, "Rab1a regulates minus-end-directed motility largely by recruiting Kifc1"], integrin beta1 recycling during cell spreading and migration [PMID:20639577, "decreased recycling of integrin beta1 to the plasma membrane"], and ER export of HSV-1 glycoproteins to post-ER assembly compartments during secondary envelopment [PMID:21680502, "In the absence of Rab1a/b, the viral glycoproteins are unable to traffic"].

PMID:25446900 identifies a signaling role rather than another ER-to-Golgi cargo route: amino acids stimulate RAB1A GTP binding and interaction with mTORC1/RAPTOR at the Golgi, and Rab1A overexpression increases mTORC1 signaling and oncogenic growth in a Golgi- and GTP-dependent manner [PMID:25446900, "AA stimulates Rab1A GTP binding and interaction with mTORC1 and Rheb-mTORC1 interaction in the Golgi"]. The current GOA row for MTOR/RPTOR is only bare `GO:0005515 protein binding`, so this review removes the generic binding rows and tracks the mTORC1 biology as a secondary signaling output needing a precise GO modeling decision.

RNF115 restrains a TLR-specific RAB1A route. In that model, RAB1A carries TLR cargoes from the ER to the Golgi; RNF115 K11-ubiquitinates RAB1A and RAB13 near their switch regions and impairs GDI1 recruitment, thereby limiting reuse of the two Rabs [PMID:35343654, "Specifically, RAB1A promotes the trafficking of TLRs from the ER to the Golgi apparatus"].

## GO-CAM 65692e7e00001822 consistency notes

- The model's RAB1A activity uses `GO:0003924` at the ER and `part_of` `GO:0006888`. This is consistent with the RAB1A review: the same molecular function, ER localization, and ER-to-Golgi process are accepted and central.
- The GO-CAM still connects RAB1A only by the incoming GDI1 edge. PMID:35343654 assigns RAB1A to the first cargo leg of the pathway, ER-to-Golgi TLR traffic, while RAB13 mediates the next Golgi-to-surface leg. The final GO-CAM notes PR should keep the existing model note that an edge from RAB1A to the RAB13/TLR cargo step would make RAB1A's pathway role explicit.
