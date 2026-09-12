# EIF3G review notes

## Scope and research provenance

- Reviewed human EIF3G (UniProt O75821), its reviewed UniProt record, all 61 seeded GOA annotation groups (68 source GOA rows), and all PMID-backed evidence cached for those annotations.
- The required Falcon deep-research request failed with HTTP 402, and the Perplexity-lite fallback failed with HTTP 401 (quota). No provider-named file was created. Manual synthesis is recorded in EIF3G-deep-research-manual.md.

## Protein identity and architecture

- EIF3G is a 320-aa subunit of the 13-subunit eukaryotic translation initiation factor 3 (eIF3) complex. It belongs to the conserved eIF3b/eIF3g/eIF3i-containing module and has a C-terminal RNA-recognition motif (RRM; residues 239-317 in UniProt).
- The original human cloning study directly placed p44/EIF3G in eIF3, mapped its interaction with eIF3A/p170, and showed RNA binding: [PMID:9822659, "Northwestern blotting shows that eIF3-p44 binds 18 S rRNA and beta-globin mRNA."]
- An independent cloning study purified recombinant p42/EIF3G and confirmed RNA binding: [PMID:9973622, "The purified protein binds RNA in agreement with the presence of a putative RNA binding motif in the deduced amino acid sequence."]

## Core eIF3 role, with an important boundary

- EIF3G is an established structural subunit of eIF3. Native-complex mass spectrometry places it in the stable eIF3(a:b:i:g) module and next to the decoding center: [PMID:18599441, "Dissociation takes place as a function of ionic strength to form three stable modules eIF3(c:d:e:l:k), eIF3(f:h:m), and eIF3(a:b:i:g)."]
- EIF3G is not part of the minimal mammalian basal-activity core in the reconstitution assay. Deleting EIF3G also removes EIF3I from the recombinant complex, yet did not prevent 40S recruitment to beta-globin mRNA or alter bulk protein synthesis after EIF3G knockdown: [PMID:17581632, "Furthermore, the rate of overall protein synthesis does not change by knockdown of the eIF3g subunit in HeLa cells"] and [PMID:17581632, "Thus, these two subunits might be involved in translational control of specific mRNAs or in particular cellular conditions."]
- Consequently, general translation-initiation annotations are biologically valid at the holo-eIF3 level, but the most defensible EIF3G-specific molecular activity is RNA/mRNA binding rather than an independently enabled catalytic activity.

## Direct mRNA engagement and transcript-selective translation

- PAR-CLIP of endogenous human eIF3 identified EIF3G as one of four subunits that directly crosslink RNA and mapped EIF3G contacts to 352 transcripts: [PMID:25849773, "After RNase digestion, separation of crosslinked eIF3–RNA complexes by denaturing gel electrophoresis demonstrated that four of the thirteen subunits crosslink directly to RNA"] and [PMID:25849773, "eIF3a, b, d, and g crosslinking to 328, 264, 356, and 352 transcripts, respectively"]
- eIF3-binding sites were enriched in 5-prime UTRs and the eIF3 complex could activate c-JUN translation while repressing BTG1 translation. These regulatory outcomes are established for the complex; the study does not isolate which outcome requires EIF3G specifically.
- A follow-up study directly observed EIF3G protection/crosslinking to the internal c-JUN 5-prime-UTR RNA element, whereas EIF3D alone contacted the cap: [PMID:27462815, "the four eIF3 RNA-binding subunits, eIF3a, b, d, and g, provide RNase protection to internally 32P-labeled c-Jun 5' UTR RNA upon UV254-induced crosslinking"]
- These data justify a new, more informative mRNA binding annotation (GO:0003729). The older in-vitro 18S-rRNA binding result is noted but not promoted to a new rRNA-binding annotation because PAR-CLIP did not detect rRNA crosslinking and modern structural work places eIF3 mainly on the protein-rich face of the 40S subunit.

## Context-specific interactions

- AIFM1 directly binds the EIF3G N-terminus and suppresses translation during apoptotic signaling; excess EIF3G competitively reduces this inhibition: [PMID:17094969, "The direct interaction between AIF and eIF3g was confirmed in a GST pull-down assay and also verified by the results of co-immunoprecipitation and confocal microscopy studies."] This is a meaningful stress-context interaction, but generic GO protein binding remains uninformative.
- SLIP1/MIF4GD binds an EIF3G motif and may bridge histone-mRNA translation machinery: [PMID:23804756, "We confirmed the binding of SLIP1 to DBP5 and eIF3g by pull-down assays"]
- Paip1 connects to eIF3 through EIF3G in an amino-acid/mTOR/S6K-regulated interaction that stimulates translation: [PMID:24396066, "the interaction of PABP-interacting protein 1 (Paip1) with PABP and eukaryotic translation initiation factor 3 (eIF3; via the eIF3g subunit) further stimulates translation."]
- PELO, DDX3X, DHX33, and multiple high-throughput interactome studies report additional associations. They may be real, but GO:0005515 protein binding does not state the functional relation; all such annotations are marked over-annotated rather than removed.

## Viral termination-reinitiation

- Purified eIF3 stimulates influenza B BM2 termination-reinitiation [PMID:21347434, "exogenous eIF3 specifically stimulated synthesis of the BM2fluc reinitiation product with all of the mRNAs tested"]. The experiment tested the holo-complex, not an EIF3G-depleted complex, so the existing EIF3G annotation is retained as non-core microbial-infection context rather than treated as an EIF3G-specific core function.

## Localization and negation

- Cytoplasm/cytosol is the primary site of function. PMID:12426392 reported broad nuclear exclusion of translation factors, including eIF3, in the tested baseline context.
- UniProt also records nucleus/perinuclear localization from the AIFM1 study. The older NOT-nucleus annotation is therefore interpreted as context-dependent rather than a universal negation; it is retained as non-core with this qualification.

## Annotation decision summary

- ACCEPT: eIF3 complex membership, translational initiation/initiation-complex formation, RNA binding, cytoplasm/cytosol, and complex-level translation initiation factor activity (with contributes-to interpretation).
- MODIFY: broad nucleic acid binding to the more informative RNA binding term.
- KEEP_AS_NON_CORE: 43S/48S transient-complex membership, perinuclear localization, baseline NOT-nucleus observation, and viral termination-reinitiation.
- MARK_AS_OVER_ANNOTATED: all generic protein-binding annotations; the underlying interactions are preserved in their summaries.
- NEW: mRNA binding (GO:0003729), supported by direct biochemical and crosslinking evidence.

## Open issues

- Which EIF3G-contacted transcripts actually require EIF3G, rather than another RNA-binding eIF3 subunit, for translational activation or repression?
- Does the RRM recognize sequence/structure directly, and how do its targets differ from those of EIF3A, EIF3B, and EIF3D?
- Is the early in-vitro 18S-rRNA binding physiologically relevant, or an affinity of isolated EIF3G that is not used in assembled eIF3?
- How do phosphorylation and the EIF3G-EIF3I partnership tune target-selective initiation under stress or nutrient signaling?
