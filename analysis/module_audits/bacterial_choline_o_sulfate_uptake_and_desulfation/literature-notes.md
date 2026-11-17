# Choline-O-sulfate uptake and desulfation: comparative audit notes

## 2026-11-06 — boundary and evidence audit in progress

The existing module defines a two-step boundary: intact choline-O-sulfate (COS)
import followed by BetC-catalyzed hydrolysis. Retain this biochemical boundary and
Bacteria scope, while distinguishing organism-level pathway evidence from a
resolved gene assignment. Neither transport alone nor BetC alone demonstrates
the complete module. Downstream choline oxidation, osmoprotection and sulfur
assimilation are different outcomes, not interchangeable pathway readouts.

The pre-audit topology incorrectly required the Pseudomonas BetD/BetE candidates,
although its own prose said their cargo and physical association are unresolved.
Moreover, the original connection note overinterpreted a **betC** deletion as evidence for
transporters other than BetDE. BetD and BetE were not deleted in that experiment;
it shows transport without hydrolysis, not independence from BetDE.

### Comparative reviews

- **PMID:10717312**, Kertesz (2000), *Riding the sulfur cycle*. The review
  distinguishes sulfate-ester utilization as sulfur nutrition from metabolism
  of the carbon skeleton. Do not transfer sulfur-starvation regulation or an
  arylsulfatase substrate range wholesale onto BetC. The local cache currently
  contains its abstract; the publisher full-text request returned HTTP 403.
- **PMID:11421275**, Kertesz (2001), *Bacterial transporters for sulfate and
  organosulfur compounds*. This is historical comparative support for keeping
  transport distinct from intracellular conversion and for distinguishing
  transporter architectures. Its then-known sulfate-ester importers were ABC
  systems; that dated survey cannot prove every modern COS importer is ABC or
  turn SulP membership into cargo evidence. The cache is abstract-only.
- **PMID:23354714**, Wargo (2013), *Homeostasis and catabolism of choline and
  glycine betaine*. The review distinguishes accumulation for osmoprotection
  from nutrient catabolism and describes multiple transporter routes. It
  supports keeping downstream choline/betaine metabolism outside this module
  and treating transporter family membership separately from physiological
  cargo. The publication cache is abstract-only; the official PMC HTML was
  independently retrieved and the article text inspected (PMC3623244).

### Primary experimental distinctions

- **PMID:17116241**, KT2440: BetC deletion retains intact COS accumulation but
  loses its use as carbon/nitrogen. This is strong organism-level evidence for
  uptake and a separate hydrolytic role; it does not resolve importer identity.
- **PMID:21369825**, Pseudomonas sp. ATCC19151: BetD/PBP and BetE/STAS architecture
  is a candidate-locus observation, not a demonstrated transport complex or
  COS-specific uptake assay.
- **PMID:9736747**, Sinorhizobium: BetC-dependent hydrolysis supplies choline for
  downstream betaine synthesis. The genetic strain is 102F34, distinct from
  the 1021 reference protein and later recombinant experiments.
- **PMID:29458126**: purified Sinorhizobium 1021 BetC (O69787) directly establishes
  sulfatase chemistry. **PMID:35503214** instead used CECT 4857/MH208481. Its
  product-binding structures are homolog evidence unless identity is explicitly
  established; do not relabel them as measurements on the 1021 accession.
- **PMID:9925583**, Bacillus: OpuC directly imports COS, but the tested strains
  accumulate it intact and do not use it as carbon, nitrogen or sulfur. This
  is a useful positive transport / negative complete-module comparator, not an
  excuse to assign Bacillus a BetC pathway. The four OpuC subunits require
  separate contribution-aware reviews and an assembled-complex selector.
- **PMID:26058574**, Ruegeria DSS-3: selective COS-growth loss in the betC mutant
  grounds the marine hydrolysis exemplar. The betT mutant has a 38% reduction
  in COS growth and an 84% reduction in choline depletion. COS itself was not
  quantified in the uptake/depletion assay. These findings support a possible
  contribution without demonstrating direct COS transport by BetT.
- **PMID:40801533** labels BetT as a choline/COS transporter in a proposed
  pathway diagram, but the study primarily investigates transcriptional
  regulation. Assess that label against the earlier measurements; a diagram
  alone must not erase the unresolved cargo evidence. Locus mapping separates
  BetC-1/SPO1083 from the second BetC-like SPO2214 protein.

### Integration requirements

1. Require actual COS import and BetC hydrolysis, with cargo visible on the
   transport function. Generic transport activity alone cannot satisfy import.
2. Keep BetD/BetE and Ruegeria BetT as explicitly qualified candidates until
   direct cargo evidence is established. No invented complex or family ID.
3. Add the four reviewed Bacillus OpuC units as a resolved import implementation;
   its transport capacity must not imply native hydrolysis.
4. Keep an unresolved-importer role for organisms where the pathway is observed
   but the gene assignment remains open. Genomic incompleteness must not be
   reported as biological absence. Directly observed intact accumulation can support the
   role separately from a gene-based capacity test. Ruegeria COS growth is
   insufficient for that override because BetC location and intact uptake are
   unresolved.
5. Complete all ten member reviews, preserve machine payloads and raw/provider
   sources, validate the revised topology and evidence, then publish one module
   PR and shepherd its actual merge.

Module-focused Falcon research was attempted on 2026-11-06 and failed with
HTTP403 authentication. These are manual literature notes, not a provider report.
