# PIN2 (EIR1/AGR1/WAV6; At5g57090; UniProt Q9LU77) notes

Deep research: `just deep-research-falcon ARATH PIN2` failed (Edison API 429 rate limit, 2026-10-05); review based on cached publications and UniProt/GOA.

## Identity
- Auxin efflux carrier component 2, long PIN, 10 TM helices with central hydrophilic loop [PMID:9843496 "encodes a 69 kDa protein with 10 putative transmembrane domains interrupted by a central hydrophilic loop"].

## Molecular function
- Exports IAA: yeast expressing AGR1 shows increased IAA efflux [PMID:9844024 "AGR1 promotes an increased efflux of radiolabeled IAA from the cells"].
- PINs catalyse rate-limiting auxin efflux in heterologous systems [PMID:16601150 "PINs mediate auxin efflux from mammalian and yeast cells without needing additional plant-specific factors"].

## Localization / polarity
- Polar PM in root cortex and epidermis [PMID:9843496 "The AtPIN2 protein was localized in membranes of root cortical and epidermal cells in the meristematic and elongation zones revealing a polar localization."].
- Apical (shootward) in epidermis [PMID:33705718 "we thus replaced the apical PIN2 with a predominantly basally localized PIN1-GFP2"]; basal in young cortex (BFA-induced basal-to-apical transcytosis in cortex) [PMID:33705718 "following the rapid BFA-induced basal-to-apical transcytosis of PIN2 in these cells"].
- GOA has basal PM (cortex) only; added NEW apical plasma membrane (IDA PMID:33705718).
- Vacuolar degradation via retromer [PMID:19004783 "In vivo visualization of PIN2 vacuolar targeting revealed its differential degradation in response to environmental signals, such as gravity."].

## Process
- Root gravitropism: pin2 null agravitropic [PMID:9843496 "Roots of the Atpin2::En701 null-mutant were agravitropic and showed altered auxin sensitivity"]; eir1 ethylene-insensitive roots [PMID:9679062 "are agravitropic and have a reduced sensitivity to ethylene"].

## Regulators (interactions; GO:0005515 rows removed as uninformative)
- PID/WAG pull-down with PIN2 loop, MAB4/MEL1 interaction [PMID:33705718]; PP6 (FyPP1/3) [PMID:22715043]; SAV4 [PMID:35274300].

## Decisions
- IBA ER: MARK_AS_OVER_ANNOTATED (short-PIN property). ISM chloroplast: REMOVE.
- Expression responses (glucose, hypoxia), ethylene/auxin response: KEEP_AS_NON_CORE.
