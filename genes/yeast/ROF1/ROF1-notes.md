# ROF1 (YHR177W) — S. cerevisiae — Curation Notes

Journal for the AI GO-annotation review of ROF1. Provenance recorded inline as
`[PMID:xxxx "verbatim supporting text"]` or `[SGD]` / `[UniProt]` where appropriate.

## Identity (verified)

- **Standard name:** ROF1 (SGD standard name description = **"Regulator Of Fluffy"**, verified via SGD API for locus S000001220). NOTE: the task hint "Repressor Of Filamentation" is NOT the SGD name; the SGD-verified expansion is "Regulator Of Fluffy 1" [PMID:28673928 "we have given YHR177W the name ROF1 (Regulator Of Fluffy1)"]. The two are conceptually related (ROF1 represses the fluffy/filamentous colony program), but I use the SGD-verified name.
- **Systematic name / ORF:** YHR177W (Verified ORF, chromosome VIII).
- **UniProt:** P38867 (YHX7_YEAST), reviewed Swiss-Prot, 453 aa, PE=1 (evidence at protein level). [UniProt]
- **SGD:** S000001220.
- **NCBI Taxon:** 559292 (S. cerevisiae S288C).

## Domain / structure (inline domain analysis)

- **Pfam PF09729 (Gti1_Pac2); InterPro IPR018608 (Gti1/Pac2)** — this is the **WOPR domain**, the DNA-binding domain of the Wor1/Mit1/Ryp1/Gti1/Pac2/Sge1 family of fungal transcriptional regulators. [UniProt DR lines]
- **PANTHER PTHR28027 "TRANSCRIPTIONAL REGULATOR MIT1"**, subfamily SF2. Family members include ROF1 (P38867), its S. cerevisiae paralog **MIT1 (P40002)**, C. albicans **Wor1 (Q5AP80)**, S. pombe **Gti1/Pac2**, Fusarium/Verticillium **Sge1**, and H. capsulatum **Ryp1**. [interpro/panther/PTHR28027/PTHR28027-entries.csv]
- **PDB 4M8B** — 2.6 Å crystal structure of the WOPR domain of YHR177W (residues **6–201**) bound to an optimized 19-bp DNA site [PMID:24994900 "the 2.6-Å crystal structure of a WOPR domain in complex with its preferred DNA sequence"]. The paper's abstract describes the fold as "two highly conserved regions, separated by an unconserved linker, form an interdigitated β-sheet that is tilted into the major groove of DNA" and notes minor-groove contacts "primarily through a deeply penetrating arginine residue." This is the structural basis for ROF1 being a bona fide sequence-specific DNA-binding protein.
- UniProt features: two disordered regions (183–210, 428–453), a basic-residue compositional bias (198–207) just C-terminal to the structured WOPR domain — consistent with a nuclear TF (DNA-binding domain + disordered activation/regulatory tail). [UniProt FT]

Domain reasoning: The WOPR domain is a *demonstrated* DNA-binding fold (co-crystal with DNA for this exact protein fragment). Sequence-specific DNA binding and nuclear localization are therefore domain-defensible. Family membership (Wor1/Mit1) makes "transcription regulator" a well-supported functional class.

## What is KNOWN (experimental / structural)

1. **Sequence-specific DNA binding (WOPR domain).** The YHR177W WOPR domain (res 6–201) was crystallized bound to its preferred DNA site [PMID:24994900]. → supports GO:0003677 DNA binding (IDA, SGD) and GO:0043565 sequence-specific DNA binding (domain-defensible). Cromie: "YHR177W has been shown to encode a protein having DNA-binding properties (Cain et al. 2012)" [PMID:28673928].

