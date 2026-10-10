# hif1an (Danio rerio) review notes


## Batch 05 curation notes
- Core interpretation: hif1an encodes factor inhibiting HIF, a 2-oxoglutarate/Fe(II)-dependent protein hydroxylase that hydroxylates HIF-alpha and ankyrin-repeat proteins in nucleus/cytoplasm. The core function is protein asparagine/histidine/aspartate dioxygenase activity; vascular and Notch/HIF pathway annotations are regulatory consequences of that catalytic role.
- Key UniProt support: Hydroxylates a specific Asn residue in the C-terminal transactivation domain.
- Existing GOA annotations were reviewed against this core role; broad, inferred, or downstream phenotype annotations were kept as non-core unless they overstate the direct function.

## Re-review 2026-09-29
- Rewrote all templated review blocks (previously every row cited the same two UniProt FUNCTION lines). Localization rows now cite the SUBCELLULAR LOCATION line; the metal/dimerization rows cite COFACTOR/SUBUNIT/BINDING evidence.
- Core molecular function confirmed as protein Asn/His/Asp dioxygenase activity (GO:0036140/0036139/0062101, all ACCEPT) with three regiospecificities of one 2-OG/Fe(II) active site [file:...uniprot.txt "Hydroxylates a specific Asn residue in the C-terminal transactivation domain (CAD) of HIF-1 alpha"; "Also hydroxylates specific Asn, Asp and His residues within ankyrin repeat domain-containing proteins"]. Resolved the two PENDING rows (GO:0030947 IGI, GO:0062101 IEA).
- GO:0008270 zinc ion binding kept as non-core: physiological metal is Fe(II); Zn(II) is the crystallographic surrogate [PMID:12446723 "structures with the inhibitors Zn((II)) and N-oxaloylglycine"]. GO:0031406 (2-OG cosubstrate) and GO:0042803 (obligate homodimer, "homodimerization is essential for catalytic activity") kept as non-core mechanistic components.
- Vascular annotations (GO:0030947, GO:1901343) set/kept KEEP_AS_NON_CORE as downstream regulatory outputs: zebrafish fih-1 morphants show elevated vegf-aa165 and ectopic ISVs, overexpression suppresses ISVs, both VEGF-A-dependent [PMID:25347788 "the expression level of vegf-aa165 is substantially elevated in fih-1 MO-injected embryos"; "our data suggest that FIH-1 negatively regulates VEGF-A signaling via HIF-1"].
- GO:0045746 negative regulation of Notch kept as non-core with propagation_review: mammalian FIH hydroxylates the Notch ICD ankyrin repeats and the biochemical capacity is conserved, but zebrafish canonical Notch targets grl and dll4 are unaltered in fih-1 morphants [PMID:25347788 "expression of grl and dll4, known targets of Notch signaling, appears to be unaltered"], so a zebrafish Notch role is not demonstrated.
- Added PMID:12446723 to references; both PMIDs given reference_review (VERIFIED). Validation: 0 errors, 1 soft warning (no deep-research quote used).
