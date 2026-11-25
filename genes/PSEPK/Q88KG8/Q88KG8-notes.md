# Q88KG8 (oprI / PP_2322) curation notes

## 2026-11-17 — the substrate lipoprotein of the tether-remodeling module

Q88KG8 is the major outer-membrane lipoprotein OprI of *Pseudomonas putida*
KT2440 (locus PP_2322), the ortholog of the well-studied *P. aeruginosa* OprI. It
is the structural substrate of the module: the ErfK-family L,D-transpeptidase
(PP_2320 / PA2854) covalently attaches it to a peptidoglycan stem, and the
YafK/LdtF-family hydrolase can later release it.

It is an 83-residue protein with an N-terminal signal peptide and a lipobox
cysteine (Cys20) that is triacylated (N-palmitoyl + S-diacylglycerol), anchoring
the mature protein in the inner leaflet of the outer membrane; a long coiled-coil
(alanine-zipper, Pfam PF11839; InterPro IPR021793 "Oprl") region mediates
oligomerisation. These are the UniProt sequence-feature annotations on the record
(`file:PSEPK/Q88KG8/Q88KG8-uniprot.txt`, FT:SIGNAL / FT:LIPID / FT:COILED).

## Covalent acceptor residue

The mechanism is established in the *P. aeruginosa* ortholog: the acceptor is the
C-terminal lysine side chain of OprI [PMID:42100858, "Furthermore, we reconstitute
this reaction in vitro with the use of purified recombinant PA2854, OprI, and
synthetic samples of the cell-wall peptidoglycan, in each case documenting the
attachment of the side-chain ε-amino group of Lys83 of OprI to the peptide stem of
the peptidoglycan."]. The KT2440 OprI likewise ends in a C-terminal lysine
(…SRK, Lys83), the expected acceptor; direct demonstration in *P. putida* is still
a gap.

## Curation stance

OprI is the **substrate** being cross-linked, not a participant that performs the
cross-linking chemistry, so it is NOT annotated to GO:0018104
peptidoglycan-protein cross-linking (that process belongs to the transpeptidase).
Its core role is structural: a Braun-lipoprotein-like outer-membrane-to-sacculus
connector. There are no curated GOA annotations for this entry, so the review
proposes two conservative NEW rows (GO:0009279 cell outer membrane location;
GO:0042834 peptidoglycan binding molecular function). The molecular-function term
was chosen by the comparator check: the canonical structural OM lipoprotein,
E. coli Braun's lipoprotein Lpp (P69776), is annotated to GO:0042834 peptidoglycan
binding (TAS) and carries neither GO:0005198 structural molecule activity nor
GO:0005199 structural constituent of cell wall. So GO:0042834 is the convention
for this kind of covalently PG-attached OM lipoprotein, better grounded than a
generic structural term.
