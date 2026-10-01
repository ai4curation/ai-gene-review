# CPR7 review notes

## 2026-10-01 IBA and current-GOA re-review

Forced a current UniProt/GOA refresh and rechecked CPR7 against the PTHR11071
PAINT cache and the cached primary papers. A Web/PubMed search for recent
CPR7/Cpr7/YJR032W literature did not find a newer direct yeast CPR7 paper that
changed the GO review.

The current GOA has three live IBA rows:

- `GO:0003755 peptidyl-prolyl cis-trans isomerase activity`
- `GO:0006457 protein folding`
- `GO:0005829 cytosol`

The PPIase and protein-folding rows trace to `PANTHER:PTN008511653`, and cytosol
traces to `PANTHER:PTN004228220`; all three are accepted as inherited
cyclophilin/Hsp90-co-chaperone biology. CPR7's own SGD seed in the `WITH/FROM`
lists is not circular: target-species experimental annotations are legitimate
descendant evidence supporting PAINT's ancestral node placement.

Several older assertions no longer exist in current GOA and are now explicit
`retired: true` rows:

- `GO:0005737 cytoplasm` IBA
- `GO:0016018 cyclosporin A binding` IBA
- `GO:0016853 isomerase activity` IEA from UniProt keyword mapping
- `GO:0051082 unfolded protein binding` IEA from ARBA
- `GO:0051082 unfolded protein binding` IDA from SGD

The stale unsplit `GO:0005515 protein binding` placeholders for `PMID:16554755`
and `PMID:19536198` were deleted rather than retired. They were old aggregate
IntAct rows with no exact interactor in the YAML, and the current refresh has no
live exact CPR7 row from either PMID.

The eight live exact `GO:0005515` IPI rows were re-reviewed by partner. The five
HSP82/HSC82 rows were changed to `MODIFY` with `GO:0051087 protein-folding
chaperone binding` as the replacement. The RPD3 row and two CNS1 rows were
changed to `REMOVE`: those physical associations are not being disputed, but
generic `protein binding` does not add useful molecular-function information for
CPR7.
