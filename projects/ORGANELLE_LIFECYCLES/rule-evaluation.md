# Rule evaluation across reference proteomes

[Back to the project](../ORGANELLE_LIFECYCLES.md)

**Bottom line:** every eukaryote-wide rule candidate was evaluated with the module engine against
PANTHER's release-19 sequence classification files for 24 organisms. Three things show up. First,
in lineages that certainly have the organelle, several rules fail on a single selector that holds
only the human protein or misses one lineage's subfamily; those are selector defects, not biology,
and are listed below for fixing. Second, the lineages with reduced or absent organelles (the
mitosome-bearing *Giardia* and *Entamoeba*, the hydrogenosome-bearing *Trichomonas*, the non-ciliated
lineages for the cilium) fail as expected, so the rules discriminate. Third, the engine cannot evaluate
a protein-complex step from family selectors, because it compiles the complex into one atom without its
units; the census supplies the units itself.

## Method

[selector_census.py](selector_census.py) compiles each module with `ai_gene_review.module_logic`, so
optional parts, variant sets and module references count as the engine reads them. A step holds in an
organism when one of its PANTHER family or subfamily ids selects a protein in that organism's
classification file; a protein-complex step holds when every active unit's ids do. The per-organism
counts, the verdicts and the engine's innermost gaps are in
[selector-census.yaml](selector-census.yaml). Regenerate both with:

```
uv run python projects/ORGANELLE_LIFECYCLES/selector_census.py \
    mitochondrial_protein_import mitochondrial_iron_sulfur_cluster_assembly \
    peroxisomal_protein_import escrt_iii_intralumenal_vesicle_formation \
    vacuolar_atpase_acidification er_cotranslational_translocation \
    er_oxidative_protein_folding autophagosome_core_biogenesis \
    intraflagellar_transport_core golgi_copi_vesicle_coat nuclear_pore_transport_core \
    lipid_droplet_neutral_lipid_storage phagosome_maturation synaptic_vesicle_cycle \
    -o projects/ORGANELLE_LIFECYCLES/selector-census.yaml
```

The classification files are reference proteomes as PANTHER classifies them. A missing protein can be a
real loss, a protein PANTHER placed in another subfamily, or a gene missing from the proteome; the
census cannot tell these apart, and none of the gaps below was checked against the proteomes themselves.

## Results

✓ = all required parts met; a number = the engine's innermost gaps in that organism.

