# tauD (Escherichia coli K-12) notes

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
- PMID:9287300 (abstract): purification and reaction stoichiometry ["The pure
  enzyme converted taurine to sulfite and aminoacetaldehyde"]; taurine is the
  preferred substrate (Km 55 uM).
- PMID:11955067 (abstract): crystal structure with Fe(II), 2-oxoglutarate and
  taurine.
- PMID:22221834 (abstract): TauD(Ec) and TauD(Pp) are homotetramers.
- PMID:16165092 and PMID:16643838 (abstracts): inhibition kinetics and a coupled
  succinate assay, both measuring TauD activity directly.

Decisions: broad oxidoreductase, 2-oxoglutarate-dependent dioxygenase and sulfur
compound metabolic process rows are refined to GO:0000908 and GO:0019529.
Ferrous iron binding, identical protein binding and homotetramerization are kept
as non-core. PAINT node PTN000765929 (GO:0000908, Bacteria) is seeded by this
protein.
