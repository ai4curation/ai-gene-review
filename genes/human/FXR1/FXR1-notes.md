# FXR1 curation notes

## Evidence synthesis

- `just fetch-gene human FXR1` returned 142 GOA rows; the GOA file is not header-only.
- Human FXR1 has direct evidence for core RNA and mRNA regulation. PMID:17382880 shows FXR1 and AGO2 associate with AREs during translation activation and are required for ARE-mediated reporter activation. PMID:30067974 shows human VSMC FXR1 binds ARE-containing TNF 3' UTR probes and destabilizes inflammatory transcripts. PMID:34731628 shows FXR1 binds the cMYC 3' UTR and promotes cMYC translation by recruiting eIF4F.
- FXR1 has two strong mRNP-assembly branches beyond ordinary mRNA regulation. PMID:39106863 shows long mRNAs and FXR1 form a cytoplasmic mRNP network that scaffolds RhoA-pathway proteins for actomyosin remodeling. PMID:32706158 shows FXR1 at the nuclear envelope and loss of FXR1 causing cytoplasmic nucleoporin condensates.
- Developmental rows are contextual. PMID:35951695 supports late spermatid translational activation by mouse Fxr1; the UniProt curated FUNCTION lines summarize FXR1's skeletal-muscle requirement and cite PMID:30770808 for the human congenital multi-minicore myopathy mutations.
- The nucleolar row is isoform-specific: PMID:10888599 maps a nucleolar-targeting sequence present in some FXR1 isoforms and in FXR2, while other FXR1 isoforms are nucleoplasmic after nuclear-export inhibition.
- Bare `GO:0005515` protein-binding rows were removed under `src/ai_gene_review/validation/protein_binding_policy.py`; that removes only the uninformative GO term and does not dispute the underlying high-throughput interaction records.

## PAINT and GO-CAMs

- PTHR10603 family-root PAINT rows for mRNA 3'-UTR binding, translation regulator activity, positive regulation of translation and regulation of mRNA stability match the shared FMR/FXR RNA-binding biology.
- The Bilateria node rows for positive long-term neuronal synaptic plasticity and presynaptic translation are each seeded by rat Fmr1 in the local PAINT slice. A single curated seed is not weak by count, so FXR1 keeps these rows as non-core inherited neuronal contexts rather than as direct core functions.
- The `GO_REF:0000108` `GO:0098793 presynapse` row is a logical cellular-component assertion derived from `GO:0099577 regulation of translation at presynapse, modulating synaptic transmission`. Keep `GO:0098793` with the same non-core status as the PAINT presynaptic-translation row.
- The production GO-CAM index already links FXR1 to `63894f2500000826`, `63894f2500000870`, and `66b5638000000353`. They cover FXR1/cMYC translation, late spermatid translation, and nuclear-pore localization as process-specific models; there was no reusable multi-part module to add in this content PR.
