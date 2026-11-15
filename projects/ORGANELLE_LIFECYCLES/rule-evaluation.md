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
The census reads PANTHER's files only. Where UniProt's PANTHER cross-reference places a protein elsewhere,
the repository's member index accepts either placement, but the census does not, so a gap here can be a
disagreement between the two sources rather than a wrong selector.

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

## Selector defects in the model organisms

Only the well-studied model organisms are triaged here: *Drosophila*, *C. elegans*, the two yeasts,
*Neurospora*, Arabidopsis, rice, Chlamydomonas and Dictyostelium. They certainly have mitochondria,
peroxisomes, an ER, a Golgi and a nucleus, so a failure in one of them is a selector that misses its
protein rather than a missing organelle. The same reasoning applies to most of the other lineages, whose
gaps are listed in the [full gap list](#full-gap-list) but not yet triaged; several of the steps below
fail there too (Nup88, for example, in ten lineages). Gap names are the engine's.

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
  `PTHR11851:SF103` and `SF192`, the mammalian and primate subfamilies, which hold none of the other
  organisms' proteins in PANTHER's files. Every other lineage's MPP is elsewhere in PTHR11851 (beta
  mostly in SF149, alpha mostly in SF49), so the rule fails in every non-human genome on MPP, and in some
  on further steps as well. Both of those subfamilies are mixed: SF149 also holds proteins that serve as
  cytochrome bc1 core protein I (fission-yeast Q9P7X1, on a branch where PAINT records loss of MPP
  activity), and SF49 holds bacterial M16 proteases, so widening the selectors to them over-matches.
- **Pex2.** `peroxisomal_protein_import` selects Pex2 by the family `PTHR48178`, which in these files
  holds only the human, moss, Arabidopsis and rice proteins. This one is mostly a disagreement between
  sources rather than a wrong selector: PANTHER's files put the fly, worm, Dictyostelium and Chlamydomonas
  Pex2 proteins in `PTHR23350:SF4` (a subfamily named Peroxisome biogenesis factor 2 in the Pex10-named
  family), while UniProt puts them in `PTHR48178:SF1`; *Neurospora* (Q7SEZ3) and *Trypanosoma* (Q582U7)
  Pex2 are in SF4 in both PANTHER's files and UniProt's cross-references. Yeast PEX2 is not in PANTHER's yeast file at all, though UniProt places it in `PTHR48178`.

- **ISD11.** The iron-sulfur rule selects ISD11 by the family `PTHR13166`, which recovers it in only
  part of the eukaryotes: it holds no protein from Arabidopsis, rice, moss, Chlamydomonas, Monosiga,
  Batrachochytrium, Phytophthora, Thalassiosira, Giardia, Trichomonas or Entamoeba in these files. No plant
  protein is named ISD11 or LYRM4 in PANTHER's plant files or in UniProt, and the plant LYR-motif proteins
  UniProt lists are in other families. Whether these lineages carry a divergent ISD11 the family does not
  capture is open; the selector is not changed.

## The cilium rule outside its defining lineages

`intraflagellar_transport_core` was defined on eleven ciliated lineages. Of the ciliated or flagellated
lineages outside that set, *Drosophila* fails on IFT81, IFT74 and IFT139, *C. elegans* on the dynein-2
intermediate chain DYNC2I2 and Trichoplax on IFT74; moss fails on 8 steps and Thalassiosira on 10, as the
module's notes already record. Fly and worm both build IFT-dependent sensory cilia, so their gaps are
lineage-specific placements, divergent orthologs or real losses; which is not checked here.

## Expected failures

- **Reduced mitochondria.** *Giardia* and *Entamoeba* (mitosomes) and *Trichomonas* (hydrogenosomes)
  fail `mitochondrial_protein_import` on 7 to 10 steps and the iron-sulfur rule on 2 to 4. That fits
  reduced import machinery, but the counts also include the MPP and other selector defects above, so
  they are not yet a clean description of what these organelles keep.
- **Peroxisomes.** The same three lineages and *Plasmodium* fail `peroxisomal_protein_import` on 8 to 10
  steps.
- **Cilia.** Every non-ciliated lineage (Arabidopsis, rice, both yeasts, *Neurospora*, Dictyostelium,
  Entamoeba) fails `intraflagellar_transport_core` on all 14 required steps. *Plasmodium* fails on all 14
  as well, although its male gametes are flagellated: the census finds no IFT subunit in it.

## Engine limitation

`module_logic` compiles a protein-complex annoton into one atom from the participant's `gene`,
`gene_product` or `family` slots, and its `active_units` are not read. A family-keyed oracle therefore
sees no selector for the complex, and the step can never hold. The census works around this by reading
the units itself. A fix in the engine, compiling a complex into an AND over its units, would let any
oracle evaluate these steps.

