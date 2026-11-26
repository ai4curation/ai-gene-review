# Manual deep research for S. pombe tim44

Automated deep research was unavailable for this review, so the evidence was
assembled from the S. pombe UniProt record, the cached PAM-import literature
used by other genes in this GO-CAM campaign, and the PTHR10721 Tim44 PAINT
table.

## Identity and family placement

The S. pombe O60084 record curates `tim44` as mitochondrial import inner
membrane translocase subunit Tim44, a member of the Tim44 family with the
Tim44 InterPro signature `IPR017303` and with PANTHER placement in
`PTHR10721:SF1`, the same subfamily as budding-yeast TIM44/Q01852
[file:SCHPO/tim44/tim44-uniprot.txt, "PANTHER; PTHR10721:SF1"].

PTHR10721 PAINT places three assertions at the eukaryotic Tim44 node
`PTN000076497`: `GO:0001405 PAM complex, Tim23 associated import motor`,
`GO:0140378 protein complex scaffold activity`, and `GO:0030150 protein
import into mitochondrial matrix`
[file:interpro/panther/PTHR10721/PTHR10721-paint.tsv,
"PTHR10721	PTN000076497"]. `just paint-losses SCHPO tim44` reported no IRD
or IKR losses on the S. pombe `tim44` lineage.

## PAM motor scaffold for matrix import

Budding-yeast evidence establishes the conserved role of Tim44 at the matrix
face of the TIM23/PAM motor. Truscott and colleagues summarized the known PAM
motor at the time as mtHsp70/Ssc1, Tim44, and Mge1, saying that "the
peripheral inner membrane protein Tim44 ... serves as a binding partner for
mtHsp70" [PMID:14638855].

Hutu and colleagues then directly assayed conditional budding-yeast `tim44`
mutants. The paper states that `tim44-804` mitochondria are "selectively
impaired in the import of matrix-targeted precursor proteins" and shows that
Tim44 is needed for the normal association of the Pam18/Pam16 J-complex with
TIM23 while also restraining Pam17 association [PMID:18400944]. Its final model
is that "Tim44 promotes the binding of the J-complex to the presequence
translocase but impairs the binding of Pam17" [PMID:18400944]. This is more
specific than a passive scaffold, but it still supports GO:0140378 for a
protein that helps assemble and position PAM modules at the translocase.

## Localization and GO-CAM context

UniProt places S. pombe tim44 at the mitochondrial inner membrane as a
peripheral membrane protein by similarity to budding-yeast Tim44
[file:SCHPO/tim44/tim44-uniprot.txt, "Mitochondrion inner membrane"]. That
matches the two current inner-membrane CC rows. The GO-CAM
`69729a3800007453` activity for Tim44 instead has `occurs_in GO:0005759
mitochondrial matrix`; this is not a conflict for an activity node because
Tim44 is a peripheral inner-membrane protein whose Hsp70/J-complex scaffold
function acts on the matrix face of TIM23.

## Existing annotation review

The two `GO:0001405` rows and all three `GO:0030150` rows should be accepted
as conserved Tim44/PAM assertions. The InterPro2GO `GO:0051087
protein-folding chaperone binding` row should also be accepted because Tim44
binds the mtHsp70 chaperone at the presequence translocase rather than acting
as the Hsp70 ATPase itself. The matching IBA row to `GO:0051087` is stale
relative to the current PTHR10721 PAINT table, which now asserts
`GO:0140378 protein complex scaffold activity` instead, but the underlying
Tim44-mtHsp70 binding claim remains true. GOA is missing that 2026 PAINT
assertion to `GO:0140378`, which matches both the budding-yeast `tim44`
mutant evidence and this GO-CAM activity.
