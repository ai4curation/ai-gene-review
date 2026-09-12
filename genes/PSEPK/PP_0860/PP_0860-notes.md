# PP_0860 curation notes

## First-pass synthesis

- The unreviewed Q88PJ0 record calls PP_0860 a sulfite-reductase flavoprotein
  component, but supplies no EC number or catalytic reaction
  [UniProtKB:Q88PJ0, "Sulfite reductase, flavoprotein component"].
- Its 849-residue architecture includes flavodoxin-like, FAD/NAD-binding, and
  PepSY-associated transmembrane features. PANTHER places it in an
  iron-regulated inner-membrane-protein-related family, not a specific CysJ
  subfamily.
- Pseudomonas evidence supports an FprA-fed CysI pathway and explicitly
  distinguishes it from E. coli CysJI [PMID:23794620, "pseudomonads utilize
  sulfite reduction enzymology distinct from that of E. coli"].

## Curation decision

PP_0860 remains an unresolved membrane flavoprotein. FMN binding is retained as
a plausible non-core property, the exact ARBA electron-acceptor assignment is
undecided, and the protein is not used to satisfy the core sulfate-reduction
module. Its FAD-binding-domain architecture motivates direct cofactor testing
before proposing GO:0050660.
