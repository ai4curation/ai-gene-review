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
