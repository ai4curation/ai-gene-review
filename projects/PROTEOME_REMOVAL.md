# UniProt Proteome Removal Impact Assessment

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
| A0A1S7IWC7 | M2 | Influenza A | 9INFA/M2 |
| A0A1V0M5B3 | merB | Pseudomonas aeruginosa | PSEAI/merB |
| A0A1Y0Y121 | xdhB | Acetobacter pasteurianus | ACEPA/xdhB |
| A0A2Z5TSL2 | fae1A | Ruminiclostridium josui | RUMJO/fae1A |
| A0A9Q6Z964 | stx2A | E. coli O157:H7 | ECO57/stx2A |
| D2STP8 | PGRPS3 | Anopheles gambiae | ANOGA/PGRPS3 |
| D2SU82 | PGRPS2 | Anopheles gambiae | ANOGA/PGRPS2 |
| D9J262 | amoA | Nitrobacter sp. | NITRP/amoA |
| O30741 | dorR | Cereibacter sphaeroides | CERSP/dorR |
| Q1IFG0 | Q1IFG0 | Pseudomonas entomophila | PSEEN/Q1IFG0 |
| Q6DTY2 | Q6DTY2 | Clostridium cellulovorans | CLOCL/Q6DTY2 |
| Q9RGE6 | Q9RGE6 | Clostridium cellulovorans | CLOCL/Q9RGE6 |
| Q9RGE7 | Q9RGE7 | Clostridium cellulovorans | CLOCL/Q9RGE7 |
| Q9RGE8 | Q9RGE8 | Clostridium cellulovorans | CLOCL/Q9RGE8 |
| Q9XJG2 | darB | Bacteriophage | 9CAUD/darB |

### Action Required

- [ ] Find alternative entries or archive affected reviews
- [ ] Consider if UniParc references are acceptable for these use cases

## Tooling

Download the removal list and check entries:

```bash
just fetch-uniprot-removal-list       # Download ~578MB file to cache/uniprot/
just check-uniprot-removal ID1 ID2    # Check specific IDs
just check-all-uniprot-removal        # Check all gene reviews
```

---
# STATUS

- [x] Download protein removal list (58M entries, 578MB)
- [x] Set up cache directory and just targets
- [x] Comprehensive check of all 896 gene review UniProt IDs
- [x] Identify 15 entries being removed
- [ ] Find alternative entries or archive affected reviews

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
