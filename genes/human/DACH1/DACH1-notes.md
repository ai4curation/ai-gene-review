# DACH1 notes

Automated deep research was unavailable for this review (falcon 402, OpenAI 401); notes compiled manually from cached publications and UniProt (Q9UI36).

## Corepressor role (primary)
- NCoR and SMAD4: [PMID:14525983 "DACH1 bound to endogenous NCoR and Smad4 in cultured cells and DACH1 co-localized with NCoR in nuclear dotlike structures."]; [PMID:14525983 "DACH1 participates in the negative regulation of TGF-beta signaling by interacting with NCoR and Smad4."]
- Cyclin D1 via c-Jun: [PMID:16980615 "DACH1 repressed cyclin D1 through a novel mechanism via a c-Jun DNA-binding partner, requiring the DACH1 alpha-helical DS domain which recruits corepressors to the local chromatin."]
- Mouse Six6-Dach: [PMID:12130660 "Six6, in association with Dach corepressors, regulates proliferation by directly repressing cyclin-dependent kinase inhibitors, including the p27Kip1 promoter."]
- Six1-Dach-Eya switch: [PMID:14628042 "The phosphatase function of Eya switches the function of Six1-Dach from repression to activation, causing transcriptional activation through recruitment of co-activators."]; Eya-Dach synergy via CBP [PMID:12215533].

## DNA binding (secondary; evaluated carefully)
- Structure: [PMID:12057194 "The protein forms an alpha/beta structure containing a DNA binding motif similar to that found in the winged helix/forkhead subgroup of the helix-turn-helix family."]
- Biochemistry: [PMID:12215533 "Dach binds to chromatin DNA by itself, not being tethered by GAL4-Eya3. Dach also binds to naked DNA with lower affinity. The conserved DD1 domain is responsible for binding to DNA."]
- Reporter/ChIP: [PMID:20956529 "Thus, DACH1 represses gene transcription through direct DNA binding to the promoter region of target genes by recruiting the transcriptional co-regulator, TCERG1."]
- Assessment: direct DNA binding is supported by three independent lines (structure, in vitro binding, DRE reporters + ChIP-seq), and the curators' IDA rows were made from full text, so DNA-binding TF annotations are accepted. However, naked-DNA affinity is reported as low and no high-resolution intrinsic motif exists; DACH1 ChIP peaks co-localize with FOX motifs, so some "sequence-specific" binding may reflect partner tethering. The corepressor function is therefore listed as the first core function, and DNA-binding repression as a second, more weakly characterised mode.

## Tumor suppression
- Glioma FGF2 repression [PMID:21750150]; breast cancer DNA synthesis/cyclin D1 [PMID:16980615]. Downstream proliferation/migration terms kept as non-core.

## Module
Module annoton GO:0003712 (transcription coregulator activity) is consistent; this review's core MF is the more specific child GO:0003714 transcription corepressor activity (NEW), plus GO:0001227.
