# ampD (PA4522, G3XCW9) review notes

## Review session 2026-11-05 (PseudoCAP IBA-seed protocol, tier 2)

Fetched with `just fetch-gene PSEAE G3XCW9 --alias ampD`; accession matches the worklist.
Unreviewed entry. No deep-research provider was used. Literature: the cached seed papers,
PubMed MCP and web searches for "AmpDh2", "AmpDh3", "ampD aeruginosa amidase" (Europe PMC
and NCBI eutils were returning errors during the session).

### Literature

- Seed paper PMID:9835532 (Langaee et al. 1998), abstract only; PMC106040 is a scanned
  article and no text could be retrieved. [PMID:9835532 "The ampD product transcomplemented
  Escherichia coli ampD mutants to wild-type beta-lactamase expression."]
- PMID:23510438 (Zhang et al. 2013, full text cached): purified AmpD hydrolyses only
  1,6-anhydromuramyl peptides [PMID:23510438 "AmpD is the true protease for the recycling
  process in P. aeruginosa, as its function is exclusive for turnover of 1,6-anhydromuramyl
  variants 4–6"]; it is the cytoplasmic paralogue [PMID:23510438 "This analysis identifies
  AmpD of P. aeruginosa as the cytoplasmic protease for commitment to the cell-wall
  recycling events"]. The same paper notes "AmpD is believed to be cytoplasmic and the
  cellular location of AmpDh3 is currently unknown".
- Comparators fetched by `ampD-bioinformatics/fetch_comparators.sh`: E. coli AmpD P13016
  is cytoplasmic; E. coli AmiD P75820 is an outer-membrane lipoprotein.
- The UniProt record for G3XCW9 has no signal peptide.

### Annotation decisions

- GO:0008745 amidase (IBA, IEA, IMP): ACCEPT, core MF.
- GO:0005737 cytoplasm (IEA): ACCEPT, core location.
- GO:0009254 peptidoglycan turnover (IBA): ACCEPT, core BP.
- GO:0009253 peptidoglycan catabolic process (IEA): KEEP_AS_NON_CORE.
- GO:0009276 cell wall (IMP, IBA): REMOVE; AmpD is cytoplasmic.
- GO:0033252 regulation of beta-lactamase activity (IMP): REMOVE; AmpD affects ampC
  expression through the AmpR inducer, not beta-lactamase activity.
- Action counts: ACCEPT 5, KEEP_AS_NON_CORE 1, REMOVE 3.
- GO:0009392 N-acetyl-anhydromuramoyl-L-alanine amidase activity exists but is not under
  GO:0008745, and its reaction is the GlcNAc-containing disaccharide, which was not assayed
  with P. aeruginosa AmpD. Not proposed as NEW; raised as a suggested question.

## PseudoCAP IBA-seed assessment

| PTN node | node term | n_seeds | leaf IBAs | seed annotation (term, evidence, PMID) | verdict | rationale | other seeds | IBD stands without this seed? |
|---|---|---|---|---|---|---|---|---|
| PTN001252273 | GO:0008745 N-acetylmuramoyl-L-alanine amidase activity | 5 | 37 (19 taxa) | GO:0008745, IMP, PMID:9835532 | SOUND | Heterologous complementation of the E. coli ampD defect; the activity was later confirmed with purified enzyme (PMID:23510438). | E. coli AmpD P13016 and AmiD P75820 (experimental), ampDh2, ampDh3 (IDA, PMID:23510438) | Yes |
| PTN002019137 | GO:0009276 Gram-negative-bacterium-type cell wall | 3 | 18 (11 taxa) | GO:0009276, IMP, PMID:9835532 | WRONG | A complementation of beta-lactamase expression cannot localize the protein; AmpD is the cytoplasmic paralogue. | ampDh2, ampDh3 (IDA, PMID:23510438; location inferred from substrate preference) | No: the node term does not suit the clade |

### Node PTN001252273 (amidase activity)

Leaves include the AmpD orthologues of E. coli, Salmonella, H. influenzae, Yersinia, Vibrio,
Coxiella and Shewanella, E. coli AmiD, Bacillus CwlA, CwlH, XlyA, XlyB and BlyA, Streptomyces
and Chloroflexus Amidase_2 proteins, and Trichoplax B3SF77. The seeds include E. coli AmpD and
AmiD, both characterised enzymes, so the IBD stands without any P. aeruginosa seed. The term
suits an Amidase_2 clade. No GO_CENTRAL defect. A second IBD on this node (GO:0009254
peptidoglycan turnover, seeded by E. coli AmpD alone) is sound. Shared with ampDh2 and ampDh3,
whose notes cross-reference this one.

### Node PTN002019137 (cell wall)

All three seeds are the P. aeruginosa paralogues (this batch). The 18 leaves are E. coli AmpD
P13016 and AmiD P75820, Salmonella P0CL03 and Q8ZQF3, H. influenzae P44624, Yersinia Q0WBM3,
Q0WGA0 and A0A3N4B5Z4, Coxiella Q83EE5, Bradyrhizobium Q89FT8, Shewanella Q8EJP2, Xanthomonas
Q8P4A5 and Q8PAE6, Neisseria Q9K0E1, Vibrio Q9KPE7 and the three P. aeruginosa proteins. The
node therefore covers the cytoplasmic AmpD lineage as well as the periplasmic or
outer-membrane AmiD, AmpDh2 and AmpDh3. Without the wrong ampD seed the IBD rests on two
periplasmic paralogues, which cannot justify a cell-wall location for the cytoplasmic AmpD
orthologues. The node-level `resource: GO_CENTRAL` defect is recorded once, here (on the
ampD IBA row), because ampD is the gene for which the propagation is directly wrong; ampDh2
and ampDh3 cross-reference it. The ampD PseudoCAP cell-wall row gets a `resource: PSEUDOCAP`
WRONG_TERM defect. Both PROBABLE: the 1998 full text was not read and the tree topology
under the node was not inspected.