| Module | Hs | Dm | Ce | Nv | Ta | Mb | Bd | Cr | Pp | Tb | Lm | Gi | Tv | Pt | Ph | Pf | Tp | At | Os | Sc | Sp | Nc | Dd | Eh |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `mitochondrial_protein_import` | ✓ | 2 | 2 | 5 | 3 | 4 | 2 | 2 | 2 | 6 | 6 | 10 | 7 | 3 | 2 | 2 | 3 | 2 | 2 | 2 | 2 | 2 | 3 | 10 |
| `mitochondrial_iron_sulfur_cluster_assembly` | ✓ | ✓ | ✓ | ✓ | 1 | 1 | 1 | 1 | 1 | ✓ | ✓ | 2 | 2 | ✓ | 2 | 1 | 3 | 1 | 1 | ✓ | ✓ | ✓ | ✓ | 4 |
| `peroxisomal_protein_import` | ✓ | 1 | 2 | 4 | 4 | 7 | 2 | 1 | ✓ | 3 | 3 | 10 | 8 | 4 | 2 | 10 | 8 | ✓ | 1 | 1 | 1 | 1 | 1 | 9 |
| `escrt_iii_intralumenal_vesicle_formation` | ✓ | ✓ | ✓ | ✓ | ✓ | 1 | ✓ | ✓ | ✓ | ✓ | ✓ | 2 | ✓ | 1 | ✓ | 1 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `vacuolar_atpase_acidification` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 1 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `er_cotranslational_translocation` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 3 | 1 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 1 | ✓ | ✓ | 1 |
| `er_oxidative_protein_folding` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `autophagosome_core_biogenesis` | ✓ | ✓ | ✓ | 2 | 1 | 5 | 3 | ✓ | ✓ | 2 | 2 | 11 | 3 | 4 | 1 | 4 | 2 | ✓ | 2 | ✓ | ✓ | ✓ | ✓ | 4 |
| `intraflagellar_transport_core` | ✓ | 3 | 1 | ✓ | 1 | ✓ | ✓ | ✓ | 8 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 14 | 10 | 14 | 14 | 14 | 14 | 14 | 14 | 14 |
| `golgi_copi_vesicle_coat` | ✓ | ✓ | ✓ | 1 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 3 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 1 | ✓ | 1 | ✓ | ✓ | 1 |
| `nuclear_pore_transport_core` | ✓ | ✓ | 1 | 2 | 2 | 1 | ✓ | ✓ | ✓ | 1 | 1 | 2 | 3 | 2 | ✓ | 3 | ✓ | 1 | 1 | ✓ | ✓ | ✓ | ✓ | 3 |
| `lipid_droplet_neutral_lipid_storage` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 1 | 1 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 1 |
| `phagosome_maturation` | 3 | 1 | 1 | 1 | 2 | 1 | 2 | 3 | 3 | 4 | 4 | 7 | 3 | 3 | 4 | 3 | 5 | 5 | 4 | 2 | 4 | 2 | 3 | 4 |
| `synaptic_vesicle_cycle` | ✓ | ✓ | ✓ | ✓ | 1 | 3 | 3 | 2 | 3 | 4 | 4 | 4 | 4 | 3 | 3 | 4 | 3 | 3 | 3 | 3 | 3 | 3 | 2 | 4 |

Key: Hs *Homo sapiens*; Dm *Drosophila melanogaster*; Ce *Caenorhabditis elegans*; Nv *Nematostella vectensis*; Ta *Trichoplax adhaerens*; Mb *Monosiga brevicollis*; Bd *Batrachochytrium dendrobatidis*; Cr *Chlamydomonas reinhardtii*; Pp *Physcomitrium patens*; Tb *Trypanosoma brucei*; Lm *Leishmania major*; Gi *Giardia intestinalis*; Tv *Trichomonas vaginalis*; Pt *Paramecium tetraurelia*; Ph *Phytophthora ramorum*; Pf *Plasmodium falciparum*; Tp *Thalassiosira pseudonana*; At *Arabidopsis thaliana*; Os *Oryza sativa*; Sc *Saccharomyces cerevisiae*; Sp *Schizosaccharomyces pombe*; Nc *Neurospora crassa*; Dd *Dictyostelium discoideum*; Eh *Entamoeba histolytica*.

## Selector defects in lineages that have the organelle

These organisms certainly have mitochondria, peroxisomes, an ER, a Golgi and a nucleus, so a failure is
a selector that misses their protein rather than a missing organelle. Gap names are the engine's.

- `mitochondrial_protein_import`
  - Drosophila melanogaster: `mpp_beta_peptidase`, `mpp_alpha_subunit`
  - Caenorhabditis elegans: `mpp_beta_peptidase`, `mpp_alpha_subunit`
  - Saccharomyces cerevisiae: `mpp_beta_peptidase`, `mpp_alpha_subunit`
  - Schizosaccharomyces pombe: `mpp_beta_peptidase`, `mpp_alpha_subunit`
  - Neurospora crassa: `mpp_beta_peptidase`, `mpp_alpha_subunit`
  - Arabidopsis thaliana: `mpp_beta_peptidase`, `mpp_alpha_subunit`
  - Oryza sativa: `mpp_beta_peptidase`, `mpp_alpha_subunit`
  - Chlamydomonas reinhardtii: `mpp_beta_peptidase`, `mpp_alpha_subunit`
  - Dictyostelium discoideum: `tim44_tether`, `mpp_beta_peptidase`, `mpp_alpha_subunit`
