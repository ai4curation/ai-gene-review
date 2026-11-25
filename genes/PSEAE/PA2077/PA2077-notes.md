# PA2077 (Q9I238) notes

## Review session 2026-11-05 (PseudoCAP IBA-seed protocol, tier 2)

Fetched with `just fetch-gene PSEAE Q9I238 --alias PA2077`; accession matches the worklist.
Unreviewed entry (ProtNLM name "Cytochrome c"). No deep-research provider. PubMed eutils and
Europe PMC searches failed during the session (HTTP 500/503); a web search
("Pseudomonas aeruginosa PA2077 PA2078 10S-dioxygenase 7,10-diol synthase") found the 2015
PLoS One follow-up, cached with `ai-gene-review fetch-pmid 26154497` (full text). Reviewed
together with PA2078 (operon partner, same PAINT node).

### Literature

- PMID:24980978 (Estupinan et al. 2014), abstract only: PA2077 and PA2078 mutants lose
  oleate-diol synthase activity; complementation assigns the first step to PA2077:
  [PMID:24980978 "gene PA2077 codes for the 10S-dioxygenase activity (10S-DOX) responsible for
  the first step of the reaction"]; enzymes act separately [PMID:24980978 "no hetero-complex
  formation is required for enzymatic activity"].
- PMID:26154497 (Estupinan et al. 2015), full text: di-heme (CXXCH x2) cytochrome c
  peroxidase-family proteins, closest to RoxA; both hemes needed for PA2077 activity
  [PMID:26154497 "both histidines (the two hemes) are required by PA2077 to display activity"];
  periplasmic, signal peptide, PhoA fusion [PMID:26154497 "a fact experimentally confirmed by
  PhoA fusion screening"]; PA2077 and PA2078 are in-paralogs with very low homology to anything
  except Pseudomonas orthologues [PMID:26154497 "PA2077 and PA2078 display very low homology to
  other proteins in the databases, except for those corresponding to their orthologues in
  other P."]; new subfamily FadCcp, outside the characterized Ccp branch.
- UniProt Q9I238: signal peptide 1-21, PANTHER PTHR30600:SF9 (BLR7738 PROTEIN), Pfam
  RoxA-like_Cyt-c (PF21419).

### Annotation decisions

- GO:0051213 dioxygenase activity (IMP): ACCEPT, core (no oleate 10S-dioxygenase term in GO;
  proposed new term).
- GO:0031408 oxylipin biosynthetic process (IMP, IBA): ACCEPT (catalyses the first step).
- GO:0020037 heme binding (IEA): ACCEPT (both CXXCH hemes required for activity).
- GO:0004130 cytochrome-c peroxidase activity (IBA, PTN000779264): MARK_AS_OVER_ANNOTATED.
  Ancestral family activity, never tested; PA2077 is a neofunctionalized FadCcp outside the
  characterized Ccp branch.
- GO:0009055 electron transfer activity (IEA): MARK_AS_OVER_ANNOTATED (enzyme, not a carrier).
- GO:0098869 cellular oxidant detoxification (IEA from GO:0004130): REMOVE; PA2077 makes a
  hydroperoxide, it does not detoxify one.
- NEW GO:0042597 periplasmic space (IC): signal peptide plus PhoA fusion data.
- Action counts: ACCEPT 4, MARK_AS_OVER_ANNOTATED 2, REMOVE 1, NEW 1.

## PseudoCAP IBA-seed assessment

Node-level assessment recorded here once (PA2077 has the most direct evidence: its 10S-DOX
step and heme mutants); PA2078 cross-references it.

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN002826263 | GO:0031408 oxylipin biosynthetic process | 2 | 7 (3 taxa) | GO:0031408, IMP, PMID:24980978 | SOUND | Mutant loses 10-H(P)OME and 7,10-DiHOME production; complementation shows PA2077 is the 10S-dioxygenase, the first step of oxylipin synthesis. | PA2078 (Q9I237; PseudoCAP IMP, same paper, SOUND) | Yes on the seeds, but the node term does not suit the clade (see below) |

### Node PTN002826263

Leaves (`.cache/paint/leaf.gaf.gz`): PA2077, PA2078, PA0007 (Q9I7B9), PA1941 (Q9I2G3),
Bradyrhizobium diazoefficiens blr7738 (Q89CQ8) and bll0021 (Q89YD3), and Rhodopirellula
baltica RB5128 (Q7UGM5). The two seeds are sound for their own genes. But the authors place
the pair as in-paralogs from a recent duplication, with very low homology to anything except
Pseudomonas orthologues, and state that no functionally characterized orthologues exist. The
node sits above that duplication and also covers two further PAO1 paralogs and proteins of
other phyla, with no evidence that any of them acts on fatty acids. The closest characterized
relative, RoxA, is a rubber oxygenase. GO_CENTRAL defect recorded on the PA2077 IBA row
(PROBABLE; the paper's tree was not compared with the PANTHER tree): the term should sit on the
PA2077/PA2078 clade, or be dropped from the node. PA2077 keeps the IBA term because its own
IMP supports it. No PSEUDOCAP defects.

PTN000779264 (GO:0004130, seeded by E. coli YhjA and P. aeruginosa CcpA) is not a PseudoCAP
seed here; it is a family-level Ccp IBD covering many RoxA/MauG-like members. Its application
to the FadCcp pair is over-annotation, recorded as MARK_AS_OVER_ANNOTATED without a defect,
because peroxidase activity was not tested.
