# BACSU proB: comparative module audit

2026-11-07 UTC. The reference sequence is strain 168; the 2011 pathway genetics used JH642 derivatives. Their pathway architecture is comparative support, not a purified-enzyme or localization assay on this exact strain-168 sequence.

ProB supplies the kinase step of the anabolic branch; the separate ProJ paralog supplies the osmotically induced branch.

Curated HAMAP statements are the target-specific computational support. Primary publications are distinguished from exact-strain assays. All source annotation payloads and order are preserved, with no NEW rows. Broad true terms refine to supported descendants; nucleotide binding is part of catalysis. RNA binding, where present, remains UNDECIDED pending target evidence.

The Falcon research attempt failed; no provider report is represented as successful. Manual literature research is recorded here and in the review references.

- PMID:25367752: Comparative review; cached abstract read and publisher full text accessible. Supports pathway conservation and alternative routes; older channeling interpretations must be checked against PMID:39514317.
- PMID:21784929: Full primary text read. JH642-derivative genetics separates ProB/ProJ branches and shared ProA; reference target is strain168. Feedback resistance of ProJ is argued physiologically rather than measured here.
- PMID:8083159: Cached abstract read; UniProt identifies strain168 and records sequence conflicts in the original sequence. Gene organization supports pathway context. Multicopy protease phenotypes do not establish a direct protease regulatory activity of ProB.
- PMID:37511294: Full primary text read. ASKA K12 ProB was recloned into pET21a and assayed by SELEX/EMSA. This is positive Ecoli binding evidence, not an assay on the present target; binding site and physiological regulatory effect remain unresolved.

## Independent annotation-reviewer consultation (2026-11-07 UTC)

Catalytic and pathway decisions are retained. Nucleotide binding is integral to the curated reaction: ATP donates phosphate in ProB/ProJ, while NADPH supplies reducing equivalents to ProA. These are mechanistic/HAMAP inferences, not measurements of target affinity or stoichiometry. The ATP rows now quote both the target reaction and a HAMAP ATP-contact feature. Cytosol is inferred from the cytoplasmic family assignment and soluble enzyme architecture; another annotation row is not independent support. RNA binding remains UNDECIDED: E. coli ProB is a positive biochemical comparator, not evidence that every homolog binds RNA or that the PUA domain mediates it.

PMID:25367752 publisher full text was independently accessible at https://onlinelibrary.wiley.com/doi/10.1111/brv.12146; the local cache remains abstract-only, and no publication file was rewritten. Its stale full_text_unavailable flag was removed. The findings now state biology with source quotations rather than repeat the access notes.

Selected evidence anchors:
- [PMID:21784929] In JH642-derived B. subtilis, the proHJ branch responds transcriptionally to osmotic stress, whereas the anabolic proBA branch does not; this supports distinct physiological roles for ProJ and ProB. Source: "Northern blot analysis demonstrated that the transcription of the proHJ operon is osmotically inducible, whereas that of the proBA operon is not."
- [PMID:8083159] The B. subtilis proB and proA genes are adjacent and encode successive reactions in the glutamate route. The multicopy protease phenotype does not itself establish direct regulation of proteases by either enzyme. Source: "The proB gene encoding gamma-glutamyl kinase was followed by the proA gene encoding glutamyl-gamma-semialdehyde dehydrogenase at an interval of 39 nucleotides, suggesting that the genes constitute an operon."
- [PMID:37511294] E. coli ProB enriches RNA sequences by SELEX and binds one tested RNA specifically in EMSA, but the interaction is weak and its binding site and physiological effect remain unresolved. This does not demonstrate RNA binding by the present target. Source: "SELEX with glutamate-5-Kinase (ProB) revealed a small number of highly amplified RNA fragments. Representative EMSA experiments with one of those sequences confirmed the specific binding."

No NEW rows, subtype-specific physiological annotations, target RNA activity, stable ProA-ProB complex or demonstrated substrate channeling were added. The five original Falcon attempts failed and remain documented in the original logs.

PAINT check: `just paint-losses BACSU proB` reported no IRD or IKR loss on this target lineage. The retained IBA therefore does not contradict a cached PAINT loss.
