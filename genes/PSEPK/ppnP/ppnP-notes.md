# ppnP curation notes

## 2026-08-19

- Replaced the earlier `GO:0009164 nucleoside catabolic process` proposal with
  `GO:0043101 purine-containing compound salvage`. PpnP phosphorolyzes diverse
  purine nucleosides to reusable bases, but the reversible reaction and current
  KT2440 evidence do not establish a strictly catabolic physiological direction
  [file:PSEPK/ppnP/ppnP-uniprot.txt "Catalyzes the phosphorolysis of diverse
  nucleosides, yielding"; file:PSEPK/ppnP/ppnP-deep-research-falcon.md
  "downstream of nucleoside uptake, producing bases and ribose-1-phosphate for
  reuse"].
- The salvage process is attached only to the purine-phosphorylase core function;
  the pyrimidine activity remains outside the purine-salvage module boundary.
- OpenScientist recovered structural and biochemical work on bacterial PpnP
  orthologs but no direct KT2440 enzymology [file:PSEPK/ppnP/ppnP-deep-research-openscientist.md
  "No direct enzymology on the *P. putida* protein."]. The Q88F51 assignment
  therefore remains a strong family inference rather than organism-specific
  experimental evidence.

## 2026-10-05 review follow-up

The pyrimidine half of PpnP's broad substrate range is now explicitly linked to
`GO:0008655 pyrimidine-containing compound salvage`. The earlier
purine-module-boundary rationale was too narrow for the standalone gene review:
Q88F51 can phosphorolyze uridine, cytidine, and thymidine, releasing free
pyrimidine bases for salvage [file:PSEPK/ppnP/ppnP-uniprot.txt "Can use
uridine,"; file:PSEPK/ppnP/ppnP-deep-research-falcon.md "downstream of
nucleoside uptake, producing bases and ribose-1-phosphate for reuse"].
