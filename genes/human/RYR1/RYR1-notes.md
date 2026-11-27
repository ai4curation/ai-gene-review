# RYR1 notes

## 2026-11-26 Codex review

Perplexity deep research could not run in this sparse ROS worktree: the first
attempt failed before provider execution because `templates/` was absent, and
the fallback reported that the Perplexity backend was not configured. I did not
spawn a Claude Code research worker on this two-CPU lane; this review instead
uses the fetched UniProt record, GOA rows, PAINT node table and cached primary
PMIDs.

RYR1 is the skeletal-muscle ryanodine receptor: a homotetrameric, multi-pass
sarcoplasmic-reticulum calcium-release channel whose cytosolic N-terminal
assembly is coupled to the Cav1.1 voltage sensor at the triad. UniProt records
human RYR1 as a cytosolic calcium-activated calcium channel that releases Ca2+
from the sarcoplasmic reticulum into the cytosol and triggers muscle
contraction after T-tubule depolarization [file:human/RYR1/RYR1-uniprot.txt].

Main curation decisions:

- Keep the conserved `GO:0005219` ryanodine-sensitive calcium-release channel
  activity, SR calcium-release process, SR membrane, channel complex and
  homotetramerization rows as the core RYR1 function, and keep
  calcium-induced calcium release as a true but secondary RYR1 gating mode
  relative to DHPR/Cav1.1-driven depolarization-induced Ca2+ release.
- Treat `GO:0005262` calcium channel activity, `GO:0005216` monoatomic ion
  channel activity, `GO:0006811` ion transport, `GO:0051209` release of
  sequestered calcium ion into cytosol and generic `membrane`/`protein-containing
  complex` terms as correct but less informative than existing RYR-specific
  rows.
- Keep ATP-, calmodulin-, calcium-, caffeine- and magnesium-linked regulatory
  terms as non-core contexts where the evidence identifies direct allosteric
  modulation of the RYR1 channel rather than a separate evolved activity.
- Remove the propagated voltage-gated calcium-channel rows, and mark
  sarcolemma and T-tubule rows as over-annotated: the
  skeletal-muscle channel is positioned across the junction from the T-tubule
  voltage sensor but is itself an SR/terminal-cisterna membrane protein.
- Mark developmental and phenotype-level propagated processes such as skin
  development, ossification and outflow-tract morphogenesis as over-annotated
  for the human gene product. Those rows trace to mouse phenotypes and do not
  identify a direct RYR1 execution step.
