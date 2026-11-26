# mge1 review notes

## Retrieval

- `just fetch-gene SCHPO mge1` seeded UniProt, GOA and the review YAML on the
  `mge1` branch.
- `just fetch-gene-pmids SCHPO mge1` found only PMID:12756240, already cached.
- `just mod-description-deep-research SCHPO mge1` skipped `SCHPO`; there is no
  MOD-description provider for PomBase genes in this repository.
- `just deep-research-falcon SCHPO mge1 --fallback perplexity-lite` failed
  because Falcon was unavailable and the Perplexity fallback was not configured.
  I wrote `mge1-deep-research-manual.md` from the cached local evidence instead.
- `just paint-losses SCHPO mge1` reported no PAINT IRD or IKR loss on the
  mge1 lineage.

## GO-CAM 69729a3800007453

The model activity `gomodel:69729a3800007453/6994852c00000297` uses
PomBase:SPBC3B9.19/mge1 to enable `GO:0000774 adenyl-nucleotide exchange
factor activity` in `GO:0005759 mitochondrial matrix`, as part of
`GO:0030150 protein import into mitochondrial matrix` and `GO:0001405 PAM
complex, Tim23 associated import motor`. Those assertions agree with the gene
review: budding-yeast Mge1 stimulates release of both ATP and ADP from Ssc1
[PMID:9048947, "The release of both ATP and ADP from Ssc1 was stimulated in the presence of Mge1"],
and Mge1 is one of the named essential PAM motor subunits
[PMID:14638855, "the nucleotide exchange factor Mge1"].

I did not find a model disagreement for mge1. The GO-CAM evidence also agrees
with the cached PTHR21237 PAINT rows for adenyl-nucleotide exchange, PAM
membership and mitochondrial-matrix import in this fission-yeast GrpE target,
while the PTHR21237 family review leaves the full eukaryotic breadth of the
PAM/import node unresolved.

## Annotation synthesis

mge1 is the single fission-yeast mitochondrial GrpE-family nucleotide-exchange
factor. The UniProt record places the protein in the mitochondrial matrix and
maps it to InterPro:IPR000740, the GrpE family. S. pombe lacks direct
single-gene publications in the local cache, so the functional review rests on
the curated fission-yeast record, orthology to budding-yeast MGE1, human
GRPEL1/2 evidence and the existing PTHR21237 family review.

The core molecular function is nucleotide exchange on mitochondrial Hsp70.
Budding-yeast Mge1 stimulates Ssc1 ATP and ADP release and binds stably to
Ssc1 in vitro [PMID:9048947, "Mge1 bound stably to Ssc1 in vitro"]. Human
GrpEL1 and GrpEL2 independently preserve this function, associating with
mtHsp70 and regulating import and Fe-S biogenesis [PMID:28848044,
"both GrpEL1 and GrpEL2 associate with mtHsp70 as a hetero-oligomeric subcomplex"].

Protein import into the mitochondrial matrix is a direct biological-process
context for the same exchange activity: the PAM motor uses mitochondrial Hsp70
and its J-protein and nucleotide-exchange cofactors to drive matrix
translocation [PMID:14638855, "Transport of preproteins into the mitochondrial matrix is mediated by the presequence translocase-associated motor (PAM)"].
Protein folding and Fe/S cluster assembly are kept as real, broader
mitochondrial Hsp70 contexts rather than as errors: Mge1 drives the Hsp70
nucleotide cycle used after import for substrate folding, and S. cerevisiae
Ssq1 shares Mge1 with Ssc1 during iron-sulfur center biogenesis
[PMID:12756240, "shares a nucleotide exchange factor, Mge1, with a second mitochondrial Hsp70, Ssc1"].
