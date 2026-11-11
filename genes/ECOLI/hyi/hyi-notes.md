# hyi (P30147) notes — E. coli K-12 hydroxypyruvate isomerase

## Deep research
- 2026-10-23: `just deep-research ECOLI hyi --provider perplexity` failed
  ("Provider 'perplexity' not available. Available: falcon, openscientist";
  agentapi not in PATH). No deep-research file was generated; review based on
  cached publications and the UniProt record.

## Key findings
- Hyi (gip, ybbG, b0508) is hydroxypyruvate isomerase, EC 5.3.1.22
  [PMID:10561547 "We found a significant activity of hydroxypyruvate isomerase in Escherichia coli clone cells harboring an E. coli gene (called orf b0508 or gip)"].
- Strict specificity, no cofactor
  [PMID:10561547 "The enzyme required no cofactor. It exclusively catalyzed the isomerization between hydroxypyruvate and tartronate semialdehyde."];
  Km 12.5 mM for hydroxypyruvate, optimum pH 6.8-7.2 (same source).
- UniProt: no sugar isomerase or racemase activity
  [file:ECOLI/hyi/hyi-uniprot.txt "Does not catalyze the isomerization of D-fructose to D-"].
- Homodimer [PMID:10561547 "The enzyme had a molecular mass of 58 kDa and was composed of two identical subunits."].
- Genomic context: immediately downstream of gcl (glyoxylate carboligase), which
  makes tartronate semialdehyde from glyoxylate
  [PMID:8440684 "catalyzes the condensation of two molecules of glyoxylate to give tartronic semialdehyde, a key intermediate in glyoxylate catabolism"].
- Dispensable: [PMID:8440684 "disruption of the chromosomal copy of orf258 did not affect growth on glyoxylate or glycolate"]
  (orf258 = hyi, 258 aa).
- Family: xylose isomerase-like TIM barrel; NCBIfam TIGR03234 (OH-pyruv-isom);
  PANTHER PTHR43489:SF13. Predicted active-site residues 143 and 240 by similarity.

## Curation decisions
- GO:0008903 hydroxypyruvate isomerase activity (IBA/IDA/IEA): ACCEPT, core.
- GO:0042803 protein homodimerization activity (IDA): KEEP_AS_NON_CORE.
- GO:0046487 glyoxylate metabolic process (IBA/IDA): ACCEPT at pathway level; the
  in vivo direction of the reaction is unknown, so no more specific catabolic term.
- No NEW annotations proposed.

## Open questions
- Physiological direction and conditions where Hyi matters (not needed for growth
  on glyoxylate/glycolate).
