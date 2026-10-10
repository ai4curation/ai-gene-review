---
title: "VAMPIROME"
maturity: IN_PROGRESS
last_reviewed: 2026-10-05
tags: [BIOLOGY_DOMAIN]
species: [DESRO]
genes: [K9IFT7, K9IFY6, K9IIP0, K9IJK6, K9IMD0, K9IUF6, K9IWC0, K9IWH5, K9IWR0, K9IWX5, K9IYM3, K9IZA2, K9J287, K9J2R0]
manifest:
  slides:
    - href: VAMPIROME/slides/VAMPIROME-slides.html
      description: VAMPIROME salivary modulators slides
---

# VAMPIROME

**Bottom line:** blood feeding requires a vampire bat to keep blood flowing at
the bite site, and the Vampirome salivary-gland study exposed a secretome
enriched for anticoagulants, protease inhibitors, candidate vasodilators, and
immune modulators. Working from the
Vampirome transcriptome and proteome study, we mapped the reported transcripts
to UniProt, found that *Desmodus rotundus* has no Swiss-Prot entries at all in
this set, picked a 13-protein shortlist on hemostasis and immune relevance, and
reviewed them plus draculin (K9IMD0). Across 14 reviewed proteins there are 136
annotation rows: 66 ACCEPT, 27 MODIFY, 21 MARK_AS_OVER_ANNOTATED, 8
KEEP_AS_NON_CORE, 7 UNDECIDED, 4 NEW and 3 REMOVE. The 13 Table 4 shortlist
proteins are all TrEMBL entries with only electronic GOA rows, while draculin
is a reviewed Swiss-Prot seed with direct experimental rows; the UNDECIDED and
over-annotated calls are the honest result for a project dominated by homology
transfer from experiments on other mammals. Twelve of the 14 reviewed proteins
have final descriptions and synthesized core functions; K9IUF6 and K9J2R0
still need description and core-function synthesis, and the `CALCA`/vCGRP seed
is not yet reviewed because a transcriptome search found no matching peptide.
Remaining DESRO work is tracked in
[#3994](https://github.com/ai4curation/ai-gene-review/issues/3994).

We did this because saliva proteins of blood-feeding animals are annotated
almost entirely by homology to their host counterparts, which imports the
host's biology wholesale. The C1-inhibitor homolog K9IYM3 is the clearest case:
its serpin ancestry brought peptidase activity and proteolysis, both removed,
and blood coagulation, hemostasis and fibrinolysis, all marked over-annotated.

## Overview

Project to curate vampire bat (Desmodus rotundus; UniProt code DESRO) salivary gland proteins that modulate host hemostasis and immunity, based on the Vampirome transcriptome/proteome study. This project cross-links with PARASITE_IMMUNE_MODULATORS for broader parasite immune modulators work.

## Sources and project files

- Table 4 extract: `projects/VAMPIROME/table4_extract.md`
- UniProt mapping table: `projects/VAMPIROME/uniprot_mapping.md`
- UniProt mapping JSON: `projects/VAMPIROME/uniprot_mapping.json`
- Candidate list JSON (UniProtKB reviewed vs TrEMBL split): `projects/VAMPIROME/uniprot_candidates.json`
- Related project: `projects/PARASITE_IMMUNE_MODULATORS.md`

## Reviewed seed gene (DESRO)

- Done: Draculin (Lactotransferrin; UniProt: K9IMD0)

## Unmapped DESRO peptide seeds

- Blocked: `CALCA`/vCGRP - peptide reported, but no matching DESRO transcript or
  UniProt accession has been found yet.

## Vampirome candidates (prioritize Swiss-Prot)

### Reviewed (Swiss-Prot)

None detected for DESRO in this candidate set (all mapped entries are UniProtKB unreviewed/TrEMBL).

### Reviewed priority shortlist

- Done: t-plasminogen activator (UniProt: K9IJK6; entry K9IJK6_DESRO; transcript BatTrinityAbyss-499018)
- Done: Kunitz-type protease inhibitor 2 (UniProt: K9IZA2; entry K9IZA2_DESRO; transcript BatTrinityAbyss-541822)
- Done: Putative plasma protease c1 inhibitor (UniProt: K9IYM3; entry K9IYM3_DESRO; transcript DrSigp-SigP-532391)
- Done: Deoxyribonuclease-1-like 1 (UniProt: K9J287; entry K9J287_DESRO; transcript BatTrinityAbyss-532109)
- Done: C-C motif chemokine (UniProt: K9IFY6; entry K9IFY6_DESRO; transcript BatTrinityAbyss-506850)
- Done: Lymphotoxin-alpha (UniProt: K9IWR0; entry K9IWR0_DESRO; transcript BatTrinityAbyss-86412)
- Done: Beta-defensin 1 (UniProt: K9IFT7; entry K9IFT7_DESRO; transcript BatTrinityAbyss-401005)
- Done: lysozyme (UniProt: K9IWH5; entry K9IWH5_DESRO; transcript BatTrinityAbyss-500942; gene LYZ)
- Done: Tumor necrosis factor-inducible gene 6 protein (UniProt: K9IIP0; entry K9IIP0_DESRO; transcript BatTrinityAbyss-527888)
- Done: A disintegrin and metalloproteinase with thrombospondin motifs 1 (UniProt: K9IUF6; entry K9IUF6_DESRO; transcript BatTrinityAbyss-517665; description/core synthesis pending)
- Done: C-type natriuretic peptide / NPPC (UniProt: K9IWC0; entry K9IWC0_DESRO; transcript BatTrinityAbyss-538594; UniProt currently misnames this entry Natriuretic peptides B)
- Done: Putative scp crisp: scp-like extracellular (UniProt: K9IWX5; entry K9IWX5_DESRO; transcript BatTrinityAbyss-495870)
- Done: Dipeptidyl peptidase 4 (UniProt: K9J2R0; entry K9J2R0_DESRO; transcript BatTrinityAbyss-561424; description/core synthesis pending)

### Full mapped TrEMBL candidate pool

All mapped DESRO candidates below are UniProtKB unreviewed (TrEMBL); several of
these accessions also appear in the reviewed priority shortlist above.

- 2-phosphoxylose phosphatase 1 (UniProt: K9IKM9; entry K9IKM9_DESRO; transcript BatTrinityAbyss-508800)
- 5'-nucleotidase domain-containing protein 1 (UniProt: K9IKC7; entry K9IKC7_DESRO; transcript BatTrinityAbyss-537653)
- A disintegrin and metalloproteinase with thrombospondin motifs 1 (UniProt: K9IUF6; entry K9IUF6_DESRO; transcript BatTrinityAbyss-517665)
- Acid sphingomyelinase-like phosphodiesterase (UniProt: K9IL01; entry K9IL01_DESRO; transcript BatTrinityAbyss-549118)
- Beta-defensin 1 (UniProt: K9IFT7; entry K9IFT7_DESRO; transcript BatTrinityAbyss-401005)
- C-C motif chemokine (UniProt: K9IFY6; entry K9IFY6_DESRO; transcript BatTrinityAbyss-506850)
- Deoxyribonuclease-1-like 1 (UniProt: K9J287; entry K9J287_DESRO; transcript BatTrinityAbyss-532109)
- Dipeptidyl peptidase 4 (UniProt: K9J2R0; entry K9J2R0_DESRO; transcript BatTrinityAbyss-561424)
- Epoxide hydrolase (UniProt: K9IKD6; entry K9IKD6_DESRO; transcript BatTrinityAbyss-508632)
- Kunitz-type protease inhibitor 2 (UniProt: K9IZA2; entry K9IZA2_DESRO; transcript BatTrinityAbyss-541822)
- Lymphotoxin-alpha (UniProt: K9IWR0; entry K9IWR0_DESRO; transcript BatTrinityAbyss-86412)
- Metalloproteinase inhibitor 1 (UniProt: K9IGJ9; entry K9IGJ9_DESRO; transcript BatTrinityAbyss-37180)
- Metalloproteinase inhibitor 3 (UniProt: K9IHC5; entry K9IHC5_DESRO; transcript BatTrinityAbyss-534229)
- C-type natriuretic peptide / NPPC (UniProt: K9IWC0; entry K9IWC0_DESRO; transcript BatTrinityAbyss-538594; UniProt currently misnames this entry Natriuretic peptides B)
- Putative alpha-1-antichymotrypsin (UniProt: K9IXP7; entry K9IXP7_DESRO; transcript BatTrinityAbyss-518161)
- Putative cystatin-m (UniProt: K9IWH8; entry K9IWH8_DESRO; transcript BatTrinityAbyss-41885)
- Putative disintegrin and metalloproteinase (UniProt: K9IZP9; entry K9IZP9_DESRO; transcript BatTrinityAbyss-521171)
- Putative iggfc-binding protein (UniProt: K9J450; entry K9J450_DESRO; transcript DrSigp-SigP-495835)
- Putative neuroserpin is a inhibitory member of (UniProt: K9J0L7; entry K9J0L7_DESRO; transcript BatTrinityAbyss-548577)
- Putative pituitary adenylate cyclase-activating (UniProt: K9IGD6; entry K9IGD6_DESRO; transcript BatTrinityAbyss-500584)
- Putative plasma protease c1 inhibitor (UniProt: K9IYM3; entry K9IYM3_DESRO; transcript DrSigp-SigP-532391)
- Putative salivary lipocalin (UniProt: K9IRT4; entry K9IRT4_DESRO; transcript BatTrinityAbyss-466603)
- Putative salivary lipocalin (UniProt: K9IHB8; entry K9IHB8_DESRO; transcript BatTrinityAbyss-495622)
- Putative salivary lipocalin (UniProt: K9IWR5; entry K9IWR5_DESRO; transcript BatTrinityAbyss-495624)
- Putative salivary lipocalin (UniProt: K9IQU6; entry K9IQU6_DESRO; transcript BatTrinityAbyss-495626)
- Putative salivary lipocalin (UniProt: K9IWP0; entry K9IWP0_DESRO; transcript BatTrinityAbyss-495631)
- Putative salivary lipocalin (UniProt: K9IYU4; entry K9IYU4_DESRO; transcript BatTrinityAbyss-496761)
- Putative scp crisp: scp-like extracellular (UniProt: K9IWX5; entry K9IWX5_DESRO; transcript BatTrinityAbyss-495870)
- Putative secreted mucin (UniProt: K9IGW6; entry K9IGW6_DESRO; transcript DrSigp-SigP-36965)
- Putative secreted protein precursor (UniProt: K9IFW5; entry K9IFW5_DESRO; transcript BatTrinityAbyss-36340)
- Putative serpin (UniProt: K9IJG1; entry K9IJG1_DESRO; transcript BatTrinityAbyss-25903)
- Serpin B6 (UniProt: K9J5D5; entry K9J5D5_DESRO; transcript BatTrinityAbyss-543253)
- Tumor necrosis factor-inducible gene 6 protein (UniProt: K9IIP0; entry K9IIP0_DESRO; transcript BatTrinityAbyss-527888)
- lysozyme (UniProt: K9IWH5; entry K9IWH5_DESRO; transcript BatTrinityAbyss-500942; gene LYZ)
- t-plasminogen activator (UniProt: K9IJK6; entry K9IJK6_DESRO; transcript BatTrinityAbyss-499018)

## Unmapped Vampirome transcripts (no TSA/UniProt hit yet)

- vCGRP (calcitonin gene-related peptide-like; vasodilatory peptide). Reported peptide sequence:
  SCNTATCVTHRLAGLLSRSGGVVSSDFTPTDTGSNSY (Toxins 2019, Kakumanu et al.). Mapping to
  DESRO transcript/UniProt pending.
- BatTrinityAbyss-321620
- BatTrinityAbyss-429618
- BatTrinityAbyss-489254
- BatTrinityAbyss-499100
- BatTrinityAbyss-499228
- BatTrinityAbyss-500441
- BatTrinityAbyss-509950
- BatTrinityAbyss-523646
- BatTrinityAbyss-8258
- DrSigp-SigP-210264

---
# STATUS

## 2026-01-21

- Done: Create Vampirome project structure and cross-link to PARASITE_IMMUNE_MODULATORS
- Done: Import Table 4 extract and UniProt mapping artifacts
- Done: Build candidate list with Swiss-Prot prioritization (none found)
- Done: Select priority shortlist (13 candidates)
- Todo: Expand seed list with any additional vampire bat modulators supplied by user
- Done: Fetch UniProt/GOA data for prioritized candidates
- Done: Deep research (falcon) for 13 shortlisted candidates
- Done: Review existing annotations (annotation-reviewer)
- Todo: Synthesize top-level descriptions and core functions for K9IUF6 and K9J2R0 (12/14 complete)

## 2026-01-22

- Done: Add core_functions and descriptions for Draculin and three priority candidates
- Done: Add deep-research support snippets for core functions where available
- Done: Create notes files for Draculin (K9IMD0), K9IZA2, K9IYM3, and K9J287
- Done: Create notes files for remaining shortlist candidates (K9IJK6, K9IFY6, K9IWR0, K9IFT7, K9IWH5, K9IIP0, K9IUF6, K9IWC0, K9IWX5, K9J2R0)

# NOTES

## 2026-01-21

- Created VAMPIROME project and moved Vampirome artifacts into `projects/VAMPIROME/`.
- UniProt mapping indicates all current DESRO candidates are UniProtKB unreviewed (TrEMBL); no Swiss-Prot entries detected.
- Cross-link with `projects/PARASITE_IMMUNE_MODULATORS.md` added.
- Selected a 13-gene priority shortlist focused on hemostasis/immune modulation and fetched UniProt/GOA data (K9IJK6, K9IZA2, K9IYM3, K9J287, K9IFY6, K9IWR0, K9IFT7, K9IWH5, K9IIP0, K9IUF6, K9IWC0, K9IWX5, K9J2R0).
- Falcon deep-research completed for all 13 shortlisted candidates; needed extended timeouts for some runs.
- Completed annotation review for Draculin (K9IMD0 / LTF).
- Completed annotation reviews for K9IJK6, K9IZA2, K9IYM3, K9J287, and K9IWR0.
- Completed annotation reviews for K9IFT7, K9IWH5, K9IIP0, K9IUF6, and K9IWC0.
- Completed annotation reviews for K9IWX5 and K9J2R0.

## 2026-01-22

- Added core_functions/description edits for Draculin (K9IMD0), K9IZA2, K9IYM3, and K9J287.
- Added deep-research support snippets for core functions where available.
- Created notes files for K9IMD0, K9IZA2, K9IYM3, and K9J287.
- Created notes files for remaining shortlisted candidates (K9IJK6, K9IFY6, K9IWR0, K9IFT7, K9IWH5, K9IIP0, K9IUF6, K9IWC0, K9IWX5, K9J2R0).
- Started `CALCA`/vCGRP mapping via transcriptome search; no peptide matches in RefSeq or TSA GABZ01 (see `CALCA-bioinformatics` RESULTS).
