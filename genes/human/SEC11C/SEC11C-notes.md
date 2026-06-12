# SEC11C (Q9BY50, SPC21) review notes

## Identity / overview
SEC11C is a single-pass type II ER membrane protein and one of the two catalytic serine-endopeptidase
subunits of the human signal peptidase complex (SPC). It is the proteolytic subunit of the SPC-C paralog
(with accessory subunits SPCS1, SPCS2, SPCS3) and cleaves N-terminal signal/leader peptides from secretory
and membrane pre-proteins as they are translocated into the ER lumen (EC 3.4.21.89). Peptidase family S26B;
Ser/His/Asp charge-relay catalytic triad (catalytic Ser-68). It is the paralog of SEC11A (SPC-A).

- UniProt FUNCTION: "Catalytic component of the signal peptidase complex (SPC) which catalyzes the cleavage
  of N-terminal signal sequences from nascent proteins as they are translocated into the lumen of the
  endoplasmic reticulum"; specificity for h-regions shorter than 18-20 aa [file:human/SEC11C/SEC11C-uniprot.txt].
- SUBUNIT: "Component of the signal peptidase complex paralog C (SPC-C) composed of a catalytic subunit
  SEC11C and three accessory subunits SPCS1, SPCS2 and SPCS3 ... Within the complex, interacts with SPCS2
  and SPCS3" [file:human/SEC11C/SEC11C-uniprot.txt].
- SUBCELLULAR LOCATION: "Endoplasmic reticulum membrane ... Single-pass type II membrane protein"
  [file:human/SEC11C/SEC11C-uniprot.txt].
- Catalytic triad ACT_SITE 68/108/134; MUTAGEN S68A "Loss of catalytic activity"; CTS helix essential
  [file:human/SEC11C/SEC11C-uniprot.txt].

## Key functional evidence
- Structure of the human SPC: PMID:34388369 (Liaci et al., Mol Cell 2021): "the human SPC exists in two
  functional paralogs with distinct proteolytic subunits"; "The active site is formed by a catalytic
  triad and abuts the ER membrane ... locally thins the bilayer" [PMID:34388369]. EXP/IDA support for the
  catalytic and complex-membership annotations of SEC11C (SPC-C).

## Annotation review decisions
- Core MF: serine-type endopeptidase activity (GO:0004252) / signal peptidase activity (GO:0009003);
  generic peptidase activity (GO:0008233) ACCEPTed as parent.
- Core CC: signal peptidase complex (GO:0005787); ER membrane (GO:0005789); generic membrane (GO:0016020)
  KEEP_AS_NON_CORE.
- Core BP: signal-peptide cleavage captured by protein processing (GO:0016485) / protein maturation
  (GO:0051604). GO:0006465 (signal peptide processing) is in UniProt DR but not in the GOA tsv, so
  core_functions uses GO:0016485 (present in GOA).
- protein binding (GO:0005515) IPI rows: high-throughput captures (BioPlex PMID:28514442, HuRI
  PMID:32296183, BioPlex PMID:33961781, cell-map PMID:40205054) + intra-complex SPCS2/SPCS3 (PMID:34388369).
  KEEP_AS_NON_CORE.
- No "response to virus" annotation for SEC11C (unlike SEC11A).

## Falcon deep-research findings (incorporated 2026-06)

The Falcon report (Edison Scientific) for SEC11C is built almost entirely on literature already in
the review: Liaci 2021 SPC cryo-EM (PMID:34388369), the Zanotti/Feige SPC quality-control function
(PMID:36454823, Science 2022), Chung 2024 Spc2 yeast study (PMID:39565596), and cavinafungin
(PMID:28423309). All already incorporated.

- NEW reference added: Cui et al. 2015, competitive inhibition of ER signal peptidase by
  non-cleavable preprotein cargos [PMID:26446786 "it binds to the catalytic SPase subunit SEC11A,
  inhibiting SPase activity in a dose-dependent manner"]. PubMed-verified (DOI 10.1074/jbc.M115.692350,
  J Biol Chem 2015). Note: the abstract names SEC11A (not SEC11C) as the bound catalytic subunit, so
  relevance to SEC11C is LOW (background for the conserved eukaryotic SPase catalytic mechanism and
  druggability). Not in GOA; no new GO annotation.
- Falcon emphasises SEC11A/SEC11C paralog redundancy: SEC11A knockdown did not abolish noncanonical
  cleavage of Cx32, "consistent with compensation by SEC11C," and notes SEC11C can be hard to detect
  in some cell lines at baseline, suggesting a context-dependent/backup catalytic role
  [PMID:36454823 (Zanotti 2022) / the linked Zanotti 2023 thesis (heidok.00033417)]. This already
  matches the SEC11C review framing; no annotation change. The thesis (heidok.00033417) is a
  non-PMID secondary version of the Science paper and was not added as a separate reference.
- Falcon notes both SEC11A- and SEC11C-containing SPC paralogs cleaved a pre-beta-lactamase model
  substrate with similar efficiency in vitro (Liaci 2021), supporting that SEC11C is a fully active
  catalytic paralog [PMID:34388369]. Consistent with existing GO:0009003/GO:0004252 ACCEPT decisions;
  no change.
- Falcon's "ssrn.3778304" DOI for the Liaci structure is the preprint of PMID:34388369; not added.
