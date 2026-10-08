# PAX7 (human, P23759) — curation notes

Project: NEURAL_CREST_ORIGINS, Tier 4 (missing module members). Reviewed 2026-10-08.

## Identity and molecular activity

- Paired box protein Pax-7, Pax3/7 subgroup (paired domain + paired-type homeodomain + OAR tail in isoform 3).
  1p36; rearranged with FOXO1 in alveolar rhabdomyosarcoma [PMID:9339373 "a rearrangement of the PAX7 gene by
  chromosomal translocation is frequently found in alveolar rhabdomyosarcoma tumors"].
- Close paralog of PAX3 [PMID:9339373 "The gene encodes a predicted protein of 520 amino acids that is 47 amino acids
  longer at the carboxy end than the highly related PAX3 protein"]. UniProt: can bind DNA as a PAX3 heterodimer.
- Sequence-specific DNA binding of full-length human PAX7 measured by methyl-SELEX [PMID:28473536 "By analysis of 542
  human TFs with methylation-sensitive SELEX ... we found that there are also many TFs that prefer CpG-methylated
  sequences"]. Abstract and conclusion do not name PAX7; the IDA row relies on the supplementary motif tables (accepted).
- Activator / pioneer: in mouse pituitary, Pax7 opens a melanotrope enhancer repertoire [PMID:29358650 "Pax7, by
  opening a unique repertoire of enhancers, is necessary and sufficient for specification of one pituitary lineage"].
  In chick crest, Pax7 binds and activates the FoxD3 NC1 enhancer (below). In muscle, Pax7 activates Myf5 via
  Carm1/MLL recruitment and Id3 (deep research; mouse). Activator is the dominant mode -> NEW GO:0001228 (ISS).

## Neural crest / neural plate border role (network layer = border specifier)

- Chick: Pax7 marks a region of gastrula epiblast specified to form crest, and is required for crest markers
  [PMID:16688176 "This region expresses the transcription factor Pax7 by stage 4 + and later contributes to neural folds
  and migrating neural crest"; "In chicken embryos, Pax7 is required for neural crest formation in vivo, because
  blocking its translation inhibits expression of the neural crest markers Slug, Sox9, Sox10 and HNK-1"]. Abstract only.
- Chick FoxD3 enhancers [PMID:23284303, full text]: "Detailed regulatory analysis shows that initial expression of
  FoxD3 in both cranial and trunk neural crest requires direct input from neural plate border genes, Pax7 and Msx1/2."
  ChIP: "These data demonstrate that Pax7, Msx1 and Ets1 bind in vivo to the NC1 enhancer element in the cranial neural
  crest." NC2 (trunk): Pax7, Msx1/2 and Zic1 required; "these results place Pax7 and Msx1/2 as general regulators of
  FoxD3 expression, while Ets1 and Zic1 seem to specifically regulate NC1 and NC2, respectively."
  Sox10 is NOT a direct Pax7 target: "For the case of Sox10, regulatory analysis revealed direct inputs from Sox9, Ets1
  and Myb, but not Pax7 [5], suggesting that effects of loss of Pax7 on Sox10 expression are likely to be indirect."
  Pax7 knockdown lowered cranial FoxD3 "but not Sox9 or HNK-1 expression" at HH9.
  The authors themselves call Pax7 "the neural plate border marker".
- Mouse: Pax7-/- mice have cephalic crest-derived facial malformations, with Pax3 redundancy proposed
  [PMID:8631261 "Our analysis suggests that the observed phenotype is due to a cephalic neural crest defect"].
  Lineage tracing: Pax7 descendants contribute more to cranial than trunk crest [PMID:22848431 "we found a higher
  contribution of Pax7 descendants in the cranial compared to either cardiac or trunk neural crest"], and early
  Pax7+ cells are a subset of the crest domain.
- Module deep research (falcon, read only): chick single-cell data show Pax7+ border cells are not exclusively
  crest-fated (Williams 2022; not cached, not cited in the YAML).
- Amphioxus: Pax3/7 marks the neural plate border without the crest specifiers [PMID:18562679 "Ectodermal Zic and
  Pax3/7 expression marks the neural plate border, and amphioxus SoxB1-a expression labels the entire neural plate."].

### Layer judgement and term level

PAX7 is a neural plate border specifier, the chick/amniote counterpart of frog Pax3 in the border layer. It
is expressed in the border before crest specifiers. It is required for them and binds a specifier enhancer
directly (FoxD3 NC1, in vivo ChIP). It is not itself a crest specifier: its expression domain includes non-crest
border fates and dorsal neural tube. No gain-of-function sufficiency for crest has been shown (unlike the frog
Pax3+Zic1 pair). Sox10 and Sox9 responses are indirect or absent.

Decision: NEW `GO:0014029` neural crest formation (ISS; chick Basch 2006 plus mouse Mansouri 1996). This matches
the convention that border genes keep `GO:0014029`. `GO:0014034` commitment was NOT added. Frog Pax3 carries it
from existing IMP/IGI rows based on Pax3+Zic1 *sufficiency* to induce crest, and PAX7 has no equivalent
sufficiency data. The direct FoxD3 enhancer input is captured as an MF (`GO:0001228`) and as a module edge,
not as a commitment process. `GO:0014036` is rejected: PAX7 is upstream of the specifiers. Flagged as a
suggested question: should the direct-binding evidence alone justify `GO:0014034`?

## Muscle satellite (stem) cells — major mammalian role

- [PMID:11030621 "Cell culture and electron microscopic analysis revealed a complete absence of satellite cells in
  Pax7(-/-) skeletal muscle."]
- Pax3/Pax7 progenitors [PMID:15843801 "In the absence of both Pax3 and Pax7, further muscle development is arrested and
  only the early embryonic muscle of the myotome forms."]
- Adult requirement [PMID:24065826 "Here, we demonstrate that Pax7 is an absolute requirement for satellite cell
  function in adult skeletal muscle."; "Therefore, we conclude that Pax7 is essential for regulating the expansion and
  differentiation of satellite cells during both neonatal and adult myogenesis."]
- Human: biallelic PAX7 variants cause myopathy with satellite-cell exhaustion [PMID:31092906 "A lack of PAX7
  expression was associated with satellite cell pool exhaustion"; "biallelic variants in the master transcription
  factor PAX7 cause a new type of myopathy that specifically affects satellite cell survival"].
- Decision: satellite cell differentiation rows (ISS/IEA from mouse) are ACCEPTED as core. NEW `GO:0043403` skeletal
  muscle tissue regeneration (ISS from mouse; matches mouse Pax7's IMP term). Not proposed: `GO:0014813`
  satellite cell commitment, a part of the existing satellite cell differentiation term, so it would be redundant.

## Dorsal neural tube

- Pax3/Pax7 double mutants: [PMID:9858722 "Analysis of Pax3 and Pax7 double mutant mice demonstrates that both genes
  share redundant functions to restrict ventral neuronal identity in the spinal cord."] -> NEW `GO:0021904` (ISS),
  non-core. Mouse Pax7's own `GO:0021904` IDA comes from an FKBP8 paper (PMID:18590716) where Pax7 is a marker.
  The double-mutant paper is better grounding.

## Comparator checks (QuickGO, 2026-10-08)

NC-branch query: GO:0014029, 0014031, 0014032, 0014033, 0014034, 0014036 and 0001755, with is_a/part_of descendants,
across taxa 9606, 10090, 10116, 7955, 8355, 8364 and 9031. Results filtered to Pax genes:

- **Human PAX7 (P23759) and human PAX3 (P23760): no NC term.** Human PAX3 has only MF/CC rows plus a TAS
  "apoptotic process" row from PMID:10871843, the same paper as PAX7's apoptosis row.
- **Mouse Pax7 (P47239): no NC term.** It carries `GO:0014813` satellite cell commitment (IMP, PMID:11030621),
  `GO:0043403` regeneration (IMP, PMID:9608680), `GO:0048706` embryonic skeletal system development (IMP,
  PMID:8631261 — the cephalic-crest paper, curated to skeleton, not crest), `GO:0021904` (IDA, PMID:18590716) and
  `GO:0014816` (IDA, PMID:34059674).
- **Mouse Pax3 (P24610)**: `GO:0001755` NC migration (IMP, PMID:15384171) only.
- **Chicken**: no Pax entry in any species carries an NC term in chicken. Chick PAX7 (O42349, unreviewed) carries
  only ISS terms from mouse (muscle, `GO:0021904`, `GO:0048706`). **Basch 2006 is uncurated.**
- **Zebrafish pax7a (O57418)**: `GO:0048066` developmental pigmentation (IMP, PMID:18417109), xanthophore
  differentiation (IGI); **pax7b (C0M005)**: MF/CC only. Zebrafish pax3a: `GO:0001755` (IMP).
- **Xenopus**: experimental `GO:0014029`/`GO:0014034` only on pax3-a/pax3-b (Q645N4/Q0IH87). pax7.L/S carry
  only the ARBA IEA `GO:0014034`. X. tropicalis pax3 Q28DP6 carries ISS `GO:0014029`/`GO:0014034`.
- Conclusion: no Pax7 in any species has an experimental crest-formation term. The chick functional
  data (Basch 2006, Simoes-Costa 2012) are uncurated, and mouse Pax7's crest phenotype was curated to skeletal
  development. This is a coverage gap, not a convention. Same-layer peers (frog pax3, zic1; MSX1/TFAP2A NEW ISS)
  carry `GO:0014029`.
- `GO:0001228` among Pax genes in the 6 taxa (first page): only PAX1 (IEA); Pax3/7 typically sit at `GO:0000981`.
  Frog pax3-a review added `GO:0001228` NEW (IDA).
- `GO:0021904`: mouse Pax7 (IDA), rat Pax7 (ISO), chick Pax-7 (ISS), frog zic1 (IMP). Human PAX7 lacks it; it
  was probably not projected because the mouse row carries acts_upstream_of_or_within.
- `GO:0014834` satellite cell maintenance in regeneration: carried only by Wnt7a, Fzd7, Igf1, Ezh2 and Selenon,
  never Pax7. So `GO:0043403` (the mouse convention) was used instead.

## Row decisions (22 GOA rows)

- MF: all DNA-binding/TF rows ACCEPT. The IDA `GO:0003700` row (PMID:31092906, abstract-only; the curator
  likely saw reporter assays in the full text) is accepted.
- CC: chromatin and nucleus rows ACCEPT.
- `GO:0007399` IBA: KEEP_AS_NON_CORE (as for pax3-a).
- `GO:0009653` IEA/TAS: KEEP_AS_NON_CORE. Generic; the TAS paper is a gene-structure paper.
- `GO:0014816` IEA/ISS: ACCEPT (core muscle role).
- `GO:0043066` TAS PMID:10871843: UNDECIDED. The abstract covers PAX3 and PAX3/FKHR only, and the full text is not
  available. A PAX7 survival role in satellite cells is plausible (PMID:31092906) but not established
  as anti-apoptotic.

## Module placement

Add PAX7 as a Pax3/7 paralog variant in the border-specification part, next to frog pax3-a. Edges:
PAX7 -> foxd3, direct (ChIP + enhancer knockdown, chick, both NC1 and NC2). Msx1/2 are co-inputs, with Ets1
at NC1 (cranial) and Zic1 at NC2 (trunk). PAX7 -> sox10 is indirect (via Sox9/Ets1/Myb). The evidence is
chick-grounded, so use the human P23759 entry as representative with a chick note.

## Open issues

- Is the Pax3 vs Pax7 border role lineage-specific (frog Pax3, chick Pax7)? Mouse shows redundancy (Pax3/7).
- Does PAX7 direct binding at FoxD3 justify `GO:0014034`?
- The apoptosis TAS row is unresolved.
- Human data are almost entirely muscle (myopathy, RMS fusion); crest evidence in human is absent.
