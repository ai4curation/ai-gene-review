# tauA (Escherichia coli K-12) notes

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
- PMID:17203388 (abstract): purified TauA binds taurine ["Measurement of K (d)
  value (mean 11.3 nM) by binding/dialysis studies revealed high affinity and
  specificity with taurine"]. This supports the NEW GO:0030977 taurine binding
  row.

Decisions: membrane and periplasmic-space rows are refined to GO:0030288 as for
SsuA; the generic transporter row becomes a contributes_to reading of
GO:0015411. Sulfate/sulfur-starvation rows are accepted consistently with the
sibling Tau and Ssu subunits.
