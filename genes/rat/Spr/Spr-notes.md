# Spr notes

- UniProtKB:P18297 states: FUNCTION: Catalyzes the final one or two reductions in tetrahydrobiopterin biosynthesis to form 5,6,7,8-tetrahydrobiopterin. [UniProtKB:P18297].
- Core interpretation: NADP-dependent sepiapterin reduction in tetrahydrobiopterin biosynthesis.
- Accepted direct GO terms include: pteridine metabolic process, sepiapterin reductase (NADP+) activity, tetrahydrobiopterin biosynthetic process, tetrahydrobiopterin metabolic process.
- Non-core/context terms are mostly localization, binding/cofactor, inferred pathway context, or exposure-response annotations; generic parent terms are modified when a specific catalytic term is available.

## Re-review 2026-10-10

GOA refresh changes:
- 4 new rows seeded: GO:0004757 sepiapterin reductase (NADP+) activity ISO and GO:0005829 cytosol ISO, both now also sourced from human SPR (UniProtKB:P35270) as donor-split duplicates of the existing mouse-sourced rows; GO:0046146 tetrahydrobiopterin metabolic process ISO (mouse Spr, involved_in); GO:0141151 negative regulation of nitric oxide-cGMP mediated signal transduction ISO (mouse Spr, source IMP PMID:19429835).
- 1 row retired: GO:0006558 L-phenylalanine metabolic process ISO (kept as KEEP_AS_NON_CORE, flagged as no longer in GOA).

Decisions:
- P35270 donor-split rows: ACCEPT (MF) and KEEP_AS_NON_CORE (cytosol), consistent with the mouse-sourced siblings.
- GO:0046146 (involved_in): ACCEPT; Spr catalyzes BH4-forming reductions.
- GO:0141151: REMOVE. The source paper shows the opposite sign [PMID:19429835 "In cells transiently transfected with SPR gene, SPR activity (HPLC) was dramatically increased by 19-fold, corresponding to a significant increase in endothelial H(4)B content (HPLC) and NO(*) production (electron spin resonance)."] and SPR knockdown lowered BH4 and NO. No cGMP readout; the effect is indirect cofactor supply to NOS. Recorded as SOURCE_BAD / REGULATORY_SIGN_INVERSION on the mouse donor.
- GO:0008284 positive regulation of cell population proliferation (IMP, PMID:12604243): kept MARK_AS_OVER_ANNOTATED with a sharper reason: the cell-number effect was seen only under phenylpropanedione challenge and attributed to carbonyl detoxification [PMID:12604243 "Thus, the SDR activity of SPR in PC12 cells may serve for detoxification of exogenous carbonyl compounds besides functioning as a specific enzyme for the formation of tetrahydrobiopterin."].
- All 20 UniProt quotes were stale (the refreshed FUNCTION line hyphen-breaks "tetra-hydrobiopterin"); replaced with the CATALYTIC ACTIVITY reaction, SUBCELLULAR LOCATION: Cytoplasm., or SUBUNIT: Homodimer. as appropriate.
- Description rewritten to remove review commentary.

Open questions:
- Should the mouse Spr IMP to GO:0141151 (PMID:19429835) be reported to MGI as a sign error? The paper supports a positive effect on NO bioavailability.
