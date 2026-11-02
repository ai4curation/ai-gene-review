

## 2026-10-26 complete annotation review

ProS is a class II prolyl-tRNA synthetase that charges tRNA(Pro) and removes alanine errors through pretransfer Ala-AMP hydrolysis and posttransfer Ala-tRNA(Pro) editing. HAMAP MF_01569 and the ProRS-INS editing-domain assignment support alanine proofreading. The curated rule explicitly distinguishes mischarged Cys-tRNA(Pro), which is not edited by this ProRS activity. Source: `proS-uniprot.txt`, curated HAMAP MF_01569, catalytic-activity, domain and subcellular-location sections. Exact-target kinetic and localization experiments were not located; the retained claims are explicitly conserved functional inferences. Integral ATP/tRNA/cofactor properties are not peripheral merely because support is computational.

All original rows and machine fields were preserved. Broad ligase/binding terms were refined to supported descendants; the verified obsolete amino-acid-specific process was replaced in review metadata by current GO:0006418. Original IDs and labels remain intact. No new annotation rows were proposed. The source specifically assigns deacylation of Ala-tRNA(Pro), so the supported descendant GO:0043906 is preferable to the generic deacylase term. The Ala-AMP pretransfer reaction is separate, and Cys-tRNA(Pro) editing is explicitly excluded by the curated family rule.

The actual Falcon attempt failed (HTTP 403), fallback Perplexity-lite failed (HTTP 401/quota), and the fitness retrieval failed; no provider or fitness report was fabricated. Normal publication caching completed. Per-target outcomes are recorded under `.cache/module-audit-logs/aminoacyl-root-acquisition/PSEPK-proS-results.json`. Manual review used the independently curated sequence record, domain assignments and live GO definitions.

Open question: What are the relative pretransfer and posttransfer alanine-editing rates of KT2440 ProS with native tRNA(Pro)?
