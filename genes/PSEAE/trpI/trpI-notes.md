# trpI (PA0037, P11720) notes

No deep-research provider was available. Literature: PMID:1904858 and PMID:2107533 (abstracts only;
no PMC body available).

## Biology

- In vitro transcription with purified TrpI [PMID:1904858 "purified TrpI protein and indoleglycerol
  phosphate (InGP) activate transcription initiation at the trpBA promoter (trpPB) and repress
  initiation at the trpI promoter (trpPI)"]; direct effect [PMID:1904858 "activation of trpPB is
  mediated by a direct effect of TrpI on transcription initiation at trpPB"].
- Binding sites [PMID:2107533 "in the absence of InGP, the binding site of TrpI is located in the -52 to
  -77 region of the trpBA promoter; in the presence of InGP, the binding region is extended to the -32
  region"].
- No GO term for regulation of tryptophan biosynthesis; GO:2000284 is the most specific available.
- Related reviews in this folder: trpC, trpE, trpG (biosynthetic enzymes).

### Annotation decisions

- GO:0003700 (IBA, IEA), GO:0006355 (IBA, IDA, IEA), GO:2000284 (IMP): ACCEPT.
- GO:0032993 protein-DNA complex (IPI, CollecTF): KEEP_AS_NON_CORE.
- GO:0043565 (IPI, CollecTF): MODIFY to GO:0000976 transcription cis-regulatory region binding.
- The GOA file lists the CollecTF IPI rows twice; the review stub holds one row per distinct annotation.
- Action counts: ACCEPT 6, KEEP_AS_NON_CORE 1, MODIFY 1.

## PseudoCAP IBA-seed assessment

Node-level record for PTN000794521 (shared with ampR, PA4109) is kept here, trpI having the most
direct seed evidence (purified in vitro transcription).

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN000794521 | GO:0006355 regulation of DNA-templated transcription | 6 | 174 (18 taxa) | GO:0006355, IDA, PMID:1904858 (PseudoCAP) | SOUND | Abstract: purified TrpI + InGP activates trpBA and represses trpI transcription in vitro (CONFIRMED-level fact). | ampR P24734 (SOUND term; evidence code should be IMP, see ampR), E. coli GcvA P0A9F6, TtdR P45463, DmlR P76250, PgrR P77333 | Yes; four E. coli LysR regulators plus ampR, and the undirected regulation term suits a LysR clade of 174 leaves |

No GO_CENTRAL defect on this node, and no PSEUDOCAP defect on trpI.
