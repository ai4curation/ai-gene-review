# PP_0908 (Q88PE2) notes

## Origin: KBase gene-annotate dashboard (Dark Protein Atlas)

- Dashboard protein: `NZ_QHJD01000032.1_729` (*Pseudomonas putida*, 365 aa, tier A, strata Biotech-Significant / Core / Dark-Function), https://gene-annotate-dashboard.kbase.us/review/NZ_QHJD01000032.1_729
- UniProt mapping: 100% identical over 365/365 residues to KT2440 PP_0908 (Q88PE2), from the BERIL run `20261030T210853Z-final-putida-mapping`. The exact UniParc entries are deleted as non-reference-proteome entries.
- Call: "Soluble exported DUF1513-family protein associated with a putative ferrous iron uptake system." GO terms: GO:0008198 ferrous iron binding, GO:0033212 iron import into cell, GO:0042597 periplasmic space.
- GOA for Q88PE2 is empty.

## Conclusion

PP_0908 is an exported DUF1513 beta-propeller protein of unknown molecular function. It is encoded in a conserved imelysin / di-haem peroxidase gene cluster that is plausibly involved in iron acquisition. Neither the iron link nor the location has been tested for any DUF1513 protein.

## Evidence

### Genomic neighbourhood

Source: BERIL run `20261030T211421Z-pp0908-neighbourhood`, file `PP_0908-bioinformatics/neighbourhood_results.json`. All the genes below are on the complement strand of AE015451.2.

| Locus | Coordinates | Product |
|---|---|---|
| PP_0913 | 1054500..1055831 | Imelysin-like (PF09375), with a signal peptide |
| PP_0912, PP_0911 | | Hypothetical proteins |
| PP_0910 | 1051939..1053366 | DHOR di-haem oxidoreductase / putative peroxidase (PF06537), with a signal peptide |
| PP_0909 | 1050855..1051919 | Imelysin-like (PF09375), with a signal peptide |
| PP_0908 | 1049755..1050852 | The query. It starts 2 bp after the PP_0909 stop. |
| PP_0907, PP_0906 | 1045333..1049599 | RND efflux MFP and transporter. PP_0907 starts 155 bp after PP_0908 ends, in the same orientation. |

- **Synteny with *P. aeruginosa*.** The cluster matches PA4370 (IcmP imelysin), PA4371 (DHOR), PA4372 (imelysin), PA4373 (DUF1513) and PA4374–PA4375 (RND). Xu et al. 2011 (PMID:21799754) call PA4370–PA4373 the "Fur-regulated imelysin operon".
- **Is it an EfeUOB/FTR1 system? Not exactly.**
  - There is no EfeU/FTR1 permease in the cluster. The only FTR1-family protein in KT2440 is PP_0180 (cytochrome c + FTR1), which is encoded elsewhere.
  - There is no DyP-type EfeB (PF04261) in KT2440. The "efeB-like" partner is the DHOR protein PP_0910.
  - The "efeO-like" partners are imelysin-only proteins with no cupredoxin domain.
  - This is the EfeU-less, "outer-membrane" type of imelysin cluster described by Xu et al. The substrate of this type, Fe2+ or Fe3+, is unknown.

### Signal peptide

- **Predictions.** DeepTMHMM (dashboard) predicts SP 1–25, with no TM segment and no beta-barrel. UniProt's SignalP run gives no signal feature.
- **Tat-like motif.** The N-terminus is `MLRRQALKLGSVLLSALTLGGW`, with an RRQALK twin-arginine-like motif. It is conserved in PA4373 (`MLRRHVIGLG`). PROSITE Tat profiles hit the 32.4% and 32.6% identical *Silicibacter* and *Rhizobium* homologues.
- **No lipobox.** There is no Cys in the first 30 residues.
- **Location.** The most likely location is the periplasm. The Pfam / Fitness Browser "outer membrane component" label is not supported by the architecture.

### Fitness

- `just fetch-fitness` failed. The Fitness Browser returned 403 and there is no local FEBA database.
- The dashboard's embedded data (frozen in `PP_0908-dashboard-prediction-evidence/dashboard_call.json`) show KT2440 fitness of −2.93 to −1.97 (|t| 4.2–7.2) in six R2A + fusaric acid 480 µg/mL experiments.
- Fusaric acid is a metal chelator, but it is probably also an efflux substrate. PP_0908 sits directly upstream of the co-directional RND pump PP_0907–PP_0906, so polar effects on that pump are a real alternative explanation.
- Orthologue phenotypes are pleiotropic (*P. fluorescens* GW456-L13: vancomycin, Zn, Ni, D-cycloserine), with no iron-limitation condition shown.

### Literature

- No experimental paper on PP_0908, PA4373 or any DUF1513 protein was found (deep research report plus Europe PMC searches).
- The Pfam DUF1513 description cites Price et al. 2018 (PMID:29769716; the Fitness Browser reannotations) and Miethke et al. 2013 (PMID:23764491; *B. subtilis* EfeUOB). EfeUOB is the analogy behind "ferrous", not evidence about DUF1513.
- The PaperBLAST hits shown to the annotator are expression-only:
  - PA4373 is under-expressed in pan-drug-resistant (PDR) clinical strains.
  - The *R. sphaeroides* homologue is in the IscR regulon and co-transcribed with hemP/irpA/bfd/bfr. This is weak but iron-consistent.
  - The *R. etli* homologue was found in culture supernatant.

## Dashboard verdict

**Supported**, with caveats.

- **Text.** The call text is hedged ("associated with", "putative") and matches the evidence.
- **Tier rationale.** It sensibly rejects the "outer membrane" label and the amine-dehydrogenase activity.
- **Weak points:**
  - "ferrous" is analogy only, since the cluster has no EfeU/FTR1 permease;
  - the fusaric acid phenotype may be polar;
  - tier A rests on a fusaric acid phenotype that does not address iron.
- **Corrected annotation:** "Exported (Tat-like signal peptide) DUF1513 beta-propeller protein of unknown function, encoded in a conserved imelysin / di-haem peroxidase cluster implicated in iron acquisition."

GO terms (`PP_0908-dashboard-predictions-review.yaml`):

| Term | Code | Reason |
|---|---|---|
| GO:0008198 ferrous iron binding | UNC (1) | The extractor took it from the word "ferrous". There is no binding evidence. |
| GO:0033212 iron import into cell | UNC (1) | A plausible hypothesis from gene context, Fur regulation in PAO1 and FB cofitness, but untested. |
| GO:0042597 periplasmic space | UNC (1) | Export is well supported, but periplasmic residence is predicted only. |

## Caveats

- No fitness data was retrieved directly (403); the review relies on the frozen dashboard copy.
- SignalP 6 / TatP were not run locally (not installed). The Tat-like motif is a regex match.
- No GO terms were added to the gene review. `core_functions` gives a description only.

## Tooling

- `just fetch-gene` timed out at the EBI OLS step (www.ebi.ac.uk read timeout, twice). The UniProt and GOA files were written; the review YAML was written by hand.
- `just fetch-fitness` failed with 403.
- Deep research used the claude-code provider.

## Status: DRAFT

What would close it out: KT2440 RB-TnSeq data for PP_0908 and its cluster partners PP_0913-PP_0909 under iron limitation, from the BERDL Fitness Browser copy (fit.genomics.lbl.gov returned 403 here). Cofitness with the imelysin and di-haem peroxidase genes, or an iron-limitation phenotype, would decide whether the hedged iron-acquisition role can enter `core_functions` as a process term. Until then the core function stays without GO terms. (Added after PR #5755 review.)
