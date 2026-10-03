# MAK (P20794) curation notes

## Deep research status
DR_STATUS_PLACEHOLDER

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
- Interpretation: partial agreement. HPA places MAK at the basal body (and sperm connecting piece) rather than at the ciliary tip; in photoreceptors MAK is in the connecting cilium/axoneme (mouse) or inner segment (human), and no study has shown MAK at the primary-cilium tip in cultured cells. I therefore argue against the module's ciliary tip location for MAK: core_functions use photoreceptor connecting cilium and axoneme, not ciliary tip. The length-control role itself is supported (GO:1902856, a descendant of the module's GO:1902017), but evidence is essentially photoreceptor-specific.
