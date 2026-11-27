# algF curation notes

- P. aeruginosa nonpolar algF deletion produces non-acetylated alginate and is
  rescued by complementation [PMID:12003941, "each mutant produced alginate
  lacking O-acetyl groups"].
- Unlike algI or algJ deletion, AlgF deletion also impairs alginate production,
  and AlgF stability depends on the polymerase context [PMID:31900562, "only
  the AlgF deletion impaired alginate production"].
- GO:0051979 is not a descendant of GO:0042121. The review therefore retains
  alginic acid biosynthetic process and adds alginic acid acetylation
  separately.
- No direct catalytic activity is established for AlgF; it remains a
  noncatalytic accessory component rather than receiving an invented molecular
  function.


## 2026-10-25 cross-species evidence audit

Normal `just fetch-gene PSEPK algF` was run without forcing source replacement. The helper backfilled supporting entities (and algF qualifiers); remote differences in existing source records were reported and preserved. Every pre-existing review row and all its machine-source fields were retained. References to GOA and the derived module were removed from the evidence bibliography because they are annotation/curation outputs, not independent biological support. No matching activity was found for these four accessions in the local GO-CAM index.

Publication caching used the normal pipeline concurrently with provider attempts. PMID:25165982 and PMID:37797696 were read in full. PMID:36494359 was newly fetched with full text. PMID:12003941 and PMID:23779107 currently have abstract-only caches; explicit abstract findings are used, without inventing unreported methods. PMID:31900562 is an abstract plus repository landing-page extract despite legacy full-text metadata; its explicit mutant/stability/pull-down summary is usable, but the cache does not supply full experimental methods.

Bacterial fitness retrieval was attempted with `just fetch-fitness PSEPK algF`. It failed because no local FEBA database or reachable remote source was available; no fitness artifact was written. This is missing data, not evidence of normal fitness or dispensability.

The exact physiological acetyl donor and detailed AlgI→AlgJ→AlgX transfer chemistry remain unresolved. PMID:40171682 is a 2025 review that explicitly says “This full model has yet to be demonstrated experimentally”. Its C-terminal AlgI acyl-shuttle proposal is informed by work on other MBOAT/SGNH systems. Direct Dlt intermediate chemistry cannot be silently reassigned to AlgI. PMID:40821665 is likewise a review, not a new target-specific AlgI assay.

Neither GOA evidence codes nor absence of a foreground gene in a title were used as grounds for rejection. In particular, the P. aeruginosa-titled papers contain direct P. putida construct experiments. Protein interaction evidence supports assembly participation, but no bare protein-binding annotation is added. Hydrolysis of an artificial ester proves catalytic capacity under the assay conditions, not the full physiological transfer reaction.

The genuine existing algF-deep-research-falcon.md report was inspected and reused (provider metadata and artifacts present); no replacement was fabricated. Its secondary synthesis was checked against the newer primary construct evidence.

### AlgF conclusions

PMID:37797696 Methods explicitly use KT2440 AlgF29–215, matching Q88ND4; that accession is separately listed in the computational Methods. Binary ITC demonstrated binding of PpAlgF to PpAlgJ75–370 (Kd86±12µM) and PpAlgX (178±5µM). Results use AlgFPp30–215 once whereas Methods and Figure3 use29–215; this minor boundary inconsistency does not change the organism/target mapping. The paper's acetylesterase Results also contain a P. aeruginosa/AlgFPp text typo; the constructs and figure labels identify Pp proteins. PpAlgF showed no detectable hydrolysis of ACC, alone or in combinations. This supports a nonenzymatic organization model, but is not a proof that every conceivable AlgF enzymatic activity is absent.

Species boundary matters: the NMR structure and failure to bind ManA4–ManA12 were measured for PaAlgF. They are not direct negative KT2440 binding measurements. Binary interactions do not independently prove simultaneous ternary bridging, and an acetyl relay was not reconstituted. The core therefore describes direct binding plus proposed organization, with no catalytic MF.

AlgF contributes structural work in the acetylation machinery, so process participation is appropriate; it is not merely a substrate consumed by another enzyme. The broader biosynthesis annotation is retained for assembly coupling supported by direct target interactions and the explicit PaPDO300 production/stability results of PMID:31900562. The latter phenotype is not stated as measured in KT2440, and “uniquely links” was softened to the actual evidence. Classification is AlgF IPR035422/PF11182, with no PANTHER cross-reference in the source.

## Independent final QA, 2026-10-25

Reassessed the pre-existing NEW process proposal rather than assuming it was justified. Live exact GO:0051979 QuickGO annotation queries found P. aeruginosa AlgI Q51392 (1), AlgJ Q51393 (2), AlgF Q06062 (2), and A. vinelandii AlgF P70799 (1), all experimental. Pa and Az AlgF are exact same-role organizational-component comparators; AlgI/J are acetyl-processing machinery comparators for the catalytic components. These counts are annotation-convention checks only, not supporting evidence. The term means addition of O-acetyl ester groups to alginate; the proteins perform catalytic or structural machinery work, rather than serving as its polymer substrate. GO:0051979 and GO:0042121 are not ancestor/descendant duplicates. A fresh search of gocams/index.tsv found none of Q88ND0/Q88ND2/Q88ND3/Q88ND4, so there is no cached target model whose different role is being overridden.

Retained the nonredundant NEW acetylation process: AlgF supplies an interaction/organizational contribution inferred with native ortholog genetics and direct target contacts; AlgX supplies conserved catalytic machinery with a direct ortholog transfer assay. This does not assert an experimentally observed AlgF bridge or a direct KT2440 polymer-transfer assay.

The live OLS parent lookup for GO:0051979 returned GO:0005976 polysaccharide metabolic process. This classifies modification of a polysaccharide; it does not restrict the participants to a polymer substrate or imply synthesis of the backbone.
