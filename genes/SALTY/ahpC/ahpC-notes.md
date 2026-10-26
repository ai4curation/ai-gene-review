# SALTY ahpC: complete annotation review

## 2026-10-26 — source-grounded review

Reviewed all 14 seeded annotation rows, preserving every non-review field and both raw source files. No NEW annotation is added. Default Falcon plus perplexity-lite fallback and publication retrieval were actually attempted by the shared acquisition worker; provider attempts failed and no provider report was fabricated. The fitness fetch also failed because no FEBA source was reachable. Manual primary/source assessment supplies the review.

Salmonella typhimurium AhpC is a typical 2-Cys peroxiredoxin that reduces hydrogen peroxide and organic hydroperoxides to water and alcohols. Its peroxidatic cysteine is regenerated through a resolving disulfide and the AhpF reductase. Purified Salmonella AhpC and AhpF reconstitute peroxide reduction with NADH or NADPH as the ultimate electron donor. AhpC is the peroxide-reacting component, not an autonomous nicotinamide-nucleotide reductase. Its dimer/decamer distribution depends on redox state and experimental conditions.

### Evidence and scope

PMID:8555198 explicitly compares purified native Salmonella protein with recombinant Salmonella protein expressed in E. coli, finding the same tested activities. Its apparent NADH/NADPH Km difference is from DTNB reduction, not a universal cellular flux ratio. PMID:8555199 assigns peroxide chemistry to AhpC and regeneration to AhpF. PMID:2643600 purified the system from an oxyR1 regulatory mutant; the current database LT2 annotation does not establish that every later experiment used unmodified LT2.

### Review decisions and provenance

The coupled NADH-dependent peroxide-reduction rows are retained as valid component activities. Core functions distinguish direct molecular function from contribution; ordinary relationship qualifiers never determine the action. Homodimeric AhpF does not imply a fixed permanent AhpCF supercomplex. Broad binding terms refine to the independently supported NAD and FAD binding functions. Obsolete GO:0008379 is independently checked against QuickGO before refinement to the existing peroxiredoxin term.

Source access and short mined findings are recorded per reference in the review. Questions about unknown native donor kinetics or localization remain biological questions; failure of a research service is not a biological knowledge gap. Focused checks, record-section backfill, rendering and helper provenance are recorded in the panel handoff.
