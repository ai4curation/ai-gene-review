# dsbA: PA14 disulfide-pathway review

## 2026-11-06

Official accession Q02DM0; taxon 208963 UCBPP-PA14. PMID:24327342 explicitly maps the four PA14 loci; no transfer from PAO1 is needed. Original seed and all protected bytes were frozen before edits in `.cache/module-audit-logs/dsbab-20261106/pa14-panel/dsbA-baseline.json`.

Normal Falcon research was attempted and failed with authentication HTTP 403; these are manual literature notes, not a provider report. PAINT-loss checking was attempted; an absent accession leaf does not establish a loss or justify invented ancestral placement. See the preserved tool log.

Full primary PMID:24327342 separates native PA14 deletion/AMS redox phenotypes from recombinant biochemistry. DsbB preparations were expressed in an E. coli dsbB mutant and partially purified; decylubiquinone was the assay acceptor. Insulin reduction used 150 micromolar insulin, 10 micromolar DsbA, and 0.8 mM DTT. These artificial conditions establish molecular chemistry without making insulin a native substrate. DsbA2 expression was not detected, and plasmid DsbA2 failed to rescue the DsbA1 phenotype. No native A2 redundancy or native homeostasis function is inferred.

Current QuickGO GO:0015035 defines reversible protein thiol/disulfide exchange and descends from GO:0015036 and GO:0016491. Its name does not exclude physiological oxidation. No native cellular process gap is manufactured. DsbA2 receives only one missing direct molecular-function proposal; its unknown physiological role remains explicit. Other genes use supported broad-row refinement. Signal/TM annotations support localization inference but do not constitute direct mapping of every boundary.

Text S2 was recovered from the genuine EuropePMC supplementary archive. All four genes were PCR-amplified from PA14 genomic DNA and sequence-checked. See `../dsbA/dsbA-source-analysis/identity-and-assay-scope.md` for mature-chain DsbA constructs and separate DsbB expression/preparation contexts; complete source files stay ignored.

## PR6129 evidence follow-up (2026-11-06)

Removed the unanchored core GO0006457 process assertion, while retaining direct protein-substrate disulfide chemistry and native PA14 scope. No NEW BP was manufactured for validator coverage. The same-role upstream search returned zero rows; repository Ecoli/Pputida DsbA and BdbD entries are authored proposals, not positive GOA convention. This does not deny that DsbA1 performs oxidative-folding chemistry. Also corrected core wording to regeneration of the oxidized active site.

## 2026-11-06: protein-folding proposal evidence threshold

Clarified the common decision rule: direct oxidation plus productive functional-substrate evidence in the target organism supports the BdbD proposal; in vitro archived-record transfer or PAO1-to-PA14 extrapolation remains a reason to defer a new BP. The upstream convention gap is shared uncertainty, not the discriminator. All annotation payloads, actions, quotations and core functions are unchanged.
