# FKBP65 (ROF2, At5g48570) – manual literature synthesis

No deep-research API was available; this synthesis was assembled by hand from cached
publications (publications/PMID_*.md), a PubMed search
(`(ROF2 OR FKBP65 OR AtFKBP65) AND Arabidopsis`, 10 hits) and the UniProt record Q9FJL3.

## Identity and domain architecture

- Q9FJL3 (FKB65_ARATH), 578 aa; gene FKBP65 / ROF2 (ROTAMASE FKBP 2), At5g48570, GeneID 834913.
- Three FKBP-type PPIase domains (65-153, 181-271, 299-393), three TPR repeats (410-526) and a
  predicted calmodulin-binding region (539-555) [UniProt FT]. Architecture is that of the large
  multidomain FKBPs (mammalian FKBP51/FKBP52, wheat FKBP73/77), PANTHER PTHR46512.
- Closest paralog ROF1/FKBP62 (At3g25230, Q38931) shares 85% identity
  [PMID:17080288 "Although ROF1 and ROF2 share 85% identity, their expression in response to heat stress is differentially regulated"].
- In ROF1 only the first FKBD carries PPIase activity; FKBD2/3 are degenerate
  [PMID:23133621 "ROF1 contains an FK506 Binding Domain (FKBD) with PPIase activity, (FKBD1), two degenerate FKBDs (FKBD2 and FKBD3)"].
  No direct PPIase assay on ROF2 was found in the cached literature; the activity is inferred
  from family membership (IBA PTN002471265; InterPro IPR001179).

## Expression

- ROF2 is a bona fide heat-stress protein, undetectable at 22 C and induced at 37 C
  [PMID:17080288 "only ROF2 is a bonafide heat-stress protein, undetected when plants are grown at 22 degrees C"].
- ROF2 transcription is modulated by HsfA2 [PMID:19876748 "ROF2 transcription is modulated by HsfA2"].
- Induced by intracellular acid stress (weak organic acids) [PMID:22268595].
- Induced locally upon P. syringae infection [PMID:24440291].

## Heat stress / thermotolerance (main characterised role)

- Meiri et al. 2010: rof2 knockouts over-express small HSPs and are more heat resistant, the
  opposite of rof1 [PMID:19876748 "In the absence of ROF2, the small heat shock proteins were highly expressed and the plants were resistant to heat stress, opposite to the effect observed in the absence of ROF1"].
- ROF2 forms heterodimers with ROF1 and, through it, is proposed to join the ROF1-HSP90.1-HsfA2
  complex; co-expression of ROF2 with ROF1 represses sHSP transcription; model is negative
  feedback on HsfA2 [PMID:19876748 "A model describing the mode of action of ROF2 as a heat stress modulator which functions in negative feedback regulation of HsfA2 is proposed"].
- ROF2 itself does not bind HSP90.1 [PMID:38250364 "ROF2 does not interact with HSP90.1, and its"].
- Heat-induced relocalisation from cytoplasm to nucleus, independent of HSP90.1 and HsfA2
  [PMID:19876748 "its translocation to the nucleus was independent from the presence of HSP90.1 or HsfA2"].
- Proteomics of rof1/rof2 mutants after acclimation: double mutant over-accumulates heat-stress,
  folding and ER-processing proteins [PMID:38250364].
- Recombinant ROF2 CD spectroscopy: ~40% beta sheet; refolds into a heat-stable structure above
  65 C [PMID:23996408, abstract only].

## Intracellular pH homeostasis

- rof2 loss of function (and especially rof1 rof2) is acid sensitive; ROF2 overexpression confers
  acid tolerance by increasing proton extrusion, indirectly via activation of K+ uptake and
  membrane depolarisation [PMID:22268595 "The activation of the plasma membrane proton pump (H(+) -ATPase) is indirect"].
  Mechanism linking ROF2 to K+ uptake unknown.

## Biotic stress

- fkbp65 knockouts more susceptible to P. syringae; overexpression enhances resistance, alters
  defense gene transcription and callose deposition; protein reported nucleus-directed
  [PMID:24440291 "one nucleus directed FKBP known as AtFKBP65"].
- Y2H screen: ROF2 binds At1g70790 (C2-domain lipid-binding protein) and At2g30020 (putative PP2C)
  [PMID:29671793].

## Osmotic/salt stress and phosphoinositides

- ROF2 was enriched from salt-stressed cell extracts on a PI(3,5)P2 affinity column (ROF1 binding
  shown directly; ROF2 only as co-purifying candidate). rof1 rof2 double mutants lose enhanced
  germination under salt [PMID:23133621].

## Localisation

- Cytoplasm in unstressed cells, nucleus after heat stress [PMID:19876748]; nucleus [PMID:24440291].
- High-throughput detections: vacuole proteome [PMID:15539469]; membrane-associated / plastid
  fractions by SEC-MS [PMID:28887381]. Neither is supported by targeted studies; both may reflect
  co-fractionation of a soluble cytosolic protein.
