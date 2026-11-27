# PMII (plasmepsin II, PF3D7_1408000, Q8I6V3) - curation notes

**Note:** Automated deep research was unavailable in this environment (Falcon auth failure,
invalid OpenAI key). These notes are a manual literature review based on the UniProt record,
the cached publications in `publications/`, and targeted web searches for key primary papers.

## Identity and family

- Plasmepsin II, pepsin-family (MEROPS A01.023) aspartic protease of *Plasmodium falciparum* 3D7,
  EC 3.4.23.39. 453 aa precursor; propeptide 1-124 containing the transmembrane anchor; mature
  chain 125-453 (UniProt).
- One of four food-vacuole plasmepsins (PMI, PMII, PMIV, HAP) encoded in a tandem cluster on
  chromosome 14, products of recent gene duplication
  [PMID:11782538 "PM I, II, and IV and HAP lie in a cluster on chromosome 14"]
  [PMID:11782538 "High levels of sequence identity in both pro and mature regions suggest that PM I, II, and IV and HAP have arisen through relatively recent gene duplication events."]

## Molecular function: aspartic endopeptidase, hemoglobinase

- PMI and PMII initiate hemoglobin degradation by cleaving native Hb in the hinge region
  [PMID:11782538 "Two homologous aspartic proteases, called plasmepsins I and II (PM I and II) initiate the degradative process by cleaving the native hemoglobin molecule in a highly conserved hinge region"].
- Gluzman et al. 1994 isolated vacuolar proteases; the second aspartic protease (later named PMII)
  [PMID:8163662 "A second aspartic protease is capable of cleaving hemoglobin with an overlapping specificity, but seems to prefer acid-denatured globin."]
  (abstract only; the identity of this enzyme as PMII is from later literature).
- Recombinant mature PMII degrades hemoglobin and a fluorogenic peptide, and is inhibited by pepstatin A
  [PMID:29943906 "The direct indication of hemoglobin degradation by PMII confirms the activity of the mature enzyme."]
  [PMID:29943906 "The mature PMII cleaves the fluorogenic substrate with the Km value of ~0.68 µM."]
- PMII acts synergistically with HAP and PMIV on native hemoglobin
  [PMID:11782538 "A combination of HAP and PM II, or PM IV and PM II cleaved hemoglobin much faster than each enzyme alone."]
- Zymogen structure: prosegment holds the domains apart rather than occluding the active site
  [PMID:9886289 "Proplasmepsin II is the zymogen of plasmepsin II, an aspartic proteinase used by Plasmodiumfalciparum to digest hemoglobin during the blood stage of malaria."]

## Localization and trafficking

- Food vacuole by IF and immunoEM
  [PMID:11782538 "Immunoelectron microscopy confirmed that PM I, II, and IV and HAP are in the FV (Fig. 1 B ). Gold labeling was found exclusively within the FV."]
- Type II integral membrane proenzyme; trafficked through the ER to cytostomal vacuoles, then with
  hemoglobin to the food vacuole where it is cleaved to soluble mature enzyme
  [PMID:14709539 "PM I and II are synthesized as unglycosylated type II integral membrane proenzymes"]
  [PMID:14709539 "Our data support a model whereby proPM II is transported through the secretory system to cytostomal vacuoles and then is carried along with its substrate hemoglobin to the food vacuole where it is proteolytically processed to mature PM II."]
  [PMID:14709539 "In the acidic environment of the food vacuole, the proenzyme is cleaved and mature, active, soluble PM II is released."]
- With ALLN (blocks maturation), proPMII-GFP accumulates in the food vacuole membrane
  [PMID:14709539 "ALLN treatment results in accumulation of proPM II–GFP in the food vacuole membrane."]
- So: active enzyme = food vacuole lumen; membrane-bound forms (ER, cytostomal vacuole membrane,
  food vacuole membrane) are biosynthetic/trafficking intermediates.
- The food vacuole (GO:0020020) is a lysosome-like organelle; in GO, food vacuole is_a phagolysosome
  is_a lysosome (checked via OLS), so the IBA "lysosome" is a correct but general location.
  [PMID:14709539 "The food vacuole is a lysosome-like organelle unique to the genus Plasmodium."]

## Activation

- Proplasmepsin maturation is mainly by falcipains, with autoprocessing as backup
  [PMID:18308731 "These studies reveal that plasmepsin processing occurs primarily via the falcipains; however, if falcipain activity is blocked, autoprocessing can take place, serving as an alternate activation system."]

## Complex

- Part of a ~200 kDa hemozoin formation complex (HFC) in the food vacuole with falcipain 2/2',
  PMIV, HAP, HDP
  [PMID:23471987 "This complex contains several parasite proteins, including falcipain 2/2', plasmepsin II, plasmepsin IV, histo aspartic protease, and heme detoxification protein."]
- No GO CC term exists for this complex (none in GOA for PMII). Not proposed as new term here; the
  complex has only co-IP/co-elution support.

## Genetics / redundancy

- PMII knockout viable, modestly slower growth; substantial redundancy among FV plasmepsins
  [PMID:15513918 "PM II and PM IV/I disruptions have longer doubling times than the 3D7 parental line in rich RPMI medium."]
  [PMID:15513918 "These results suggest substantial functional redundancy and have important implications for the design of antimalarial drugs."]
- In Dd2 background, PMII double knockouts grew normally; only Δpm4 reduced hemozoin
  [PMID:17207486 "Only Deltapfpm4 had a statistically significant reduction in hemozoin accumulation, indicating that hemoglobin digestion was impaired in this mutant."]

## Curation thoughts

- MF GO:0004190 aspartic-type endopeptidase activity: experimentally solid; core.
- BP hemoglobin catabolic process (GO:0042540): PMII catalyses hemoglobin cleavage steps itself;
  core. Host hemoglobin is endocytosed and catabolised inside the parasite food vacuole, so the
  plain (non-host-interaction) catabolic process term is appropriate.
- BP proteolysis: true but general; refine to hemoglobin catabolic process (not an is_a
  descendant of proteolysis in GO - it sits under protein catabolic process - but it is the
  informative process the proteolysis serves).
- CC: food vacuole and vacuolar lumen = site of action; vacuolar membrane, membrane and cytostome =
  zymogen trafficking intermediates (non-core). Lysosome IBA -> refine to food vacuole.
- Possible in vitro activity on erythrocyte membrane skeleton proteins at neutral pH has been
  reported in the literature (not cached, not used).
