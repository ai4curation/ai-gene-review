# VC_1370 (Q9KS89) notes

## Origin: KBase gene-annotate dashboard (Dark Protein Atlas)

- **Dashboard protein:** `NZ_AFOM01000014.1_606` (*Vibrio cholerae*, 443 aa),
  https://gene-annotate-dashboard.kbase.us/review/NZ_AFOM01000014.1_606
- **Mapping:** exact sequence match to N16961 VC_1370 / Q9KS89, 443/443 identical. Sources:
  `final_mapping.tsv` from run `20261030T212629Z-finalize-vibch-mapping`, and
  `VC_1370-bioinformatics/results.json`. The dashboard id is recorded as an alias in the
  review.
- **Frozen inputs:** call, call row, sequence and page are in
  `VC_1370-dashboard-prediction-evidence/`. They come from run
  `20261030T212643Z-dashboard-page-nz-afom01000014-1-606` and
  `user_data/dashboard_calls/NZ_AFOM01000014.1_606.*`.

## Dashboard call

> Inner-membrane c-di-GMP-binding protein containing HAMP and GGDEF signaling domains.
> (Tier A; GO:0035438 cyclic-di-GMP binding, GO:0005886 plasma membrane)

**Assessment: under-called.** Both GO terms are correct (COR/COR), but the call leaves out the
protein's primary activity, diguanylate cyclase:

- **The cyclase is intact.** The GGDEF domain is catalytically intact (RLGGDEF 349-353, DLD
  metal site, NDTKGHEVGD GTP-binding stretch).
- **Binding is a cyclase property.** The c-di-GMP binding the call relies on comes from a
  canonical I-site (RESD 340-343, spaced from GGDEF as in PleD). In an active DGC, that site
  mediates allosteric product inhibition.
- **The annotator had the evidence.** It explicitly withheld DGC activity because "binding does
  not establish catalysis". Its own evidence still included the intact GGDEF domain, the
  PANTHER/eggNOG DGC family call, and PaperBLAST snippets on VC1370 overexpression causing
  biofilm.
- **Suggested annotation:** "Inner-membrane HAMP-GGDEF diguanylate cyclase with
  c-di-GMP-binding I-site".

## Literature (V. cholerae; locus written VC1370)

- **PMID:26506097** (Roelofs et al. 2015): the DRaCALA ORFeome screen was positive for VC1370
  (Table 1). His-VC1370 gave a fraction bound of 0.45 with no competitor and 0.03 with unlabeled
  c-di-GMP (p < 0.001); cGMP (0.51) and GTP (0.47) did not compete. The His-MBP fusion gave the
  same pattern. Binding is therefore specific to c-di-GMP. The screen used E. coli lysates, not
  purified protein.
- **PMID:22802636** (Massie et al. 2012, Waters lab). Per the PMC full text, read with WebFetch
  and not in the cache, VC1370 is in the list of DGCs that "did not show increased biofilm
  induction in response to IPTG when analyzed by flow cytometry". The same paper says these
  did induce biofilm in the MBEC assay. Only the abstract is cached (not OA), so this is not
  quoted in the YAML.
- **No biochemistry.** There is no purified-protein DGC assay and no catalytic mutant. Beyhan et
  al. 2008 (PMID:18790873) and Lim et al. 2006 (PMID:16573684) deleted the GGDEF genes as a set.
  Their abstracts do not single out VC1370 (full texts were not available).
- **Regulation:**
  - quorum-sensing induced, with no HapR binding (PMID:18223081);
  - SOS regulon, co-transcribed with VC1369; vc1369 and vc1370 mutants are UV-sensitive
    (PMID:29783948). The UV phenotype was not turned into a GO term, because it is pleiotropic
    and its mechanism is unknown;
  - RpoS binds the promoter (PMID:40953128);
  - induced by nitric oxide (PMID:41329732) and by exogenous peptidoglycan (PMID:39753671; full
    text not cached).

## Tooling

- `just fetch-gene-pmids`: the YAML had no PMIDs, so nothing was fetched.
- `just fetch-fitness VIBCH VC_1370` failed: there is no local FEBA data, and the bulk download
  failed. No fitness data was used.
- `just fetch-pmid` sometimes failed the first time (exit 1) and succeeded on retry. This looked
  transient, possibly from parallel agents.
- **Full text:**
  - Massie 2012 (PMC3411991) and Beyhan 2008 (PMC2576663) are not open access. The EuropePMC
    REST full text returned HTTP 500, and the PubMed MCP returned abstracts only.
  - The Massie VC1370 sentence was read with WebFetch on the PMC page.
- **Deep research:** `just deep-research-claude-code` ran to completion, despite logging
  "agentapi not found in PATH". It agrees with this review and was used for cross-checking.
- **Validation:**
  - `just validate` gives one non-blocking warning: no annotation cites the deep-research file.
  - `validate-terms` on the sidecar fails with "No such slot locus_tag", because the sidecar is
    not GeneReview schema; this is the same as the yxcA example. `validate-predictions`
    (including `validate-prediction-terms`) is clean.
  - The signal transduction row was first marked TOO_GENERAL. The validator warned that no more
    specific asserted term entails it, so it was changed to KEEP_AS_NON_CORE.
- **Analysis run:** `projects/hackathon/runs/20261030T213647Z-vc1370-ggdef-motifs`.
