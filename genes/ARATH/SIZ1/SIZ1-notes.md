# SIZ1 (Arabidopsis thaliana, Q680Q4, At5g60410) - curation notes

## Identity and family

- Sole Arabidopsis Siz/PIAS (SP-RING) SUMO E3; PANTHER PTHR10782:SF102 (E3 SUMO-PROTEIN LIGASE SIZ1).
  [PMID:19837819 "SIZ1 (for yeast SAP and MIZ1) encodes the sole ortholog of mammalian PIAS (for protein inhibitor of activated STAT) and yeast SIZ SUMO (for small ubiquitin-related modifier) E3 ligases in Arabidopsis"]
- Domains: SAP (11-45), PHD-type zinc finger (112-168, plant-specific), PINIT, SP-RING (346-429, Zn ligands C379/H381/C402/C405), SXS. (UniProt features; [PMID:19837819 "SIZ1 contains, in addition, a PHD (for plant homeodomain) typical of plant PIAS proteins."])
- PHD finger binds SCE1 (E2) and is needed for GTE3 sumoylation [PMID:18502747 "the PHD domain binds AtSCE1 and contributes to the SUMO ligase function, being partially and absolutely required for AtSCE1 and GTE3 sumoylation, respectively"].

## Biochemistry

- In vitro E3 activity; global sumoylation impaired in siz1 [PMID:15894620 "AtSIZ1 has SUMO E3 ligase activity in vitro, and immunoblot analysis revealed that the protein sumoylation profile is impaired in siz1 plants."]
- Heat-induced SUMO1/2 conjugation largely SIZ1-dependent and nuclear [PMID:17644626 "This increase involves SUMO1 and SUMO2 and is mainly driven by the SUMO protein ligase SIZ1, with most of the conjugates accumulating in the nucleus."]
- SUMO1/SUMO2 preference; splice variant SSV2 is plasma-membrane localized and sumoylates CNGC6 [PMID:38497423 "SSV2 mainly localized to the plasma membrane, whereas SIZ1, SSV1/SSV4, and SSV3 localized to the nucleus."]
- SP-RING needed for activity and nuclear localization [PMID:19837819 "Domain SP-RING is required for SUMO conjugation activity and nuclear localization of SIZ1."]

## Localization

- Nuclear foci / speckles [PMID:15894620 "AtSIZ1-GFP was localized to nuclear foci."]; [PMID:15894620 "AtSIZ1 compartmentalizes to nuclear speckles, as do PIAS proteins"].

## Substrates with mapped mechanism (basis for "does the work" judgements)

| Substrate | Process | Evidence |
|---|---|---|
| PHR1 (K261/K372) | Pi starvation | [PMID:15894620 "PHR1, a MYB transcriptional activator of AtIPS1 and AtRNS1, is an AtSIZ1 sumoylation target."] |
| ICE1 K393 | cold/freezing | [PMID:17416732 "A K393R substitution in ICE1 [ICE1(K393R)] blocked SIZ1-mediated sumoylation in vitro and in protoplasts"] |
| ABI5 K391 | ABA (negative) | [PMID:19276109 "SIZ1-dependent sumoylation of ABI5 attenuates ABA signaling"] |
| MYB30 K283 | ABA | [PMID:22814374 "A K283R substitution in MYB30 blocks its SUMO E3 ligase SIZ1-mediated sumoylation in Arabidopsis protoplasts"] |
| FLD | flowering (FLC) | [PMID:18069938 "SIZ1 facilitates sumoylation of FLD that can be suppressed by mutations in three predicted sumoylation motifs in FLD"] |
| NIA1/NIA2 | nitrate assimilation | [PMID:21772271 "The nitrate reductases, NIA1 and NIA2, are sumoylated by AtSIZ1, which dramatically increases their activity."] |
| GTE3, SCE1, self | - | [PMID:18502747 "self-sumoylation and AtSIZ1-mediated sumoylation of the E2 enzyme AtSCE1 and GTE3"] |
| NF-YC10 | heat | [PMID:36282496 "the SUMO ligase SIZ1 (SAP AND MIZ1 DOMAIN-CONTAINING LIGASE1) interacts with NF-YC10 and enhances its SUMOylation during HS"] |
| MAC components | immunity (positive, when overaccumulated) | [PMID:41986387 "SIZ1 SUMOylates and stabilizes MAC components, reinforcing MDNC formation and sustaining immune signaling."] |

## Phenotype-only / indirect roles

- SA hyperaccumulation, constitutive SAR, PAD4-dependent; JA arm unaffected [PMID:17163880 "Jasmonic acid (JA)-induced PDF1.2 expression and susceptibility to Botrytis cinerea were unaltered in siz1 plants."]
- Dwarfism, cell size/number reduction is SA-dependent [PMID:20007967 "Cell division and expansion defects caused by siz1 were also suppressed by the expression of nahG."] -> cell division and unidimensional cell growth marked over-annotated.
- Basal NOT acquired thermotolerance [PMID:17041025 "SIZ1 controls basal, but not acquired, thermotolerance"] -> heat acclimation MODIFY to response to heat.
- Drought [PMID:17905899 "Mutant plants of siz1-3 have significantly lower tolerance to drought stress."]
- Female gametophyte degeneration after FG7; pollen tube guidance defect is secondary; SIZ1 not expressed in pollen [PMID:22253727 "SIZ1 showed enhanced expression in female organs, but was not detected in the anther or pollen."]
- Shoot regeneration repressed [PMID:32611787 "the SUMO E3 ligase SIZ1 negatively regulates in vitro shoot regeneration in Arabidopsis"].
- Pi: wild-type internal Pi in siz1 [PMID:15894620 "even though intracellular Pi levels in siz1 plants were similar to wild type"] -> "detection of phosphate ion" is a sensor claim not supported; MODIFY to regulation of cellular response to phosphate starvation.

## Decisions summary

- protein binding: SCE1 row MODIFY -> GO:0044390 ubiquitin-like protein conjugating enzyme binding; GTE3/GTE5 rows REMOVE (substrate interactions; covered by SUMO transferase/sumoylation).
- innate immune response-activating signaling pathway -> MODIFY to GO:2000031 regulation of SA mediated signaling pathway (no negative-regulation term exists in GO; SIZ1 also has a positive context-dependent role per PMID:41986387).
- regulation of ABA signaling -> MODIFY to GO:0009788 negative regulation.
- No NEW annotations proposed: candidate processes (heat response via NF-YC10, immune condensates) are either covered by MODIFY replacements or rest on single recent studies.

## Deep research verification

OpenScientist report claims checked against cached primary papers listed above. Not verified (no cached text): HAT1 (PMID:42260756), AL6 (PMID:39562527), HLS1 (PMID:36890719), FLC stabilization (PMID:24218331), COP1/VPS29 regulation of SIZ1 (PMID:28979848, PMID:40286281), cadmium (PMID:35718335); these were not used for annotation decisions.
