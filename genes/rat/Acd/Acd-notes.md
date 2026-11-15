# Acd (Q4FZR5) Curation Notes — Rat Shelterin Subunit TPP1

## 1. Gene & Protein Overview

- **Organism & Identifiers**: *Rattus norvegicus* `Acd` (`RGD:1565053`, `UniProtKB:Q4FZR5`, sequence version 1, **417 aa**; `PANTHER:PTHR14487` / `PANTHER:PTHR14487:SF3` `ADRENOCORTICAL DYSPLASIA PROTEIN HOMOLOG`).
- **Direct Experimental Evidence vs. Orthology Transfer**:
  - Direct rat-specific experimental evidence in UniProt (`Q4FZR5`) is limited to full-length thymus cDNA cloning (`PMID:15489334`) and quantitative phosphoproteomic detection of Ser25 phosphorylation across rat tissues (`PMID:22673903`). All 42 GOA rows on `rat/Acd` are orthology/phylogenetic or electronic projections (`IBA` from `PANTHER:PTN002683935`, `ISO` from human `Q96AP0` and mouse `Q5EE38` via `GO_REF:0000121`, and `IEA` from InterPro/UniProtKW/SubcellularLocation/ARBA).
- **Sequence & Functional-Site Conservation**:
  - Rat `Q4FZR5` (417 aa) shares >88% sequence identity with mouse `Q5EE38` (416 aa) and retains every functional element characterized in human `Q96AP0` and mouse `Q5EE38`:
    1. **NOB hydrophobic motif**: `P11-W12-I13` (`RLVLRPWIRELIL`, `FT MOTIF 11..13 /note="PWI"` in `Q4FZR5` SV 1).
    2. **TEL patch acidic loop**: `D78-W79-E80-E81-K82-E83` (`DWEEKEFGFRGTEGRLLLL` at positions 78–96 in `Q4FZR5` SV 1, identical to `DWEEKEFGFRGTEGRLLLL` at positions 80–98 in human `Q96AP0` SV 4), including the essential disease-associated `Lys82` (`Lys84` in `Q96AP0` / `Lys170` in 544-aa `TPP1-L`) and `Arg92` (`Arg94` in `Q96AP0`).
    3. **POT1-interaction domain (`aa 156–245`)** and **C-terminal TIN2-binding helix (`aa 390–412`, including conserved `Pro364` corresponding to `Pro405` in `Q96AP0`)**.

## 2. Key Annotation Decisions (Harmonized with `human/ACD`, `mouse/Acd`, and `PANTHER:PTHR14487`)

- **`ACCEPT` (core)**: `GO:0070187` (`shelterin complex`), `GO:0016233` (`telomere capping`), `GO:0031848` (`protection from non-homologous end joining at telomere`), `GO:0007004` (`telomere maintenance via telomerase`), `GO:0032211` (`negative regulation of telomere maintenance via telomerase`), `GO:0070198` (`protein localization to chromosome, telomeric region`), `GO:0070200` (`establishment of protein localization to telomere`), `GO:0032202` (`telomere assembly`), `GO:0070182` (`DNA polymerase binding`).
- **`NEW` (`ISO` from `UniProtKB:Q96AP0`)**:
  - `GO:0030674` (`protein-macromolecule adaptor activity`) and `GO:0032212` (`positive regulation of telomere maintenance via telomerase`), matching the conserved shelterin-bridging and TEL-patch telomerase-activating roles established in human `Q96AP0` and mouse `Q5EE38` (neither term is present in rat GOA).
- **`MODIFY` (refinement)**:
  - `GO:0000781` (`chromosome, telomeric region`) & `GO:0005654` (`nucleoplasm`) → `GO:0140445` (`chromosome, telomeric repeat region`).
  - `GO:0000783` (`nuclear telomere cap complex`) → `GO:0070187` (`shelterin complex`).
  - `GO:0000723` (`telomere maintenance`) → `GO:0016233` (`telomere capping`) and `GO:0007004` (`telomere maintenance via telomerase`).
  - `GO:0006886` (`intracellular protein transport`) → `GO:0070200` (`establishment of protein localization to telomere`).