2. **Negative regulator of complex ("fluffy") colony morphology / biofilm formation.** In an overexpression screen for genes that reduce fluffy colony structure, ROF1/YHR177W was one of the verified hits [PMID:28673928 "five genes were verified: SAN1, TOS8, YHR177W, HEK2, and SFL1"]. Overexpression REDUCES fluffy morphology and DELETION INCREASES colony structure [PMID:28673928 "Increase in copy number of DIG1, SFL1, HEK2, ROF1/YHR177W, SAN1, and TOS8 leads to a reduction in fluffy morphology in strain F45" ; "Deletion of DIG1, SFL1, HEK2, ROF1/YHR177W, SAN1, and TOS8 leads to an increase in fluffy morphology in strain F13"]. This defines ROF1 as a **repressor** of the biofilm/complex-colony program.

3. **Overexpression represses the FLO11/filamentation-MAPK regulon.** The ROF1 overexpression transcriptional profile is part of a "common factor" shared with SFL1/HEK2/SAN1 in which FLO11, FLO10, TEC1 and filamentation-MAPK/mating genes are repressed [PMID:28673928 "TEC1 itself was also one of the genes commonly repressed, as were the flocculin genes FLO10 and FLO11 that are known to be effectors of complex colony phenotypes"]. The ROF1 overexpression profile correlated most strongly with SAN1 (R = 0.84).

4. **Overexpression cell-cycle phenotype.** SGD description: "overexpression causes a cell cycle delay or arrest" [SGD; underlying screens PMID:16455487 (Sopko 2006), PMID:18617996 (Niu 2008)].

5. **Family / orthology:** paralog of MIT1 (S. cerevisiae master regulator of pseudohyphal growth) and ortholog of C. albicans WOR1 [PMID:28673928 "YHR177W is a paralog of MIT1 ... and is an ortholog of WOR1, a master regulator of the white-opaque phenotypic switch in Candida albicans"; PMID:22095082 for Mit1 being a master regulator of pseudohyphal growth]. Cain 2012 showed Wor1/Mit1/Ryp1 recognize the same DNA sequence but control largely non-overlapping gene sets between species [PMID:22095082 "the genes controlled by the orthologous regulators overlap only slightly ... despite the fact that the DNA binding specificity of the regulators has remained largely unchanged"].

## What is NOT known (knowledge gaps)

- **Direct in vivo target genes of Rof1 in S. cerevisiae.** Genome-wide ChIP for Rof1 (as done for Mit1 in PMID:22095082) has not, to my knowledge, been reported; the overexpression RNA-seq (PMID:28673928) reports downstream expression changes, not direct binding. SGD lists "0 known targets."
- **Activator vs repressor direction.** The GO annotation set encodes GO:0045944 **positive** regulation of transcription (ISS from C. albicans Wor1, which is an activator of white-opaque genes). However, the S. cerevisiae experimental data (PMID:28673928) show ROF1 behaving as a **repressor** of the FLO11/filamentation program (overexpression represses; deletion de-represses colony structure). WOPR proteins can act as activators or repressors depending on target/context (Wor1 activates opaque genes; Sfl1 is a repressor in the same regulon). The physiological direction of Rof1's transcriptional effect on its own direct targets in budding yeast is unresolved.
- **Loss-of-function phenotype is background-dependent / conflicting.** Deletion reduced complex colony morphology in one study (Furukawa et al. 2011) but had little effect in another (Cain et al. 2012), per Cromie [PMID:28673928 "deletion reducing complex colony morphology in one study (Furukawa et al. 2011) but having little effect in another (Cain et al. 2012)"]. There is no clean, penetrant single-deletion phenotype under standard laboratory conditions.
- **Physiological condition / signal that activates Rof1.** Unknown upstream signal; WOPR-family members respond to nutrient/morphogenic cues, but the S. cerevisiae Rof1 trigger is uncharacterized.
- **Whether Rof1 and its paralog Mit1 act antagonistically, redundantly, or on distinct regulons** in budding yeast is not established.

## Annotation-by-annotation reasoning (7 GOA rows)

GOA source: genes/yeast/ROF1/ROF1-goa.tsv (7 annotations).

