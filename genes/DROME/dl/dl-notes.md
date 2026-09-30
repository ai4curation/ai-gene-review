# dl (dorsal, P15330) review notes

Reviewed together with Dif (P98149) for the INNATE_IMMUNITY project (batch 1, Toll/TLR axis). Actions were kept consistent between the two paralogues.

## Biology (with provenance)

- Rel homology domain TF; DNA binding through the rel domain [PMID:1988156 "We present evidence that the DNA-binding activity of the dl protein is mediated by the region of homology (the rel domain) conserved in the rel and NF-kappa B proteins."]
- Morphogen: nuclear gradient specifies D/V fates [PMID:2598266 "My findings suggest that nuclear localization is critical for dorsal to function as a morphogen and that the distribution of the dorsal protein determines cell fate along the dorsal-ventral axis."]
- Activator of twist [PMID:1648449 "by transient cotransfection assays, we show that the dorsal protein specifically activates expression from the twist promoter."]
- Repressor at zen VRR via Groucho [PMID:9774673 "This complex includes Dorsal, Gro, and additional DNA binding proteins, which appear to convert Dorsal from an activator to a repressor by enabling it to recruit Gro to the template."]
- Cactus retains Dorsal in cytoplasm [PMID:9025065 "As in the case for I kappa B and NF-kappa B, Cactus inhibits Dorsal by retaining it in the cytoplasm."]
- Toll/Tube/Pelle relay releases Dorsal [PMID:9367441 "free Dorsal translocates into nuclei and directs expression of ventral fates."]
- Larval immunity, redundant with Dif [PMID:10369678 "This result suggests a functional redundancy between both Rel proteins in the control of drosomycin gene expression in the larvae of Drosophila."]
- Obligate dimers; all homo/heterodimer combinations with Dif and Relish form [PMID:20679214 "The results show that all combinations of homo- and heterodimers are formed, but with varying degrees of efficiency."]
- Hemocytes [PMID:17060622 "Specific expression of Dif or dorsal in the blood cell lineage is sufficient to restore blood cell number, clear microbes, and allow survival to the adult stage."]
- Dorsal B at NMJ, no nuclear translocation [PMID:26167685 "Dorsal B interacts with and stabilizes Cactus at the neuromuscular junction, but exhibits Cactus independent localization and an absence of detectable nuclear translocation."]
- The fly IKKbeta (ird5) is not needed for Cactus degradation in D/V patterning [PMID:11156609 "ird5/DmIkk β homozygous mutant females are fertile, demonstrating that this gene is not required for degradation of Cactus during dorsal-ventral patterning in the embryo."]

## Key curation decisions

1. **Toll signaling pathway (GO:0008063)**: all rows accepted. This is the correct Drosophila-specific pathway term. Neither dl nor Dif carries GO:0002224 (TLR signaling), and none should be added: Toll is activated by the cytokine Spaetzle, not by microbial patterns.
2. **Canonical NF-kappaB signal transduction (GO:0007249)**: kept as non-core. The definition requires IKK, but Cactus degradation downstream of Toll is ird5-independent (PMID:11156609). The cassette (IkB degradation followed by NF-kB release) is conserved; the IKK clause is not met. This is raised as a suggested question and not removed.
3. **Non-canonical NF-kappaB (GO:0038061) IBA**: removed. It is defined by NIK/IKKalpha-dependent p100 processing; Dorsal is a class II Rel protein released from Cactus. propagation_review points at PTN000652441.
4. **Protein binding**: the Dif/Rel rows become MODIFY to protein heterodimerization activity, and identical protein binding becomes protein homodimerization activity. The Cactus, Tube and Tamo rows are REMOVEd as uninformative (inhibitor/cargo interactions).
5. **GO:0140297 DNA-binding TF binding**: the partners are Groucho (FBgn0001139, a corepressor with no DNA-binding activity) and DSP1 (HMGB, a putative corepressor). Both become MODIFY to GO:0001222 transcription corepressor binding.
6. **NEW**: GO:0001227 DNA-binding transcription repressor activity, RNA pol II-specific and GO:0000122 negative regulation of transcription by RNA pol II. Dorsal's repression of zen/dpp via the VRR is textbook biology, it is Dorsal's own DNA-binding activity, and it is absent from GOA. The other NEW candidates did not pass the participation test and were not added.
7. **Rows citing papers whose cached abstract does not mention Dorsal** (PMID:9806924 Apterous/FMRFa, PMID:12748300 CtBP, PMID:12556495 dTRAP80/Dif): these are abstract-only, and the functions (DNA binding, nucleus) are well established, so they were ACCEPTed in deference to the curator, per CLAUDE.md.
8. NMJ, subsynaptic reticulum, hemocyte, PNS, melanization and immune-response rows are kept as non-core.
9. GO:0002225 (positive regulation of antimicrobial peptide production) is KEEP_AS_NON_CORE for dl, but ACCEPT for Dif. Dif alone is required in adults; Dorsal's role is larval and redundant [PMID:10843389 "DIF alone is required for the antifungal response in adults, but is redundant in larvae with Dorsal"].

## Deep research

Falcon deep research had been queued by a background job but had not finished by the time this review was written. The review is based on the UniProt record and the cached publications.
