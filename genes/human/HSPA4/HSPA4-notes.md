# HSPA4 notes


## 2026-09-08 paired human–horse review



HSPA4, also called Apg2, is an Hsp110-family chaperone that serves as a nucleotide-exchange factor for Hsc70. Together with Hsp70 and J-domain co-chaperones it supports refolding and disaggregation of proteins. Its substrate-binding and distinctive C-terminal regions tune Hsc70 engagement and nucleotide exchange.

## Apg2 exchange activity versus RAC membership

Apg2/HSPA4 belongs to the Hsp110 branch of the Hsp70 superfamily. Human biochemical work measures its effect on the Hsc70 ATPase cycle, aggregate binding and refolding. The concentration dependence is important: low Apg2 stimulates the system, while high concentrations can inhibit it. Its acidic and C-terminal regions regulate association and exchange. Those studies do not make HSPA4 the Hsp70L1 subunit of the Mpp11/Hsp70L1 ribosome-associated complex. General chaperone activity is transferable at a broader level than membership of a specific ribosome-bound assembly. A Tom40-import annotation must be checked in the complete original paper, since its abstract emphasizes Hsp90 rather than resolving every chaperone tested.

## Decisive inspected evidence

From [PMID:30521813](https://pubmed.ncbi.nlm.nih.gov/30521813/):

> Hsp110s support the refolding of aggregated polypeptides acting as specialized nucleotide exchange factors of Hsp70. We have studied how Apg2, one of the three human Hsp110s, regulates the activity of Hsc70 (HspA8), the constitutive Hsp70 in our cells.

## Evidence inventory

- [PMID:30521813: Regulation of Human Hsc70 ATPase and Chaperone Activities by Apg2: Role of the Acidic Subdomain.](https://pubmed.ncbi.nlm.nih.gov/30521813/). [DOI:10.1016/j.jmb.2018.11.026](https://doi.org/10.1016/j.jmb.2018.11.026). The repository cache contains the abstract; source-specific claims beyond it remain unresolved.
- [PMID:36167183: Fine-tuning of the Hsc70-based Human Protein Disaggregase Machinery by the Distinctive C-terminal Extension of Apg2.](https://pubmed.ncbi.nlm.nih.gov/36167183/). [DOI:10.1016/j.jmb.2022.167841](https://doi.org/10.1016/j.jmb.2022.167841). The repository cache contains the abstract; source-specific claims beyond it remain unresolved.
- [PMID:36604744: The human ribosome-associated complex suppresses prion formation in yeast.](https://pubmed.ncbi.nlm.nih.gov/36604744/). [DOI:10.1002/prot.26461](https://doi.org/10.1002/prot.26461). Full text is available in the repository cache.
- [PMID:15644312: Dissection of the mitochondrial import and assembly pathway for human Tom40.](https://pubmed.ncbi.nlm.nih.gov/15644312/). [DOI:10.1074/jbc.M413816200](https://doi.org/10.1074/jbc.M413816200). The repository cache contains the abstract; source-specific claims beyond it remain unresolved.

## Transfer to the selected horse protein

The exact target is [A0A9L0S5Z5](https://www.uniprot.org/uniprotkb/A0A9L0S5Z5/entry), not an arbitrary horse record with a matching name. The reproducible [paired-sequence analysis](../../HORSE/HSPA4/HSPA4-bioinformatics/RESULTS.md) records identity, coverage and internal gaps. It supports homology but is not a reciprocal orthology test. Molecular properties are transferred only with the relevant domain, targeting and paralog constraints. The prediction-time sequence is not independently verified.

## Open evidence questions

The following annotation scopes need source-specific follow-up: ATP hydrolysis activity, chaperone-mediated protein complex assembly, nucleus, protein binding, protein import into mitochondrial matrix, response to unfolded protein. Experimental annotations are not removed merely because a cached abstract omits the gene or a specific assay. High-throughput protein-binding rows require their actual partner or complex context before replacement with an informative molecular function.


Research provenance: external Falcon/Edison was attempted with Perplexity fallback. Some requests returned HTTP 429 and fallback returned insufficient-quota HTTP 401; successful external reports are preserved separately. Primary-source manual synthesis is explicitly labeled manual where no external report was available.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

Scope: full re-review of P34932 for the HORSE40_HUMAN_PAIR cohort. No ProtNLM2 file or prediction-evidence folder was opened or used.

### Identity
- P34932 is the reviewed, canonical UniProt entry (HSP74_HUMAN, 840 aa, isoform 1 displayed). It is not a fragment or alternative gene model. Isoform 2 (P34932-2, VSP_056885) is a splice variant; no GO row is isoform-specific.
- PANTHER: PTHR45639:SF6 (HEAT SHOCK 70 KDA PROTEIN 4), within PTHR45639 (HSC70CB, ISOFORM G-RELATED). Paralogs in the Hsp110 clade: HSPH1 (Q92598, SF2), HSPA4L (O95757, SF5); Grp170/HYOU1 (SF3/SF9).

### Deep research
- `just deep-research-falcon human HSPA4 --fallback perplexity-lite` failed on 2026-10-20: falcon "Failed to authenticate"; perplexity-lite HTTP 401 insufficient_quota. Review proceeded from cached primary literature and PAINT data. Existing `HSPA4-deep-research-manual.md` left untouched.

### Evolutionary grounding (from interpro/panther/PTHR45639/PTHR45639-paint.tsv)
- PTN002900795 (GO:0000774 nucleotide-exchange factor) seeds: CGD:CAL0000182153, SGD SSE2 (S000000373), LHS1 (S000001556), SSE1 (S000006027), human HSPH1 (Q92598). The Hsp110/Grp170 clade, which contains HSPA4. IBA sound; also directly shown for Apg2 [PMID:36167183 "During aggregate reactivation, Apg2 performs as a specialized nucleotide exchange factor"].
- PTN000452854 (eukaryotic Hsp110 node): nucleus, cytosol, protein folding.
- PTN000452648 (canonical Hsp70 node) carries GO:0016887 ATP hydrolysis and GO:0042026 protein refolding. These were NOT propagated to the Hsp110 node; treated as a deliberate PAINT decision. Consistent with [PMID:22990239 "This Hsp110 effect relies on nucleotide exchange, not on ATPase activity"].

### Decisions (changed from previous version)
- GO:0016887 ATP hydrolysis (IEA InterPro): UNDECIDED -> MARK_AS_OVER_ANNOTATED (PAINT omission + Hsp110 mechanism).
- Bare GO:0005515 rows: HSPA8 partner rows (5) -> MODIFY to GO:0030544 Hsp70 protein binding [PMID:36167183 "interacts with the nucleotide binding domain of Hsc70 in a nucleotide-dependent manner"]; EGFR/AGTRAP/APPBP2/POU6F2 HTP rows (6) -> REMOVE (protein-binding policy; not a claim the interactions are false).
- Cytoplasm IEA -> MODIFY to cytosol; organelle (ARBA) -> MODIFY to nucleus.
- Nucleus IBA: UNDECIDED -> KEEP_AS_NON_CORE.
- Response to unfolded protein (NAS, 1993 cloning paper): UNDECIDED -> MARK_AS_OVER_ANNOTATED (sequence-only statement).
- Tom40 paper (PMID:15644312) rows: still UNDECIDED. Abstract does not mention HSPA4; JBC PDF unretrievable (HTML landing page). Noted that Tom40 is an outer-membrane protein so GO:0045040 would fit the substrate better than matrix import, raised as a suggested question.
- ATP binding rows kept non-core; cytosol IBA/IDA, protein folding IBA, NEF IBA accepted.
- No NEW terms: protein refolding / disaggregation-type terms were deliberately not propagated by PAINT to the Hsp110 node.

### Relative and modules
- Mouse Hspa4 (Q61316, SF6 ortholog) has no experimental GO annotations of its own (only IBA/IEA/ISO), so it is not a well-characterised relative. Nearest experimentally characterised relative: human HSPH1 (Q92598, SF2 paralog in the same Hsp110 clade, PAINT seed for both Hsp110 nodes). No human HSPH1 review exists (only genes/CRIGR/HSPH1, status DRAFT).
- PANTHER family review interpro/panther/PTHR45639/PTHR45639-review.yaml places HSPA4 in SF6; no disagreement.
- Module: modules/heat_shock_response.yaml (has an hsp110_nef role, currently represented by worm HSP-110).
