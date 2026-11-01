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
- **The error also runs the other way:** ARBA rules ARBA00067001 (name)
  and ARBA00052213 (EC 1.2.1.75 catalytic activity) name the true ASD,
  Msed_1700, as a malonyl-CoA reductase. Both rules have only two
  conditions: FunFam 3.40.50.720:FF:000411 (itself named
  "Aspartate-semialdehyde dehydrogenase", covering both paralogs) and the
  taxon Archaea. Of the 40 archaeal UniProt entries named EC 1.2.1.75, 19
  match MCR-type CDD models, 17 match only ASD-type models (probably
  misnamed true ASDs, including Msed_1700 and *Sulfurisphaera tokodaii*
  ST1242) and 4 match neither. No GO row derives from this naming yet.
  The Msed_1700 review (genes/METS5/Msed_1700/) accepts its ASD terms.
- **Possible fix:** split the malonyl-CoA reductase clade into its own
  PANTHER subfamily, and add the CDD models as conditions in the ARBA
  rules: cd23940/cd24150 for MCR, cd18130/cd02315 for ASD. NCBIfam
  TIGR00978 (asd_EA) cannot be used, because both paralogs carry it.
- **Structured record:** rule reviews
  `rules/arba/ARBA00067001/ARBA00067001-review.yaml` (name) and
  `rules/arba/ARBA00052213/ARBA00052213-review.yaml` (catalytic activity),
  both action MODIFY, with the per-protein classification in
  `rules/arba/ARBA00067001/RESULTS.md`: of 38 rule-annotated entries, 17
  are MCR-type, 17 ASD-type and 4 unclassified. No GO row derives from the
  rules yet, but a new malonyl-CoA reductase GO term would carry the error
  into GO through Rhea-to-GO mapping, so the rules should be fixed first.
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

## 8. InterPro2GO puts catalytic activity on non-catalytic proteasome alpha subunits

- **Pipeline:** InterPro2GO (GO_REF:0000002), IPR019982 (archaeal
  proteasome alpha subunit) to threonine-type endopeptidase activity
  (GO:0004298) with `enables`.
- **Example:** HALVD/psmA1 (Q9V2V6). The alpha subunits form the gated
  outer ring of the 20S core particle; the catalytic nucleophile is the
  N-terminal threonine of the beta subunit. The InterPro row and three
  endopeptidase rows (2 IDA, 1 ARBA IEA) were modified to structural
  constituent of proteasome (GO:0140756), the same choice as the repo's
  human PSMA1 review, with `contributes_to` GO:0004298 in core_functions.
- **Scale:** about 786 archaeal GO:0004298 rows in QuickGO come from this
  mapping.
- **Possible fix:** drop the mapping or change it to `contributes_to`.

## 9. Ubiquitin-dependent terms on organisms without ubiquitin

- **Pipeline:** InterPro2GO, IPR000426 (proteasome alpha subunit N-terminal
  domain) to ubiquitin-dependent protein catabolic process (GO:0006511).
- **Example:** HALVD/psmA1. Archaea have no ubiquitin; *Haloferax* uses
  SAMP conjugation, and its link to proteasomal degradation is indirect.
  The row was removed.
- **Scale:** about 888 of the 910 archaeal GO:0006511 rows in QuickGO come
  from this mapping.
- **Possible fix:** add a Eukaryota taxon restriction to the mapping.
- **Implemented as CR-0003 (2026-10-31).** Evaluated on all 610 archaeal
  proteomes with an IPR000426 member: the ubiquitin relay is absent from 501
  complete proteomes, so the rule removes 733 of the 888 archaeal rows (83%).
  It keeps the term in two Asgard archaea and *Candidatus* Methanoplasma
  termitum, which encode a UBC E2, a ubiquitin-like protein and a RING
  protein, and in 106 proteomes too incomplete to call the relay absent
  (`rules/curated/context/RESULTS.md`).

## 10. Microbial rhodopsin pumps annotated as channels