## Full gap list

Every step that fails in at least one organism, with the organisms it fails in (codes as in the matrix). Generated from the census; steps whose gaps sit inside a variant set are listed under the variant set's id.

- `mitochondrial_protein_import`
  - `mpp_alpha_subunit` (23): Dm, Ce, Nv, Ta, Mb, Bd, Cr, Pp, Tb, Lm, Gi, Tv, Pt, Ph, Pf, Tp, At, Os, Sc, Sp, Nc, Dd, Eh
  - `mpp_beta_peptidase` (23): Dm, Ce, Nv, Ta, Mb, Bd, Cr, Pp, Tb, Lm, Gi, Tv, Pt, Ph, Pf, Tp, At, Os, Sc, Sp, Nc, Dd, Eh
  - `tim44_tether` (7): Nv, Tb, Lm, Gi, Tp, Dd, Eh
  - `tim17_subunit` (5): Tb, Lm, Gi, Tv, Eh
  - `tim23_channel` (5): Tb, Lm, Gi, Tv, Eh
  - `sam50_insertase` (4): Nv, Gi, Pt, Eh
  - `tim22_insertase` (4): Ta, Gi, Tv, Eh
  - `tom40_channel` (4): Tb, Lm, Gi, Tv
  - `erv1_oxidase` (3): Gi, Tv, Eh
  - `pam16_regulator` (3): Mb, Gi, Eh
  - `pam18_j_protein` (3): Nv, Mb, Eh
- `mitochondrial_iron_sulfur_cluster_assembly`
  - `isd11_subunit` (11): Mb, Bd, Cr, Pp, Gi, Tv, Ph, Tp, At, Os, Eh
  - `frataxin_activator` (4): Gi, Pf, Tp, Eh
  - `hscb_cochaperone` (4): Ta, Ph, Tp, Eh
  - `glrx5_carrier` (2): Tv, Eh
- `peroxisomal_protein_import`
  - `pex2_e3_unit` (20): Dm, Ce, Nv, Ta, Mb, Bd, Cr, Tb, Lm, Gi, Tv, Pt, Ph, Pf, Tp, Sc, Sp, Nc, Dd, Eh
  - `pex14_importomer_unit` (10): Ce, Nv, Mb, Gi, Tv, Pt, Ph, Pf, Tp, Eh
  - `pex1_atpase_unit` (8): Nv, Ta, Mb, Gi, Tv, Pf, Os, Eh
  - `pex3_family_membrane_docking` (8): Mb, Tb, Lm, Gi, Tv, Pt, Pf, Eh
  - `pex13_importomer_unit` (7): Nv, Tb, Lm, Gi, Pf, Tp, Eh
  - `pex19_family_cargo_recognition` (7): Ta, Gi, Tv, Pt, Pf, Tp, Eh
  - `pex12_e3_unit` (6): Ta, Mb, Gi, Pf, Tp, Eh
  - `pex5_family_pts1_binding` (6): Mb, Bd, Gi, Tv, Pf, Tp
  - `pex6_atpase_unit` (6): Mb, Gi, Tv, Pf, Tp, Eh
  - `pex10_e3_unit` (5): Gi, Tv, Pf, Tp, Eh
- `escrt_iii_intralumenal_vesicle_formation`
  - `vps20_chmp6_nucleator` (3): Gi, Pt, Pf
  - `snf7_chmp4_polymer` (2): Mb, Gi
- `vacuolar_atpase_acidification`
  - `v1_g_stator` (1): Tp
- `er_cotranslational_translocation`
  - `srp_receptor_beta` (3): Gi, Tv, Sp
  - `srp72_core` (2): Gi, Eh
  - `sec61_gamma` (1): Gi
- `autophagosome_core_biogenesis`
  - `atg13_regulator` (9): Nv, Mb, Tb, Lm, Gi, Tv, Pt, Pf, Eh
  - `atg12_ubl` (8): Mb, Tb, Lm, Gi, Tv, Pt, Ph, Eh
  - `atg2_lipid_transfer` (8): Nv, Ta, Bd, Gi, Pt, Pf, Os, Eh
  - `atg5_e3` (5): Mb, Bd, Gi, Tv, Tp
  - `atg6_beclin` (4): Bd, Gi, Pf, Eh
  - `atg9_scramblase` (3): Gi, Pt, Pf
  - `atg7_e1` (2): Mb, Gi
  - `atg7_e1_atg8` (2): Mb, Gi
  - `atg1_ulk_kinase` (1): Tp
  - `atg3_e2` (1): Gi
  - `atg4_protease` (1): Gi
  - `atg8_lc3` (1): Gi
  - `vps15_regulator` (1): Os
