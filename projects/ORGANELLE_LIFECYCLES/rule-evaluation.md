# Rule evaluation across reference proteomes

[Back to the project](../ORGANELLE_LIFECYCLES.md)

**Bottom line:** every eukaryote-wide rule candidate, and the lineage-scoped acidocalcisome rule, was evaluated with the module engine against
PANTHER's release-19 sequence classification files for 24 organisms. Three things show up. First,
in lineages that certainly have the organelle, several rules failed on a single selector that held
only the human protein or missed one lineage's subfamily; those are selector defects, not biology. The
two largest, MPP and Pex2, are fixed (#6416, #6418) and the results below are rerun with the fixes; the
rest are listed below for fixing. Second, the lineages with reduced or absent organelles (the
mitosome-bearing *Giardia* and *Entamoeba*, the hydrogenosome-bearing *Trichomonas*, the non-ciliated
lineages for the cilium, the lineages without VTC for the acidocalcisome) fail as expected, so the rules
discriminate. Third, the engine cannot evaluate
a protein-complex step from family selectors, because it compiles the complex into one atom without its
units; the census supplies the units itself.

## Method

[selector_census.py](selector_census.py) compiles each module with `ai_gene_review.module_logic`, so
optional parts, variant sets and module references count as the engine reads them. A step holds in an
organism when one of its PANTHER family or subfamily ids selects a protein in that organism's
classification file; a protein-complex step holds when every active unit's ids do. A step that also
requires an InterPro domain holds only when a selected protein carries that domain in UniProt's InterPro
cross-references, which the script fetches once and caches. The per-organism
counts, the verdicts and the engine's innermost gaps are in
[selector-census.yaml](selector-census.yaml). Regenerate both with:

```
uv run python projects/ORGANELLE_LIFECYCLES/selector_census.py \
    mitochondrial_protein_import mitochondrial_iron_sulfur_cluster_assembly \
    peroxisomal_protein_import escrt_iii_intralumenal_vesicle_formation \
    vacuolar_atpase_acidification er_cotranslational_translocation \
    er_oxidative_protein_folding autophagosome_core_biogenesis \
    intraflagellar_transport_core golgi_copi_vesicle_coat nuclear_pore_transport_core \
    lipid_droplet_neutral_lipid_storage acidocalcisome_polyphosphate_storage \
    phagosome_maturation synaptic_vesicle_cycle \
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
| `mitochondrial_protein_import` | ✓ | ✓ | ✓ | 3 | 1 | 2 | ✓ | ✓ | ✓ | 4 | 4 | 9 | 5 | 1 | ✓ | ✓ | 1 | ✓ | ✓ | ✓ | ✓ | ✓ | 1 | 9 |
| `mitochondrial_iron_sulfur_cluster_assembly` | ✓ | ✓ | ✓ | ✓ | 1 | 1 | 1 | 1 | 1 | ✓ | ✓ | 2 | 2 | ✓ | 2 | 1 | 3 | 1 | 1 | ✓ | ✓ | ✓ | ✓ | 4 |
| `peroxisomal_protein_import` | ✓ | ✓ | 2 | 4 | 3 | 7 | 1 | ✓ | ✓ | 2 | 2 | 10 | 8 | 4 | 1 | 10 | 8 | ✓ | 1 | 1 | 1 | ✓ | ✓ | 9 |
| `escrt_iii_intralumenal_vesicle_formation` | ✓ | ✓ | ✓ | ✓ | ✓ | 1 | ✓ | ✓ | ✓ | ✓ | ✓ | 2 | ✓ | 1 | ✓ | 1 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `vacuolar_atpase_acidification` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 1 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `er_cotranslational_translocation` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 3 | 1 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 1 | ✓ | ✓ | 1 |
| `er_oxidative_protein_folding` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `autophagosome_core_biogenesis` | ✓ | ✓ | ✓ | 2 | 1 | 5 | 3 | ✓ | ✓ | 2 | 2 | 11 | 3 | 4 | 1 | 4 | 2 | ✓ | 2 | ✓ | ✓ | ✓ | ✓ | 4 |
| `intraflagellar_transport_core` | ✓ | 3 | 1 | ✓ | 1 | ✓ | ✓ | ✓ | 8 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 14 | 10 | 14 | 14 | 14 | 14 | 14 | 14 | 14 |
| `golgi_copi_vesicle_coat` | ✓ | ✓ | ✓ | 1 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 3 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 1 | ✓ | 1 | ✓ | ✓ | 1 |
| `nuclear_pore_transport_core` | ✓ | ✓ | 1 | 2 | 2 | 1 | ✓ | ✓ | ✓ | 1 | 1 | 2 | 3 | 2 | ✓ | 3 | ✓ | 1 | 1 | ✓ | ✓ | ✓ | ✓ | 3 |
| `lipid_droplet_neutral_lipid_storage` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 1 | 1 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 1 |
| `acidocalcisome_polyphosphate_storage` | 1 | 1 | 1 | 1 | 1 | 1 | ✓ | ✓ | 1 | ✓ | ✓ | 1 | 1 | 1 | 1 | ✓ | ✓ | 1 | 1 | ✓ | ✓ | ✓ | 1 | 1 |
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
  - Dictyostelium discoideum: `tim44_tether`
- `mitochondrial_iron_sulfur_cluster_assembly`
  - Arabidopsis thaliana: `isd11_subunit`
  - Oryza sativa: `isd11_subunit`
  - Chlamydomonas reinhardtii: `isd11_subunit`
- `peroxisomal_protein_import`
  - Caenorhabditis elegans: `pex14_importomer_unit`, `pex10_e3_unit`
  - Saccharomyces cerevisiae: `pex2_e3_unit`
  - Schizosaccharomyces pombe: `pex2_e3_unit`
  - Oryza sativa: `pex1_atpase_unit`
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

Two defects found by the first run are fixed, and the matrix and lists above are rerun with the fixes:

- **MPP (#6416).** `mitochondrial_protein_import` selected the MPP beta and alpha subunits only by
  `PTHR11851:SF103` and `SF192`, the mammalian and primate subfamilies, which hold none of the other 23
  organisms' proteins in PANTHER's files, so the rule failed on MPP in every non-human genome. The beta
  step now also selects SF149, and the alpha step SF49, SF203 and SF194. The rule is now met in 13
  organisms. Both added subfamilies are mixed. SF149 also holds proteins that serve as cytochrome bc1 core
  protein I, such as *Euglena* P43264. Its fission-yeast member, Q9P7X1, is named a probable MPP beta by
  UniProt and `qcr1` in the committed entries table, and lies on a branch where PAINT records loss of MPP
  activity, so fission yeast's pass on the beta step is not evidence of MPP beta activity. SF49 also
  holds bacterial M16 proteases, which the module's Eukaryota context leaves out of scope.
- **Pex2 (#6418).** `peroxisomal_protein_import` selected Pex2 only by the family `PTHR48178`, which in
  these files holds the human, moss, Arabidopsis and rice proteins. PANTHER's files put the fly, worm,
  Dictyostelium and Chlamydomonas Pex2 proteins in `PTHR23350:SF4` (named Peroxisome biogenesis factor 2,
  in the Pex10-named family), while UniProt puts them in `PTHR48178:SF1`. *Neurospora* Pex2 (Q7SEZ3) and
  *Trypanosoma* Pex2 (Q582U7) are in SF4 in both sources: in PANTHER's `PTHR19.0_neurospora` and
  `PTHR19.0_t_brucei` classification files, and in UniProt's PANTHER cross-references. The Pex2 step now
  selects both, and the Pex10 step is narrowed from the whole `PTHR23350` family to its Pex10 subfamily
  SF0, so the two steps no longer share a selector. Fly, Chlamydomonas, *Neurospora* and Dictyostelium now
  meet the rule. Both yeasts still fail on Pex2: budding-yeast PEX2 (P32800) is not in PANTHER's yeast
  file, though UniProt places it in `PTHR48178`, and the census finds no fission-yeast protein in either
  Pex2 selector. *C. elegans* now fails on Pex10 because its PEX10 (C0HKD7) is missing from PANTHER's worm
  file; the whole-family selector had let the worm SF6 RING protein Q18355 pass in its place.

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

## The acidocalcisome rule

`acidocalcisome_polyphosphate_storage` is scoped to the lineages that make polyphosphate with the VTC
complex. It needs a VTC-domain subunit of `PTHR46140:SF1` (InterPro IPR018966; Vtc4 in most lineages)
and an acidifying pump (the H+-PPase `PTHR31998` or the V-ATPase rule). It is met in the nine organisms
with such a subunit: the chytrid, Chlamydomonas, *Trypanosoma*, *Leishmania*,
*Plasmodium*, Thalassiosira and the three fungi. Every other organism fails on the Vtc4 step alone. The
domain requirement excludes the Vtc1-like proteins, which have only the DUF202 membrane domain.
Dictyostelium's two `PTHR46140:SF1` proteins (Q54JW8, Q54ZD5) are of that kind, so without the domain the
rule would pass there on the wrong protein. The domain does not exclude every non-catalytic VTC subunit:
*Toxoplasma* has both a Vtc2 and a Vtc4 (PMID:42126255), and the entries table places its Vtc2 in
`PTHR46140:SF1`, so an apicomplexan VTC-domain protein in that subfamily need not be the catalytic subunit.
Nothing establishes which kind the putative *Plasmodium* protein C6KT60 is, so its pass may rest on a
non-catalytic subunit. The other passes are on proteins named Vtc4,
or on the Chlamydomonas, Leishmania and Thalassiosira VTC-domain proteins (the module lists them).

The failures in animals and land plants are expected, since neither has VTC. A failure does not mean the
organism lacks acidocalcisomes. Dictyostelium has polyphosphate-rich mass-dense granules with an H+-PPase
activity (PMID:11748243), but no VTC-domain protein and no `PTHR31998` protein in these files, and it makes
polyphosphate with a bacterial-type PPK1 (PMID:17940044). Paramecium and Phytophthora have no Vtc4-type
protein in these files either, and whether they have acidocalcisomes is not checked here. The three fungi
pass on their polyphosphate-filled vacuole, which the rule does not distinguish from an acidocalcisome.

## Expected failures

- **Reduced mitochondria.** *Giardia* and *Entamoeba* (mitosomes) and *Trichomonas* (hydrogenosomes)
  fail `mitochondrial_protein_import` on 5 to 9 steps and the iron-sulfur rule on 2 to 4. That fits
  reduced import machinery. With the MPP selectors fixed the counts no longer include that defect: the
  census finds an MPP beta but no MPP alpha in *Giardia* and *Entamoeba*, and both in *Trichomonas*.
  Other selector defects may still be among these gaps, so the counts are not yet a clean description
  of what these organelles keep.
- **Kinetoplastids.** *Trypanosoma* and *Leishmania* fail the import rule on TOM40, TIM23, Tim17 and
  Tim44. As `coverage.yaml` records, kinetoplastids replace the TIM23/TIM22 pair with a single
  Tim17-family translocase, so the rule needs a lineage variant set before it can be read there.
- **Peroxisomes.** The same three lineages and *Plasmodium* fail `peroxisomal_protein_import` on 8 to 10
  steps.
- **Cilia.** Every non-ciliated lineage (Arabidopsis, rice, both yeasts, *Neurospora*, Dictyostelium,
  Entamoeba) fails `intraflagellar_transport_core` on all 14 required steps. *Plasmodium* fails on all 14
  as well, although its male gametes are flagellated: the census finds no IFT subunit in it.

## Engine limitation

`module_logic` compiles a protein-complex annoton into one atom from the participant's `gene`,
`gene_product` or `family` slots, and its `active_units` are not read. A family-keyed oracle therefore
sees no selector for the complex, and the step can never hold. The census works around this by reading
the units itself. It also reports, per module, any complex whose units mix family-keyed and gene-keyed
selectors (`mixed_complex_steps` in the census), because such a complex is evaluated on its family-keyed
units alone; none of the 15 modules has one. A fix in the engine, compiling a complex into an AND over
its units, would let any oracle evaluate these steps.

## Full gap list

Every step that fails in at least one organism, with the organisms it fails in (codes as in the matrix). Generated from the census; steps whose gaps sit inside a variant set are listed under the variant set's id.

- `mitochondrial_protein_import`
  - `tim44_tether` (7): Nv, Tb, Lm, Gi, Tp, Dd, Eh
  - `tim17_subunit` (5): Tb, Lm, Gi, Tv, Eh
  - `tim23_channel` (5): Tb, Lm, Gi, Tv, Eh
  - `sam50_insertase` (4): Nv, Gi, Pt, Eh
  - `tim22_insertase` (4): Ta, Gi, Tv, Eh
  - `tom40_channel` (4): Tb, Lm, Gi, Tv
  - `erv1_oxidase` (3): Gi, Tv, Eh
  - `pam16_regulator` (3): Mb, Gi, Eh
  - `pam18_j_protein` (3): Nv, Mb, Eh
  - `mpp_alpha_subunit` (2): Gi, Eh
- `mitochondrial_iron_sulfur_cluster_assembly`
  - `isd11_subunit` (11): Mb, Bd, Cr, Pp, Gi, Tv, Ph, Tp, At, Os, Eh
  - `frataxin_activator` (4): Gi, Pf, Tp, Eh
  - `hscb_cochaperone` (4): Ta, Ph, Tp, Eh
  - `glrx5_carrier` (2): Tv, Eh
- `peroxisomal_protein_import`
  - `pex14_importomer_unit` (10): Ce, Nv, Mb, Gi, Tv, Pt, Ph, Pf, Tp, Eh
  - `pex2_e3_unit` (9): Nv, Gi, Tv, Pt, Pf, Tp, Sc, Sp, Eh
  - `pex1_atpase_unit` (8): Nv, Ta, Mb, Gi, Tv, Pf, Os, Eh
  - `pex3_family_membrane_docking` (8): Mb, Tb, Lm, Gi, Tv, Pt, Pf, Eh
  - `pex10_e3_unit` (7): Ce, Mb, Gi, Tv, Pf, Tp, Eh
  - `pex13_importomer_unit` (7): Nv, Tb, Lm, Gi, Pf, Tp, Eh
  - `pex19_family_cargo_recognition` (7): Ta, Gi, Tv, Pt, Pf, Tp, Eh
  - `pex12_e3_unit` (6): Ta, Mb, Gi, Pf, Tp, Eh
  - `pex5_family_pts1_binding` (6): Mb, Bd, Gi, Tv, Pf, Tp
  - `pex6_atpase_unit` (6): Mb, Gi, Tv, Pf, Tp, Eh
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
- `acidocalcisome_polyphosphate_storage`
  - `vtc4_catalytic_subunit` (15): Hs, Dm, Ce, Nv, Ta, Mb, Pp, Gi, Tv, Pt, Ph, At, Os, Dd, Eh
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
