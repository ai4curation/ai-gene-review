# sqrd-1 review notes

## Session 1 (2026-10-28)

- Task named UniProt A0A061ADY3. `just fetch-gene worm sqrd-1` resolved C6KRP5 instead. Both are
  unreviewed TrEMBL entries for the same gene (sqrd-1, WormBase WBGene00008538, GeneID 178374).
  The GOA file is keyed to C6KRP5 (4 IEA rows), and A0A061ADY3 has no GO rows, so C6KRP5 is reviewed.
  A0A061ADY3 is isoform f (F02H6.5f). It lacks the N-terminal GxGxxG FAD motif present in C6KRP5
  (isoform b), so C6KRP5 is the better representative anyway.
- Literature: see sqrd-1-deep-research-manual.md. Key papers: PMID:21840852 (forward screen,
  HIF-1 induction, ethe-1 pathway), PMID:26677221 (proteostasis in H2S), PMID:39178951 (rhodoquinone,
  docking), PMID:23484030 (gei-8 paper; weak RNAi gonad phenotype in a sensitized background),
  PMID:25225291 (human SQOR glutathione acceptor).
- UniProt C6KRP5 function, catalytic activity, cofactor and location statements are all ARBA, so
  they are not cited as support. Family cross-references (PANTHER PTHR10632:SF2, InterPro IPR015904)
  are cited for membership.

## Decisions

- mitochondrion (IEA): ACCEPT under the organelle policy. The UniProt SubCell is ARBA. The claim
  holds by orthology to human SQOR and because the reaction reduces the mitochondrial quinone pool.
  Caveats: there is no worm localization experiment. The Horsman and Miller statement "SQRD-1
  localizes to mitochondria" cites Budde and Roth, who show no mitochondrial marker. The C6KRP5 gene
  model has no obvious presequence. No inner-membrane NEW row: there is only one independent line
  (homology), and the targeting sequence is unclear.
- oxidoreductase activity (IEA InterPro): MODIFY to GO:0106436.
- sulfide:quinone oxidoreductase activity GO:0070224 (IEA ARBA): MODIFY to GO:0106436, its sibling
  that names the animal (glutathione-acceptor) reaction. Same treatment as fly Sqor.
- GO:0106436 (IEA EC): ACCEPT. Rests on orthology with human SQOR (PMID:25225291); not assayed in worm.
- NEW GO:0019418 sulfide oxidation (ISS from human SQOR, supported by worm genetics). SQRD-1 performs
  the first catalytic step, so it passes the "does the work" test. Comparators: fly Sqor carries
  GO:0019418 by ISS, and the fly sulfide-oxidation GO-CAM (69d8496c00000431) types Sqor with
  GO:0106436 / GO:0019418 / mitochondrion.
- Not proposed: response to hydrogen sulfide, proteostasis/UPR, gonad development (all
  necessity/phenotype evidence).

## 2026-10-28 PR review fixes

Extended the truncated 'Neither predicted product carries an obvious N-terminal' quotes through 'mitochondrial presequence comparable to the ~40-residue extension of human SQOR'. Added supporting_entities UniProtKB:Q9Y6N5 (SQOR_HUMAN, verified in UniProt) to the NEW ISS GO:0019418 row.
