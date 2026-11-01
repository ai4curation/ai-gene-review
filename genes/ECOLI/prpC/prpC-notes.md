# prpC (P31660, b0333) notes

## Session log (2026-10-23)

- Provider deep research (`just deep-research ECOLI prpC --provider ...`) could not be run in this session because provider API credentials were unavailable. No `*-deep-research-*.md` file was created; this review is based on the curated UniProt entry and cached publications (all abstract-only).
- Fetched additional cache: PMID:28956599 (Reddick et al. 2017) via `just fetch-gene-pmids ECOLI prpC`.

## Function

- PrpC was first purified as a dimeric second citrate synthase from a gltA revertant [PMID:8508809 "that produces a dimeric citrate synthase with altered kinetic and regulatory properties"]; it is encoded by a gene distinct from gltA [PMID:8508809 "the mutant citrate synthase is encoded by a gene distinct from the E. coli gltA gene"].
- Propionate-induced enzyme condensing propionyl-CoA with oxaloacetate [PMID:9325432 "Extracts of propionate-grown cells contained a specific enzyme that catalyses the condensation of propionyl-CoA with oxaloacetate, most probably to methylcitrate. The enzyme was purified and identified as the already-known citrate synthase II."].
- 2-methylcitrate synthase with minor citrate synthase activity [PMID:9579066 "is in fact a 2-methylcitrate synthase that possesses citrate synthase activity as a minor component"]; GltA (hexamer) is constitutive while PrpC is propionate-induced [PMID:9579066 "Whereas the hexameric citrate synthase is constitutively produced, the 2-methylcitrate synthase is induced during growth on propionate"].
- Kinetics (UniProt, from PMID:9579066): Km 37 uM propionyl-CoA vs 101 uM acetyl-CoA; Vmax 0.33 vs 0.11 umol/min/mg. Homodimer.
- Pathway: E. coli oxidizes propionate via the methylcitrate cycle [PMID:9325432 "The results indicate that E. coli oxidises propionate to pyruvate via the methylcitrate cycle known from yeast."].
- Product stereochemistry disputed [PMID:28956599 "we showed that MmgD and PrpC (from Escherichia coli) in fact produce the same stereoisomer."].

## Curation decisions

- Accept: 2-methylcitrate synthase activity (all rows), propionate catabolic process (all rows), cytoplasm.
- Non-core: citrate synthase activity (all four rows; real but minor), protein homodimerization.
- Over-annotated: TCA cycle (IBA, IEA) - GltA is the TCA citrate synthase.
- Remove: carbohydrate metabolic process (IBA from deep CS node; wrong branch). Mirrors genes/PSEPK/prpC.
- Too general: acyltransferase activity, acyl groups converted into alkyl on transfer (parent of GO:0050440).
