# ASK8 (ASK-theta / AtSK32 / At4g00720) - manual literature research

No deep-research API was available; this summary was assembled manually from the
cached publications, the UniProt record (Q96287, KSG8_ARATH) and PubMed searches
(query: `(ASKtheta OR "ASK theta" OR At4g00720 OR AtSK32 OR "AtSK3-2") AND Arabidopsis`,
3 hits: PMID:20128883, PMID:17427040, PMID:25997736).

## Identity and family

- UniProt Q96287, 472 aa, Swiss-Prot reviewed, PE 2 (transcript level). Gene ASK8,
  synonym SK32 (TAIR AT4G00720 "SK32"), GeneID 828023.
  [file:ARATH/ASK8/ASK8-uniprot.txt "Belongs to the protein kinase superfamily. CMGC Ser/Thr
  protein kinase family. GSK-3 subfamily."]
- Kinase domain 138-423, ATP-binding Lys167, proton acceptor Asp263, conserved
  activation-loop Tyr298 (phosphotyrosine by similarity to BIN2).
  InterPro IPR039192 STKc_GSK3; PANTHER PTHR24057:SF60.
- One of 10 Arabidopsis GSK3/SHAGGY-like kinases (ASKs), grouped into four classes;
  ASK-theta is group III (with ASK-beta), whereas BIN2, ASK-iota and ASK-zeta form group II
  [PMID:20128883 "Arabidopsis thaliana possesses 10 GSK3/Shaggy-like kinases (ASKs), which can be grouped into four classes (Jonak and Hirt, 2002). BIN2, ASKι and ASKζ constitute group II."].

## Kinase activity (PMID:20128883, full text read)

- Immunoprecipitated ASK-theta-Myc phosphorylates myelin basic protein; a K167R
  kinase-dead version (ASKthetaLOF) lacks activity
  [PMID:20128883 "Plants overexpressing a kinase-dead version of ASKθ, carrying the point mutation K167R in the ATP-binding pocket (ASKθLOF-Myc), looked like the wild type (Figure 1a). As expected, no ASKθ-Myc kinase activity was observed in these plants"].
- Recombinant GST-ASK-theta directly phosphorylates BZR1, BES1 and BEH2 and autophosphorylates
  [PMID:20128883 "GST-ASKθ phosphorylated GST-BZR1, GST-BES1 and GST-BEH2, but not GST alone (Figure 5). In addition, autophosphorylation of GST-ASKθ was observed"].
- In Arabidopsis protoplasts, ASK-theta dose-dependently increases phosphorylated BEH2 (and BZR1, BES1);
  kinase-dead version has no effect; bikinin blocks it
  [PMID:20128883 "These findings indicate that ASKθ phosphorylates BES1/BZR1-like transcription factors in vitro and in vivo."].
- Independent cell-free autophosphorylation screen of 759 Arabidopsis kinases (PMID:21477822,
  abstract only) is the source of the HDA rows; GSK group kinases were among the most active.
- Claisse et al. 2007 (PMID:17427040, abstract only) studied "AtSK3-2" (K167 and R178 mutants,
  residues that match Q96287 positions 167 and 178, so this is ASK-theta): K167A is inactive,
  R178A loses ~90% primed activity; overexpressing R178A reduces floral organ cell size
  [PMID:17427040 "In vitro kinase activity assays of the mutated recombinant protein AtSK3-2-R178A showed that the \"primed activity\" of the mutated kinase was reduced by 90% while the \"non-primed\" activity was only 20% reduced compared to the wild-type protein kinase."].

## Brassinosteroid signalling (PMID:20128883)

- Endogenous ASK-theta activity rises in bri1-1 and cpd and falls with brassinolide
  [PMID:20128883 "showing that the protein kinase activity of ASKθ is negatively regulated by BR levels and by the BRI1 receptor complex."].
- 35S:ASK-theta lines are bri1-like dwarfs, BR-insensitive, ABA-hypersensitive, accumulate BRs,
  and show bri1-like marker gene expression; severity tracks kinase activity.
- Interacts (Y2H) with BEH2, BES1 and BZR1; ASK-beta (closest homologue) does not.
- Authors' model: [PMID:20128883 "Our data indicate a model in which ASKθ acts in a BR-regulated manner downstream of BRI1 to phosphorylate BES1/BZR1-like transcription factors."]
- Loss of function: knockouts have normal growth, implying redundancy with BIN2, ASK-iota, ASK-zeta
  [PMID:20128883 "The normal growth phenotype of knock-outs of ASKθ (Claisse et al., 2007) suggests that ASKθ works in parallel with BIN2, ASKι and ASKζ in the BR response pathway."].

## Localization

- ASK-theta-YFP mainly nuclear with low cytoplasmic signal, in tobacco leaves, Arabidopsis protoplasts
  and stable lines [PMID:20128883 "ASKθ-YFP mainly localized to the nucleus, but low levels were also observed in the cytoplasm (Figure 4)."].

## Nomenclature caution

- Dong et al. 2015 (PMID:25997736) label ASK-beta (At3g61160) as "AtSK32"; UniProt/TAIR assign SK32
  to At4g00720 (ASK8/ASK-theta), and the K167/R178 numbering in Claisse 2007 matches At4g00720.
  PMID:25997736 is therefore about At3g61160 (ASK-beta), not this gene, and is not used.