- **`TOO_GENERAL` / `KEEP_AS_NON_CORE` / `MARK_AS_OVER_ANNOTATED`**: `GO:0005634` (`nucleus` → `TOO_GENERAL`), `GO:0016604` (`nuclear body` → `KEEP_AS_NON_CORE`), `GO:0044877` (`protein-containing complex binding` → `KEEP_AS_NON_CORE`), and `ISO` projections of mouse *acd* p53-dependent developmental phenotypes (`GO:0001501` `skeletal system development`, `GO:0001655` `urogenital system development`, `GO:0030326` `embryonic limb morphogenesis`, `GO:0035282` `segmentation`, all `MARK_AS_OVER_ANNOTATED`).
- **`REMOVE` (refuted / mis-propagated)**:
  - `GO:0005697` (`telomerase holoenzyme complex`, `IEA` `IPR019437`).
  - `GO:0042162` (`telomeric repeat DNA binding`, `IBA`/`IEA`/`ISO`): Acd/TPP1 does not bind DNA directly; POT1/TRF1/TRF2 do (`PMID:31216472`, `PMID:35201900`).
  - `GO:0010521` (`telomerase inhibitor activity`, `ISO` from `Q96AP0`) and `GO:0070203` (`regulation of establishment of protein localization to telomere`, `ISO` from `Q96AP0`), both propagated from erroneous BHF-UCL annotations on `PMID:25172512`.

## 2026-11-15 follow-up: limits of transferred assertions

The earlier GO:0010521 and GO:0070203 REMOVE recommendations are superseded by UNDECIDED. Human inhibitor activity and the interpretation of localization regulation remain unresolved; neither transfer validity nor target-function absence is established. No human long-isoform mechanism is asserted for rat. The mouse skeletal p53-rescue results do not establish a urogenital mechanism: GO:0001655 is also UNDECIDED, while skeletal/limb/segmentation judgments are explicitly restricted to the studied source phenotypes. The review remains DRAFT. Native GOA identifiers and citations were retained.

## 2026-11-15 round-four follow-up: source queries and transfer scope

The preceding entry's UNDECIDED inhibitor decision is superseded by REMOVE for the GO:0010521 ISO transfer. The weakly grounded human source and the absence of the human long-form extension from retained canonical rat Q4FZR5 do not support that transfer. This does not establish absence of every inhibitory context or survey all rat transcripts. The PMID:31216472 statement about mice is removed from rat annotation evidence. GO:0070203 remains UNDECIDED because neither the negative human localization result nor the inhibitor-specific sequence argument settles the regulatory role in rat. Rat status remains DRAFT with two UNDECIDED contexts.

PMID:22101936's Lys233/POT1 localization comparison uses human TPP1 constructs and mouse POT1a in mouse MEFs: "we co-transfected Myc-mPOT1a with either FLAG-hTPP1WT or FLAG-tagged hTPP1 mutants into wild-type MEFs.". The earlier shorthand contrasting mouse and human results must not be read as a controlled comparison of the two species' TPP1 proteins. Regulation of TPP1 itself does not settle whether it performs GO:0070203.

Sequence comparison: the retained human Q96AP0 short-form, mouse Q5EE38 and rat Q4FZR5 records each place the shared PWIRELILGS anchor at residues 11-20. PMID:31216472 defines the human short form as residues 87-544 of the long form; the anchor thus maps to long-form residues 97-106, after the inhibitory-extension R43/R46/R48 region. The sequence evidence comes from the three committed *-uniprot.txt files, not from the paper's mouse-only Discussion sentence.

The validator flags the raw UniProt sequence quotation as a sequence-evidence advisory. It is retained here to make the N-terminal comparison inspectable; the activity decision also depends on the cited human functional experiment and the explicit sequence comparison above.
