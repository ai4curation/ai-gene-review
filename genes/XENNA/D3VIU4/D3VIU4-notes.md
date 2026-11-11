# D3VIU4 (XNC1_0570, "fliY") notes

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

No notes file existed before this session; this is the first entry. ProtNLM2 files and the
`D3VIU4-hypotheses/` prediction folder were not consulted.

### Identity

- D3VIU4 is the full-length, canonical (and only) UniProt product of locus XNC1_0570 in
  Xenorhabdus nematophila ATCC 19061: 262 aa, SignalP signal peptide 1-28, single SBP_bac_3
  domain 40-259 (SMART SM00062). Not a fragment, isoform or alternative gene model. TrEMBL,
  PE 3; no experimental work on this protein exists. The gene name "fliY" is a submitter
  transfer from E. coli (where fliY sits near the flagellar genes) and carries no motility
  meaning.

### Evolutionary placement (see `D3VIU4-bioinformatics/RESULTS-rereview.md`)

- PANTHER PTHR35936:SF34 (YCKB-RELATED) with B. subtilis TcyA (P42199) and YckB (P42400);
  CDD cd13711 PBP2_Ngo0372_TcyA.
- The E. coli high-affinity cystine SBP TcyJ/FliY (P0AEM9) is in a DIFFERENT subfamily
  (SF35, cd13712), as is Ngo0372 (Q5F9M1). The earlier review and the falcon deep-research
  report treated D3VIU4 as the E. coli FliY ortholog and transferred E. coli kinetics
  (Km ~30 nM); that transfer is not supported by subfamily placement. Identity to E. coli
  TcyJ is 39%, versus 48% to TcyA and 48% to Ngo0372.
- Despite the different subfamily, Xenorhabdus has no SF35 member, and D3VIU4 sits in an
  SBP-ATPase-permease cluster (XNC1_0570-0572; yecC, yecS/TcyL-named) that matches the
  E. coli tcyJ-tcyN-tcyL arrangement. A second SF34 SBP, XNC1_0574 (D3VIU8, 57% identity),
  is just downstream; it is unknown which SBP(s) the permease uses.
- The two Ngo0372 pocket residues tested by mutagenesis (Tyr59, crucial for L-cystine
  binding, and Trp97 in the paper's numbering) align to D3VIU4 Tyr49 and Trp87.
- Literature: B. subtilis TcyABC (YckKJI) mediates L-cystine uptake [PMID:15262924
  "The symporter YhcL and two ATP binding cassette transporters, YtmJKLMN and YckKJI, were
  shown to mediate L-cystine uptake in Bacillus subtilis."]; Ngo0372 binds L-cystine with
  Kd 21 nM [PMID:22138345 "Dissociation constants of 21 and 33 nM for L-cystine and
  L-selenocystine, respectively, were determined by isothermal titration calorimetry."];
  E. coli FliY [PMID:26350134 "The FliY periplasmic protein binds cystine and had been
  proposed to be the periplasmic binding component of an import system"]. The same paper
  cautions that similarity alone is approximate [PMID:26350134 "periplasmic binding proteins
  and secondary transporters may exhibit significant similarity to FliY and YdjN without
  employing cystine as a substrate."].
- PAINT: PTN000438641 (taxon:2) carries IBD GO:0030288 and GO:0016597 in PTHR35936, but
  D3VIU4 has no IBA rows in GOA, so its descent from that node is not established here.

### Decisions

- GO:0030288 periplasmic space (IEA ARBA): ACCEPT, supported by the SignalP signal peptide
  and SBP family membership, not by the ARBA rule itself.
- GO:0030313 cell envelope (IEA SubCell): correct but general; MODIFY to GO:0030288
  (previously KEEP_AS_NON_CORE, which the repo rule disallows for a too-general term).
- NEW rows kept (amino acid binding; L-cystine transport) but re-grounded on SF34/TcyA,
  pocket conservation and synteny rather than E. coli orthology; complex NEW refined from
  GO:0043190 to GO:0055052 (substrate-binding subunit-containing ABC complex).
- Description rewritten to drop the E. coli Km and to state the subfamily caveat.

### Relative to review next

B. subtilis TcyA (P42199), same PANTHER subfamily SF34, experimentally implicated in
L-cystine uptake. No review in the repo. E. coli TcyJ (P0AEM9) is the best-studied
cystine SBP but is in SF35; it also has no review.

### Family review

`interpro/panther/PTHR35936/PTHR35936-review.yaml` records D3VIU4 in SF34, agreeing with
UniProt. No placement disagreement. No module in `modules/` covers bacterial cystine ABC
import.
