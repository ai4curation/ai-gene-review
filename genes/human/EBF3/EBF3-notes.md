# EBF3 review notes

## 2026-10-18: source-preserving review

All 14 imported assertions were reviewed: eight are accepted and six receive narrower terms. The original identifiers, evidence codes, references and supporting entities remain intact. There are no new annotation rows, retirement flags or new verbatim excerpts.

The refinements preserve the documented biology while identifying the Pol II context: broad DNA binding becomes GO:0000978; generic DNA-binding TF activity becomes GO:0000981; general transcription regulation becomes GO:0006357; and the three positive-transcription IMP assertions become GO:0045944. Current official typed ancestor records confirm each relationship. Existing PAINT and manual TFClass assertions supply independent specificity alongside the human experiments.

One integrated transcription-factor core covers DNA recognition, dimerization architecture and transcriptional regulation. Chromatin and nucleus are retained as supported compartments. A generic binding, metal-binding or second dimerization core would not add an independently established biological function. Disease genetics and fly rescue are not used to manufacture process annotations. The project-specific generic-binding exception was retained as a standing rule, although this gene's imported set contains no GO:0005515 row.

### Assay and product boundaries

[Sleven et al., PMID:28017370](https://pmc.ncbi.nlm.nih.gov/articles/PMC5223060/) expressed human EBF3 in a plasmacytoma assay in which surface IgM reports Cd79a-linked activation. Wild-type protein activated at low/intermediate expression but gave a reduced response at the highest expression category. P177L and K193N retained activity at high dosage; R163P did not. Each tested mutant still associated with WT in tagged co-IP. This does not establish a complete dimerization defect, purified DNA affinity, or a uniform dominant-negative mechanism.

[Chao et al., PMID:28017372](https://pmc.ncbi.nlm.nih.gov/articles/PMC5223093/) used untagged human EBF3 in a controlled six-COE-site reporter assay in HEK293 cells. Separate HA-tagged human constructs were tested in fly knot-null complementation. Both deposited templates named in the paper translate exactly to the current 551-residue Short product. This maps the deposited template, not every physical experimental vial, and does not establish activity equivalent to Long.

[Harms et al., PMID:28017373](https://pmc.ncbi.nlm.nih.gov/articles/PMC5223027/) supports nuclear WT localization, tight chromatin association, CDKN1A reporter activation and binding/transcriptional effects in SK-N-SH cells. The nuclear observation is confined to the tested WT assay; mutants can redistribute, retain some DNA binding, and have differing coexpression effects. Detailed supplemental Methods and figure pixels were not independently assessed.

[Siponen et al., PMID:20592035](https://pmc.ncbi.nlm.nih.gov/articles/PMC2923972/) directly studied EBF3 TIG-HLH/HLHLH fragments. Its DNA-binding-domain and isolated IPT/TIG structures were EBF1 constructs. The EBF3 fragment structures support dimerization architecture, but the zinc-bearing EBF1 DBD is not a direct EBF3 metal-occupancy assay.

### Inference, source access and reproducibility

The official PANTHER tree places human EBF3 below PTN000844136; its ungapped target sequence matches Long exactly. Four literal IBD assertions are retained. The human target's presence among nuclear IBD sources is expected experimental grounding, not circular evidence. Current exact-term donor queries were a limited corroboration, not independent full reads of every historical donor study.

The genuine ordinary caches were preserved byte-for-byte. Those for 28017370 and 28017372 remain abstract-only, although operative originals were separately recovered and read. The richer genuine 28017373 cache was selected for publication; an independently fetched abstract-only variant remains preserved in the private provenance. Reference-level access flags describe the actual assessed source access and do not rewrite cache flags.

The configured Falcon research attempt failed with HTTP 403 authentication rejection, and the genuine Perplexity-lite fallback failed with HTTP 401 quota exhaustion. No synthetic provider report was created. Manual research and independent source assessment support this review.

The [source guide](EBF3-source-guide.md) records precise claim boundaries and public locators. The [small evidence replay](EBF3-evidence/README.md) reproduces family placement and deposited-template identities from hash-checked raw inputs. It contains no full article bodies and does not compute biological verdicts. The unresolved question is how the two natural products differ in endogenous targets, dosage sensitivity and tissue-specific function.
