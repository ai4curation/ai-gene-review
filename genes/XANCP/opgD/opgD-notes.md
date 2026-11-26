# XANCP OpgD review notes

## 2026-11-06 primary cyclase review

Reviewed all seven pristine seeded rows and preserved every non-review payload. No inherited NEW was present and no new existing_annotations row was added. A single proposed molecular-function term captures the directly demonstrated chemistry missing from the searched ontology; no redundant broad GO MF or necessity-only BP was manufactured.

PMID38957137 full text establishes an anomer-inverting transfer reaction producing alpha1,6-cyclized beta1,2-glucohexadecaose (DP16), identified by MS and NMR. This is not a uniform GH186 endohydrolase annotation. Exact ATCC33913 Q8P3C6 identity and the distinction between wild-type biochemical assays and D379N structure are verified in opgD-source-analysis/construct-proof.json. TableS4 primer translation supports added M plus residues29 onward; the structure entity contains the precursor and LEHis6 with D379N. A structure database precursor does not override the actual signal-deleted experimental design. Native cleavage, localization, flux, gene-deletion effects and direct host/pathogenesis roles are not newly asserted from these assays.

Genuine supplemental PDF was recovered via official ACS Figshare article26062998 and EuropePMC PMC11228985 ZIP; identical SHA256410c83b9c3f422807877d272bdf062b81db1cf7239213704f1a8090627507eb0. TablesS3/S4 were visually checked: WT0.29U/mg, D379N below0.00029U/mg, with0.1mMlinear beta1,2glucan. The full PDF/extract remains ignored; committed scoped evidence/provenance gives only needed construct, chemistry and activity details. Primary publication cache was not edited or refreshed.

QuickGO searches for glucohexadecaose, glucan cyclase, beta-glucan cyclotransferase and inverting transglycosylase found no exact term. GO0033913 is hydrolysis. GO0043895 cyclomaltodextrin glucanotransferase is specifically alpha1,4-glucan/alpha1,4 cyclization and is not suitable. Proposed activity: alpha-1,6-cyclized beta-1,2-glucohexadecaose synthase activity, parent GO0016757. The general glycosyltransferase hierarchy includes carbohydrate cyclization, but exact substrate, ring linkage and DP matter here.

Existing broad biosynthetic rows refine to OPG biosynthesis because this protein itself catalyzes product formation. The beta-glucan IBA from PTN001253664 does not assert hydrolase chemistry; the cyclized product remains predominantly beta-linked. Its OPG-process refinement is lateral in the current ontology closure. The periplasmic IBA is a considered node judgment from P40120; conserved Tat-type export supports it and the normal PAINT-loss command found no IRD/IKR. This is inferred location, not direct native assay. Carbohydrate binding refines to polysaccharide binding as ancillary substrate recognition.

Default Falcon was genuinely attempted via `just deep-research XANCP opgD --provider falcon` and failed403 authentication. No provider file was fabricated; research was performed manually using the primary paper, authoritative supplement, frozen UniProt, RCSB identity and current ontology. COMPLETE reflects completed evidence-based decisions with those native-context limits explicit.


## 2026-11-06 PR2142 follow-up

Retained GO:0051274 as ACCEPT. The OPG-specific process is already represented but does not currently entail beta-glucan biosynthesis; the independently supported beta-glucan claim must not be replaced away. The ontology relationship is now a suggested question. Original row identifiers, evidence and source metadata are unchanged.
