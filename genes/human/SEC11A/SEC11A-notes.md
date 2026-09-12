# SEC11A (P67812, SPC18) review notes

## Identity / overview
SEC11A is a single-pass type II ER membrane protein and one of the two catalytic serine-endopeptidase
subunits of the human signal peptidase complex (SPC). It is the proteolytic subunit of the SPC-A paralog
(with accessory subunits SPCS1, SPCS2, SPCS3) and cleaves N-terminal signal/leader peptides from secretory
and membrane pre-proteins as they are translocated into the ER lumen (EC 3.4.21.89). Peptidase family S26B;
Ser/His/Asp charge-relay catalytic triad (catalytic Ser-56). The other catalytic paralog is SEC11C (SPC-C).

- UniProt FUNCTION: "Catalytic component of the signal peptidase complex (SPC) which catalyzes the cleavage
  of N-terminal signal sequences from nascent proteins as they are translocated into the lumen of the
  endoplasmic reticulum"; "Specifically cleaves N-terminal signal peptides that contain a hydrophobic
  alpha-helix (h-region) shorter than 18-20 amino acids" [file:human/SEC11A/SEC11A-uniprot.txt].
- SUBUNIT: "Component of the signal peptidase complex paralog A (SPC-A) composed of a catalytic subunit
  SEC11A and three accessory subunits SPCS1, SPCS2 and SPCS3 ... Within the complex, interacts with SPCS2
  and SPCS3" [file:human/SEC11A/SEC11A-uniprot.txt].
- SUBCELLULAR LOCATION: "Endoplasmic reticulum membrane ... Single-pass type II membrane protein"
  [file:human/SEC11A/SEC11A-uniprot.txt].
- Catalytic triad ACT_SITE 56/96/122; MUTAGEN S56A "Loss of catalytic activity"; CTS helix (165-176)
  essential for catalysis [file:human/SEC11A/SEC11A-uniprot.txt].

## Key functional evidence
- Structure of the human SPC: PMID:34388369 (Liaci et al., Mol Cell 2021): "the human SPC exists in two
  functional paralogs with distinct proteolytic subunits"; "The active site is formed by a catalytic triad
  and abuts the ER membrane, where a transmembrane window collectively formed by all subunits locally thins
  the bilayer"; specificity for SPs based on hydrophobic segment length [PMID:34388369]. EXP/IDA evidence
  for catalytic and complex-membership annotations.

## Annotation review decisions
- Core MF: serine-type endopeptidase activity (GO:0004252) / signal peptidase activity (GO:0009003);
  generic peptidase activity (GO:0008233) ACCEPTed as parent.
- Core CC: signal peptidase complex (GO:0005787); ER membrane (GO:0005789); generic membrane (GO:0016020)
  KEEP_AS_NON_CORE.
- Core BP: signal-peptide cleavage captured by protein processing (GO:0016485) / protein maturation
  (GO:0051604). Note: GO:0006465 (signal peptide processing) is in the UniProt DR block but NOT in the GOA
  tsv, so it cannot be added as an existing_annotation; core_functions therefore uses GO:0016485 which is
  present.
- GO:0009615 response to virus (TAS, Reactome RSV pathway): MARK_AS_OVER_ANNOTATED — reflects generic
  signal peptidase processing of viral substrates, not a dedicated antiviral response.
- protein binding (GO:0005515) IPI rows: high-throughput captures (HuRI PMID:32296183, BioPlex
  PMID:33961781, cell-map PMID:40205054) + intra-complex SPCS2/SPCS3 (PMID:34388369). KEEP_AS_NON_CORE.

## Falcon deep-research findings (incorporated 2026-06)

The Falcon report (Edison Scientific) for SEC11A largely recapitulates literature already in the
review: Liaci 2021 SPC cryo-EM (PMID:34388369), the SPC quality-control function (PMID:36454823),
cavinafungin (PMID:28423309), the Chung 2024 Spc2 yeast mechanism (PMID:39565596), and the two
cancer biomarker papers (gastric PMID:36456166; HNSC PMID:35653344). All were already incorporated.

- NEW reference added: competitive inhibition of ER signal peptidase by non-cleavable preproteins.
  The non-cleavable variant "binds to the catalytic SPase subunit SEC11A, inhibiting SPase activity
  in a dose-dependent manner" and impairs processing in trans, including of viral polypeptides; the
  authors propose eukaryotic SPase as an antiviral drug target [PMID:26446786 "it binds to the
  catalytic SPase subunit SEC11A, inhibiting SPase activity in a dose-dependent manner"]. PubMed-
  verified (DOI 10.1074/jbc.M115.692350, J Biol Chem 2015). Added to references (relevance MEDIUM,
  correctness VERIFIED). Not in GOA, so no new GO annotation; supports SEC11A's signal peptidase
  activity (GO:0009003/GO:0004252) and its druggability. The Falcon report cites this paper only in
  its SEC11C report, but the abstract names SEC11A specifically.
- Falcon quantitative context (already consistent with review): SPC processes ~3,000 human signal
  peptides; membrane-thinning TM window reduces bilayer from ~4 nm to ~2.3-2.6 nm; ~1,500 membrane
  proteins predicted to carry cryptic SPC cleavage sites [PMID:36454823]. No annotation change.
- Falcon's "ssrn.3778304" DOI for the Liaci structure is the preprint of the published Mol Cell paper
  already cited as PMID:34388369; no separate reference added.
