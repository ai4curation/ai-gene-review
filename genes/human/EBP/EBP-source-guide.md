---
gene: EBP
annotation_scope:
  historical_annotations: 40
  machine_added_annotations: 172
  reviewed_annotations: 212
  new_annotations: 0
  retired_source_contexts: 2
---

# EBP source and evidence guide

This guide records actual source access and locates the supporting evidence. It is not an independent biological study. Existing publication caches and their availability flags remain unchanged even when an original was obtained separately. All source identities are retained; only two historical export contexts receive source-lifecycle retirement markers.

## Primary sources

| Source | Effective cache | Actual reading and limits |
| --- | --- | --- |
| [PMID:10391218](https://pubmed.ncbi.nlm.nih.gov/10391218/) | Abstract only; preserved existing cache | Human CDPX2 and tattered-mouse genetic evidence. No unseen full-paper assay or construct detail; independent human biochemistry supports the retained isomerase function. |
| [PMID:10391219](https://pubmed.ncbi.nlm.nih.gov/10391219/) | Abstract only; preserved existing cache | Human patient sterol profiles and yeast complementation of human variants; developmental conclusion. No independently recovered full-body assay detail; retains experimental source and separates host from protein species. |
| [PMID:10406945](https://pubmed.ncbi.nlm.nih.gov/10406945/) | Abstract only; preserved existing cache | Native human cell ER/nuclear-envelope microscopy and mitotic vesicle redistribution. No figure pixels; text/caption antibody panel letters conflict, so no panel-specific assignment. Old four-TM proposal superseded by structure. |
| [PMID:12760743](https://pubmed.ncbi.nlm.nih.gov/12760743/) | Abstract only; preserved existing cache | Explicit human EBP positive controls versus EBPL; cross-linking self-association. Foreground EBPL title is not misattribution. Detailed unseen constructs not asserted. |
| [PMID:7706302](https://pubmed.ncbi.nlm.nih.gov/7706302/) | Abstract only; preserved existing cache | Human and guinea-pig cloning/heterologous drug-binding study; historical hydropathy topology. Four predicted helices not treated as current structure; no full-body claim. |
| [PMID:8798407](https://pubmed.ncbi.nlm.nih.gov/8798407/) | Abstract only; preserved existing cache | Human and mouse cDNAs restore sterol-isomerase activity in yeast. No human-cell flux claim or unseen exact substrate panel. |
| [PMID:9894009](https://pubmed.ncbi.nlm.nih.gov/9894009/) | Abstract only; preserved existing cache | Human EBP mutagenesis/yeast sterol function. Full original unavailable; historical H77/E81/E123/W197 numbering remains source-specific. |
| [PMID:20615952](https://pubmed.ncbi.nlm.nih.gov/20615952/) | Abstract only; preserved existing cache | Cooperative EBP/DHCR7 ChEH evidence from COS-7 coexpression and human MCF-7 depletion. No independent autonomous EBP hydrolase proof; supplemental routes unavailable. Preserved main abstract-only cache remains unchanged. |
| [PMID:15175332](https://pubmed.ncbi.nlm.nih.gov/15175332/) | Abstract only; added cache | EBP/DHCR7 coexpression and interaction in microsomal antiestrogen-binding context. Abstract-only supporting context; no unseen body details. |
| [PMID:25910212](https://pubmed.ncbi.nlm.nih.gov/25910212/) | Full text; preserved existing cache | Sequence-verified WT/mutant Y2H profiling and pairwise confirmation. Literal EBP/CREB3 variants and assay fields extracted from IntAct. Do not assign a tested orthogonal assay to a pair merely because a subset was benchmarked. |
| [PMID:32296183](https://pubmed.ncbi.nlm.nih.gov/32296183/) | Full text; preserved existing cache | HuRI binary Y2H screens, sequence-confirmed retesting and subset orthogonal benchmarking. No universal native physiological interaction or per-pair orthogonal validation; interactor ROGID is not complete construct authentication. |
| [PMID:31165728](https://pubmed.ncbi.nlm.nih.gov/31165728/) | Full text; added cache | Human purified zymostenol-d7 assay, five-TM crystal structure, ligand binding, dimer/coassociation and mutant tests. No native stoichiometry requirement, substrate cocrystal or measured drug export; no figure pixels/SI read. Current H76/E80/E122/W196 matches the source. |
| [PMID:12133002](https://pubmed.ncbi.nlm.nih.gov/12133002/) | Abstract only; added cache | Sequence-verified human hSI; substrate breadth and GC-MS product identification in recombinant preparations. Table3 uses bacterial homogenates; yeast-purified kinetics and oligomer estimate are separate. No endogenous human fecosterol pathway or obligatory native tetramer. |

The original PMID:10406945 Methods, native localization Results, mitotic-vesicle Results, Figure8 caption and Discussion were read through the [publisher text](https://febs.onlinelibrary.wiley.com/doi/10.1046/j.1432-1327.1999.00500.x). The panel-letter discrepancy is retained; no image pixels were inspected.

For PMID:12133002, the [author-uploaded original](https://www.researchgate.net/publication/11248791_Purification_characterization_and_catalytic_properties_of_human_sterol_8-isomerase) supplies human construct Methods and Tables 3–4. The human cDNA identity, substrate-specific bacterial-homogenate activity and GC-MS product assignments were read; the normal repository cache remains abstract-only. The separate yeast-purified assays and oligomer estimate do not establish obligatory native stoichiometry.

The [PMID:31165728 original](https://pmc.ncbi.nlm.nih.gov/articles/PMC6549186/) supplies the human recombinant purification, zymostenol-d7 assay and five-helix structural Results. The [PMID:20615952 main original](https://pmc.ncbi.nlm.nih.gov/articles/PMC2922168/) supplies the cooperative ChEH Methods/Results; supplementary access failed. The latter full main paper was read separately from its preserved abstract cache. Neither source establishes an autonomous EBP drug-export activity.

The interaction Methods/Results were read from the full text of [PMID:25910212](https://pmc.ncbi.nlm.nih.gov/articles/PMC4441215/) and [PMID:32296183](https://pmc.ncbi.nlm.nih.gov/articles/PMC7169983/). Their sequence-confirmed Y2H retesting is distinguished from orthogonal benchmarking of a subset. No pair-specific orthogonal assay is inferred solely from study-wide benchmarking.

## Database and reaction evidence

The [portable source audit](EBP-bioinformatics/source-audit/RESULTS.md) contains a saved-input script, exact hashed database archive, complete selected interaction fields and an independent [partner-class table](EBP-bioinformatics/source-audit/partner-classes.md). Its 527 selected records are the union of 524 HuRI records and 3 disease-screen records. The historical aggregate remains separate from the 169 individual HuRI source rows. Sequence checks authenticate 1,042 current-record occurrences plus 3 historical SLC3A2 occurrences; 9 clone-only occurrences remain unresolved. These counts describe evidence scope, not assay strength.

The [official human EBP record](https://www.uniprot.org/uniprotkb/Q15125/entry) supplies one 230-aa primary sequence. The current sequence agrees with the 2019 residue numbering; the 1999 abstract uses H77/E81/E123/W197; the cause of the offset is unestablished. Initiator processing is not a separate splice isoform, and differing oligomer estimates from different preparations do not define an obligatory native assembly.

The PTHR14207 audit retains the exact target sequence, 263-node topology and literal family IBD/IRD assertions. It separately grounds the donor contexts in [mouse P70245](https://www.uniprot.org/uniprotkb/P70245/entry), [rat Q9JJ46](https://www.uniprot.org/uniprotkb/Q9JJ46/entry), [human EBPL Q9BY08](https://www.uniprot.org/uniprotkb/Q9BY08/entry) and [Arabidopsis O48962](https://www.uniprot.org/uniprotkb/O48962/entry). EBPL-branch IRDs lie outside the EBP path; broad GO-slim display strings are not substitutes for literal assertions.

The [HPA EBP subcellular page](https://www.proteinatlas.org/ENSG00000147155-EBP/subcellular) independently marks ER and nuclear membrane as supported, with the multiple-gene-target antibody caution. A431, HaCaT and U2OS cell contexts are kept distinct. No HPA pixel inspection is claimed.

[Reactome R-HSA-195690](https://reactome.org/content/detail/R-HSA-195690) and [R-HSA-6807052](https://reactome.org/content/detail/R-HSA-6807052) join through catalyst 195674/entity 195697 to Q15125 residues 2–230 in ER membrane. Their explicit zymosterol and zymostenol reactions are retained despite a mismatched generic activity label. [GO-CAM 6796b94c00001560](../../../gocams/6796b94c00001560/6796b94c00001560-src.yaml) is also preserved locally at `gocams/6796b94c00001560/`: activity 6796b94c00002826 uses GO:0000247 but explicitly models CHEBI:18252 zymosterol to CHEBI:16290 cholesta-7,24-dien-3beta-ol. This is a term-scope discrepancy in an existing model, not an omitted substrate pair or evidence for a human fecosterol pathway.

Current [GO:0047750](https://www.ebi.ac.uk/QuickGO/term/GO:0047750), [GO:0000247](https://www.ebi.ac.uk/QuickGO/term/GO:0000247) and [GO:0004769](https://www.ebi.ac.uk/QuickGO/term/GO:0004769) definitions distinguish the principal cholestenol chemistry, experimentally supported broader substrate use and the incorrectly specific steroid reaction label. The saved term responses are included in the executed audit.

## Source lifecycle and quotation scope

The [source provenance](source-snapshots/source-provenance.json) preserves the exact historical GOA, complete current/historical key comparison and the two absent historical contexts. All 40 original source dictionaries remain unchanged except the explicit retirement flag at indices 5 and 14; 172 additions are imported source contexts. The original notes are an exact prefix. The 49 inherited row excerpt occurrences and 2 inherited core excerpts are preserved. No new supporting-text quotation is introduced.
