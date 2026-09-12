# TIAL1 review notes

## Scope and provenance

- Reviewed human TIAL1 (UniProt Q01085; historical protein name TIAR) against all 35 grouped GOA annotations fetched on 2026-07-18.
- Reviewed the current UniProtKB/Swiss-Prot record, cached primary papers, the local Reactome record, and current GO term labels.
- The configured Falcon deep-research attempt failed with HTTP 402 and the Perplexity-lite fallback failed with HTTP 401. No provider-named deep-research file was created; the manual synthesis is in `TIAL1-deep-research-manual.md`.

## Protein architecture and isoforms

TIAL1 is a 375-aa RNA-binding protein with three N-terminal RNA recognition motifs (RRM1, RRM2, and RRM3) and a glutamine-rich, low-complexity C terminus. UniProt lists two isoforms; isoform 2 inserts 18 residues at canonical position 43 within RRM1. The primary biochemical study found RRM2 necessary and sufficient for specific recognition of uridylate-rich RNA, with RRM1 and RRM3 increasing affinity or supporting other RNA contacts [PMID:8576255 "it is the second RNA binding domain (RRM 2) which mediates the specific binding to uridylate-rich RNAs"].

## Core RNA activities

### Uridine-rich RNA recognition and alternative splicing

TIAR/TIAL1 binds uridine-rich RNA. It regulates alternative pre-mRNA splicing by promoting weak 5-prime splice sites followed by U-rich intronic enhancers [PMID:17135269 "TIA-1 (T-cell intracellular antigen 1) and TIAR (TIA-1-related) proteins regulate alternative pre-mRNA splicing by promoting the use of suboptimal 5' splice sites followed by uridine-rich intronic enhancer sequences"]. Depletion in human cells changes the ratio of TIA1 isoforms, providing direct evidence for an endogenous splicing-regulatory role [PMID:17488725 "TIAR depletion from HeLa and mouse embryonic fibroblasts results in an increased ratio of TIA-1b/a expression"]. Reactome also places TIAL1 among factors contributing to epithelial FGFR2 IIIb splicing, although it notes that its precise role there remains unresolved.

### 3-prime-UTR binding and translational repression

TIAR binds AU-rich 3-prime UTR elements. The TNF study directly identified TIAR in the cytosolic complex bound to the TNF-alpha AU-rich element [PMID:9890998 "Here, we report the identification of the RNA-binding protein TIAR as a protein involved in complex 1"]. Direct human-cell experiments showed that TIAR binds the GADD45A 3-prime UTR and inhibits translation [PMID:16600875 "TIAR potently inhibited GADD45alpha translation"]. A broader target study found binding to the 3-prime UTRs of translation-factor mRNAs and strong repression, with TIAR knockdown relieving global UVC-induced translation inhibition [PMID:16537914 "The UVC-imposed global inhibition of the cellular translation machinery was significantly relieved after silencing of TIAR expression"]. This supports a new negative-regulation-of-translation annotation.

### Stress granules

At steady state TIAL1 is concentrated in the nucleus, but stress causes nuclear-to-cytoplasmic redistribution and colocalization with untranslated poly(A)-positive RNA in stress granules [PMID:10613902 "In response to environmental stress, the related RNA-binding proteins TIA-1 and TIAR colocalize with poly(A)(+) RNA at cytoplasmic foci that resemble the stress granules"]. The study directly supports stress-granule localization and a role in routing untranslated mRNPs, but its dominant-negative perturbation targeted TIA1 while secondarily trapping endogenous TIAR. Therefore stress-granule assembly is retained as a core biological role in synthesis, while the review avoids overstating a TIAL1-specific single-gene requirement.

### Protein-RNA adaptor activity and Hippo/miRNA regulation

The Drosophila Rox8 study showed direct yki 3-prime-UTR binding and recruitment/stabilization of miR-8-loaded RISC. Importantly for the human product, human TIAR promoted yki mRNA degradation in flies and destabilized YAP mRNA in human cells [PMID:33203680 "TIAR, the human ortholog of Rox8, is able to promote the degradation of yki mRNA when introduced into Drosophila and destabilizes YAP mRNA in human cells"]. The experimental human annotations for protein-RNA adaptor activity, 3-prime-UTR binding, Hippo activation, miRNA silencing, and reduced proliferation are retained, but the downstream pathway and proliferation terms are non-core context-specific consequences.

