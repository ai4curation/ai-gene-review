# mge1 manual deep research

The automated Falcon and Perplexity deep-research providers were unavailable
for this review, so this file records a concise manual synthesis from the
cached repository evidence.

## Identity and family

S. pombe mge1 (SPBC3B9.19; UniProt O43047) encodes a 223-aa mitochondrial
GrpE-family protein with a predicted N-terminal mitochondrial transit peptide.
The UniProt entry calls it an essential PAM-complex component that controls the
nucleotide-dependent binding of the matrix Hsp70 ssc1 to substrate proteins by
similarity, places it in the mitochondrial matrix and maps it to InterPro
GrpE signatures IPR000740, IPR013805 and IPR009012.

The local PTHR21237 PAINT cache contains three relevant non-bacterial
assertions on the GrpE family:

- `PTHR21237 PTN000478264 GO:0000774 F IBD false`: adenyl-nucleotide exchange
  factor activity.
- `PTHR21237 PTN000478265 GO:0001405 C IBD false`: PAM complex, Tim23
  associated import motor.
- `PTHR21237 PTN000478265 GO:0030150 P IBD false`: protein import into
  mitochondrial matrix.

The family review judged the nucleotide-exchange activity sound across
GrpE-like proteins. It retained the mitochondrial PAM/import assertions but
left the full breadth of the eukaryotic PTN000478265 node unresolved, so this
review accepts the two S. pombe mge1 transfers from a clean PAINT loss check,
the fission-yeast mitochondrial GrpE identity and the local GO-CAM/UniProt
context rather than by declaring the whole family node settled.

## Primary evidence from orthologs

Miao et al. directly characterized S. cerevisiae Mge1 and concluded that it
functions as the nucleotide-release factor for matrix Hsp70 Ssc1: "The release
of both ATP and ADP from Ssc1 was stimulated in the presence of Mge1" and
"Mge1 bound stably to Ssc1 in vitro" [PMID:9048947]. This supports
`GO:0000774 adenyl-nucleotide exchange factor activity` and
`GO:0051087 protein-folding chaperone binding`.

Truscott et al. reviewed the state of the PAM motor when characterizing Pam18,
listing mitochondrial Hsp70, Tim44 and "the nucleotide exchange factor Mge1" as
three known essential subunits of the motor, and placed PAM in matrix
preprotein transport [PMID:14638855]. This supports the model's use of mge1 in
`GO:0030150 protein import into mitochondrial matrix` and the curated
`GO:0001405 PAM complex, Tim23 associated import motor` row.

Srivastava et al. showed that human GRPEL1 and GRPEL2 associate with mtHsp70
and regulate mtHsp70 functions including "import of preproteins and biogenesis
of Fe-S clusters" [PMID:28848044]. Their discussion also contrasts mammalian
NEF oligomers with the NEF dimers observed in lower organisms, consistent with
the InterPro homodimerization mapping for single-copy fungal Mge1.

Dutkiewicz et al. studied the budding-yeast Ssq1/Jac1/Isu system and note that
Ssq1 "shares a nucleotide exchange factor, Mge1, with a second mitochondrial
Hsp70, Ssc1" [PMID:12756240]. The cached record is abstract-only, but the
PomBase ISO row is biologically plausible and is retained as a non-core
Mge1/Ssq1 Fe/S-assembly role.

## GO-CAM consistency

GO-CAM 69729a3800007453 represents mge1 as a mitochondrial-matrix
adenyl-nucleotide exchange factor in the PAM motor for preprotein import into
the mitochondrial matrix. The gene review agrees with those assertions and
does not add a mge1-specific GO-CAM disagreement.
