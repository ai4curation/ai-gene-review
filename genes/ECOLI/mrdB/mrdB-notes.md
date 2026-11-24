# Manual notes on mrdB/RodA

RodA/MrdB is the SEDS-family peptidoglycan glycosyltransferase of the Rod complex and should be curated as the glycan-polymerase half of the RodA-PBP2 pair, not as a D,D-transpeptidase.

## UniProt and literature synthesis

- UniProtKB:P0ABG7 records MrdB/RodA as peptidoglycan glycosyltransferase EC 2.4.99.28, a multipass inner-membrane SEDS protein, and the Rod-system partner of MrdA/PBP2.
- Classical genetics split the mrdA/pbpA and mrdB/rodA functions and showed that mrdB/rodA defects make cells spherical and mecillinam-resistant [PMID:6243629, PMID:6451612].
- Biochemical overproduction of PBP2 and RodA in membranes supported their paired requirement for peptidoglycan formation [PMID:3009484].
- Modern in vivo and structural studies assign the glycan-polymerase half of the RodA-PBP2 pair to RodA, with PBP2 providing transpeptidase activity [PMID:27643381, PMID:37620344].

## Annotation review decisions

- The GO:0008955 and peptidoglycan biosynthesis rows are core and should be accepted for RodA.
- RodA is a lateral-wall elongation protein, not the septal FtsW paralog. Cell-division-site and cell-division annotations propagated from the broad SEDS family should therefore be removed.
- The lipid-linked peptidoglycan transporter and lipid-linked peptidoglycan transport rows appear to be FtsW flippase carry-over and should not be kept for RodA.
- Generic protein-binding rows for RodA-PBP2 or RodA-ZapG/YhcB contacts should not be retained as GO:0005515 molecular functions.
