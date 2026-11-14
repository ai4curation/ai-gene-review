# E. coli MmuM evidence and identity

Read 2026-11-07. The protected publication caches have not been overwritten. PMID9882684 is full text; PMID10026151,26564203,23912937 and11967071 are abstract-only. PMID25046177 was newly fetched normally and remains abstract-only. Publisher DOI access attempts for10026151 and26564203 did not yield full text; this is not evidence that their experiments are absent.

## Identity and direct chemistry

The frozen curated Q47690 record identifies mmuM, synonymous yagD, at b0261/JW0253 in E. coli K-12. PMID9882684 explicitly renames yagD as mmuM. Its native experiments use KL19 and derived MTD23 (metE/metH lesions), MTD123 (additional yagD lesion) and MTD234 (additional ykfD/mmuP lesion). Growth in M9 with0.8% glucose and15 micromolar supplements was assessed after18h aerobically at37C. SMM-supported growth is lost in the mmuM lesion background. MmuP loss blocks low-concentration utilization while some growth occurs above50 micromolar SMM; no unconditional transporter specificity is inferred here.

The purified-YagD catalytic observations summarized in9882684 refer to the companion biochemical study10026151. Its accessible abstract explicitly describes cloned, overproduced and purified E. coli YagD and both SMM and SAM donors. The frozen curated record assigns that biochemical study to JM109. The earlier KL19/JM109 plasmid sequences were not recovered, so those assays are not relabeled MG1655-specific measurements.

Official RCSB5DMM entity1 is310 residues and is exactly identical to frozen Q47690; the entity reports zero mutations and a genetically engineered K-12 source. SIFTS independently maps it to Q47690. The entry is linked to PMID26564203. Nonpolymer entity2 is zinc and entity4 is homocysteine. This directly grounds the structural target and zinc association, without asserting that crystallization conditions measure native metal occupancy. See identity-results.json and the reproducible checker.

## Process and donor boundaries

Current GO0033477 explicitly includes SMM conversion to methionine and distinguishes that reaction from a cycle established by concurrent MMT activity. Its only current children are SMM biosynthesis and the SMM cycle; neither is a supported refinement of the imported-substrate utilization shown here. Retain the general metabolic process as precise as warranted.

The GO0033528 SMM-cycle claim requires context beyond the demonstrated reaction. No complete endogenous SAM-to-SMM-to-methionine cycle is established by the inspected E. coli work. The recorded PAINT node PTN001843930 remains a real source assertion, and the independently captured official release19 tree verifies Q47690 leaf PTN001078917 below rootPTN001843930 viaPTN000472791 andPTN000473134. The topology and propagated GO summary do not themselves establish native cycle context; the complete underlying experimental IBD scope remains unresolved. The normal loss command returned no IRD/IKR; that result is not used to claim a fully inspected loss-free lineage. The cycle row remains UNDECIDED, not a claim that methyl transfer is absent.

PMID23912937 tests externally provided SAM in an engineered delta-metK strain carrying a rickettsial SAM transporter. PMID25046177 discusses preferential use of the damaged(R,S) stereoisomer by HMTs. These contexts do not show that MmuM alone supplies net methyl groups for a self-sustaining native methionine cycle. A preference is not an absolute exclusion of the alternate stereoisomer. The existing SAM-dependent catalytic annotations remain as precise secondary chemistry supported by10026151, without invented stereospecific kinetics.

The DNA-damage IEP observation is retained in its immutable payload. The current term includes cellular responses such as expression changes, but the target role remains unresolved: an expression screen alone does not identify whether MmuM performs damage-response work or changes secondarily. No target functional counter-assay was located, so UNDECIDED is used rather than claiming the annotation false.
