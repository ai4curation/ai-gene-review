# PGL-1 motif and domain audit, 2026-09-21

The report's two strict motif patterns also fail on its chosen GLH-1 positive control.
PGL-1 lacks all five tested patterns, including versions allowing the actual GLH-1
residues. This supports a difference from the conventional DEAD-box architecture;
it is not a direct negative RNA-unwinding assay or proof that every ATP-binding
mechanism is absent.

## Recomputed sequence results

Inputs are exact UniProt JSON records for C. elegans PGL-1 Q9TZQ3 (730 aa) and
GLH-1 P34689 (763 aa). `motif-results.json` contains all coordinates, input hashes,
and patterns; `source-provenance.json` records retrieval URLs and times.

| Pattern | PGL-1 | GLH-1 |
| --- | --- | --- |
| Report `G....GK[TS]` | no match | no match |
| Report `DEAD` or `DE.H` | no match | DEAD, 499–502 |
| Report `Q..GR.GR` | no match | no match |
| Audit `[HQ]..GR.GR` | no match | HRIGRTGR, 692–699 |
| Audit `[AG]....GK[TS]` | no match | AQTGSGKT, 385–392 |

The report gave approximately correct control coordinates but overspecified the
amino-acid patterns at their starts. Allowing these observed variants recovers the
control sites. A short regex scan is not an alignment or profile-HMM test, and a
negative result is not a mapped catalytic-residue loss claim. The motifs are neither
an exhaustive catalog of helicase families nor sufficient by themselves to establish
activity in any protein.

## Independently inspected InterPro scope

The complete target response contains five signatures and no next page. Its PGL_N
Pfam match PF29800/IPR062035 covers 10–211 (score 4.1e-75), and PGL_C
PF29799/IPR062036 covers 220–448 (score 1.4e-104). PTHR23237, officially named
H/ACA Ribonucleoprotein Complex Subunit GAR1, covers only residues 629–728
(score 0.00072), an RGG-rich C-terminal segment. These are the reported source scores,
not scores recalculated here or directly compared across search methods.

The GAR1 match is a partial tail match, not evidence that the whole protein has been
reclassified as GAR1. No GAR1 biological role is inferred. The independently saved
PAINT tree still places exact Q9TZQ3 beneath positive helicase/splicing/export nodes;
see ../pgl-1-paint-lineage.json and ../pgl-1-paint-lineage.md. This domain audit does not
identify a misgraft or establish a new phylogeny. It narrows the resource discrepancy
that a PAINT curator needs to inspect against the alignment and target identity.

The control has conventional DEAD and helicase-C Pfam matches (365–544 and 605–701)
and a PTHR47958 match at 290–737. Both control InterPro pages are saved. The target's
experimentally characterized domains are addressed in ../pgl-1-report-assessment.md;
no newly predicted structure or target/comparator residue alignment was performed here.

## Checklist

- [x] Scripts have no hardcoded sequence inputs, outputs or biological conclusions;
  input accessions/files and patterns are explicit parameters.
- [x] The motif script ran on the independent GLH-1 control as well as PGL-1.
- [x] Analysis completed; strict-pattern control failures are reported, not hidden.
- [x] Exact downloaded inputs, provenance, executable scripts and computed output are saved.
- [x] The interpretation states method scope, source provenance and remaining uncertainty.

Activity and phylogenetic placement remain inconclusive; the reproducible result is
limited to the specified patterns and the inspected database-match coordinates.
