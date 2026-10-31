# HPR2 (At1g79870, Q9CA90) curation notes

**Deep research could not be run** in this environment (no provider API keys). These notes
are built only from cached publications (`publications/PMID_*.md`) and the UniProt record
(`HPR2-uniprot.txt`). No `-deep-research-*.md` file exists for this gene.

## Identity and family

- Glyoxylate/hydroxypyruvate reductase A HPR2; 313 aa; D-isomer specific 2-hydroxyacid
  dehydrogenase family, GyaR subfamily (UniProt SIMILARITY, ECO:0000305; Pfam PF00389/PF02826;
  PANTHER PTHR10996:SF178).
- Also named HPPR2 (hydroxyphenylpyruvate reductase 2) in the tyrosine-pathway literature
  [PMID:30233632 "the predicted proteins encoded by At1g79870, At1g12550, and At2g45630 share 76, 48, and 45% identities with the HPPR (CAD47810.2) from Coleus blumei"].

## Enzymatic activity

- Purified from hpr1 knockout leaves as the NADPH-dependent HPR activity; identified as
  At1g79870 by MS and cross-reaction with anti-spinach HPR2 serum [PMID:18952776 "The smallest protein, which was also shown to interact with the spinach anti-HPR2 antibodies ( Figure 3B ), was identified as Arabidopsis protein At1g79870."].
- Recombinant enzyme prefers NADPH and hydroxypyruvate; NADH rates ~4x lower; glyoxylate
  also reduced [PMID:18952776 "Tag-purified recombinant At1g79870 was most active in the presence of NADPH and hydroxypyruvate, whereas NADH-dependent rates were about four times lower."]
  [PMID:18952776 "The enzyme also accepts glyoxylate as a substrate, but at a considerably lower efficiency in the NADH-driven reaction."].
- Strongly inhibited by oxalate (UniProt ACTIVITY REGULATION, ECO:0000269 PubMed:18952776).
- Also reduces 4-hydroxyphenylpyruvate (pHPP) to 4-hydroxyphenyllactate (pHPL), but its highest
  catalytic efficiency is with hydroxypyruvate [PMID:30233632 "HPPR2 had the highest affinity for pHPP, although its highest catalytic efficiency was detected with hydroxypyruvic acid."].

## Localization

- Cytosolic. GFP-HPR2 showed no organelle targeting [PMID:18952776 "Initial analyses with green fluorescent protein–HPR2 fusion proteins in transgenic Arabidopsis also gave no indication for organelle targeting"];
  independent GFP study in protoplasts [PMID:30233632 "HPPR2, HPPR3, and HPPR4 are localized in the cytosol."].
- A mitochondrion HDA call (membrane-fraction SEC profiling, PMID:28887381) is not supported
  by any targeting data; the same study notes extensive cytosol/membrane partitioning.

## Physiological role

- Cytosolic bypass of peroxisomal HPR1 in photorespiration [PMID:18952776 "We have identified a second hydroxypyruvate reductase, HPR2, and present genetic and biochemical evidence that the enzyme provides a cytosolic bypass to the photorespiratory core cycle"].
- hpr2 single mutants nearly wild-type; hpr1 hpr2 double mutants air-sensitive and rescued
  by 1% CO2 [PMID:18952776 "Growth under the nonphotorespiratory conditions of air enriched with 1% CO 2 restored the phenotype to normal"].
- HPR1 dominant; HPR2 an overflow route [PMID:22303256 "This suggests that peroxisomal HPR1 plays a dominant role under moderate growth conditions whereas HPR2 provides an overflow mechanism for the utilization of excess hydroxypyruvate leaking from peroxisomes under conditions of very high photorespiratory flow."].
- A third enzyme HPR3 adds further redundancy [PMID:21205613 "In addition, a NADPH-dependent cytosolic HPR2 provides an efficient extraperoxisomal bypass."].
- Secondary role in tyrosine-derived pHPL formation [PMID:30233632 "These findings present strong evidence that TAT1, HPPR2, and HPPR3 contribute to pHPL production in Arabidopsis."].

## Other

- Salicylic acid binding: HPR2 bound SA in two in vitro assays (SPR with 3AESA; SA-competable
  4AzSA crosslinking) [PMID:25628632 "Five of these eight, including glutathione peroxidase 2 (GPX2), GSR2, hydroxypyruvate reductase 2 (HPR2), UDP-glucose 4-epimerase 2 (UGE2), and RBC small subunit 1A (RBCS1A), bound 3AESA and crosslinked to 4AzSA in an SA-inhibitable manner, indicating that they are SABPs"].
  No effect of SA on HPR2 activity or physiological significance was reported.

## Curation decisions (summary)

- Core MF: hydroxypyruvate reductase [NAD(P)H] activity (GO:0016618), NADPH preferred
  (GO:0120509 also accepted). Glyoxylate reductase (NADPH) and HPPR activity kept as non-core.
- Core BP: oxidative photosynthetic carbon pathway (GO:0009854, part_of photorespiration).
- Core CC: cytosol. Cytoplasm rows modified to cytosol; mitochondrion HDA marked over-annotated.
- SA binding kept as non-core (in vitro only).
