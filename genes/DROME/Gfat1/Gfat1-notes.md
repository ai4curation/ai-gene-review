# Gfat1-PF review notes

Native 434-residue PF is a C-terminal isoform, with intact SIS domains but no catalytic Cys2 and only 40/299 residues of the GATase domain. The complete glutamine-dependent enzyme assertion is removed; broad binding is retained by comparison with isolated human ligand-bound isomerase structures [PMID:19059404](https://pubmed.ncbi.nlm.nih.gov/19059404/). Biosynthetic-process rows stay UNDECIDED because noncatalytic contribution is possible but unverified. The exact function paragraph is reviewed separately with NPI and raw metadata preserved.

## Provider research assessment

The Falcon synthesis integrates fly zeppelin genetics, hexosamine-pathway biology and distinction from Gfat2. However, its catalytic summary and domain discussion concern the 694-residue gene product, not the exact 434-residue PF accession. The complete enzyme and developmental evidence therefore inform gene-level context but cannot restore the missing glutaminase domain and catalytic Cys2 in PF. The exact-isoform analysis governs the activity assessment.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

**Identity (re-checked).** A8Y5A1 is the FlyBase Gfat1-PF polypeptide (FBpp0112413; transcript Gfat1-RF FBtr0113690, NP_001015162), 434 aa. FlyBase lists nine annotated Gfat1 transcripts, with CDSs of 694 aa (PA Q7PLC7; PN), 685, 682, 673, 665, 643, 493 and 434 aa (PF). An independent Python check on the two UniProt flat files shows A8Y5A1 is an exact suffix of Q7PLC7 starting at Q7PLC7 position 261 (Met261). PF therefore lacks the GATase type-2 domain (Q7PLC7 2..300, with the Cys2 nucleophile; ACT_SITE 2 PRU00609) apart from residues 261-300, and keeps both SIS domains (Q7PLC7 372..512 and 543..684; A8Y5A1 112..252 and 283..424). Neither Q7PLC7 nor any fly Gfat1 entry is reviewed (Swiss-Prot); Q7PLC7 (Gfat1-PA) is the full-length canonical product. Existing analysis: file:DROME/Gfat1/Gfat1-bioinformatics/RESULTS.md (not modified).

**Gene-level literature (newly cached).**
- Graack et al. 2001 [PMID:11716769 "Expressing Dmel/GFAT1 in yeast we showed that Dmel/GFAT1 activity is controlled by UDP-N-acetylglucosamine and PKA in the yeast total protein extract system."]: the FlyBase IDA basis for GO:0004360 at the gene level, presumably from a full-length cDNA. Expression in "embryonic chitin-synthesizing tissues and in the corpus cells of salivary glands".
- Chen et al. 2020 [PMID:32615907 "Deletions for either enzyme were fully lethal"]: GlcN6P rescues gfat2-/- but "glucosamine-6-phosphate did not rescue gfat1-/- animals". FlyBase also has IMP for GO:0004360 and UDP-GlcNAc metabolic process, and IDA for cytoplasm/cytosol, from this paper. These are gene-level results and do not show what PF does.
- Falcon deep research (Jackson 2007 thesis; zep alleles; Gfat2 distinction) refers to the 694-aa product, not PF.

**Evolutionary placement.** UniProt places every fly Gfat1 entry (including A8Y5A1 and Q7PLC7) and fly Gfat2 (Q9VAW3) in PTHR10937:SF0. Per PTHR10937-entries.csv, SF0 also contains E. coli GlmS P17169, S. cerevisiae GFA1 P14742 and S. pombe gfa1 Q09740. Human GFPT1 Q06210 is in SF12 and GFPT2 O94808 in SF10. PAINT IBD for GO:0004360 is at PTN000101302, seeded by FB:FBgn0287209 (Gfat1), FB:FBgn0039580 (Gfat2), yeast, E. coli, human and rat. It describes the two-domain enzyme. PF descends from that node, but its sequence has lost the glutaminase module, so the activity is not transferred to this accession. Only family-wide isomerase-site sugar-phosphate binding is transferred (human isomerase-domain structures, PMID:19059404).

**Changes from the previous version.**
- Description rewritten to describe the gene first (full-length GFAT1 reaction and fly biology), then PF identity.
- GO:0004360 REMOVE kept; reason now notes that the activity belongs to the full-length products (gene-level IDA, PAINT seed) and that the removal applies only to this accession.
- GO:0030246 carbohydrate binding changed ACCEPT -> MODIFY to GO:0097367. The SIS-site ligands are sugar phosphates (carbohydrate derivatives); GO:0097367 is not a descendant of GO:0030246, so this is a lateral correction to a term the product already carries.
- GO:0097367 ACCEPT kept (core function). GO:0070095 fructose-6-phosphate binding (is_a GO:0097367, checked in OLS) was considered and not used: there is no PF-specific binding data, and the site binds substrate, product and a glucose 6-phosphate analogue.
- The four process rows stay UNDECIDED, each with a separate rationale. No NEW process terms: PF has not been shown to do any step of hexosamine synthesis.
- References added: PMID:11716769, PMID:32615907. reference_review added for all literature references. No references removed.
- Added suggested questions and experiments (PF protein existence, mixed dimers, non-GlcN6P role suggested by the gfat1 rescue failure).

**Family review note.** interpro/panther/PTHR10937/PTHR10937-review.yaml describes SF0 as containing "fly Gfat1-related proteins" and calls it "the fly-associated SF0". SF0 is in fact a broad subfamily that also contains E. coli GlmS, yeast GFA1, S. pombe gfa1 and fly Gfat2. Its GO:0004360 assessment (UNRESOLVED, depending on isoform completeness) agrees with this review. This is not edited here.

**Next relative.** Canonical product of the same gene: Q7PLC7 (Gfat1-PA, 694 aa); no review exists. Folder would be genes/DROME/Gfat1__Q7PLC7. The closest experimentally characterised relative in the same subfamily (SF0) is yeast GFA1, already reviewed (genes/yeast/GFA1, COMPLETE). Module: modules/hexosamine_biosynthesis.yaml (GFAT step).
