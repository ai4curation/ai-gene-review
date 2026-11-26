# Manual deep research for S. pombe ssc1

Automated deep research was unavailable for this review, so the evidence was
assembled from cached S. pombe publications, the UniProt record, the PAM import
literature already used in this GO-CAM campaign, and the PTHR19375 Hsp70 family
review.

## S. pombe identity and localization

Powell and Watts cloned an S. pombe gene encoding a mitochondrial Hsp70 and
showed that antibody to the C terminus of Ssp1 detected a 70-kDa protein
associated with mitochondria [PMID:2123810, "Western-blot analysis with
immunoglobulin G raised against a peptide corresponding to the C terminus of the
SSP1 protein indicates a 70-kDa protein which is associated with the
mitochondria"]. Kasai and Isono cloned the same locus as a homolog of
budding-yeast SSC1 and identified predicted mitochondrial targeting-sequence
features at the N terminus [PMID:1923816, "The SSP1 gene contains two
methionine codons in the region predicted to encode a mitochondrial targeting
signal sequence of its protein (Ssp1)"].

UniProt curates the mature S. pombe protein as mitochondrial matrix-localized,
with a cleavable N-terminal transit peptide, an Hsp70 ATPase catalytic record,
and interaction with the Fe/S-cluster assembly proteins Isu1 and Jac1
[file:SCHPO/ssc1/ssc1-uniprot.txt, "Mitochondrion matrix"]. That record also
states by similarity that ssc1 is a PAM-complex component and the ATP-driven
core of the mitochondrial import motor [file:SCHPO/ssc1/ssc1-uniprot.txt,
"Constitutes the ATP-driven core of the motor"].

## Matrix-import motor

Budding-yeast work establishes the mechanistic role of the Ssc1 ortholog in
matrix import. Geissler and colleagues described the presequence
translocase-associated motor as the TIM23-associated matrix motor for
preproteins, with mtHsp70/Ssc1 at the core: "the mitochondrial Hsp70 (mtHsp70)
of the matrix forms the core of the protein import motor and directly binds to
the preprotein in transit" [PMID:14638855]. Schilke, Hayashi and Craig later
summarized the same module as a highly conserved Hsp70-based import motor on
the matrix side of the inner membrane [PMID:22298705, "A highly conserved,
Hsp70-based, import motor, which is associated with the translocase on the
matrix side of the inner mitochondrial membrane, is critical for protein
translocation into the matrix."].

The existing PomBase ISO rows to `GO:0001405 PAM complex, Tim23 associated
import motor`, `GO:0030150 protein import into mitochondrial matrix`, and
`GO:0140388 protein translocation chaperone activity` are therefore supported
by orthology to budding-yeast SSC1 plus the S. pombe-specific mitochondrial
Hsp70 identity. The current GO-CAM captures ssc1 in the right process, complex,
and matrix compartment, but it still types the activity as generic
`GO:0016887 ATP hydrolysis activity`; the gene review keeps that ATPase term and
also accepts the more specific existing GOA row for
`GO:0140388 protein translocation chaperone activity`.

## Fe/S-cluster biogenesis

S. pombe Ssc1 is also the mitochondrial Hsp70 that services Fe/S-cluster
biogenesis. Delewski and colleagues compared S. pombe Jac1/Ssc1 with the S.
cerevisiae Jac1/Ssq1 pair and noted that "in most eukaryotes, including
Schizosaccharomyces pombe, FeS biogenesis involves interaction between the
J-protein Jac1 and the multifunctional Hsp70 Ssc1" [PMID:26545917]. The same
paper is the direct experimental source for the S. pombe ATP hydrolysis,
ATP-dependent chaperone, and [2Fe-2S] cluster assembly rows.

The PTHR19375 Hsp70 PAINT review agrees with this division of labor. Its
mitochondrial Hsp70 node supports both mitochondrion and iron-sulfur cluster
assembly for ssc1, while the Hsp70-family root supports ATP hydrolysis and
generic Hsp70 co-chaperone binding [file:interpro/panther/PTHR19375/PTHR19375-review.yaml,
"ATP hydrolysis by the nucleotide-binding domain is the shared engine of the
family"].

## Over-broad inherited annotations

Two inherited rows need qualification rather than simple acceptance. The PAINT
cytoplasm row is true only because GO's cytoplasm class includes mitochondria;
the active compartment for ssc1 is better stated as the mitochondrial matrix
[file:interpro/panther/PTHR19375/PTHR19375-review.yaml, "Cytoplasm (which in GO
includes mitochondria, plastids and the ER) is true of every compartment branch
seeded at this node."]. The PTHR19375 root protein-refolding assertion is a
real Hsp70-family statement for DnaK, cytosolic Hsp70s and BiP, but the family
review already flags this root placement as over-propagating to specialized
Fe/S branches [file:interpro/panther/PTHR19375/PTHR19375-review.yaml,
"Refolding of denatured or aggregated proteins is well supported for DnaK,
cytosolic HSC70/HSP70 and BiP, but the root placement also propagates it to the
dedicated Fe-S branch"].
