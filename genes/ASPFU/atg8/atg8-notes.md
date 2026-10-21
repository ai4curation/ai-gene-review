# ASPFU atg8 manual review notes

## Scope

Deep-research providers were unavailable in this sparse worktree, so this notes
file records manual review of the seeded `ASPFU/atg8` GOA rows, the local
`PTHR10969` PAINT data, direct cached literature, and a PubMed/Europe PMC scan
for 2024-2026 Aspergillus fumigatus autophagy papers.

## PTHR10969 PAINT

`Q4WJ27` is the A. fumigatus Af293 member of PANTHER family `PTHR10969`,
`MICROTUBULE-ASSOCIATED PROTEINS 1A/1B LIGHT CHAIN 3-RELATED`, listed in
`PTHR10969-entries.csv` as `Q4WJ27,Autophagy-related protein 8,protein,330879`.

The important PAINT nodes for the Aspergillus entry are:

- `PTN000103522`, a eukaryotic node, carries `GO:0000421 autophagosome
  membrane`, `GO:0008429 phosphatidylethanolamine binding`, `GO:0000045
  autophagosome assembly`, `GO:0000423 mitophagy`, `GO:0006995 cellular
  response to nitrogen starvation`, and `GO:0097352 autophagosome maturation`.
  All six propagate to Q4WJ27, and the placement is appropriate for a
  single-copy fungal Atg8-family ubiquitin-like modifier.
- `PTN000861115`, a fungal node seeded by budding- and fission-yeast Atg8
  annotations, carries `GO:0000329 fungal-type vacuole membrane`. That is the
  specific fungal compartment term to keep for A. fumigatus; the generic
  `GO:0005774 vacuolar membrane` SubCell and ISS rows are true but redundant.

No Aspergillus-specific divergence or loss was found for the eukaryotic or
fungal nodes.

## Cached papers

Richie et al. 2007 directly constructed a GFP-tagged A. fumigatus Atg8 using
Q4WJ27 and imaged it during starvation-induced autophagy. The key localization
result is that "Under starvation conditions, fluorescently labeled Atg8
accumulated within the vacuoles of wt A. fumigatus" [PMID:17921348 Unexpected
link between metal ion deficiency and autophagy in Aspergillus fumigatus.].
This is direct AfAtg8 support for vacuolar delivery during starvation, but the
paper perturbs `Af atg1`, not `Af atg8`.

Osakina et al. 2022 tagged Atg8 with RFP at the native locus and showed that
"under carbon and nitrogen starvation (C/N-) conditions, Atg8 localized to
punctate autophagosomal structures" [PMID:35448585 Protein Kinase A Regulates
Autophagy-Associated Proteins Impacting Growth and Virulence of Aspergillus
fumigatus.]. The same paper reports that "Deletion of Atg8 resulted in reduced
conidiation on glucose minimal medium agar (GMM)" and that Atg8 loss increases
PKA activity, useful A. fumigatus-specific biology that does not require a new
GO process term here.

Liu et al. 2025 analyzed Sec2p rather than Atg8. It is relevant newer context
because it places autophagy downstream of Sec2p in A. fumigatus and concludes
that "Sec2p positively regulated the autophagy pathway to enhance CWI pathway
gene expression in the presence of autophagy inducers" [PMID:39852455 Roles of
the Sec2p Gene in the Growth and Pathogenicity Regulation of Aspergillus
fumigatus.]. It does not justify modifying an atg8 row.

Jung et al. 2025 tested fungal ATG4 inhibitors using recombinant ATG4/ATG8
substrates from Cryptococcus, A. fumigatus, and A. niger. They cloned
`AfAtg4 (A0A9P9N7X1)` and an A. fumigatus Atg8 substrate in vitro [PMID:41407331
Evaluating the Antifungal Potential of Autophagy-Related Protein 4 (ATG4)
Inhibitors against Human Fungal Pathogens.]. This supports biochemical
conservation of ATG4-mediated fungal Atg8 processing and is useful context, but
it is not better row-level evidence than the local PAINT calls for Q4WJ27.

## Update scan

PubMed and Europe PMC searches for 2024-2026 `Aspergillus fumigatus` with
`Atg8`, `AFUA_1G07470`, `AfuAtg8`, or `autophagy` found new autophagy-related
work, especially the Sec2p and ATG4-inhibitor papers above. The other newer
hits are regulator-level, host-response, or review articles and do not change
the seeded Q4WJ27 GO decisions.
