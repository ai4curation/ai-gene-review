# APH1B curation notes

## 2026-06-19

- Deep-research attempt with `just deep-research-falcon human APH1B --fallback perplexity-lite` timed out after 180 seconds with no generated research artifact, so this manual review uses cached UniProt, GOA, and publication evidence.
- APH1B encodes gamma-secretase subunit APH-1B, a multipass membrane protein and probable non-catalytic component of a subset of gamma-secretase complexes. UniProt frames APH1B as less abundant than APH1A-containing complexes and as a stabilizing cofactor for presenilin-containing complexes.
- APH1B-specific support comes from papers that discuss Aph1 isoforms and defined complex combinations. One abstract states that genes encoding "APH1a, APH1b, PEN2, and Nicastrin proteins" are part of the gamma-secretase complex with PS1 and that RNAi evidence indicates these components are essential for activity [PMID:12763021 "APH1a, APH1b, PEN2, and Nicastrin proteins, which are part of the gamma-secretase complex with PS1"; PMID:12763021 "these components are essential for gamma-secretase activity"].
- APH1B-containing complexes have substrate/complex-combination nuance. A defined-complex study states that "Aph1 has two isoforms, Aph1a and Aph1b" and reports different APP/Notch cleavage behavior across PS/Aph1 combinations [PMID:27608597 "Aph1 has two isoforms, Aph1a and Aph1b"; PMID:27608597 "PS2/Aph1b had a clear substrate specificity: APP-Gal4, but not Notch-Gal4, was cleaved"].
- Cell-surface/plasma-membrane annotations are plausible for APH1B because the cached Aph-1 localization abstract says Aph-1 is present at the cell surface, presumably in active gamma-secretase complexes [PMID:15715652 "Aph-1 is present at the cell surface, presumably in active gamma-secretase complexes"].
- APH1B should not be curated as an independent protease. Its core molecular role is adaptor/assembly/stabilizing contribution to the presenilin/nicastrin/PEN-2 gamma-secretase complex, with contribution to intramembrane aspartyl endopeptidase activity.
- Generic `protein binding` annotations reflect real interaction data but are less informative than gamma-secretase complex membership and APH1B adaptor/activator terms, so I marked them as over-annotated.

## 2026-06-20 second-pass audit

The second-pass audit added manual `reference_review` metadata for APH1B-relevant gamma-secretase references, emphasizing direct APH1B/APH1-isoform evidence where available and family-level APH-1 complex evidence where not isoform-specific. No annotation action changes were needed: APH1B remains curated as an APH-1 paralog in a subset of gamma-secretase complexes, with its strongest distinction being substrate-preference context rather than independent catalytic activity.
