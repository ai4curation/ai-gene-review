# ureH (Q09067, H. pylori 26695) - curation notes

Deep research: unavailable in this checkout. `just deep-research HELPY ureG --provider
perplexity` was attempted once (2026-10-23) and failed ("Provider 'perplexity' not available.
Available: falcon, openscientist"); no `-deep-research-*.md` file was hand-written. Evidence
below is from cached publications (22369361, 24115911, 24627523, 11196647, 1313413 present;
22013070 and 26401965 fetched for this review) and the UniProt record.

## What UreH is

The H. pylori ortholog of UreD, i.e. the urease-apoprotein-binding maturation protein
[PMID:24115911 "UreH is an ortholog of UreD found in other species"]. It partners UreF; two
heterodimers give the (UreF-UreH)2 platform that recruits two UreG copies
[PMID:24115911 "UreF and UreH form a complex to recruit UreG, which is a SIMIBI class GTPase,
to the preactivation complex."], and nickel-charged UreG can only activate apo-urease when
UreF/UreH is present [PMID:24115911 "We found that the nickel-charged UreG dimer can activate
urease only in the presence of the UreF/UreH complex (Figure 7A)."]. ureH mutation abolishes
urease activity in the E. coli reconstitution [PMID:1313413].

## Nickel

Two strands of family-level evidence keep `GO:0016151` alive as a non-core property:

- K. aerogenes MBP-UreD binds divalent metals [PMID:22369361 "MBP-UreD binds divalent metal
  ions (~2.5 Ni per protomer, Kd ~50 uM; ~4 Zn per protomer, Kd ~5 uM)"] - note zinc binds
  more tightly than nickel.
- A buried channel runs from the UreG metal site through UreF and out of UreH
  [PMID:26401965 "Prior in silico analysis of the homologous, structurally characterized
  UreH/UreF/UreG complex from Helicobacter pylori identified a water tunnel originating at a
  likely nickel-binding motif in UreG, passing through UreF, and exiting UreH"], and
  disrupting the equivalent tunnel in K. aerogenes UreD reduces urease activity and urease
  nickel content without disturbing complex formation [PMID:26401965 "These findings support
  the role of a molecular tunnel in UreD as a direct facilitator of nickel transfer into
  urease"].

Nothing has been measured on Q09067 itself, and the measured nickel load of the H. pylori
preactivation complex sits on the UreG dimer interface - hence KEEP_AS_NON_CORE rather than
ACCEPT or REMOVE. This matches the treatment of genes/PSEPK/ureD.

## Decisions

- Three bare `GO:0005515` rows (all partner UreF): MODIFY to `GO:0018237 urease activator
  activity`.
- `GO:0018237` (IBA, node PTN008658292, Arabidopsis UreD donor): ACCEPT, core.
- `GO:0019627`: MODIFY to `GO:0043419` with a `propagation_review` (node transfer sound,
  granularity only).
- `GO:0150006 urease activator complex` added as NEW (IDA, PMID:24115911).
