# eef1da notes (Danio rerio, eukaryotic translation elongation factor 1 delta a; UniProt A0A8M6Z1P2)

## 2026-09-28 — session log (DANRE_DUPLICATION batch 3, random sample)

**Deep research:** not available for this gene (Edison/Falcon returned 402 Payment Required;
the OpenAI key is invalid). Not attempted, per instructions. No `-deep-research-*.md` file
exists. Literature searched by hand in Europe PMC ("(eef1d OR eef1da OR eef1db OR
"EF-1delta" OR "eEF1Bdelta") AND zebrafish"; title searches for EF-1 delta / eEF1D).
**No zebrafish-specific functional paper exists for either paralog.** The only zebrafish data
are one high-throughput whole-mount in situ entry per gene in ZFIN and Bgee RNA-seq/array calls.

Accession: A0A8M6Z1P2 (TrEMBL, 463 aa, RefSeq model XP_017214236.2, chromosome 2) holds all 6
GOA rows (IEA/IBA only). UniProt also has seven other eef1da entries, including short isoforms
(245-291 aa). Paralog eef1db (A0A8M2B7W1, chromosome 20). Human ortholog EEF1D (P29692).

### PANTHER
- `TGD_tree`, Neopterygii|Teleostei, 1:1; one gar co-ortholog, two medaka co-orthologs.
- Family PTHR11595 is labelled "EF-HAND AND COILED-COIL DOMAIN-CONTAINING FAMILY MEMBER" in
  `interpro/panther/panther.obo`. The label does not describe these proteins, which carry the
  EF1B beta/delta GEF domain (InterPro IPR014038, IPR049720) and no EF-hand. The subfamilies
  are correctly named (SF88 "ELONGATION FACTOR-1, DELTA, A ISOFORM X1"; SF86 "ELONGATION
  FACTOR 1-DELTA ISOFORM X1"; SF19 "ELONGATION FACTOR 1-BETA_1-DELTA 2-RELATED"). I do not rely on
  the family label. I did not investigate why PANTHER gives it that name.

### Protein (eef1da-bioinformatics/RESULTS.md)
- Reviewed long isoforms: eef1da vs eef1db 40.5% identity overall, but 89.0% in the GEF
  region and 71.9% over the shared core. Shortest isoforms 62.8%.
- eef1da vs human GEF region 78.0%; leucine zipper 47.2%.
- The N-terminal extension of the eef1da long model is not distinguishable from a
  composition-matched shuffle (36.7% observed vs max 38.2% shuffled). eef1db is modestly above
  background; gar clearly above.
- Background on human EEF1D:
  [PMID:36576126 "the eEF1B complex acts as a guanine exchange factor (GEF) of GTP for GDP indirectly catalyzing the release of eEF1A from the ribosome."]
  [PMID:36576126 "EEF1D is alternatively spliced giving rise to one long and three short isoforms."]
  [PMID:21597468 "The long isoform of eEF1Bδ (eEF1BδL) is localized in the nucleus and induces heat-shock element (HSE)-containing genes in cooperation with heat-shock transcription factor 1 (HSF1)."]
  [PMID:25686034 "The orthologs of eEF1BδL are not found in reptiles or lower species."]
  The last statement conflicts with the RefSeq/Ensembl long models in gar and zebrafish. Those
  models are computational; whether a long protein is made in fish is untested.
  [PMID:10375624 "EF-1beta and EF-1delta are homologous in their C-terminal domain."]
- Comparator: Xenopus laevis (allotetraploid) keeps two EF-1 delta proteins in the same complex
  [PMID:8647113 "Both EF-1 delta proteins are simultaneously present in oocytes extracts, at a molecular ratio around 1:10 for p34 versus p36 proteins."]

### Expression
- Bgee: 29 anatomical entities, all shared with eef1db; both near the top of the score range
  everywhere. eef1da is higher in maternal/early stages (cleaving embryo 91.6 vs 64.7; mature
  ovarian follicle 98.2 vs 73.0; early embryo 97.1 vs 74.5).
- ZFIN: one whole-organism in situ row (Thisse high-throughput, ZDB-PUB-040907-1).

### Annotation decisions
- All 6 rows ACCEPT: GEF activity, translation elongation factor activity, eEF1 complex,
  cytosol, translational elongation. The catalytic region is intact and conserved; no
  zebrafish experiment contradicts the family function.
- No NEW terms: nothing zebrafish-specific supports the nuclear/heat-shock role of eEF1BdeltaL.