- **Pipeline:** InterPro2GO, IPR018229 (rhodopsin retinal-binding site) to
  monoatomic ion channel activity (GO:0005216); proteorhodopsin also gets
  light-activated channel activity (GO:0010461) through IPR017402.
- **Example:** HALSA/bop (P02945), bacteriorhodopsin, a light-driven proton
  pump. The channel row was removed. The same row is on every microbial
  rhodopsin pump checked: halorhodopsins P0DMH7, P15647 and P33742,
  sensory rhodopsin II P42196 and proteorhodopsin Q9F7P4.
- **Why it is wrong:** among microbial rhodopsins only the algal
  channelrhodopsins are channels.
- **Possible fix:** remove the channel mapping from IPR018229 (it is a
  retinal-binding-site signature shared by pumps, sensors and channels).

## 11. The Chloroflexus 3-hydroxypropionate cycle term on the archaeal 3HP/4HB cycle

- **Pipelines:** UniProt ARBA (GO_REF:0000117), plus one IDA row.
- **Problem:** GO:0043427 carbon fixation by 3-hydroxypropionate cycle is
  defined as the pathway "by which two molecules of carbon dioxide are fixed
  to form glyoxylate", with malyl-CoA cleaved to acetyl-CoA and glyoxylate.
  That is the Chloroflexus bicycle. The crenarchaeal 3HP/4HB cycle regenerates
  acetyl-CoA through 4-hydroxybutyrate and has no malyl-CoA lyase.
- **Scale:** 729 of the 766 GO:0043427 annotations in QuickGO (2026-10-31) are
  on archaeal proteins, 727 of them from ARBA.
- **Examples:** METS5/Msed_1456 (IDA and ARBA rows modified); Msed_0709,
  Msed_2001, Msed_1424 and Msed_0406 use GO:0015977 carbon fixation instead.
- **Possible fix:** create the proposed term "carbon fixation by
  3-hydroxypropionate/4-hydroxybutyrate cycle" and repoint the ARBA rules to it.

## 12. A Swiss-Prot name and EC number for the wrong step of a pathway

- **Example:** METS5/Msed_1424 (A4YGN0) is named succinate-semialdehyde
  dehydrogenase (acetylating), EC 1.2.1.76, with RHEA:26450. The purified
  native enzyme is the NADPH succinic semialdehyde reductase, the next step
  (PMID:19684143), and EC 1.2.1.76 belongs to Msed_0709 from the same paper.
  The protein is a zinc alcohol dehydrogenase (IPR002328), not an aldehyde
  dehydrogenase.
- **Risk:** no GO row derives from it yet, but a succinyl-CoA reductase GO
  term mapped from RHEA:26450 would carry the error into GO.

## 13. EC-to-GO chain-length mismatch

- **Example:** METS5/Msed_0406. EC 6.2.1.2 (butanoate--CoA ligase) maps to
  GO:0031956 medium-chain fatty acid-CoA ligase activity, which GO defines for
  C6 to C12; the enzyme acts on C2 to C5 acids. Modified to GO:0031955
  short-chain fatty acid-CoA ligase activity, including the IDA row.

## 14. TreeGrafter and SubCell terms from the wrong reaction or a weak prediction

- **Synthase for synthetase:** PANTHER node PTN008683229 (PTHR43605) gives
  Msed_0406, an AMP-forming acyl-CoA ligase, GO:0004321 fatty-acyl-CoA
  synthase activity (the fatty acid synthase reaction) and fatty acid
  biosynthesis, in an archaeon whose membrane lipids are isoprenoid ethers.
- **Membrane from one predicted helix:** Msed_0406 has a UniProt
  transmembrane prediction (ECO:0000255) inside its N-terminal domain, but was
  purified from the soluble fraction and has crystal structures. This is a
  sub-pattern of pattern 4.
- **Family-founder process terms:** Msed_2001 inherits fatty acid
  beta-oxidation from the ECHS1-named crotonase subfamily, and Msed_1456
  acetyl-CoA biosynthesis from the acetyl-CoA synthetase family (pattern 1).

