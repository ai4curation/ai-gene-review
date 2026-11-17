# Caulobacter annotation-reviewer consultation — 2026-11-07

Scope: fresh CAUVN/groEL B8H163, CAUVN/groES B8H164, CAUVN/CCNA_00109 A0A0H3C5Z7. The parent-frozen `caulobacter-seed-baseline.json` is the immutable annotation baseline. No module, family, project, inventory, upstream source record, GOA, or provider artifact was edited by this consultation.

## Decisions

| Member | Seeded rows | ACCEPT | MODIFY | UNDECIDED | Core |
|---|---:|---:|---:|---:|---|
| groEL | 6 | 5 | 1 | 0 | ATP-dependent folding/refolding, GroEL/GroES chamber |
| groES | 6 | 4 | 0 | 2 | GroEL binding; contributes to ATP-dependent folding |
| CCNA_00109 | 4 | 3 | 1 | 0 | Protein-disulfide reductase plus general holdase NTR |

All 16 ordered source payloads retained, zero added/deleted/NEW/retired annotation rows. GroEL GO:0044183 is refined to existing GO:0140662. CnoX GO:0005737 is refined to existing cytosol GO:0005829. No assay-derived claim is added merely to silence a validator warning.

GroES GO:0044183 is **accepted**: its current definition explicitly includes binding to a protein-containing complex to assist folding. The core records GO:0051087 with `contributes_to_molecular_function: GO:0140662`; it does not assign intrinsic ATP hydrolysis to GroES. ATP binding and metal ion binding remain UNDECIDED. E. coli nucleotide measurements (PMID:7867782) do not directly assay this target, and the absence of Cys/His is not a valid general argument against metal binding. No target-specific metal site was established. These uncertainties are not disguised as demonstrated InterPro/PAINT mapping defects.

CcCnoX is a **constitutive** holdase and a TrxR-recycled reductase. Native CcCnoX's transient catalytic mixed disulfides must not be conflated with stable protective mixed disulfides in E. coli CnoX or trapped resolving-cysteine-mutant complexes. CcCnoX alone does not refold citrate synthase. The general holdase NTR is supported by direct aggregation suppression and avoids an unsupported carrier/escort claim under GO:0140309. There is no NEW process row.

## Identity and source adjudication

PMID:30482828 full text and official supplements were read. Table S2 identifies CB15N; the frozen UniProt records explicitly identify NA1000 / CB15N, taxon565050. Same-strain loci are CCNA_00721 (GroEL), CCNA_00722 (GroES), CCNA_00109 (CnoX). Table S2 identifies recombinant Caulobacter constructs in BL21; Text S1 distinguishes untagged CnoX/GroEL and C-terminally His-tagged GroES. BL21 is the expression host, not the source organism. The main recovery assay explicitly uses Caulobacter GroEL14/ES7 and ATP. This supports biochemical cooperation and recovery, not stable CnoX–GroEL binding, direct transfer kinetics, or cross-species equivalence of all CnoX mechanisms.

The original primary paper does not provide these UniProt accession identifiers. CnoX's explicit CCNA_00109 crosswalk was checked in normally fetched full-text PMID:33996917; the frozen reference sequence has thioredoxin–TPR architecture and WCGPC46–50 with only C47/C50. This is a supported strain/locus mapping, not an independent experimental-clone sequence comparison. The secondary review's approximately90 aggregation-protected proteins conflicts with the primary distinction between50 aggregation-associated proteins and90 putative redox substrates. Its identity crosswalk is used; its conflated count and broad oxidative-activation language are not adopted. The reference review and notes record this limitation.

Current QuickGO definitions are retained in `caulobacter-ontology.json`. The three consulted publication caches and six raw gene sources are hashed in `caulobacter-protected-baseline.json`. The entire source snapshot (67,853 existing files at capture) is in the ignored audit cache and was also rechecked unchanged. PMID:33996917 was acquired normally in this consultation; the other papers were acquired by the coordinator/other worker and only read here.

## Validation and limitations

Three focused `just validate` runs PASS, three renders PASS, three generated histories validate. GroEL and GroES each produce the advisory that core GroEL-GroES complex GO:1990220 is absent from seeded annotations; the independently supported complex core is retained without manufacturing an extra row. CnoX validates without curation warnings. Following coordinator verification, all three records are COMPLETE: every seeded annotation has been adjudicated, and the two explicit UNDECIDED binding judgments and advisory complex-core coverage notices do not represent pending scientific review. A separate generated history per gene records this status-only follow-up; notes, renders, focused validation and the frozen handoff were refreshed.

All three `just paint-losses` commands complete, but each says the accession is **not a leaf** in the available family tree and “losses not checked.” The tool's generic final no-loss sentence must not be reported as a lineage-negative result. No IBA rows occur among these16 seeds; no invented lineage-loss records were created.

All three actual Falcon attempts fail403 authentication. No provider text was invented; manual primary-source research is documented in each notes journal. Exact log paths and outcomes are in `caulobacter-validation.json`. The reusable `caulobacter-preservation.py` verifies source hashes and ordered annotation payload equality against the parent baseline. No full-repository validation, commit, or push was performed. Coordinator owns any broader validation and publication.
