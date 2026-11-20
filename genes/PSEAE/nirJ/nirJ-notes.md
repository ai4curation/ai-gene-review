# nirJ (G3XD10, PA0511) notes

## Review session 2026-10-28 (PseudoCAP IBA-seed protocol, worklist rank 71)

No deep-research provider was available; these notes are my own reading of the UniProt record, the
PseudoCAP-cited paper (PMID:8982003, abstract only; the PubMed MCP returned no PMC body text for PMC178684)
and three NirJ biochemistry papers found by PubMed search and cached with `just fetch-pmid`
(PMID:20420837 and 29076625 abstract-only; PMID:40318205 full text).

## Identity

- PAO1 PA0511, UniProtKB G3XD10 (unreviewed), 387 aa. Radical SAM core (PS51918, residues 20-239) with the
  CxxxCxxC SAM-cluster cysteines (Cys37, Cys41, Cys44), followed by a SPASM-type C-terminal region.
  NCBIfam TIGR04051 rSAM_NirJ; InterPro IPR023992 Pre-heme d1 synthase NirJ; SFLD heme_D1_biosynthesis
  (NirJ-like); PANTHER PTHR11228:SF7.
- Encoded in the *nirSMCFDLGHJEN* cluster for cytochrome cd1 nitrite reductase and its heme d1 cofactor.
- The UniProt FUNCTION text and name are ARBA predictions and are not used as evidence here.

## Literature

- Genetics in *P. aeruginosa*: [PMID:8982003 "Insertional mutation and complementation analyses showed that
  all of the nirFDLGHJE genes were necessary for the biosynthesis of heme d1."]. Polarity on the downstream
  *nirE* is a concern for an insertion in an operon, but complementation was performed (details not visible
  in the abstract).
- Radical SAM nature: [PMID:20420837 "The purified protein was found to contain a 4Fe-4S centre, in line
  with the prediction that it belongs to the radical SAM class of enzymes."]
- Activity (ortholog, abstract does not name the organism): [PMID:29076625 "we show that NirJ indeed
  catalyzes the removal of the two propionate side chains under simultaneous SAM cleavage."]; substrate
  [PMID:29076625 "NirJ tightly binds its substrate 12,18-didecarboxysiroheme"].
- Mechanism (*Dinoroseobacter shibae* NirJ): auxiliary [4Fe-4S] cluster and acrylate byproduct
  [PMID:40318205 "Here, we demonstrate by Mössbauer spectroscopy that NirJ contains a [4Fe-4S] cluster
  ligated by cysteine residues as its auxiliary cluster."]; [PMID:40318205 "We show that acrylate is
  released during the NirJ reaction as the cleavage byproduct"]. NirJ is related to AhbC of the
  siroheme-dependent (alternative) heme b pathway, which acts on the same substrate [PMID:40318205 "Thus,
  NirJ and AhbC use the same substrate."].

## Is heme d1 'heme' in GO?

GO:0006783 heme biosynthetic process is defined for "heme, any compound of iron complexed in a porphyrin
(tetrapyrrole) ring". Heme d1 is an iron dioxo-isobacteriochlorin, not a porphyrin in the strict sense, but
GO already places GO:0019354 siroheme biosynthetic process (also an iron isobacteriochlorin) under
GO:0006783, so heme d1 synthesis falls within the term as GO uses it. There is no heme d1-specific GO term;
GO:0006783 is the most precise available, and it says nothing wrong about NirJ. A "heme d1 biosynthetic
process" NTR (is_a GO:0006783) would make the annotation informative and would separate it from protoheme
synthesis. The term must not be read as protoheme (heme b) synthesis for NirJ.

## The node PTN000132400

QuickGO (2026-10-28): 15 GO:0006783 IBA leaves, 6 taxa. Apart from NirJ, all are archaeal SPASM-domain
radical SAM proteins: *Korarchaeum cryptofilum* (B1L4Z0, B1L5P2, B1L7M3), *Methanosarcina acetivorans*
(Q8THT9, Q8TIJ8, Q8TL56, Q8TLK1, Q8TR79, Q8TU98), *Pyrobaculum aerophilum* (Q8ZYW8), *Sulfolobus
solfataricus* (Q97WC3, Q97XA7, Q97XS7) and *Halobacterium salinarum* (Q9HQF7). UniProt/InterPro
(2026-10-28) classify only Q8TLK1 as a heme-pathway enzyme (TIGR04546 12,18-didecarboxysiroheme
deacetylase, i.e. AhbC; IPR030894). The others carry generic SPASM signatures (TIGR04085), TIGR03961
PTO1314 family, TIGR04347 pseudo-SAM/SPASM (Q9HQF7, despite its "Heme biosynthesis protein" name), or names
such as "tungsten-containing aldehyde ferredoxin oxidoreductase cofactor modifying protein" (Q8TR79). The
node is therefore a broad archaeal SPASM radical SAM clade in which heme (or heme d1) synthesis is
established for at most two lineages (NirJ, AhbC). The IBD over-generalises one gene's pathway.

## Annotation decisions

- GO:0006783 heme biosynthetic process (IMP PseudoCAP; IBA): ACCEPT for NirJ (most precise GO term;
  heme d1 synthesis), with a GO_CENTRAL defect on the node placement.
- GO:0003824 catalytic activity (IEA InterPro): MODIFY to an NTR for the NirJ reaction (no GO term exists).
- GO:0046872 metal ion binding, GO:0051536 iron-sulfur cluster binding (IEA): MODIFY to GO:0051539.
- GO:0051539 4 iron, 4 sulfur cluster binding (IEA): ACCEPT (radical SAM cluster motif; ortholog
  spectroscopy shows two [4Fe-4S] clusters).

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN000132400 | GO:0006783 heme biosynthetic process | 1 (sole) | 15 (6 taxa) | GO:0006783, IMP, PMID:8982003 (PseudoCAP) | OVER-SPECIFIC | For NirJ the seed is sound: insertion plus complementation shows nirJ is needed for heme d1, and ortholog biochemistry shows NirJ performs a step (propionate removal from 12,18-didecarboxysiroheme). Heme d1 counts as heme in GO (siroheme biosynthesis is_a GO:0006783), though it is not protoheme. The node, however, is a broad archaeal SPASM radical SAM clade; of 14 other leaves only Q8TLK1 (AhbC) is a heme-pathway enzyme. The IBD should be withdrawn or moved to a NirJ (TIGR04051) node. |