- `intraflagellar_transport_core`
  - `dync2i2` (11): Ce, Pp, Pf, Tp, At, Os, Sc, Sp, Nc, Dd, Eh
  - `ift74` (11): Dm, Ta, Pp, Pf, At, Os, Sc, Sp, Nc, Dd, Eh
  - `ift139` (10): Dm, Pf, Tp, At, Os, Sc, Sp, Nc, Dd, Eh
  - `ift140` (10): Pp, Pf, Tp, At, Os, Sc, Sp, Nc, Dd, Eh
  - `ift144` (10): Pp, Pf, Tp, At, Os, Sc, Sp, Nc, Dd, Eh
  - `ift38` (10): Pp, Pf, Tp, At, Os, Sc, Sp, Nc, Dd, Eh
  - `ift81` (10): Dm, Pp, Pf, At, Os, Sc, Sp, Nc, Dd, Eh
  - `ift122` (9): Pf, Tp, At, Os, Sc, Sp, Nc, Dd, Eh
  - `ift172` (9): Pf, Tp, At, Os, Sc, Sp, Nc, Dd, Eh
  - `ift46` (9): Pf, Tp, At, Os, Sc, Sp, Nc, Dd, Eh
  - `ift52` (9): Pp, Pf, At, Os, Sc, Sp, Nc, Dd, Eh
  - `ift57` (9): Pf, Tp, At, Os, Sc, Sp, Nc, Dd, Eh
  - `ift70` (9): Pp, Pf, At, Os, Sc, Sp, Nc, Dd, Eh
  - `ift80` (9): Pf, Tp, At, Os, Sc, Sp, Nc, Dd, Eh
- `golgi_copi_vesicle_coat`
  - `copd` (2): Gi, Sp
  - `cope` (2): Gi, Eh
  - `copb2` (1): Os
  - `copg` (1): Gi
  - `gbf1_arf_gef` (1): Nv
- `nuclear_pore_transport_core`
  - `nup88_82` (10): Ce, Ta, Mb, Tb, Lm, Gi, Tv, Pt, Pf, Eh
  - `seh1` (5): Nv, Gi, Tv, Pf, Eh
  - `cse1_exportin` (4): Tv, Pf, Os, Eh
  - `crm1_exportin` (1): Pt
  - `ntf2_ran_import` (1): Ta
  - `nup98_96` (1): Nv
  - `sec13` (1): At
- `lipid_droplet_neutral_lipid_storage`
  - `dgat_family` (3): Gi, Tv, Eh
- `phagosome_maturation`
  - `rilp_rab7_effector` (23): Dm, Ce, Nv, Ta, Mb, Bd, Cr, Pp, Tb, Lm, Gi, Tv, Pt, Ph, Pf, Tp, At, Os, Sc, Sp, Nc, Dd, Eh
  - `lamp_proteins` (18): Bd, Cr, Pp, Tb, Lm, Gi, Tv, Pt, Ph, Pf, Tp, At, Os, Sc, Sp, Nc, Dd, Eh
  - `hops_tether` (14): Cr, Pp, Tb, Lm, Gi, Tv, Pt, Ph, Pf, Tp, At, Os, Dd, Eh
  - `mon1_ccz1_rab7_gef` (6): Tb, Lm, Gi, Ph, Tp, Sp
  - `pikfyve_pi35p2` (6): Hs, Ta, Gi, Tp, Os, Eh
  - `rab5_gtpase` (4): Hs, Gi, At, Sp
  - `v_atpase` (2): Hs, At
  - `rab7_gtpase` (1): Gi
- `synaptic_vesicle_cycle`
  - `synapsin_vesicle_tether` (20): Ta, Mb, Bd, Cr, Pp, Tb, Lm, Gi, Tv, Pt, Ph, Pf, Tp, At, Os, Sc, Sp, Nc, Dd, Eh
  - `cycle_synaptotagmin` (19): Mb, Bd, Cr, Pp, Tb, Lm, Gi, Tv, Pt, Ph, Pf, Tp, At, Os, Sc, Sp, Nc, Dd, Eh
  - `cycle_snare_complex` (11): Mb, Pp, Tb, Lm, Gi, Tv, Ph, Pf, Tp, At, Os
  - `cycle_vesicular_transporter` (11): Bd, Tb, Lm, Gi, Tv, Pt, Pf, Sc, Sp, Nc, Eh
  - `cycle_clathrin_coat` (1): Eh
