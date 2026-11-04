# ureF (Q09065, H. pylori 26695) - curation notes

Deep research: unavailable. One attempt (`just deep-research HELPY ureG --provider
perplexity`, 2026-10-23) failed - the checkout only has `falcon` and `openscientist`
providers. No `-deep-research-*.md` was written. Sources below are cached publications
(several fetched for this review with `just fetch-pmid`) and the UniProt record.

## Role in the pathway

UreF partners UreH (the UreD ortholog) to build the platform that recruits UreG:

- UreF-UreH crystal structure: complex formation orders the UreF C-terminal tail (Arg250) and
  uncoils the first turn of helix alpha2 to expose Tyr48; R250A and Y48A both abolish
  UreG-UreF-UreH formation and urease maturation [PMID:22013070 "Substitution of R250A or
  Y48A in UreF abolishes the formation of the heterotrimeric complex of UreG-UreF-UreH and
  abolishes urease maturation."].
- (UreG/UreF/UreH)2 structure: UreF and UreH facilitate UreG dimerization and juxtapose the
  two Cys66-Pro67-His68 motifs into one nickel site; a dimerization-interface UreF variant
  (R179A/Y183D) still binds UreH but cannot activate urease in vivo
  [PMID:24115911 "homodimerization of the UreF/UreH complex is essential for the recruitment
  of two copies of UreG to form the (UreG/UreF/UreH)2 complex and urease maturation"].
- Nickel-charged UreG activates apo-urease only in the presence of UreF/UreH
  [PMID:24115911 "We found that the nickel-charged UreG dimer can activate urease only in the
  presence of the UreF/UreH complex (Figure 7A)."]. This is literally the GO:0018237
  definition ("Increases the activity of urease by promoting the incorporation of nickel into
  the active site").
- ureF is required for urease activity in the E. coli reconstitution [PMID:1313413].

## The nickel-binding row

`GO:0016151` (UniRule) was initially a REMOVE candidate by analogy with genes/PSEPK/ureF, but
there *is* a statement that H. pylori UreF binds nickel by ITC
[PMID:26401965 "HpUreF was structurally characterized25 and isothermal titration calorimetry
demonstrates it binds nickel,26 although the functional relevance of metal binding was not
tested."]. Since no nickel site appears in either H. pylori structure and the measured metal
load of the preactivation complex is on the UreG dimer interface, the row is kept as
KEEP_AS_NON_CORE rather than removed. If the PSEPK ureF review is re-touched, the same
evidence should be weighed there.

## Decisions

- Four bare `GO:0005515` rows (partners UreH x3, UreG x1): MODIFY to `GO:0018237 urease
  activator activity`, which is what the UreF-UreH and UreF-UreG contacts accomplish.
- `GO:0008152 metabolic process` (IMP, PMID:1313413): MODIFY to `GO:0043419`.
- `GO:0018237` (IBA, node PTN008658147, Arabidopsis UreF donor): ACCEPT, core.
- `GO:0019627`: MODIFY to `GO:0043419` with a `propagation_review` recording that the node
  transfer is sound and only the granularity is at issue.
- `GO:0150006 urease activator complex` added as NEW (IDA, PMID:24115911) - the term's
  definition ("Activator subunits dissociate before urease has catalytic function") describes
  the (UreG-UreF-UreH)2 complex exactly, and no H. pylori subunit carried it.
