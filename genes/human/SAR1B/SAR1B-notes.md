# SAR1B notes

Review created 2026-10-09 from the GOA stub (76 annotations). The literature work was
done manually with PubMed and the cached `publications/` files. A Falcon deep-research
run (`just deep-research-falcon human SAR1B`) timed out after 600 s, so no deep-research
file exists.

## Normal function

- SAR1B is a COPII small GTPase. "Secretion-associated Ras-related GTPase 1 (SAR1) is a
  small GTPase that is part of COPII and, upon GTP binding, recruits the other COPII
  proteins to the endoplasmic reticulum membrane." [PMID:32358066]
- Coat cycle: "GTP-bound SAR1 inserts its hydrophobic N-terminus into the ER membrane and
  recruits SEC23-SEC24 heterodimers to the ER exit site"; "SEC23 also functions as the
  GTPase-activating protein for SAR1 and stimulates SAR1 GTP hydrolysis." [PMID:36594468]
- Directly measured human SAR1B GTPase activity. The alarmone ppGpp inhibits SAR1A but not
  SAR1B: "the alarmone ppGpp could bind to and inhibit the GTPase activity of human Sar1a
  but could not inhibit the GTPase activity of human Sar1b." [PMID:36369712]
- Paralog specificity: "SAR1B knockdown caused loss of lipoprotein secretion,
  overexpression of SAR1B but not of SAR1A could restore secretion" [PMID:32358066]. SAR1B
  binds SEC23A more strongly than SAR1A does [PMID:32358066].
- Lipoprotein export with the SURF4 cargo receptor: "this process is quantitatively
  governed by the GTPase SAR1B and SURF4, a high-efficiency cargo receptor" [PMID:33186557].
- Leucine sensor: "Under conditions of leucine deficiency, SAR1B inhibits mTORC1 by
  physically targeting its activator GATOR2." [PMID:34290409]. UniProt notes that this is
  independent of the GTPase activity.

## Disease link (normal function vs dysfunction)

- Chylomicron retention disease (Anderson disease): "Here we identify eight mutations in
  SARA2 that are associated with three severe disorders of fat malabsorption."
  [PMID:12692552]
- In Caco-2/15 cells, "SAR1B deletion resulted in significantly decreased secretion of
  triglycerides (≈40%), apolipoprotein B-48 (≈57%), and chylomicron (≈34.5%)." Abolishing
  output required a SAR1A/SAR1B double knockout [PMID:28982670].
- SAR1B also has a hepatic role: "Sar1B also promotes hepatic apolipoprotein (apo) B
  lipoprotein secretion" [PMID:24338480].
- The dismech entry `Chylomicron_Retention_Disease` marks GO:0003924 GTPase activity
  DECREASED on the SAR1B molecular node and GO:0090114 / GO:0006888 DECREASED downstream.
  This agrees with core function 1 here (GTPase activity, COPII coat assembly, ER to
  Golgi transport).

## Curation decisions

- GO:0005515 protein binding: removed (four high-throughput interactome screens; partners
  SAR1A, Q9NUH8 and CIDEB). This does not dispute the interactions.
- GO:0002474 MHC class I antigen presentation (Reactome TAS) and GO:1902953 positive
  regulation of ER to Golgi transport (NAS): marked as over-annotated. SAR1B is a core
  component of ER export, not a pathway-specific participant or a regulator.
- GO:0032580 Golgi cisterna membrane (IEA, from a by-similarity UniProt location): marked
  as over-annotated.
- The PMID:34015269 annotations (TMEM41B paper; only the abstract is cached and it does
  not mention SAR1B) are deferred to the curator. Lipoprotein transport is accepted
  because other papers support it independently. Regulation of lipid transport and lipid
  homeostasis are kept as non-core.
