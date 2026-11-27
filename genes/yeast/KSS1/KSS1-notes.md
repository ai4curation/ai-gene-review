# KSS1 (YGR040W, UniProt P14681) curation notes

## Identity

- Mitogen-activated protein kinase KSS1, 368 aa, TEY activation-loop motif
  (Thr183/Tyr185), EC 2.7.11.24; PANTHER PTHR24055 (MAPK). Paralog of FUS3
  (the two are ~55% identical) [PMID:23953117 "Fus3 and Kss1 are 55 % identical,
  are both targets of the MAPKK Ste7"].

## Pathway position and activation

- Ordered Ste11 -> Ste7 -> Kss1; Kss1 dually phosphorylated on Thr183 and Tyr185
  after pheromone [PMID:7579701 "In MATa haploids exposed to alpha-factor, Kss1
  was rapidly phosphorylated on both Thr183 and Tyr185, and both sites were
  required for Kss1 function in vivo"; "suggesting an order of function:
  Ste11-->Ste7-->Kss1"].
- High-affinity docking complex with Ste7 (Kd ~5 nM), independent of Ste5;
  Ste7 phosphorylates Kss1 and Kss1 phosphorylates Ste7 [PMID:8668180 "Kss1 and
  Fus3 could each form a tight complex (Kd of approximately 5 nM) with Ste7 in
  the absence of any additional yeast proteins"].
- Kss1 is intrinsically an excellent Ste7 substrate and does not need the Ste5
  scaffold's allosteric unlocking that Fus3 requires [PMID:19303851 "We find that
  Fus3 is intrinsically a poor substrate for activated Ste7, while Kss1 is
  intrinsically a very good substrate."].
- Catalytic activity required for signalling [PMID:7579701 "Catalytic activity
  was essential for Kss1 function in signal transmission"].

## Filamentous / invasive growth (core)

- Kss1 is the MAPK of the filamentous growth pathway; Fus3 is the mating MAPK
  [PMID:9393860 "The Fus3 MAPK regulates mating, whereas the Kss1 MAPK regulates
  filamentation and invasion."].
- Dual role: activated Kss1 stimulates, unphosphorylated Kss1 represses, via
  direct binding to Ste12 [PMID:9744865 "unphosphorylated Kss1 binds directly to
  the transcription factor Ste12, that this binding is necessary for
  Kss1-mediated repression of Ste12"; "the inhibitory function of Kss1 requires
  neither"].
- Repression requires Dig1 and Dig2 [PMID:9860980 "Herein we show that two
  nuclear proteins, Dig1 and Dig2, are required cofactors in Kss1-imposed
  repression."].
- Dig1/Dig2 identified as Kss1 two-hybrid partners and substrates
  [PMID:8918885 "Kss1 binds specifically to a GST-Dig1 fusion in the absence of
  any other yeast protein."; "Dig1 colocalizes with Kssl in the nucleus"].
- Kss1 relocalises to the nucleus during filamentous growth [PMID:18417610
  "they localized predominantly to the nucleus during filamentous growth"].

## Pheromone response (partial redundancy with Fus3)

- Kss1 is activated by pheromone in wild-type cells and contributes to
  pheromone-induced gene expression; Fus3 limits Kss1 activation
  [PMID:11583629 "Kss1 is rapidly phosphorylated and potently activated by
  mating pheromone in wild-type cells"].
- UniProt: "FUS3 can partially compensate for the lack of KSS1".
- Deep research (falcon): single kss1 or fus3 deletions are fertile, double
  mutant is sterile.

## Localization

- Nucleus by immunofluorescence [PMID:7579701 "Kss1 is concentrated in the
  nucleus"]; shuttles nucleus/cytoplasm (UniProt). UniProt SubCell "Periplasm"
  (cited to PMID:11781566, a Fus3/Ste5 localisation paper) is not biologically
  plausible for an intracellular kinase lacking a signal peptide; the
  resulting GO:0042597 IEA is removed.
- Bud neck (PMID:27400980): Kss1 overexpression suppresses slt2 rim101
  lethality and raises Bni4 phosphorylation; treated as a non-core, multicopy
  suppression phenotype.

## Protein-binding rows (GO:0005515)

Partners: STE7 (P06784), STE11 (P23561), STE12 (P13574), DIG1 (Q03063),
DIG2 (Q03373), BCK2 (P33306), FUS3 (P16892).

- Ste7 -> MODIFY to GO:0031434 MAPKK binding (direct, Kd ~5 nM, PMID:8668180).
- Ste11 -> MODIFY to GO:0031435 for low-throughput two-hybrid rows
  (PMID:7851759, PMID:8062390); REMOVE the HTP AP-MS row (likely Ste5/Ste7
  bridged).
- Ste12 -> MODIFY to GO:0061629 (direct binding, PMID:9744865).
- Dig1/Dig2 -> MODIFY to GO:0001222 transcription corepressor binding (Dig1 has
  GO:0003714 IDA; Dig1/Dig2 are required cofactors of Kss1 repression).
- Bck2, Fus3 -> REMOVE (no informative MF; removal does not mean the
  interaction is false).

## Candidate new annotation

- GO:2000218 negative regulation of invasive growth in response to glucose
  limitation: Kss1 itself performs the repression by binding Ste12
  (kinase-independent); comparator Dig1 carries this term by IGI from
  PMID:8918885. Proposed as NEW.
- Considered GO:0003714 transcription corepressor activity for the
  Kss1-Ste12 repression, but left as a question (Kss1 is not known to be
  promoter-bound in the repressive state).