- `mitochondrial_iron_sulfur_cluster_assembly`
  - Arabidopsis thaliana: `isd11_subunit`
  - Oryza sativa: `isd11_subunit`
  - Chlamydomonas reinhardtii: `isd11_subunit`
- `peroxisomal_protein_import`
  - Drosophila melanogaster: `pex2_e3_unit`
  - Caenorhabditis elegans: `pex14_importomer_unit`, `pex2_e3_unit`
  - Saccharomyces cerevisiae: `pex2_e3_unit`
  - Schizosaccharomyces pombe: `pex2_e3_unit`
  - Neurospora crassa: `pex2_e3_unit`
  - Oryza sativa: `pex1_atpase_unit`
  - Chlamydomonas reinhardtii: `pex2_e3_unit`
  - Dictyostelium discoideum: `pex2_e3_unit`
- `er_cotranslational_translocation`
  - Schizosaccharomyces pombe: `srp_receptor_beta`
- `autophagosome_core_biogenesis`
  - Oryza sativa: `vps15_regulator`, `atg2_lipid_transfer`
- `golgi_copi_vesicle_coat`
  - Schizosaccharomyces pombe: `copd`
  - Oryza sativa: `copb2`
- `nuclear_pore_transport_core`
  - Caenorhabditis elegans: `nup88_82`
  - Arabidopsis thaliana: `sec13`
  - Oryza sativa: `cse1_exportin`

The two largest are:

- **MPP.** `mitochondrial_protein_import` selects the MPP beta and alpha subunits by the subfamilies
  `PTHR11851:SF103` and `SF192`, which hold only the human proteins in PANTHER's files. Every other
  lineage's MPP is elsewhere in PTHR11851 (beta mostly in SF149, alpha mostly in SF49), so the rule fails
  in every non-human genome on MPP alone.
- **Pex2.** `peroxisomal_protein_import` selects Pex2 by the family `PTHR48178`, which in these files
  holds only the human, moss, Arabidopsis and rice proteins. The fly, worm, *Neurospora*, Dictyostelium
  and Chlamydomonas proteins named Pex2 in these files are in `PTHR23350:SF4`, a family PANTHER names after
  Pex10; the two yeasts' Pex2 proteins were not found there by name, and their placement is not checked.

## The cilium rule in fly and worm

`intraflagellar_transport_core` was defined on eleven ciliated lineages that did not include
*Drosophila* or *C. elegans*. Both build IFT-dependent sensory cilia, yet the rule fails in both: the fly
on IFT81, IFT74 and IFT139, the worm on the dynein-2 intermediate chain DYNC2I2. Whether these are
lineage-specific placements, divergent orthologs or real losses is not checked here.

## Expected failures

- **Reduced mitochondria.** *Giardia* and *Entamoeba* (mitosomes) and *Trichomonas* (hydrogenosomes)
  fail `mitochondrial_protein_import` on 7 to 10 steps and the iron-sulfur rule on 2 to 4. That fits
  reduced import machinery, but the counts also include the MPP and other selector defects above, so
  they are not yet a clean description of what these organelles keep.
- **Peroxisomes.** The same three lineages and *Plasmodium* fail `peroxisomal_protein_import` on 8 to 10
  steps.
- **Cilia.** Every non-ciliated lineage fails `intraflagellar_transport_core` on all 14 required steps.

## Engine limitation

`module_logic` compiles a protein-complex annoton into one atom from the participant's `gene`,
`gene_product` or `family` slots, and its `active_units` are not read. A family-keyed oracle therefore
sees no selector for the complex, and the step can never hold. The census works around this by reading
the units itself. A fix in the engine, compiling a complex into an AND over its units, would let any
oracle evaluate these steps.
