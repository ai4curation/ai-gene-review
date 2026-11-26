# NFKB1 review notes

## PTHR24169 context

NFKB1 is the p105/p50 member of the reviewed human PANTHER family `PTHR24169`. The
same family also contains the reviewed human NF-kappaB subunits NFKB2, REL, RELA
and RELB; RELA was already complete on `main`, while NFKB1, NFKB2, REL and RELB
are reviewed in this branch.

## Evidence synthesis

NFKB1 has two tightly linked functional forms. The N-terminal Rel-homology
domain of p105 yields the p50 DNA-binding subunit; purified recombinant p50 was
one of the NF-kappaB/Rel proteins used to select kappaB DNA-binding motifs from
random oligonucleotides [PMID:1406630, "Using purified recombinant p50, p65, and
c-Rel proteins"]. The C-terminal ankyrin-repeat half of p105 provides an
IkappaB-like inhibitory surface: p105 was found with c-Rel or p65 in the
cytoplasm, retained those Rel proteins in cotransfections, and inhibited c-Rel
DNA binding in gel-shift assays [PMID:1423592, "serves I kappa B-like
functions"].

p105 also binds MAP3K8/TPL2 in resting macrophages, stabilizing the kinase but
preventing MEK access until IKK-induced p105 degradation releases MAP3K8 for
MAPK1/3 activation [Reactome:R-HSA-451634; Reactome:R-HSA-5684273]. The
MAPK-cascade rows are therefore biologically real for p105 but secondary to the
core NF-kappaB DNA-binding and cytoplasmic-sequestration functions.

The ACTN4-binding row is similarly direct but specialized: PMID:25411248 assayed
ACTN4 binding to the NFKB1 p50 subunit and recruitment to NF-kappaB promoters in
podocytes, making the row real but not one of the general Rel-family activities.
PMID:20018240 supports collagen I/ILK-induced NF-kappaB activation upstream of
Snail and LEF1 expression; that is a downstream transcriptional output rather
than NFKB1 itself executing a canonical Wnt-signaling step.

Many of the GOA process rows are stimulus-specific outputs of NFKB1-containing
NF-kappaB dimers in macrophages, cancer cells, vascular cells or virus/host
models. They were kept as non-core when they were compatible with direct NFKB1
transcription-factor activity and marked as over-annotated only when the term
placed the transcription factor in a downstream response or a secretory-granule
compartment rather than in the cytoplasmic and nuclear NF-kappaB cycle.

## Automated research

`just deep-research human NFKB1 --provider perplexity` was attempted on
2026-11-26, but this environment exposed only `claude_code` as an available
provider. No `NFKB1-deep-research-perplexity.md` artifact was created or filled
manually.
