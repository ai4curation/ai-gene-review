# Msed_2001 (A4YI89, HPCD_METS5) - curation notes

Metallosphaera sedula DSM 5348; 3-hydroxypropionyl-CoA dehydratase (EC 4.2.1.116),
crotonase (enoyl-CoA hydratase/isomerase, PF00378) family. ARCHAEA project gene.

**Provenance note:** automated deep research was unavailable in this session. No
`-deep-research-*.md` file was created. Literature was found with NCBI E-utilities
(esearch "Msed_2001", "3-hydroxypropionyl-CoA dehydratase Metallosphaera", "crotonyl-CoA
hydratase Metallosphaera sedula"), and each PMID was checked by esummary and cached with
`just fetch-pmid`. GO terms were checked with OLS4 REST and QuickGO; Rhea reactions with
the Rhea REST API.

## Identity and activity

- Purified from autotrophically grown M. sedula and identified by peptide mass
  fingerprinting. [PMID:19429610 "The best hit was the Msed_2001 gene annotated as an enoyl-CoA hydratase gene (100% identity and 41% coverage) coding for a 28.3-kDa (259 amino acids) protein."]
- Reaction: [PMID:19429610 "3-Hydroxypropionyl-CoA dehydratase (E.C.4.2.1.17) catalyzes the following reversible reaction: 3-hydroxypropionyl-CoA → acryloyl-CoA + H 2 O."]
  Recombinant His-tagged enzyme: Km 60 uM for 3-hydroxypropionyl-CoA, kcat about 96/s at 65 C.
- Second substrate, crotonyl-CoA / (S)-3-hydroxybutyryl-CoA:
  [PMID:19429610 "3-Hydroxypropionyl-CoA dehydratase acted nearly equally as well on ( S )-3-hydroxybutyryl-CoA as on 3-hydroxypropionyl-CoA."]
  [PMID:19429610 "The enzyme did not convert the ( R )-stereoisomer of 3-hydroxybutyryl-CoA."]
  [PMID:19429610 "Therefore, the dehydratase may fulfill a dual function."]
- Liu et al. 2021 re-examined all six M. sedula crotonase homologs (enzyme kinetics plus
  quantitative proteomics of autotrophic cells) and concluded Msed_2001 performs both
  hydratase steps of the cycle in vivo:
  [PMID:33472982 "we conclude that Msed_2001 is a promiscuous 3-hydroxypropionyl-CoA dehydratase/crotonyl-CoA hydratase that is responsible for both conversions in vivo."]
  [PMID:33472982 "Msed_2001 is responsible for 99% of 3-hydroxypropionyl-CoA dehydratase activity and for 86% of crotonyl-CoA hydratase activity in M. sedula"]
  Msed_2001 was the most abundant of the six homologs. The crotonase domain of the fusion
  protein Msed_0399, previously credited with the crotonyl-CoA step, carries only a small
  flux. The companion paper on Msed_0399 / Msed_0384 etc. is PMID:32218776
  [PMID:32218776 "The studied crotonases are homologous to 3-hydroxypropionyl-CoA dehydratase Msed_2001 and possess low 3-hydroxypropionyl-CoA dehydratase activity"].
- So the crotonyl-CoA activity matters: it is a second physiological activity in the
  second (acetyl-CoA-regenerating) half of the same cycle, not a side activity. GO term:
  GO:0120092 (2E)-butenoyl-CoA hydratase activity ("3-hydroxybutanoyl-CoA = (2E)-butenoyl-CoA
  + H2O"; xrefs RHEA:17849 (3R), RHEA:26558 (3S), RHEA:45584 (unspecified)). Rhea itself
  assigns RHEA:26558, the (3S) reaction, to EC 4.2.1.116, which fits this enzyme. Proposed as
  NEW (IDA).
- GO:0043956 definition (OLS): "Catalysis of the reaction: 3-hydroxypropionyl-CoA =
  acryloyl-CoA + H2O." xrefs EC:4.2.1.116, RHEA:26518. Parent GO:0004300 enoyl-CoA
  hydratase activity. Both GOA rows (IDA, IEA) correct.

## Structure and oligomeric state (disputed)

- Crystal structure with CoA (PDB 5ZAI, 1.8 A). Catalytic Glu113 and Glu133 conserved; the
  enoyl pocket is small and lined by bulky aromatic residues, suited to short-chain
  substrates. [PMID:30013155 "Ms3HPCD has a tightly formed α3 helix near the active site, and bulky aromatic residues are located at the enoyl-group binding site, resulting in the enzyme having an optimal substrate binding site for accepting short-chain 3-hydroxyacyl-CoA as a substrate."]
- Oligomeric state reported three ways: monomer by gel filtration (PMID:19429610, which the
  authors themselves say may be underestimated; this is UniProt's SUBUNIT line), hexamer in
  crystal and solution [PMID:30013155 "Size-exclusion chromatography confirmed that the enzymes also exists as a hexamer in solution (Fig. 2c)."],
  homo-octamer [PMID:27771364 "Recombinant HPCD formed a homo-octamer, with an estimated molecular mass of 220 kDa"].
  The hexamer agrees with the crotonase-family norm. UniProt's "Monomer" is probably out of
  date. No complex or CC term is proposed.
- Possible association with the preceding enzyme, 3-hydroxypropionyl-CoA synthetase
  (Msed_1456), by yeast two-hybrid and co-purification:
  [PMID:27771364 "The results demonstrate that HPCS and HPCD interact in vivo in yeast, although there is no evidence of interaction between ACR and SSR (Figure 2)."]
  [PMID:27771364 "Thus, a weak association between HPCS and HPCD is plausible and may be representative of a larger metabolon involving some or all of the 3HP/4HB cycle enzymes."]
  Evidence is preliminary; not annotated.

## Pathway context

- 3HP/4HB cycle [PMID:18079405 "This intermediate was reduced to 4-hydroxybutyrate and converted into two acetyl-CoA molecules via 4-hydroxybutyryl-CoA dehydratase."]
- Activity is not regulated by growth mode: [PMID:19429610 "was not downregulated in heterotrophically grown cells"]. So the enzyme is present during heterotrophic growth too; any heterotrophic role is unknown.
- Chloroflexus uses an unrelated trifunctional propionyl-CoA synthase for the same reaction
  (PMID:19429610 abstract), so the archaeal and Chloroflexus cycles evolved independently.
- Process term: GO:0043427 "carbon fixation by 3-hydroxypropionate cycle" is defined as the
  Chloroflexus glyoxylate-forming cycle (OLS definition checked). Following the Msed_0709
  review, use GO:0015977 carbon fixation and the proposed term "carbon fixation by
  3-hydroxypropionate/4-hydroxybutyrate cycle". Note: QuickGO shows UniProt has annotated
  Msed_1456 (A4YGR1) and S. tokodaii STK_07830 to GO:0043427 by IDA (PMID:18165310), and
  ARBA (GO_REF:0000117) puts GO:0043427 on many archaeal enzymes, so UniProt treats the term
  as covering the archaeal cycle. Flagged as a suggested question rather than resolved here.

## Fatty acid beta-oxidation (GO:0006635, TreeGrafter)

- Source: PANTHER PTN000235214; the subfamily is PTHR11941:SF54 "ENOYL-COA HYDRATASE,
  MITOCHONDRIAL" (named for ECHS1), so the term is the mitochondrial crotonase's role.
- GO:0006635 definition: complete oxidation of a long-chain fatty acid. Msed_2001 has a
  short-chain pocket (PMID:30013155), is characterized only on C3/C4 substrates, and is
  accounted for by the CO2-fixation cycle (PMID:33472982). No study shows fatty acid
  degradation by M. sedula or a role of Msed_2001 in it. In S. acidocaldarius, beta-oxidation
  genes sit in a dedicated FadR-regulated cluster [PMID:30948713 "acting as a repressor of a 30-kb gene cluster comprising 23 open reading frames encoding lipases and β-oxidation enzymes."];
  Msed_2001 is instead the universally conserved cycle enzyme of autotrophic Sulfolobales.
- The crotonyl-CoA hydration it catalyses is the same chemistry as the last round of
  beta-oxidation, but in M. sedula it runs in the anabolic direction of the cycle. So the
  term is a family-level over-annotation; it cannot be ruled out entirely (the enzyme could
  in principle hydrate crotonyl-CoA during butyrate/fatty acid catabolism), so
  MARK_AS_OVER_ANNOTATED rather than REMOVE.
- Pattern for the catalogue: same shape as pattern 1 (a recruited paralog inherits the
  ancestral family's process) — here crotonase family -> fatty acid beta-oxidation.

## GOA summary and decisions

| Term | Evidence | Action |
|---|---|---|
| GO:0003824 catalytic activity | IEA InterPro | MODIFY -> GO:0043956 |
| GO:0006635 fatty acid beta-oxidation | IEA TreeGrafter | MARK_AS_OVER_ANNOTATED |
| GO:0043956 3HP-CoA dehydratase | IDA PMID:19429610 | ACCEPT |
| GO:0043956 3HP-CoA dehydratase | IEA (Rhea/EC) | ACCEPT |
| GO:0120092 (2E)-butenoyl-CoA hydratase | IDA (new) | NEW |
| GO:0015977 carbon fixation | IDA (new) | NEW |
