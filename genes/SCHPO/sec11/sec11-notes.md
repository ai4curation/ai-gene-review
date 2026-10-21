# sec11 review notes

## Deep-research attempt

I attempted to generate a provider-backed deep-research file with:

```bash
just deep-research SCHPO sec11 --provider perplexity --timeout 60
```

The command failed because no research provider/API key was configured in this environment. No `sec11-deep-research-*.md` file was written; the manual literature and PAINT review is recorded here instead.

## Literature summary

The fission-yeast-specific cached literature for `sec11` is sparse. The direct `PMID:16823372` GOA source is the Matsuyama et al. ORFeome/YFP localization screen, whose cached record is abstract-only; PomBase curates an ER high-throughput direct assay annotation from that work, and the ER assignment is biologically coherent for the signal peptidase complex catalytic subunit.

The main functional evidence comes from budding yeast and mammalian orthologs. `PMID:3283143` showed that temperature-sensitive `S. cerevisiae sec11` cells are specifically defective in signal peptide processing and that a null mutation at `SEC11` is lethal. `PMID:1846444` biochemically placed the SEC11 product in a four-polypeptide yeast microsomal signal peptidase complex and described it as necessary for signal peptidase activity. `PMID:10206957` then mapped conserved Sec11 residues important for ER signal peptidase catalytic activity.

Newer structural work supports the same conserved eukaryotic mechanism. `PMID:34388369` resolved human SPC-A and SPC-C paralogs and placed the SEC11A/SEC11C catalytic site at the ER membrane next to a transmembrane window formed by all subunits. `PMID:42173868` resolved a human SPC-A model-signal-peptide complex and showed how a luminal binding groove and the transmembrane window cooperate in signal peptide recognition. `PMID:42586426` extended that mechanism in `S. cerevisiae`, showing that the Sec11 C-terminal short helix spans the membrane and preferentially stabilizes internal signal sequences for productive SPC engagement.

I did not find a newer direct `S. pombe sec11` biochemical or genetic paper beyond the PomBase-localization source. The orthology and PAINT support are nevertheless strong: UniProt O74323 is reviewed, belongs to the Peptidase_S26B/PANTHER PTHR10806 family, and is classified in the fungal `PTHR10806:SF6` subfamily with experimentally characterized `S. cerevisiae` SEC11.

## PAINT and annotation decisions

PANTHER `PTHR10806-paint.tsv` contains three ancestral assertions for this family:

- `PTN000086749` at the PTHR10806 root: `GO:0008233 peptidase activity`.
- `PTN000086750` at Eukaryota: `GO:0005787 signal peptidase complex`.
- `PTN000086750` at Eukaryota: `GO:0051604 protein maturation`.

The eukaryote-scoped `PTN000086750` rows are good matches for `S. pombe sec11`, so the IBA annotations to signal peptidase complex and protein maturation were accepted. The family-root `PTN000086749` peptidase-activity row is directionally correct but uninformative beside the accepted signal peptidase activity rows, so it was marked `TOO_GENERAL` rather than removed.

All three `GO:0009003 signal peptidase activity` rows were accepted. The generic `GO:0004252 serine-type endopeptidase activity` and `GO:0016485 protein processing` rows were modified to the more specific `GO:0009003` and `GO:0051604` terms. The root `GO:0008233 peptidase activity` and generic `GO:0016020 membrane` rows were marked `TOO_GENERAL`, because accepted descendant annotations in the same review cover the activity and compartment more precisely.

I verified that `GO:0006465 signal peptide processing` is obsolete and replaced by `GO:0051604 protein maturation`, so no new signal-peptide-processing term was proposed.
