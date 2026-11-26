# dltA (Bacillus subtilis 168, P39581) - curation notes

## Literature search (2026-11-21)

No deep-research provider keys were available, so no `-deep-research-*.md` file
was generated. Searches were run with the PubMed tools:

- `dltA Bacillus subtilis D-alanine teichoic acid` -> 7 hits: 7797557, 18847223,
  19324056, 39308478, 14762009, 8682792, 18474639
- `DltA structure D-alanyl carrier protein ligase` -> 7 hits: 35362466, 19324056,
  25285205, 8682792, 18847223, 18784082, 25296179
- `D-alanine:D-alanyl carrier protein ligase Bacillus subtilis inhibition antibiotics`
  -> 1 hit: 15955059

Cached with `just fetch-pmid`: 7797557, 15955059, 18784082, 18847223, 19324056,
14762009, 8682792, 25285205.

## Findings

- dlt operon of B. subtilis (dltA-dltE) is required for D-alanine esters on both
  LTA and WTA; dltA is the proposed D-alanine-D-alanyl carrier protein ligase (Dcl)
  and dltC the carrier (Dcp). [PMID:7797557 "Insertional inactivation of dltA-dltD
  results in complete absence of D-alanine from both LTA and WTA"]
- Recombinant B. subtilis DltA was purified and assayed with its substrate DltC;
  a D-alanyl-adenylate analogue inhibits D-Ala adenylation (Ki 232 nM).
  [PMID:15955059 "We have heterologously expressed, purified, and assayed the
  substrate selectivity of the recombinant proteins DltA with its substrate DltC"]
- Crystal structures of B. subtilis DltA (PDB 3E7W, 3E7X; with AMP) show the
  D-Ala specificity determinants and a thiolation conformation.
  [PMID:18784082 "The structures of DltA reported here reveal the determinants for
  D-Ala substrate specificity"]
- B. cereus DltA ortholog structures with D-Ala-AMP and ATP (PMID:18847223,
  PMID:19324056); CoA as DltC mimic enhances D-Ala recognition (PMID:25285205).
- dltA mutant B. subtilis is more sensitive to nisin; dlt operon is in the sigma-X
  regulon (PMID:14762009).
- L. casei Dcp/Dcl biochemistry established the two-protein reaction (PMID:8682792).

## Verdict on RHEA:55132 / GO:0047473

Supported on the target itself: purified B. subtilis DltA was characterized with
B. subtilis DltC as substrate (PMID:15955059), the structure shows the adenylation
and thiolation states (PMID:18784082), and dltA inactivation abolishes D-alanyl
esters of teichoic acids (PMID:7797557). ACCEPT.

## Process term

GO:0070400 teichoic acid D-alanylation is the most accurate process: in B. subtilis
the dlt pathway D-alanylates both LTA and WTA. GOA has only GO:0070395 LTA
biosynthetic process (UniRule). Proposed NEW GO:0070400 (IMP, PMID:7797557);
DltA catalyses the first step of the pathway, so it does part of the work.