## 15. An experimental row with the wrong cofactor variant of the activity

- **Example:** METS5/Msed_1426 (A4YGN2), acryloyl-CoA reductase. A UniProt IDA
  row assigns GO:0043958 acryloyl-CoA reductase (NADH) activity, but the cited
  paper (PMID:19429610) reports that the enzyme "did not act on either NADH or
  crotonyl-CoA". Corrected to GO:0043957, the NADPH term, which an EXP row
  already carried. Worth reporting to UniProt.

## 16. Whole-complex activity on a single subunit

- **Example:** METS5/Msed_1375, the carboxyltransferase subunit of the
  acetyl-CoA/propionyl-CoA carboxylase, received propionyl-CoA carboxylase
  activity from TreeGrafter and ligase activity from InterPro2GO; the ATP-using
  ligation belongs to the biotin carboxylase subunit. The PANTHER node also
  misses the enzyme's equal activity on acetyl-CoA. A wider form of pattern 8.

## Related findings from round 2

- **Under-annotation reaches the best-studied archaeal proteins too.**
  bop is the only gene product in GOA annotated to light-driven active
  monoatomic ion transmembrane transporter activity (GO:0015454), with no
  ion named; no archaeal protein in GOA has any retinal-binding term. Two
  of its three experimental rows come from one 1973 abstract. psmA1's six
  IDA rows come from two papers by one lab. See pattern 5.
- **ESCRT-III vacuolar transport (pattern 3) hits paralogs arbitrarily.**
  In *M. sedula*, only Msed_1695 (CdvB2) carries the row, because only it
  also matches Pfam PF03357 / IPR005024; its close paralog Msed_2179
  (CdvB1) escapes. The 41 InterPro2GO rows span about 36 archaeal taxa.
- **Unsupported process terms on ammonia monooxygenase.** The merged NITRP
  amoA review dropped an anammox term (anaerobic respiration, using
  ammonium as electron donor, GO:0019331) from an aerobic ammonia
  oxidizer, and found that GO:0019409 (aerobic respiration, using ammonia
  as electron donor) is defined through hydrazine intermediates, which
  does not fit aerobic nitrification.

## Structured records

The upstream-fixable patterns are recorded in machine-readable form, ready to
send to the resource that owns them:

| Pattern | Record | Verdict | Replacement rule |
|---|---|---|---|
| 1 (ARBA naming) | `rules/arba/ARBA00067001/ARBA00067001-review.yaml`, `rules/arba/ARBA00052213/ARBA00052213-review.yaml` | MODIFY: require MCR-type CDD models | CR-0004 |
| 3 (ESCRT-III vacuolar transport) | `projects/INTERPRO/interpro2go.sssom.yaml`, IPR005024 to GO:0007034 | broadMatch | CR-0001 (Eukaryota), CR-0002 (archaeal Cdv cytokinesis) |
| 6 (default NAD binding) | same file, IPR000534 to GO:0051287 | broadMatch, narrow | none yet |
| 8 (catalytic activity on proteasome alpha) | same file, IPR019982 to GO:0004298 | REMOVE | not needed |
| 9 (ubiquitin terms in archaea) | same file, IPR000426 to GO:0006511 | broadMatch | CR-0003 (module context, evaluated per proteome) |
| 10 (rhodopsin pumps as channels) | same file, IPR018229 to GO:0005216 and IPR017402 to GO:0010461 | REMOVE | not needed |

The replacement rules live in [rules/curated](../../rules/curated/README.md).
A taxon or module condition is used only where the lineage or the missing
component is what separates right from wrong members; where the term is wrong
for every member, the record is a removal and no rule is needed.

Patterns 2 (plant-seeded PAINT node on lacS) and 4 (SubCell nucleoid
mapping) are not yet in a structured record: the first belongs with PANTHER
IBA reviews (see [IBA_REVIEW](../IBA_REVIEW.md)), the second with UniProt's
SubCell-to-GO mapping, which has no review file in this repository yet.

