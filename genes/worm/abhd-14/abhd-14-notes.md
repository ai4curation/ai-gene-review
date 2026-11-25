# abhd-14 (C. elegans) — review notes

Family-coordinated review of *Caenorhabditis elegans* `abhd-14` (`UniProtKB:Q9N366`, WormBase `WBGene00021927` / `Y55F3AM.10`, `PANTHER:PTHR46197:SF3`, 246 aa).

## 1. Phylogenetic placement, domain architecture, and WormBase MOD status

*C. elegans* `abhd-14` (`Q9N366`, 246 aa, unreviewed TrEMBL `Q9N366_CAEEL`, `sequence_version: 1`) is the sole nematode representative of `PANTHER:PTHR46197` (`PROTEIN ABHD14B-LIKE`), classified in invertebrate/divergent subfamily `PANTHER:PTHR46197:SF3` (`AB HYDROLASE-1 DOMAIN-CONTAINING PROTEIN`) rather than vertebrate `SF1` (`ABHD14A`) or `SF2` (`ABHD14B`).
- **WormBase MOD description check**: Running `ai-gene-review mod-description-deep-research worm abhd-14` returned `no_curated: 1` (WormBase carries no hand-written curated `concise_description` for `abhd-14`, only Alliance automated ontology text). Per `AGENTS.md`, no `-deep-research-wormbase.md` file is fabricated when WormBase lacks a hand-written description.
- **Sequence & active-site inspection (`Q9N366`, 246 aa)**:
  - Carries Pfam `PF12697` (`AB hydrolase-1`, residues 73–169) and retains a putative alpha/beta-hydrolase catalytic triad at `Ser145`, `Asp193`, and `His220`, **but** its nucleophilic elbow sequence (`CASMAAQY`, residues 143–150) substitutes the characteristic vertebrate ABHD14A/ABHD14B `SxSxS` (`SPSLS`) motif with `CASMA` (`Cys143-Ala144-Ser145-Met146-Ala147`)!
  - Lacks an annotated transmembrane signal-anchor in `Q9N366-uniprot.txt`, though it has a 45-residue N-terminal extension upstream of the beta-core (`MVLLHHQPLGSHHATTSGGSLLERADLSHPIPENARKLAQLVEYD...`) unlike the compact 210-aa mammalian `ABHD14B`.
  - Also note an upstream Reactome orthology projection artifact in `Q9N366-uniprot.txt`: `DR Reactome; R-CEL-156584; Cytosolic sulfonation of small molecules.` — projected from the human `R-HSA-156584` *p*-nitrophenyl butyrate / *p*-nitrophenol surrogate-substrate error on `ABHD14B`! Fortunately, `R-CEL-156584` has not been exported as a GOA row on `Q9N366`.

## 2. Review of the 2 existing GOA rows and knowledge gaps

1. **`GO:0005737` (`cytoplasm`, `IBA` `GO_REF:0000033` from `PANTHER:PTN002475422` seeded by `MGI:MGI:1915894|UniProtKB:Q96IU4`) -> `ACCEPT` (harmonized with `PTN002475422` `SOUND` / `FAMILY_WIDE`)**:
   - No direct experimental data exist for *C. elegans* `abhd-14`, and `Q9N366` lacks any predicted signal peptide or transmembrane helix, making cytoplasmic localization of this soluble alpha/beta-hydrolase protein plausible by ancestral inheritance from `PTN002475422` (supported by human `Q96IU4` cytosolic/cytoplasmic experimental evidence `PMID:14672934`, `PMID:31478652`).
2. **`GO:0005737` (`cytoplasm`, `IEA` `GO_REF:0000044`, `UniProtKB-SubCell:SL-0086` derived from unvetted `ARBA:ARBA00004496`) -> `ACCEPT`**:
   - Per `AGENTS.md`, we do **not** cite unvetted `ECO:0000256|ARBA:ARBA00004496` lines from `abhd-14-uniprot.txt` as evidence; instead, consistency with the phylogenetic `IBA` (`PTN002475422`) and the experimental mammalian ortholog localization (`PMID:31478652`) supports retaining `GO:0005737`, while noting that no nematode experiment has localized ABHD-14 directly.
3. **Knowledge gaps (`MF_DARK` and `BP_DARK`)**:
   - No molecular function or biological process is experimentally established for *C. elegans* `abhd-14`, and because `SF3` predates or diverges from the vertebrate `ABHD14A`/`ABHD14B` split and replaces the `SPSLS` nucleophile motif with `CASMA`, mammalian `ABHD14B` CoA-dependent lysine deacetylase activity must **not** be transferred to `abhd-14` without biochemical testing. Both `MF_DARK` and `BP_DARK` `BIOLOGY` knowledge gaps are recorded (`core_functions: []`).
