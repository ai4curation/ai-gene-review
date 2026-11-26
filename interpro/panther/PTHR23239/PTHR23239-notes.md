# PTHR23239 (INTERMEDIATE FILAMENT) family review notes

Working notes for `PTHR23239-review.yaml`, written 2026-11-26 alongside the human KRT9 review.

## Deep research

No family deep-research report is filed.

- Providers available in this environment: `asta`, `openscientist`, `claude_code`. Falcon,
  Perplexity and OpenAI were not available.
- `just deep-research-interpro-family PTHR23239 asta --database panther` ran and wrote a report,
  but the retrieval was keyed on the template text, not the family: all 13 papers returned were
  about the InterPro database and unrelated subjects, and the word "keratin" did not occur in the
  file. The file was discarded as ungrounded and is not committed.
- The review therefore rests on the PAINT slice, the PANTHER tree, QuickGO seed annotations and
  the cached publications listed in the review's `references`.

## What the family contains

Read from `PTHR23239-entries.csv` and the PANTHER 19.0 tree (545 leaves, 470 internal nodes):

- Type I (acidic) keratins: human KRT9, KRT10, KRT12 to KRT20, KRT23 to KRT28 (epithelial) and
  KRT31 to KRT40 (hair keratins).
- Phakinin (BFSP2), subfamily SF32, the one non-keratin group.
- No type II keratins, vimentin or lamins. In `panther.obo` the type II keratin subfamilies sit
  under PTHR45616 and vimentin and lamin subfamilies under PTHR45652.

Tree outline (leaf counts in brackets):

```
PTN008383940 root (545)
  2 amphioxus leaves
  PTN001905729 vertebrates (543)                 IBD: cytoskeleton
    PTN002757456 phakinin BFSP2 (21)             IBD: intermediate filament, IF organization
    PTN002757475 KRT18 (37)                      IBD: keratin filament, IF cytoskeleton organization
    three small fish/frog groups (23)
    PTN002757528 type I keratins (462)           IBD: keratin filament, structural constituent of
                                                      skin epidermis, morphogenesis of an epithelium
      PTN001905860 ray-finned fish keratins (24)
      PTN008383948 tetrapod type I keratins (438) IBD: epithelial cell differentiation, IF organization
        PTN000580356 KRT19 + hair keratins KRT31-40 (149)
        PTN000754807 KRT10, KRT12, KRT25-28 (92)
          PTN000580359 KRT10 (18)                IBD: keratinocyte differentiation
          PTN004620770 KRT25/27/28 (36)          IBD: hair follicle morphogenesis
          PTN000580219 mammalian KRT12 (13)      requested IRD for GO:0030280
        PTN008594621 KRT9, KRT13, KRT15 (74)
          PTN000581398 KRT9 (14)                 no PAINT row of its own
        PTN008594611 KRT14, KRT16, KRT17, KRT20 (67)
          PTN001508564 KRT14/KRT16 (24)          IBD: keratinocyte differentiation
        PTN009066884 KRT24 (38), PTN009066916 KRT23 (18)
```

## Seeds behind the six IBA rows on human KRT9 (P35527)

Seed identifiers are PAINT's with/from. MGI and RGD ids were resolved to UniProt accessions by
UniProt cross-reference search, and the experimental annotations were read from QuickGO by gene
product and GO id (with descendants), not by term name. The queries returned positives for every
seed, so an empty result was never relied on.

| Term | IBD node | Seeds and their evidence | Verdict |
|---|---|---|---|
| GO:0005856 cytoskeleton | PTN001905729 | 21 seeds across phakinin, KRT18 and the main keratin clade; direct localisations (IDA, IPI) to cytoskeleton or its descendants | SOUND |
| GO:0045095 keratin filament | PTN002757528 | rat Krt9 IDA PMID:11071770; human KRT14 IDA PMID:11724817, PMID:22705788; mouse Krt14 and Krt10 IDA PMID:14673151; human KRT13 IDA PMID:9714826; human KRT15 IDA PMID:41511042; chicken KRT14 IDA PMID:15157236; human KRT36 and KRT25 IPI PMID:32296183; human KRT10 IPI PMID:27595935 | SOUND |
| GO:0045109 intermediate filament organization | PTN008383948 | human KRT9 IMP PMID:10218578; human KRT20 and mouse Krt20 IMP PMID:12857878; mouse Krt25 IMP PMID:17920809; mouse Krt10 IGI PMID:24751727; mouse Krt17 IGI PMID:15601842; human KRT14 IMP PMID:11724817 (GO:0045110) | SOUND |
| GO:0030280 structural constituent of skin epidermis | PTN002757528 | human KRT10 IDA PMID:7543090 and NAS PMID:2459124; mouse Krt36 IDA PMID:1385239 | NEEDS_PRUNING (ADD_IRD at PTN000580219, KRT12) |
| GO:0002009 morphogenesis of an epithelium | PTN002757528 | mouse Krt12 and human KRT12 IMP PMID:26758872; mouse Krt16 IMP PMID:24218583; mouse Krt17 IGI PMID:15601842 and IMP PMID:12050118 (GO:0031069); mouse Krt25 and Krt27 IMP PMID:17920809 (GO:0031069) | UNRESOLVED |
| GO:0030855 epithelial cell differentiation | PTN008383948 | mouse Krt10 and Krt14 IDA PMID:19303854; rat Krt14 IDA PMID:8950218; chicken KRT14 IDA PMID:15157236; mouse Krt16 IDA PMID:11029038 (GO:0030216, GO:0031424); mouse Krt17 IGI PMID:15601842 (GO:0031424); human KRT10 IDA PMID:7543090 (GO:0070268) and IEP PMID:22170488 (GO:0030216) | UNRESOLVED |

`just paint-losses human KRT9` reports no IRD or IKR on the KRT9 lineage.

## Points for the KRT9 gene review

- KRT9 is in its own WITH/FROM for GO:0045109. That is expected: its IMP annotation is one of
  the descendant evidences for the IBD, so the source is not circular.
- KRT9 has no IBA for GO:0005200 structural constituent of cytoskeleton because the family has no
  IBD for that term. The absence is a gap in PAINT coverage, not a judgement against the term.
- GO:0030280 is right for KRT9 itself. The pruning request concerns KRT12 only.
- The two broad process rows are not established by this review as inherited functions. The human
  KRT19 review keeps GO:0002009 as non-core and marks GO:0030855 as over-annotated.

## Limits

- Most seed papers were cached as abstracts only. PMID:8950218 (rat Krt14) and PMID:1691189
  (mouse Krt18) could not be fetched.
- The IRD request names only the KRT12 clade. KRT19, KRT20 and KRT13 receive the same
  GO:0030280 IBA and are probably the same case, but their tissue evidence was not examined here.
- Whether the non-mammalian members of SF369 (one Anolis, one chicken sequence under
  PTN008383982) are corneal keratins was not checked, so the requested target is the mammalian
  node PTN000580219.
