# SEC11 curation notes

## Deep research

I checked for pre-existing `SEC11-deep-research-*.md` files in
`genes/CANAL/SEC11` and none were present in this sparse worktree.

I attempted repository deep research with:

```bash
just deep-research CANAL SEC11 --provider perplexity
```

The wrapper found Q5A869 and launched the Perplexity provider, but no provider
API keys were configured:

> ERROR - No research providers available. Please set API keys

No `SEC11-deep-research-perplexity.md` file was created.

## Manual literature summary

`SEC11` has a strong conserved-function case but little direct `C. albicans`
literature. The 2020 Candida secretory-pathway review summarizes the relevant
step as follows: "Following translocation into the ER, the N-terminal signal
peptide is cleaved by signal peptidase" and notes that "Spc3p, and Sec11p have
been identified as subunits in the signal peptidase complex", while adding that
SEC11's exact Candida function had not been characterized directly
[PMID:32102426].

The primary Candida signal peptidase-complex paper is about `SPC3`, not `SEC11`.
It cloned `CaSPC3`, showed that it could rescue an `S. cerevisiae spc3`
phenotype, and found that conditional repression made `CaSPC3` essential for
viability [PMID:15300682]. I therefore treated it as support for a conserved
Candida SPC, not as direct experimental evidence for Q5A869 catalytic activity.

The 2021 human cryo-EM paper resolved SEC11A- and SEC11C-containing SPC
paralogs and showed that the active site lies next to an ER-membrane window that
helps discriminate signal peptides by hydrophobic-region length
[PMID:34388369]. A 2026 `S. cerevisiae` paper then mapped the Sec11
C-terminal short helix and showed that it helps stabilize internal signal
sequences in the TM window [PMID:42586426]. These later papers are useful
mechanistic context for conserved Sec11 biology, but they do not change the
Candida-level annotation set.

## PAINT and annotation decisions

`PTHR10806-paint.tsv` has only three IBD rows:

- `PTN000086749` at the family root for `GO:0008233 peptidase activity`
- `PTN000086750` at `taxon:2759` for `GO:0005787 signal peptidase complex`
- `PTN000086750` at `taxon:2759` for `GO:0051604 protein maturation`

`Q5A869` belongs to `PTHR10806:SF6`, the fungal
`SIGNAL PEPTIDASE COMPLEX CATALYTIC SUBUNIT SEC11` subfamily. The root
`peptidase activity` assertion is biologically right but deliberately generic,
so I refined the IBA and UniProt/InterPro peptidase rows to the already present
`GO:0009003 signal peptidase activity` term. I accepted the eukaryotic
`PTN000086750` rows for signal peptidase complex membership and protein
maturation because `C. albicans` SEC11 is inside that eukaryotic placement and
there is no Candida-specific loss evidence.

The one biological-process row I removed is the EnsemblFungi transfer to
`GO:0045047 protein targeting to ER`. ER targeting is carried out by the signal
sequence, SRP/SRP receptor and the translocon; SEC11 acts afterward by cleaving
the signal peptide as the substrate enters the ER lumen. The old CGD `ND` row to
the `biological_process` root is no longer informative now that GOA has a
specific protein-maturation row.
