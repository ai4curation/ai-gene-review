# MAK (P20794) curation notes

## Deep research status
`just deep-research-falcon human MAK` first failed (falcon timed out at 600 s; perplexity-lite fallback unavailable in this environment). Re-run with `--timeout 2400` succeeded: see MAK-deep-research-falcon.md.

## Summary of function
- RCK kinase; testis-enriched expression [PMID:2183027 "These results suggest that the mak gene plays an important role in spermatogenesis."] (expression-based inference only).
- Photoreceptor cilium length control in mouse [PMID:21148103 "Here we show that male germ cell-associated kinase (Mak) regulates retinal photoreceptor ciliary length and subcompartmentalization."; "Mak was localized both in the connecting cilia and outer-segment axonemes of photoreceptor cells."; "In the Mak -null retina, photoreceptors exhibit elongated cilia and progressive degeneration."]. IFT88/IFT57 accumulate in mutant axonemes; Mak phosphorylates RP1 N-terminus. Respiratory (motile) cilia length unaffected.
- Human RP: homozygous Alu insertion in exon 9 [PMID:21825139 "We used exome sequencing to identify a homozygous Alu insertion in exon 9 of male germ cell-associated kinase (MAK) as the cause of disease in an isolated individual with RP."]; human IHC: inner segments, cell bodies and axons, little distal to connecting cilium.
- Activation by TDY dual phosphorylation, autophosphorylation and CCRK [PMID:21986944 "We found that MAK kinase activity requires dual phosphorylation of the conserved TDY motif"]; prostate cancer cell observations: AR coactivator [PMID:16951154], CDH1 phosphorylation, spindle/centrosome/midbody localization [PMID:21986944].

## Key decisions
- Kinase activity rows ACCEPT; AR protein binding MODIFY -> nuclear androgen receptor binding (GO:0050681); CDK20 and FZR1 binding REMOVE.
- Transcription coactivator / positive regulation of transcription KEEP_AS_NON_CORE (cancer cell lines).
- Spermatogenesis NAS MARK_AS_OVER_ANNOTATED (expression-based).
- cilium assembly IBA KEEP_AS_NON_CORE (MAK restricts length, not required for assembly).
- NEW negative regulation of non-motile cilium assembly (GO:1902856), ISS from mouse Mak (PMID:21148103; mouse ortholog already carries IMP/IDA/IGI).

## HPA cilium atlas vs module role
- Module (stage 6 length control): RCK kinase restricting length at the ciliary tip (protein serine/threonine kinase activity; regulation of cilium assembly; ciliary tip).
- HPA v25: Basal body (Approved); main locations Basal body; Connecting piece; Cytosol; Nucleoplasm. GOA HPA rows: nucleoplasm, nucleolus.
- Interpretation: partial agreement. HPA places MAK at the basal body (and sperm connecting piece) in cultured cells, whereas the module assigns it to the ciliary tip. Mouse photoreceptor and cultured-cell data (Chaya et al. 2024, PMID:39293864) do place Mak at ciliary tips, so I keep ciliary tip in core_functions (as a NEW ISS location) together with the photoreceptor connecting cilium and axoneme. The HPA basal-body call may reflect a base pool or cell-type differences; human retina immunostaining placed MAK mainly in inner segments. The length-control role is supported (GO:1902856, a descendant of the module's GO:1902017), but the evidence is essentially photoreceptor-specific, and in non-retinal cells CILK1 is the better-supported length-control kinase.

## Additional points from deep research (falcon) and follow-up
- Chaya et al. 2024 (PMID:39293864, cached full text) show that mouse Mak localizes to ciliary tips and regulates IFT together with Ick [PMID:39293864 "Here, we identified that the ciliopathy kinase Mak is a ciliary tip-localized IFT regulator that cooperatively acts with the ciliopathy kinase Ick, an IFT regulator."]; Mak/Ick double loss abolishes photoreceptor axonemes, and Ccrk (CDK20) activates both. IFT components concentrate at connecting-cilium tips in Mak-/- retina.
- Added NEW ciliary tip (ISS) and ciliary tip in core_functions based on this paper.
