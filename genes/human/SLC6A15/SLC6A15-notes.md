# SLC6A15 (B0AT2) review notes

- B0AT2 is a Na+-dependent, Cl--independent, concentrative symporter for small hydrophobic
  neutral amino acids, with a strong preference for branched-chain amino acids (Leu, Val, Ile)
  plus Met; also carries proline (electrogenic 1:1 proline:Na+) and several low-affinity neutral
  amino acids [PMID:16226721 "SBAT1 exhibited a strong preference for branched-chain amino acids (BCAA) and methionine"].
- Brain-restricted expression; proposed to supply amino-acid (BCAA) nitrogen for neurotransmitter
  biosynthesis. Surface density is PKC-regulated
  [PMID:16226721 "PKC activation reduced the plasma-membrane population of SBAT1 protein"].

## Neurotransmitter-exclusion argument
- The NAS/TAS neurotransmitter-transporter rows derive from pre-functional SLC6 family placement
  [PMID:11112352 "the substrates transported by these transporters remain unknown"]. Functional
  characterization shows B0AT2 EXCLUDES neurotransmitters
  [PMID:16226721 "SBAT1 excluded aromatic or charged amino acids, beta-amino acids, glycine, and GABA."].
- Because glycine and GABA are explicitly excluded, GO:0005326 neurotransmitter transmembrane
  transporter activity is FALSE for this gene (not merely over-reaching) → changed to REMOVE.
  GO:0006836 neurotransmitter transport (process) rows kept MARK_AS_OVER_ANNOTATED (pathway context).
  Contrast SLC6A14, which carries glycine and so stays MARK_AS_OVER_ANNOTATED there.

## Decisions
- Item-1 action framework (2026-11-14 ruling): generic substrate-named amino-acid parent terms
  (GO:0003333, GO:0006865, GO:0015171) treated as ACCEPT (substrate-named, respectably specific).
  Bare parents set to TOO_GENERAL: GO:0015370 solute:sodium symporter activity (bare solute,
  entailed by GO:0005295/GO:0015657) and GO:1905039 carboxylic acid transmembrane transport
  (broader chemical class, parent of amino-acid transport).
- GO:0016020 membrane: action follows whether the row's own evidence resolves the compartment.
  The IDA (PMID:16226721) and NAS rows carry plasma-membrane-resolving evidence and are
  MODIFY -> GO:0005886; the IEA (GO_REF:0000120) electronic row stops at "membrane" on its own
  evidence and is TOO_GENERAL (consistent with SLC6A14, whose membrane rows are all electronic).
- Minor/low-affinity substrate facets changed ACCEPT → KEEP_AS_NON_CORE: GO:0015655 (alanine:Na+),
  GO:0140901 (asparagine:Na+), GO:0006867 (asparagine transport), GO:0032328 (alanine transport).
- Five bare HuRI GO:0005515 rows REMOVEd; dropped the paper-title supporting_text on those rows.
