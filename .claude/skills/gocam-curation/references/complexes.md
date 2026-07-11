# Complexes

How a protein complex's activity is attributed determines whether the model is
informative. A mismatch is QC flag `COMPLEX_SUBUNIT_REPRESENTATION`.

## Three cases

1. **Known active subunit** — when one subunit carries the catalytic/transport/
   binding activity, represent **that specific gene product** as `enabled_by`,
   not the complex. (e.g. attribute the kinase activity to the catalytic
   subunit, not the holoenzyme.)
2. **Unknown active subunit** — when the activity cannot be attributed to a
   specific subunit, use the **GO complex term** as the enabler.
3. **Shared / multi-subunit activity** — when several subunits genuinely
   contribute to the activity, represent the relevant contributing subunits.

## How this maps to our model representation

In our module schema, a complex is a `ProteinComplexDescriptor`; role-bearing
components surface via `active_units`. When grounding a module annoton in a
GO-CAM activity, prefer the GO-CAM that attributes the activity to the correct
subunit (case 1) over one that uses the bare complex term, unless the subunit is
genuinely unknown.

## Check

- Is the activity attributed to the subunit that actually performs it?
- If the complex term is used, is that because attribution is truly unclear (OK)
  or because the curator defaulted to it (flag it)?
