# SPAC25B8.09 (Q9UTA9) — evidence and prediction assessment

SPAC25B8.09 is a soluble methyltransferase type-11 protein found in the nucleus and cytosol. PomBase assigns trans-aconitate methyltransferase activity through curated orthology to budding-yeast Tmt1. This supports a probable small-molecule methyltransferase, while the predominant endogenous substrate and physiological role in fission yeast remain untested. Budding-yeast Tmt1 also methylates 3-isopropylmalate, so trans-aconitate detoxification is not the only plausible metabolic context.

## Evidence and family boundary

The [PomBase target page](https://www.pombase.org/gene/SPAC25B8.09) explicitly labels biological role inferred and provides TMT1/SGD:S000000977 orthology. The downloaded [P32643 record](SPAC25B8.09-P32643-ortholog-uniprot.txt) verifies that identifier and its experimental sources. [PMID:11695919](https://pubmed.ncbi.nlm.nih.gov/11695919/) establishes Tmt1 trans-aconitate methyltransferase activity; [PMID:15147181](https://pubmed.ncbi.nlm.nih.gov/15147181/) identifies 3-isopropylmalate as its major endogenous substrate in yeast extracts. The two substrate observations are compatible; neither makes the other reaction false.

Curated orthology is reasonable support for target molecular capability. It does not settle the dominant physiological substrate, conservation of the starvation response, or a universal substrate for PTHR44942. Falcon misses both Tmt1 orthology and the target HDA nucleus/cytosol record. Its blanket “location unknown” is therefore not adopted; nor is absence of a target biochemical paper treated as grounds for erasing a curator-supported localization.

## External ProtNLM statements

[Exact retained output](SPAC25B8.09-protnlm-source.json). These are name/location claims, not emitted GO/EC predictions. CNN denotes overlap with existing supported annotation; it does not establish literal membership in the training set.

| Claim type | Verbatim output | Assessment | Evidence and interpretation |
|---|---|---|---|
| name | Methyltransferase type 11 domain-containing protein | CNN | The claim specifies a domain class, not a methyl acceptor. IPR013216/PF08241 directly support that class. The curated Tmt1 orthology makes small-molecule methylation a reasonable additional inference but does not experimentally identify the target substrate. |

## Source quotations

[PMID:11695919](https://pubmed.ncbi.nlm.nih.gov/11695919/):

> We have identified the yeast open reading frame YER175c as the gene encoding the
> trans-aconitate methyltransferase of Saccharomyces cerevisiae.

[PMID:15147181](https://pubmed.ncbi.nlm.nih.gov/15147181/):

> the major
> methylated endogenous product of Tmt1 in yeast extracts

## Research provenance

The genuine [Falcon report](SPAC25B8.09-deep-research-falcon.md) is retained with its provider metadata and artifact. Its conclusions were checked against the target record, exact accession and primary sources described above. Scientific uncertainties are recorded as UNC/UNDECIDED findings rather than a request for another reviewer to perform this assessment.

## 2026-10-21 — Full re-review, independent of the ProtNLM2 predictions

Identity: Q9UTA9 is the canonical, reviewed (Swiss-Prot) full-length product of SPAC25B8.09 (251 aa,
sequence version 1). It is not an isoform, fragment or alternative gene model. It carries the complete
Methyltransf_11 (PF08241) / SAM-dependent MTase superfamily (IPR029063) fold.

Evolutionary placement (new analysis: `SPAC25B8.09-bioinformatics/RESULTS-rereview.md`,
script `compare_sf4_yeast_members.py`):
- UniProt places Q9UTA9 in PTHR44942:SF4. The subfamily has two members in each yeast: SPAC25B8.09
  and its tandem neighbour SPAC25B8.10 (Q9UTA8), and S. cerevisiae TMT1 (P32643) and CRG1 (P38892).
- The fission-yeast pair is 68% identical (a lineage-specific tandem duplication). Each copy is 25-29%
  identical to both TMT1 and CRG1, and TMT1/CRG1 are 36% identical to each other. Pairwise data do not
  single out TMT1 as a 1:1 ortholog. This is not a tree, so it is inconclusive on co-orthology.
- The official PANTHER 19.0 per-organism file places Q9UTA9 in PTHR42912:SF95, not PTHR44942:SF4. This
  conflict is pinned in `interpro/panther/panther-members-overrides.tsv` and recorded in the family review
  `interpro/panther/PTHR44942/PTHR44942-review.yaml`. That review lists only TMT1 as the SF4 representative
  and treats SPAC25B8.09 as comparative evidence. I do not disagree with that treatment; the open
  question is the target's parent family.
- SF4 also contains fungal natural-product O-methyltransferases (ptaH, nsrG, cfoB, pgmE; family entries
  CSV), so SF4 membership does not imply one acceptor.
- The IBA (GO:0008168) comes from PTN008676703, a deep node whose donors are E. coli RlmA (P36999),
  human TMT1A/METTL7A (Q9H8H3), Mtb Rv2952 (P9WIN3) and P. aeruginosa PA4379 (Q9HW23). These donors span
  PTHR43460, PTHR45036 and PTHR42912. Tmt1 is not a donor, and no acceptor-specific term was propagated.
  I read that omission as a deliberate PAINT decision.

Annotation decisions (changes vs previous review):
- trans-aconitate 3-methyltransferase activity (ISO from TMT1): ACCEPT -> UNDECIDED. It is plausible, but
  orthology and acceptor specificity are unresolved (see above).
- cellular response to amino acid starvation (ISO from TMT1): UNDECIDED -> MARK_AS_OVER_ANNOTATED. On the
  donor side this is Gcn4-driven induction plus a Saccharomyces invasive-growth signal (PMID:18092814,
  abstract). Induction is expression, not participation, and orthology is unresolved.
- cellular detoxification (ISS from P32643): KEEP_AS_NON_CORE -> MARK_AS_OVER_ANNOTATED. For Tmt1 itself
  the detoxification role is a hypothesis ("appears to be"), and its major endogenous substrate is
  3-isopropylmalate (PMID:15147181).
- cytoplasm (IEA SubCell): ACCEPT -> MODIFY to cytosol (GO:0005829). This comes from the same
  localization study that PomBase curated as cytosol.
- nucleus HDA/IEA and cytosol HDA: ACCEPT (target observation, PMID:16823372).
- methyltransferase activity (IBA): MODIFY -> GO:0008757 (unchanged). GO:0008757 IEA: ACCEPT.

Core function: SAM-dependent methyltransferase activity (GO:0008757) in cytosol and nucleus, with an
unknown acceptor. Description was rewritten to state the paralog pair and the unresolved orthology.

Relative to review next: budding-yeast TMT1 (P32643), the experimentally characterized SF4 member. There is
no review of it in the repo (no genes/yeast/TMT1). Its 1:1 orthology to SPAC25B8.09 is unresolved, so the
relation is recorded as a same-subfamily member. The tandem paralog SPAC25B8.10 (Q9UTA8) is also
unreviewed. No module in modules/ covers this gene or Tmt1.
