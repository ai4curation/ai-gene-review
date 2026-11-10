# glnB (P0A9Z1) notes

Provider deep research was NOT run for this gene (not available in this session); the review is
based on the cached publications (`publications/PMID_*.md`, mostly abstract-only) and the curated
UniProt record.

## Summary
- PII signal transducer, homotrimer [PMID:8293810 "This result is consistent with the native protein being a homotrimer."]
- Binds ATP and 2-oxoglutarate [PMID:7629080 "Our results indicate that PII is activated upon binding ATP and either 2-ketoglutarate or glutamate"]; ATP-bound structure [PMID:11277925].
- Stimulates NRII (NtrB) phosphatase on NRI-P [PMID:2874557 "In the presence of PII, the product of glnB, NRII catalyzes the removal of the phosphate from NRI-phosphate."]
  and inhibits NRII kinase [PMID:10074086 "We showed that PII was also an inhibitor of the kinase activity of NRII."]; binds the NRII kinase domain [PMID:11063581].
- Uridylylation by GlnD abolishes the NRII effect [PMID:7961766 "In contrast, the uridylylated form of the PII protein had no discernible effect on NRI phosphorylation."]
- Interacts with ATase (GlnE) [PMID:2885322 "a tetrameric PIID molecule interacts with only one ATase molecule at a time"].
- Inhibits acetyl-CoA carboxylase BC-BCCP [PMID:25557370 "This interaction results in ACC inhibition by decreasing the enzyme turnover number."]
- Stimulates AspA [PMID:33012071 "GlnB interacted with AspA and stimulated its L-aspartate deaminase activity"].

## Curation decisions
- GO:0005515 rows: functional ones MODIFY (phosphatase activator, enzyme inhibitor, enzyme activator); HTP/Y2H rows REMOVE per protein-binding policy.
- GO:0030234 enzyme regulator activity: MODIFY to GO:0019211 / GO:0004860 / GO:0004857 / GO:0008047 as supported per row.
- GO:0036094 small molecule binding: MODIFY to ATP binding + carboxylic acid binding (no GO term for 2-oxoglutarate binding exists; possible ontology request).
- GO:0042304: MODIFY to GO:0045717 negative regulation of fatty acid biosynthetic process (ACC inhibition, in vitro).
- Homotrimer (GO:0042802): KEEP_AS_NON_CORE.
