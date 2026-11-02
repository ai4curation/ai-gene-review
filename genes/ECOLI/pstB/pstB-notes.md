# pstB notes

## 2026-10-02

`pstB` encodes the ABC nucleotide-binding subunit of the E. coli PstSACB
high-affinity phosphate importer. In the assembled importer, two PstB chains sit
on the cytoplasmic side of the PstA/PstC permease and supply ATP hydrolysis for
phosphate uptake.

Cox et al. 1989 is the best E. coli site-directed evidence for this role:
Gly48Ile and Lys49Gln substitutions in the putative PstB nucleotide-binding site
abolished phosphate transport through the Pst system and derepressed alkaline
phosphatase [PMID:2646285]. That supports PstB as the transport ATPase and also
reinforces that a defective Pst transporter feeds into Pho signaling.

Gardner et al. showed that PstB interacts physically with PhoU, and PhoU also
contacts PhoR in a membrane-associated phosphate-signaling complex
[PMID:24563032]. That paper validates the EcoCyc interaction behind the
`protein binding` row, but the generic GO term is uninformative for PstB. The
review removes the row while preserving the interaction in the rationale and
keeps the transport module centered on ATP hydrolysis plus phosphate import.
