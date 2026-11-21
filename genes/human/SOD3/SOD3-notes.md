# SOD3 notes

Deep research provider status, 2026-11-21: `just deep-research-falcon human SOD3
--fallback perplexity-lite` could not run because only the `claude_code`
provider was available in this checkout, and `just deep-research-claude-code
human SOD3` failed because the Claude Code CLI was not authenticated. These
manual notes are the literature trail for the first SOD3 review.

## Core picture

SOD3 encodes extracellular Cu/Zn superoxide dismutase, a secreted, tetrameric
metalloenzyme that catalyzes dismutation of extracellular superoxide to
molecular oxygen and hydrogen peroxide. Its specific activity depends on copper
loading [PMID:15761197 "the specific activity of SOD3 directly correlates with
its copper content"], and the first human SOD3 crystal structure resolved a
homotetramer with Cu/Zn metal-binding sites similar to SOD1 [PMID:19289127 "The
metal-binding sites are similar to those found in SOD1"; PMID:19289127 "The
dimers form a functional homotetramer"].

The extracellular matrix is the core site of action. Placenta assays localized
and measured extracellular SOD in human villous extracellular matrix
[PMID:9699963 "Placental EC-SOD localized within the villous extracellular
matrix around arterioles"], and R213G studies show that the C-terminal
heparin-binding region is needed for normal heparan-sulfate and endothelial
surface affinity [PMID:8546689 "the binding of m-EC-SOD to vascular endothelial
cells is much decreased in vivo"].

SOD3 is loaded with copper in the secretory pathway rather than by CCS. ATOX1
supports SOD3 activity and expression [PMID:15761197 "Atox1 functions not only
as a copper chaperone for SOD3 but also as a positive regulator for SOD3
transcription"], and ATP7A/Menkes ATPase directly interacts and colocalizes with
SOD3 in the trans-Golgi network during copper delivery [PMID:16371425 "Copper
treatment in wild-type cells promoted the direct interaction and colocalization
of SOD3 with MNK in the trans-Golgi network"].

SOD3 can also be stored and acutely released by inflammatory cells. In human
macrophages, LPS stimulation releases SOD3 from an intracellular compartment to
the cell surface and extracellular space within 30 minutes [PMID:31326693 "human
macrophages release SOD3 from an intracellular compartment within 30 min
following LPS stimulation"].

## Annotation decisions

- `GO:0004784` superoxide dismutase activity, `GO:0019430` removal of
  superoxide radicals, and extracellular-region rows are accepted as core.
- `GO:0005507` copper ion binding is accepted. Add `zinc ion binding`, because
  human SOD3 is a Cu/Zn enzyme and its crystal structure resolved the SOD1-like
  metal-binding sites [PMID:19289127].
- Generic `GO:0046872` metal ion binding is too general once the specific copper
  and zinc terms are asserted.
- The mouse `GO:0046209` nitric oxide metabolic process rows are over-annotated:
  extracellular SOD3 preserves NO bioavailability by removing superoxide, which
  prevents superoxide from inactivating NO, but SOD3 does not metabolize nitric
  oxide.
- The `GO:0005737` cytoplasm ARBA call is removed. SOD3 has a signal peptide and
  functions in the secretory pathway, extracellular region, and macrophage
  storage vesicles, not as a soluble cytosolic enzyme.
- Golgi and vesicle rows are kept non-core. They are biologically plausible
  maturation, trafficking, or storage compartments, but the enzyme's direct
  catalysis occurs extracellularly.
- All bare `GO:0005515` rows are removed under the project protein-binding
  policy; even the ATP7A and FBLN5 contacts are better captured as evidence in
  notes than as a retained generic molecular function.
