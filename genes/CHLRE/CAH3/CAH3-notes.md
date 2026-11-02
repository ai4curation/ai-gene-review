# CAH3 (Q39588, Cre09.g415700) review notes

## 2026-10-03 session

### Deep research
- `scripts/deep_research_wrapper.py CHLRE CAH3 falcon --fallback perplexity-lite` failed:
  falcon returned HTTP 402 Payment Required; the perplexity-lite fallback failed with
  "Provider 'perplexity' not available". Not retried. Literature gathered directly from
  PubMed (esearch "Cah3 AND Chlamydomonas", "cia3 AND Chlamydomonas") and cached with
  `ai-gene-review fetch-pmid`.

### Identity and biochemistry
- Alpha-type CA, first intracellular alpha-CA found in a photosynthetic eukaryote; lumenal
  [PMID:9482718 "the presence of mature sized Cah3 after thermolysin treatment of intact
  thylakoids"].
- Bipartite transit peptide with twin-arginine lumen-targeting domain; the cia3 substitutions
  lie next to it [PMID:38247801 "the presence of two point changes near the twin arginine
  motif in the case of CAH3 is enough to completely disrupt the transport of the precursor
  protein from the stroma to the thylakoid lumen"].
- Crystal structures 4XIW/4XIX; zinc site, disulfide, N-terminal arm-swapped dimer; most
  active at mildly acidic pH [PMID:25617045 "CrCAH3 was most active at the slightly acidic
  pH values prevalent in the thylakoid lumen under illumination"].
- Recombinant CAH3 highly active [PMID:39795314 "showed more than three times higher
  activity compared to CAH1"].

### CCM role (main function)
- ca-1 nonsense allele complemented by CAH3 [PMID:9159949 "the carbonic anhydrase produced
  from the CAH3 gene is essential to the inorganic carbon-concentrating mechanism"].
  Important because cia3 (the other allele) is a transit-peptide lesion and might have
  mistargeting side effects; ca-1 is a null-type allele.
- In vivo, cia3 is limited by CO2 supply to Rubisco, not PSII [PMID:12913181 "the mutant
  lacks the ability to supply Rubisco with adequate CO(2) for effective CO(2) fixation and
  is not limited directly by any aspect of PSII function"].
- Epistasis: cah3 suppresses lcib air-dier; internal Ci >20-fold up [PMID:19074623 "LCIB
  functions downstream of CAH3 in the CO2-concentrating mechanism and probably plays a role
  in trapping CO2 released by CAH3 dehydration of accumulated Ci"].
- BST1-3 supply lumenal bicarbonate; cia3 used as CCM-deficient control [PMID:31391312
  "accumulated HCO3− is converted to CO2 by CAH3"].

### Localization: pyrenoid tubules and CO2 dependence (conflicting)
- Immunogold: mostly in thylakoids through the pyrenoid [PMID:22709623 "luminal Cah3 is
  mostly located in the thylakoid membranes that pass through the pyrenoid"].
- Blanco-Rivero 2012: phosphorylated after low CO2, activity up 5-6 fold, pyrenoid fraction
  19% -> 37% [PMID:23139834 "only 19% of the total Cah3 was associated with the pyrenoid
  region, while in low-CO2-grown cells 37% of the Cah3 protein was associated with the
  pyrenoid"]. So even at low CO2 most CAH3 is outside the pyrenoid in this study.
- Garde et al. 2026 bioRxiv (preprint): CAH3 in central reticulated tubules, membrane
  associated, and unchanged between high and low CO2 [PMID:42465278 "we observed no change
  in the localization of CAH3 under high CO2 compared to low CO2"]. Conflicts with the
  relocalization claim; not yet peer reviewed.

### PSII donor-side hypothesis (critical evaluation)
- Villarejo 2002: cia3 PSII particles have impaired water splitting, ~2 Mn per RC, rescued
  by bicarbonate [PMID:11953312 "Cah3 activity is necessary to stabilize the manganese
  cluster"].
- Shutova 2008: O2 evolution in cia3 PSII preps raised by HCO3- and further by CAH3; model of
  bicarbonate as proton carrier [PMID:18239688 "Cah3 promotes proton removal from the Mn
  complex by locally providing HCO(3)(-)"].
- Terentyev 2019, 2026 [PMID:31226314; PMID:42511718] further in vitro and cia3
  photoinhibition data.
- Assessment: supporting data are mainly from isolated PSII membranes and the single cia3
  allele (a targeting mutant). Hanson et al. 2003 found no PSII limitation in vivo at low Ci.
  Pyrenoid tubules lack PSII (D1 absent from isolated pyrenoids, PMID:23139834), and the
  expansion-microscopy preprint finds CAH3 concentrated in tubules even at high CO2, which
  sits awkwardly with a large PSII-associated pool. The PSII effect is plausible as a
  secondary, local proton-consuming effect of CA activity but is not established as a
  physiological function. GO:0009781 photosynthetic water oxidation is obsolete; no
  annotation proposed. Recorded as a suggested question/experiment instead.

### Annotation decisions
- GO:0004089 IEA: ACCEPT (core MF).
- GO:0008270 IEA: ACCEPT (catalytic zinc, structure-confirmed).
- NEW GO:0009543 chloroplast thylakoid lumen (IDA, PMID:9482718).
- NEW GO:0160223 pyrenoid tubule (IDA, PMID:23139834; also PMID:22709623, PMID:42465278).
- No BP proposed: GO has no CCM process term; CAH3 supplies substrate to Rubisco but does
  not carry out a step of the reductive pentose-phosphate cycle, so that term would fail the
  participation test.
