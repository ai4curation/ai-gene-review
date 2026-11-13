# tauB (Escherichia coli K-12) notes

## Session 2026-11-11 (Claude, AI-assisted)

Reviewed as a member of `modules/taurine_uptake_and_desulfonation.yaml`
(TauABC import plus TauD desulfonation). E. coli K-12 is the experimental
reference implementation of that module.

Deep research: no provider deep-research file was generated for this gene in
this session (no provider run was available). The review instead rests on the
cached publications for every GOA reference, read directly:

- PMID:8808933 (abstract): identification of the sulfate-starvation-regulated
  tauABCD cluster ["Disruption of these genes resulted in the loss of the
  ability to utilize taurine (2-aminoethanesulfonate) as a source of sulfur"].
- PMID:10781534, read in full through its PMC101965 copy: in-frame deletions
  with complementation ["The growth data indicate that taurine entered the cell
  exclusively via the TauABC transporter"]; TauABC also imports some other
  sulfonates ["Some sulfonates were taken up via both the TauABC and the SsuABC
  systems."]; Tau and Ssu components do not form hybrid transporters.

Decisions: ATP binding rows are non-core (part of the ATP hydrolysis core, as
for P. putida TauB). GO:0042918 alkanesulfonate transmembrane transport is kept
as non-core rather than refined, because E. coli TauABC demonstrably imports
several non-taurine sulfonates. The GO:0015411 transport row is accepted with
TauB recorded as contributing to the complex activity in core_functions.
