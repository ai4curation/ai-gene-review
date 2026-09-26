# LONRF1 review notes

## Identity and source reconstruction

LONRF1 is the current approved HGNC symbol (HGNC:26302) for reviewed human UniProt Q17RB8. UniProt displays a 773-aa canonical product and one annotated splice product, Q17RB8-2, which lacks residues 452–462. No current GOA row targets an isoform: all 110 live QuickGO rows use canonical `UniProtKB:Q17RB8`.

The 110 live rows normalize to 11 review objects. The apparent compression is almost entirely interaction-screen multiplicity: PMID:25416956 contributes 27 distinct WITH/FROM partners to one GO:0005515 row, PMID:32296183 contributes 73 partners to another, and PMID:31515488 contributes two. Ordered source unions were restored exactly, giving 108 WITH/FROM tokens across the 11 objects. Live QuickGO contains no NOT qualifiers and no annotation extensions.

## Domain and database evidence

The current UniProt record has no curated FUNCTION or SUBCELLULAR LOCATION comment. It annotates two zinc-binding regions, including a RING-type zinc finger at residues 479–517, and a C-terminal LON peptidase N-terminal domain at residues 558–768. The name and domain architecture must not be used to infer protease activity: the annotated LON-family segment is not itself a complete peptidase catalytic module.

The existing GO molecular-function evidence consists of an IBA `ubiquitin protein ligase activity` row and an InterPro-derived generic `metal ion binding` row. UniProt also displays electronic `zinc ion binding`, which is more specific than generic metal-ion binding but does not by itself demonstrate catalysis. Whether the RING domain is an active E3 module, and whether the N-terminal zinc-binding region contributes to activity or scaffolding, require literature or biochemical evidence.

The reproducible analysis in `LONRF1-bioinformatics/RESULTS.md` confirms two conserved Cys/His-rich RING regions with InterPro conserved-site annotations. The first has a canonical-looking C3HC4 spacing and is 97.3% identical to the mouse ortholog; the second is identical to mouse and strongly conserved in human LONRF2/3. This supports structural zinc coordination and compatibility with a RING-E3 mechanism, but sequence conservation alone is not a catalytic assay. In contrast, LONRF1 contains the Lon N-terminal substrate-binding domain but lacks the AAA+ ATPase, peptidase, and active-site features recovered in the LONP1 control, strongly bounding the name-based peptidase hazard.

Reactome places LONRF1 in generic cytosolic ubiquitination-cycle reactions (E3/substrate/E2-Ub engagement, ubiquitin transfer, substrate polyubiquitination, and E3 release). Those pathway records describe a general RING-E3 mechanism and do not expose an LONRF1-specific substrate or biochemical experiment in their cached summaries. Cytosol is therefore plausible pathway context rather than a directly imaged core location.

## Interaction-screen boundary

Five normalized annotations use GO:0005515 `protein binding`. Four are proteome-scale interaction or edgotyping datasets and one is an E2-enzyme network. The individual edges may be valid source observations, but the generic GO term is not an informative molecular function. Large partner counts, repeated partners across studies, and isoform-form accessions in WITH/FROM must be preserved as provenance without treating LONRF1 as a stable member of one enormous complex.

PMID:19549727 is the most mechanistically relevant interaction source because it reports an LONRF1–UBE2L6 Y2H edge in a human E2/E3-RING network [PMID:19549727, “In this study, yeast two-hybrid (Y2H) screens were combined with true homology modeling methods to generate a high-density map of human E2/E3-RING interactions.”]. The exact pair is not shown to belong to the paper's functionally validated subset, so it supports `ubiquitin conjugating enzyme binding` and an E3 hypothesis, not demonstrated ubiquitin transfer.

No primary study located in the audit directly demonstrates LONRF1 autoubiquitination, substrate ubiquitination, or a physiological substrate. The only LONRF1-focused paper is a mouse expression/transcriptomics study and explicitly leaves its physiological function unresolved [PMID:36888978, “However, the physiological implications of other LONRF isozymes remain unclear.”]. Direct LONRF2 protein-quality-control evidence and fission-yeast Pqr1 phosphate-regulation evidence are family context only; neither paralog's substrates or processes should be transferred to LONRF1.

The review should distinguish three questions:

1. Does LONRF1 physically engage one or more E2 ubiquitin-conjugating enzymes in a way that supports a specific `ubiquitin-conjugating enzyme binding` or catalytic E3 mechanism?
2. Are any screen partners validated endogenous substrates, adaptors, or localization determinants?
3. Is there direct evidence for LONRF1-dependent ubiquitination, ubiquitin-chain architecture, or substrate fate?

Until those are answered, the interaction rows should not substitute for a demonstrated core reaction or stable complex.

## Open experimental priorities

- Reconstitute full-length LONRF1 and RING-disrupting variants with a panel of human E2 enzymes, measuring E2~Ub discharge, autoubiquitination, substrate ubiquitination, and chain linkage.
- Identify endogenous, LONRF1-dependent ubiquitination targets using acute knockout/degradation plus diGly proteomics and quantitative proteome turnover, followed by direct biochemical validation.
- Determine endogenous localization and membrane/cytosol partitioning with knock-in tags rather than inferring location from generic Reactome pathway membership.
- Test canonical and isoform-2 products separately; the 452–462 deletion lies upstream of the annotated second RING region and could alter local structure or regulation without proving isoform-specific function.
- Resolve whether the LON-family domain has a noncatalytic substrate-recognition role and explicitly test for the absence or presence of any peptidase activity rather than transferring Lon-protease biology by name.
