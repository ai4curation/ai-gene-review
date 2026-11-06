# mucB (PA0764, P38108) notes

## Identity

- Sigma factor AlgU regulatory protein MucB (AlgN), RseB family, 316 aa with a
  Sec signal peptide (1-21). Encoded in the algU-mucA-mucB-mucC-mucD operon.
  UniProt: "Negative regulator of the sigma factor AlgU." (Swiss-Prot, P38108).
- No deep-research provider was available; notes below are from cached
  publications and PubMed searches.

## Literature

- Genetics: chromosomal insertional inactivation of mucB in PAO makes the strain
  mucoid with strong algD activation
  [PMID:8412698 "Insertional inactivation of mucB on the chromosome of the standard genetic strain PAO resulted in mucoid phenotype, and in a strong transcriptional activation of algD."].
- PseudoCAP seed paper (Mathee et al. 1997; abstract only, full text PMC179169 not
  retrievable through the PMC tool): an algT clone kept PAO1 nonmucoid only while
  the coupled mucB was intact
  [PMID:9171421 "However, the bacterial cells remained nonmucoid if the transcriptionally coupled mucB on the clone remained intact."];
  MucB localised to the periplasm by Western blot and phoA fusions
  [PMID:9171421 "By Western blotting and phoA fusion analyses, the MucB antagonist of sigma22 was found to localize to the periplasm of the cell."].
- Mechanism: purified MucB binds the MucA periplasmic domain tightly and blocks
  its cleavage by the site-1 protease AlgW (DegS homolog)
  [PMID:19298369 "We demonstrate that tight binding of MucB to MucA strongly inhibits this cleavage."].
  MucB is the RseB homolog of E. coli
  [PMID:19298369 "RseB (a MucB homolog), which is a protein that inhibits DegS cleavage of RseA"].
- In vivo: MucB is part of the MucA sigma-sequestration complex
  [PMID:19226327 "Here we showed that MucB, encoded by the algT-mucABCD operon, interacts with MucA in the sigma-sequestration complex."].
- Structures (6IN8 MucB alone, 6IN9 MucA-peri/MucB)
  [PMID:31297938 "MucB binds MucA in the periplasm and inhibits proteolysis of MucA and subsequent release of AlgU."];
  a hydrophobic cavity senses lipids that trigger MucA-MucB dissociation
  [PMID:32747658 "These results provide evidence that the hydrophobic cavity of MucB is a primary site for sensing lipid molecules"].

## Interpretation

MucB is a periplasmic co-antagonist of the ECF sigma factor AlgU: it binds the
anti-sigma factor MucA (MF: antisigma factor binding, GO:0045152) and shields it
from regulated intramembrane proteolysis. Alginate (polysaccharide) overproduction
in mucB mutants is the AlgU-regulon output in P. aeruginosa; it is a true
regulatory role of this gene, but it is not the conserved family function. In
E. coli and other enterobacteria, RseB controls the sigmaE envelope-stress
response, not polysaccharide synthesis.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale |
|---|---|---|---|---|---|---|
| PTN002215378 | GO:0032885 regulation of polysaccharide biosynthetic process | 1 (sole seed) | 7 (7 taxa) | GO:0032885 regulation of polysaccharide biosynthetic process, IMP, PMID:9171421 (PseudoCAP) | OVER-SPECIFIC | The seed is acceptable for MucB itself: mucB loss gives alginate overproduction because AlgU directly drives algD. But alginate control is a Pseudomonas-specific output of the AlgU regulon, not the RseB-family function. The node's other six leaves are enterobacterial/Vibrio/Shewanella/Haemophilus RseB orthologs (E. coli P0AFX9, Salmonella H9L461, Yersinia A0A2U2GWS2, Haemophilus P44792, Shewanella Q8EH85, Vibrio Q9KPA8) that regulate sigmaE, with no evidence of polysaccharide-synthesis control. The node term should not propagate; antisigma factor binding (already at this node, seeded by E. coli RseB) is the conserved claim. |

Node leaves were taken from the PAINT leaf GAF (`.cache/paint/leaf.gaf.gz`).

## Decisions summary

- MODIFY: protein binding IPI x2 -> antisigma factor binding (GO:0045152).
- ACCEPT: antisigma factor binding (IBA), outer membrane-bounded periplasmic space
  (IBA), periplasmic space (IEA).
- KEEP_AS_NON_CORE: regulation of polysaccharide biosynthetic process (IMP, IBA).
- GO_CENTRAL defect (PROBABLE): remove/restrict the GO:0032885 IBD at PTN002215378.
- No PSEUDOCAP defect.

## Leaf evidence check (2026-11-06)

Audit of the leaf claims in the `GO_CENTRAL` source defect on PTN002215378.
Membership confirmed with
`uv run python projects/PSEUDOCAP/panther_tree.py node PTN002215378 --leaves`
(7 leaves, all PTHR38782:SF1); UniProt flat files fetched for all seven. All
seven are 310-321 aa and match Pfam PF03888 MucB_RseB plus PF17188
MucB_RseB_C; six also match NCBIfam NF006990 rseB (Shewanella Q8EH85 does not).

| Leaf | Name and its evidence | Experimental annotations | Verdict |
|---|---|---|---|
| P0AFX9 (E. coli RseB) | RecName, curated (Reviewed); PE 1 | **GO:0045152 antisigma factor binding (IDA), GO:0050821 protein stabilization (IDA), GO:0042597 periplasmic space (EXP), GO:1903865 sigma factor antagonist complex (IPI), GO:0030288 (IDA)**; ECO:0000269 FUNCTION/SUBUNIT incl. LPS binding | "RseB ortholog" claim survives on evidence. No polysaccharide-related annotation of any kind |
| H9L461 (S. typhimurium) | RecName from **ECO:0000256\|ARBA** (an association rule, not curation); PE 3 | none | Identity rests on the family signature, not on the name or on ARBA text |
| A0A2U2GWS2 (Y. pestis) | **SubName** {ECO:0000313\|EMBL}; PE 3 | none | Same |
| P44792 (H. influenzae) | RecName, curated (Reviewed); PE 3 | none; FUNCTION all ECO:0000250 "By similarity" | Curated name, but no experimental data behind it |
| Q8EH85 (S. oneidensis) | **SubName** {ECO:0000313\|EMBL}; PE 3 | none | Family signature only; lacks NF006990 |
| Q9KPA8 (V. cholerae) | **SubName** {ECO:0000313\|EMBL}; PE 3 | none | Family signature only |

Outcome: the clade is genuinely homogeneous, so the "spans RseB orthologs"
observation survives — but on the domain architecture, not on the names (four of
six are SubName/ARBA). The load-bearing claim "with no reported role in
polysaccharide synthesis" **does not survive** as stated: it is an absence, and
there is a real counter-consideration. E. coli RseB binds LPS (curated
ECO:0000269 statements) and the sigmaE regulon includes LPS biogenesis genes, so
the broad GO:0032885 may be defensible for the enterobacterial leaves by a
mechanism unrelated to the seed's. What we can assert is narrower: the *route*
in the seed phenotype is lineage-restricted, because the alginate *algD* operon
is confined to *Pseudomonas* and *Azotobacter*.

Confidence lowered PROBABLE -> SUSPECTED, and the entry rewritten to query the
IBD rather than to assert the term is false for the other leaves.