## DNA binding and transcriptional regulation

DNA binding is not merely a domain prediction. Recombinant TIAR bound T-rich single-stranded DNA with higher apparent affinity than the matched RNA and could be displaced by active transcription [PMID:16091628 "TIAR had a nearly 6-fold greater affinity for DNA than RNA"]. An older alternatively spliced T-cluster-binding product from the same locus bound the PF4 promoter and reduced reporter expression [PMID:9207209 "Co-transfection experiments showed that TCBP reduced the gene expression from the PF4 promoter"]. DNA binding and transcriptional regulation are therefore retained as experimentally supported but non-core functions; the older TCBP product is not among the two current UniProt isoforms.

## Cytolytic-granule, lysosome, defense, and apoptosis boundary

The founding paper identified a lysosome-targeting motif, inferred cytotoxic-granule association, and found that purified recombinant TIAR induced DNA fragmentation in permeabilized target cells [PMID:1326761 "Like TIA-1, purified recombinant TIAR induced DNA fragmentation in permeabilized target cells"]. This supports cytolytic-granule localization as a historical, context-specific observation. Generic lysosome is modified to the more specific cytolytic granule. Defense response and apoptotic process are marked over-annotated because the permeabilized-cell assay and candidate-effector interpretation do not establish a normal, broad physiological role for TIAL1 in either process.

## Protein interaction annotations

The three generic protein-binding annotations derive from large-scale DZIP3/MOV10 interaction datasets. The physical associations may be real, but GO protein binding is not informative and does not identify a molecular activity. All three are marked over-annotated; no replacement term is proposed without a demonstrated mechanism for each interaction.

## Existing annotation decisions

| Group | Decision | Rationale |
|---|---|---|
| AU-rich 3-prime-UTR binding IBA | ACCEPT | Direct TNF, GADD45A, and target-mRNA evidence |
| protein-RNA adaptor IBA/IDA | ACCEPT | Phylogenetic support plus Rox8/TIAR-RISC mechanism |
| alternative splicing regulation IBA | ACCEPT | Direct human depletion and splice-site studies |
| nucleic acid binding IEA | MODIFY | Replace with RNA binding; generic parent is uninformative |
| DNA binding IEA | KEEP_AS_NON_CORE | Direct biochemical DNA binding, secondary to RNA roles |
| RNA binding and 3-prime-UTR binding | ACCEPT | Multiple direct and high-throughput studies |
| nucleus/nucleoplasm and cytoplasm/cytosol | ACCEPT | Direct localization and shuttling evidence |
| cytoplasmic stress granule | ACCEPT | Direct stress-dependent localization |
| regulation of proliferation IEA | MODIFY | More specific negative regulation is already experimentally supported |
| cytolytic granule | KEEP_AS_NON_CORE | Historical direct/candidate granule evidence |
| three protein binding records | MARK_AS_OVER_ANNOTATED | Generic term from interaction screens |
| negative proliferation, Hippo, miRNA silencing | KEEP_AS_NON_CORE | Supported but pathway/context-specific |
| defense response | MARK_AS_OVER_ANNOTATED | Candidate CTL effector inference is too broad |
| lysosome | MODIFY | Cytolytic granule is the supported LRO compartment |
| Pol II transcription regulation | KEEP_AS_NON_CORE | Direct reporter evidence for older TCBP product |
| apoptotic process | MARK_AS_OVER_ANNOTATED | Permeabilized-cell DNA fragmentation is insufficient for broad process assignment |

## Proposed new annotation

- GO:0017148 negative regulation of translation, supported by direct TIAR target binding, reporter/translation measurements, and relief after TIAL1 silencing in human cells [PMID:16537914 "TIAR bound the 3'-untranslated regions of these mRNAs and potently suppressed their translation"]

## Open issues

- Determine whether the RRM1 insertion in isoform 2 alters DNA recognition, RNA target choice, nucleocytoplasmic shuttling, or condensation.
- Test whether the old TCBP transcript/protein is still produced from the human TIAL1 locus and how it relates to current transcript models.
- Resolve the TIAL1-specific contribution to stress-granule assembly separately from the partly redundant TIA1 and G3BP proteins.
- Reassess endogenous cytolytic-granule localization and physiological CTL effector function with modern isoform-specific reagents.

