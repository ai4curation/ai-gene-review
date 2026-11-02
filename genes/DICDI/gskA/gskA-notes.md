# gskA (GSK-3, P51136) – Dictyostelium discoideum – curation notes

## Deep research status

`just deep-research-falcon DICDI gskA --fallback perplexity-lite` was run (2026-10-05) and
failed: Falcon (Edison API) returned `402 Payment Required`, and the perplexity-lite
fallback was not available ("'perplexity' not available. Available: openai, falcon,
openscientist"). No deep-research file was produced. The review is therefore based on
the cached publications (16 PMIDs, `just fetch-gene-pmids DICDI gskA`) and the UniProt record.

Full text available: 11032815, 20534815, 21205787, 22020250, 23135995, 23787121,
24653039, 31263268. Abstract-only: 7813009, 10571182, 15342480, 15366765, 22944283,
27237792, 29626371; 9784196 has no abstract text at all.

## Identity

- Single GSK-3 gene in Dictyostelium; 467 aa CMGC Ser/Thr kinase, GSK-3 subfamily (UniProt).
- "Dictyostelium possesses only a single GSK-3 gene that can be deleted to eliminate all
  GSK-3 activity" [PMID:23787121].
- Lithium-inhibited; Mg2+ cofactor (UniProt). Kinase-dead GskA(K85R) fails to rescue the
  null [PMID:20534815 "no phenotypic rescue was seen after expression of a mutant gene that
  lacks kinase activity (GskAK85R)"].

## Upstream regulation

- Activated downstream of cAMP receptor cAR3 via tyrosine kinases ZAK1 and ZAK2
  [PMID:10571182 "recombinant ZAK1 phosphorylates and activates GSK3 in vitro"]
  [PMID:21205787 "we now identify ZAK2 as the other tyrosine kinase in the cAMP-activation
  pathway for GSK3"].
- LKB1 acts upstream; lkb1 knockdown lowers GSK3 activity [PMID:22020250 "LKB1 positively
  functions at the upstream of GSK3 during development"].

## Cell-fate (prespore vs prestalk B) – classic role

- Null mutant: few spores, excess stalk/pstB cells; cAMP fails to inhibit pstB and to induce
  prespore differentiation [PMID:7813009 "We propose that cAMP acts through a common pathway
  that requires GSK-3 and determines the proportion of prespore and pstB cells"].
- Ax2/gskA- strain: accelerated early development, curtailed slug migration, DIF-1
  hypersensitivity, ectopic ecmB [PMID:15342480 "GskA forms part of the repressive signalling
  pathway that prevents premature commitment to stalk cell differentiation"].
- Cell-type specific regulation by ZAK1 (pstB, autonomous) and ZAK2 (prespore)
  [PMID:21205787 "Conversely, prestalk B differentiation is negatively regulated autonomously
  by ZAK1/GSK3"].

## Substrates / direct kinase function

- Dd-STATa: serine phosphorylation by GskA enhances nuclear export [PMID:11032815
  "Phosphorylation by GskA enhances nuclear export of Dd-STATa"].
- TacA: nuclear export partially GskA dependent [PMID:22944283].
- GtaC (GATA TF): GskA required for cAMP-induced mobility shift; purified Flag-GskA restores
  shift in vitro [PMID:24653039].
- DydA (Daydreamer, MRL adaptor) [PMID:23135995]; GflB (RapGEF) [PMID:27237792];
  PdeD, dynacortin, SogA [PMID:29626371]; RacE (Rho) Ser192 → mTORC2 activation
  [PMID:31263268 "chemoattractant stimulation induces GSK-3-mediated S192 phosphorylation of
  RacE-GDP to activate mTORC2-mediated AKT phosphorylation"]. Note: in 23135995 and 31263268
  the in vitro phosphorylation used recombinant human GSK-3beta; in-cell dependence used
  gskA- cells or GSK-3 inhibitors.

## Chemotaxis / signaling

- gskA- cells chemotax poorly to cAMP and folate, fail to activate PIP3 and TORC2 signalling
  [PMID:20534815].
- Kolsch et al. 2013: Ras kinetics misregulated in gskA-, extended PI3K recruitment and
  PKB/PKBR1 phosphorylation, reduced MyoII assembly [PMID:23135995]. This conflicts in part
  with Teo 2010 (reduced TORC2/PKB activation); the Senoo 2019 mechanism supports a positive
  role toward mTORC2.
- Polarization toward cAMP depends on ZAK1 phosphorylation of GSK3 [PMID:21205787].

## Mitosis

- GskA-GFP on central spindle and centrosomes; null fails to elongate spindle, cytokinesis
  defect in suspension, no chromosome segregation defect [PMID:23787121].

## Curation decisions (summary)

- GTPase regulator activity (IDA, PMID:23135995): REMOVE – full text read; the evidence is
  altered Ras-GTP kinetics in gskA- cells (indirect), GskA is a kinase not a GTPase regulator.
- tau-protein kinase activity (IEA from EC 2.7.11.26): over-annotation; no tau in Dictyostelium.
- TOR signaling (IMP): MODIFY to positive regulation of TORC2 signaling.
- cell differentiation (IMP, 7813009): MODIFY to positive regulation of sorocarp spore cell
  differentiation / negative regulation of sorocarp stalk cell differentiation.
- regulation of cell adhesion (TAS, review 15366765, abstract-only, does not mention GSK3):
  UNDECIDED.
