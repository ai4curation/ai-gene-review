# wzz (PA3160, G3XCY2, Wzz1) review notes

No deep-research provider was available. Sources: UniProt record (TrEMBL), cached PMID:9045803 and
PMID:12534470 (abstract only; no PMC full-text XML obtainable), PMID:24309320 and PMID:20418877 (full
text in the cache). PubMed MCP searches on 2026-11-05 returned no hits (search service failing).

## Function

- Wzz1 (PA3160, encoded in the B-band O-antigen cluster) regulates the chain-length distribution of
  B-band (O-specific antigen) O-polysaccharide made by the Wzx/Wzy pathway
  [PMID:9045803 "This study describes the molecular characterization of the corresponding wzz (rol) gene, responsible for modulating O-antigen chain length."].
- wzz knockouts in O5 and O16 change chain-length distribution; the gene complements O5, O16 and
  E. coli wzz mutants
  [PMID:9045803 "The P. aeruginosa O5 wzz gene complemented both O5 and O16 wzz mutants as well as an E. coli wzz mutant."].
- Wzz1 forms dimers in vivo (Wzz2 octamers) and co-precipitates with O5 polymer; modal chain length is
  set before ligation to lipid A-core [PMID:12534470 "In vivo protein cross-linking followed by Western immunoblotting indicated that Wzz1 forms dimers whereas Wzz2 forms octamers."].
- Wzy cytoplasmic-loop mutations alter Wzz1- but not Wzz2-specified modality, suggesting a Wzz1-Wzy
  interaction [PMID:24309320 "regulation of polymer length is affected by interaction of Wzz with Wzy"].
- Sequence: 348 aa; Phobius TM helices 29-48 and 319-343 flanking a large periplasmic domain; Pfam
  PF02706 (Wzz N-terminal). No C-terminal cytoplasmic BY-kinase (Walker A/B) domain: the chain ends 5
  residues after TM2. Polysaccharide co-polymerase PCP-1 class.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN000794252 | GO:0005886 plasma membrane | 5 | 62 (23 taxa) | GO:0098567 periplasmic side of plasma membrane, IDA, PMID:9045803 (PseudoCAP) | UNVERIFIABLE | The term is right (two TM helices flanking a periplasmic domain; PCP-1 family topology), but the abstract reports genetics, complementation and sequence analysis only; whether the full text has a topology or fractionation assay cannot be seen. No defect filed. | E. coli Wzc P76387 and Etk P38134 (IDA plasma membrane, EcoCyc), E. coli FepE P26266 (IDA, PMID:15919996), PAO1 Wzz2 PA0938 Q9I520 | Yes; three E. coli seeds have IDA plasma-membrane annotations. No GO_CENTRAL defect for GO:0005886. |

Node-level GO_CENTRAL defect (recorded here, cross-referenced from PA0938): PTN000794252 also carries
an IBD of GO:0004713 protein tyrosine kinase activity, seeded by the E. coli BY-kinases Wzc P76387 and
Etk P38134. The node also contains PCP-1 chain-length regulators that lack the kinase domain (Wzz1,
Wzz2/PA0938, E. coli FepE; the fepE review in this repository reached the same conclusion), so the
kinase term does not suit the clade. The kinase IBD should move to the Wzc/Etk (PCP-2a) subclade.
CONFIRMED (sequence checked: no kinase domain after TM2).

Defects recorded: PSEUDOCAP 0; GO_CENTRAL 1 (WRONG_TERM at PTN000794252 for GO:0004713, CONFIRMED).
