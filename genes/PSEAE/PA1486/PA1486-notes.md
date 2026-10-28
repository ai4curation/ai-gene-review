# PA1486 (Q9I3M6) notes

## Identity

- PA1486 is *bapF*, the beta-peptidyl aminopeptidase BapF of *P. aeruginosa* PAO1. The Pseudomonas Genome
  Database lists PA1486 as *bapF* ("beta-peptidyl aminopeptidase"), and MEROPS files BapF as P01.003,
  matching the `DR MEROPS; P01.003` line on Q9I3M6.
- Family: peptidase S58/DmpA (Pfam PF03576 Peptidase_S58; InterPro IPR005321 Peptidase_S58_DmpA; CDD
  cd02253 DmpA; PANTHER PTHR36512 D-AMINOPEPTIDASE). These are N-terminal-nucleophile (Ntn) hydrolases that
  autoprocess at a Gly-Ser bond and use the new N-terminal serine as nucleophile.
- Own sequence check (UniProt sequence, positions 230-245: `EGTPGMGSIVVILATD`): residue 237 is Ser,
  preceded by Gly236, i.e. the canonical DmpA-family Gly-Ser autoprocessing site. This matches the
  "catalytic Ser" S237 mutated in PMID:23728237.

## Literature

- [PMID:23728237 "We specifically examined β-peptidyl aminopeptidase of Pseudomonas aeruginosa PAO1 (BapF)
  to assess the effects of mutation of catalytic Ser with Cys or Thr on its catalytic ability."]
- [PMID:23728237 "Recombinant BapF and its S237C mutant exhibited p-nitroaniline release activity toward
  β-homo-Gly-p-nitroanilide (βhGly-pNA)"] — direct in vitro aminopeptidase (N-terminal beta-amino acid
  release) activity of the purified recombinant enzyme.
- [PMID:23728237 "Wild-type BapF showed βhGly-βhGly-pNA synthetic activity, but the product vanished in a few
  minutes and converted to free βhGly."] — aminolysis (transpeptidation) in addition to hydrolysis.
- The cached paper is abstract-only. Earlier BapF work from the Arima group (2010-2011, Appl Environ
  Microbiol / FEBS J) is not in the cache; I did not find it via the PubMed MCP search.
- No physiological substrate or phenotype is known for PA1486.

## GO terms

- No GO term exists for beta-peptidyl aminopeptidase (EC 3.4.11.25); searched OLS and the local GO db.
- GO:0070009 serine-type aminopeptidase activity (child of GO:0004177) fits the catalytic-Ser Ntn
  mechanism shown by the S237 mutagenesis.

## Annotation decisions

- GO:0004177 aminopeptidase activity, IDA PseudoCAP (PMID:23728237): MODIFY to GO:0070009 serine-type
  aminopeptidase activity (the paper itself identifies Ser237 as the catalytic residue). The aminopeptidase
  claim is sound.
- GO:0004177 aminopeptidase activity, IBA (PTN002194605): MODIFY to GO:0070009 (consistent with the IDA row; the node term itself is sound for the clade). The seed is direct biochemistry and
  aminopeptidase activity is the characterised activity of the DmpA family (D-aminopeptidase DmpA,
  beta-peptidyl aminopeptidases BapA/BapF).

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN002194605 | GO:0004177 aminopeptidase activity | 1 (sole) | 12 (12 taxa) | GO:0004177, IDA, PMID:23728237 (PseudoCAP) | SOUND | Purified recombinant BapF (PA1486) releases p-nitroaniline from beta-homoGly-pNA, a direct aminopeptidase assay. The generic aminopeptidase term (not a beta-peptide-specific one) is appropriately broad for a 12-leaf S58/DmpA subclade whose members include D-aminopeptidases and beta-peptidyl aminopeptidases with differing stereo-specificity. |
