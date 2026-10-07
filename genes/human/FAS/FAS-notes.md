# FAS (CD95/APO-1) Notes - ISOFORMS Project

## Key Isoform Biology

FAS is a classic example of **antagonistic membrane vs soluble isoforms**.

### Isoforms (7 named)

| Isoform | UniProt ID | Synonym | Key Feature | Function |
|---------|------------|---------|-------------|----------|
| Isoform 1 | P25445-1 | - | Full-length, membrane-bound | **INDUCES APOPTOSIS** |
| Isoform 2 | P25445-2 | del2, D | Lacks exons | Soluble, blocks apoptosis |
| Isoform 3 | P25445-3 | del3, E | Lacks exons | Soluble, blocks apoptosis |
| Isoform 4 | P25445-4 | B | - | Soluble, blocks apoptosis |
| Isoform 5 | P25445-5 | C | - | Soluble, blocks apoptosis |
| **Isoform 6** | P25445-6 | TMdel, A | **Lacks TM domain** | Soluble, **BLOCKS APOPTOSIS** |
| Isoform 7 | P25445-7 | FasExo8Del | - | Unknown |

### Critical Antagonism: Membrane vs Soluble

**Membrane-bound FAS (Isoform 1)**:
- Contains transmembrane domain
- Forms DISC (Death-Inducing Signaling Complex)
- Recruits FADD and CASP8
- **TRIGGERS APOPTOSIS**

**Soluble FAS (Isoforms 2-6)**:
UniProt states:
> "The secreted isoforms 2 to 6 block apoptosis (in vitro)"

Mechanism: Soluble FAS acts as a **decoy receptor**, binding FasL without triggering apoptosis.

### Tissue-Specific Expression (UniProt)

> "Isoform 1 and isoform 6 are expressed at equal levels in resting peripheral blood mononuclear cells. After activation there is an increase in isoform 1 and decrease in the levels of isoform 6."

This suggests splicing regulation shifts towards the pro-apoptotic membrane form upon immune activation.

## GOA Annotation Status

- **96 total annotations**
- **NO isoform-specific annotations** (no P25445-X identifiers)
- All apoptosis annotations likely refer to membrane-bound isoform 1

## Expected Annotation Issues

1. **"Positive regulation of apoptotic process"** - TRUE for isoform 1, FALSE for isoforms 2-6
2. **"Negative regulation of apoptotic process"** - should be annotated for soluble isoforms!
3. **Death domain** - present in all, but only functional in membrane form

## Key References

- PMID:7533181, PMID:9184224 - Soluble FAS blocks apoptosis
- PMID:7575433 - Isoform expression patterns

## 2026-09-30 APOPTOSIS generic-binding cleanup

`just fetch-gene human FAS` appended 17 partner-specific `GO:0005515` rows
that were split out from IntAct/UniProt imports already represented by older
generic rows:

- Tightened canonical DISC-context rows with CASP8 or FADD support
  (PMIDs 11717445, 16498403, 17159907, 21382479, 21625644) to FAS
  `GO:0005031` receptor activity, matching the existing core function.
- Removed the NAS `cytosol` row sourced to PMID:7533181 because the paper
  supports secreted soluble FAS splice isoforms rather than cytosolic FAS.
- Left abstract-only rows `UNDECIDED` where the cached abstract did not verify
  the exact partner imported by IntAct: the TNFR1-specific PMID:12887920 row,
  the FADD/CASP8 rows from the CD95/Yes/PI3K glioblastoma paper
  (PMID:18328427), PMLRARalpha rows whose partners were not evident in
  PMID:21803845.
- Removed generic `protein binding` rows for non-core inhibitory cap proteins
  from PMID:18846110, the direct PMLRARalpha inhibitory interaction from
  PMID:21803845, the FADD/DAXX rows from the proximity-ligation screen
  (PMID:25241761), and the BioPlex AP-MS FAS-CASP8 row from PMID:33961781
  because none supports a more informative FAS-side molecular function.
