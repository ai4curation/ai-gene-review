# algX curation notes

- Q88ND0 is curated by explicit transfer from reviewed P. aeruginosa AlgX
  Q51372, not from the target UniProt record's circular "By similarity" line.
- Catalytic-triad substitutions in Q51372 produce non-acetylated alginate in
  vivo [PMID:23779107, "site-specific mutation of these residues results in
  non-acetylated alginate"].
- Purified Q51372 binds polymannuronic acid in a length-dependent manner and
  O-acetylates it with a surrogate donor [PMID:25165982, "AlgX binds
  polymannuronic acid specifically in a length-dependent manner"].
- GO:0016413 captures the demonstrated transferase class, GO:0030247 captures
  polymer binding, and GO:0051979 supplies alginate-specific process context.


## 2026-10-25 cross-species evidence audit

Normal `just fetch-gene PSEPK algX` was run without forcing source replacement. The helper backfilled supporting entities (and algF qualifiers); remote differences in existing source records were reported and preserved. Every pre-existing review row and all its machine-source fields were retained. References to GOA and the derived module were removed from the evidence bibliography because they are annotation/curation outputs, not independent biological support. No matching activity was found for these four accessions in the local GO-CAM index.

Publication caching used the normal pipeline concurrently with provider attempts. PMID:25165982 and PMID:37797696 were read in full. PMID:36494359 was newly fetched with full text. PMID:12003941 and PMID:23779107 currently have abstract-only caches; explicit abstract findings are used, without inventing unreported methods. PMID:31900562 is an abstract plus repository landing-page extract despite legacy full-text metadata; its explicit mutant/stability/pull-down summary is usable, but the cache does not supply full experimental methods.

Bacterial fitness retrieval was attempted with `just fetch-fitness PSEPK algX`. It failed because no local FEBA database or reachable remote source was available; no fitness artifact was written. This is missing data, not evidence of normal fitness or dispensability.

The exact physiological acetyl donor and detailed AlgI→AlgJ→AlgX transfer chemistry remain unresolved. PMID:40171682 is a 2025 review that explicitly says “This full model has yet to be demonstrated experimentally”. Its C-terminal AlgI acyl-shuttle proposal is informed by work on other MBOAT/SGNH systems. Direct Dlt intermediate chemistry cannot be silently reassigned to AlgI. PMID:40821665 is likewise a review, not a new target-specific AlgI assay.

Neither GOA evidence codes nor absence of a foreground gene in a title were used as grounds for rejection. In particular, the P. aeruginosa-titled papers contain direct P. putida construct experiments. Protein interaction evidence supports assembly participation, but no bare protein-binding annotation is added. Hydrolysis of an artificial ester proves catalytic capacity under the assay conditions, not the full physiological transfer reaction.

`just deep-research-falcon PSEPK algX --fallback perplexity-lite` was attempted. Falcon failed with HTTP403 Forbidden; fallback Perplexity failed with HTTP401 insufficient_quota. No successful provider report was generated, and these manual notes are not labeled as provider output. The existing genuine shared OpenScientist project report was reused as literature triage, not direct experimental evidence.

### AlgX conclusions

PMID:36494359 is newly cached in full (https://doi.org/10.1038/s41467-022-35131-6). It explicitly identifies KT2440 Q88ND0 and Q88NC7, crystallizes their AlgKX complex (PDB7ULA,2.5Å), and directly measures binding of isolated PpAlgX and the complex to polyM/polyMG oligosaccharides. The target's structure claim was valid but previously inadequately sourced.

Crucial species distinction: PaAlgX showed stronger affinity with longer polyM in PMID:25165982, but PMID:36494359 states “however, we did not observe this trend with AlgXPp”. No polyM-versus-polyMG preference was clear. AlgKX binds some ligands more strongly than either component alone. The existing ISS proposal is preserved as a source row, while its review now cites this newer direct target support and removes the transferred length dependence.

Direct KT2440 surrogate-substrate hydrolysis is measured in PMIDs:36494359/37797696; direct chemical detection of acetylated mannuronate products using 4-nitrophenyl acetate is from PaAlgX Q51372 in PMID:25165982. The terminal transferase core remains explicitly inferred for Q88ND0 rather than claiming target-specific polymer product chemistry. In-vivo interface disruption/secretion and biofilm phenotypes in36494359 are in P. aeruginosa. Chain protection is a functional model based on assembly and ortholog evidence, not a direct KT2440 AlgL-protection assay.

Target AlgX also directly binds AlgF (PMID:37797696). Curated architecture includes IPR034655 AlgX_N, IPR031798 AlgX_C, PF16822 ALGX and PF16824 CBM_26. No PANTHER cross-reference appears in the source; SGNH membership alone cannot select terminal polymer acetyltransferases. The biosynthesis core includes polymer handling/assembly in addition to acetylation.

## Independent final QA, 2026-10-25

Reassessed the pre-existing NEW process proposal rather than assuming it was justified. Live exact GO:0051979 QuickGO annotation queries found P. aeruginosa AlgI Q51392 (1), AlgJ Q51393 (2), AlgF Q06062 (2), and A. vinelandii AlgF P70799 (1), all experimental. Pa and Az AlgF are exact same-role organizational-component comparators; AlgI/J are acetyl-processing machinery comparators for the catalytic components. These counts are annotation-convention checks only, not supporting evidence. The term means addition of O-acetyl ester groups to alginate; the proteins perform catalytic or structural machinery work, rather than serving as its polymer substrate. GO:0051979 and GO:0042121 are not ancestor/descendant duplicates. A fresh search of gocams/index.tsv found none of Q88ND0/Q88ND2/Q88ND3/Q88ND4, so there is no cached target model whose different role is being overridden.

Retained the nonredundant NEW acetylation process: AlgF supplies an interaction/organizational contribution inferred with native ortholog genetics and direct target contacts; AlgX supplies conserved catalytic machinery with a direct ortholog transfer assay. This does not assert an experimentally observed AlgF bridge or a direct KT2440 polymer-transfer assay.

The live OLS parent lookup for GO:0051979 returned GO:0005976 polysaccharide metabolic process. This classifies modification of a polysaccharide; it does not restrict the participants to a polymer substrate or imply synthesis of the backbone.