1. **GO:0003700 DNA-binding transcription factor activity — IBA (GO_REF:0000033), enables.**
   PANTHER IBA from the WOPR/Mit1/Wor1 family. Family members are DNA-binding transcription factors; the WOPR domain is a demonstrated DNA-binding fold and Mit1/Wor1 are TFs. Domain-defensible. ACCEPT (this is a strong, family-supported MF; the specific *activity* subtype—activator vs repressor—is the open question, but "DNA-binding transcription factor activity" is the correct parent). Core MF.

2. **GO:0005634 nucleus — IBA (GO_REF:0000033), is_active_in.** Nuclear localization expected for a DNA-binding TF; consistent with IC nucleus below. ACCEPT.

3. **GO:0043565 sequence-specific DNA binding — IBA (GO_REF:0000033), enables.** Directly supported by the co-crystal structure with a specific DNA site [PMID:24994900] and family DNA-binding specificity [PMID:22095082]. ACCEPT. Core MF.

4. **GO:0045944 positive regulation of transcription by RNA polymerase II — IBA (GO_REF:0000033), involved_in.** IBA-propagated from the family; but note the *direction* (positive) is not established for Rof1 in S. cerevisiae and the direct budding-yeast experimental data point to repression of the FLO11 program. The safe, defensible statement is that Rof1 is involved in **regulation** of Pol II transcription; the specific positive direction is a knowledge gap. KEEP_AS_NON_CORE (regulatory role is real but non-core given uncertain direction / no direct targets), and flag the directionality gap. Consider that a more neutral term (regulation of transcription by RNA polymerase II) better reflects current evidence — but per guidance I will not rewrite the GOA id; I will note this in the review reason and knowledge_gaps and propose the neutral parent as a replacement suggestion.

5. **GO:0003677 DNA binding — IDA (PMID:24994900), enables.** Directly from the crystal structure of the YHR177W WOPR domain bound to DNA. Strong experimental support. ACCEPT. (GO:0043565 is the more specific term; this is the general parent — both are fine to retain, keep IDA general one as ACCEPT.)

6. **GO:0005634 nucleus — IC (PMID:24994900), located_in.** Inferred by curator (IC) from the transcription-factor role. Reasonable for a sequence-specific DNA-binding TF. ACCEPT. Core location.

7. **GO:0045944 positive regulation of transcription by RNA polymerase II — ISS (PMID:24994900, with/from UniProtKB:Q5AP80 = C. albicans Wor1), involved_in.** ISS from Wor1, an *activator* of opaque-phase genes. The inference transfers "regulates Pol II transcription" but the *positive* direction is Wor1-specific; S. cerevisiae Rof1 experimental data (PMID:28673928) indicate repression of FLO11/filamentation genes. Do NOT REMOVE (experimental/curator ISS grounded in real orthology), but mark the directionality as uncertain. KEEP_AS_NON_CORE with a note that direction is a knowledge gap.

## Core functions (defensible)

- MF: sequence-specific DNA-binding transcription factor activity (WOPR domain; co-crystal with DNA). Domain- and structure-supported.
- CC: nucleus.
- BP: regulation of transcription by RNA polymerase II, in the context of the FLO11/filamentous-growth (complex colony / biofilm) regulon — experimentally a repressor of that program on overexpression. Direction of effect on direct targets is unresolved; treat BP role as a regulator of the filamentous-growth transcriptional program.

## References gathered
- PMID:24994900 (Lohse 2014) — WOPR domain crystal structure + DNA binding (GO source; abstract-only cache, full_text_available:false).
- PMID:28673928 (Cromie 2017) — biofilm-regulator overexpression screen; ROF1 naming; repressor of fluffy/FLO11 program (FULL TEXT cached).
- PMID:22095082 (Cain 2012) — Mit1/Wor1/Ryp1 conserved regulator; YHR177W DNA-binding; paralog relationship (abstract-only cache).
- PMID:16455487 (Sopko 2006) — systematic overexpression phenotypes (abstract-only) — overexpression cell-cycle phenotype context.
- PMID:18617996 (Niu 2008) — cell cycle control by overexpression (full text cached) — overexpression phenotype context.
</content>
</invoke>
