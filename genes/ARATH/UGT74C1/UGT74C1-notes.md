# UGT74C1 - Arabidopsis thaliana - review notes

UniProt: Q9SKC1 · At2g31790 · EC 2.4.1.- (UniProt) / thiohydroximate glucosyltransferase EC 2.4.1.195 · Taxon 3702
Context: S-glucosylation step of aliphatic GSL core structure (module annoton ugt74_activity).
No falcon deep-research file was present at review time.

## Core function
- Thiohydroximate S-glucosyltransferase, accessory to UGT74B1, specialized for aliphatic GSLs.
  [PMID:24779768 "Systematic genetic analysis of this clade indicates that UGT74C1 plays a special role in the synthesis of aliphatic glucosinolates"]
  [PMID:24779768 "the ability of UGT74C1 to complement phenotypes and chemotypes of the ugt74b1-2 knockout mutant and to express thiohydroximate UGT activity in planta"]
  [PMID:23144921 "UGT74C1 glucosylates methionine-derived thiohydroximates; UGT74B1 metabolizes tryptophan-derived thiohydroximates"]
- PMID:24779768 is abstract-only in the cache; kinetic data not reviewed.

## Comparator check (NEW GO:0019761)
- QuickGO (2026-09-30): UGT74B1 (O48676) has GO:0047251 IDA (PMID:15584955) and GO:0019761 IMP + IBA;
  CYP83A1, CYP79F1/F2 carry GO:0019761. UGT74C1 has neither -> gap, not convention.
- Participation: UGT74C1 catalyzes the glucosylation step itself.

## Localization
- Soluble family 1 UGT (no TM/transit peptide in UniProt features); cytoplasm IBA accepted.
- Chloroplast ISM -> REMOVE; peroxisome HDA (PMID:28887381) -> MARK_AS_OVER_ANNOTATED.

## Decisions
- GO:0035251 UDP-glucosyltransferase (ARBA IEA) -> MODIFY to GO:0047251 thiohydroximate beta-D-glucosyltransferase activity
- GO:0008194 IEA -> KEEP_AS_NON_CORE
- GO:0080043 / GO:0080044 quercetin 3-O/7-O-glucosyltransferase IBA -> MARK_AS_OVER_ANNOTATED
  (deep family 1 node seeded by flavonol UGTs; no evidence for UGT74C1)
- GO:0005737 IBA -> ACCEPT
- NEW GO:0019761 glucosinolate biosynthetic process (IMP, PMID:24779768)


## Module-member evidence audit — 2026-10-25

Reviewed every original row (8) and core function using review/annotation-reviewer instructions, current cached primary publications and the existing research. Preserved all source annotation fields and all pre-existing proposed rows. Reused the existing genuine Falcon provider report and its artifacts. These plant targets do not require bacterial FEBA retrieval.

PMID24779768 supports genetic complementation and thiohydroximate UGT activity in planta, not a requirement that every UGT74 member has identical substrate preference. Broad UDP-glycosyltransferase is refined consistently to the experimentally supported thiohydroximate activity. Retained the pre-existing biosynthesis NEW based on catalytic participation; no additional process row added. Unchecked peroxisomal HDA is undecided.

Broad and substrate-specific terms were assessed consistently across evidence codes. No NEW rows were added. Previously proposed rows were evaluated for direct participation rather than filled from pathway adjacency. Experimental cohort calls whose protein-level data were not verified were left UNDECIDED; full-text availability alone was not treated as proof of a target-specific assay. Original sources and provider reports were not hand-edited.

### Final consistency QA, 2026-10-26

Removed chain-length feature text as localization evidence. Retained the PAINT cytoplasm judgment at its warranted precision, and left the unverified plastid prediction unresolved because absent targeting annotations do not establish absence.
