# SLC43A3 (ENBT1) review notes

## Family-overturning nucleobase argument
- Despite sequence classification within the SLC43 "system-L" amino acid transporter family
  (with LAT3/LAT4), SLC43A3 is NOT an amino acid transporter. It is a Na+/H+-independent,
  facilitative, purine-selective nucleobase transporter for adenine, guanine and hypoxanthine
  [PMID:26455426 "SLC43A3 expressed in MDCKII cells mediated the uptake of purine nucleobases such as adenine, guanine, and hypoxanthine without requiring typical driving ions such as Na(+) and H(+), but it did not mediate the uptake of nucleosides"].
- It explicitly does not transport amino acids
  [PMID:26455426 "supporting a previous study indicating that SLC43A3 expression did not induce any amino acid transport activity in Xenopus oocytes"].
- Core MF therefore set to purine nucleobase transmembrane transporter activity (GO:0005345), not
  an amino-acid transporter term. Basolateral/sinusoidal hepatocyte localization is directly shown.
- Thiopurine (6-MP/azathioprine) transport is a genuine secondary (xenobiotic) activity kept non-core
  [PMID:30910793 "both variants of ENBT1 are key players in the transfer of 6-MP into and out of cells"],
  mirroring how a secondary/promiscuous activity is handled.
- Fatty-acid transporter activity rows (IEA/ISS) marked over-annotated: they trace to a mouse
  By-similarity "May regulate FA transport in adipocytes" note, a putative regulatory role, not a
  demonstrated transporter activity.

## Decisions
- Item-1 action framework (2026-11-14 ruling) recorded for the batch: generic substrate-named
  amino-acid parent terms treated as ACCEPT; only bare transmembrane-transport/transporter/solute
  parents TOO_GENERAL. (SLC43A3 carries no such amino-acid parent rows; its core review was not
  altered.)
- Added reference_review to the GO_REF references.
