# dsbB1: PA14 disulfide-pathway review

## 2026-11-06

Official accession Q02TM7; taxon 208963 UCBPP-PA14. PMID:24327342 explicitly maps the four PA14 loci; no transfer from PAO1 is needed. Original seed and all protected bytes were frozen before edits in `.cache/module-audit-logs/dsbab-20261106/pa14-panel/dsbB1-baseline.json`.

Normal Falcon research was attempted and failed with authentication HTTP 403; these are manual literature notes, not a provider report. PAINT-loss checking was attempted; an absent accession leaf does not establish a loss or justify invented ancestral placement. See the preserved tool log.

Full primary PMID:24327342 separates native PA14 deletion/AMS redox phenotypes from recombinant biochemistry. DsbB preparations were expressed in an E. coli dsbB mutant and partially purified; decylubiquinone was the assay acceptor. Insulin reduction used 150 micromolar insulin, 10 micromolar DsbA, and 0.8 mM DTT. These artificial conditions establish molecular chemistry without making insulin a native substrate. DsbA2 expression was not detected, and plasmid DsbA2 failed to rescue the DsbA1 phenotype. No native A2 redundancy or native homeostasis function is inferred.

Current QuickGO GO:0015035 defines reversible protein thiol/disulfide exchange and descends from GO:0015036 and GO:0016491. Its name does not exclude physiological oxidation. No native cellular process gap is manufactured. DsbA2 receives only one missing direct molecular-function proposal; its unknown physiological role remains explicit. Other genes use supported broad-row refinement. Signal/TM annotations support localization inference but do not constitute direct mapping of every boundary.

Text S2 was recovered from the genuine EuropePMC supplementary archive. All four genes were PCR-amplified from PA14 genomic DNA and sequence-checked. See `../dsbA/dsbA-source-analysis/identity-and-assay-scope.md` for mature-chain DsbA constructs and separate DsbB expression/preparation contexts; complete source files stay ignored.

## Quinone-qualified core refinement

GO:0016672 now represents the quinone-coupled catalytic core, with one authored NEW IC annotation. The five seeded rows and their payloads remain unchanged. GO:0015035 and GO:0009055 remain valid and accepted: neither entails the sulfur-donor/quinone-acceptor combination, and the seed has no broad GO:0016491/GO:0016667 row that could be refined. No additional process or location term is proposed.

PMID:24327342 Figure2A shows slow background DsbA1 fluorescence change, no acceleration on quinone addition, and rapid oxidation on DsbB1 addition; the text reports analogous B2 behavior. Figure2B/C supplies individual substrate-dependent initial-velocity curves (apparent Km 8.1 micromolar for dsbB1), and AMS confirms DsbA1 cysteine oxidation. Figure5 includes DsbA2-alone and DsbA2-plus-quinone negative controls. These support a curated inference of quinone-coupled catalysis; they are not direct measurements of quinone redox state or equilibrium binding affinity. The inspected figures do not display a DsbB-containing minus-quinone comparison.

Partial purification and the distinct main-text versus TextS2 expression/preparation descriptions remain explicit; no homogeneous preparation or exact preparation-to-figure reconciliation is invented. The assay uses 30 micromolar decylubiquinone, which does not identify a particular native quinone. DsbA2 oxidation remains in-vitro capacity, not a demonstrated native A2 pathway. The earlier primary identity/source analysis remains unchanged.

## PR6129 evidence follow-up (2026-11-06)

Added a primary activity-result quote to GO0015035 alongside the retained preparation-method quote. The B1 fluorescence decrease is a result, not merely evidence of preparation. No action, source payload or original experimental caveat changed.
