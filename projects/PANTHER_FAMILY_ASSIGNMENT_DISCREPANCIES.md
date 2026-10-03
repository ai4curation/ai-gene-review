---
title: "PANTHER family assignment discrepancies"
maturity: SCOPING
tags: [EVALUATION, PIPELINE]
species: [human, worm]
genes: [MEGF10, ced-1]
---

# PANTHER family assignment discrepancies

**Bottom line:** the same PANTHER release can put a protein in different
families depending on where you look. UniProt's `DR PANTHER` cross-references
come from InterPro's best-hit HMM match. PANTHER's own sequence classification
files (and the PAINT trees that IBA annotations come from) come from PANTHER's
own pipeline. When the two disagree, a module or review that takes its family
id from UniProt can be grounded on a family that has no PAINT tree for the
protein, while the family that does carry that tree goes unused. This project
records such cases. So far it holds one, found while building the phagocytosis
modules.

## Why this matters here

- **Module grounding.** `FamilyDescriptor.term` ids are checked against
  `interpro/panther/panther-members.tsv`, which mixes PANTHER classification
  rows with UniProt fallback rows (`ai-gene-review refresh-panther-members`). A
  curator who copies the family id from a UniProt entry may get an error, or
  may get a family that differs from the one the validator checks against.
- **IBA interpretation.** PAINT nodes (PTNs) belong to PANTHER's own trees. If
  the UniProt cross-reference names another family, the IBAs a protein carries
  appear to come from a family it does not belong to.
- **Orthology claims.** Family ids are used as evidence of orthology between
  representative members. Two sources that disagree make that evidence
  ambiguous.

## Case log

| # | Proteins | UniProt / InterPro family | PANTHER 19.0 classification | PAINT | Status | Found in |
|---|---|---|---|---|---|---|
| 1 | C. elegans ced-1 (UniProtKB:Q9XWD6), human MEGF10 (UniProtKB:Q96KG7) | ced-1 → PTHR24043:SF8 (SCAVENGER RECEPTOR CLASS F / EGF-LIKE DOMAIN-CONTAINING PROTEIN); MEGF10 → PTHR24052:SF13 (DELTA-RELATED / MULTIPLE EGF LIKE DOMAINS 11) | Both in PTHR24035 (MULTIPLE EPIDERMAL GROWTH FACTOR-LIKE DOMAINS PROTEIN): ced-1 → SF109 PROTEIN DRAPER; MEGF10 → SF136 | MEGF10 IBAs come from PTN002372116 and PTN009076277, nodes whose seeds include ced-1, Draper and mouse Megf10 | Open: PANTHER classification preferred; family not yet asserted in the module | [phagocytic engulfment module](../modules/phagocytic_engulfment.yaml) |

### Case 1: CED-1 / Draper / MEGF10 engulfment receptors

CED-1 (C. elegans), Draper (Drosophila) and MEGF10 (vertebrates) are the
standard orthologous engulfment receptors for apoptotic cells. They are
multiple-EGF-like-domain transmembrane proteins with an EMI domain and NPxY /
YxxL tail motifs.

**What UniProt says** (entry version 168 for Q9XWD6 and 173 for Q96KG7,
2026-06-10; InterPro 110.0, PANTHER 19.0):

- ced-1 → `PTHR24043` SCAVENGER RECEPTOR CLASS F, subfamily `PTHR24043:SF8`.
  The InterPro match covers only residues 685–963 of 1111, which lie in the
  EGF-like-repeat region.
- MEGF10 → `PTHR24052` DELTA-RELATED, subfamily `PTHR24052:SF13`
  ("MULTIPLE EGF LIKE DOMAINS 11"). The InterPro match covers residues 9–675
  of 1140.

**What PANTHER's own classification says** (`PTHR19.0_<organism>` sequence
classification files, cached under `.cache/panther/` by
`refresh-panther-members`):

