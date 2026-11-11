# CG32706 / Q8IRM9

Exact Q8IRM9 is the 230-residue CG32706-PA protein, with an ABT1/Esf2-specific InterPro classification and RRM at residues 62–140. [PMID:15964808](https://pubmed.ncbi.nlm.nih.gov/15964808/), DOI https://doi.org/10.1128/MCB.25.13.5523-5534.2005, is cached with full text and experimentally establishes the yeast homolog’s early rRNA-processing and processome-assembly function. The GOA IBA sources include yeast Esf2; this is a conserved family transfer with a characterized mechanism, not a donor-count argument. The provided ProtNLM paragraph is already reflected in those existing annotations.

The original phmmer donor O74362 is fission-yeast Esf2, whose identical UniProt functional paragraph is itself by-similarity. The direct experimental anchor is the budding-yeast paper, not repetition of the donor paragraph. [PMID:18245331](https://pubmed.ncbi.nlm.nih.gov/18245331/) remains abstract-only: both PMC and EuropePMC full-text attempts failed. The specific defense-versus-endurance mutant classification cannot be checked, so its experimental GO annotation remains UNDECIDED.

## Sequence and research provenance

The selected frozen UniProt record is retained in [CG32706-uniprot-source.json](CG32706-uniprot-source.json), with the complete original prediction metadata in [CG32706-predictions-source.json](CG32706-predictions-source.json). It maps the exact accession to this FlyBase gene; current sequence identity does not establish the historical predictor input. Gene-level experiments support conserved functions unless a relevant isoform difference is established. Falcon research was requested with perplexity-lite fallback alongside publication caching. Primary publications and sequence observations, rather than AI summaries or ARBA assertions, support the curated conclusions.

## Provider readback and narrative specificity

The completed Falcon report was inspected. It supports the Esf2 family-based ribosome-biogenesis inference and identifies additional yeast Dbp8 cofactor experiments, but no direct fly reaction. The broad SSU-processome/18S narrative claims are CNN; the precise requirement at yeast-named A0/A1/A2 sites is separately UNC because target site correspondence and requirement are not established. Broad conservation does not validate exact site names.

## Final research readback

The full Falcon output was inspected. It supports the conserved Esf2 mechanism while identifying uncertainty about exact fly RNA contacts; no yeast experiment is labeled as direct fly evidence.

## 2026-10-20 — Full re-review, independent of the ProtNLM2 predictions

**Identity.** Q8IRM9 (230 aa, TrEMBL, CG32706-PA) is the only UniProt entry for FlyBase
FBgn0052706, so the benchmark accession is the canonical product, not a fragment or
alternative model. It starts with Met, carries the full RRM (62-140, SMART) and the
ABT1/Esf2 post-RRM core. It is shorter than yeast Esf2 (316 aa) and human ABT1 (272 aa)
because it lacks the yeast acidic N-terminal extension and the yeast C-terminal tail, ending
instead in a Lys/Ala-rich repeat (`CG32706-bioinformatics/RESULTS-rereview.md`, new script
`compare_sequences_rereview.py`; identity 33.6% to P53743, 29.4% to Q9ULW3 over ~215 columns).

**Evolutionary grounding.** PANTHER PTHR12311 has a single subfamily, SF7, holding fungal
Esf2, Dictyostelium esf2, vertebrate ABT1 and CG32706 (`interpro/panther/PTHR12311/PTHR12311-entries.csv`).
The family is one-to-one in fly, so yeast Esf2 (P53743) is the ortholog. All IBA rows come from
PAINT node PTN000267771. PAINT propagated RNA binding, nucleolus, SSU-processome assembly and
the three early cleavages, but not Esf2's Dbp8 ATPase-stimulating activity
[PMID:16772403 "show that it enhances Dbp8 ATPase activity by decreasing the K(M) for ATP"];
I treat that omission as deliberate, and the fly protein has only part of the yeast C-terminal
Dbp8-binding region, so no ATPase-activator term is proposed.

**Changes vs previous review.**
- The three endonucleolytic-cleavage IBA rows went from ACCEPT to KEEP_AS_NON_CORE. Esf2 is a
  processome component but not the nuclease, and the yeast paper attributes the cleavage block
  to failed assembly [PMID:15964808 "This suggests that in the absence of proper SSU processome
  assembly, early pre-rRNA processing is inhibited"]. Core = GO:0034462 + RNA binding + nucleolus.
- PMID:16772403 added as direct support for RNA binding
  [PMID:16772403 "We show that Esf2 can bind to pre-rRNAs"].
- GO:0042742 defense response to bacterium (IMP, PMID:18245331) went from UNDECIDED to
  KEEP_AS_NON_CORE. The full text was read online at https://pmc.ncbi.nlm.nih.gov/articles/PMC2278058/
  (not cacheable locally: Europe PMC and BioC return nothing). Table 3 lists PBac line 10881
  "Within 100 bp of 3' end of CG32706", and Table 4 scores it + S. aureus, 0 S. typhimurium,
  + bacterial load, i.e. the defense class, which matches the curator. It is a single insertion
  allele with no reported revertants, and could be an indirect ribosome-biogenesis effect, so non-core.
- The description was rewritten as a project-independent summary. Status set to COMPLETE.

**Relative for next review.** Yeast ESF2 (P53743, SGD:S000005337) is the experimentally
characterised one-to-one ortholog in the same PANTHER subfamily and the PAINT donor. No review
exists in the repo (no genes/*/ESF2, nor P53743, Q9ULW3, O74362 or Q9QYL7 ids).

**Family review / modules.** `interpro/panther/PTHR12311/PTHR12311-review.yaml` agrees with the SF7
placement and lists CG32706 as SF7's representative; there is no subfamily disagreement. It leaves
GO:0034462 scope UNRESOLVED family-wide, but this review accepts it for CG32706 via the PAINT node.
No module under modules/ models the SSU processome. The nearest is `modules/dmel_small_nucleolar_rnps.yaml`
(the U3 box C/D snoRNP, whose partner Esf2 is in yeast); CG32706 is not a participant there and should
not be, since it is not a snoRNP subunit. CG32706 is not in gocams/index.tsv.
