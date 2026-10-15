---
title: "Archaeal GO annotation error patterns"
species: [METTH, METS5, SACS2, ACIAM, SULAC]
---

# Archaeal GO annotation error patterns

[Back to the ARCHAEA project](../ARCHAEA.md)

This catalogue records recurring ways that GO annotation goes wrong for
archaeal gene products. Each entry names the pipeline involved, gives an
example from a completed review, and says what a fix might look like. It
was started from the five-gene pilot (October 2026): Msed_0709, sor, lacS,
mcrA (*Methanothermobacter*) and cdvB.

The five pilot genes had 20 GOA rows between them: 17 electronic (IEA or
IBA), one ISS, and two EXP (both on *Methanothermobacter* mcrA).

## 1. A neofunctionalized paralog inherits its ancestor's annotation

- **Pipelines:** PANTHER TreeGrafter (GO_REF:0000118), InterPro2GO
  (GO_REF:0000002), UniProt ARBA naming.
- **Example:** METS5/Msed_0709 (A4YEN2), the malonyl-CoA/succinyl-CoA
  reductase of the 3HP/4HB CO2-fixation cycle. It evolved from
  aspartate-semialdehyde dehydrogenase (ASD) by gene duplication. It
  carried ASD activity (GO:0004073), threonine biosynthesis (GO:0009088)
  and amino acid biosynthetic process (GO:0008652); all three were
  removed. The genuine *M. sedula* ASD, Msed_1700 (A4YHF3), shares the
  PANTHER subfamily (PTHR46718:SF1) and the InterPro signatures, so both
  genes receive the same GO set.
- **The error also runs the other way:** ARBA rule ARBA00067001 names the
  true ASD, Msed_1700, as a malonyl-CoA reductase.
- **Possible fix:** split the malonyl-CoA reductase clade into its own
  PANTHER subfamily, and use the TIGR00978 (asd_EA) signature as a
  negative condition in the ARBA rule.
- **Where else to look:** other enzymes of the 3HP/4HB cycle and other
  archaeal pathways that recruited enzymes from amino acid metabolism.

## 2. A plant-seeded PAINT node is propagated to an archaeal enzyme

- **Pipeline:** PANTHER/PAINT IBA.
- **Example:** SACS2/lacS (P22498), the GH1 beta-glycosidase. It carried
  galactosyltransferase activity (GO:0008378) by IBA from node
  PTN008498319, whose only experimental seed is Arabidopsis SFR2, a
  galactolipid transferase that has lost hydrolase activity. Of the 58
  GO:0008378 IBA rows citing that node, lacS is the only non-plant one. The
  row was removed.
- **Latent risk:** the same node has a negated IRD for beta-glucosidase
  activity (GO:0008422), an activity that has been measured directly in
  lacS.
- **Possible fix:** restrict the SFR2 IBD to the plant clade, or move the
  archaeal GH1 enzymes out of the SFR2-named subfamily (SF209).

## 3. Eukaryotic compartment terms on archaeal ESCRT-III homologs

- **Pipelines:** InterPro2GO (GO_REF:0000002), TreeGrafter
  (GO_REF:0000118).
- **Example:** cdvB itself is not affected, because its InterPro family is
  IPR053654 (CdvB). But InterPro2GO maps IPR005024 (Snf7) to vacuolar
  transport (GO:0007034) on about 41 archaeal ESCRT-III/CdvB homologs,
  including Sulfolobales proteins such as Q972B4 (ST1214) and A4YHE8
  (Msed_1695). TreeGrafter puts multivesicular-body and
  endosome-to-vacuole transport terms (GO:0032511, GO:0043328) on Asgard
  archaeal ESCRT proteins.
- **Why it is wrong:** archaea have no vacuole or endosome. The archaeal
  process is Cdv-dependent cytokinesis (GO:0061639).
- **Possible fix:** add a Eukaryota taxon restriction to the IPR005024 to
  GO:0007034 mapping.

## 4. A subcellular-location description is mapped to the wrong compartment

- **Pipeline:** UniProt SubCell mapping (GO_REF:0000044).
- **Example:** SULAC/cdvB (Q4J924) carried nucleoid (GO:0009295). The
  UniProt note says the protein forms bands *between* segregating
  nucleoids at mid-cell. The controlled value "Cytoplasm, nucleoid" and
  the mapping turned this into a nucleoid location. Modified to cell
  division site (GO:0032153).
- **Where else to look:** CdvA, CdvC and other archaeal division-site
  proteins described relative to nucleoids.

## 5. Under-annotation: experimental evidence never reaches GO

- **Example:** ACIAM/sor (P29082), sulfur oxygenase/reductase. Only five
  proteins in GOA carry GO:0033755, all by IEA. No SOR has an experimental
  GO annotation or any process term, despite biochemistry since 1989 and
  more than ten crystal structures. UniProt records experimentally
  supported iron-binding residues (86, 90, 114), but GOA has no metal- or
  iron-binding row.
- **Example:** cdvB had no process term at all. GO:0061639 Cdv-dependent
  cytokinesis, the term created for this machinery, has no annotations
  for any organism in GOA.
- **Action:** the pilot reviews propose NEW annotations for these with
  IDA evidence.

## 6. Generic or misleading terms where the archaeal biology is known

- **Generic methanogenesis.** InterPro2GO assigns methanogenesis
  (GO:0015948) to MCR family members even where the organism's only route
  is known. *Methanothermobacter* strain Delta H grows only on H2 and CO2,
  so its mcrA was modified to methanogenesis, from carbon dioxide
  (GO:0019386).
- **Missing GO terms for archaeal pathways.** GO has no activity terms for
  malonyl-CoA reductase (NADP+, EC 1.2.1.75) or succinyl-CoA reductase
  (NADP+, EC 1.2.1.76), and no term for the 3HP/4HB cycle. Carbon fixation
  by 3-hydroxypropionate cycle (GO:0043427) describes the *Chloroflexus*
  bicycle, a different pathway. The Msed_0709 review proposes three new
  terms.
- **Look-alike term.** Aerobic sulfur oxidation (GO:0070220) is defined
  through the sulfur dioxygenase reaction (EC 1.13.11.18), not the
  sulfur oxygenase/reductase reaction, so the sor review avoided it.
- **Default NAD binding.** InterPro2GO maps the Rossmann-fold domain
  IPR000534 to NAD binding even for NADPH-specific enzymes such as
  Msed_0709. The row was removed.

## 7. Evidence attributed to one isoenzyme from a mixed assay

- **Example:** one of the two EXP rows for coenzyme-B
  sulfoethylthiotransferase activity on *Methanothermobacter* mcrA cites a
  cell-extract assay (PMID:3122735). Extracts contain both MCR isoenzymes
  (MCR I and MCR II), so the activity cannot be attributed to MCR I alone.
  The row was accepted, because the activity itself is not in doubt, and
  the caveat is recorded in the review.
