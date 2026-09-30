# kuz (Kuzbanian, ADAM10 ortholog) — curation notes

Drosophila melanogaster, FBgn0259984, CG7147. No Swiss-Prot entry exists; all six UniProt
entries for kuz are unreviewed TrEMBL. The first fetch resolved to A8DZ02 (26 GOA rows); the
FlyBase GO annotations are attached to **Q9VJW9** (48 GOA rows), so the gene was re-fetched
with `--uniprot-id Q9VJW9`. PANTHER PTHR45702 (ADAM10/ADAM17 METALLOPEPTIDASE FAMILY MEMBER),
subfamily PTHR45702:SF2 (KUZBANIAN, ISOFORM A).

## Notch role: S2 protease (signal-receiving cell)

- Protease activity required; catalytically dead KUZ is dominant negative; Notch is an in vivo
  substrate [PMID:9244301 "We provide genetic and biochemical evidence that Notch is an in vivo
  substrate for the KUZ protease"].
- S2 cleavage [PMID:11799064 "Our data suggest that in Drosophila, kuzbanian can mediate S2
  cleavage of Notch."]; required independently of any role in Delta processing.
- Cell-autonomous in the Notch-activated cell, upstream of Su(H) [PMID:9428413].
- Ligand-dependent activation; overexpression gives ligand-independent activation
  [PMID:18535782]; Kuz levels in the midgut set a proteolytic threshold, ligand-independent
  cleavage restrained by cis-Delta [PMID:41556123].
- "Notch activation normally depends on Kuz (S2) and γ-secretase (S3) cleavages."
  [PMID:29195077].
- TspanC8 tetraspanins (Tsp3A, Tsp86D, Tsp26D) regulate Kuz trafficking/distribution
  [PMID:23091066].

## Other substrates
- Delta ectodomain shedding [PMID:9872749]; paralog Kul is the main Dl sheddase in wing
  [PMID:15576412].
- Robo ectodomain cleavage required for midline repulsion [PMID:20570941].

## Pathway variant notes
- Drosophila has Kuz (ADAM10), Kul (Kuzbanian-like, ADAM10-like paralog, mainly Dl) and Tace
  (ADAM17; can activate Notch ligand-independently, [PMID:18535782]). C. elegans uses SUP-17
  (ADAM10) and ADM-4 (ADAM17).

## Annotation decisions
- REMOVE GO:0005515 (TspanC8 IPI; uninformative).
- MARK_AS_OVER_ANNOTATED: GO:0005737 cytoplasm, GO:0043226 organelle (ARBA IEA; TM protein).
- IDA metalloendopeptidase from PMID:15576412 (abstract foregrounds Kul): ACCEPT, deferring to
  curator per project rules.

## Deep research
- falcon runs hit rate limits/timeouts; relaunched with longer timeout.
