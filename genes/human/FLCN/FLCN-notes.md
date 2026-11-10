# FLCN (human, Q8NFG4) notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Context: this review is the experimental reference for transfer to donkey FLCN (EQUAS A0A8C4MM62). Donkey and
human FLCN are in the same PANTHER subfamily, PTHR31441:SF2 (FOLLICULIN). Human FLCN is the main experimental donor
under TreeGrafter node PTN009120754. No ProtNLM2 files were opened.

### Deep research
`just deep-research-falcon human FLCN --fallback perplexity-lite` failed: falcon could not authenticate, and
perplexity returned HTTP 401 (insufficient_quota). No deep-research file exists. The review is built from the
cached publications (all GOA PMIDs plus the mouse donor papers behind the ISS rows, fetched with `just fetch-pmid`)
and the UniProt record.

### Evolutionary grounding
- UniProt places FLCN in PANTHER PTHR31441:SF2. The family file `interpro/panther/PTHR31441/PTHR31441-entries.csv`
  has one subfamily, SF2, which contains yeast LST7 (P53237), S. pombe bhd1 (O74769), bovine FLCN and Xenopus flcn.
- PAINT node PTN002833743 is deep: its donors include yeast LST7 and S. pombe Bhd1. Terms propagated from it are
  positive regulation of TORC1 signaling, the FNIP-folliculin RagC/D GAP complex, cytosol and nucleus. So the Rag GAP
  module is ancestral to opisthokonts.
- The transcription-repression and TGF-beta terms were propagated from vertebrate-level nodes (PTN001265854 and
  PTN001265856) seeded by MGI Flcn.
