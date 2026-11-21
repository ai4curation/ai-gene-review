# XRCC6 notes

## 2026-11-21

Deep-research providers were not available in this checkout. `just deep-research-falcon
human XRCC6 --fallback perplexity-lite` reported that only `claude_code` was available,
and `just deep-research human XRCC5 claude-code --timeout 300` confirmed that the
Claude Code provider was not logged in. This review therefore uses the fetched GOA rows,
UniProt, cached publications, PANTHER/PAINT files, and the existing
`modules/nonhomologous_end_joining.yaml` review.

PTHR12604 holds the eukaryotic Ku70 and Ku80 subunits. In the reviewed human
Swiss-Prot set, XRCC6 is Ku70 in PTHR12604:SF5 and XRCC5 is Ku80 in
PTHR12604:SF4. They form the Ku70:Ku80 ring that binds broken DNA ends, recruits
DNA-PKcs, and promotes classical NHEJ. Ku also binds telomeric DNA, contributes
to telomere maintenance, and has smaller reported cytosolic DNA-sensing and
RNA-processing roles.

PAINT places five positive assertions at the PTHR12604 root node PTN000288287:
Ku70:Ku80 complex, double-stranded DNA binding, telomeric repeat DNA binding,
telomere maintenance, and NHEJ. The only loss rows in the fetched PAINT slice
sit on Drosophila node PTN000288402. `just paint-losses human XRCC6` reported
no IRD/IKR loss on the human XRCC6 lineage, so the human IBA rows are retained.

Review calls:

- Retain the Ku heterodimer, DNA end-binding, telomeric-repeat binding, NHEJ, and
  classical NHEJ rows as XRCC6 core biology.
- Retain ATPase, DNA helicase, and AP lyase rows as real but non-core
  biochemical activities; the 1997 separate-subunit paper assigns the helicase
  to Ku70 and the 2010 lyase paper showed Ku70 and Ku80 adducted to AP-site DNA.
- Mark generic DNA-damage-response and irradiation-response process rows as
  over-annotated when they describe downstream consequences of disabling Ku
  rather than a direct molecular step performed by Ku.
- Keep or mark peripheral transcription and cytosolic DNA-sensing rows as
  non-core. Those contexts do not alter the family conclusion that PAINT's
  conserved root functions are the Ku70:Ku80 complex and its direct DNA-binding
  contributions to NHEJ and telomere maintenance.
- Remove the imported `GO:0005515` physical-interaction rows under the repo's
  generic protein-binding policy.
