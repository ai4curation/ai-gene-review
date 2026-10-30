# VC_1669 (Q9KRH3) notes

## Origin: KBase gene-annotate dashboard (Dark Protein Atlas)

- Dashboard protein: `NZ_JADNQR010000211.1_1` (*Vibrio cholerae*, 447 aa), https://gene-annotate-dashboard.kbase.us/review/NZ_JADNQR010000211.1_1
- 98.2% identical to N16961 VC_1669 / Q9KRH3 over 447 aligned residues (bioinformatics `results.json`; mapping run `20261030T212629Z-finalize-vibch-mapping`).
- Dashboard page and GO terms come from run `20261030T212650Z-dashboard-page-nz-jadnqr010000211-1-1` and are frozen in `VC_1669-dashboard-prediction-evidence/`.
- No gene name is established in the literature, so the directory keeps the locus tag.

## Dashboard call

> Putative sodium-dependent tryptophan transporter of the sodium:neurotransmitter symporter family. (Tier A; GO:0015196, GO:0015293, GO:0015827, GO:0031402)

Verdict: **overreach**. The family-level call is fine; the tryptophan substrate is a paralog transfer.
- GO:0015196 L-tryptophan transmembrane transporter activity: **PLI** (PARALOG_OVERANNOTATION).
- GO:0015827 tryptophan transport: **PLI**.
- GO:0015293 symporter activity: **COR** (NSS family, Na+-coupled symport; Tyt1, TnaT).
- GO:0031402 sodium ion binding: **UNC**. The extractor derived it from the word "sodium-dependent"; Na sites were not examined.

Suggested corrected annotation: "Putative Na+-coupled NSS-family symporter, substrate unknown (paralog of tryptophan transporter AatX/VC2283)".

Why PLI rather than UNC: the call's only tryptophan evidence is AatX/VC2283, a 54.9%-identical paralog in the same genome. Tryptophan was assigned to VC2283 because of its TrpR regulation. VC1669 lacks the TrpR operator, has no tryptophan-related neighbours, and is no closer than AatX to any characterized tryptophan-transporting NSS. No experiment rules tryptophan out as a VC_1669 substrate, so PLI is a judgment about an unsupported transfer, not a refutation.

## Paralog comparison (shared with aatX)

`VC_1669-bioinformatics/` (`analyze.py`, `justfile`, `results.json`, `RESULTS.md`), recorded as BERIL run `20261030T213758Z-vc2283-vc1669-nss-paralog-comparison`. Inputs: the UniProt FASTAs, the NC_002505.1 and NC_002506.1 genome FASTAs and NCBI feature tables (in `data/`), and both dashboard FASTAs.

## Other evidence

- PaperBLAST, as shown on the dashboard, reports VC1669 as a direct CarR (RstA) ChIP-seq target (PMID:35676416). The main text of PMC9178039 does not mention VC1669; the hit is presumably in the supplementary tables, which I did not check. `just fetch-pmid 35676416` failed with HTTP 429 and was not retried, so that paper is not cited in the review YAML.
- The closest annotated homolog, *Shewanella* SO_4339 (48.1%), is a "hypotaurine transporter" assigned from fitness data (PMID:22125499). It is no closer to VC1669 than to AatX (45.2%), so it was not transferred.
- The deep-research report (claude-code) found no literature on VC_1669 and missed PMID:36130487.

## Tooling

- `just fetch-fitness VIBCH VC_1669` failed: "No FEBA organism mapping for 'VIBCH'".
- `just validate-terms` on the sidecar fails on `locus_tag` (GeneReview schema). This is expected; `validate-predictions` passes.
