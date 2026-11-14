# NME1 (P15531, NDPK-A / NM23-H1) curation notes

## Literature search (2026-11-13)

Deep research could not be generated: `just deep-research human NME1 --provider perplexity`
failed ("Provider 'perplexity' not available"). The review is based on the cached
publications for every GOA-cited PMID (most JBC/Cell papers are abstract-only in the
cache; Europe PMC lists no open full text for them), the two cached full texts
(PMID:19956735, PMID:33903070), the cached Boissan et al. 2014 Science abstract
(PMID:24970086), Reactome entries and the curated UniProt record.

## Core activity

- Classical group I NDP kinase: transfers the gamma-phosphate of ATP to any (d)NDP via a
  His118 phosphohistidine ping-pong intermediate [PMID:1851158 "The phosphorylation site on
  the enzyme is located at His-118."; PMID:9488696 "Nucleoside-diphosphate kinases (NDKs)
  catalyze the transfer of gamma-phosphoryl groups from NTPs via an active site histidine to
  NDPs using a ping-pong mechanism."].
- Broad substrate range, fastest with guanine nucleotides [PMID:9488696 "In all cases, second
  order rate constants were highest for guanine followed by adenine and lowest for cytosine
  nucleotides."].
- Hexamer, homo- or hetero- with NME2 (A/B chains) [PMID:1851158].
- Redox regulation: Cys109 oxidation/glutathionylation and CoAlation inhibit NDPK activity;
  Cys4-Cys145 disulfide dissociates the hexamer [PMID:19956735; PMID:23519676; PMID:33903070].
- Group I (NME1-4) are active NDPKs; group II (NME5-10) have little or none [PMID:33903070
  "The members of group I (NME1-4) share 40–88% sequence homology and possess NDPK activity."].
  Human NME5-9 are not in PANTHER PTHR11349 (PANTHER 19.0 human classification).

## Cellular roles built on the NDPK activity

- Local GTP supply to dynamin at clathrin-coated pits [PMID:24970086 "NM23-H1/H2 localized at
  clathrin-coated pits and interacted with the proline-rich domain of dynamin."]. NME4, not
  NME1, is the mitochondrial NDPK that feeds OPA1 [PMID:24970086].

## Secondary / contested activities

- Protein histidine phosphotransfer (succinyl-CoA synthetase, NME2, GST-NME1 as substrates)
  [PMID:9038158]. Accepted in the field as a genuine secondary activity; non-core.
- Ser/Thr "protein phosphotransferase": stoichiometric, requires urea, no turnover
  [PMID:8529641 "Because of the absence of a substrate turn-over, the novel function was termed
  protein phosphotransferase activity instead of protein kinase activity."]. Over-annotated as
  protein serine kinase activity.
- Geranyl/farnesyl diphosphate kinase activity [PMID:10952986]; not followed up; treated as
  in vitro activity of a broad-specificity enzyme of unknown physiological relevance.
- Nuclease activities: GzmA-activated DNase (single-strand nicking) in the ER-associated SET
  complex [PMID:12628186; PMID:16818237]; 3'-5' exonuclease [PMID:14960567; PMID:16313181];
  PDGF-A promoter cleavage [PMID:11694515]. Experimental, kept as non-core.
- Metastasis suppression / motility: phenotype-level; mutants P96S and S120G lose motility
  suppression without losing NDPK activity [PMID:9038158]. No effect on proliferation
  [PMID:8810265 "No effect was observed on cellular proliferation"].

## Localization

Cytoplasm/cytosol predominant, nuclear pool (DNA damage, GzmA), membrane recruitment
(clathrin-coated pits, cell periphery). The mitochondrion IBA (PTN000142925) is placed at the
eukaryotic NDK node; NME1 itself has no mitochondrial evidence and NME4 is the
mitochondria-specific paralog [PMID:24970086].

## PAINT losses

`just paint-losses human NME1`: no IRD/IKR on the NME1 lineage.