- `PTHR24035:SF109` PROTEIN DRAPER: ced-1 (Q9XWD6), Drosophila drpr (Q9W0A0),
  and Dictyostelium sibA–sibD (Q54KF7, Q54JE1, Q54JA5, Q54JA4).
- `PTHR24035:SF136` MULTIPLE EPIDERMAL GROWTH FACTOR-LIKE DOMAINS PROTEIN 10:
  MEGF10 orthologs from human, mouse, rat, cow, chicken, Xenopus and
  zebrafish.

**What PAINT says** (QuickGO IBA rows for Q96KG7, WITH/FROM column):

- `GO:0043652` engulfment of apoptotic cell, from `PTN002372116`. Seeds:
  FB:FBgn0027594 (drpr), MGI:2685177 (Megf10), WB:WBGene00000415 (ced-1).
- `GO:0005044` scavenger receptor activity, from `PTN009076277`. Seeds:
  Q96KG7 and WB:WBGene00000415.

PAINT therefore treats CED-1, Draper and MEGF10 as a single clade inside
PANTHER's tree. This agrees with the PANTHER classification and the
literature, and disagrees with the UniProt cross-references.

**Caveats.**

- PTHR24035 is a broad family. Of its 11 human members, 9 sit in a
  laminin-dominated subfamily (`SF127` LAMININ SUBUNIT ALPHA-5-RELATED, which
  also holds MEGF11) and MEGF6 has its own subfamily (`SF137`). A family-level
  id alone therefore says little. No single subfamily contains both
  representatives.
- The name of the UniProt-assigned subfamily (`PTHR24052:SF13`, "MULTIPLE EGF
  LIKE DOMAINS 11") does not match PANTHER's own placement of human MEGF11,
  which is `PTHR24035:SF127`. In the cached classification files the only
  member of `PTHR24052:SF13` is bovine MEGF11 (F1MRL6). MEGF11 may be a second
  case; it has not been checked.
- The likely mechanism is an assumption, not a verified fact. InterPro keeps
  the single best-scoring family HMM, and EGF-repeat-rich proteins score well
  against several neighbouring EGF-rich families. This needs confirming, for
  example by comparing full HMM score tables or asking the PANTHER and
  InterPro teams.

**Current handling.** In `modules/phagocytic_engulfment.yaml` the CED-1/MEGF10
annoton lists both proteins as `representative_members` and asserts no
PANTHER id. Planned resolution: once a MEGF10 gene review exists and its GOA
file carries the IBA row with PTN002372116 in WITH/FROM, ground the annoton on
`PTHR24035` and declare PTN002372116 as its ancestral node.

## Reproduce

```bash
# UniProt cross-reference (InterPro-derived)
curl -s https://rest.uniprot.org/uniprotkb/Q96KG7.txt | grep '^DR   PANTHER'
# InterPro match coordinates
curl -s https://www.ebi.ac.uk/interpro/api/entry/panther/protein/uniprot/Q96KG7
# PANTHER's own classification (after `just refresh-panther-members`)
grep -h Q96KG7 .cache/panther/PTHR19.0_human
# PAINT provenance of the IBAs
curl -s -H 'Accept: application/json' \
  'https://www.ebi.ac.uk/QuickGO/services/annotation/search?geneProductId=UniProtKB:Q96KG7&evidenceCode=ECO:0000318'
```

## Next steps

- [ ] MEGF10 and ced-1 gene reviews (these unblock case 1 in the module).
- [ ] Check MEGF11 (possible case 2).
- [ ] Scope a systematic scan: for every accession cited in `modules/`,
      compare the UniProt `DR PANTHER` family with the PANTHER classification
      row and flag disagreements. Tooling question: should
      `refresh-panther-members` record the source of each row (classification
      or UniProt fallback) so such disagreements are visible?
- [ ] Decide whether disagreements of this kind should be reported to
      PANTHER/InterPro.