- On QuickGO, mouse Flcn (Q8QZS3) carries GO:0005096 by IBA with `contributes_to`, seeded from LST7. Human IDA rows use
  enables, which is appropriate because FLCN carries the catalytic Arg164 [PMID:31672913 "First, we identified Arg164
  of FLCN as a catalytically required arginine residue for GAP activity."].

### Experimentally established in human (direct)
- RagC/D GAP activity of FLCN-FNIP [PMID:24095279 "we identified the FLCN-FNIP complex as a potent GTPase activating
  protein (GAP) for RagC/D"]. This is supported by the R164A catalytic mutant (PMID:31672913, PMID:31704029) and by
  the GAP-competent structure (PMID:36103527).
- Substrate-specific TORC1 control of TFEB/TFE3, but not S6K/4E-BP1 [PMID:32612235 "Importantly, expression of
  active RagCS75L or RagDS77L mutants in FLCN KO cells rescued TFEB phosphorylation"].
- Lysosomal membrane localization in amino acid starvation and cytosol on refeeding (PMID:24081491, PMID:24095279,
  PMID:29848618, PMID:31672913).
- Secondary functions: perinuclear lysosome clustering via RILP-Rab34 (PMID:27113757); LDHA inhibition
  (PMID:34381247, one laboratory); a moderate effect on basal autophagy (PMID:25126726); localization at cilia,
  centrosomes and the mitotic spindle (PMID:23784378; PMID:27072130).

### Inferred / phenotype-only (mostly mouse)
QuickGO shows that the mouse source annotations for embryonic development, haemopoiesis, kidney proliferation,
ERK/AKT, TOR regulation and pro-B differentiation are IMP annotations with `acts_upstream_of_or_within`. The human ISS
rows restate them as `involved_in`. These rows are MARK_AS_OVER_ANNOTATED, as knockout phenotypes, not participation.

The adipose browning and thermogenesis terms are kept as non-core. They have a mechanism through FLCN's core axis
(PMID:27913603: FLCN-mTOR-TFE3-PGC-1beta), but the evidence is from mouse only.

The "negative regulation of TOR signaling" rows are marked as over-annotation. mTORC1 hyperactivation in FLCN-null
kidney depends on TFEB [PMID:32612235 "TFEB is constitutively nuclear and active in Flcn-KO kidneys and its depletion
rescues mTORC1 hyperactivation."].

The "regulation of Ras protein signal transduction" rows are MODIFY to GO:1904263. GO:0007265 is defined for the Ras
subfamily, and the Rags are not in it.

### Transfer guidance for orthologs (e.g. EQUAS/HORSE FLCN in SF2)
Safe to transfer within SF2: GO:0005096, GO:1990877, GO:1904263, GO:0005765, GO:0005829 and GO:0034198.
Do not transfer: the mouse knockout phenotype terms listed above; GO:0160193 (LDHA inhibition, one human study only).


## 2026-10-28 — ClinGen Mendelian audit

The current disposition is in [FLCN-ai-review.yaml](FLCN-ai-review.yaml); this appended entry supersedes conflicting interpretations in the historical journal above without rewriting it. The [source evidence guide](FLCN-source-evidence.yaml) records assay boundaries, actual source access, PAINT provenance, product reconstruction and quotation relocations.

All 121 original machine contexts and their order, all three natural-product records, and all 244 inherited quotation/reference occurrences (46 resolved pairs) are preserved. Actual formatter/seeder replay resolves 125 current raw rows through 124 formatted rows into the same 121 contexts, with no missing annotation or added row. The review has 36 ACCEPT, 63 KEEP_AS_NON_CORE, 19 MODIFY and three TOO_GENERAL decisions; no NEW assertion is proposed.

The explicit campaign instructions retain supported generic binding as non-core and prohibit new publication quotations, overriding conflicting local skill defaults. The 20 generic-binding contexts are assessed by partner and source. Their association assays do not automatically establish binary contact or an adapter subtype. In particular, FLCN is an Hsp90 client; FNIP1/2 supply cochaperone activity (PMID:27353360). Default validators remain unchanged, so their policy advisories are disclosed rather than suppressed.

Twenty inherited quote occurrences are relocated to truthful reference findings because the excerpts did not establish their original row-specific claims. Each finding records its original occurrence path. Repeated excerpts preserve the original provenance and are not counted as independent experiments. The remaining excerpts and all source identifiers remain intact; newly consulted primary evidence is reference-only. This includes separating the PMID:22709692 pro-B phenotype from the current PMID:21258407 hemopoiesis donor, and separating TFE3 transcription from the unidentified higher-mass modification in PMID:21209915.

The two molecular cores are partner-dependent RagC/D GAP activity and directly measured LDHA inhibition. The latter is supported by purified human protein experiments and tested-cell glycolytic effects, while endogenous stoichiometry and broader physiological replication remain open (PMID:34381247). Natural truncated products are not equated with canonical Arg164 mutants or the synthetic inhibitory peptide. Structural inactive/intermediate states in PMID:31672913 and PMID:31704029 are distinguished from the engineered active complex in PMID:36103527.

Context-dependent negative TOR regulation in flow/ciliary and renal experiments coexists with the predominant positive Rag/TFEB role (PMID:27072130; PMID:32612235). S6K/4E-BP1 selectivity is conditional: PMID:24081491 also measures S6K/S6 effects in its human depletion model. Embryonic, hematopoietic, junction, renal and pro-B annotations are retained as contextual non-core associations with actual species, allele and endpoint limits. Fnip1 rescue/transplant experiments are not transferred to Flcn. Unknown higher-mass TFE3 modification is distinct from FLCN-promoted phosphorylation (PMID:21209915).

Selected actual primary sections were read across the 28 accessible papers and independent consultations; PMID:18663353 remains abstract/preview-only and is corroborated independently where retained. Several ordinary caches are abstract-only or omit Results despite a full-text flag. Separately recovered original text is identified by official URL and hash in the guide, without replacing those caches. No claim is made to have inspected every figure pixel or supplementary file.

All 31 existing normal sources were hydrated from exact main bytes before genuine fetch. The only new normal source is the qualified PTHR31441 PAINT slice. The actual 91-node tree and 91-sequence MSA reproduce the 579-aa human target and all six incoming IBD joins; the seventh family record is not a new annotation. Original PAINT GAF and PANTHER API release 19 retain separate provenance. Human experimental grounding among IBD seeds is legitimate, not circular.

Canonical schema, ontology, GOA, reference-title and quotation validation passes with 20 generic-binding advisories under the explicit campaign policy. The status manager computes DRAFT; the existing status is updated accordingly, with validators unchanged.


## 2026-10-28 — Scientific review follow-up for PR #5707

The follow-up to [review comment 6479089271](https://github.com/ai4curation/ai-gene-review/pull/5707#issuecomment-6479089271) retains all 121 actions and both cores. The eleven non-core process rationales now state their positive experimental endpoints: lineage-directed embryoid-body outcomes and separate embryo alleles, junction organization/barrier measurements, apoptosis perturbation with Bhd re-expression, renal signaling readouts, measured energy balance, postnatal renal proliferation and the direct conditional Flcn pro-B phenotype. These support context-limited regulatory or developmental involvement; their retention does not assign an unmeasured direct enzyme activity. Unresolved lineage autonomy, survival versus differentiation and conservation in humans remain in suggested questions.

This explicitly answers the historical blanket-withdrawal suggestion above. A donor relation label is provenance, not a substitute for biological assessment. The blanket premise is also inaccurate for junction assembly: the current mouse GO:0007043 IMP/PMID:22965878 donor uses involved_in. Other original donor and human relation fields are preserved unchanged. Actual source-specific measurements, perturbations and the available re-expression evidence support the retained non-core scope; no blanket inference from a knockout to an untested molecular activity is made.

All 244 inherited quotation/reference occurrences and 46 resolved pairs are preserved, with no new quotation. Six renal TFEB-feedback excerpts move from the three negative-TOR rows to their actual PMID:32612235 reference findings, making 26 relocations in total. Human flow/ciliary negative-TOR support remains a source-only citation to the inspected PMID:27072130 primary Results. This distinguishes complementary experimental contexts instead of presenting renal feedback excerpts as the flow mechanism. The quote-free stray PMID:32612235 row 103 support entry is removed; the existing excerpt remains conserved with its actual reference finding.

Repeated statements now have one biological Finding per distinct statement. Remaining exact inherited occurrences are stored under FindingReview.supported_by, with explicit original-to-current occurrence mappings in review_notes and the source guide. This preserves every occurrence without representing ten repetitions as ten findings. The repeated evidence records do not count as independent observations or increase evidence strength. The explicit user campaign no-new-quote and conservation instructions continue to override conflicting local quotation defaults. No validator policy is changed.

The AKT explanation distinguishes the mouse AKT1/2 transcript comparison from human tumor protein/phosphorylation measurements (PMID:19850877). The unchanged PMID:18182616/PMID:19850877 normal caches remain abstract-only; selected original Results and main Methods were recovered separately, as documented with official source URLs in the guide. Exact PANTHER API node metadata now makes the Metazoa-Choanoflagellida placement independently inspectable while preserving the blank taxon in the original IBD GAF. Broad TOR regulation remains TOO_GENERAL because both supported signed descendants are retained; the broad term is correct but redundant.
