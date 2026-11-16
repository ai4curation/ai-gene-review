---
title: "Actin Dynamics: Process Terms to Molecular Functions"
maturity: SCOPING
tags: [OBSOLETION, BIOLOGY_DOMAIN]
species: [human, yeast, SCHPO, DROME]
collections: [GO_TRACKER_BACKLOG]
---

# Actin Dynamics: Process Terms to Molecular Functions

**Bottom line:** Five GO tracker issues opened between 2019 and 2021 ask
for single-protein actin activities, currently modelled as biological
processes, to become molecular functions: severing, fragmentation,
cross-linking, nucleation and polymerase activity. Two of the requested MFs
now exist (GO:0003789 *actin filament severing activity*, restored in 2022,
and GO:7770064 *actin-filament cross-linking activity*, created 2026-04-16).
None of the process terms they replace has been obsoleted. Nucleator and
polymerase MFs are still missing, blocked on design questions. In this repo,
94 rows on 50 reviewed genes use the affected terms. Most are ACCEPTed
process rows that would need a per-gene MF decision. That decision is what
the cross-linking and severing obsoletions are waiting for. Scoped, not
started.

## Upstream tickets

| Issue | Opened | Request | Last substantive comment | State in go-edit.obo |
|---|---|---|---|---|
| [go-ontology#18437](https://github.com/geneontology/go-ontology/issues/18437) | 2019-12-13 | severing as an MF | 2023-03-08 | MF GO:0003789, GO:0000513, GO:0140775 exist; BPs GO:0051014, GO:1903918-20, GO:0071846 still live |
| [go-ontology#18555](https://github.com/geneontology/go-ontology/issues/18555) | 2020-01-17 | obsolete GO:0030043 actin filament fragmentation | 2024-07-22 | still live |
| [go-ontology#18609](https://github.com/geneontology/go-ontology/issues/18609) | 2020-01-21 | NTR actin nucleator activity (Arp2/3, formins) | 2026-04-22 | no nucleator MF; GO:0140490 microtubule nucleator activity is the precedent |
| [go-ontology#19185](https://github.com/geneontology/go-ontology/issues/19185) | 2020-03-29 | NTR actin-filament cross-linking activity | 2026-04-20 | GO:7770064 created; BP GO:0051764 still live |
| [go-ontology#22594](https://github.com/geneontology/go-ontology/issues/22594) | 2021-12-17 | NTR actin polymerase activity (formins, Ena/VASP) | 2024-06-15 | no polymerase MF; GO:0061863 microtubule plus end polymerase activity is the precedent |

Term states were read from a go-ontology checkout of 2026-11-12. Thread
summaries are as of 2026-11-16. Nothing has been posted to these issues.

## Where the threads stand

- **Severing (#18437).** In 2022 an editor restored GO:0003789 and created
  GO:0000513 *actin severing activator activity* (for Aip1) and GO:0140775
  *actin filament debranching activity*. The editor then proposed obsoleting
  GO:0051014 *actin filament severing*, its three regulation terms and
  GO:0071846 *actin filament debranching*, but left the replacement line
  blank. PomBase later questioned whether the process should go, because Aip1
  promotes severing without being a severing protein: "Hmm, we might need to
  keep "actin severing" as a process too." (2023-03-08). A proposed "actin
  severing inhibitor activity" MF, for a disputed MYH9/gelsolin annotation,
  was never created.
- **Fragmentation (#18555).** This is mechanical: obsolete GO:0030043 (is_a
  GO:0030042 actin filament depolymerization) in favour of GO:0003789. It is
  labelled waiting for the notice period.
- **Cross-linking (#19185).** GO:7770064 exists, is_a GO:0008093 cytoskeletal
  adaptor activity. What remains is migrating the experimental rows on
  GO:0051764 *actin crosslink formation* and obsoleting that term. The editor
  asked for the reannotation list to move to an annotation-review ticket.
- **Nucleation (#18609).** PomBase proposed two MFs under GO:0140489
  molecular template activity (linear filament / branched filament actin
  nucleator activity). It asked whether the Arp2/3 activity belongs to the
  whole complex or to Arp2 and Arp3. Meanwhile GO-CAMs are using actin
  binding as a placeholder: "Currently, I fudged with existing annotation
  "actin binding" until such a term is available." (2026-03-25). No editor
  has answered the complex-versus-subunit question.
- **Polymerase (#22594).** PomBase argues formin and Ena/VASP activity is
  catalytic, not adaptor. An editor asked whether the polymerization BPs
  should instead collapse into actin cytoskeleton organization. Neither the
  parent nor the fate of GO:0030041 is settled. The capping BPs are in a
  related open obsoletion
  ([go-ontology#28151](https://github.com/geneontology/go-ontology/issues/28151)).

## What this repo already has

Rows in `existing_annotations` across all reviews, by action, computed
2026-11-16 with
[`term_actions.py`](GO_TRACKER_BACKLOG/term_actions.py). "Core in" counts
reviews naming the term in `core_functions`.

| Term | Rows | Genes | ACCEPT | KEEP_AS_NON_CORE | MODIFY | MARK_AS_OVER_ANNOTATED | REMOVE | UNDECIDED | Other | Core in |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| GO:0003789 actin filament severing activity | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  | 1 |
| GO:0051014 actin filament severing | 2 | 2 | 1 | 0 | 0 | 0 | 1 | 0 |  | 1 |
| GO:1903919 negative regulation of actin filament severing | 3 | 1 | 0 | 0 | 0 | 3 | 0 | 0 |  | 0 |
| GO:0071846 actin filament debranching | 4 | 2 | 4 | 0 | 0 | 0 | 0 | 0 |  | 2 |
| GO:0030043 actin filament fragmentation | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  | 0 |
| GO:7770064 actin-filament cross-linking activity | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |  | 1 |
| GO:0051764 actin crosslink formation | 10 | 7 | 7 | 1 | 0 | 0 | 0 | 1 | NEW 1 | 4 |
| GO:0051017 actin filament bundle assembly | 14 | 12 | 7 | 3 | 0 | 1 | 0 | 1 | NEW 2 | 5 |
| GO:0045010 actin nucleation | 2 | 2 | 0 | 0 | 1 | 0 | 0 | 0 | NEW 1 | 1 |
| GO:0034314 Arp2/3 complex-mediated actin nucleation | 16 | 5 | 16 | 0 | 0 | 0 | 0 | 0 |  | 5 |
| GO:0030041 actin filament polymerization | 21 | 17 | 10 | 6 | 3 | 2 | 0 | 0 |  | 5 |
| GO:0008154 actin polymerization or depolymerization | 12 | 9 | 3 | 1 | 4 | 3 | 0 | 1 |  | 1 |
| GO:0030042 actin filament depolymerization | 8 | 5 | 4 | 0 | 4 | 0 | 0 | 0 |  | 1 |
| GO:0051693 actin filament capping | 2 | 2 | 1 | 1 | 0 | 0 | 0 | 0 |  | 0 |

Total: 94 rows on 50 reviewed genes. GO:0000513, GO:0140775, GO:1903918,
GO:1903920 and GO:0070060 have no rows.

What stands out:

- **Our reviews accept the process terms GO wants to retire.** All 16 rows
  on GO:0034314 are ACCEPT across ARPC1B, ARPC4, ARPC5 and DROME SCAR and
  wash, and seven of ten GO:0051764 rows are ACCEPT, on FLNA, BAIAP2,
  BAIAP2L1 and DPYSL3. Under the
  [precomposition guidance](INVOLVED_IN_PRECOMPOSITION.md) these are the
  rows that should carry an MF instead, once one exists.
- **One review already uses GO:7770064 as a core MF** (human/ESPN), and
  human/AFAP1's review cites it as supported, so the cross-linking replacement
  has been exercised here. Likewise human/CFL2 already names GO:0003789 as its
  core MF while still accepting the GO:0051014 process row.
- **Cross-linking is the closest to done.** The experimental GO:0051764 rows
  are few. A reviewed list of which genes are true cross-linkers (MF
  GO:7770064) and which only bind filaments (GO:0051015) is the input the
  editor asked for.

## What gene review can and cannot settle

- **Can settle:** for each gene now carrying a severing, debranching,
  fragmentation or cross-linking process row, whether the gene product itself
  performs the activity (MF), regulates a partner that does (an activator or
  inhibitor MF), or acts upstream. This is the per-gene replacement mapping
  that #18437, #18555 and #19185 lack.
- **Can document:** the evidence for nucleator and polymerase activity on
  Arp2/3 subunits, formins and Ena/VASP proteins, as `proposed_new_terms`
  entries matching PomBase's draft definitions.
- **Cannot settle:** whether the Arp2/3 nucleator MF belongs to the complex or
  to subunits, the parent of an actin polymerase MF, or whether the
  polymerization BPs survive. These are editor decisions. Our output is
  evidence, not a resolution.

## Plan

### Re-check existing reviews (process rows that need an MF decision)

- [ ] human/FLNA, BAIAP2, BAIAP2L1, BAIAP2L2, DPYSL3; DROME/wash; and the
      mouse/Afap1l2 NEW row: GO:0051764, decide GO:7770064 vs GO:0051015
- [ ] human/CFL2 (GO:0051014 ACCEPT beside a GO:0003789 core MF), CAPG
      (GO:0051014 REMOVE), MYH9 (GO:1903919 marked over-annotated): severing
- [ ] human/GMFB, GMFG: GO:0071846, decide GO:0140775
- [ ] human/ARPC1B, ARPC4, ARPC5; DROME/SCAR, wash: GO:0034314, record nucleator
      evidence pending the NTR
- [ ] human/DIAPH1, DIAPH3; SCHPO/cdc12: GO:0030041, record polymerase evidence

### New reviews (genes named in the threads, not yet reviewed)

- [ ] Cross-linkers: human PLS1, PLS3, LCP1, ACTN1, ACTN4, FSCN1; yeast SAC6,
      SCP1; SCHPO fim1, ain1
- [ ] Severing and debranching: human CFL1, GSN, WDR1; yeast COF1, AIP1;
      SCHPO adf1
- [ ] Nucleators and polymerases: human ACTR2, ACTR3, ARPC2, ARPC3, VASP,
      ENAH, FMN2; SCHPO for3, fus1

### Deliverable

A per-gene table (gene, current process row, proposed MF, evidence) for the
cross-linking and severing rows, kept in this project folder and offered to
the issue owners. Nothing is posted to the tracker without a decision by the
project lead.

## STATUS

- 2026-11-16: project scoped from the GO tracker backlog. No reviews started.

## NOTES

### 2026-11-16

- Created from the [GO tracker backlog](GO_TRACKER_BACKLOG.md). Threads read
  in full. Term states checked against go-edit.obo (checkout 2026-11-12).
- GO:0003789 carries an EXACT synonym "actin depolymerizing activity", which
  sits oddly with a severing definition. Worth raising if severing rows are
  migrated.
- `genes/yeast/FMN1` is riboflavin kinase, not a formin. Do not queue it
  here.
