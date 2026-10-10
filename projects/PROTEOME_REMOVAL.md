---
title: "UniProt Proteome Removal Impact Assessment"
maturity: IN_PROGRESS
tags: [PIPELINE]
species: [9INFA, PSEAI, ACEPA, RUMJO, ECO57, ANOGA, NITRP, CERSP, PSEEN, CLOCL, 9CAUD]
genes: [M2, merB, xdhB, fae1A, stx2A, PGRPS3, PGRPS2, amoA, dorR, Q1IFG0, Q6DTY2, Q9RGE6, Q9RGE7, Q9RGE8, darB]
last_reviewed: 2026-10-05
sidecars:
  slide_figures:
    - PROTEOME_REMOVAL/slides/removal-flow.svg
    - PROTEOME_REMOVAL/slides/removal-status.svg
manifest:
  slides:
    - href: PROTEOME_REMOVAL/slides/PROTEOME_REMOVAL-slides.html
      description: AI generated
---

# UniProt Proteome Removal Impact Assessment

**Bottom line:** UniProt planned to drop about 58M unreviewed (TrEMBL)
entries from redundant and non-reference proteomes by release 2026_02,
archiving them in UniParc, which would leave any gene review keyed on one of
those accessions pointing at an entry that no longer exists. We downloaded
UniProt's explicit removal list and on 2026-02-03 checked all 896 UniProt
IDs then in the repo against it:
15 reviews, all non-model microbes, phage, influenza and mosquito proteins,
were on the list. None of the 15 has been fixed or archived yet. A lookup
against the UniProt REST API on 2026-10-05 shows five of them now return
`entryType: Inactive` (PSEAI merB, ACEPA xdhB, RUMJO fae1A, ECO57 stx2A,
PSEEN Q1IFG0) and the other ten still return active TrEMBL entries. The repo
has since grown to 5,630 gene folders, so the February scan no longer covers
it and should be re-run; the `just` targets listed under Tooling are not in
the current justfiles and would need to be restored first. Follow-up is
tracked in [#4003](https://github.com/ai4curation/ai-gene-review/issues/4003).

We did this because a review's primary key is its UniProt accession: when
the entry disappears, `just fetch-gene` and the validators can no longer
refresh the review, and the curated judgement is stranded.

## Overview

UniProt is removing TrEMBL entries from non-Reference Proteomes by release 2026_02.

**Sources:**

- Protein removal list: https://ftp.ebi.ac.uk/pub/contrib/UniProt/proteomes/proteins_to_remove_from_UniProtKB.txt
- Proteins retained: https://ftp.ebi.ac.uk/pub/contrib/UniProt/proteomes/proteins_retained_in_UniProtKB.txt
- Help doc: https://www.uniprot.org/help/proteome_redundancy

**What happens:**

- TrEMBL entries from "Redundant Proteomes" and "Other Proteomes" will be **removed from UniProtKB**
- They will be **archived in UniParc** (still accessible via UniParc, but not in UniProtKB)
- SwissProt entries are NOT affected
- ~253M entries dropping to ~141M entries (~58M being removed)

## Impact Summary

**VERIFIED against `proteins_to_remove_from_UniProtKB.txt` (58M entries):**

We have **15 entries** that WILL BE REMOVED from UniProtKB.

## Entries Being Removed

| UniProt ID | Gene | Organism | Review File |
|------------|------|----------|-------------|
| `A0A1S7IWC7` | M2 | Influenza A | 9INFA/M2 |
| `A0A1V0M5B3` | merB | Pseudomonas aeruginosa | PSEAI/merB |
| `A0A1Y0Y121` | xdhB | Acetobacter pasteurianus | ACEPA/xdhB |
| `A0A2Z5TSL2` | fae1A | Ruminiclostridium josui | RUMJO/fae1A |
| `A0A9Q6Z964` | stx2A | E. coli O157:H7 | ECO57/stx2A |
| `D2STP8` | PGRPS3 | Anopheles gambiae | ANOGA/PGRPS3 |
| `D2SU82` | PGRPS2 | Anopheles gambiae | ANOGA/PGRPS2 |
| `D9J262` | amoA | Nitrobacter sp. | NITRP/amoA |
| `O30741` | dorR | Cereibacter sphaeroides | CERSP/dorR |
| `Q1IFG0` | Q1IFG0 | Pseudomonas entomophila | PSEEN/Q1IFG0 |
| `Q6DTY2` | Q6DTY2 | Clostridium cellulovorans | CLOCL/Q6DTY2 |
| `Q9RGE6` | Q9RGE6 | Clostridium cellulovorans | CLOCL/Q9RGE6 |
| `Q9RGE7` | Q9RGE7 | Clostridium cellulovorans | CLOCL/Q9RGE7 |
| `Q9RGE8` | Q9RGE8 | Clostridium cellulovorans | CLOCL/Q9RGE8 |
| `Q9XJG2` | darB | Bacteriophage | 9CAUD/darB |

### Action Required

- **Todo:** Find alternative entries or archive affected reviews
  ([#4003](https://github.com/ai4curation/ai-gene-review/issues/4003))
- **Todo:** Consider if UniParc references are acceptable for these use cases
  ([#4003](https://github.com/ai4curation/ai-gene-review/issues/4003))

## Tooling

Download the removal list and check entries:

```bash
just fetch-uniprot-removal-list       # Download ~578MB file to cache/uniprot/
just check-uniprot-removal ID1 ID2    # Check specific IDs
just check-all-uniprot-removal        # Check all gene reviews
```

---
# STATUS

- **Done:** Download protein removal list (58M entries, 578MB)
- **Done:** Set up cache directory and just targets
- **Done:** Comprehensive check of all 896 gene review UniProt IDs
- **Done:** Identify 15 entries being removed
- **Todo:** Find alternative entries or archive affected reviews
  ([#4003](https://github.com/ai4curation/ai-gene-review/issues/4003))

# NOTES

## 2026-02-03

### Methodology

1. Downloaded `proteins_to_remove_from_UniProtKB.txt` (578MB, 58M entries)
2. Created `cache/uniprot/` directory (gitignored)
3. Added just targets for automated checking
4. Extracted all 896 UniProt IDs from gene reviews
5. Used `LC_ALL=C comm -12` for fast intersection (locale matters for sort order!)
6. Found 15 entries in removal list

### Lessons Learned

- Proteome-based inference is unreliable - use the explicit protein removal list
- Sort locale matters: must use `LC_ALL=C` for consistent results with comm
- The removal list is already sorted (alphanumeric), so comm is O(n) - much faster than grep

### Full Verification Output

```
$ just check-all-uniprot-removal
Found 896 unique UniProt IDs in our reviews
Checking against removal list (58M entries)...

Entries being removed from UniProtKB:
  A0A1S7IWC7: 9INFA/M2
  A0A1V0M5B3: PSEAI/merB
  A0A1Y0Y121: ACEPA/xdhB
  A0A2Z5TSL2: RUMJO/fae1A
  A0A9Q6Z964: ECO57/stx2A
  D2STP8: ANOGA/PGRPS3
  D2SU82: ANOGA/PGRPS2
  D9J262: NITRP/amoA
  O30741: CERSP/dorR
  Q1IFG0: PSEEN/Q1IFG0
  Q6DTY2: CLOCL/Q6DTY2
  Q9RGE6: CLOCL/Q9RGE6
  Q9RGE7: CLOCL/Q9RGE7
  Q9RGE8: CLOCL/Q9RGE8
  Q9XJG2: 9CAUD/darB

Summary: 15 will be removed, 881 safe
```
