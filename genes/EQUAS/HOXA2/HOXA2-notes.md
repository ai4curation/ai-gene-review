# HOXA2 (donkey, A0A9L0JBM7) notes

## Sources
- Donkey UniProt A0A9L0JBM7 (unreviewed; function text and location are ARBA/PROSITE predictions).
- Human HOXA2 O43364 and mouse Hoxa2 P31245 UniProt records fetched into HOXA2-bioinformatics/ (O43364-uniprot.txt, P31245-uniprot.txt).
- Experimental GO annotations of human/mouse orthologs from QuickGO: HOXA2-bioinformatics/ortholog_experimental_goa.txt.
- No HOXA2 review exists for human or mouse in this repository; the key primary papers (e.g. PMID:15634706, PMID:25889273) are not in the local publication cache, so ortholog evidence is taken from the GOA records rather than full text.

## Biology
- Human/mouse HOXA2: [file:EQUAS/HOXA2/HOXA2-bioinformatics/O43364-uniprot.txt "Sequence-specific transcription factor which is part of a"] developmental regulatory system providing positional identity on the anterior-posterior axis; nuclear.
- Mouse Hoxa2 is a sequence-specific DNA-binding transcriptional repressor of RNA polymerase II targets [file:EQUAS/HOXA2/HOXA2-bioinformatics/ortholog_experimental_goa.txt "P31245 Hoxa2 enables GO:0001227 \"DNA-binding transcription repressor activity, RNA polymerase II-specific\" IDA PMID:15634706"], and also has IDA support for positive regulation of RNA Pol II transcription (PMID:18787068).
- Mouse Hoxa2 developmental roles: second pharyngeal arch identity, middle ear and skeletal morphogenesis, hindbrain rhombomere 2/3 development (IMP/IGI/IDA rows in ortholog_experimental_goa.txt).
- Human disease: microtia, hearing impairment and cleft palate (MHICP) [O43364-uniprot.txt].

## Donkey sequence
- 97.6% identity; homeodomain 60/60 identical; hexapeptide identical [file:EQUAS/HOXA2/HOXA2-bioinformatics/RESULTS.md].

## Decisions
- Core: DNA-binding TF activity, RNA Pol II-specific (ACCEPT), repressor activity (ACCEPT), cis-regulatory region sequence-specific DNA binding (ACCEPT), nucleus (ACCEPT), regulation of transcription by RNA Pol II (TreeGrafter, ACCEPT), negative regulation of transcription by RNA Pol II (ACCEPT).
- Generic DNA binding, DNA-binding TF activity, regulation of DNA-templated transcription: TOO_GENERAL (entailed by the accepted specific terms).
- Developmental processes: pharyngeal system development and embryonic skeletal system development ACCEPT; muscle structure development KEEP_AS_NON_CORE.

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

ProtNLM2 output was not consulted.

### Identity
- A0A9L0JBM7 is the full-length canonical donkey HOXA2 product: 373 aa vs 376 aa for human O43364. It has a 3-residue deletion relative to human 116-118 and the same C-terminus. The homeodomain (human 143-202) is 60/60 identical and the hexapeptide (human 94-99) is identical [file:EQUAS/HOXA2/HOXA2-bioinformatics/RESULTS.md "human region 143-202: 60 of 60 residues aligned, 60 identical"]. It is not a fragment, isoform or alternative gene model.
- PANTHER: donkey (UniProt DR line), human O43364 and mouse P31245 all sit in PTHR45664:SF3 "HOMEOBOX PROTEIN HOX-A2" (interpro/panther/PTHR45664/PTHR45664-entries.csv). Transfers from mouse and human Hoxa2 therefore stay within the same subfamily. The TreeGrafter rows come from node PTN000674557. No family review YAML exists for PTHR45664, only entries/metadata, so there is no subfamily disagreement.

### Deep research
- `just deep-research-falcon EQUAS HOXA2 --fallback perplexity-lite` failed. Edison auth returned `403 Forbidden` at /auth/login, and the perplexity-lite fallback produced no file. I went ahead with the cached primary literature.

### Evidence changes
- Cached the primary mouse papers behind the Ensembl Compara and combined IEA transfers: PMID:15634706, PMID:18787068, PMID:16221728, PMID:25889273, PMID:10536059, PMID:7903600 and PMID:7903601 (all abstract-only).
- Swapped all support quotes taken from `ortholog_experimental_goa.txt` (a QuickGO listing of ortholog annotations) for quotes from these primary papers. A GOA listing says what is annotated, not why. That file stays in references, with a note that it is no longer used as support.
- Key evidence:
  - Six2 is a direct repressed target [PMID:15634706 "Hoxa2 regulation of Six2 is confined to a 0.9 kb fragment of the Six2 promoter and that Hoxa2 binds to this promoter region"].
  - Hox/Pbx and Meis sites activate the Krox20 element C enhancer [PMID:18787068 "Krox20 is under the direct transcriptional control of both Meis (presumably Meis2) and Hox/Pbx factors in r3"].
  - Hoxa2 acts as a selector gene in the second arch [PMID:7903601 "Hoxa-2 acts as a selector gene in the second arch"] and is required in the neural crest [PMID:16221728 "Hoxa2 is selectively required in cranial neural crest cells (NCCs)"].
- PMID:7508007 is attached to a mouse rhombomere 2/3 IMP/IGI row in the ortholog listing. Its cached title ("Molecular phenotype of simian virus 40 large T antigen-induced primitive neuroectodermal ...") does not look like a Hoxa2 rhombomere paper. This is a possible mis-keyed reference on the mouse side. I did not verify it further, and it does not affect any donkey row.

### Action changes vs previous review
- GO:0043565 sequence-specific DNA binding: ACCEPT -> TOO_GENERAL. It is an ancestor of the accepted GO:0000978 (OLS hierarchicalAncestors), so the earlier "conveys specificity" reasoning does not hold.
- GO:1990837 sequence-specific double-stranded DNA binding: ACCEPT -> TOO_GENERAL. It is also an ancestor of GO:0000978.
- GO:0061061 muscle structure development: KEEP_AS_NON_CORE -> MARK_AS_OVER_ANNOTATED.
  - The source study (PMID:25889273) is a neural crest overexpression study whose abstract is about skeletal transformation.
  - Arch muscle is mesoderm-derived, so any Hoxa2 effect on it is non-cell-autonomous and downstream of crest activity.
  - Not removed, because the mouse curator had the full text.
- All other actions kept. Core function: RNA Pol II-specific TF activity (repressor and activator) in the nucleus, in pharyngeal (second-arch) and embryonic skeletal development.

### Relative
- Closest experimentally characterised relative in the same subfamily (PTHR45664:SF3) is mouse Hoxa2 (P31245), the donor of almost all experimental evidence. The repo has no review of it (no genes/mouse/Hoxa2) and none for human HOXA2 (O43364). The horse partner genes/HORSE/HOXA2 is reviewed separately in this campaign.

### Modules
- modules/neural_crest_gene_regulatory_network.yaml covers cranial neural crest regulation. HOXA2 is mentioned only in its deep-research file and is not a module part.
