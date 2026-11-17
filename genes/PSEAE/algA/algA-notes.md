# algA (PA3551, P07874) notes

## Identity

Swiss-Prot entry, 481 aa, "Alginate biosynthesis protein AlgA"; bifunctional
phosphomannose isomerase (PMI, EC 5.3.1.8) / GDP-mannose pyrophosphorylase
(GMP, EC 2.7.7.13), type II PMI family, NCBIfam TIGR01479, PANTHER
PTHR46390:SF1. algA is the 3'-terminal gene of the alginate biosynthetic
operon (algD ... algA).
Paralogues WbpW (PA5452, A-band LPS; reviewed in this batch) and PslB (Psl).

## Literature

**Shinabarger et al. 1991, PMID:1846611 (abstract only; JBC 1991, no PMC).**
Purification of the bifunctional PMI-GMP from P. aeruginosa; PMI and GMP
co-purify through three chromatographic steps; kinetics for both reactions.
UniProt (Swiss-Prot) cites the same paper for N-terminal sequence (1-10),
catalytic activities, cofactor and kinetics, all ECO:0000269.
[PMID:1846611 "The PMI and GMP activities co-eluted in the same protein peak through successive fractionation on hydrophobic interaction, ion exchange, and gel filtration chromatography."]
[PMID:1846611 "For the GMP forward reaction, apparent Km values of 20.5 microM and 29.5 microM for D-mannose 1-phosphate and GTP, respectively, were obtained from double reciprocal plots."]
[PMID:1846611 "DNA sequencing of a cloned mutant algA gene from P. aeruginosa revealed that a point mutation at nucleotide 961 greatly decreased the levels of both PMI and GMP in a crude extract."]

The alginic acid biosynthetic process IMP from this paper rests on the algA
point mutant; the abstract does not state the mutant's alginate phenotype,
but the role of AlgA in producing the GDP-mannose precursor of alginate is
well established and curated in Swiss-Prot. Accepted, as for algC.

**Rocchetta et al. 1998, PMID:9781879** (wbpW paper) states that alginate
mannuronate and A-band rhamnose both derive from GDP-D-mannose, and that
wbpW algA double mutants still make some A-band (PslB compensates).

## PseudoCAP IBA-seed assessment

Seeds from .cache/paint/IBD.gaf; E. coli ManC (P24174) GO:0004475 IDA
PMID:4908790 (EcoCyc) from QuickGO 2026-11-05.

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN000283179 | GO:0004475 mannose-1-phosphate guanylyltransferase (GTP) activity | 2 | 30 (26 taxa) | GO:0004475, IDA, PMID:1846611 | SOUND | Purified enzyme with GMP forward and reverse kinetics; exactly the node term. Suits the PMI-GMP clade. | E. coli ManC P24174 (IDA, PMID:4908790) | Yes |

The sister IBD at the same node, GO:0009298 GDP-mannose biosynthetic process,
is seeded by ManC and WbpW (see genes/PSEAE/wbpW, where the WbpW seed row has
a PSEUDOCAP evidence-code CHECK). Both node IBDs stand; no GO_CENTRAL defect
for PTN000283179. No PSEUDOCAP defect on algA.

## Review decisions

- ACCEPT: GMP activity (IBA, IDA, IEA); PMI activity (IDA, IEA); GDP-mannose
  biosynthetic process (IBA, IEA); alginic acid biosynthetic process (IMP).
- TOO_GENERAL: polysaccharide biosynthetic/metabolic process (alginic acid
  biosynthesis accepted, is_a polysaccharide biosynthesis); nucleotidyltransferase
  activity (GO:0004475 accepted).
