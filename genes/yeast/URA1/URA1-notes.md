# URA1 (YKL216W, UniProt P28272) notes

## Function
- Fumarate-dependent DHODH (EC 1.3.98.1), class 1A, FMN, homodimer [UniProt:P28272].
- "in vitro studies have revealed that the DHOdehase of S. cerevisiae uses fumarate as terminal electron acceptor" [PMID:1409592].
- Cytosolic: "The DHOdehase from Sch. pombe was localized in the mitochondria whereas its homolog from S. cerevisiae was found to be cytosolic" [PMID:1409592].
- Purified native enzyme "70% identical to that of the Lactococcus lactis DHOD (family IA)"; acceptor preference in vitro "ferricyanide (1), DCPIP (0.54), Qo (0.28), fumarate (0.15), and O2 (0.035)" [PMID:10871048].
- Horizontal transfer: "this enzyme is closely related to a bacterial DHODase from Lactococcus lactis"; "Only the cytoplasmic DHODase promotes growth in the absence of oxygen" [PMID:15014982].

## YeastCyc / GO-CAM issues
- PYRIMID-RNTSYN-PWY uses the quinone reaction DIHYDROOROTATE-DEHYDROGENASE-RXN (EC 1.3.5.2, inner-membrane quinone) for URA1; GO-CAM conversion gave GO:0004152 with no location. Other pathways (PWY-5686-1, PWY0-162, PRPP-PWY-1) correctly use RXN-9929 (fumarate). Module already notes this.

## Review decisions
- Accept GO:1990663 (IEA, RCA) and cytoplasm/cytosol rows.
- MODIFY all GO:0004152 rows (IBA, IEA, IDA, IMP, RCA) -> GO:1990663; MODIFY GO:0016627 -> GO:1990663; MODIFY PRPP-PWY-1 'nucleotide biosynthetic process' -> GO:0044205.
