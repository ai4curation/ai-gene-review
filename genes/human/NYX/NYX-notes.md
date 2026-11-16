# NYX (nyctalopin, Q9GZU5) review notes

Session 2026-11-16, DISMECH vision-alignment campaign (complete CSNB).

## Biology (with provenance)

- Class IV small leucine-rich proteoglycan (SLRP), 11 LRRs flanked by cysteine-rich caps; human protein
  predicted GPI-anchored [PMID:11062471 "NYX, which encodes a glycosylphosphatidyl (GPI)-anchored protein called nyctalopin"];
  the only SLRP anchored to the plasma membrane, transmembrane in mouse
  [PMID:25701227 "It is the only member of this family that is GPI-anchored to plasma membrane"; "in the mouse eye, nyctalopin is a transmembrane SLRP rather than anchored via GPI"].
- X-linked complete CSNB (CSNB1A), ON-pathway defect [PMID:11062471]; mouse nob is an 85-bp Nyx deletion
  [PMID:12506099].
- Postsynaptic requirement: nob DBCs fail to respond to glutamate; EYFP-nyctalopin on DBC dendritic tips
  rescues [PMID:17881478] (mouse).
- Binds TRPM1 directly and is required for TRPM1 on DBC dendrites; proposed accessory subunit
  [PMID:21734298] (mouse). Reported to bind mGluR6 too (review PMID:25701227; primary paper not cached).
- No catalytic, channel or receptor activity is known.

## Decisions summary

- Signaling receptor activity IBA (LRR receptor node) removed: no evidence nyctalopin transduces a signal.
- ECM IBA over-annotated; interstitial gel rows removed (their own TAS source says nyctalopin is the
  membrane-anchored exception among SLRPs).
- No GO MF fits a non-catalytic accessory/scaffold protein without inventing a function; core function
  left at process level: protein localization to postsynaptic membrane (TRPM1), plus visual perception.
  Added NEW ISS rows for that process and for external side of plasma membrane.
