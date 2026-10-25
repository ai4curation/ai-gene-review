# ABA module cross-species audit

## 2026-10-25

This audit covers all six steps and all 19 representative proteins. The module
remains one PR, including its member reviews and source caches. The parent module
uses the Embryophyta taxonomic envelope for shared signaling components; its
connections and optional guard-cell output explicitly carry narrower scope where
native experiments justify it.

### Literature and taxon decisions

- The evolutionary reviews [PMID:32754170](https://pubmed.ncbi.nlm.nih.gov/32754170/) and [PMID:33459424](https://pubmed.ncbi.nlm.nih.gov/33459424/) distinguish the conserved receptor/phosphatase/kinase toolkit from lineage-specific output wiring. Recent reviews PMID:42457603 and PMID:42533760 were also checked. Their evolutionary framing is used without importing the proposed noncanonical CHLH receptor trajectory as an established step.
- [PMID:33911084](https://pubmed.ncbi.nlm.nih.gov/33911084/) and [PMID:37276398](https://pubmed.ncbi.nlm.nih.gov/37276398/) replace the old universal SnRK2 self-reactivation story with Raf initiation followed by SnRK2 amplification. Constitutive Arabidopsis B2 RAF activity is distinct from stress-responsive B3 RAF regulation.
- [PMID:30675528](https://pubmed.ncbi.nlm.nih.gov/30675528/) places moss PP2CA primarily downstream of SnRK2 and documents ABA-dependent SnRK2 phosphorylation without PP2CA. Thus the direct upstream PP2C inhibition edge is angiosperm-scoped. The moss ARK assays directly use SnRK2B/D; SRK2A is supported independently by kinase-loss and complementation experiments, not misrepresented as the assayed ARK substrate.
- [PMID:31744875](https://pubmed.ncbi.nlm.nih.gov/31744875/) establishes basal and hormone-stimulated MpPYL1 activity; the biochemical MpABI1 substrate is N-terminally truncated. [PMID:24743650](https://pubmed.ncbi.nlm.nih.gov/24743650/) establishes basal inhibition by monomeric rice RCAR5, called OsPYL11 in that paper and PYL5 in the selected UniProt record. The rice protoplast assay in PMID:26300907 measures context-dependent hormone-responsive reporter rescue. Those assays are not treated as contradictory.
- Native Arabidopsis and rice evidence supports the optional guard-cell channel output. The module does not infer a native bryophyte stomatal channel circuit merely because a bryophyte kinase can activate Arabidopsis SLAC1 in oocytes. Liverworts lack stomata.

### Family and representative audit

All eight annotons use FAMILY selectors. Every supplied PANTHER label was read
from the official local OBO; the release-19 member index was rebuilt and checked.
Broad PP2C and Raf classifications are constrained by the demonstrated molecular
role. No ancestral PTN placement was inferred from the choice of exemplars.

| Lineage | Reviewed representatives |
| --- | --- |
| Arabidopsis/eudicot | PYR1, ABI1, RAF11, OST1, SnRK2.2, SnRK2.3, ABF2, ABI5, SLAC1 |
| Rice/monocot | PYL5/RCAR5, PP2C06, SAPK9, SAPK10, BZIP46, SLAC1 |
| Marchantia/liverwort | MpPYL1, ABI1 |
| Physcomitrium/moss | ARK, SRK2A |

The 19 reviews contain 524 adjudicated rows, including explicitly unresolved
claims where the relevant evidence could not be established. Review notes record
provider failures and primary-source research. The Marchantia ABI1 accession is
anchored to the cloned GQ504039/D3W6X9 protein from male thalli; an inconsistent
modern sex-linked name is not imposed on that clone.

Moss transcriptional output has direct support in PMID:29575231 and
[PMID:40333983](https://pubmed.ncbi.nlm.nih.gov/40333983/), but current ABI5A/B
protein models disagree with the reported identical cloned coding sequences.
The module records this accession-mapping gap rather than inserting a dubious
representative. ABI5C has a plausible complete model but was not the focus of the
functional assays and is not substituted as if directly assayed.

### Rice SLAC1 identity and substrate specificity

[PMID:26481009](https://pubmed.ncbi.nlm.nih.gov/26481009/) reports nitrate selectivity with no obvious chloride permeability.
Nitrate is polyatomic, so the module's shared channel function is GO:0015267
channel activity; the rice gene review refines the transferred monoatomic-anion
annotations to nitrate transport and preserves the independently supported pore
mechanism. SAPK8 channel-current activation is distinguished from SAPK10
interaction/phosphorylation and water-loss evidence.

The [retained primer analysis](../genes/ORYSJ/SLAC1/SLAC1-bioinformatics/RESULTS.md)
checks PMID:31134357 Supplementary Table S1 against Q7XTX7, with SAPK10 as an
independent positive control and AK106615/BAG97777.1 as a comparison. Paired
terminal and internal fragment matches support the intended Q7XTX7 construct
despite the article's inconsistent locus string. The conflicting identifiers in
PMID:22915747 remain unresolved; that paper is not used for Q7XTX7-specific
functional claims. Short primer matches do not validate the full cloned insert.

### Validation and remaining limits

- Module schema, reference/title/quote validation, and PANTHER member checks pass.
- All 19 targeted gene validations and all 20 matching history records pass.
- The module has nine nonblocking conformance advisories: six ligand-binding assertions are retained annotations rather than separately enumerated core functions; rice channel activity is a retained replacement under its nitrate-specific core; two Raf subfamily assertions encounter an intentionally unresolved broad family review. Per-member experiments support the selected Rafs, without resolving kinase activity across the entire family.
- Repository-wide `just validate-all` is running; its result and PR CI must be checked before merge. Biological gaps are explicit, and neither schema validation nor a COMPLETE module status proves that every lineage uses identical wiring.
