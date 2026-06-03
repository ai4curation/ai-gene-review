# ANAPC2 notes

## Deep research status

Requested Falcon deep research was attempted with fallback:

`just deep-research-falcon human ANAPC2 --fallback perplexity-lite`

The Falcon provider timed out after the wrapper's 600 second timeout. The configured
`perplexity-lite` fallback then failed with a Perplexity API 401 quota error. No
`ANAPC2-deep-research-falcon.md` or fallback deep-research report was produced, so
this review uses the fetched UniProt record, cached publications, Reactome cache,
PANTHER family metadata, and project-local PN projection reports.

## PN projection evaluation

The PN projection report lists three ANAPC2 gene-GO projections:

- `GO:0005680 anaphase-promoting complex`: `already_in_goa_exact`, so no new
  annotation is needed [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv].
- `GO:0000151 ubiquitin ligase complex`: `entailed_by_goa_closure` from existing
  `GO:0005680 anaphase-promoting complex` and `GO:0031461 cullin-RING ubiquitin
  ligase complex`, so no new direct annotation is needed [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv].
- `GO:0160072 ubiquitin ligase complex scaffold activity`: `new_to_goa` from the
  PN code `Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cullin|degenerate,
  APC sununit` [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_candidate_additions.tsv].

Conservative decision: ANAPC2 is not a canonical cullin like CUL1-CUL5, but the
cached literature supports a cullin-like APC/C scaffold role. UniProt describes
ANAPC2 as belonging to the cullin family and states that ANAPC2 with ANAPC11
constitutes the catalytic APC/C component [genes/human/ANAPC2/ANAPC2-uniprot.txt].
The structural papers describe the catalytic module as Apc2-Apc11 and the
cullin Apc2/RING Apc11 pair as the site where substrates are ubiquitinated
[PMID:16364912; PMID:26083744]. I therefore added `GO:0160072` as a proposed
`NEW` annotation rather than automatically changing existing GOA.

## Annotation review summary

Core ANAPC2 function is as the cullin-like scaffold subunit of the APC/C
E3 ubiquitin ligase catalytic module. It works with ANAPC11 and E2 enzymes to
ubiquitinate APC/C substrates, especially in mitotic cell-cycle transitions and
APC/C-dependent proteasomal degradation [PMID:16364912; PMID:18485873;
PMID:26083744; PMID:29033132].

Neuron-development annotations transferred from mammalian orthology were kept
as non-core where they represent CDC20-APC/C pathway context rather than a
distinct ANAPC2 molecular function. Generic `protein binding` annotations were
not treated as core because they primarily record individual physical
interactions and are less informative than the APC/C scaffold and ubiquitin
ligase module interpretation.
